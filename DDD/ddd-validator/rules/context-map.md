---
category: Context Map
rules: C1-C6
applies_to: [docs/context-map.md]
sources: [Lesson 5.2, Lesson 5.3]
merged_from: [V3 Context Boundary Consistency]
---
# Context Map Rules (C1-C6)

### C1: Mỗi cặp BC phải có Integration Pattern
- **Nguồn:** Lesson 5.2 — *"Mỗi cặp BC PHẢI có integration pattern rõ ràng"*
- **Merged from:** V3 (Context Boundary Consistency)
- **7 patterns:** Partnership, Shared Kernel, Customer-Supplier, Conformist, ACL, OHS, Published Language
- **Checklist:**
  - [ ] Mỗi relationship ghi rõ pattern name?
  - [ ] Pattern name đúng DDD definition?
  - [ ] Mỗi context có ≥1 relationship (không orphan)?

### C2: Conformist = Downstream HOÀN TOÀN theo Upstream
- **Nguồn:** Lesson 5.2 — *"Downstream chấp nhận model upstream, không fight"*
- **Checklist:**
  - [ ] Downstream thực sự dùng upstream model as-is?
  - [ ] Nếu downstream translate/rename → clarify scope (display-only vs model-level)?
  - [ ] Nếu model-level translation → reclassify to Customer-Supplier or ACL?

### C3: ACL = Translation Layer bảo vệ Domain Model
- **Nguồn:** Lesson 5.2/5.3 — *"ACL bảo vệ domain model. Nếu SAP đổi API → chỉ sửa ACL"*
- **Checklist:**
  - [ ] ACL relationship có Vocabulary Translation table?
  - [ ] Translation table cover ALL shared terms (structural + employee + events)?
  - [ ] Kafka/async event format mapping documented?

### C4: OHS = Public API cho N Consumers
- **Nguồn:** Lesson 5.2 — *"Upstream expose API cho N consumers"*
- **Decision guide:**
  - 1 consumer → Customer-Supplier
  - N consumers + stable API → OHS + Published Language
- **Checklist:**
  - [ ] OHS relationship has >1 consumer? If not → reclassify or add future-proofing rationale?
  - [ ] Published Language (schema versioning) documented?

### C5: Upstream/Downstream Direction nhất quán
- **Nguồn:** Lesson 5.2 — *"Upstream = cung cấp data, có power. Downstream = tiêu thụ, thích nghi"*
- **Checklist:**
  - [ ] Diagram labels match relationships table?
  - [ ] Each relationship clearly states who is U and who is D?
  - [ ] Pattern name attributed to correct side (Conformist = Downstream behavior, ACL = Downstream builds)?

### C6: BC Ownership Evidence — assignment phải có evidence, không chỉ dựa tên
- **Nguồn:** Review Correction Log #7 (2026-07-09) — Agent đặt Prepaid Wallet vào Cash Management BC vì "ví = quản lý tiền". Thực tế thuộc Payment Planning BC vì toàn bộ logic diễn ra trên UI lập kế hoạch.
- **Tại sao:** BC assignment chỉ dựa vào "tên miền nghe giống" → concept bị đặt sai chỗ → team sai own concept → integration overhead, code ở sai module, khó maintain.
- **3 Dimensions kiểm tra:**
  1. **Domain Semantics** — concept thuộc miền nghiệp vụ nào theo định nghĩa?
  2. **UI Flow** — user tương tác với concept này trên màn hình/module nào?
  3. **Integration** — concept tích hợp chặt với BC nào (shared transactions, same aggregate)?
- **Checklist:**
  - [ ] Mỗi concept assignment vào BC có ≥1 evidence: UI screen, integration point, hoặc domain expert confirmation?
  - [ ] Nếu 2/3 dimensions trỏ về BC khác với BC được assign → flag 🟠 cần review?
  - [ ] Concept không có UI riêng (no dedicated screen/module) → thuộc BC chứa UI chính mà nó xuất hiện?
  - [ ] Assignment KHÔNG chỉ dựa trên "tên miền nghe giống" mà thiếu evidence từ dimensions khác?
- **Ví dụ lỗi:** *Prepaid Wallet (Ví AV/DP) bị đặt vào Cash Management vì "ví → tiền → Cash Management". Nhưng: (1) UI: user thao tác ví trên màn hình Payment Planning, (2) Integration: logic tạo ADAV + cấn trừ nằm trong Payment Planning aggregate, (3) Cash Management chỉ có Import Bank Transaction + Payment Allocation. 2/3 dimensions → Payment Planning.*
