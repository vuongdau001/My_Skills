# Learning-content method

Use this reference when creating or reviewing theory. The objective is not to summarize a source; it is to convert reliable domain knowledge into an observable professional capability.

## 1. Define the learning promise

Record the target audience, prerequisites, module boundary, and the change expected after learning. Write outcomes with observable verbs such as distinguish, derive, diagnose, review, calculate, model, choose, justify, or produce.

Reject outcomes that only say “know”, “understand”, “be familiar with”, or list topics without expected behavior.

## 2. Establish the knowledge baseline

Create a source map before drafting. Prefer canonical specifications, official documentation, primary research, or the recognized foundational work for the domain. Use secondary sources for interpretation, not to override primary definitions.

Classify claims as:

- `canonical`: stable foundational definition or principle;
- `official-current`: vendor, standard, or product behavior that may change;
- `community`: useful interpretation without normative authority;
- `local-convention`: an AI Academy framework, threshold, naming rule, or workflow;
- `lesson-only`: a simplified model or simulated case used for teaching.

For time-sensitive claims, record the verification date. For direct quotes, preserve exact wording, page/section, and permitted quotation length. Mark paraphrases as paraphrases.

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

Use a coherent learning loop, adapting the amount of each element to the subject:

1. **Problem or prediction:** expose a decision, failure, or misconception worth resolving.
2. **Concept:** teach the minimum model needed to reason about it.
3. **Worked application:** demonstrate the model on concrete evidence.
4. **Boundary and trade-off:** state when the model does not apply or what it costs.
5. **Practice:** require the learner to perform the target behavior.
6. **Summary and transition:** compress the decision rule and connect it to the next capability.

Case details, code, tables, and visuals must carry explanatory value. Remove a character name, company name, number, diagram, or anecdote if removing it does not change the learner's reasoning.

For dense topics, separate a concise core lesson from optional deep dives. Do not force a fixed word count; optimize for one coherent capability per module.

### Technical terminology and Vietnamese prose

Maintain a track glossary with the English term, a concise Vietnamese explanation, its technical context, and nearby concepts learners may confuse. Preserve established English technical terms when translating would blur their meaning or make engineering prose unnatural. Introduce their meaning at first substantive use in theory, then use the same term consistently in theory, stems, options, and explanations. Use Vietnamese for actors, actions, evidence, and reasoning; avoid gratuitous English mixing and repeated bilingual parentheticals.

Distinguish terms by meaning rather than mechanically translating or replacing words. Do not flatten relations such as category/subcategory or confuse adjacent concepts. Local labels must be explicitly identified as local. When changing a term or definition, inspect dependent claims and items. Quiz wording may briefly clarify a taught term when necessary for the scenario, but must not supply the answer through that clarification.

### Learner-facing content and editorial cleanup

Keep authoring and release-process notes in review artifacts, not lesson prose. Examples include candidate status, pending independent review, reviewer instructions, and publishing checklists. Preserve their accurate status in the review record; removing them from a lesson does not grant release approval.

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

## 6. Post-release evidence

When data is available, inspect completion time, item difficulty, distractor uptake, discrimination, repeated attempts, learner questions, dropout points, and transfer tasks. Use those signals to revise the lesson; do not rewrite solely to maximize pass rate.
