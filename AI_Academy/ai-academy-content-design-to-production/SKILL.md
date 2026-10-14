---
name: ai-academy-content-design-to-production
description: Turn AI Academy lesson content that exists in design form (docs/learning-content/<track>/…, Content-and-Presentation, visual specs, assessment sidecars) into app-ready curriculum (curriculum/<track>/index.json, theory md, quiz json, static visuals), validate it, render it on a localhost-only DB, and screenshot-compare it against a reference track (default Testing) until it reads as well. Uses AGY gemini-4-argon-high (/goal for conversion, /teamwork-preview for visual polish). Use for any track; not for production sync/publish.
---

# AI Academy: content design → production-ready

## Inputs
- Repo checkout + branch (ai-academy-dev). Track id, design folder, reference track (default `testing`).
- Quality skill: `My_Skills/AI_Academy/ai-academy-quiz-quality` (incl. TERM-EN-01 `references/terminology-en-keywords.md`).
- Owner decisions: branch/commit/push rights, visuals format.

## Hard rules (do-not)
- DB: localhost only. Every DB/dev command goes through `scripts/guard.sh` (aborts if `DATABASE_URL` host ≠ localhost/127.0.0.1 or a `.env` exists). Existing worktree `.env.local` files usually point to **Neon** — never reuse them. Never print secrets.
- Never `content:sync`/`seed` against staging/prod. `seed` wipes the DB: only on the dedicated pilot DB.
- Keep `isPublished:false` in committed files; publish only in the local pilot DB via `scripts/local-sync.sh` (temp flip + restore).
- AGY never commits/pushes, never runs DB commands, ends with `READY_FOR_REVIEW` (never self-PASS). On argon error/429: retry same model; no silent Flash fallback.
- Push only the agreed feature branch, only after all gates pass.

## Steps
1. **Inspect gaps**: design artifacts vs app contract — `scripts/lib/curriculum.ts` (index.json schema), reference theory md conventions, quiz json `{questions:[…]}`, renderer `src/components/common/MarkdownRenderer.tsx` (see references/renderer-facts.md).
2. **Promote**: `git mv` the app-format bundle to `curriculum/<track>/`; keep docs as design history and repoint relative links (check 0 broken). Commit.
3. **Contract gates**: `npm run content:validate`, `npm run content:audit:quiz`, quiz-quality `validate-assessment-blueprint.mjs --blueprint … --quiz …`, `audit-quiz-bank.mjs --root . --track <t> --strict`. Check DB length limits (e.g. question row id `qq-<moduleId>-<questionId>` ≤ 50 chars → use short ids like `pvs-q01`). Commit fixes.
4. **Local DB**: `sudo -u postgres` create role + DB `ai_academy_<track>_pilot` on 127.0.0.1; write repo `.env.local` (gitignored, umask 077) with DATABASE_URL + NEXTAUTH_URL/SECRET; `npm ci`; `guard.sh npx drizzle-kit push --force`; `local-sync.sh seed` (creates fixture users, e.g. `cmc001` / `Password123!`).
5. **Dev server**: `guard.sh npx next dev -p 3100`. Content is cached in memory → **restart dev after every sync**.
6. **Baseline screenshots**: `node scripts/shot.mjs <outdir> -baseline` (login with retry, desktop 1440×900 + mobile 390×844, theory full page + quiz after "Đã đọc xong" → "start-practice"; writes stats json: chars, h2, tables, imgs, broken imgs, overflowX, raw md, console errors).
7. **AGY /goal (conversion)**: write a goal file from `references/goal-template.md`; run
   `agy --model gemini-4-argon-high --effort high --dangerously-skip-permissions --add-dir <quality-skill> --add-dir <pilot-dir> -p "/goal $(cat GOAL.md)" --output-format stream-json > agy-goal.log`
   (print mode works with slash commands; check `init.model` in log; long runs 30–60 min). Re-run gates yourself, commit.
8. **Resync + restart + screenshot v1**; score the checklist (references/visual-checklist.md) against the reference.
9. **AGY /teamwork-preview (polish)** with a brief listing concrete FAIL items + evidence PNG paths: same command with `/teamwork-preview`. Max 2 rounds; then report remaining items as NEEDS_OWNER.
10. **Final**: gates, final screenshots, report (per item status + evidence), push feature branch if approved.

## Outputs
Commits on the feature branch; `curriculum/<track>/…`, `public/curriculum/<track>/*.svg`; pilot dir with PROGRESS.md, logs, evidence PNGs, stats json, checklist, report.

## Resumability
Runs get cut (~50 min): keep a PROGRESS.md (DB, scripts, commits, current step), commit after each step, run agy with nohup and poll its log.
