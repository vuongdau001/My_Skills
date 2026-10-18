"""
Shared timing constants for generate_audio.py and lint_script.py.
Keep them in ONE place so the linter's duration estimate matches the real build.
"""

FPS = 30

# Frames before the first cue of a beat (stage animates in) and after the last cue (settle).
LEAD_IN = {"real": 10, "tech": 16, "bridge": 8, "outro": 8, "summary": 10}
TAIL = {"real": 16, "tech": 18, "bridge": 10, "outro": 45, "summary": 18}
CUE_GAP = 7  # frames of silence between cues inside a beat

# Measured on edge-tts vi-VN-NamMinhNeural at rate "+12%": 1934 tts chars → 145.5 s audio.
# Note: spelled acronyms ("H T T P") slow speech down, so this is chars of the `tts` field.
MEASURED_CPS = 13.3
MEASURED_RATE_PCT = 12


def chars_per_sec(rate: str) -> float:
    """Scale the measured speed to another edge-tts rate string like '+5%' or '-10%'."""
    pct = int(str(rate).strip().rstrip("%") or 0)
    return MEASURED_CPS * (100 + pct) / (100 + MEASURED_RATE_PCT)
