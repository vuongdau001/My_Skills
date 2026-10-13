# Review gates and verdicts

Use the smallest set of milestones that covers the requested work, but never skip an upstream gate whose failure would invalidate later work.

## R0 — Intake and baseline

Record scope, files, question counts, current validation status, working-tree risks, and whether the task is Audit, Normalize, Author, or Gate.

Output: inventory and baseline. Do not edit content in Audit or Gate.

Process lessons in curriculum order using sequential-learning-review.md. Gates R1–R5 run per lesson; retain cross-lesson dependencies for the final track review. Track question IDs reviewed and pending so partial progress is not presented as whole-bank approval.

## R1 — Authority and outcomes

Confirm the source hierarchy, terminology, learner audience, prerequisites, and observable learning objectives.

Evidence: lesson learning promise and track glossary, distinguishing current content from proposed outcomes.

Block when material authority is absent, conflicting without a decision, or objectives are only topic labels.

## R2 — Theory correctness

Build the claim ledger. Check definitions, boundaries, causal claims, quotations, numbers, examples, absolutes, and freshness.

Evidence: section-by-section theory review, including each section's teaching purpose and contribution to outcomes.

Block dependent items for `CONTRADICTED` or `UNVERIFIABLE` material claims. Produce a separate theory-correction list; do not silently repair theory outside the authorized scope.

## R3 — Assessment blueprint

Map objectives to source anchors, skills, cognitive levels, question families, and misconception sets.

Evidence: taught-content → intended assessment purpose → item mapping, with justified recall and applied demands.

Block final item authoring when important objectives have no plan, quiz scope exceeds taught theory, or the bank is dominated by recall without justification.

## R4 — Item correctness

Blind-solve every item, verify the decision rule, compare all options, and review the explanation against the final wording.

Evidence: item cards comparing intended learning purpose with actual learner reasoning, suitability, and disposition. Correctness and disposition are separate judgments.

Block `AMBIGUOUS`, `CONDITIONALLY_CORRECT`, `INCORRECT`, and `UNSUPPORTED` items.

## R5 — Bank quality

Review coverage, duplicates, cognitive mix, answer distribution, cue resistance, explanation reuse, and random-delivery risk.

Evidence: lesson closure with missing, repeated, overrepresented, or untaught outcomes; final track review checks prerequisites and terminology across lessons.

Block systematic shortcuts, missing critical-objective coverage, or a pool containing filler items that are unsafe when sampled.

## R6 — Independent semantic review

A reviewer who did not author the candidate repeats source verification and blind solving. Record disagreements rather than averaging them away.

Hide the author's intended purpose as well as the key and explanation until the reviewer has recorded the reasoning actually needed to answer.

If independent review did not occur, verdict must say `PENDING INDEPENDENT REVIEW`; author self-review is not a release PASS.

## R7 — Release gate

- `PASS`: no semantic blocker; requested structural checks pass; independent review evidence exists.
- `CONDITIONAL PASS`: only explicitly bounded non-semantic issues remain, with owner and follow-up; use only when those issues cannot change the answer or learning claim.
- `BLOCK`: theory contradiction, unsupported claim, wrong or ambiguous key, untaught concept, critical coverage gap, systematic answer cue, or missing required independent review.

Report machine evidence separately from reviewer judgment.

## R8 — Learner validation

After release or pilot, inspect completion time, item difficulty, discrimination, distractor selection, retry patterns, learner feedback, and transfer performance.

Before R8, describe material as `content-ready, pilot-pending`; do not claim demonstrated learning effectiveness.

## Finding format

Each finding must identify:

- track, module, question or claim ID;
- milestone and severity (`BLOCKER`, `MAJOR`, `MINOR`);
- current content;
- evidence and source anchor;
- why it affects correctness or assessment validity;
- proposed correction;
- proof required to close the finding;
- potentially related items.
