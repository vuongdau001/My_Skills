#!/usr/bin/env python3
"""
Print QA frames (global frame numbers) for every beat of a part, so each beat can be checked
with `remotion still`. For each cue we sample the point at `--frac` (default 0.85) of the cue,
i.e. after that cue's animation has played out.

Usage:
  tools/.venv/bin/python3 tools/qa_frames.py --part 1                 # table
  tools/.venv/bin/python3 tools/qa_frames.py --part 1 --beat s3_tech  # one beat
  tools/.venv/bin/python3 tools/qa_frames.py --part 1 --csv           # "beatId_cueN frame" lines
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("--part", type=int, default=1)
ap.add_argument("--beat", default=None)
ap.add_argument("--frac", type=float, default=0.85)
ap.add_argument("--csv", action="store_true")
a = ap.parse_args()

m = json.loads((ROOT / "src" / f"manifest-part{a.part}.json").read_text(encoding="utf-8"))
for b in m["beats"]:
    if a.beat and b["id"] != a.beat:
        continue
    for i, c in enumerate(b["cues"]):
        g = b["startFrame"] + c["startFrame"] + int(c["durationInFrames"] * a.frac)
        if a.csv:
            print(f"{b['id']}_cue{i} {g}")
        else:
            print(f"{b['id']:11s} {b['mode']:7s} cue{i}  frame={g:5d}  {c['sub'][:48]}")
