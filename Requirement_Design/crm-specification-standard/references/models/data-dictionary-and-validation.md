# D04 — Từ điển dữ liệu và validation

Mã tài liệu: **D04** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Fields/schema/relationships; required/default/domain; valid/invalid groups và boundaries
- **Reviewer thực hiện:** Rà field một lượt, rồi cross-field/uniqueness/normalization; thử witness tại biên và các giá trị đặc biệt
- **Điều kiện dừng ở mức đặc tả:** Không còn field/constraint áp dụng thiếu meaning/domain/outcome; mỗi nhóm/biên chọn có expected behavior, hoặc N/A có lý do

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d04"></a>

### D04. Data dictionary, validation và ranh giới dữ liệu

**Khi dùng:** mọi input/output/persisted data mới hoặc thay đổi; có thể tham chiếu contract đã baseline nếu không đổi.

**Trường tối thiểu:** field/entity, meaning, type/unit/precision/timezone, source/owner, required/default/null behavior, valid domain/length/range, normalization, relationship/uniqueness, error outcome và data/privacy handling liên quan.

**Review đủ:**

- [ ] Phân biệt absent/null/empty/whitespace, zero/negative và default nếu có ý nghĩa khác nhau.
- [ ] Chốt thứ tự normalize → validate → compare/store và kênh nào phải áp dụng cùng rule.
- [ ] Chốt khóa duy nhất, soft-delete/status scope, referential rules và concurrency liên quan.
- [ ] Các khoảng có đầu mút đóng/mở, đơn vị, làm tròn và timezone rõ; cross-field validation có điều kiện.
- [ ] QA có nhóm hợp lệ/không hợp lệ và boundary theo đúng domain; invalid inputs độc lập khi cần để nhìn ra lỗi.

Ví dụ giả định field số nguyên cho phép `[1,100]`: xét các nhóm dưới miền/trong miền/trên miền và các điểm `0,1,2,99,100,101`. Đây là ví dụ lập test conditions, không đặt ngưỡng thật cho CRM. Với chuỗi/tiền/ngày, phải dùng biên phù hợp kiểu dữ liệu, không áp máy móc công thức số nguyên.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
