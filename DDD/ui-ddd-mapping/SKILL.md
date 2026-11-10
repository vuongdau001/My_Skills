---
name: ui-ddd-mapping
description: "Dùng khi cần mapping mockup UI/UX vào DDD artifacts (enrichment flow diagrams, aggregate UI Mapping, screen registry) — áp dụng Hybrid SCEB methodology. Kích hoạt khi tạo UI Context, gắn Screen ID, enrich flow, hoặc phát hiện gap giữa mockup và DDD. Là mandatory gate trước ddd-backlog-planner: phát hiện screen read-only thiếu Query Model (chống Write-side bias), làm nguồn cho validator V12. Tham chiếu references/ui-ux-domain-integration.md."
version: 1.1
---

# Hybrid SCEB — UI ↔ DDD Mapping Skill

> **Mandatory Gate (khi dự án có mockup/UI):** Skill này PHẢI chạy xong TRƯỚC ddd-backlog-planner (pre-check 4). Nó là gap-detector cuối cùng đối chiếu mockup thực tế với DDD Core để bắt Read Model bị bỏ sót — chống Write-side bias. Validator rule V12 (Screen ↔ Command/Query Coverage) dựa trên output của skill này.

## Khi nào kích hoạt

- Người dùng muốn "mapping mockup vào DDD"
- Tạo hoặc sửa `## UI Context (Brandolini Design-Level)` trong flow files
- Thêm `## UI Mapping` section vào aggregate files
- Gắn `data-command`, `data-screen-id` vào HTML mockup files
- Phát hiện gap giữa Screen và Command
- Nhận mockup mới cần tracking

## Methodology Reference

Đọc file methodology đầy đủ (load khi cần chi tiết lý thuyết / ví dụ): `references/ui-ux-domain-integration.md`

## Quy Tắc Bắt Buộc

### 1. Không Dùng Viết Tắt

Luôn viết đầy đủ kèm viết tắt trong ngoặc ở lần đầu xuất hiện. Bảng viết tắt lấy từ glossary/stakeholder-map của dự án; bảng dưới là **worked example (CRM)**:

| Viết tắt | Phải viết |
|:---------|:----------|
| AM | Account Manager (AM) |
| KT | Kế toán (KT) |
| KTT | Kế toán trưởng (KTT) |
| KTV | Kế toán viên (KTV) |
| PM | Payment Milestone |
| PM Detail | Payment Milestone Detail |
| DP | Deposit |
| AV | Advance |
| GL | Group Lead |
| DU | Delivery Unit |

### 2. Không Thêm Examples/Specification by Example

KHÔNG thêm Given/When/Then examples vào flow files. Mermaid flowcharts đã thể hiện đầy đủ happy path + rejection paths. Examples thuộc về phase Backlog Generation.

### 3. Mermaid Diamond Nodes PHẢI Quote

```
❌ CMD --> ST{PM status = NEW?}
✅ CMD --> ST{"PM status = NEW?"}
```

Quote TẤT CẢ diamond labels — kể cả khi label đơn giản. Ký tự nguy hiểm: `(`, `)`, `>`, `∈`, `≥`, `*`, `-` trong prefix.

### 4. Relative Path Convention

Mockup đặt tại `input/mockups/` (layout generic; CRM dùng `phase-2/input/mockups_<ddmmyyyy>/`).

Từ flow files (depth 4: `docs/bounded-contexts/{bc}/flows/*.md`):
```
../../../../input/mockups/{filename}.html
```

Từ aggregate files (depth 3: `docs/bounded-contexts/{bc}/*.md`):
```
../../../input/mockups/{filename}.html
```

### 5. Screen Reference PHẢI Có Link

```markdown
| Screen | **SCR-B02** ([Create_payment_milestone.html](../../../../input/mockups/Create_payment_milestone.html)) |
```

KHÔNG viết chỉ `| Screen | SCR-B02 |` — thiếu clickable link.

## Quick Reference: Top-Down vs Bottom-Up

- **Top-Down (UI → Domain):** UI Mockup → Trích xuất Data/Actions → Map vào Glossary/Command → Phát hiện Gap
- **Bottom-Up (Domain → UI):** Domain Change → Xem xét ảnh hưởng UI (New form? New fields? Validation message?)

## Quick Reference: Mapping Patterns

| UI Component | Domain Primitive |
|:--|:--|
| Form + Submit button | Command |
| Data table | Read Model |
| Status badge | Value Object (enum) |
| Validation error | Precondition/Invariant violation |

## Quick Reference: Read Model

Read Model là "Query side" — mô tả data cần để render UI. Mỗi BC có catalog riêng. Event Storm Command có cột `Read Model` reference (input), và section `## Query Models (Output)` + `## Projectors` cho read side.

## Read-Only Screen Detection (BẮT BUỘC — bắt Read Model bị bỏ sót)

Khi annotate/mapping, mỗi screen PHẢI rơi vào 1 trong 2 loại:

| Dấu hiệu trên mockup | Loại | Yêu cầu DDD |
|:--|:--|:--|
| Form + Submit button (`data-command`) | Write screen | PHẢI có Command trong aggregate |
| Data table / detail card / report / export, KHÔNG có `data-command` | **Read-only screen** | PHẢI có **Query Model (output)** trong aggregate `## Query Models` |

**Quy tắc:** Screen read-only mà aggregate KHÔNG có Query Model tương ứng = **gap read side** → tạo Late Discovery `[LATE-P1] LD-nn: Missing Query <GetXListQuery>` và ghi vào Gap Detection. Đây chính là loại gap khiến backlog rớt ~40% scope hiển thị (Sprint Plan Coverage review). Filter/sort/paging/phân quyền data trên table = params của Query, phải ghi rõ.

## Quick Reference: AI Prompt (Wireframe → Screen Spec)

```
[Đây là wireframe...]
1. Liệt kê data fields
2. Map vào Glossary
3. Liệt kê actions → map vào Commands
4. Lên danh sách validation rules → map BRs
5. Tạo Screen Spec markdown
6. Highlight domain gaps
```

## Template: UI Context Table

```markdown
## UI Context (Brandolini Design-Level)

| Attribute | Value |
|:----------|:------|
| Screen | **SCR-{id}** ([{filename}.html]({relative-path})) |
| Entry Point | SCR-{parent} ({Parent Screen Name}) → Click "{Button}" button |
| Actor | {Full Name} ({Abbreviation}) |
| Form Fields | {Field1} (type), {Field2} (type), ... |
| Success Action | Redirect → SCR-{target} ({Target Screen Name}) + Toast "{message}" |
| Error Action | Inline validation messages per field |
| Pre-load Data | {Data Source 1}, {Data Source 2} |
| Conditional UI | If {condition} → {UI change} |
```

**Lưu ý**:
- `Conditional UI` chỉ thêm khi có logic UI phức tạp (enable/disable fields, show/hide sections)
- `Pre-load Data` chỉ thêm khi screen cần load data từ API trước khi render

## Template: Aggregate UI Mapping

```markdown
## UI Mapping

| Command | Screen | Trigger UI Element | Notes |
|:--------|:-------|:-------------------|:------|
| {CommandName} | SCR-{id} | {Button/Form/Link} | {Description} |

| Read Model | Screen | Fields Displayed |
|:-----------|:-------|:-----------------|
| {ReadModelName} | SCR-{id} | {field1}, {field2}, ... |
```

## Template: Late Discovery Entry

```markdown
## [LATE-{Priority}] LD-{nn}: {Title}

| Attribute | Value |
|:----------|:------|
| Discovered during | UI Mapping — {aggregate} × SCR-{id} |
| Screen | SCR-{id} ([{filename}.html]({path})) |
| Aggregate | {BC} / {Aggregate} |
| Issue | {Mô tả gap} |
| Impact | {Ảnh hưởng nếu không fix} |
| Options | **A**: ... **B**: ... |
| Action needed | ❓ Clarify với BA/PO |
```

## Quy Trình 6 Bước

1. **Screen Inventory** → `mapping/screen-registry.md`
2. **Enrich DDD Artifacts** → UI Context + Mermaid trong flows, UI Mapping trong aggregates
2b. **Annotate HTML Mockups** → Gắn `data-screen-id`, `data-command`, `data-navigate` vào mockup HTML. Nếu phát hiện Late Discovery → thực hiện ngay bước 3.
3. **Gap Detection** → `mapping/late-discoveries.md` + cập nhật `screen-registry.md` phần Gap Detection. **Bắt buộc** khi bước 2b phát hiện command thiếu flow file.
4. **Review & Cleanup** → Viết tắt, Mermaid quotes, paths, annotations
5. **Change Tracking** → `mapping/mockup-changelog.md`

## HTML Annotation Convention

### 3 Attributes duy nhất

| Attribute | Gắn vào | Giá trị | Mục đích |
|:----------|:--------|:--------|:---------|
| `data-screen-id` | Root `<div>` của page | `SCR-B05` | Identify screen — 1 per page |
| `data-command` | `<button>`, `<form>` submit | `AddPaymentItem` | Map trigger → DDD command |
| `data-navigate` | `<a>`, `<button>` navigation | `SCR-B04` | Map navigation → target screen |

### Template

```html
<!-- Root container — PHẢI có data-screen-id -->
<div data-screen-id="SCR-{id}">

  <!-- Action button — gắn data-command = DDD command name -->
  <button data-testid="btn-{action}-{entity}" 
          data-command="{CommandName}">
    {Button Label}
  </button>

  <!-- Navigation — gắn data-navigate = target screen ID -->
  <a data-testid="link-{description}"
     data-navigate="SCR-{target-id}">
    {Link Label}
  </a>

</div>
```

### Quy tắc

1. `data-command` value = **exact DDD command name** từ aggregate (PascalCase, ví dụ `AddPaymentItem`)
2. `data-screen-id` value = **exact Screen ID** từ screen-registry.md
3. `data-navigate` value = **exact Screen ID** của target screen
4. **KHÔNG sửa** layout, style, hoặc nội dung hiển thị mockup — chỉ thêm attributes
5. **KHÔNG thêm** `data-event`, `data-policy`, `data-aggregate`, `data-validation` — quá chi tiết
6. Mỗi page chỉ có **1** `data-screen-id` trên root container
7. Mỗi button chỉ có **1** `data-command` (nếu button trigger 1 command duy nhất)
8. Nếu button mở dialog confirm → `data-command` vẫn gắn trên button ban đầu, không phải confirm button

### Late Discovery trong bước Annotate

Khi bước 2b phát hiện `data-command` không có flow file tương ứng trong DDD:

1. **HTML**: Gắn `data-command="{CommandName}"` + chèn `<!-- LD-{nn} pending -->` ngay trước element
2. **late-discoveries.md**: PHẢI tạo/cập nhật entry theo template `[LATE-{Priority}] LD-{nn}` — bao gồm: Issue, Impact, Options, Action needed
3. **screen-registry.md**: PHẢI cập nhật phần "Gap Detection > GAP-A" với entry tương ứng
4. **Báo cáo hoàn thành**: PHẢI liệt kê danh sách LD kèm link đến `late-discoveries.md`, KHÔNG chỉ đề cập comment HTML

> **Quy tắc**: Comment `<!-- LD-xx -->` trong HTML là shortcut cho grep. Tài liệu chính thức là `late-discoveries.md`. Nếu chỉ có comment HTML mà thiếu entry trong `late-discoveries.md` = CHƯA HOÀN THÀNH bước Gap Detection.

### Ranh giới — KHÔNG annotate

- ❌ `data-event` — Events thuộc về aggregate/flow docs
- ❌ `data-policy` — Policies thuộc về aggregate/flow docs  
- ❌ `data-aggregate` — Quá chi tiết, gây coupling
- ❌ `data-validation` — Validation rules thuộc về flow docs

## Mermaid Color Palette

| Ý nghĩa | Hex | Style directive |
|:---------|:----|:----------------|
| Rejection | `#ff6b6b` | `style R1 fill:#ff6b6b,color:#fff` |
| Success Event | `#51cf66` | `style EVT fill:#51cf66,color:#fff` |
| Pivotal Event | `#51cf66` + border | `style EVT fill:#51cf66,stroke:#fff,stroke-width:3px,color:#fff` |
| Policy | `#ffd43b` | `style POL fill:#ffd43b,color:#333` |
| Branching/Logic | `#4dabf7` | `style LOGIC fill:#4dabf7,color:#fff` |
| System Trigger | `#4dabf7` | `style CRON fill:#4dabf7,color:#fff` |

## File Map

```
input/
└── mockups/                    ← Layer 4: HTML files với data-* annotations
mapping/
├── screen-registry.md          ← Layer 1: Screen catalog
├── late-discoveries.md         ← Layer 5: Gap log
└── mockup-changelog.md         ← Layer 6: Change tracking

docs/bounded-contexts/{bc}/
├── aggregate-*.md              ← Layer 2: UI Mapping section (cuối file)
└── flows/*.md                  ← Layer 3: UI Context table + Mermaid flowchart

.agents/skills/ui-ddd-mapping/references/
└── ui-ux-domain-integration.md ← Methodology onboarding guide (đi kèm skill)
```
