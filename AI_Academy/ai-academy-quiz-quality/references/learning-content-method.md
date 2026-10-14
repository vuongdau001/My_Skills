# Learning-content method

Use this reference when creating or reviewing theory. The objective is not to summarize a source; it is to convert reliable domain knowledge into an observable professional capability.

## 1. Define the learning promise

Record the target audience, prerequisites, module boundary, and the change expected after learning. Write outcomes with observable verbs such as distinguish, derive, diagnose, review, calculate, model, choose, justify, or produce.

Reject outcomes that only say “know”, “understand”, “be familiar with”, or list topics without expected behavior.

Separate the professional capability the course supports from the operation assessed in this lesson. A lesson can demonstrate a technique while its quiz checks only recall/concept discrimination. Do not infer demonstrated professional competence from a knowledge-check score. Record the agreed assessment scope before selecting examples or activities; for the BA/PO course use [ba-po-content-profile.md](ba-po-content-profile.md).

## 2. Establish the knowledge baseline

Create a source map before drafting. Prefer canonical specifications, official documentation, primary research, or the recognized foundational work for the domain. Use secondary sources for interpretation, not to override primary definitions.

Classify claims as:

- `canonical`: stable foundational definition or principle;
- `official-current`: vendor, standard, or product behavior that may change;
- `community`: useful interpretation without normative authority;
- `local-convention`: an AI Academy framework, threshold, naming rule, or workflow;
- `lesson-only`: a simplified model or simulated case used for teaching.

For time-sensitive claims, record the verification date. For direct quotes, preserve exact wording, page/section, and permitted quotation length. Mark paraphrases as paraphrases.

For each core content, record the source title/author/edition, section/page or term entry, the concept actually supported there, the claim taught in the lesson, and the editorial bridge between them. One citation to a book or an inspirational quote is not support for an entire workflow. Record access limits; do not claim to have read an unavailable handbook or infer its contents from a glossary. Use existing manifest/assessment metadata and review artifacts rather than introducing an incompatible frontmatter or runtime schema.

## 3. Build a claim ledger

Extract claims that can fail independently:

- definitions and category boundaries;
- rules and conditions of application;
- causal claims;
- recommendations and trade-offs;
- numbers, thresholds, dates, performance claims, and quotations;
- absolutes such as “always”, “only”, “must”, and “never”.

Give each claim a source anchor and verdict: `SUPPORTED`, `PARTIALLY_SUPPORTED`, `CONTRADICTED`, or `UNVERIFIABLE`. Record which learning objectives and quiz items depend on it.

A contradicted definition, fabricated quotation, unlabelled simulated statistic, or local heuristic presented as universal is release-blocking.

## 4. Design the lesson

Design in this order: professional capability -> authority baseline -> core concepts and assessed outcomes -> misconceptions -> worked example and assessment blueprint -> learner-facing prose. Present a coherent learning loop, adapting the amount of each element to the subject:

1. **Problem or prediction:** expose a decision, failure, or misconception worth resolving.
2. **Concept:** teach the minimum model needed to reason about it.
3. **Worked application:** demonstrate how evidence is interpreted, what options follow, and why a bounded conclusion is justified. A template or list of unanswered questions alone does not demonstrate the technique.
4. **Boundary and trade-off:** state when the model does not apply or what it costs.
5. **Practice or knowledge check:** ask for the operation agreed in the assessment scope. Artifact creation belongs only where practical assessment is authorized; a level-1 knowledge check remains recall/understanding.
6. **Summary and transition:** compress the decision rule and connect it to the next capability.

Case details, code, tables, and visuals must carry explanatory value. Remove a character name, company name, number, diagram, or anecdote if removing it does not change the learner's reasoning.

For dense topics, separate a concise core lesson from optional deep dives. Do not force a fixed word count; optimize for one coherent capability per module.

### Worked examples, cases, and adapted frameworks

Use a realistic question, opportunity, ambiguity, or decision as the opening; failure/incident is not mandatory. Revisit the opening case when demonstrating reasoning, and introduce another context only when it clarifies transfer or a boundary. Use consistent case facts without forcing a single company, recurring persona, or role stereotype across the course.

Show information -> interpretation -> candidate options -> relevant trade-off -> conclusion within scope -> remaining uncertainty. A before/after comparison can be a requirement, question, rule table, model, or decision record; code/UI is not required. Distinguish the grounds for a conclusion from facts still needing confirmation. When the right conclusion is to seek evidence, demonstrate what is unresolved, why, and which evidence would resolve it; do not fabricate policy to complete an example.

Analyse information, constraints, decisions, coordination, and mechanisms without attributing personal incompetence or declaring a system/process the cause before evidence supports it. Do not put an author's words into a fictional incident; identify an application of their concept as editorial interpretation.

Treat PHÁT and similar narrative structures as local teaching conventions. Select useful elements such as motivation, worked before/after reasoning, and limits; do not import universal ten-line limits, 90/10 ratios, quote/visual quotas, mandatory persona names, or per-lesson artifact exercises. Supporting theory must remain deep enough for the assessed operation. Preserve source distinctions instead of pursuing novel synthesis for its own sake.

Finish with one main takeaway and supporting principles. Use a short actionable checklist when it helps recall; it is not a replacement for explanation. A visual should explain the core concept, relation, or mindset and be referenced in the prose, rather than merely depict a story or satisfy a figure quota.

Design the reading layout as well as the reasoning. Use [content-layout-and-visuals.md](content-layout-and-visuals.md) to choose callouts, comparisons, process/state/concept diagrams and fallback. A diagram can replace a verbal walk through a process; preserve the explanation of why and its limits. Keep a complete source/core/quiz chain while moving detailed editorial mapping out of the learner page. If the user assigns visual production to another agent later, deliver design briefs and placement only, with visual status pending.

### Technical terminology and Vietnamese prose

Maintain a track glossary with the English term, a concise Vietnamese explanation, its technical context, and nearby concepts learners may confuse. Preserve established English technical terms when translating would blur their meaning or make engineering prose unnatural. Introduce their meaning at first substantive use in theory, then use the same term consistently in theory, stems, options, and explanations. Use Vietnamese for actors, actions, evidence, and reasoning; avoid gratuitous English mixing and repeated bilingual parentheticals.

Distinguish terms by meaning rather than mechanically translating or replacing words. Do not flatten relations such as category/subcategory or confuse adjacent concepts. Local labels must be explicitly identified as local. When changing a term or definition, inspect dependent claims and items. Quiz wording may briefly clarify a taught term when necessary for the scenario, but must not supply the answer through that clarification.

Apply rule TERM-EN-01 ([quiz-authoring-and-review.md](quiz-authoring-and-review.md) §3a): technical and domain terms use the English keyword, with an optional short Vietnamese gloss on first use, and "nghiệp vụ" is never used alone. Seed the track glossary from [terminology-en-keywords.md](terminology-en-keywords.md).

### Learner-facing content and editorial cleanup

Keep authoring and release-process notes in review artifacts, not lesson prose. Examples include candidate status, pending independent review, reviewer instructions, and publishing checklists. Preserve their accurate status in the review record; removing them from a lesson does not grant release approval.

Keep detailed core IDs, claim classifications, mapping tables, and author-versus-source labels in review/assessment artifacts unless learners need them to understand the concept. Keep concise citations, genuine source disagreements, simulated-case labels, and interpretation boundaries in the lesson. Avoid repeating an audit label after every paragraph.

When the app already provides the quiz or lab entry point, avoid a redundant quiz-navigation footer in theory. A teaching exercise that develops the learning outcome remains valid. If a question count is shown, distinguish the full bank from the number delivered per attempt.

During editorial cleanup, inspect every module in the requested scope, not only the reported example. Remove process-only material while preserving citations, meaningful image attribution, simulated-case labels, and boundaries or caveats needed to interpret the lesson correctly. Check the rendered lesson when display behavior matters.

## 5. Technical and pedagogical review

Review theory across five dimensions:

- **Factual:** definitions, claims, numbers, quotes, and examples match the authority baseline.
- **Boundary:** canonical doctrine, heuristic, preference, and local convention are clearly separated.
- **Technical:** code and implementation advice state prerequisites, failure modes, security/accessibility concerns, and relevant alternatives.
- **Pedagogical:** outcome, explanation, example, practice, and assessment are aligned.
- **Editorial:** terminology is consistent; Vietnamese is readable; English technical terms are introduced deliberately rather than mixed gratuitously.

Do not infer pedagogical effectiveness from completeness or prose quality. Mark new material `content-ready, pilot-pending` until learner evidence exists.

Correctness, source support, taught-content alignment, and defensible keys are hard gates. A numerical average, engaging narrative, named product, completed checklist, or claim of novelty cannot compensate for their failure. Claims about learning gains, cognitive load, or retention multipliers need a primary study and its measurement context; otherwise omit the number or label a genuinely illustrative value as simulated. Adapted exercise labels are local, not Bloom categories; classify the actual operation rather than the existence of an artifact or section title.

## 6. Post-release evidence

When data is available, inspect completion time, item difficulty, distractor uptake, discrimination, repeated attempts, learner questions, dropout points, and transfer tasks. Use those signals to revise the lesson; do not rewrite solely to maximize pass rate.
