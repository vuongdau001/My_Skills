# Content layout, diagrams and visual handoff — AI Academy

Use when authoring or rewriting learner-facing theory, or when the user requests a layout/visual design. Preserve source-backed knowledge and assessment alignment while reducing repeated prose.

## Choose the representation

| Knowledge relationship | Preferred representation |
|---|---|
| Sequence/branching | Flowchart, optionally Mermaid |
| Multi-party process with event/message semantics | BPMN when those semantics matter and can be specified correctly |
| State changes/guards | State diagram |
| Interactions in time | Sequence diagram |
| Concepts, scope, objects | Concept/domain diagram |
| Comparable concepts/options | Concise table |
| Takeaway mindset | Concept illustration when it explains the idea |

A diagram may carry the main explanation of a process. Prose explains interpretation, why, boundaries and the conclusion rather than repeating every arrow. Keep the notation accurate; naming a flowchart BPMN does not make it BPMN. Distinguish confirmed and simulated flows. Choose complexity by purpose, not a mandatory diagram/figure quota.

## Content blocks and density

- Start with a concise situation or central question; preserve simulation labels. Keep learning objectives in the design dossier. For the BA/PO profile, do not add a standalone “Sau bài này…” paragraph by default.
- Use meaningful heading hierarchy, short single-idea paragraphs, and restrained bold emphasis. Highlight one governing idea, not every sentence.
- Compare along common criteria in tables. Long paragraphs in cells and many columns indicate that the comparison should be split or partly returned to prose.
- Show worked reasoning in numbered steps, annotated artifacts or before/after comparison. Preserve facts, inference and conclusion; removing duplicate words must not remove a premise needed by a quiz.
- Place limits near the principle they qualify; end with one takeaway and supporting points. Use expandable material for supporting detail, but do not label quiz prerequisites as optional; mark required reading clearly or teach them in the main flow. Detailed source/core/item mapping remains in sidecars/review artifacts with concise citations in theory.
- Code blocks are for code, syntax or genuinely structured technical specimens, not colored containers for ordinary prose.

## Whole-picture process visuals

When the teaching goal is end-to-end thinking, a short chain of role names may hide the key lesson. Show enough participants, external parties, systems/manual records, inputs/outputs and handoffs to explain where the work crosses boundaries. Include decision branches, returns or waiting states that affect the question and the completion condition. Complexity serves the reasoning; do not invent confirmed organization policy or add systems merely for visual density.

Use a cross-functional process map, swimlane or valid BPMN according to the needed semantics. Distinguish work order from supporting tools and automated integration. Mark simulated roles/tools/branches where case evidence is absent. On narrow screens preserve readable labels with a zoomable/openable image, horizontal diagram scrolling or split views and a text equivalent; page overflow checks alone do not prove diagram readability.

## Principle-level takeaway visual

When a concluding infographic helps, explain the reusable principle or relationship, rather than retelling the case. Record the intended takeaway, semantic relationships, limits, and misleading implications to avoid. Check whether the visual still makes sense after removing project names, role names, and story objects. Candidate paths must not imply a proven winner; arrows must not turn a revisitable reasoning aid into a mandatory linear process.

Choose the number of visuals by teaching purpose, not a quota. Do not replace an entire theory page with images or duplicate long prose inside an image. Keep equivalent text, concise source links, and qualifications accessible; inspect legibility at the actual display size. A visually attractive image is not evidence of learning effectiveness.

## Design-only versus visual production

Follow the user's requested phase. If visual production belongs to a specialist later, author content and complete the brief only. Do not spawn/message that agent or generate diagrams/images merely because a brief exists.

Each brief records visual ID, teaching purpose, type, content insertion point, nodes/relations, role/scope boundaries, caption, alt text, factual/simulated status, forbidden implications, source/claim/core mapping, output expectations and review criteria. The specialist retains visual implementation choices within that content contract.

Until assets exist, use a non-visible marker such as `<!-- visual: visual-id -->` in learner Markdown, and provide enough text/table fallback for the taught knowledge. For content-design deliverables, describe placement and the brief inline in Markdown; label instructions as designer notes so the implementer can separate them from learner prose. Do not create HTML/UI previews or diagram assets by default. A preview is a separate implementation deliverable when explicitly requested. Use hidden markers only when preparing an import-ready learner file; never insert broken image links. Record `VISUAL PRODUCTION PENDING`; a design-ready brief is not a completed visual.

When production is authorized, retain editable diagram source and export a compatible SVG/PNG if the runtime does not render Mermaid/BPMN. Check the actual renderer first; a Mermaid fence rendered as code is not a delivered diagram. Keep caption/source mapping when replacing a marker with the real asset.

## Render review — LAYOUT-01

During design-only work, review the Markdown content and representation brief; mark implementation/render validation deferred. When rendered implementation is requested, inspect learner layout using the project's actual renderer and styles at desktop and mobile widths. A standalone preview with custom CSS is exploratory, not evidence of final app display. Validate heading hierarchy, reading density, callouts, table wrapping, diagram labels/branches, contrast and image/link behavior; absence of page overflow alone is insufficient.

For unfinished visuals, review insertion points and content blocks but leave diagram typography/legibility pending. For completed visuals, inspect at the size displayed in the page; split/rearrange rather than merely shrink a wide diagram. Use labels/shapes along with color. Report layout evidence separately from semantic review and learner-effectiveness claims.
