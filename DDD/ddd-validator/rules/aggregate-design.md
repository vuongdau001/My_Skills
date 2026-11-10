---
category: Aggregate Design
rules: A1-A4
applies_to: [docs/bounded-contexts/*/aggregate-*.md (Aggregates section)]
sources: [Lesson 7.2, Vaughn Vernon Ch.10]
---
# Aggregate Design Rules (A1-A4)

### A1: Invariant quyết định Aggregate Boundary
- **Nguồn:** Lesson 7.2 Rule 1 — *"Invariant cần 2+ objects → cùng aggregate"*
- **Tại sao:** Allocation tách khỏi Resource → không ai check tổng → 110% bug.
- **Checklist:**
  - [ ] Mỗi Aggregate liệt kê invariants?
  - [ ] Invariant cần >1 object → objects cùng aggregate?
  - [ ] Cross-aggregate invariants → handled by Domain Service (ghi rõ)?

### A2: Prefer Small Aggregates
- **Nguồn:** Lesson 7.2 Rule 2 — *"Large aggregates → performance + concurrency issues"*
- **Tại sao:** Aggregate lớn = lock nhiều rows = slow + conflicts.
- **Checklist:**
  - [ ] Aggregate chỉ chứa objects CẦN cho invariant?
  - [ ] Nếu 2 objects share table nhưng tách aggregate → justify why (khác invariant boundary)?

### A3: Reference Other Aggregates by Identity
- **Nguồn:** Lesson 7.2 Rule 3 — *"Giữa aggregates = ID, không nested object"*
- **Tại sao:** Nested object = load cả database per operation.
- **Checklist:**
  - [ ] Aggregate definition ghi "References (by ID only)" section?
  - [ ] Event data chứa IDs, không full objects?

### A4: Eventual Consistency Outside Boundary
- **Nguồn:** Lesson 7.2 Rule 4 — *"Giữa aggregates = eventually consistent (events)"*
- **Tại sao:** Atomic cross-aggregate → lock contention → performance hit.
- **Checklist:**
  - [ ] Cross-aggregate operations dùng Domain Events hoặc Saga?
  - [ ] Nếu business yêu cầu Atomic cross-aggregate → có ADR justify pragmatic trade-off?
  - [ ] Domain Service cho global invariants (cross-aggregate checks) documented?
