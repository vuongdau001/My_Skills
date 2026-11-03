# D06 — Hành vi UI và trạng thái tương tác

Mã tài liệu: **D06** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Screens/actions/fields; empty/loading/error/success/disabled và navigation liên quan
- **Reviewer thực hiện:** Walkthrough mockup với inputs/permission/state; so contract và outcome server
- **Điều kiện dừng ở mức đặc tả:** Mọi UI state áp dụng có behavior; không có nút/field làm phát sinh rule chưa được quyết định

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d06"></a>

### D06. UI/UX và quan hệ với contract

**Khi dùng:** có màn hình/tương tác người dùng bị thay đổi.

**Trường tối thiểu:** screen/version, entry/navigation, field/action, visibility/editability, success/error/empty/loading/disabled states; copy/validation và accessibility/usability criteria liên quan.

**Review đủ:** UI khớp flow/data/quyền; biết xử lý double click, chờ lâu, lỗi server và input không hợp lệ; field error và server error không bị đồng nhất; nếu upload/pagination/search có giới hạn thì phải rõ. Mockup là hình minh họa, không đủ thay decision table hoặc API contract.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
