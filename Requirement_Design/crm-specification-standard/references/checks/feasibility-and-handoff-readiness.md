# Q07 — Khả thi và sẵn sàng bàn giao

Mã tài liệu: **Q07** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Thực hiện phép kiểm có thao tác, evidence và điều kiện kết luận.

**Đọc khi:** Review toàn bộ phải xét phép kiểm này; review riêng chỉ kết luận cho target này.


## Đầu vào, trách nhiệm và kết quả

Đầu vào: target/selected scope/revision, source/authority, model/contract refs và các câu hỏi/findings liên quan. BA/Business xác nhận nghiệp vụ, Dev/TL xác nhận kỹ thuật, QA phản biện và kiểm chứng; chọn reviewer theo target. Owner sửa findings; PM dùng verdict chuyên môn để xét gate, không ký thay expected behavior.

Thực hiện các bước bên dưới và lưu [review record](../../assets/templates/requirements-review-record-template.md). Đạt/Không đạt theo exit criteria của phép kiểm; thiếu input hoặc reviewer ghi Chưa kiểm. N/A chỉ khi phép kiểm không áp dụng cho target đã giới hạn, có reason và reviewer; không dùng N/A để che unknown. Gap chặn scope ngăn bàn giao. [Quy trình verdict](../requirements-review-process-and-verdicts.md).


<a id="spec-3-10"></a>

### Q07 — Kiểm khả thi và đúng mức bàn giao

**Cách kiểm:**

1. Dev/TL đối chiếu yêu cầu với code/data/interfaces/constraints hiện tại; ghi solution delta và cơ sở nhận định. Không coi việc tên API có trong tài liệu là API đã tồn tại/được phép dùng.
2. Kiểm dependency owner/counterpart, quyền, giới hạn hệ ngoài, dữ liệu/môi trường và khả năng quan sát kết quả. Ghi commitment hoặc blocker.
3. Với điều chưa biết có thể làm thay đổi feasibility/expected behavior, thực hiện khảo sát/PoC/benchmark phù hợp rủi ro, hoặc giữ scope ở trạng thái chưa đạt. Không tạo Task phân tích mặc định; nghiên cứu có thể nằm trên Epic, Task kỹ thuật độc lập chỉ khi cần output/timebox được lập kế hoạch riêng.
4. QA xác nhận phương pháp kiểm khả thi; PM/leads kiểm estimate, capacity và mốc bàn giao. Requirement phải mô tả what/constraint đúng cấp; giải pháp how để trong solution, trừ constraint đã được chấp thuận.
5. Ghi feasibility verdict và assumptions còn lại. Assumption ảnh hưởng nội dung bắt buộc phải được giải quyết hoặc theo cơ chế được cấp có thẩm quyền duyệt; không dùng một nhãn risk accepted để tuyên bố điều chưa biết là đã chứng minh được.

**Evidence:** solution/constraint refs, reality check hoặc PoC khi cần, dependency commitment, verification feasibility và estimate rationale.

**Đạt khi:** có cơ sở hợp lý để thực hiện/kiểm chứng phần được giao trong constraint và không còn blocker quan trọng bị che. Chứng minh ở mức đủ cho bàn giao, không phải đã viết xong mọi dòng code. **Không đạt khi:** chỉ ghi “AI có thể làm” hoặc “sẽ xin quyền sau” dù quyền đó quyết định giải pháp có làm được không.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
