---
name: ddd-validator
description: "Dùng ngay sau khi tạo hoặc sửa bất kỳ DDD artifact ở Phase 3 (incremental validate) và bắt buộc trước khi unlock Phase 5 (full gate ở Phase 4). Validate bằng 49 rules (39 quality: Strategic Design, Glossary, Event Storm incl. read-side E10-E11, Aggregate, Context Map, ADR + 10 structural/cross-BC), load on-demand theo artifact type, severity-aware scoring với minimum threshold per category."
version: 3.5
---
# DDD Validator — Skill Definition v3.5

## Mô tả
Bộ validator đảm bảo DDD artifacts đúng chuẩn. Gồm **39 quality rules** (S1-S4, G1-G11, E1-E11 [12 rules incl. E1b], A1-A4, C1-C6, R1-R2) và **10 structural/cross-BC rules** (V5, V7, V8, V9, V10, V11, V12, XB-1→3). **Tổng: 49 rules.** Chạy **incremental** sau mỗi artifact ở Phase 3, và **full gate** ở Phase 4.

## Phase: 3 (incremental) + 4 (full gate)

> **Nguồn trích dẫn trong rules:** `Lesson x.y` = giáo trình DDD nội bộ (M1-M7) mà bộ rule được rút ra; `CTEER v2.0` = framework review nội bộ; `Review Correction Log #n` / `Session review` = lỗi thực chiến trên dự án CRM. Không cần các tài liệu này để chạy validator — mỗi rule đã tự chứa checklist.

## Rule Categories — Load on Demand

**QUAN TRỌNG:** Chỉ load rule file cần thiết cho artifact đang validate. KHÔNG load toàn bộ.

| Category | File | When to Load | Applies to |
|:--|:--|:--|:--|
| Strategic Design (S1-S4) | `rules/strategic-design.md` | Sau khi tạo/sửa Domain Map hoặc Priority Matrix | `docs/domain-map.md`, `docs/domain-priority.md` |
| Glossary (G1-G11) | `rules/glossary.md` | Sau khi tạo/sửa bất kỳ glossary file | `docs/bounded-contexts/*/glossary/*.md` |
| Event Storm (E1-E11) | `rules/event-storm.md` | Sau khi tạo/sửa Event Storm (E10-E11 sau Step 4.6 Read Model & Query Modeling) | `docs/bounded-contexts/*/aggregate-*.md` |
| Aggregate (A1-A4) | `rules/aggregate-design.md` | Sau khi tạo/sửa Aggregates section | Event Storm aggregate sections |
| Context Map (C1-C6) | `rules/context-map.md` | Sau khi tạo/sửa Context Map | `docs/context-map.md` |
| ADR (R1-R2) | `rules/adr.md` | Sau khi tạo/sửa bất kỳ ADR | `docs/bounded-contexts/*/decisions/ADR-*.md` |
| Structural (V5, V7-V12) | `rules/structural.md` | Phase 4 full gate only (V12 khi có screen-registry) | All `docs/`, `clarification/`, `validation/`, `mapping/` files |
| Cross-BC (XB-1—XB-3) | `rules/structural.md` | Phase 4 full gate, khi ≥ 2 BCs | All event storms + context map + shared kernel |

## Rule Severity Levels

Mỗi rule có severity xác định impact khi fail:

| Severity | Ý nghĩa | Hành động khi Fail |
|:--|:--|:--|
| 🔴 **blocking** | Thiết kế sai cơ bản, downstream artifacts sẽ sai | **STOP** — fix trước khi tiếp tục |
| 🟠 **degrading** | Artifact thiếu chiều sâu, có rủi ro khi implement | **WARNING** — ghi Action Item P1, cho qua nhưng phải fix trước Phase 5 |
| 🟡 **cosmetic** | Naming/format không chuẩn, không ảnh hưởng logic | **NOTE** — ghi Action Item P2, fix khi có thời gian |

### Severity Assignment

| Rule | Severity | Rationale |
|:--|:--|:--|
| S1 Core ≤ 3 | 🔴 blocking | Sai → phân tán resource, đầu tư sai domain |
| S2 Business Strategy | 🔴 blocking | Sai → classify dựa trên complexity thay vì value |
| S3 Investment Strategy | 🟠 degrading | Thiếu → PO/PM không biết Build vs Buy |
| S4 Objective Criteria | 🟠 degrading | Thiếu → scoring subjective, bias |
| G1 Glossary 8 phần | 🟠 degrading | Thiếu → dev tự suy, schema drift |
| G2 DDD Taxonomy | 🔴 blocking | Sai Entity/VO → design sai cơ bản |
| G3 Conflict Severity | 🟡 cosmetic | Thiếu → team có thể miss multi-context issues |
| G4 Glossary Coverage | 🔴 blocking | Thiếu terms → Event Storm dùng từ không định nghĩa |
| E1 Tense Convention | 🟡 cosmetic | Sai tense → confusing nhưng không break logic |
| E2 Command ≥2 Events | 🔴 blocking | Thiếu failure events → miss error handling |
| E3 Core ≥15 Events | 🟠 degrading | Ít events → chắc chắn thiếu flows |
| E4 Policy Format | 🔴 blocking | Policy không traceable → BR bị orphan |
| E5 Hot Spots ≥3 | 🟠 degrading | 0 hot spots → chưa đào đủ sâu |
| A1 Invariant Boundary | 🔴 blocking | Sai boundary → invariant violation ở runtime |
| A2 Small Aggregates | 🟠 degrading | Quá lớn → performance + concurrency issues |
| A3 Reference by ID | 🟡 cosmetic | Nested object → performance nhưng fixable |
| A4 Eventual Consistency | 🟠 degrading | Atomic cross-aggregate → lock contention |
| C1 Integration Pattern | 🔴 blocking | Thiếu pattern → API crash khi integrate |
| C2 Conformist Check | 🟡 cosmetic | Mislabel → confusing nhưng không break |
| C3 ACL Translation | 🟠 degrading | Thiếu translation table → mapping sai lúc implement |
| C4 OHS Consumer Count | 🟡 cosmetic | Wrong pattern choice → refactor later |
| C5 U/D Direction | 🟡 cosmetic | Label inconsistency → confusing diagram |
| R1 ADR 4 phần | 🟠 degrading | Thiếu consequences → không thấy trade-off |
| R2 ADR Business Invariant | 🟠 degrading | Override không gắn BR → mất context |
| V5 ADR Justification | 🟠 degrading | Missing rationale → questionable classification |
| V7 Priority ↔ Pain Point | 🔴 blocking | Core without evidence → đầu tư mù |
| V8 P0→ADR Coverage | 🔴 blocking | Decision mất ADR → mất context vĩnh viễn |
| V9 Artifact Freshness | 🔴 blocking | Stale validation → Phase 5 trên nền chưa verify |
| V10 BC Folder Completeness | 🔴 blocking | Thiếu artifact type (VD: flows/) → validation pass nhưng thực chất thiếu artifacts |
| V11 Read-Flow Completeness | 🟠 degrading | Thiếu read-flow → backlog không sinh được Read Story |
| V12 Screen ↔ Command/Query Coverage | 🔴 blocking | Screen orphan → Read Model bị bỏ sót, gap backlog |
| E6 Read Model per Command (input) | 🟠 degrading | Thiếu → dev tự bịa screen flow, UX inconsistent |
| E10 Query Model Coverage (output) | 🟠 degrading | Thiếu → read side tàng hình, backlog rớt ~40% scope hiển thị |
| E11 Projector Coverage | 🟠 degrading | Thiếu → output Read Model không cập nhật, màn hình stale |
| E7 Pivotal Events ≥ 1 | 🟡 cosmetic | Thiếu → chưa nhận diện phase boundaries, nhưng không break logic |
| E8 Recovery Path per Failure | 🔴 blocking | Failure event thiếu recovery → agent/dev tự giả định retry logic sai |
| E9 State Transition Trigger | 🔴 blocking | Lifecycle thiếu trigger chính xác → sai timing đóng băng/lock |
| G10 Enum Value Completeness | 🔴 blocking | Gộp nhầm enum values → schema sai, code thiếu case handling |
| G11 Alias Verification | 🔴 blocking | Alias sai → Ubiquitous Language ô nhiễm toàn hệ thống |
| C6 BC Ownership Evidence | 🟠 degrading | Assignment chỉ dựa tên → concept ở sai BC, team sai own |
| XB-1 Cross-BC Event Coverage | 🔴 blocking | Orphan cross-BC event → integration failure ở runtime |
| XB-2 Shared Kernel Consistency | 🔴 blocking | Term drift → 2 teams implement cùng concept khác nhau |
| XB-3 Context Map Bidirectionality | 🟠 degrading | Missing reference → confusing nhưng có thể fixable |

## Workflow — Phase 3 Incremental

```
AI tạo artifact (VD: glossary/unit.md)
  ↓
AI reads SKILL.md index (file này) → xác định: glossary → load rules/glossary.md
  ↓
AI load rules/glossary.md (~50 dòng)
  ↓
AI chạy G1-G11 against unit.md
  ↓
Pass? → tiếp tục. Fail (blocking)? → fix ngay, re-validate.
  ↓
Late Discovery? → ghi vào clarification/clarification-questions.md § Late Discoveries
```

## Workflow — Phase 4 Full Gate

```
AI load ALL rule files (rules/*.md)
  ↓
AI chạy toàn bộ 49 rules against ALL artifacts
  ↓
Check Minimum Threshold: mỗi category ≥ 50%?
  ↓
Check Blocking Rules: any 🔴 blocking rule fail?
  ↓
Tạo validation/validation-report.md (template bên dưới)
  ↓
All pass + thresholds met? → unlock Phase 5
Any blocking fail OR category < 50%? → STOP, fix, re-validate
```

## Workflow — Phase 4 Convergence

```
Full Gate validate → có blocking failures?
  ↓
YES → Convergence Loop (xem `../_shared/references/gates-and-project-state.md` § Convergence Loop)
  - Fix upstream artifacts
  - Re-validate (lặp, tối đa 3 vòng)
  - Log mỗi vòng vào validation/convergence-log.md
  ↓
NO blocking + tất cả categories ≥ 50%?
  → Trigger Gate G4 (Stakeholder Architecture Sign-off)
  ↓
G4 Approve → Unlock Phase 5
G4 Request Changes → thêm 1 vòng convergence
```

## Feedback Loop — Late Discoveries (Phase 3 → Phase 2)

Khi Phase 3 modeling phát hiện gaps mới chưa cover ở Phase 1-2:

```
Phase 3: Đang tạo Event Storm → phát hiện flow chưa ai hỏi
  ↓
KHÔNG quay lại Phase 2 chính thức (không reset phase state)
  ↓
Ghi câu hỏi mới vào clarification/clarification-questions.md § "Late Discoveries"
  ↓
Tag [LATE-P0/P1/P2] + ghi "Discovered during: [artifact name]"
  ↓
LATE-P0 → pause artifact đang viết, đợi answer trước khi tiếp
LATE-P1/P2 → ghi nhận, tiếp tục viết, đánh dấu assumption trong artifact
```

## Report Template

```markdown
# Validation Report — [Project Name]
## Date: [YYYY-MM-DD]
## Summary: X/49 passed | Y warnings | Z failures

### Gate Decision
- Blocking failures: [count] → [PASS/BLOCK]
- Category minimum (≥50% each): [PASS/BLOCK]
- Overall: [UNLOCK Phase 5 / BLOCKED — fix required]

### Quality Rules
| Category | Rules | Pass | Partial | Fail | Score | Min 50% |
|:--|:--|:--|:--|:--|:--|:--|
| Strategic Design | S1-S4 (4) | | | | /100 | ✅/❌ |
| Glossary | G1-G11 (11) | | | | /100 | ✅/❌ |
| Event Storm | E1-E11 incl. E1b (12) | | | | /100 | ✅/❌ |
| Aggregate Design | A1-A4 (4) | | | | /100 | ✅/❌ |
| Context Map | C1-C6 (6) | | | | /100 | ✅/❌ |
| ADR | R1-R2 (2) | | | | /100 | ✅/❌ |

### Structural + Cross-BC Rules
| Rule | Severity | Status | Details |
|:--|:--|:--|:--|
| V5 ADR Justification | 🟠 degrading | ✅/❌ | |
| V7 Priority ↔ Pain Point | 🔴 blocking | ✅/❌ | |
| V8 P0→ADR Coverage | 🔴 blocking | ✅/❌ | |
| V9 Artifact Freshness | 🔴 blocking | ✅/❌ | |
| V10 BC Folder Completeness | 🔴 blocking | ✅/❌ | |
| V11 Read-Flow Completeness | 🟠 degrading | ✅/❌ | |
| V12 Screen ↔ Command/Query Coverage | 🔴 blocking | ✅/❌ | (khi có screen-registry) |
| XB-1 Cross-BC Event Coverage | 🔴 blocking | ✅/❌ | (khi ≥2 BCs) |
| XB-2 Shared Kernel Consistency | 🔴 blocking | ✅/❌ | (khi ≥2 BCs) |
| XB-3 Context Map Bidirectionality | 🟠 degrading | ✅/❌ | (khi ≥2 BCs) |

### Blocking Failures (must fix)
- [ ] [rule]: [details]

### Degrading Warnings (fix before Phase 5)
- [ ] [rule]: [details]

### Cosmetic Notes (fix when possible)
- [ ] [rule]: [details]
```

## Evaluation Scorecard Weights

| Category | Rules | Weight | Min Threshold | Rationale |
|:--|:--|:--|:--|:--|
| Glossary | G1-G11 | 25% | ≥50% | Contract giữa Business và Tech |
| Event Storm | E1-E11 (incl. E1b) | 25% | ≥50% | Bản đồ hành vi (Write + Read) — thiếu = miss flows/queries |
| Strategic Design | S1-S4 | 20% | ≥50% | Sai → đầu tư sai domain |
| Aggregate Design | A1-A4 | 15% | ≥50% | Boundary sai → invariant violation |
| Context Map | C1-C6 | 10% | ≥50% | Pattern sai → API crash |
| ADR | R1-R2 | 5% | ≥50% | Thiếu → mất context quyết định |

> **Minimum Threshold Rule:** Dù weighted average cao, nếu BẤT KỲ category nào < 50% → BLOCK Phase 5. Lý do: Aggregate 0% nhưng Glossary 100% → weighted average có thể pass, nhưng invariant boundaries sai = hệ thống crash ở runtime.

> **Cross-BC Rules:** XB-1→XB-3 không tính vào weighted average. Chúng là pass/fail gates riêng, chỉ kiểm tra khi ≥ 2 BCs.

## Changelog
| Version | Date | Changes |
|:--|:--|:--|
| 2.0 | 2026-06-30 | Initial: 20 quality + 2 structural rules, load-on-demand, scorecard weights |
| 2.1 | 2026-06-30 | Added: V8 (P0→ADR), V9 (Freshness), severity levels, min threshold per category, feedback loop protocol |
| 3.0 | 2026-07-01 | Added: E6 (Read Model), E7 (Pivotal Events), XB-1→3 (Cross-BC rules), Convergence Loop workflow, Gate G4 integration |
| 3.1 | 2026-07-09 | Root cause fixes: E8 (Recovery Path), E9 (State Trigger Precision), G10 (Enum Completeness), G11 (Alias Enforcement), C6 (BC Ownership Evidence). Source: review-correction-log Phase 2 |
| 3.2 | 2026-07-11 | Added: V10 (BC Folder Completeness — blocking). Source: Memo project — agent skipped flows/ in Phase 3, validator didn't catch |
| 3.3 | 2026-07-13 | Fixed rule-count drift: frontmatter/workflow/report template said 24-34 rules, actual count from rules/*.md = 45 (37 quality + 8 structural/cross-BC). Scorecard rule ranges (G1-G4→G1-G11, E1-E5→E1-E9, C1-C5→C1-C6) updated to match. Also fixed stale `docs/domain/` paths → actual repo structure. Source: Antigravity/Claude Code skill migration review |
| 3.4 | 2026-07-20 | Read-side coverage: E10 (Query Model Coverage), E11 (Projector Coverage) chống Write-side bias; V11 (Read-Flow Completeness), V12 (Screen↔Command/Query Coverage). Rule count 45→49 (39 quality + 10 structural). Also folded V10 into frontmatter/load-table (đã thêm ở 3.2 nhưng chưa đồng bộ). Source: read-write-model + Sprint Plan Coverage review — backlog rớt ~41.4 MD Read Models |
| 3.5 | 2026-11-10 | Packaging cho My_Skills/DDD: sửa workflow incremental G1-G4→G1-G11; trỏ Convergence Loop + Gates sang `_shared/references/`; V9 dùng git commit time thay mtime; path generic `mapping/`; G2 taxonomy đồng bộ template; G5/G6/G8/G9 bỏ hard-code CRM và file discovery không tồn tại |
