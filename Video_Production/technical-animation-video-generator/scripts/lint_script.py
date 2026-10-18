#!/usr/bin/env python3
"""
Lint content/script.json and estimate duration per part (same timing constants as the generator).

Checks:
  - cue `sub` length ≤ cueSubMaxChars (2 lines on 9:16)
  - every `hl` highlight is a substring of its `sub`
  - REAL beats contain no forbidden tech terms (stage + subs) and have no mapBar
  - TECH beats have a mapBar whose real/tech pair counts match (split on " · ")
  - stage labels ≤ stageLabelMaxWords alphabetic words (real/tech beats)
  - each part's estimated duration vs `targetSec` (if set in script.json)

Usage: tools/.venv/bin/python3 tools/lint_script.py content/script.json
Exit code 1 if any problem is found.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from timing import CUE_GAP, FPS, LEAD_IN, TAIL, chars_per_sec  # noqa: E402

p = Path(sys.argv[1] if len(sys.argv) > 1 else "content/script.json")
s = json.loads(p.read_text(encoding="utf-8"))
r = s["authoringRules"]
cps = chars_per_sec(s.get("ttsRate", "+0%"))
target = s.get("targetSec")

problems: list[str] = []
part_frames: dict[int, float] = defaultdict(float)

for sc in s["scenes"]:
    part = sc.get("part", 1)
    for b in sc["beats"]:
        mode = b["mode"]
        frames = LEAD_IN.get(mode, 10) + TAIL.get(mode, 16)
        for c in b["cues"]:
            if len(c["sub"]) > r["cueSubMaxChars"]:
                problems.append(f"{b['id']}: sub {len(c['sub'])} chars > {r['cueSubMaxChars']}: {c['sub']}")
            for h in c.get("hl", []):
                if h not in c["sub"]:
                    problems.append(f"{b['id']}: highlight not in sub: {h!r}")
            frames += len(c["tts"]) / cps * FPS + CUE_GAP
        frames -= CUE_GAP
        part_frames[part] += frames

        if mode == "real":
            text = " ".join([c["sub"] for c in b["cues"]] + b.get("stage", []))
            for t in r["realModeForbiddenTerms"]:
                if re.search(rf"\b{re.escape(t)}\b", text, re.I):
                    problems.append(f"{b['id']}: forbidden tech term in REAL beat: {t}")
            if b.get("mapBar"):
                problems.append(f"{b['id']}: REAL beat must not have mapBar")
        if mode == "tech":
            mb = b.get("mapBar")
            if not mb:
                problems.append(f"{b['id']}: TECH beat missing mapBar")
            elif len(mb["real"].split(" · ")) != len(mb["tech"].split(" · ")):
                problems.append(f"{b['id']}: mapBar pair count mismatch")
        if mode in ("real", "tech"):
            for lab in b.get("stage", []):
                words = [w for w in lab.split() if re.search(r"[^\W\d_]", w)]
                if len(words) > r["stageLabelMaxWords"]:
                    problems.append(f"{b['id']}: stage label > {r['stageLabelMaxWords']} words: {lab}")
        print(f"  part{part} {b['id']:12s} {mode:7s} cues={len(b['cues'])}  ~{frames / FPS:5.1f}s")

print(f"\nSpeech rate assumed: {cps:.1f} chars/s ({s.get('ttsRate', '+0%')})")
for part, fr in sorted(part_frames.items()):
    sec = fr / FPS
    flag = ""
    if target and sec > target:
        flag = f"  ⚠ over target {target}s"
        problems.append(f"part{part}: estimated {sec:.0f}s > targetSec {target}s")
    print(f"Part {part}: ~{sec:.0f}s{flag}")

if problems:
    print("\n" + "\n".join(problems))
    sys.exit(1)
print("No lint problems.")
