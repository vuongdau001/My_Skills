# D05 — Quyền và phạm vi truy cập dữ liệu

Mã tài liệu: **D05** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Actor groups × action × resource/data-scope/condition; default deny/allow theo policy
- **Reviewer thực hiện:** Kiểm allow, wrong role, wrong owner/state/tenant và privilege change nếu áp dụng; so server/UI/AC
- **Điều kiện dừng ở mức đặc tả:** Mọi lớp quyền có disposition; những lớp được gộp có cùng rule được xác nhận; không chỉ có các role được cho phép

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d05"></a>

### D05. Permission matrix và phạm vi dữ liệu

**Khi dùng:** mọi Story phải biết actor và quyền áp dụng; backend-only vẫn cần đánh giá.

**Trường tối thiểu:** role/principal, action, resource/object, ownership/tenant/data scope, state/condition, field restriction, allow/deny outcome và source authority.

**Review đủ:** có positive/negative cases; xét role đúng nhưng resource/state sai; server enforcement không chỉ ẩn nút UI; delegation/self-approval nếu có; data exposure và error message không làm lộ ngoài phạm vi; role/ownership đổi trong lúc thao tác có kết quả xác định nếu áp dụng.

Quyền dùng chung tham chiếu version chung. Story không được giảm kiểm quyền để tách thành phần nhỏ hơn.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
