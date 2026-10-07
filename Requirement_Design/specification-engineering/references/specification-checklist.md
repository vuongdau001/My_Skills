# Specification checklist

Use this after modeling and again before specification handoff. Answer with evidence, gap or justified not-applicable; do not fill blanks by guessing.

| Dimension | Review questions |
| --- | --- |
| Purpose | Is the actual problem separated from the proposed feature? Are outcomes attributable to a stakeholder? |
| Actors | Are actors and affected stakeholders distinguished? Who has authority for each action? |
| Boundary | Are responsibilities, exclusions, dependencies and handoffs explicit and confirmed where needed? |
| Domain | Are terms unambiguous? Are identity, cardinality, ownership, temporal context and provenance understood? |
| Rules | Are invariants scoped and testable? Are exceptions and policy choices separated? |
| Lifecycle | Does every transition have an event, guard, actor and effect? Are repeated/invalid events covered? |
| Scenarios | Can actor goals be walked through the model without an unexplained step? |
| Failures | Are relevant retries, partial failures, concurrency and recovery behaviors defined or openly unresolved? |
| Contracts | Are exchanged information and validation semantics clear? Are unknown fields and error policies visible? |
| Quality | Are relevant attributes observable? Are targets sourced instead of invented? |
| Verification | Does every confirmed requirement have an observable check? Are negative cases and persistent effects included? |
| Decisions | Are assumptions, proposals, conflicts and open decisions distinct, owned where possible and prioritized? |

## Contradiction probes

- Can a scenario violate an invariant while following every documented step?
- Does a state diagram allow an action that the permission model forbids?
- Can retrying an action duplicate, lose or corrupt a business object?
- Can an external change make historical evidence misleading?
- Does a test depend on an unresolved policy?
- Has an assistant suggestion, example or current implementation been mislabeled as stakeholder intent?
- Has a specific example introduced unrequested entities, roles, targets or functionality?

## Handoff status

State either ready for the agreed scope, or draft with blockers. For each blocker, list affected requirements and the decision needed. Keep conditional acceptance criteria distinguishable from approved criteria. Structural validation of this skill package does not validate a project's requirements.
