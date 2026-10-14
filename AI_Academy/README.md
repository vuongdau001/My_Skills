# AI Academy — shared skills

## Canonical skill

[ai-academy-quiz-quality](ai-academy-quiz-quality/SKILL.md) supports source-backed theory, quiz authoring/review, source → claim → core → objective → question traceability, and presentation design. The BA/PO profile uses 15 recall/understand questions per lesson. Visual specifications stay in Markdown; visual/UI production is a separate step.

This repository is the canonical editable source. Commit and push changes here so other machines can pull the same version.

## Use across local tools

Install the complete `ai-academy-quiz-quality` folder (including references, scripts and agents). On a machine with this repository checked out, link these tool directories to `AI_Academy/ai-academy-quiz-quality`:

| Tool | Skill location |
| --- | --- |
| Codex | `~/.codex/skills/ai-academy-quiz-quality` |
| Gemini / Antigravity | `~/.gemini/config/skills/ai-academy-quiz-quality` |
| Claude | `~/.claude/skills/ai-academy-quiz-quality` |

A symbolic link keeps the tools on the same files when this checkout changes. Configure the path for each machine. If a tool cannot discover linked skills, copy the complete folder and verify file hashes after updating. Start a new session or refresh skill discovery after installation if needed.

The AI Academy project also carries a portable snapshot in `.agents/skills/ai-academy-quiz-quality` on `feature/ba-po-content-design` in `ai-academy-dev`. Project snapshots must be refreshed from this canonical folder when the skill changes.

For AI Academy BA/PO content, use this skill and its BA/PO profile. A separate generic learning-content skill is not a replacement for that profile.
