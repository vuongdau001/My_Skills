# Worked example: internal e-learning issue reporting

This example is based on the referenced discussion “Đánh giá kỹ năng đặc tả”. Only the user's initial request is confirmed. The assistant's domain model, boundary, rules and states are proposals. This example demonstrates how analysis discovers questions; it is not an approved specification and must not be copied into other projects as policy.

## Confirmed starting request

An internal e-learning system supports theory study and quizzes. Users need to report incorrect content or technical failures in both areas. Administrators classify, consolidate and resolve bugs.

## 1. Purpose — uncover two outcomes

PROPOSED interpretation: learners need to report a problem with enough context for someone to act; administrators need to turn multiple observations into trackable problems. Whether the current system lacks every reporting channel is unknown. Discovery: a report button alone does not define successful handling.

## 2. Actors — expose authority gaps

CONFIRMED: users and administrators are involved. OPEN: who may view reports, change classifications, consolidate problems or declare resolution? Are content editors or developers separate actors? Do not add roles as confirmed requirements.

## 3. Boundary — unpack “resolve”

PROPOSED boundary: reporting tracks discovery, classification, consolidation and closure; actual lesson editing, quiz editing, source-code changes and deployment happen elsewhere.

OD-01 — OPEN DECISION: Does resolve mean recording completion, performing the fix, or both? Options change scope and handoffs. Owner: stakeholder, specific person not identified. Blocks: final module boundary.

## 4. Domain — reports are not necessarily issues

Three learners report the same incorrect answer in a networking quiz. These are three observations, possibly one underlying problem.

PROPOSED concepts:

```text
Learner → Report → Context (theory location or quiz question)
                   |
Several Reports → Issue managed by Admin
```

A Report represents an observation; an Issue represents a managed problem. Candidate relationship: multiple reports may support one issue. OPEN: can a report describe multiple problems, remain unassigned, or later move to another issue? The N:1 model needs confirmation rather than a database table immediately.

Context candidates: course, lesson/content location and version for theory; quiz, stable question identity and version for quiz. Display position “Question 12” alone may be unstable.

OD-02 — OPEN DECISION: Store a live reference, historical version reference, snapshot, or combination? A later content edit can make a live reference show different material than the learner saw. Snapshot availability, privacy, storage and retention implications need discussion.

## 5. Rules — preservation is a candidate invariant

PROPOSED candidates, each requiring confirmation:

- A report identifies its submission context.
- Consolidation preserves original reports and their provenance.
- A report links to at most one active issue, unless multi-problem reporting is supported.
- Resolving an issue does not itself erase its original reports.

Discovery: consolidation may mean linking observations to one issue rather than deleting or merging report text. OPEN: retention and correction policies; do not infer indefinite storage.

## 6. Lifecycle — test closure semantics

Illustrative proposed issue states: NEW → TRIAGED → IN_PROGRESS → RESOLVED. These state names and transitions are not specified by the user. Record authorized actors, guards and effects only after clarification. Reports may have their own handling status; do not assume reports and issues share a lifecycle.

OD-03 — OPEN DECISION: A new report matches an already RESOLVED issue.

- Reopen the existing issue: preserves continuity but may change closure meaning.
- Create a new issue: separates recurrence but needs a relationship to history.
- Link without reopening: preserves state but may hide actionable recurrence unless another process handles it.

No option is intrinsically correct. Resolution is Pending. Blocks: recurrence transition and acceptance criteria.

## 7. Scenarios — walk the main flow

Illustrative flow: learner reports a suspected wrong answer → system acknowledges submission → admin reviews context → classifies → associates with a managed issue → later records resolution.

Discoveries: required report information, acknowledgement meaning, matching authority and evidence needed for resolution are unknown. A technical failure may prevent submission itself; an alternative reporting channel is a question, not an automatic requirement.

## 8. Alternatives / failures — challenge the model

Counterexamples: the question is edited before triage; two admins consolidate concurrently; a timeout causes the learner to retry; one report describes two distinct problems; an admin selects the wrong issue; a new report arrives after closure.

These reveal decisions about historical context, concurrency, duplicate submission, reassignment and recurrence. Do not assume automatic deduplication, undo, notifications or reopening.

## 9. Contracts — identify semantic information

PROPOSED submission information: reporter identity if appropriate, theory/quiz context, observation and evidence. OPEN: anonymous reporting, attachments, sensitive quiz answers, field requirements and error semantics. Acknowledge whether receipt means persisted submission or merely accepted processing. Avoid choosing endpoint names before the behavior is agreed.

## 10. Quality — leave numbers open

Candidate concerns: reporting should avoid disrupting learning; learners should not see another person's private reports; quiz context should not expose restricted answer keys; admins may need action history. Targets, visibility, retention and audit requirements remain OPEN. Do not invent response-time targets or retention periods.

## 11. Verification — conditional until confirmed

Confirmed intent can support a broad scope check: reporting is available for both theory and quiz, and admin handling supports classification, consolidation and resolution. Precise acceptance tests still depend on decisions.

Conditional on approval of evidence-preserving consolidation: Given three saved reports, When admin associates them with one issue, Then each report remains individually traceable.

Conditional on a chosen context policy: Given content changes after submission, When admin examines the report, Then the displayed context follows that policy.

OD-03 remains open, so there is no unconditional test asserting automatic reopening.

## 12. Synthesis — keep readiness honest

Current result: a useful provisional model, not an implementation-ready specification. Prioritize boundary/resolve semantics, report–issue relationships, historical context, permission rules and recurrence policy. Each confirmed decision should update its model, requirement and verification together.

The reusable lesson: each modeling technique reveals a different gap. Documentation records the resulting understanding; it cannot substitute for those decisions.
