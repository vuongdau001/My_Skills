# Renderer facts (ai-academy, 2026-10)
- Theory is read from DB (`modules.theoryContent`) via `src/lib/published-content-cache.ts`; only `isPublished=true` modules appear; quiz questions are synced only for published modules.
- MarkdownRenderer: react-markdown + GFM, no rehypeRaw → raw HTML and `<!-- -->` markers are dropped silently; **no Mermaid in theory** (Mermaid only in lab components). Use static SVG under `public/curriculum/<track>/` with `![alt](/curriculum/<track>/x.svg)`.
- Styles: h2 indigo left border; h3 indigo; blockquote = amber callout; tables wrap in horizontal scroll, `th` is nowrap (long headers force scroll on mobile); code blocks dark.
- Mobile content width ≈ 358px: wide SVGs (960 viewBox) become unreadable → design narrow/vertical (640–720 wide, text ≥ 22 units).
- Lesson route `/module/<moduleId>`; tabs "Lý thuyết" / "Bài tập Lab"; quiz unlocks after `[data-testid=theory-read-done]`, then `[data-testid=start-practice]`.
