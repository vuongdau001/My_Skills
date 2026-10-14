---
name: ai-academy-quiz-quality
description: Audit, normalize, or author AI Academy theory and knowledge-check quizzes with source-backed factual review, measurable learning objectives, misconception-driven distractors, defensible answer keys, and staged release gates. Use for curriculum content quality, quiz rewrites, answer/explanation review, or assessment readiness; do not use for interactive labs or production sync.
---

# AI Academy Content & Quiz Quality

Produce learning content that is technically defensible and assessments that measure the intended capability rather than memory of prose or case-study trivia.

## Choose the operating mode

- **Audit:** inspect theory, quiz, answer keys, explanations, and coverage. Do not edit curriculum. Return evidence-backed findings and a verdict.
- **Normalize:** repair existing theory or quiz content only when the user explicitly asks for edits. Preserve stable IDs when the assessed capability is unchanged.
- **Author:** create new theory or quiz content from approved outcomes and sources. Do not begin final quiz prose before the assessment blueprint is coherent.
- **Gate:** independently verify a proposed release. Do not treat the author's self-review, `reviewedAt`, or a passing structural validator as semantic approval.

If the request is ambiguous, default to **Audit**. Audit and Gate may write a requested report, but must not mutate curriculum content.

## Route to the required references

Read only the references needed for the current mode:

- For creating or reviewing theory, including learner-facing editorial cleanup, read [references/learning-content-method.md](references/learning-content-method.md).
- For learner-facing layout, diagrams, visual design/production boundaries, and rendered review (LAYOUT-01), read [references/content-layout-and-visuals.md](references/content-layout-and-visuals.md).
- For the BA/PO course's theory + level-1 quiz contract, also read [references/ba-po-content-profile.md](references/ba-po-content-profile.md). Apply this profile only to that course or when the user explicitly adopts it; it does not impose recall-only assessment on other tracks.
- For writing or reviewing quiz items, read [references/quiz-authoring-and-review.md](references/quiz-authoring-and-review.md).
- For source selection and factual disputes, read [references/authority-registry.md](references/authority-registry.md).
- For review milestones, verdicts, and report structure, read [references/review-gates.md](references/review-gates.md).
- For AI Academy paths, schemas, source-to-runtime consistency, commands, and runtime constraints, read [references/repo-contract.md](references/repo-contract.md).
- For English-keyword terminology (rule TERM-EN-01) and the shared VI → EN glossary, read [references/terminology-en-keywords.md](references/terminology-en-keywords.md).
- For reusable claim, blueprint, item-card, and finding formats, read [references/templates.md](references/templates.md).
- For lesson-by-lesson review and question intent analysis, read [references/sequential-learning-review.md](references/sequential-learning-review.md). Required for all content review and authoring modes.

## Core workflow

1. **Ground in the repository.** Inspect the track manifest, theory, quiz files, relevant validators, and current working-tree state. Preserve unrelated changes.
2. **Establish authority.** Identify the track's canonical or official baseline and assessment scope. Design competency-first and source-first; use story-first presentation. Trace source concept -> taught claim -> core content -> objective -> item, distinguishing source doctrine from editorial application.
3. **Review theory first.** Build a claim ledger for definitions, rules, causal claims, recommendations, numbers, quotes, and absolutes. A contradicted or unsupported theory claim blocks dependent quiz items.
4. **Lock observable outcomes.** Express what the learner must distinguish, calculate, diagnose, review, produce, or decide. “Know” and “understand” alone are insufficient.
5. **Create or verify the assessment blueprint.** Map outcome -> source anchor -> observable skill -> cognitive level -> question family -> misconception set.
6. **Review each item.** Blind-solve before reading `correctIndex`; state the decision rule; compare all options on the same semantic dimension; verify that exactly one answer is best under the supplied facts.
7. **Review the bank and delivery behavior.** Check objective coverage, repeated templates, answer-position and length cues, duplicate ideas, explanation reuse, and the quality of random six-question attempts.
8. **Apply the staged gates.** Separate structural automation from semantic judgment. Report `PASS`, `CONDITIONAL PASS`, or `BLOCK` with explicit evidence and unresolved risks.

Run steps 2–7 as a complete cycle for each lesson in curriculum order. Review every theory section and then every quiz item in source order before moving to the next lesson. Record cross-lesson dependencies and revisit affected lessons at the final track review. An upstream blocker does not prevent inventorying downstream items, but their dependent claims cannot pass. For a user-scoped subset, follow its curriculum order and report prerequisite gaps.

## Non-negotiable constraints

- Do not use the current theory as proof of its own correctness when external authority is required.
- Do not put untaught concepts into a quiz; correct or expand theory first, or remove the item.
- Case studies must contain decision-relevant facts. Names and story detail that do not affect reasoning are decoration.
- A worked example must show reasoning and a bounded conclusion, not merely a blank template or list of open questions. Match learner activity to the agreed assessment scope; do not add artifact submissions, interactive labs, or fixed section quotas by adopting an external framework.
- Every distractor must represent a distinct plausible misconception in the same decision space as the key.
- Explanations must state the governing rule, apply the supplied facts, and reject the closest alternatives. They may not rescue an ambiguous stem.
- Distinguish author intent from what the learner actually has to do to answer. Every item needs one primary assessment purpose, taught support, and an explicit suitability decision; teaching or reminding through feedback is secondary.
- Automated checks can prove structure and detect cues; they cannot certify domain correctness, pedagogical validity, or a unique best answer.
- The author may prepare a candidate but may not self-certify semantic release readiness. Gate mode requires an independent blind review or an explicit `PENDING INDEPENDENT REVIEW` verdict.
- Never sync production, deploy, or change runtime behavior unless the user separately requests it.

## Deterministic helpers

Run from the repository root:

```bash
node .agents/skills/ai-academy-quiz-quality/scripts/audit-quiz-bank.mjs --root . --track testing
node .agents/skills/ai-academy-quiz-quality/scripts/validate-assessment-blueprint.mjs --blueprint path/to/module.assessment.json --quiz path/to/module.quiz.json
node .agents/skills/ai-academy-quiz-quality/scripts/analyze-quiz-samples.mjs --blueprint path/to/module.assessment.json --sample-size 6
```

Helpers print findings and do not edit curriculum. Treat heuristic findings as review leads, not automatic semantic failures.

## Completion rule

Do not claim completion merely because files validate. A content task is complete only when its requested review milestone is satisfied, all blockers are resolved or explicitly accepted by the user, and the final report distinguishes machine evidence, reviewer judgment, assumptions, and remaining validation work.
