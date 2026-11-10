---
category: ADR
rules: R1-R2
applies_to: [docs/bounded-contexts/*/decisions/ADR-*.md]
sources: [Lesson 6.2, CTEER v2.0]
---
# ADR Rules (R1-R2)

### R1: ADR đủ 4 phần
- **Nguồn:** Lesson 6.2 — *"Mọi architectural decision phải có ADR — không ai nhớ tại sao chọn X sau 6 tháng"*
- **4 phần:** Context, Decision, Consequences, Source
- **Checklist:**
  - [ ] Context = vấn đề gì, tại sao cần quyết định?
  - [ ] Decision = chọn gì, cơ chế?
  - [ ] Consequences = Positive + Negative + Trade-off?
  - [ ] Source = traceability (SRS ref, Clarification ref)?

### R2: ADR gắn với Business Invariant bị override
- **Nguồn:** CTEER v2.0 — *"Mọi DDD concept tồn tại để bảo vệ business invariant"*
- **Checklist:**
  - [ ] ADR ghi rõ BR nào bị override?
  - [ ] Override lý do gắn business value, không chỉ technical convenience?
  - [ ] Phase 2+ trigger conditions documented (khi nào revisit decision)?
