---
name: ddd-documenter
description: Dùng ở Phase 5 sau khi Phase 4 Validation PASS (0 blocking failures) và Gate G4 Architecture Sign-off approved, khi cần tổng hợp DDD artifacts thành deliverables cuối cho stakeholders — BRD, Technical Architecture Overview, Developer Onboarding Guide.
version: 2.1
---

# DDD Documenter — Skill Definition

## Mô tả
Skill tổng hợp toàn bộ DDD artifacts đã validated thành deliverables đọc được cho Dev team, BA, PO. Tạo documents tổng hợp từ các atomic artifacts.

## Phase: 5 (Documentation)

## Prerequisite
- Phase 4 (Validation) PHẢI pass: `validation/validation-report.md` → 0 blocking failures
- Tất cả core artifacts có trong `docs/`

## Pre-Check: Artifact Freshness (V9)

**TRƯỚC KHI bắt đầu tạo deliverables, PHẢI chạy freshness check:**

```
1. Đọc `validation/validation-report.md` → lấy Date field
2. Scan tất cả files trong `docs/` → lấy thời điểm sửa cuối (ưu tiên `git log -1 --format=%cI -- <file>`; file chưa commit = stale — mtime không tin cậy sau clone/checkout)
3. Nếu BẤT KỲ file nào modified SAU validation report date:
   → ❌ BLOCK Phase 5
   → List các files bị stale
   → Yêu cầu chạy lại Phase 4 (ddd-validator full gate)
4. Nếu tất cả files cũ hơn hoặc bằng validation report:
   → ✅ Proceed to Gate G4 check
```

**Tại sao:** Deliverables tổng hợp từ `docs/` artifacts. Nếu artifact bị sửa sau validation, deliverable sẽ chứa nội dung chưa được kiểm tra → phá vỡ trust chain.

## Pre-Check: Gate G4 Sign-off

**TRƯỚC KHI bắt đầu tạo deliverables, PHẢI kiểm tra:**

```
1. Đọc `project-state.md` → section "Gate Review Log" (format: `../_shared/references/gates-and-project-state.md`)
2. Gate G4 (Architecture Sign-off) phải có outcome = ✅ Approve
3. Nếu chưa có G4 → ❌ BLOCK Phase 5
4. Nếu G4 = 🔄 Request Changes → changes phải đã được apply + re-validated
```

**Tại sao:** Gate G4 là stakeholder sign-off cuối cùng trước khi tạo deliverables. Không có G4 = deliverables chưa được architect/PO duyệt.

## Deliverables

### 1. BRD — Business Requirements Document (`deliverables/brd.md`)
Tổng hợp từ:
- `discovery/intake-summary.md` → project overview, scope
- `docs/domain-map.md` → domain inventory
- `docs/bounded-contexts/*/glossary/*.md` → terminology section
- `docs/domain-priority.md` → priority & investment
- Business rules từ SRS → consolidated rules section

Cấu trúc:
```markdown
# BRD — [Project Name]
## 1. Vision & Scope
## 2. Stakeholders & Roles
## 3. Domain Inventory (from Domain Map)
## 4. Business Rules (consolidated)
## 5. Glossary (key terms)
## 6. Priority & Investment Strategy
## 7. Out of Scope
## 8. Assumptions & Dependencies
```

### 2. Technical Architecture Overview (`deliverables/technical-overview.md`)
Tổng hợp từ:
- `docs/context-map.md` → bounded contexts + integration
- `docs/bounded-contexts/*/aggregate-*.md` → key event flows
- `docs/bounded-contexts/*/decisions/ADR-*.md` → architectural decisions
- `docs/architecture/repo-structure.md` → code organization

Cấu trúc:
```markdown
# Technical Architecture — [Project Name]
## 1. Bounded Contexts Overview
## 2. Context Map & Integration Patterns
## 3. Key Event Flows (per Core domain)
## 4. Architectural Decisions (ADR summary)
## 5. Repository Structure Blueprint
## 6. Technology Stack & Constraints
```

### 3. Developer Onboarding Guide (`deliverables/onboarding-guide.md`)
Tổng hợp từ tất cả artifacts — viết cho developer mới join team.

Cấu trúc:
```markdown
# Developer Onboarding — [Project Name]
## 1. Project Overview (2 phút đọc)
## 2. Domain Map — Bức tranh tổng thể
## 3. Glossary — 10 terms quan trọng nhất
## 4. Context Map — Team nào own context nào
## 5. Event Flows — 3 flows quan trọng nhất
## 6. ADRs — Tại sao chúng ta quyết định thế này
## 7. Repo Structure — Code ở đâu
## 8. Tài liệu tham khảo
```

## Quy tắc
- **Không copy-paste nguyên văn** — tổng hợp, viết lại cho audience cụ thể
- **Cross-link về artifacts gốc** — "Chi tiết: xem [docs/bounded-contexts/<bc-name>/glossary/resource.md]"
- **Deliverable ≠ source of truth** — source of truth vẫn là atomic files trong `docs/`
- **Version control** — ghi date + version trong header mỗi deliverable
