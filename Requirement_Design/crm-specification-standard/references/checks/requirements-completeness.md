# Q02 — Đầy đủ ở mức yêu cầu và tập yêu cầu

Mã tài liệu: **Q02** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Thực hiện phép kiểm có thao tác, evidence và điều kiện kết luận.

**Đọc khi:** Review toàn bộ phải xét phép kiểm này; review riêng chỉ kết luận cho target này.


## Đầu vào, trách nhiệm và kết quả

Đầu vào: target/selected scope/revision, source/authority, model/contract refs và các câu hỏi/findings liên quan. BA/Business xác nhận nghiệp vụ, Dev/TL xác nhận kỹ thuật, QA phản biện và kiểm chứng; chọn reviewer theo target. Owner sửa findings; PM dùng verdict chuyên môn để xét gate, không ký thay expected behavior.

Thực hiện các bước bên dưới và lưu [review record](../../assets/templates/requirements-review-record-template.md). Đạt/Không đạt theo exit criteria của phép kiểm; thiếu input hoặc reviewer ghi Chưa kiểm. N/A chỉ khi phép kiểm không áp dụng cho target đã giới hạn, có reason và reviewer; không dùng N/A để che unknown. Gap chặn scope ngăn bàn giao. [Quy trình verdict](../requirements-review-process-and-verdicts.md).


<a id="spec-3-5"></a>

### Q02 — Kiểm đầy đủ ở hai mức

#### A. Đủ một phát biểu/requirement đơn lẻ

Đọc từng BR/AC và điền hoặc tham chiếu có định danh tới:

1. Ai/hệ thống nào thực hiện; action/command nào, trên đối tượng/dữ liệu nào.
2. Trigger/preconditions và phạm vi điều kiện: state, quyền, dữ liệu, thời gian/kênh liên quan.
3. Kết quả có thể quan sát: response, state/data thay đổi hoặc không đổi, side effects liên quan.
4. Các giới hạn/ngoại lệ ảnh hưởng kết quả và kết quả khi điều kiện không đạt.
5. Thuật ngữ/đơn vị/giá trị cần để hiểu đầy đủ; phần kế thừa dẫn đúng model/contract/version.

Không phải ép cả năm ý vào một câu dài; có thể diễn đạt trong nhóm hồ sơ có liên kết. Tuy nhiên, người đọc phải tìm được câu trả lời xác định, không phải suy đoán hoặc đọc một nguồn “latest” không pin.

**Ví dụ thiếu:** “Hệ thống kiểm tra trùng MST”. Còn thiếu định nghĩa chuẩn hóa, tập hồ sơ so sánh, trạng thái/tenant áp dụng, kết quả khi trùng và cách xử lý hai request cạnh tranh nếu có thể xảy ra.

#### B. Đủ cả bộ yêu cầu trong scope

Reviewer thực hiện theo thứ tự sau:

1. **Chốt đường biên và nguồn:** actor/đầu mối nghiệp vụ, hệ thống giao tiếp, tài liệu hiện hành, constraint và phần thay đổi. Đối chiếu với thực tế/legacy và hỏi người vận hành về ngoại lệ đã biết; code hiện tại là nguồn phát hiện, không tự động là yêu cầu đúng.
2. **Lập inventory cần rà** theo các chiều dưới đây và các đơn vị model trong [inventory và coverage](../coverage-inventories-and-traceability.md). Inventory là danh sách có ID/định nghĩa, không chỉ một tiêu đề “đã xem edge case”.
3. **Gán disposition cho từng item:** đã đặc tả trong scope, kế thừa baseline nào, ngoài scope theo quyết định nào hoặc không khả thi/N/A với lý do nào. Unknown/TBD là gap cần xử lý, không phải disposition hợp lệ để qua gate nếu chặn scope.
4. **Nối tới output và verification:** mỗi item trong scope phải tìm được rule/model/AC và test condition/phương pháp kiểm phù hợp. Một item có nhiều refs, không bắt tạo một AC trùng cho mỗi ô.
5. **Kiểm lỗ hổng và câu hỏi:** QA dùng inventory để tìm counterexample; Business/Dev xác nhận phần thiếu hoặc lý do loại trừ. Câu trả lời mới làm đổi tập item thì cập nhật inventory và rà lại phần ảnh hưởng.
6. **Kết luận với mẫu số nhìn thấy:** ghi số item trong từng tập, số đã có disposition, số chưa quyết và số thiếu verification mapping. Reviewer ký nhận inventory/phạm vi; không tuyên bố “mọi tình huống ngoài đời đã đủ”.

| Chiều inventory | Reviewer phải liệt kê tối thiểu gì? | Câu hỏi tìm thiếu |
|---|---|---|
| Nguồn/actor | Nhóm người, owner dữ liệu, control/operations và counterpart có tác động | Có ai nhận output hoặc gánh lỗi mà chưa được hỏi không? |
| Chức năng và flow | Use cases/commands, trigger, input/output, nhánh điều kiện và kết thúc | Sau một nhánh lỗi, dữ liệu/state nằm ở đâu? Ai xử lý tiếp? |
| Business state | Tập state, tập command và state–command disposition | Lệnh mới ở trạng thái không hợp lệ, replay và guard fail đã có kết quả chưa? |
| Rule/data | Condition domains, fields, valid/invalid groups, boundaries, cross-field constraints | Có giá trị/tổ hợp hợp lệ nào chưa biết xử lý? Có loại trừ giả để giấu gap không? |
| Quyền | Role/action/resource/ownership/state và policy default | Đúng role nhưng sai owner/state thì sao? |
| Integration | Đầu giao tiếp, successful/failure/timeout/duplicate/order và commit boundary | Lỗi trước và sau commit có bị mô tả giống nhau dù dữ liệu đã khác không? |
| NFR/transition | Control, tải/thời gian, dữ liệu chuyển đổi, khôi phục, audit/support có liên quan | Mục tiêu nghiệp vụ có đạt nếu functional đúng nhưng control/vận hành không đáp ứng không? |

**Evidence:** inventory version, disposition/coverage matrix, source/decision links, gap log và review từ các góc nhìn.

**Đạt khi:** trong scope/inventory đã được xác nhận, không còn item bắt buộc chưa có disposition/nội dung, không có câu hỏi chặn và không có requirement liên quan đã biết bị bỏ sót. **Không đạt khi:** chỉ đủ 16/16 section nhưng transition/permission/error còn ô chưa quyết.

“Đủ trong scope” có nghĩa reviewer đã thực hiện quy trình trên, không phải được quyền tự cảm nhận rằng spec có vẻ đầy đủ.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
