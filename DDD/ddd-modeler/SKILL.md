---
name: ddd-modeler
description: Dùng ở Phase 3 Modeling khi tất cả P0 clarification questions đã answered, cần tạo hoặc cập nhật DDD artifacts theo đúng thứ tự dependency cho một Bounded Context — Domain Map, Glossary, Priority Matrix, Event Storm, Flow Diagrams, Read Model & Query Modeling (read side), Context Map, ADRs, Shared Kernel, Domain Services, README per BC.
version: 3.3
---

# DDD Modeler — Skill Definition

## Mô tả
Skill tạo bộ DDD artifacts chuẩn theo đúng thứ tự dependency. Mỗi artifact tuân theo template từ DDD curriculum (M1-M6) và nguyên tắc OKF (1 file = 1 concept).

## Phase: 3 (Modeling)

## Prerequisite
- Phase 2 DONE: Tất cả P0 questions đã answered
- Discovery outputs có trong `discovery/`

## Artifact Pipeline — Thứ tự bắt buộc

### Step 0: Reference Scan (BẮT BUỘC trước khi bắt đầu)

Scan toàn bộ folder structure của BC đã hoàn thành (Phase trước) để lập checklist:
```bash
find docs/bounded-contexts/<reference-bc> -type f | sort
```
Output = **BC Folder Completeness Checklist** → áp dụng cho mọi BC mới.
**KHÔNG được tạo artifacts mà thiếu bất kỳ loại file nào so với reference BC.**

### Pipeline Steps

```
0. Reference Scan → lập BC Folder Completeness Checklist
     ↓
1. Domain Map → input cho tất cả artifacts khác
     ↓
2. Glossary (atomic files) → shared vocabulary (xem Glossary Type Coverage)
     ↓
3. Domain Priority Matrix → Core/Supporting/Generic
     ↓
4. Event Storm (per Core domain) → process flows
     ↳ Dual-Extraction BẮT BUỘC: mỗi capability trích cả Write-side (Command/Event)
       VÀ Read-side (output Read Model + Projector + Query). KHÔNG chỉ tìm động từ.
     ↓
4.5. Flow Diagrams (zoom-in from Event Storm) → mermaid flowcharts per command
     với rejection paths, policy triggers, read models, color legend
     ↓
4.6. Read Model & Query Modeling (Read Side) → điền section Query Models + Projectors
     trong aggregate-*.md + tạo read-flow `flows/view-*.md` cho mỗi màn hình List/Detail/Report
     ↓
5. Context Map + Integration → boundaries + relationships
     ↓
6. ADRs → key decisions documented
     ↓
6.5. Shared Kernel + Big Picture ES (khi ≥ 2 BCs)
     ↓
7. Domain Services (cross-aggregate logic, nếu có)
     ↓
8. README.md per BC (Domain Tree + File Map + External Dependencies)
     ↓
9. Repository Blueprint → tổng hợp cấu trúc code
```

### Pipeline Step Gate — BẮT BUỘC

**TRƯỚC KHI chuyển sang step tiếp theo, agent PHẢI:**
1. Kiểm tra output của step hiện tại đã tạo ĐÚNG và ĐỦ files
2. Đối chiếu với BC Folder Completeness Checklist
3. Nếu step hiện tại tạo file trong `flows/` → PHẢI có ≥1 flow file + `flows/README.md`
4. Sau Step 4.6: mỗi BC có màn hình List/Detail/Report PHẢI có ≥1 read-flow `flows/view-*.md`, và aggregate-*.md PHẢI có section `## Query Models` + `## Projectors` không rỗng
5. Nếu thiếu → FIX trước khi tiếp tục, KHÔNG được skip

**Anti-pattern 1 (Write-side bias):** Chỉ model Command/Event, bỏ output Read Model + Query + Projector. Read side "tàng hình" → backlog rớt toàn bộ task hiển thị (~40% scope). Đây là căn bệnh phổ biến nhất của Event Storming. Step 4.6 + rule E10/E11 chặn lỗi này.
**Anti-pattern 2:** Nhảy từ Step 4 (Event Storm) sang Step 6 (ADRs) mà bỏ qua Step 4.5 (Flow Diagrams).
**Root cause của anti-pattern:** Agent ưu tiên tốc độ (tạo nhiều artifacts nhanh) hơn completeness; Query là read-only nên không sinh Domain Event → dễ bị lướt qua.

### Step 4.6: Read Model & Query Modeling — chi tiết

Sau khi có Event Storm + command-flows, với MỖI Core Aggregate:
1. **Liệt kê màn hình đọc** từ mockup/screen-registry: List, Detail, Report, Export.
2. **Điền `## Query Models (Output)`**: mỗi màn hình → 1 Query (`Get<Thing>ListQuery`...) với source Read Model, params (filter/sort/paging), access scope (phân quyền data-level).
3. **Điền `## Projectors`**: mỗi output Read Model → Projector nào lắng nghe Event nào để cập nhật.
4. **Cập nhật `## Read Models`**: đánh dấu `Kind = output`, ghi `Projected from Event(s)`.
5. **Tạo read-flow** `flows/view-<thing>-list.md` / `-detail.md`: mermaid thể hiện chuỗi `Screen → Query → Read Model` (không có Domain Event vì là read-only).
6. Chạy validator **E10, E11** (Query/Projector coverage) ngay sau đó.

> Nếu ui-ddd-mapping đã chạy: dùng screen-registry để không sót màn hình đọc. Màn hình có data-table nhưng KHÔNG có `data-command` = read-only view = PHẢI có Query Model tương ứng.

> **Source:** Memo project (2026-07-11) — Agent skipped Step 4.5, Validator (Phase 4) didn't catch vì thiếu V10 rule. Fixed: thêm V10 vào `ddd-validator/rules/structural.md`.
## Artifact Templates — Load on Demand

**KHÔNG load toàn bộ templates/ cùng lúc.** Chỉ load file template cho artifact đang tạo ở bước hiện tại của pipeline.

| Đang tạo... | Load template | File output thật |
|:--|:--|:--|
| Domain Map | `templates/domain-map.md` | `docs/domain-map.md` |
| Glossary term | `templates/glossary-entry.md` | `docs/bounded-contexts/<bc-name>/glossary/<term>.md` |
| Priority Matrix | `templates/priority-matrix.md` | `docs/domain-priority.md` |
| Event Storm | `templates/event-storm.md` | `docs/bounded-contexts/<bc-name>/aggregate-<name>.md` |
| Context Map | `templates/context-map.md` | `docs/context-map.md` |
| ADR | `templates/adr.md` | `docs/bounded-contexts/<bc-name>/decisions/ADR-NNN-<title>.md` |

> `templates/event-storm.md` cũng chứa Event Storm Naming Rules (Event/Command naming, Lifecycle vs Event Group, flow filenames) — đọc kèm khi tạo Event Storm hoặc Flow Diagrams.

## Quy tắc quan trọng
- **OKF Atomic:** Glossary = 1 file per term. KHÔNG gộp.
- **Contextual Bridge (Preventive Rule):** Khi tạo Glossary, KHÔNG được bỏ sót các thực thể thụ động (Passive/Passthrough Reference Entities như Work Order) nếu chúng đóng vai trò là "cầu nối ngữ cảnh" nối giữa các thực thể khác (VD: Contract → WO → SWO). Việc chỉ lọc các thực thể "active" có chứa logic/policy sẽ làm gãy cấu trúc phả hệ (hierarchy) dưới góc nhìn của con người.
- **Alias/Synonym Verification (Preventive Rule):** Khi glossary ghi `Term A (còn gọi là B)` hoặc bất kỳ alias/synonym nào → PHẢI verify bằng **≥ 2 independent sources** (API doc, DB schema, domain story). Meeting notes đơn lẻ KHÔNG đủ để thiết lập alias — 2 concept nằm cạnh nhau trong MoM không có nghĩa chúng equivalent. Nếu chỉ có 1 source → ghi `[UNVERIFIED ALIAS]` và đưa vào Hot Spots. *Ví dụ lỗi: Entity Key bị gán alias MVV vì meeting note ghi "Mã vv → Entity key", nhưng thực tế Entity Key = Company Code (COMPANY_CODE_CRM trong SAP).*
- **Dependency Order:** KHÔNG tạo Event Storm khi chưa có Glossary.
- **Cross-link:** Mọi artifact phải link tới artifacts liên quan.
- **Source tracking:** Mỗi fact ghi rõ nguồn `[SRS §X.Y]` hoặc `[Clarification Q2.3]`.
- **Gate Integration:** Sau khi hoàn thành TẤT CẢ artifacts trong Phase 3 → trigger Gate G3 (Model Review). KHÔNG chuyển sang Phase 4 khi chưa có G3 outcome. Định nghĩa gate + format Gate Review Log: `../_shared/references/gates-and-project-state.md`.
- **BC Ownership Decision Rule (Preventive Rule):** Khi assign concept vào BC, PHẢI check 3 dimensions: (1) **Domain semantics** (tên miền), (2) **UI flow** (user dùng ở đâu), (3) **Integration** (concept tích hợp gì). Nếu 2/3 trỏ về BC khác → ownership = BC đó, không phải BC "nghe giống tên". *Ví dụ lỗi: Prepaid Wallet bị đặt vào Cash Management vì "ví = tiền", nhưng UI + integration đều nằm trong Payment Planning.*
- **BC Completeness:** PHẢI check BC Folder Completeness Checklist trước khi commit. Thiếu bất kỳ loại file nào → fix trước khi chuyển sang BC tiếp.

## BC Folder Completeness Checklist — BẮT BUỘC

Mỗi Bounded Context PHẢI có đầy đủ các artifacts sau. Check TRƯỚC khi commit:

```
docs/bounded-contexts/<bc-name>/
├── README.md                          ← Domain Tree + File Map + External Dependencies
├── aggregate-<name>.md                ← Event Storm (Commands, Events, Policies, Hot Spots)
├── glossary/                          ← 1 file per term (OKF atomic)
│   ├── <entity-terms>.md              ← Entities & Aggregate Roots
│   ├── <process-terms>.md             ← Actions: approve, allocate, write-off...
│   ├── <mechanism-terms>.md           ← Mechanisms: snapshot, sync, lock...
│   ├── <constraint-terms>.md          ← Constraints: ceiling, uniqueness...
│   ├── <value-object-terms>.md        ← Enums & VOs: payment-type, status, bucket...
│   └── <shared-vo-terms>.md           ← Cross-BC VOs: entity-key, payment-term...
├── flows/                             ← Zoom-in flow diagrams from Event Storm
│   ├── README.md                      ← Index: file → scope → commands → refs
│   ├── <process-name>.md             ← Command-flow: Mermaid flowcharts with color legend
│   └── view-<thing>-<list|detail>.md ← Read-flow: Screen → Query → Read Model (bắt buộc nếu có màn hình đọc)
├── decisions/                         ← ADRs (nếu có)
│   └── ADR-NNN-<title>.md
└── domain-services/                   ← Cross-aggregate logic (nếu có)
    └── <service-name>.md
```

## Glossary Type Coverage — BẮT BUỘC

Mỗi BC PHẢI có glossary terms cover **TẤT CẢ loại sau** (không chỉ entities có behavior):

| Loại | Ví dụ Phase 1 | Ví dụ Phase 2 | Bắt buộc |
|:--|:--|:--|:--|
| Entity / Aggregate Root | sales-team, team-member | payment-milestone, invoice | ✅ |
| Reference Entity (Structural) | — | work-order, contract | ✅ (Giữ Contextual Bridge) |
| Process / Action | promote, move, deactivate | write-off, approval-step | ✅ nếu BC có |
| Mechanism | batch-status-derivation | swo-snapshot, sap-sync | ✅ nếu BC có |
| Constraint | warning-flag | contract-ceiling, immutability-lock | ✅ nếu BC có |
| Value Object / Enum | member-status, team-status | payment-type, invoice-type, aging-bucket | ✅ |
| Shared VO (cross-BC) | — | entity-key, payment-term | ✅ nếu cross-BC |
| Role | ams, group-lead, team-lead | — (reuse Phase 1) | Nếu mới |

## Glossary Mandatory Sections — BẮT BUỘC

Glossary = Ubiquitous Language (khái niệm nghiệp vụ), **KHÔNG** phải field catalog / DDL thứ 2.

Mỗi glossary file PHẢI có:

1. **Definition** — Ý nghĩa chính xác của term **trong BC này** (≤ 2 câu)
2. **Bounded Context** — BC nào sở hữu term
3. **Key Attributes** (nếu Entity / Aggregate / VO phức tạp) — **CHỈ** thuộc tính định danh hoặc thay đổi hành vi nghiệp vụ. Heading: `## Thuộc tính quyết định (Key Attributes)`. Bỏ display/audit/UI-only/decorative fields. Mechanism/Process/Constraint/enum đơn giản → **được phép omit** section này.
4. **Rules** — Quy tắc / ranh giới nghiệp vụ quan trọng gắn với term
5. **Lifecycle** (nếu entity có states) — ASCII diagram
6. **Disambiguation** — Phân biệt với concepts hay nhầm (≥ 1–2 entries)
7. **Dangerous Terms ⚠️** — Từ KHÔNG được dùng (≥ 1 entry)
8. **Open Questions ❓** (nếu có) — Resolved hoặc pending

**Anti-pattern:** Liệt kê toàn bộ cột DB, kiểu SQL, bảng UI Detail, hoặc Mutation matrix đầy đủ trong glossary. Schema vật lý thuộc data-model / migrations; glossary chỉ UL.

## Flow Diagram Convention — BẮT BUỘC

Mỗi command trong Event Storm PHẢI có flow diagram tương ứng:

1. **Mermaid flowchart** với `%%{init: {'theme':'dark'}}%%`
2. **Color Legend:** 🔴 Rejection `#ff6b6b`, 🟢 Success `#51cf66`, 🟡 Policy `#ffd43b`, ⭐ Pivotal (viền dày)
3. **Rejection paths:** Mọi command phải có ≥1 rejection path
4. **Read Models:** Actor xem gì trước command (slanted parallelogram node)
5. **Policy triggers:** Sau success event
6. **Validation Notes:** Bảng check E1-E7 cuối file
7. **End-to-End Sequence Diagram:** 1 per flow file (nếu cross-BC)

### Read-Flow Convention (Read Side) — BẮT BUỘC nếu BC có màn hình List/Detail/Report

Mỗi output Query PHẢI có read-flow `flows/view-*.md`:

1. **Mermaid flowchart:** chuỗi `Screen ──► Query ──► Read Model ──► render UI`. KHÔNG có Command/Domain Event (read-only).
2. **Params:** thể hiện filter/sort/paging node nếu có query đa điều kiện.
3. **Access Scope:** node ghi rõ phân quyền data-level (user chỉ thấy data của mình/team/toàn hệ thống).
4. **Projector link:** ghi Read Model này được Projector nào cập nhật từ Event nào (traceability read↔write).

## Validator Integration — Sau mỗi artifact, chạy đúng rules

**Workflow:** Sau khi tạo/sửa artifact → load `ddd-validator` SKILL.md → load ĐÚNG rule file → validate.

| Sau khi tạo... | Load rule file | Chạy rules |
|:--|:--|:--|
| Domain Map | `ddd-validator/rules/strategic-design.md` | S1-S4 |
| Glossary file(s) | `ddd-validator/rules/glossary.md` | G1-G11 |
| Priority Matrix | `ddd-validator/rules/strategic-design.md` | S1-S4 |
| Event Storm | `ddd-validator/rules/event-storm.md` + `aggregate-design.md` | E1-E9 + A1-A4 |
| Query Models + Projectors (Read Side, Step 4.6) | `ddd-validator/rules/event-storm.md` | E10 (Query Coverage) + E11 (Projector Coverage) |
| Context Map | `ddd-validator/rules/context-map.md` | C1-C6 |
| ADR | `ddd-validator/rules/adr.md` | R1-R2 |
| Shared Kernel / Big Picture ES | `ddd-validator/rules/structural.md` | XB-1, XB-2, XB-3 |

**KHÔNG load rule files không liên quan.** VD: tạo glossary → chỉ load `glossary.md`, KHÔNG load `event-storm.md`.

## Late Discovery Handling — Convergence-Aware

Trong quá trình tạo artifacts (đặc biệt Event Storm), có thể phát hiện gaps chưa cover ở Phase 1-2.

**Workflow:**
1. **Phát hiện gap** → đánh giá severity: block artifact hay không?
2. **Ghi vào** `clarification/clarification-questions.md` section `## Late Discoveries`
3. **Format:** `[LATE-P0/P1/P2]` + `Discovered during: [artifact name]`
4. **Nếu LATE-P0:** Pause artifact hiện tại, đợi stakeholder trả lời
5. **Nếu LATE-P1/P2:** Ghi assumption trực tiếp trong artifact, đánh dấu `[ASSUMPTION — pending QL-XX]`, tiếp tục viết

**Revision Trigger:**
Khi Late Discovery ảnh hưởng artifact ĐÃ TẠO:
1. Ghi Revision Trigger: `[REV-TRIGGER] Artifact X cần update vì: [lý do]`
2. Nếu artifact upstream (Glossary, Domain Map) → **sửa ngay trước khi tiếp tục downstream**
3. Nếu artifact cùng level (Event Storm khác) → ghi nhận, sửa sau khi hoàn thành artifact hiện tại

**KHÔNG reset Phase state.** Phase 2 vẫn là DONE. Late Discoveries + Revision Triggers là append-only log.
