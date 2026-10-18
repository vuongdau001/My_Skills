#!/usr/bin/env python3
"""
Audio & Subtitle Pipeline (v5) — per-cue TTS, per-part manifests.

- Each cue in content/script.json becomes ONE mp3 (edge-tts, free) → Vietsub is exactly in sync with voice.
- Cache key = sha1(voice + rate + tts text) → editing a line always regenerates its audio; unchanged lines are reused.
- Falls back to macOS `say -v Linh` if edge-tts is unreachable (e.g. sandbox without network).
- Durations measured with macOS built-in `afinfo` (no ffmpeg needed).
- Timing constants come from tools/timing.py (shared with lint_script.py).
- Outputs per part:  src/manifest-part{N}.json  and  out/<slug>-part{N}.srt  (slug from script.json)

Usage:  tools/.venv/bin/python3 tools/generate_audio.py --part 1 [--voice nam|nu] [--allow-fallback]
Exit code 3 = some cues fell back to the macOS voice (manifest/srt are still written).
"""

import argparse
import asyncio
import hashlib
import json
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
from timing import CUE_GAP, LEAD_IN, TAIL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = ROOT / "content" / "script.json"
AUDIO_DIR = ROOT / "public" / "audio" / "cues"
OUT_DIR = ROOT / "out"

VOICES = {"nam": "vi-VN-NamMinhNeural", "nu": "vi-VN-HoaiMyNeural"}



def get_duration_seconds(file_path: Path) -> float:
    if not file_path.exists() or file_path.stat().st_size < 1000:
        return 0.0
    try:
        res = subprocess.run(["/usr/bin/afinfo", str(file_path)], capture_output=True, text=True, check=True)
        m = re.search(r"estimated duration:\s*([0-9.]+)", res.stdout)
        return float(m.group(1)) if m else 0.0
    except Exception:
        return 0.0


def format_srt_time(seconds: float) -> str:
    ms = int(round((seconds - int(seconds)) * 1000))
    t = int(seconds)
    if ms == 1000:
        t, ms = t + 1, 0
    return f"{t // 3600:02d}:{(t % 3600) // 60:02d}:{t % 60:02d},{ms:03d}"


async def _edge_tts_once(text: str, voice: str, out_mp3: Path, rate: str) -> None:
    import edge_tts

    tmp = out_mp3.with_suffix(".tmp.mp3")
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    with open(tmp, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
    tmp.replace(out_mp3)


async def synthesize_edge_tts(text: str, voice: str, out_mp3: Path, rate: str) -> None:
    last: Exception | None = None
    for attempt in range(1, 4):
        try:
            await asyncio.wait_for(_edge_tts_once(text, voice, out_mp3, rate), timeout=20.0)
            return
        except Exception as exc:  # noqa: BLE001
            last = exc
            print(f"  [retry {attempt}/3] {out_mp3.name}: {exc}")
            await asyncio.sleep(1.0)
    raise RuntimeError(f"edge-tts failed: {last}")


def synthesize_macos_fallback(text: str, base: Path) -> Path:
    """Offline fallback. Keeps the real container extension (.m4a): saving AAC under a .mp3 name
    makes afinfo misread the duration (measured 0.07s for a 1.76s clip)."""
    aiff, m4a = base.with_suffix(".aiff"), base.with_suffix(".m4a")
    subprocess.run(["/usr/bin/say", "-v", "Linh", "-r", "185", "-o", str(aiff), text], check=True)
    subprocess.run(["/usr/bin/afconvert", "-f", "m4af", "-d", "aac", str(aiff), str(m4a)], check=True)
    aiff.unlink(missing_ok=True)
    return m4a


async def build_part(part: int, voice_key: str, allow_fallback: bool = False) -> int:
    script = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
    fps: int = script["fps"]
    rate: str = script.get("ttsRate", "+5%")
    slug: str = script.get("slug", "video")
    voice = VOICES[voice_key]
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    scenes = [s for s in script["scenes"] if s.get("part", 1) == part]
    if not scenes:
        raise SystemExit(f"No scenes for part {part}")

    providers: set[str] = set()
    beats_out: List[Dict[str, Any]] = []
    chapters: List[Dict[str, Any]] = []
    srt: List[str] = []
    frame = 0
    fallback_cues: List[str] = []  # cues voiced by macOS `say` instead of the neural voice

    for scene in scenes:
        chapters.append({"id": scene["id"], "title": scene["title"], "act": scene["act"], "startFrame": frame})
        for beat in scene["beats"]:
            mode = beat["mode"]
            beat_start = frame
            cursor = LEAD_IN.get(mode, 10)
            cues_out = []
            for ci, cue in enumerate(beat["cues"]):
                key = hashlib.sha1(f"{voice}|{rate}|{cue['tts']}".encode()).hexdigest()[:12]
                base = AUDIO_DIR / f"{beat['id']}_{ci}_{key}"
                cached = [p for p in (base.with_suffix(".mp3"), base.with_suffix(".m4a")) if get_duration_seconds(p) > 0.5]
                if cached:
                    audio = cached[0]
                    tag = "cached"
                    providers.add(("edge-tts" if audio.suffix == ".mp3" else "macOS say") + " [cached]")
                else:
                    try:
                        audio = base.with_suffix(".mp3")
                        await synthesize_edge_tts(cue["tts"], voice, audio, rate)
                        tag = "edge"
                        providers.add(f"edge-tts {voice} ({rate})")
                    except Exception as exc:  # noqa: BLE001
                        print(f"  [warn] edge-tts failed ({exc}); macOS Linh fallback")
                        audio = synthesize_macos_fallback(cue["tts"], base)
                        tag = "say"
                        providers.add("macOS say Linh (fallback — re-run with network for neural voice)")
                if audio.suffix == ".m4a":
                    fallback_cues.append(f"{beat['id']} cue{ci}")
                sec = get_duration_seconds(audio)
                if sec < 0.5:
                    raise SystemExit(f"Bogus audio duration {sec:.2f}s for {audio.name} — check the file/container.")
                dur = math.ceil(sec * fps)
                cues_out.append({
                    "sub": cue["sub"],
                    "hl": cue.get("hl", []),
                    "audioFile": f"audio/cues/{audio.name}",
                    "startFrame": cursor,
                    "durationInFrames": dur,
                })
                g0 = (beat_start + cursor) / fps
                srt.append(f"{len(srt) + 1}\n{format_srt_time(g0)} --> {format_srt_time(g0 + sec)}\n{cue['sub']}\n")
                print(f"  [{tag:6s}] {beat['id']:10s} cue{ci} {sec:5.2f}s  {cue['sub'][:50]}")
                cursor += dur + CUE_GAP
            beat_len = cursor - CUE_GAP + TAIL.get(mode, 16)
            beats_out.append({
                "id": beat["id"],
                "sceneId": scene["id"],
                "sceneTitle": scene["title"],
                "act": scene["act"],
                "mode": mode,
                "stage": beat.get("stage", []),
                "mapBar": beat.get("mapBar"),
                "startFrame": beat_start,
                "durationInFrames": beat_len,
                "cues": cues_out,
            })
            frame += beat_len

    manifest = {
        "title": script["title"],
        "slug": slug,
        "part": part,
        "totalParts": max(s.get("part", 1) for s in script["scenes"]),
        "voiceProvider": " + ".join(sorted(providers)),
        "fps": fps,
        "width": script["width"],
        "height": script["height"],
        "totalFrames": frame,
        "totalDurationSec": round(frame / fps, 2),
        "chapters": chapters,
        "beats": beats_out,
    }
    (ROOT / "src" / f"manifest-part{part}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / f"{slug}-part{part}.srt").write_text("\n".join(srt), encoding="utf-8")
    print(f"\n[DONE] Part {part}: {len(beats_out)} beats, {len(srt)} cues, {frame} frames = {frame / fps:.1f}s")
    print(f"[DONE] Voice: {manifest['voiceProvider']}")
    if fallback_cues:
        print(f"\n[WARN] {len(fallback_cues)} cue(s) use the macOS fallback voice (mixed voices in one video):")
        print("       " + ", ".join(fallback_cues))
        print("       Re-run this command when the network is stable (only these cues are regenerated),")
        print("       then re-render. Do NOT hand over until this list is empty.")
        if not allow_fallback:
            print("       Exit code 3 (pass --allow-fallback to accept mixed voices for a draft).")
            return 3
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, default=1)
    ap.add_argument("--voice", choices=list(VOICES), default="nam")
    ap.add_argument("--allow-fallback", action="store_true", help="exit 0 even if some cues use the macOS fallback voice (draft only)")
    a = ap.parse_args()
    sys.exit(asyncio.run(build_part(a.part, a.voice, a.allow_fallback)))
