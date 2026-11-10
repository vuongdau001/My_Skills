# Gates, Convergence Loop, Project Layout & `project-state.md`

> Tài liệu dùng chung cho mọi skill trong `DDD/`. Các skill gọi "Gate G3/G4/G6", "Convergence Loop", "project-state.md" đều tham chiếu về đây.
> Nguồn: methodology SRS→DDD v3.0 của dự án CRM (`foundation/01-srs-to-ddd-methodology.md` Ch.4) + Gate Review Log thực tế.

## 1. Pipeline & Gates

```
Phase 0: Intake            ← ddd-discovery
Phase 1: Discovery         ← ddd-discovery
   ↓  Gate G1: Domain Walkthrough
Phase 2: Clarification     ← ddd-questioner
   ↓  Gate G2: Clarification Sign-off (100% P0 answered)
Phase 3: Modeling          ← ddd-modeler (+ ddd-validator incremental)
   ↓  Gate G3: Model Review
Phase 4: Validation        ← ddd-validator (full gate, convergence loop)
   ↓  Gate G4: Architecture Sign-off
Phase 5: Documentation     ← ddd-documenter        ┐ có thể chạy song song
UI Contract Gate           ← ui-ddd-mapping → ui-contract-reviewer (nếu có mockup/UI) ┘
   ↓  Gate G5: Final Handover (deliverables)
Phase 6: Backlog Planning  ← ddd-backlog-planner
   ↓  Gate G6: Backlog Quality Scorecard
Phase 7: Implementation    ← (coding; ddd-backlog-planner Step 6 để đối chiếu tiến độ)
```

| Gate | Reviewer (đề xuất) | Câu hỏi quyết định | Bằng chứng kiểm tra | Điều kiện Approve |
|:--|:--|:--|:--|:--|
| **G1** Domain Walkthrough | PO | Discovery đủ sâu? Câu hỏi đúng hướng? | `discovery/*` | Đủ 6 output files; `[INFERRED]` đã vào clarification queue |
| **G2** Clarification Sign-off | PO + Architect | P0 blockers đã resolve? | `clarification/clarification-questions.md` | 0 câu P0 còn `[ ]` |
| **G3** Model Review | Architect + PO | Model đúng nghiệp vụ? | Toàn bộ Phase 3 artifacts | Hot Spots blocking đã resolve; BC Folder Completeness đủ |
| **G4** Architecture Sign-off | PO + Architect + Lead | Kiến trúc vững? | `validation/validation-report.md` | 0 🔴 blocking fail, mọi category ≥ 50% |
| **G5** Final Handover | Stakeholders | Deliverables dùng được? | `deliverables/*` | Freshness (V9) pass; stakeholder accept |
| **G6** Backlog Quality | PO + Lead + QA | Backlog sẵn sàng coding? | `backlog/README.md` | Đạt Quality Scorecard minimums của `ddd-backlog-planner` |

**Outcome hợp lệ:** `✅ Approve` · `🔄 Request Changes` (phải apply + re-validate trước khi chuyển phase) · `❌ Reject` (quay lại phase trước).

## 2. Convergence Loop (Phase 4)

```
Full gate validate → có 🔴 blocking fail hoặc category < 50%?
  ↓ YES
Sửa UPSTREAM trước (Domain Map → Glossary → Event Storm → Context Map → ADR)
  — KHÔNG sửa downstream trước, vì downstream build trên upstream
  ↓
Re-validate → log vòng vào validation/convergence-log.md
  ↓
Pass? → Gate G4. Fail? → lặp, tối đa 3 vòng.
Sau 3 vòng vẫn fail → dừng, escalate cho human (thường là thiếu thông tin nghiệp vụ → Late Discovery P0).
```

`validation/convergence-log.md`:

```markdown
| Round | Date | Blocking fails | Fixed (upstream → downstream) | Remaining |
|:--|:--|:--|:--|:--|
| 1 | YYYY-MM-DD | E4, G10 | glossary/payment-item.md → aggregate-payment.md | — |
```

## 3. Project Layout (generic)

```
<project>/
├── .agents/skills/              ← cài các skill trong DDD/ vào đây (hoặc ~/.gemini/config/skills)
├── AGENTS.md                    ← từ _shared/AGENTS.template.md
├── project-state.md             ← template §4
├── input/                       ← tài liệu đầu vào (SRS, MoM, API doc, DB schema...)
│   └── mockups/                 ← HTML mockup (nếu có)
├── discovery/                   ← Phase 0-1
├── clarification/               ← Phase 2
├── docs/                        ← Phase 3 (source of truth)
│   ├── domain-map.md · domain-priority.md · context-map.md · shared-kernel.md
│   ├── bounded-contexts/<bc>/   ← README, aggregate-*.md, glossary/, flows/, decisions/, domain-services/
│   └── architecture/
├── mapping/                     ← ui-ddd-mapping, ui-contract-reviewer
├── validation/                  ← Phase 4
├── deliverables/                ← Phase 5
└── backlog/                     ← Phase 6
```

> Dự án nhiều phase (VD CRM) có thể đặt `discovery/`, `clarification/`, `mapping/`, `validation/`, `deliverables/` dưới `phase-N/`. Khi đó thay path tương ứng — skill không phụ thuộc tên phase.

## 4. Template `project-state.md`

```markdown
# Project State — [Project Name]

## Phase Tracker
| Phase | Status | Started | Completed |
|:--|:--|:--|:--|
| Phase 0: Intake | ⏳ / 🔄 / ✅ | | |
| Phase 1: Discovery | | | |
| Phase 2: Clarification | | | |
| Phase 3: Modeling | | | |
| Phase 4: Validation | | | |
| Phase 5: Documentation | | | |
| Phase 6: Backlog | | | |

## Input Files
- `input/...` — [loại tài liệu, version, trạng thái]

## Artifacts Created
- [path] — [mô tả ngắn, version]

## Open Blockers
- [P0 / LATE-P0 question IDs]

## Gate Review Log
| Gate | Phase | Date | Reviewer | Outcome | Evidence | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| G3: Model Review | Phase 3 | YYYY-MM-DD | [Tên — vai trò] | ✅ Approve | [link] | |
```

