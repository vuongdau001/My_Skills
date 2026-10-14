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

- Start with a short learning promise and a situation callout; preserve simulation labels.
- Use meaningful heading hierarchy, short single-idea paragraphs, and restrained bold emphasis. Highlight one governing idea, not every sentence.
- Compare along common criteria in tables. Long paragraphs in cells and many columns indicate that the comparison should be split or partly returned to prose.
- Show worked reasoning in numbered steps, annotated artifacts or before/after comparison. Preserve facts, inference and conclusion; removing duplicate words must not remove a premise needed by a quiz.
- Place limits near the principle they qualify; end with one takeaway and supporting points. Detailed source/core/item mapping remains in sidecars/review artifacts with concise citations in theory.
- Code blocks are for code, syntax or genuinely structured technical specimens, not colored containers for ordinary prose.

## Design-only versus visual production

Follow the user's requested phase. If visual production belongs to a specialist later, author content and complete the brief only. Do not spawn/message that agent or generate diagrams/images merely because a brief exists.

Each brief records visual ID, teaching purpose, type, content insertion point, nodes/relations, role/scope boundaries, caption, alt text, factual/simulated status, forbidden implications, source/claim/core mapping, output expectations and review criteria. The specialist retains visual implementation choices within that content contract.

Until assets exist, use a non-visible marker such as `<!-- visual: visual-id -->` in learner Markdown, and provide enough text/table fallback for the taught knowledge. For content-design deliverables, describe placement and the brief inline in Markdown; label instructions as designer notes so the implementer can separate them from learner prose. Do not create HTML/UI previews or diagram assets by default. A preview is a separate implementation deliverable when explicitly requested. Use hidden markers only when preparing an import-ready learner file; never insert broken image links. Record `VISUAL PRODUCTION PENDING`; a design-ready brief is not a completed visual.

When production is authorized, retain editable diagram source and export a compatible SVG/PNG if the runtime does not render Mermaid/BPMN. Check the actual renderer first; a Mermaid fence rendered as code is not a delivered diagram. Keep caption/source mapping when replacing a marker with the real asset.

## Render review — LAYOUT-01

During design-only work, review the Markdown content and representation brief; mark implementation/render validation deferred. When rendered implementation is requested, inspect learner layout using the project's actual renderer and styles at desktop and mobile widths. A standalone preview with custom CSS is exploratory, not evidence of final app display. Validate heading hierarchy, reading density, callouts, table wrapping, diagram labels/branches, contrast and image/link behavior; absence of page overflow alone is insufficient.

For unfinished visuals, review insertion points and content blocks but leave diagram typography/legibility pending. For completed visuals, inspect at the size displayed in the page; split/rearrange rather than merely shrink a wide diagram. Use labels/shapes along with color. Report layout evidence separately from semantic review and learner-effectiveness claims.
