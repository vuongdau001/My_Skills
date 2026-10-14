# AI Academy repository contract

Read the repository rather than assuming these facts remain unchanged. The following describes the current baseline that motivated this skill.

## Content layout

Typical tracks use:

```text
curriculum/<track>/
├── index.json
├── theory/*.md
├── quizzes/*.quiz.json
└── modules/<module-id>/{theory.md,quiz.json}   # newer colocated form
```

The track manifest is the authoritative mapping between modules and content paths. Do not infer module membership only from filenames.

## Canonical source and served content

For tracks imported from a book or another maintained source, identify the canonical authoring location and the import path before editing. Within the authorized scope, apply corrections to that source and regenerate the curriculum so a later import cannot restore removed content. If source edits are outside scope, report the mismatch instead of silently maintaining divergent copies.

Compare all affected theory and quiz files against the canonical source. Allow only explicit serving transformations, such as image URL rewriting and harmless whitespace normalization; do not silently strip editorial prose only in the runtime copy. Use existing import/verification tools where available. When assets change, check referenced files against the source and verify their served URLs.

For an authorized DB synchronization, locate the available `ai-academy-content-sync` skill in the target project's skill catalog and verify persisted runtime fields against the final curriculum. Do not assume the personal skill library has that sibling directory. If the sync skill is unavailable, report the missing capability instead of inventing a sync workflow. Source consistency checks do not authorize DB writes, deployment, or global catalog synchronization.

## Quiz contract

Current quiz objects contain `questions`; each question has:

- `id`;
- `question`;
- exactly four `options`;
- `correctIndex` from 0 to 3;
- `explanation`;
- `sourceRef` beginning with `theory/`;
- `reviewedAt` in `YYYY-MM-DD` format.

The content loader currently accepts 6–20 questions per module. The normal runtime samples six questions. Confirm current code before relying on either number.

Production synchronization does not necessarily persist authoring metadata beyond the runtime question fields. Keep learning-objective, cognitive-level, decision-rule, and misconception traceability in a review artifact or module assessment sidecar unless the product schema is deliberately expanded.

Recommended sidecar location:

```text
curriculum/<track>/assessment/<module-id>.assessment.json
```

Do not create sidecars merely to satisfy paperwork. Create or update them when the task includes authoring, normalization, or durable traceability.

## Existing checks

Run the checks relevant to changed content:

```bash
npm run content:validate
npm run typecheck:content
npm run content:audit:quiz
npm run test:unit -- tests/unit/quiz-explanation.spec.ts tests/unit/quiz-rewrite.spec.ts
```

Inspect the current scripts and tests before relying on track-specific assertions. A pass proves only the invariants implemented by those checks.

## Evidence boundaries

- `content:validate` proves schema and selected formatting/provenance rules, not factual correctness.
- `content:audit:quiz` detects structural patterns and cues; it cannot establish a unique defensible answer.
- Unit tests may encode obsolete editorial preferences. Do not weaken tests merely to make new content pass; update them when the intended quality rule has genuinely changed and preserve unrelated protections.
- A six-question UI or API sample cannot demonstrate whole-bank quality.

## Mutation and release boundaries

- Preserve unrelated dirty-worktree changes.
- Audit and Gate do not edit curriculum.
- Normalize and Author edit only the confirmed modules/files.
- Do not run content sync, deploy, push, or modify production data unless separately requested.
