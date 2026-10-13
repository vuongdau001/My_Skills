# Authority registry

Use the strongest source appropriate to the track. This registry gives defaults, not permission to claim that every source statement is correct.

## Source hierarchy

1. Normative standards, specifications, official glossaries, and primary foundational works.
2. Official current product or vendor documentation.
3. Primary research and official incident reports.
4. Recognized expert interpretation or community practice.
5. AI Academy local frameworks and simulated examples.

When sources disagree, record the conflict, scope, version, and chosen interpretation. Do not blend incompatible definitions silently.

## Testing and Quality Assurance

- Use the current ISTQB CTFL syllabus and glossary for baseline terminology and learning-objective level.
- Use official standard or tool documentation for provider-specific behavior.
- Do not turn ISTQB coverage into a requirement that every AI Academy course must be certification training.
- Distinguish Testing, Debugging, QC, QA, Verification, and Validation consistently.

## Domain-Driven Design

- Prefer Eric Evans's Domain-Driven Design Reference and the foundational book for canonical terminology.
- Treat workshop formats, scoring formulas, documentation workflows, and prioritization thresholds as community practice or local convention unless a primary source makes them normative.
- Keep Domain, Subdomain, Capability, Model, and Bounded Context distinct.
- Do not equate Domain Event with an event-sourced storage record, or require an Anti-Corruption Layer for every integration.

## Human-Centered Design

- Use the cited edition of Don Norman's work for Norman-specific concepts.
- Use applicable ISO or accessibility standards for normative usability/accessibility claims.
- Mark teaching-company names and operational numbers as simulated when they are not documented real cases.
- Do not present an illustrative UI preference as a universal design law.

## AI, software tools, and vendor behavior

- Prefer official documentation, specifications, model cards, and primary research.
- Record the checked date for model behavior, pricing, limits, API semantics, security controls, and fast-moving recommendations.
- Separate observed behavior from contractual guarantees.

## Evidence rules

- A file-level `sourceRef` proves location, not support. Reviewers need a heading, section, page, URL fragment, or claim identifier.
- `reviewedAt` is metadata, not review evidence.
- A source can support a definition without supporting a numerical threshold or recommendation derived from it.
- When only weak authority exists, qualify the claim or teach it explicitly as a heuristic.
