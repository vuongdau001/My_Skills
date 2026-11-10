---
category: Glossary
rules: G1-G11
applies_to: [docs/bounded-contexts/*/glossary/*.md]
sources: [Lesson 2.2, Lesson 2.3, Lesson 7.1]
merged_from: [V1 Glossary Coverage, V6 Conflict Check]
---
# Glossary Rules (G1-G11)

### G1: Glossary Entry tập trung Ubiquitous Language (không phải field catalog)
- **Nguồn:** Lesson 2.3 + convention 2026-08-10 — Glossary định nghĩa khái niệm trong BC, không liệt kê đủ schema/UI fields.
- **Phần cốt lõi:** Definition, Bounded Context, Business Rules, Key Attributes (nếu có), States (nếu có), Phân biệt với, Đồng nghĩa nguy hiểm, Câu hỏi mở (nếu còn)
- **Key Attributes:** CHỈ thuộc tính định danh HOẶC thay đổi hành vi nghiệp vụ. Cấm full attribute dump, UI field list, SQL types, Physical ERD mapping.
- **Mechanism / Process / Constraint / Enum đơn giản:** có thể KHÔNG có Key Attributes nếu Rules (+ Enum Values / Lifecycle) đủ.
- **Tại sao:** Field catalog làm glossary thành DDL thứ 2 → UL bị loãng; thiếu Definition/Rules → Dev A/B đặt tên khác nhau.
- **Checklist cho MỖI file:**
  - [ ] Definition ≤ 2 câu, rõ ràng trong BC này?
  - [ ] Ghi rõ Bounded Context?
  - [ ] Key Attributes (nếu Entity/Aggregate/VO phức tạp) — chỉ identity / behavior-changing; KHÔNG ≥-require đủ 4 attrs tùy tiện?
  - [ ] KHÔNG có bảng Attributes kiểu DDL (VARCHAR/DECIMAL/FK) hoặc UI column dump?
  - [ ] Business Rules (≥2, trừ term thuần định nghĩa)?
  - [ ] States/Lifecycle (nếu Entity có states)?
  - [ ] "Phân biệt với" (≥1 term dễ nhầm)?
  - [ ] "Đồng nghĩa nguy hiểm" (≥1 term KHÔNG dùng)?
  - [ ] Câu hỏi mở (nếu còn)?

### G2: DDD Taxonomy chính xác
- **Nguồn:** Lesson 7.1 — *"Entity = identity + lifecycle; Value Object = immutable + value equality"*
- **Tại sao:** Classify sai → design sai. Skill có ID = DB bloat.
- **Checklist:**
  - [ ] `type` field thuộc taxonomy chuẩn (đồng bộ với `ddd-modeler/templates/glossary-entry.md`): entity / aggregate-root / value-object / enum / status / role / role-variant / process / mechanism / constraint / domain-service?
  - [ ] Entity thỏa 3 tiêu chí: Distinguish, Lifecycle, Tracking?
  - [ ] Value Object thỏa: Equality, Immutable, No lifecycle?
  - [ ] Aggregate Root ghi rõ invariants nào nó gác cổng?

### G3: Conflict Severity cho multi-context terms
- **Nguồn:** Lesson 2.2 — *"Cùng từ 'Khách hàng' — Sales nghĩ Account, Finance nghĩ Payer → vỡ nếu gộp"*
- **Merged from:** V6 (Glossary Conflict Check)
- **Checklist:**
  - [ ] Term >1 context có `conflict_severity` rating?
  - [ ] Per-Context Meaning section giải thích khác biệt?

### G4: Glossary Coverage — mọi domain term phải có file
- **Nguồn:** Lesson 2.3 + V1 (Glossary Coverage)
- **Merged from:** V1 (Glossary Coverage)
- **Checklist:**
  - [ ] Scan Domain Map → mỗi term có glossary file?
  - [ ] Scan Event Storm → Commands/Events dùng terms nào → covered?
  - [ ] Scan Context Map → vocabulary translation terms → covered?

### G5: Industry Standard Lens — thuật ngữ phổ biến phải có context ngành
- **Nguồn:** Session review 2026-07-09 — Payment Term, Contract, Milestone chỉ viết từ góc nhìn nội bộ, người đọc mới không biết đây là concept chung hay riêng của công ty.
- **Tại sao:** Glossary không có Industry Standard context → developer/BA mới vào tưởng đây là concept "tự chế" của dự án → sai thiết kế khi tích hợp với hệ thống chuẩn (SAP, ERP). Đồng thời, việc dẫn nguồn tiêu chuẩn giúp tăng độ tin cậy cho tài liệu.
- **Áp dụng khi:** Term thuộc loại Entity, Aggregate Root, Value Object, hoặc Reference Entity **VÀ** là khái niệm phổ biến trong ngành (VD: Invoice, Contract, Payment Term, Work Order, Milestone, Currency, PO...).
- **Checklist:**
  - [ ] Có section **"Tiêu chuẩn ngành (Industry Standard)"** trong Definition?
  - [ ] Section đó giải thích term được hiểu thế nào trong ngành (B2B, ERP, Accounting...)?
  - [ ] Có section **"Trong [Dự án / Phase]"** (VD: "Trong CRM Phase 2") phân biệt rõ cách áp dụng nội bộ so với chuẩn chung?
  - [ ] Nếu cách dùng nội bộ KHÁC chuẩn chung → giải thích rõ lý do tại sao?

### G6: Inline Citation Enforcement — mô tả nội bộ dự án phải có nguồn
- **Nguồn:** Session review 2026-07-09 — Các câu mô tả logic CRM Phase 2 trong Payment Term, Contract, SWO thiếu hoàn toàn inline citation → không thể truy vết nguồn gốc.
- **Tại sao:** Câu mô tả không có citation = không ai biết nó lấy từ đâu → khi business thay đổi, không biết cập nhật chỗ nào → document rot.
- **Checklist:**
  - [ ] Mọi câu trong section **"Trong [Dự án / Phase]"** có ≥1 inline citation?
  - [ ] Citation đúng format: `[SOURCE: file.md:Lxx]`, `[CLARIFIED: CQ-xx]`, hoặc `[ASSUMED: CQ-xx]`?
  - [ ] Không có câu mô tả logic/rule mà thiếu citation?

### G7: Single Responsibility per Term — không định nghĩa lại term khác
- **Nguồn:** Session review 2026-07-09 — sub-work-order.md tự định nghĩa cả Work Order bên trong mình → overlap, risk mâu thuẫn khi update.
- **Tại sao:** Nếu Term A chứa định nghĩa của Term B → khi B thay đổi, phải sửa cả file A lẫn file B → dễ bỏ sót, gây mâu thuẫn (Ubiquitous Language drift).
- **Checklist:**
  - [ ] File chỉ định nghĩa DUY NHẤT term trong frontmatter `term:` field?
  - [ ] Không có đoạn giải thích chi tiết term khác (> 1 câu) trong Definition?
  - [ ] Nếu cần so sánh → dùng bảng **Disambiguation** với cross-link, không giải thích inline?

### G8: Open Question Guard — conflict chưa resolve không được viết như fact
- **Nguồn:** Session review 2026-07-09 — Payment Term viết "Lấy từ Project Code, không phải Contract" như fact đã chốt, trong khi VL-3 vẫn là open question trong discovery (worked example CRM: `knowledge-map.md`).
- **Tại sao:** Viết open question thành fact → downstream (Event Storm, Code) build trên giả định chưa confirm → rất khó phát hiện lỗi sau này.
- **Checklist:**
  - [ ] Scan Open Questions trong discovery + `clarification/clarification-questions.md` (`VL-x`, `AQ-x`, `OQ-x`, `Qx.y`, `QL-xx`) → term có liên quan?
  - [ ] Nếu có open question liên quan → BẮT BUỘC ghi vào section **"Câu hỏi mở ❓"** với tag `[⚠️ VALIDATE]`?
  - [ ] Nội dung Definition/Rules KHÔNG viết phía bị conflict như fact đã chốt?
  - [ ] Nếu chọn 1 phía → ghi rõ "đây là assumption, chưa confirmed" + dẫn nguồn conflict?

### G9: Contextual Bridge Coverage — không bỏ sót entity cầu nối
- **Nguồn:** Session review 2026-07-09 — Work Order bị bỏ sót khỏi glossary vì không chứa logic/policy, nhưng nó là cầu nối giữa Contract và SWO trong hierarchy.
- **Tại sao:** Chỉ lọc entity "active" (có behavior) → gãy phả hệ ngữ nghĩa → người đọc không hiểu luồng dữ liệu Contract → ? → SWO.
- **Checklist:**
  - [ ] Scan entity list trong discovery outputs (`discovery/system-inventory.md`, `discovery/domain-map-draft.md`) → mọi Reference Entity có glossary file?
  - [ ] Kiểm tra hierarchy: nếu A → B → C mà B thiếu glossary → FAIL?
  - [ ] Entity thụ động (passive/passthrough) vẫn phải có glossary nếu nó nối 2 entity khác?

### G10: Enum Value Completeness — đếm đúng, không gộp
- **Nguồn:** Review Correction Log #2 (2026-07-09) — Agent gộp ADAV và ADRR thành 1, chỉ đếm 6 loại Payment Item thay vì 7 loại độc lập.
- **Tại sao:** Gộp nhầm enum values → schema sai, code thiếu case handling → runtime errors khi gặp value bị bỏ sót. Enum là "contract" cứng giữa Business và Tech — sai 1 value = sai cả flow.
- **Áp dụng khi:** Glossary file có `type: value-object` hoặc `type: enum` hoặc Attributes có cột liệt kê enum values.
- **Checklist:**
  - [ ] Đếm số values liệt kê trong glossary → khớp với nguồn gốc (SRS, MoM, domain expert)?
  - [ ] Mỗi value có tên **riêng biệt** → KHÔNG được gộp 2 values có tên khác nhau thành 1?
  - [ ] Nếu 2 values "nghe giống nhau" → phải có evidence chúng là alias (≥2 sources), nếu không → giữ riêng?
  - [ ] Có ghi `values_count: N` trong frontmatter hoặc Attributes section?
- **Ví dụ lỗi:** *ADAV (Advance Deduction AV) và ADRR (Advance Deduction RR) bị gộp thành 1 dòng "Advance Deduction" — thực tế là 2 loại Payment Item tách biệt với logic khác nhau.*

### G11: Alias Verification Enforcement — alias phải có multi-source evidence
- **Nguồn:** Review Correction Log #6 (2026-07-09) — Agent ghi "Entity Key (còn gọi là MVV)" trong glossary, nhưng MVV = Project Code, Entity Key = Company Code — hoàn toàn khác nhau.
- **Tại sao:** Alias sai = Ubiquitous Language bị ô nhiễm → toàn bộ downstream (Event Storm, Context Map, Code) dùng sai thuật ngữ → rất khó phát hiện vì "tên đúng" bị mapping sang "concept sai".
- **Checklist:**
  - [ ] Scan mọi glossary file → tìm pattern: `(còn gọi là X)`, `alias:`, `synonym:`, `= X` trong Definition?
  - [ ] Mỗi alias claim có **≥2 independent sources** xác nhận (API doc, DB schema, domain story, SRS)? Nếu chỉ 1 source (đặc biệt meeting notes) → ❌ FAIL?
  - [ ] 2 terms được gán alias có **cùng data type** và **cùng semantic context**? (VD: cùng là mã định danh, cùng là tên, cùng là số tiền...)?
  - [ ] Nếu alias chưa verified → frontmatter ghi `[UNVERIFIED ALIAS]` và term được đưa vào Hot Spots?
- **Ví dụ lỗi:** *Meeting note ghi "Mã vv → Entity key" → agent kết luận Entity Key = MVV. Thực tế: MVV = Mã Vụ Việc (Project Code, dùng nhóm công nợ), Entity Key = Mã pháp nhân (Company Code, dùng xuất hóa đơn). Hai concepts hoàn toàn khác data type và semantic.*
