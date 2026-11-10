---
name: ddd-discovery
description: "Dùng ở Phase 0-1 khi nhận tài liệu đầu vào mới (SRS, meeting notes, RFP) và cần intake/classify + extract domain knowledge có hệ thống qua 4-lens analysis (Value Chain, Organizational, System Inventory, Pain Point). Output: intake-summary, value-chain, stakeholder-map, system-inventory, pain-points, domain-map-draft."
version: 1.3
---

# DDD Discovery — Skill Definition

## Mô tả
Skill nhận tài liệu đầu bài (SRS, meeting notes, RFP) và extract domain knowledge có hệ thống qua 4 lenses. Output = Discovery Summary + Draft Domain Map.

## Phase: 0 (Intake) + 1 (Discovery)

## Workflow Phase 0: Intake — Nhận & Classify

1. **Đọc toàn bộ tài liệu** trong `input/`
2. **Classify document type:** SRS, BRD, meeting notes, email, RFP...
3. **Extract metadata:**
   - Tên dự án, version, tác giả
   - Scope (in-scope vs out-of-scope)
   - Tech stack, constraints
   - Systems liên quan
4. **Tạo `discovery/intake-summary.md`:**
   - Document classification
   - Key metadata extracted
   - Estimated complexity (S/M/L/XL)
   - Identified gaps cần đào sâu

## Workflow Phase 1: Discovery — 4-Lens Analysis

### Lens 1: Value Chain Analysis
- Tìm dòng chảy giá trị chính trong tài liệu
- Identify: trigger → process steps → outcome
- Output: Value chain diagram (text-based)

### Lens 2: Organizational Analysis
- Extract tổ chức: departments, roles, reporting lines
- Map: role → domain ownership
- **Map: UI screen/module → domain ownership** — concept được thao tác trên UI nào? Concept không có UI riêng → thuộc BC chứa UI chính mà nó xuất hiện.
- Flag: roles mentioned but unclear ownership
- Flag: concepts xuất hiện trên UI của module khác (cross-BC candidate)

### Lens 3: System Inventory
- Liệt kê mọi system/tool được nhắc đến
- Map: system → domain → users
- Flag: domains chưa có tool (gap), domains share tool (coupling)

### Lens 4: Pain Point Mining
- Extract mọi vấn đề, pain points, requirements
- **PHẢI quantify:** tiền, thời gian, % sai — lấy từ document hoặc đánh dấu `[NEEDS QUANTIFICATION]`
- Đếm frequency: domain nào xuất hiện nhiều nhất = Core candidate

## Output Files

| File | Nội dung |
|:--|:--|
| `discovery/intake-summary.md` | Metadata, classification, gaps |
| `discovery/value-chain.md` | Dòng chảy giá trị chính |
| `discovery/stakeholder-map.md` | Roles, departments, ownership |
| `discovery/system-inventory.md` | Tools, integrations, gaps |
| `discovery/pain-points.md` | Problems + quantified impact |
| `discovery/domain-map-draft.md` | Draft Domain Map (sẽ refine ở Phase 3) |

## Key Rule: Extract vs Infer

```
Mọi thông tin trong output PHẢI được tag:

[EXTRACTED] — trích trực tiếp từ tài liệu (có line reference)
[INFERRED]  — suy luận từ context (cần confirm với user)

Ví dụ:
- [EXTRACTED] POA handles authentication (SRS §3.1)
- [INFERRED] HR Department là upstream của Resource Management (không nêu rõ trong SRS)
```

## Key Rule: Enum Counting Gate — BẮT BUỘC

Khi tài liệu liệt kê ≥3 giá trị enum (types, categories, statuses, roles):
1. **Đếm rõ ràng** từng giá trị, liệt kê tên từng cái
2. **KHÔNG gộp** 2 values có tên khác nhau trừ khi có ≥2 sources xác nhận chúng là alias
3. **Đánh dấu** `[ENUM-COUNT: N values]` trong output
4. Nếu 2 values "nghe giống nhau" nhưng tên khác → giữ riêng, đưa vào `[INFERRED]` để clarify

```
❌ SAI: Đọc ADAV và ADRR → gộp thành "Advance Deduction" → đếm 6 loại
✅ ĐÚNG: Liệt kê: RRTM, RRFP, AV, ADAV, ADRR, RRC, DP → đếm 7 loại [ENUM-COUNT: 7 values]
```

## Key Rule: Anti-Single-Write Assumption — BẮT BUỘC

Khi extract attribute có giá trị phụ thuộc vào lifecycle (dates, amounts, statuses, rates):
1. **KHÔNG giả định** attribute được set 1 lần rồi không đổi
2. **Đánh dấu** `[MUTATION-CHECK NEEDED]` và chuyển sang clarification queue
3. Chỉ được ghi `single-write` khi domain expert xác nhận

```
❌ SAI: duedate được set khi gắn Invoice → giữ nguyên (đoán là single-write)
✅ ĐÚNG: duedate [MUTATION-CHECK NEEDED] → hỏi domain expert → phát hiện: null → tạm tính → final khi SENT
```

## Key Rule: Meeting Notes Cross-Reference — BẮT BUỘC

Meeting notes (MoM) là nguồn **phi cấu trúc** — viết tắt, mơ hồ, dùng ngôn ngữ nói. Khi extract facts từ meeting notes, agent PHẢI tuân thủ:

### 1. Cross-Reference Gate
Khi extract relationship hoặc định nghĩa từ meeting notes → **BẮT BUỘC cross-reference với ≥ 1 nguồn có cấu trúc** (API doc, DB schema, domain story, knowledge map) TRƯỚC khi ghi vào discovery output.

```
❌ SAI: Đọc "Mã vv → Entity key" trong MoM → kết luận Entity Key = MVV
✅ ĐÚNG: Đọc "Mã vv → Entity key" → check API doc → thấy Entity Key = COMPANY_CODE_CRM → Entity Key ≠ MVV
```

### 2. Alias Verification Gate
Khi gán alias/synonym `A (B)` hoặc `A — còn gọi là B`:
- **≥ 2 independent sources** xác nhận A = B → ghi `[VERIFIED ALIAS]`
- **Chỉ 1 source** (đặc biệt meeting notes) → ghi `[UNVERIFIED ALIAS — cần confirm]` và đưa vào clarification queue
- **0 source khác confirm** → KHÔNG ghi alias, đưa vào `[INFERRED]` items

### 3. Proximity Trap Warning
Hai concept nằm **cạnh nhau** trong meeting notes KHÔNG có nghĩa chúng equivalent. Trước khi ghép:
- Check xem chúng có cùng data type/semantic không
- Check DB schema xem chúng có map cùng column không
- Check API doc xem chúng có cùng field không

## Key Rule: BC Validation Gate — BẮT BUỘC (v1.2)

Khi tạo `domain-map-draft.md`, agent PHẢI validate mỗi BC candidate trước khi ghi vào output:

### 1. 6-Criteria Scoring
Chấm mỗi BC theo 6 tiêu chí (thang 1-5):
- **H1: Linguistic Boundary** — Có Ubiquitous Language riêng?
- **H2: Business Capability** — Map đúng 1 business capability?
- **H3: Data Ownership** — Own data riêng?
- **H4: Team/Org Alignment** — Phù hợp team structure?
- **H5: Independent Lifecycle** — Entities có lifecycle riêng?
- **H6: Invariant Cohesion** — Business rules thuộc cùng nhóm?

**Threshold**: BC trung bình ≥ 3.5 → giữ. BC < 3.0 → xem xét gộp/hạ cấp.

### 2. Classification Gate
Mỗi "vùng" phải được phân loại chính xác:

| Loại | Khi nào | Label trên Domain Map |
|:-----|:--------|:----------------------|
| **True BC** | Có domain model, entities, aggregates, business rules riêng | `BC-N: [Name] Context` |
| **Integration Adapter** | Chỉ consume/push data từ external system, không có domain logic | `«External» [Name] Gateway` |
| **Shared Kernel** | Lookup tables, validation utils dùng chung | `Shared Kernel: [Name]` |
| **Infrastructure Service** | Side-effect (email, logging), không thay đổi domain state | `Infrastructure: [Name] Service` |

### 3. Anti-patterns (TRÁNH)
```
❌ Notification = BC       → Notification là infrastructure, domain logic (auto-sent) phải ở domain BC
❌ Approval = riêng BC     → Nếu chỉ 1 entity cần + steps hardcoded → gộp vào entity BC
❌ Master Data = BC         → Lookup tables = Shared Kernel
❌ External System = "BC"   → Adapter không có model riêng
```

### 4. Freeze Timing Gate
Khi extract "đóng băng / chặn sửa / immutable" rules:
1. **Hỏi rõ trigger point chính xác** — KHÔNG giả định
2. Ví dụ: "Invoice đóng băng" → **khi Submit** (Pending) hay **khi Approved**?
3. Đánh dấu `[FREEZE-POINT: ?]` nếu chưa rõ → đưa vào clarification queue

## Sau khi hoàn thành
- Cập nhật `project-state.md`: Phase 0-1 → DONE (template: `../_shared/references/gates-and-project-state.md`)
- Liệt kê `[INFERRED]` items → chuyển sang Phase 2 (clarification queue)
- Đề xuất chạy `ddd-questioner` skill

