---
name: ddd-questioner
description: Dùng ở Phase 2 sau khi Discovery hoàn thành, khi cần tạo bộ câu hỏi clarification có hệ thống (6 categories, priority P0/P1/P2) để fill gaps trước khi modeling. Cũng dùng khi Phase 3 modeling phát hiện Late Discovery cần ghi câu hỏi mới mà không reset phase state.
version: 1.2
---

# DDD Questioner — Skill Definition

## Mô tả
Skill tạo bộ câu hỏi clarification có cấu trúc, đảm bảo không bỏ sót thông tin quan trọng trước khi tạo DDD artifacts. Mỗi câu hỏi có priority tag và trạng thái tracking.

## Phase: 2 (Clarification)

## Prerequisite
- Phase 1 (Discovery) PHẢI hoàn thành
- `discovery/` folder phải có ≥3 output files

## 6 Question Categories

| # | Category | Focus | Ví dụ |
|:--|:--|:--|:--|
| Q1 | **Glossary & Terms** | Từ mơ hồ, từ dùng khác nhau giữa teams | "Team Lead' và 'Leader' trong SRS là cùng 1 role?" |
| Q2 | **Business Rules** | Rules implicit, rules có exception | "Allocation >100% có chấp nhận? Team không có Lead chấp nhận bao lâu?" |
| Q3 | **Process Flows** | Happy path + Exception + Edge cases | "Khi move member mà target team đã Inactive → chuyện gì xảy ra?" |
| Q4 | **Integration Points** | Systems nào nói chuyện, protocol, frequency | "ECQS push data qua Kafka hay CRM pull? Tần suất sync?" |
| Q5 | **Non-Functional** | Performance, security, compliance, scale | "Bao nhiêu teams tối đa? Bao nhiêu members tối đa per team?" |
| Q6 | **Migration & Legacy** | Hệ thống cũ, data migration, parallel run | "Dashboard cũ tắt ngay khi CRM go-live hay chạy song song?" |

## Priority Tagging

| Priority | Ý nghĩa | Impact |
|:--|:--|:--|
| 🔴 **P0** | Blocker | Chưa trả lời → KHÔNG THỂ tạo artifact ở Phase 3 |
| 🟠 **P1** | Important | Thiếu → artifact không đầy đủ nhưng vẫn tạo được |
| 🟡 **P2** | Nice-to-have | Bổ sung sau, không block |

## Mandatory Sub-Question Templates — BẮT BUỘC

~60% lỗi phát hiện khi review Phase 2 là do agent **không hỏi đúng câu** ở Phase 2. Các sub-question templates sau **BẮT BUỘC** được sinh ra khi phát hiện keyword trigger:

### T1: Retry/Recovery Point (Q3 — Process Flows)
- **Trigger:** Phát hiện từ khóa: `lỗi`, `retry`, `thất bại`, `reject`, `fail`, `error`, `SAP lỗi`, `sync fail`
- **Template:** *"Khi [process X] bị lỗi/reject tại bước [Y]:
  (1) Retry bắt đầu lại từ bước nào? Từ đầu hay từ bước bị lỗi?
  (2) Ai thực hiện retry? Cùng actor hay escalate?
  (3) Entity quay về trạng thái nào sau retry?"*
- **Priority:** 🔴 P0 (nếu là core flow) | 🟠 P1 (supporting)
- **Nguồn:** Review Correction Log #1 — SAP retry bị suy luận sai thành "duyệt lại từ đầu"

### T2: Freeze/Lock Detection (Q2 — Business Rules)
- **Trigger:** Phát hiện từ khóa: `đóng băng`, `immutable`, `chặn sửa`, `lock`, `freeze`, `không cho sửa`, `read-only`, `bảo vệ`
- **Template:** *"Entity [X] bị đóng băng/chặn sửa:
  (1) Trigger point chính xác: tại state/event nào? (VD: Pending Approval ≠ Approved ≠ Sent)
  (2) Ai/event nào gây ra đóng băng?
  (3) Có cách unlock không? Điều kiện gì?
  (4) Khi unlock, entity quay về state nào?"*
- **Priority:** 🔴 P0 (luôn luôn)
- **Nguồn:** Review Correction Log #3, #4 — sai timing đóng băng Milestone và Invoice

### T3: Attribute Mutation Pattern (Q2 — Business Rules)
- **Trigger:** Attribute có giá trị phụ thuộc vào lifecycle: `date`, `amount`, `deadline`, `duedate`, `due_date`, `total`, `balance`, `rate`
- **Template:** *"Attribute [X] của [Entity Y]:
  (1) Được set 1 lần hay thay đổi qua các stage?
  (2) Nếu multi-phase: stage nào → giá trị gì → trigger gì?
  (3) Giá trị ban đầu là null hay có default?"*
- **Priority:** 🟠 P1
- **Nguồn:** Review Correction Log #5 — duedate bị giả định set 1 lần

### T4: UI Screen / BC Ownership (Q1 — Glossary & Terms)
- **Trigger:** Concept mới chưa rõ thuộc BC nào, hoặc tên concept có thể thuộc nhiều BC
- **Template:** *"Concept [X]:
  (1) User thao tác nó trên màn hình/module nào?
  (2) Có UI riêng hay nằm trong UI của module khác?
  (3) Logic chính của nó nằm trong transaction nào?"*
- **Priority:** 🟠 P1
- **Nguồn:** Review Correction Log #7 — Prepaid Wallet bị đặt sai BC vì không xét UI flow

## Workflow

1. **Đọc Discovery output** — đặc biệt `[INFERRED]` items
2. **Scan theo 6 categories** — mỗi category ≥2 câu hỏi
3. **Tag priority** cho mỗi câu hỏi
4. **Group by stakeholder** — ai trả lời câu nào
5. **Tạo `clarification/clarification-questions.md`**

## Output Format

```markdown
# Clarification Questions — [Project Name]

## Status: X/Y answered | Z P0 remaining

### Q1: Glossary & Terms
- [ ] 🔴 Q1.1: [Câu hỏi] — Stakeholder: [ai trả lời]
- [ ] 🟠 Q1.2: [Câu hỏi] — Stakeholder: [ai trả lời]

### Q2: Business Rules
- [ ] 🔴 Q2.1: [Câu hỏi]
- [x] 🟠 Q2.2: [Câu hỏi] → Answer: [trả lời]
...
```

## Update Workflow

Khi user trả lời câu hỏi:
1. Đánh dấu `[x]` cho câu đã trả lời
2. Ghi answer inline
3. Cập nhật status count
4. Nếu tất cả P0 answered → unlock Phase 3
5. Cập nhật `project-state.md` (template: `../_shared/references/gates-and-project-state.md`)

## Late Discoveries — Feedback Loop (Phase 3 → Phase 2)

Khi Phase 3 modeling phát hiện gaps mới:

1. **KHÔNG reset phase state** — Phase 2 vẫn DONE, Phase 3 tiếp tục
2. **Ghi câu hỏi mới** vào `clarification/clarification-questions.md` section `## Late Discoveries`
3. **Tag format:** `[LATE-P0/P1/P2]` + `Discovered during: [artifact name]`
4. **Impact rule:**
   - `[LATE-P0]` → pause artifact đang viết, đợi answer trước khi tiếp tục
   - `[LATE-P1/P2]` → ghi nhận assumption trong artifact, tiếp tục viết

### Output Format cho Late Discoveries

```markdown
## Late Discoveries (Phase 3 Feedback)
- [ ] [LATE-P1] **QL-01:** [Câu hỏi] — Discovered during: Event Storm / Sales Team Config
  - Assumption used: [assumption nếu tiếp tục viết]
  — Stakeholder: [ai trả lời]
```

## Quy tắc
- Không hỏi câu đã có answer rõ ràng trong tài liệu
- Câu hỏi phải specific, có context — không hỏi chung chung
- Mỗi câu hỏi chỉ ra TẠI SAO cần biết (ảnh hưởng artifact nào)
- Tối đa 25 câu hỏi tổng cộng (bao gồm Late Discoveries) — tránh overwhelm
