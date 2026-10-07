# Analysis framework

## Evidence discipline

Use statuses: CONFIRMED (explicit requirement or decision), OBSERVED (existing system behavior), PROPOSED (candidate design/rule), ASSUMED (temporary premise), OPEN (unknown), CONFLICT (incompatible sources). Attach a source or rationale. An assumption is not permission to implement a business policy. Resolve conflicting evidence with its owner; do not pick whichever is easier to document.

## 1. Problem / purpose

Separate the requested solution from the problem. Identify whose work is impaired, in what situation and what outcome would improve. Ask how success could be observed. Do not invent numeric outcomes. Artifact: concise problem and outcome statements with evidence status.

## 2. Stakeholder / actor

Distinguish stakeholders affected by outcomes from actors interacting with the system. Model who may initiate, inspect, classify, modify and authorize each action. Do not assume all administrators have every permission. Artifact: actor/action/authority map, with unknown permissions marked.

## 3. Boundary

Define the responsibility under analysis, external systems, dependencies and explicit exclusions. Distinguish tracking a fix from performing a fix. Identify who owns each handoff. Artifact: context diagram or responsibility table. Unconfirmed exclusions remain proposals.

## 4. Domain model

Define concepts by business meaning before persistence or UI. Separate observations from managed problems when the domain warrants it. Explore identity, cardinality, ownership, time, provenance, versioning and deletion. Test ambiguous vocabulary with concrete examples. Artifact: glossary and conceptual relationship model. A conceptual relation is not a database schema commitment.

## 5. Rules / invariants

Express each candidate rule with scope, predicate, actor and exceptions. Distinguish what must always hold from a policy selecting among valid behaviors. Check whether rules survive retries, grouping, editing and concurrent actions. Artifact: rule table with status, evidence and counterexample.

## 6. State / lifecycle

Model states by business meaning and events by actors and triggers. For each transition record from-state, event, authorized actor, guard, effects and resulting state. Analyze initial, terminal, rejected and repeated events. Unknown transitions stay OPEN; proposed state names do not become requirements. Artifact: transition table or state diagram with a clear legend.

## 7. Behavior / scenarios

Walk through real actor goals against the models. Record preconditions, trigger, steps, observable result and postconditions. Check that each step has a rule and each state change has a transition. Artifact: main scenarios, with uncovered model gaps.

## 8. Alternatives / failures

Challenge the main flow: invalid or incomplete context, unauthorized access, stale versions, retries, timeouts, partial completion, concurrent edits, unavailable dependencies and recovery. Choose cases relevant to the project; do not expand scope automatically. Ask what the actor sees and what persists after failure. Artifact: counterexamples and proposed or confirmed recovery behavior.

## 9. Interfaces / data contracts

Model information crossing boundaries: producer, consumer, meaning, identity, required/optional fields, validation, version context, errors and retry semantics. Establish semantic contracts before endpoint syntax. Do not invent payload fields or retention obligations. Artifact: conceptual contract with unresolved field/policy decisions.

## 10. Quality attributes / NFR

Identify relevant reliability, usability, accessibility, privacy, security, performance, auditability and maintainability needs. Express an observable condition, measurement method and stakeholder-approved target. If a target is unknown, mark it OPEN. A plausible number is not evidence. Artifact: quality scenario table, not a list of vague adjectives.

## 11. Verification

Derive checks from confirmed behavior: Given context/state, When event, Then observable result and persistent effects. Include forbidden transitions and invariant violations as well as success. Trace checks to sources and requirement IDs. Proposed policies may have conditional checks, never unconditional acceptance gates. Artifact: verification matrix and coverage gaps.

## 12. Open questions / assumptions

Consolidate the running register. Rank by impact on scope, business meaning and implementability. Record owner when known, alternatives, affected models and what is blocked. Separate missing facts (questions), temporary premises (assumptions), policy choices (decisions) and source conflicts.

## Synthesis gate

Before drafting a specification, walk representative scenarios and counterexamples through the domain/rule/state models and map verification to confirmed requirements. Revise inconsistencies. If blockers remain, deliver an explicitly incomplete draft with those blockers; do not fabricate closure. A complete-looking template is not proof of a complete specification.
