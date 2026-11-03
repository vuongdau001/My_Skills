# D01 — Flow nghiệp vụ, use case và swimlane

Mã tài liệu: **D01** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Actor/trigger/use case; step/decision; nhánh success/alternate/exception; wait/retry nếu có
- **Reviewer thực hiện:** Lần theo từ trigger tới postcondition; tại mỗi decision xét condition overlap/default; tại mỗi giao tiếp xét lỗi trước/sau effect
- **Điều kiện dừng ở mức đặc tả:** Không có bước/nhánh bắt buộc vô chủ hoặc không biết kết quả; các loop/wait áp dụng có điều kiện kết thúc; đường quan trọng có scenario

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d01"></a>

### D01. Flow, use case và swimlane

**Khi dùng:** mọi hành vi cần có mô tả flow; dùng sơ đồ khi giúp nhìn rõ nhánh/phối hợp. Luồng nhiều phòng ban/hệ thống nên dùng swimlane/BPMN phù hợp; flow ngắn có thể dùng danh sách bước hoặc flowchart.

**Trường tối thiểu:** flow ID, mục tiêu, actor/participants, trigger, preconditions, main steps, alternate/exception paths, postconditions, dữ liệu trao đổi và BR/AC refs.

**Review đủ:**

- [ ] Mọi bước có actor/system thực hiện và output, không có bước “xử lý tiếp” vô chủ.
- [ ] Mỗi điểm rẽ có điều kiện rõ, xử lý overlap/default hoặc trường hợp không điều kiện nào đúng.
- [ ] Có lối thành công, từ chối và lỗi quan trọng; không có nhánh cụt không giải thích.
- [ ] Wait/timeout/retry/cancel và handoff qua bên khác được quyết applicability.
- [ ] Biết dữ liệu/state nào được ghi và side effect nào phát sinh ở từng điểm quan trọng.
- [ ] Điều kiện đầu/cuối khớp business state, permission matrix, contract và AC.

**Không đạt:** sơ đồ chỉ có “Nhập → Xử lý → Thành công”; thiếu kiểm quyền, validation hoặc lỗi lưu. Không bắt vẽ cả flowchart lẫn BPMN cho cùng một thông tin nếu một mô hình đã đủ và rõ.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
