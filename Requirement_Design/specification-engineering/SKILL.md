---
name: specification-engineering
description: Analyze software requirements against real project context, model domain and behavior before drafting specifications, and review specifications for ambiguity, missing decisions and verification gaps. Use for requirements analysis, feature specification and specification engineering.
---

# Specification Engineering

Turn a feature request into an evidence-backed model and a verifiable specification. Use the user's language and project terminology. This skill requires no server or external service.

## Non-negotiable rules

1. **Model before documenting.** Do not start with an SRS, user stories, UI screens, database tables or API implementation. First produce and walk through purpose, boundaries, domain concepts, rules, states and scenarios, then test them with counterexamples and verification. Analysis notes and provisional models are allowed during modeling. If asked for a document immediately, perform this modeling first and then deliver a draft with unresolved items visibly marked.
2. **Never invent missing requirements.** Do not silently choose policy, invent stakeholder agreement, fill unknown fields or turn industry conventions into confirmed requirements. Label suggestions as proposals. An assumption remains unconfirmed until the stakeholder explicitly confirms it.
3. Keep source-backed facts, confirmed decisions, proposals, assumptions, conflicts and open questions distinct. An earlier assistant's suggestion is not stakeholder confirmation. Existing implementation is evidence of current behavior, not automatically evidence of intended behavior.
4. Surface **OPEN DECISION** when alternatives change business meaning, scope, permissions, data retention, state transitions or acceptance criteria. Present options and implications; do not choose one without authority. Continue independent analysis while the decision is pending.
5. Never copy the worked example's entities, policies or states into another project as defaults. Never claim a draft is implementation-ready while blocking decisions remain unresolved.

## Workflow

Read [analysis-framework.md](references/analysis-framework.md) for the modeling method. Use available project documents, code and stakeholder statements as context; obey their access constraints. Record source locations and distinguish intended from observed behavior. Ask for missing context only when it materially affects analysis; if access is unavailable, state the limitation.

Analyze in this order, revisiting earlier models when later scenarios expose contradictions:

1. Problem / purpose and desired outcomes.
2. Stakeholders / actors and authority.
3. System boundary, exclusions and dependencies.
4. Domain model, identity, relationships and vocabulary.
5. Business rules / invariants.
6. State / lifecycle, events, guards and effects.
7. Behavior / scenarios.
8. Alternatives / failures and counterexamples.
9. Interfaces / data contracts.
10. Quality attributes / NFR.
11. Verification and traceability.
12. Open questions / assumptions and decisions.

Track questions and assumptions throughout, not only in step 12. Cover each dimension at an appropriate depth; mark genuinely irrelevant dimensions with a reason. The sequence is a reasoning workflow, not a requirement to fill twelve document sections.

For each dimension, show the model, its evidence status, what it reveals and what remains unknown. Prioritize decisions that block scope or observable behavior. Do not overwhelm the stakeholder with every minor detail at once.

Before synthesis, use [specification-checklist.md](references/specification-checklist.md) to find contradictions and verification gaps. If explaining the method or applying it to issue reporting, consult [worked-example.md](references/worked-example.md); it is an illustrative analysis, not an approved product specification.

## Deliverables

Scale to the request. For analysis, return the current model, important discoveries and prioritized open decisions. For a specification, synthesize the models into the requested format only after walking through them. Include:

- Scope and vocabulary; actors and permissions.
- Source-backed requirements with stable identifiers.
- Rules, state transitions, scenarios, contracts and quality targets, with evidence status.
- Acceptance criteria linked to confirmed requirements.
- Open decisions, assumptions, conflicts, blockers and limitations.

Use traceability: source or decision → requirement → rule/state/scenario → verification. Acceptance criteria for unconfirmed proposals must be labeled conditional. Do not invent performance numbers, SLAs, retention periods or security policies to make a requirement testable.

### Open decision record

```text
OD-01 — OPEN DECISION: <policy question>
Context/evidence: <known facts and source>
Unknown: <what is not defined>
Options: <alternatives and practical implications>
Affected: <models, requirements and acceptance criteria>
Decision owner: <known owner, or not yet identified>
Blocks: <dependent work; other analysis can continue>
Resolution: Pending
```

If recommending an option, label it a recommendation and preserve Pending until confirmed. Record confirmed decisions with who confirmed them and the source; update affected models and tests together.
