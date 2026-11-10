---
name: ui-contract-reviewer
description: Validate whether fields, columns, actions, states, and layout regions shown in a mockup are correct against the latest BA decisions and DDD/read-model contracts, then generate a signed Screen Contract Checklist and detailed UI Acceptance Criteria for implementation and QA tasks. Use after ui-ddd-mapping when preparing work, reviewing mockup-vs-code gaps, or preventing vague "match the mockup" acceptance criteria.
version: 1.0
---

# UI Contract Reviewer

Validate the mockup as a candidate consumer contract. Do not assume the mockup is correct. Produce field-level decisions and testable Acceptance Criteria (AC) before development or rework.

## Boundary with Other Skills

- `ui-ddd-mapping`: map Screen ↔ Command/Query and detect missing domain/read-side artifacts.
- `ui-contract-reviewer`: validate the correctness and presentation contract of every field/action/state on an already mapped screen.
- `ddd-backlog-planner`: consume confirmed checklist rows and generated AC to create/update executable tasks.

Do not duplicate Screen↔Command/Query mapping here. If mapping is missing, stop and route to `ui-ddd-mapping` first.

## Required Inputs

1. Screen Registry entry and chosen mockup candidate(s).
2. Latest BA/PO decisions and clarification baseline.
3. Glossary, Business Rules, aggregate, flow, and Query/Read Model for the screen.
4. Existing backlog task/story, when present.
5. Implementation and QA evidence when reviewing delivered code.

Read [checklist-template.md](references/checklist-template.md) before producing the output.

## Source Priority

Resolve conflicts in this order:

1. Latest approved BA/PO decision.
2. Validated domain model: Glossary, Business Rule, Aggregate, Flow, Query/Read Model.
3. Canonical mockup version approved for the release.
4. Backlog AC.
5. Code and QA tests as evidence only.

Never use current code or an existing QA selector to prove that a mockup field is correct.

## Workflow

### 1. Freeze the Review Baseline

- Select one canonical mockup version per Screen ID.
- Record file path, version, SHA-256, BA baseline date, and source links.
- Mark temporary, superseded, or alternative mockups explicitly.
- If no canonical version can be selected, return `CLARIFICATION_NEEDED` and block field review.

### 2. Extract the Complete UI Inventory

Inventory every visible or submitted element:

- Form fields, read-only values, hidden submitted values, defaults, and formats.
- Table columns, filters, summaries, pagination, sorting, and empty states.
- Buttons, row actions, bulk actions, navigation, confirmations, and exports.
- Regions, tabs, panels, modals/drawers, loading/error/success states.
- Actor/status/feature-flag visibility and editability rules.

Do not summarize a complex table as one row. Record each column and action separately.

### 3. Validate Business Correctness

For each inventory item, answer all questions:

- What business meaning does it have?
- Which Ubiquitous Language term does it use?
- Where does its value come from or go to?
- Is it required, optional, derived, or display-only?
- What is its default, format, unit, and currency?
- Who can see or edit it, and in which aggregate state?
- Which validation or Business Rule applies?
- Is it still valid under the latest BA baseline?

Missing answers are gaps, not assumptions.

### 4. Assign One Verdict

| Verdict | Meaning | Required action |
|:--|:--|:--|
| `CONFIRMED` | Mockup item is correct and current | Generate AC and QA coverage |
| `MOCKUP_STALE` | Later BA/domain decision supersedes it | Correct/annotate mockup |
| `BACKLOG_GAP` | Correct mockup item is absent or vague in backlog | Add/update story/task AC |
| `CODE_DEFECT` | Approved contract is not implemented | Add implementation delta |
| `QA_GAP` | Approved contract lacks verification | Add structural/behavioral/visual test |
| `CLARIFICATION_NEEDED` | Correct behavior cannot be determined | Record question; block affected P0/P1 task |
| `NOT_APPLICABLE` | Element is intentionally excluded | Record reason and authority |

Do not mark a row `CONFIRMED` without source evidence.

### 5. Generate the Screen Contract Checklist

Create `mapping/ui-contract-checklist-{bc}.md` using the reference template. The checklist is a release snapshot, not a new source of business truth.

Completeness gate:

- 100% fields, columns, actions, and states have verdicts.
- No unresolved P0/P1 `CLARIFICATION_NEEDED` rows.
- Every `MOCKUP_STALE` row is corrected or explicitly superseded.
- BA/PO signs off business correctness.
- UI/UX signs off structure/presentation.

### 6. Generate Detailed AC for Every Consumer Task

Map each `CONFIRMED` checklist row to a task and generate explicit AC:

- `AC-UI-STRUCT`: required regions/components and order.
- `AC-UI-FIELD`: label, control, source, required/default/read-only/format.
- `AC-UI-STATE`: visibility/enabled/editability by actor and domain state.
- `AC-UI-ACTION`: action, confirmation, success/error/empty/loading behavior.
- `AC-UI-VISUAL`: canonical viewport, layout constraint, tolerance, and dynamic masks.

Reject vague AC such as “match mockup,” “follow design,” or “UI looks correct.” Name the element and expected result.

### 7. Generate the QA Handoff

For each generated AC, record one verification path:

- Structural DOM/component assertion.
- Behavioral end-to-end assertion.
- Visual regression comparison.
- Manual check only when automation is not feasible, with reason.

Every confirmed checklist row must map to at least one AC and one QA check. No orphan rows.

## Stop Conditions

Stop affected downstream work when:

- Canonical mockup is ambiguous.
- A required field has no domain term or data source/destination.
- Actor/state editability conflicts with a Business Rule.
- A P0/P1 field/action remains `CLARIFICATION_NEEDED`.
- Generated AC cannot be tested deterministically.

Report the exact rows and required decision; do not improvise a design.

## Completion Report

Report:

- Screens reviewed and canonical hashes.
- Counts by verdict.
- Blocking clarification rows.
- Backlog/code/QA deltas created.
- Consumer tasks receiving generated AC.
- Sign-off status and whether implementation is unlocked.
