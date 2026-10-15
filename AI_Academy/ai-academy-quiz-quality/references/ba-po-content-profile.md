# AI Academy BA/PO — theory and level-1 quiz profile

Apply to the BA/PO course discussed with the user, or another course only after the user explicitly adopts this profile. These are course-specific editorial decisions, not universal pedagogy or a certification standard. Explicit later user instructions take precedence.

## Design and learner experience

Design competency-first and source-first: professional capability -> authoritative knowledge -> core content -> misconceptions -> worked example and quiz blueprint. Present story-first: situation -> gap in understanding -> worked reasoning with concepts explained where needed -> bounded conclusion -> reusable takeaway -> quiz. Adapt the sequence to the concept; do not force the same case structure on every lesson.

Identify the technique being taught, the one central learning promise, the misconception to resolve, the intended shift in reasoning, and the core concepts that support it. Keep objectives in the design dossier; do not display a standalone “Sau bài này…” introduction by default. Keep the number of cores meaningful; do not force five cores to make a five-times-three question grid. Explain definitions, relations, why the technique works, and its limits using official standards/glossaries or foundational works actually accessed. Preserve a complete trace:

`source (author/edition/locator) -> source concept -> taught claim -> core ID -> outcome -> question ID -> reinforcement target/explanation`

Store detailed mapping in the existing assessment sidecar and review source map. Keep learner prose readable with concise citations and necessary qualifications. Reading-time estimates are estimates, not measured pilot results.

## Theory shape

**Content designer output:** Markdown lesson content plus inline presentation instructions (visual type, purpose, nodes/relations, caption and source/core mapping). Leave asset generation, HTML/UI preview and render implementation to the specialist unless the user explicitly requests those deliverables.

1. **Situation:** a concise realistic difficulty, ambiguity, opportunity, or decision; distinguish confirmed fact from simulation. Do not require a dramatic incident or named persona.
2. **Central question:** what the learner should be able to distinguish or explain, and why it matters in BA/PO work.
3. **Core theory:** the definitions, relationships, principles and conditions needed to answer that question. Do not compress prerequisite reasoning into ten lines or replace it with an inspirational quote.
4. **Worked example:** show information -> interpretation -> unresolved points and their effect on the choice -> options -> justification -> bounded conclusion/next check. When the flow is unclear, explain relevant roles, inputs/outputs, handoffs, and completion before choosing the intervention; do not invent a failure or require exhaustive process analysis for every topic. Use a completed illustrative artifact with annotations when helpful. A blank form or question inventory alone is insufficient.
5. **Limits and takeaway:** one main idea supported by the taught principles; an actionable checklist or comparison only when useful. Distinguish when a technique is unnecessary, when to use it lightly, and when deeper analysis is justified.
6. **Quiz:** 15 four-option, single-answer questions at internal level 1, in project format.

Revisit a case across these parts when it provides continuity. Use GAMS, AI Word Add-in, Loan Management, CRM and supplementary situations according to the concept, without inventing confirmed project history. The GAMS case includes a proposal to notify about a subscription **about to expire**, not an already overdue subscription. The proposal does not by itself confirm the underlying need, recipient, responsibility, or renewal process. Member/PM/Purchase/IT roles supplied by the user are case inputs; a PM -> approval -> Purchase -> IT sequence and the relationship between invoice entry and actual renewal remain hypotheses until supported by case evidence. Keep TnM/commercial disputes out of the Loan case. Avoid recurring character stereotypes and explanations that preassign blame to either people or systems.

Before/after examples may compare interview questions, requirements, rules, models or decisions. They need no code or named commercial tool. If using actual product behavior, verify it against official documentation. Simulated examples need coherent conditions; do not invent financial rules, target metrics or approvals to fill a table.

## Case-to-concept acceptance

Each core explanation must connect meaning -> a concrete case detail -> why that interpretation matters to the analysis. A case used only for an opening story, a blank form, or labels pasted onto generic definitions is insufficient. Repair the case if it cannot carry the intended explanation. For flow-analysis lessons, show a filled main flow and meaningful branches with conditions, responses, outcomes and rejoin/termination; do not impose this layout on every lesson. Keep learner-facing prose coherent rather than repeating a mandatory three-column template.

## Chapter narrative and case continuity

Before authoring a chapter, record each lesson's central question, owned technique, prerequisites, next capability and overlap to avoid. Each lesson should contribute a new reasoning step rather than repeat the same warning with new vocabulary. Bridge from an unresolved example to a later selected/implemented solution with an explicit new simulation premise; do not silently promote unknowns into confirmed facts.

Maintain one current case ledger and apply user corrections across all lessons, visuals and source/core/item sidecars in the active scope. Preserve archived versions as history. For GAMS, current user-provided information is that the project PM initiates renewal consideration; IT does not initiate it. The future intent is system-initiated consideration, with trigger conditions still to specify. Initiation does not automatically confer approval, purchasing or renewal authority. Other workflow details remain hypothetical unless supplied or verified. Prefer a neutral “authorized approver” rather than assigning approval to a familiar role just to simplify a downstream example.

For process-led lessons, a useful optional reading path is current work -> whole picture -> concepts on the example -> worked handoff reasoning -> AS-IS/TO-BE -> support scope. Adapt it to the lesson; do not impose six headings or repeat the model in full prose. Separate known AS-IS fragments, a simulated extended flow, intended TO-BE and runtime facts. Automation of the trigger does not imply automation of decisions or the entire process.

Keep outcome/value as the purpose of solution work throughout the chapter. Metric arithmetic supports defensible evidence; place supporting detail outside the main narrative when helpful, but clearly require it before any dependent quiz. Objectives stay in the design dossier and level-1 questions remain concept checks.

## Assessment contract

For the learner page, apply [content-layout-and-visuals.md](content-layout-and-visuals.md): use short blocks/callouts and compact comparisons, process diagrams for relationships that prose obscures, and maintain text fallback when visual assets are pending. In design-only work, hand off nodes/relations, caption, scope and source/core links to the specialist; do not produce or dispatch visuals before the authorized phase.

- Internal **level 1** means remembering/understanding principles, distinguishing nearby concepts, recognising misconceptions and limits already taught. It is not a claim that all items are Bloom Remember, and is unrelated to an external Observe/Analyze/Create/Teach numbering scheme.
- Keep 15 meaningful questions per lesson. Allocate them by concept importance and distinct misconceptions; each essential core must be covered, without a mandatory three-per-core distribution. Replace filler/duplicates rather than raising cognitive demand to reach 15.
- No story trivia, novel case-solving, open-ended judgments, artifact submissions, or grading of practice competence. Teaching an applied worked example does not authorize assessing an applied case.
- Each question needs a core/claim/outcome link, exact theory anchor, source basis, one documented primary assessment purpose, reinforcement target, governing rule, three distinct plausible misconceptions, and an explanation rejecting the nearest confusion.
- Compare options along the same semantic dimension. For example, WHEN/WHILE distractors should represent event/state confusions, not invented BA/developer role restrictions. Do not let correct answers stand out as the only evidence-aware or responsible-sounding choice.
- After a theory rewrite or change of emphasis, recheck all 15 items against source -> core -> taught content -> primary assessment purpose; update stale theory anchors in sidecars. Do not treat unchanged quiz files as proof of continued alignment, and do not turn this review into case-trivia questions.
- Quiz feedback reinforces taught knowledge; it cannot supply a premise missing from the stem. A score describes knowledge-check performance, not professional readiness.

Use the existing runtime quiz fields; keep durable traceability in sidecars/review artifacts. Distinguish the full 15-question bank from the delivered attempt. For random six-question analysis set `--min-applied 0` under this profile; state the chosen objective-coverage target and inspect missing cores. Sampling analysis is not a pass criterion for semantic correctness and does not authorize changing runtime, thresholds, or production data.

## Review and delivery

Review source/claims and theory before dependent items, lesson by lesson. Check worked reasoning, boundaries, terminology, plausible distractors, unique keys, coverage, repetitions and answer cues. Missing source support or an ambiguous/wrong key cannot be offset by an average quality score. Preserve independent-review and pilot status honestly.

Save the requested theory, quiz and review package in the project's agreed output folder. Deliver one chapter for user review before starting the next. Skill updates alone do not authorize editing previously delivered lessons or releasing content. Retain TERM-EN-01 English technical keywords with readable Vietnamese explanation; apply interactive exercises only if separately requested with a learning purpose.
