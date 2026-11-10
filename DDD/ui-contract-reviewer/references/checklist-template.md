# Screen Contract Checklist Template

## 1. Review Baseline

| Attribute | Value |
|:--|:--|
| Screen ID | SCR-xxx |
| Canonical mockup | path + version |
| Mockup SHA-256 | hash |
| Superseded alternatives | paths + reason |
| BA baseline | decision/review date + link |
| Domain sources | glossary, aggregate, flow, Business Rules |
| Query/Command | exact names |
| Backlog consumers | task/story IDs |
| Implementation evidence | branch/commit/components |
| QA evidence | requirement snapshot + test cases |
| Sign-off | BA/PO + UI/UX + date |

If the canonical mockup or BA baseline changes, mark this checklist `STALE` and review it again.

## 2. Field and Column Correctness

| ID | Region | Mockup label | Control/format | Business meaning | Domain term | Data source/Command input | Required/default | Visible/editable rule | Validation/BR | Verdict | Evidence/reason | Consumer task | QA TC |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| F-01 | General Info | Contract | Select | Contract billed by milestone | ContractRef | ContractListQuery / CreatePaymentMilestone | Required/no default | Account Manager; editable on Create only | BR-xx | CONFIRMED | links | TK-xxx | TC-xxx |

Record every form field, read-only value, hidden submitted value, table column, filter, summary, unit, and currency.

## 3. Actions and Navigation

| ID | Element/label | Actor + state | Command/navigation | Confirmation | Success result | Error/empty/loading result | Verdict | Evidence | Consumer task | QA TC |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|

## 4. Structure and Visual Contract

| ID | Region/component | Required content | Order/layout constraint | Canonical viewport | Tolerance/dynamic mask | Verdict | Consumer task | QA evidence |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|

Do not require pixel equality for timestamps or dynamic values. Define masks and tolerance explicitly.

## 5. Generated Task Acceptance Criteria

```markdown
### UI Contract AC — TK-xxx / SCR-xxx

- AC-UI-STRUCT-01: [named regions/components and required order].
- AC-UI-FIELD-01: [field label/control/source/required/editable/default/format].
- AC-UI-STATE-01: Given [actor/status], [element] is [visible/enabled/editable].
- AC-UI-ACTION-01: When [action], [confirmation/success/error/loading result].
- AC-UI-VISUAL-01: At [viewport], [layout constraint] matches the canonical baseline within [tolerance], masking [dynamic regions].
```

## 6. Coverage Summary

| Metric | Result | Gate |
|:--|:--|:--|
| Inventory rows with verdict | X/X | Must be 100% |
| Confirmed rows mapped to AC | X/X | Must be 100% |
| Confirmed rows mapped to QA | X/X | Must be 100% |
| Unresolved P0/P1 clarification | X | Must be 0 |
| Mockup-stale rows unresolved | X | Must be 0 |
| BA/PO sign-off | status | Required |
| UI/UX sign-off | status | Required |

## 7. Delta Summary

| Delta | Rows | Required change | Owner | Status |
|:--|:--|:--|:--|:--|
| Mockup | IDs | update/annotate | UI/UX | todo |
| Backlog | IDs | add AC/task | BA/PM | todo |
| Code | IDs | implementation delta | Dev | todo |
| QA | IDs | add test/golden baseline | QA | todo |
