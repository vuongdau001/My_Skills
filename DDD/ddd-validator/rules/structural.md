---
category: Structural
rules: V5, V7, V8, V9, V10, V11, V12, XB-1, XB-2, XB-3
applies_to: [All docs/ files, clarification/, validation/, mapping/]
note: "V1→G4, V2→E3, V3→C1, V4→E4, V6→G3 have been merged into quality rules. V5, V7, V8, V9, V10, V11, V12 remain as standalone structural checks. XB-1→XB-3 are cross-BC rules activated when ≥ 2 BCs exist."
---
# Structural Rules (V5, V7, V8, V9, V10, V11, V12) + Cross-BC Rules (XB-1→XB-3)

> Structural checks are cross-cutting and don't fit into a single quality category. Run during Phase 4 full gate only.
> Cross-BC rules only activate when ≥ 2 Bounded Contexts exist in the project.

### V5: ADR Justification for Classification Decisions
- **Scan:** `docs/domain-priority.md` → Core/Supporting/Generic decisions
- **Check:** Mỗi classification decision có ADR hoặc clear rationale?
- **Result:** ✅ Justified | ❌ Missing justification for: [decision]
- **Note:** ADR không bắt buộc cho mọi classification — chỉ cần khi có override hoặc controversial decision.

### V7: Priority ↔ Pain Point Alignment
- **Scan:** `docs/domain-priority.md` → Core domains
- **Cross-ref:** `discovery/pain-points.md` → quantified impact
- **Check:** Core domain có quantified pain point (tiền/thời gian/%)?
- **Result:** ✅ Evidence-based | ❌ Core without evidence: [domain]

### V8: P0 Blocker → ADR Pipeline Coverage
- **Scan:** `clarification/clarification-questions.md` → tất cả items có 🔴 P0
- **Check (2 bước):**
  1. **Completeness:** Mọi P0 question đã answered (`[x]`)? Nếu còn `[ ]` → ❌ BLOCK.
  2. **ADR Coverage:** Mỗi P0 answer tạo ra decision (override BR, chốt architecture) → có ADR file tương ứng trong `docs/bounded-contexts/*/decisions/ADR-*.md`?
- **Cross-ref:** Gate Review Summary table (column "ADR") → file tồn tại?
- **Result:** ✅ All P0 covered | ❌ Missing ADR for: [Q-number → decision]
- **Tại sao:** P0 decisions chỉ ghi inline trong clarification file = mất context sau 2 tháng. ADR bắt buộc đảm bảo mọi quyết định kiến trúc được lưu trữ chính thức và traceable.

### V9: Artifact Freshness — Validation Report còn hiệu lực
- **Scan:** `validation/validation-report.md` → lấy timestamp (Date field)
- **Cross-ref:** Tất cả files trong `docs/` → lấy thời điểm sửa cuối. **Ưu tiên git:** `git log -1 --format=%cI -- <file>` (mtime filesystem bị reset khi clone/checkout → không tin cậy). Có thay đổi chưa commit trong `docs/` (`git status --porcelain docs/`) → coi là stale.
- **Check:** Có file nào trong `docs/` modified SAU validation-report.md không?
- **Result:** ✅ All artifacts fresh | ❌ Stale validation — re-validate required: [list files modified after report]
- **Tại sao:** Nếu artifact bị sửa sau validation, deliverables ở Phase 5 sẽ dựa trên trạng thái chưa được kiểm tra. Rule này buộc re-validate trước khi xuất final documents.
- **Note:** Rule này cũng được `ddd-documenter` kiểm tra như pre-check trước khi bắt đầu Phase 5.

### V10: BC Folder Completeness — tất cả artifact types phải có
- **Scan:** Mỗi `docs/bounded-contexts/<bc-name>/` directory
- **Cross-ref:** BC Folder Completeness Checklist trong `ddd-modeler` SKILL.md
- **Check:** Mỗi BC PHẢI có đầy đủ:
  1. `README.md` — Domain Tree + File Map
  2. `aggregate-*.md` — ≥1 Event Storm file
  3. `glossary/` — ≥1 glossary file
  4. `flows/` — ≥1 flow diagram file + `README.md` index
  5. `decisions/` — ≥1 ADR file (nếu BC có architectural decisions)
- **Result:** ✅ Complete | ❌ Missing: [list missing items]
- **Severity:** 🔴 blocking — Thiếu artifact type = downstream artifacts build trên nền không đầy đủ
- **Tại sao:** Agent có thể skip pipeline steps (VD: tạo Event Storm nhưng skip Flow Diagrams). Nếu không check folder completeness, validation report sẽ ghi "pass" nhưng thực chất thiếu artifacts quan trọng.

### V11: Read-Flow Completeness — luồng đọc phải có mặt
- **Scan:** Mỗi BC có `## Query Models (Output)` không rỗng trong `aggregate-*.md`
- **Cross-ref:** `docs/bounded-contexts/<bc>/flows/` → tìm file `view-*.md`
- **Check:** Mỗi output Query (màn hình List/Detail/Report) có ≥1 read-flow `flows/view-*.md` tương ứng?
- **Result:** ✅ Complete | ❌ Missing read-flow for: [Query → screen]
- **Severity:** 🟠 degrading
- **Tại sao:** Command-flow đầy đủ nhưng thiếu read-flow → backlog planner không có nguồn để sinh Read Story, read side lại "tàng hình". Song hành với V10 (chỉ check command side).

### V12: Screen ↔ Command/Query Coverage — không màn hình mồ côi
- **Khi nào chạy:** Khi `mapping/screen-registry.md` tồn tại (ui-ddd-mapping đã chạy)
- **Scan:** `screen-registry.md` → tất cả Screen ID
- **Cross-ref:** `aggregate-*.md` Commands table (`data-command`) + `## Query Models` (output)
- **Check:** Mỗi screen map được sang **≥1 Command HOẶC ≥1 Query**?
  - Screen có data-table + không có `data-command` = read-only → PHẢI có Query Model.
  - Screen có form submit → PHẢI có Command.
- **Result:** ✅ Every screen covered | ❌ Orphan screens (không có Command lẫn Query): [list]
- **Severity:** 🔴 blocking — screen orphan = gap read/write chắc chắn thiếu backlog item.
- **Tại sao:** Đây là gap-detector cuối cùng: đối chiếu mockup thực tế với DDD Core để bắt Read Model bị bỏ sót trước khi lập backlog. Screen read-only không có Query = màn hình không có API phục vụ.

---

## Cross-BC Rules (XB-1 → XB-3)

> Chỉ kích hoạt khi project có ≥ 2 Bounded Contexts. Single-BC projects skip toàn bộ section này.

### XB-1: Cross-BC Event Coverage
- **Khi nào chạy:** Khi có ≥ 2 Event Storm files
- **Scan:** Tất cả `docs/bounded-contexts/*/aggregate-*.md` → collect events marked "Downstream"
- **Cross-ref:** `docs/context-map.md` → integration relationships
- **Check:** Event published bởi BC-A phải có ≥1 subscriber ở BC khác HOẶC ghi rõ "internal only"
- **Result:** ✅ All cross-BC events covered | ❌ Orphan events: [list]
- **Tại sao:** Orphan cross-BC event = integration failure ở runtime. Không ai consume event → hoặc thiếu subscriber, hoặc event không cần publish.

### XB-2: Shared Kernel Consistency
- **Khi nào chạy:** Khi `docs/shared-kernel.md` tồn tại
- **Scan:** Shared Kernel terms → find corresponding glossary entries per BC
- **Check:** Definition identical across all consuming BCs?
- **Result:** ✅ Consistent | ❌ Drift detected: [term] defined differently in [BC-A] vs [BC-B]
- **Tại sao:** Term drift = 2 teams implement cùng concept khác nhau = integration bugs chỉ phát hiện khi test E2E.

### XB-3: Context Map Bidirectional Consistency
- **Khi nào chạy:** Khi Context Map có ≥ 2 relationships
- **Scan:** `docs/context-map.md` → Relationships table
- **Check:** Nếu BC-A upstream → BC-B downstream, thì BC-B Event Storm phải reference BC-A data
- **Result:** ✅ Consistent | ❌ Missing reference: [BC-B] claims downstream but no integration documented
- **Tại sao:** Upstream/Downstream label không khớp với thực tế data flow → confusing diagram, có thể dẫn tới sai integration pattern.

---

## Merge Log
| Old Rule | Merged Into | Rationale |
|:--|:--|:--|
| V1 Glossary Coverage | G4 | Same check: "mỗi term có file" |
| V2 Event Completeness | E3 | Same check: "core domain ≥15 events" |
| V3 Context Consistency | C1 | Same check: "mỗi BC có relationship" |
| V4 Rule Traceability | E4 | Same check: "policy traceable to BR" |
| V6 Conflict Check | G3 | Same check: "multi-context term rated" |

## Addition Log
| Rule | Version Added | Rationale |
|:--|:--|:--|
| V8 P0→ADR Coverage | v2.1 | P0 answers tạo decisions nhưng không ai kiểm tra ADR file tồn tại |
| V9 Artifact Freshness | v2.1 | Post-validation edits khiến Phase 5 deliverables dựa trên stale state |
| XB-1 Cross-BC Event Coverage | v3.0 | Multi-BC: orphan cross-BC events = integration failure |
| XB-2 Shared Kernel Consistency | v3.0 | Multi-BC: term drift across BCs = implementation mismatch |
| XB-3 Context Map Bidirectionality | v3.0 | Multi-BC: U/D label phải khớp actual data flow |
| V10 BC Folder Completeness | v3.2 | Agent skip flows/ trong Phase 3, validator không bắt |
| V11 Read-Flow Completeness | v3.4 | Command-flow đủ nhưng thiếu read-flow → read side tàng hình |
| V12 Screen ↔ Command/Query Coverage | v3.4 | Screen read-only không map Query = Read Model bị bỏ sót |
