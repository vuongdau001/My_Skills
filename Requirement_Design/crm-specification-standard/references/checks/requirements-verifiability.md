# Q04 — Khả năng kiểm chứng yêu cầu

Mã tài liệu: **Q04** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Thực hiện phép kiểm có thao tác, evidence và điều kiện kết luận.

**Đọc khi:** Review toàn bộ phải xét phép kiểm này; review riêng chỉ kết luận cho target này.


## Đầu vào, trách nhiệm và kết quả

Đầu vào: target/selected scope/revision, source/authority, model/contract refs và các câu hỏi/findings liên quan. BA/Business xác nhận nghiệp vụ, Dev/TL xác nhận kỹ thuật, QA phản biện và kiểm chứng; chọn reviewer theo target. Owner sửa findings; PM dùng verdict chuyên môn để xét gate, không ký thay expected behavior.

Thực hiện các bước bên dưới và lưu [review record](../../assets/templates/requirements-review-record-template.md). Đạt/Không đạt theo exit criteria của phép kiểm; thiếu input hoặc reviewer ghi Chưa kiểm. N/A chỉ khi phép kiểm không áp dụng cho target đã giới hạn, có reason và reviewer; không dùng N/A để che unknown. Gap chặn scope ngăn bàn giao. [Quy trình verdict](../requirements-review-process-and-verdicts.md).


<a id="spec-3-7"></a>

### Q04 — Kiểm khả năng kiểm chứng

**Cách kiểm từng requirement/AC:**

1. Viết một verification sketch: tạo actor/resource/state/data nào, gửi action/input nào và quan sát qua kênh nào.
2. Liệt kê expected response, state/data sau thao tác và side effects cần có/không được có. Chọn cách quan sát hợp lệ: API/readback, UI, event/log, measurement hoặc inspection phù hợp.
3. Xác định tiêu chí phân biệt Pass/Fail: values/ranges, control, ordering hoặc invariants; với NFR ghi workload, environment, khoảng đo và authority chốt ngưỡng.
4. Xét ít nhất case đáp ứng và case vi phạm điều kiện khi có ý nghĩa, thêm boundary/failure theo inventory. Kiểm rằng phép đo/assertion sẽ phát hiện một implementation sai, không chỉ `assert true` hoặc kiểm toast chung.
5. QA xác nhận expected result với Business/contract và tính quan sát được với Dev. Nếu cách kiểm cần access/test hook/data chưa có thì đưa sang Q07/dependency, không ghi “test sau”.

**Evidence:** verification sketch/test condition, expected outcome, data/environment/measurement requirements và reviewer.

**Đạt khi:** người kiểm độc lập có thể nói chính xác cách setup/quan sát và tiêu chí đạt, không phải hỏi thêm để tự quyết expected behavior. Đây là khả năng kiểm chứng trên giấy; chưa cần test đã chạy trước khi có code.

**Không đạt khi:** thiếu tiêu chí Pass/Fail, thiếu expected outcome của output quan trọng, phương pháp quan sát không phân biệt được kết quả đúng/sai, hoặc còn để reviewer tự đặt ngưỡng nghiệp vụ/control.

**Ví dụ không đạt:** “không tạo trùng” nhưng chỉ kiểm response success. **Sửa:** với cùng normalized key và scope đã định, xác nhận số logical records, kết quả hai thao tác cạnh tranh và side effects theo contract. Không có access DB vẫn có thể chọn readback/API/inspection phù hợp, nếu đủ chứng minh outcome.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
