# D01 — Flow nghiệp vụ, Use Case và swimlane

Mã tài liệu **D01** · CRM Workflow Kit 2.0.0

Dùng khi soạn E03, review hành vi hoặc phân bổ Story. Mỗi Epic sở hữu một Use Case `user-goal` theo [policy Epic](../epic-use-case-policy.md). Đầu ra gồm hồ sơ hành vi, inventory đường đi, refs và questions. [Mẫu Epic](../../assets/templates/epic-specification-template.md) và [ví dụ hoàn chỉnh](../examples/project-code-request-specification.md) minh họa cách ghi.

<a id="spec-d01"></a>

## D01. Soạn Use Case theo từng bước

| Bước và đầu vào | Khai thác và ghi đầu ra | Tự kiểm và ghi thiếu thông tin |
|---|---|---|
| 1. Đọc nguồn. Function list, rule sheet, BA decisions, mockup, baseline, production evidence nếu được giao. | Nguồn mô tả As-Is hay To-Be? Ai đã xác nhận điều gì? Ghi nguồn, revision, locator, điều đã xác nhận và xung đột. | Thử truy ngược từng claim. Ghi question cho nguồn thiếu hoặc mâu thuẫn, kèm ảnh hưởng và authority. |
| 2. Xác định actor và mục tiêu. Nhu cầu, bên liên quan nghiệp vụ và outcome. | Ai khởi phát hoặc cần kết quả? Họ làm tiếp được gì sau khi đạt mục tiêu? Ghi câu “actor muốn … để …”, actor hỗ trợ cùng bước tương tác, và bên liên quan có quyền lợi cần bảo vệ. | Bỏ tên nút/API mà câu vẫn có kết quả có ích. Nếu chưa rõ ai nhận giá trị hoặc ai quyết, ghi question và scope bị chặn. |
| 3. Chốt boundary. Hệ thống, tác nhân và điểm giao tiếp. | Hệ thống chịu trách nhiệm gì? Bên ngoài cung cấp hoặc nhận gì? Ghi boundary, phạm vi hành vi của mục tiêu và scope của đợt hiện tại thành ba phần. | Rà các hành trình qua nhiều mục tiêu và giao việc đúng Epic. Ghi interface/ownership chưa chốt. |
| 4. Xác định kết quả cuối. Mục tiêu, dữ liệu, quyền, state và constraints. | Thành công nhìn thấy ở đâu? Khi từ chối/lỗi còn đúng điều gì? Ghi success, failure và bảo đảm tối thiểu về dữ liệu, quyền, trạng thái và side effects. | QA có thể kiểm từng outcome từ setup. Nếu durability, audit hoặc rollback chưa rõ, ghi question, rủi ro và người xác nhận. |
| 5. Viết luồng chính. Trigger, điểm đầu và success outcome. | Trigger là việc bắt đầu. Preconditions là sự thật đã đúng trước khi bắt đầu. Điều kiện hệ thống phải kiểm nằm trong bước/guard. Mỗi bước có chủ thể, tương tác và phản hồi quan sát được, cùng locator ổn định. | Lần theo từ trigger đến success. “Xử lý” cần dữ liệu hoặc kết quả cụ thể. Ghi gap cho thứ tự, phản hồi hoặc trách nhiệm chưa rõ. |
| 6. Tìm nhánh tại từng bước. Quyết định, hành động có side effect và ranh giới giao tiếp. | Điều kiện nào rẽ nhánh? Ai làm gì, hệ thống trả gì, quay về bước nào hay kết thúc tại outcome nào? Xét input sai, quyền, trạng thái thay đổi, timeout, retry, concurrency, hủy và partial failure theo mức áp dụng. | Kiểm overlap/default, vòng lặp/điều kiện dừng và lỗi trước/sau commit. Ghi điều kiện + hành vi đã biết, outcome còn thiếu, question/authority. N/A cần lý do được review. |
| 7. Đối chiếu models. E04–E13 và contract hiện hành. | Truy step/branch tới state, BR, data, permission, UI/Prototype, interface và NFR áp dụng qua đúng ID/revision. E10 làm inventory edge cases và dẫn lại nhánh/kết quả E03. | Dùng cùng điều kiện so rule, state, quyền, UI và contract. Ghi các phát hiện thiếu authority, model hoặc solution. |
| 8. Phân bổ Story. Scenario, outcomes và phạm vi đợt. | Chọn subset/delta hữu ích và có thể kiểm. Giữ controls, dependency và phần còn lại. E14 nối scenario/kết quả cuối → AC → test condition/evidence. E15 ghi Story và cách kiểm tích hợp. | Kiểm bỏ sót và đếm trùng theo scenario/delta. Ghi unallocated scope, blocker và owner; planned coverage khác kết quả chạy. |
| 9. Review. Epic/revision, inventory và evidence. | Reviewer lần theo actor, boundary, mỗi đường đi, kết quả, guarantee và Story coverage. Ghi check, locator, expected/observed, finding, authority và follow-up ở record review. | Thiếu input để kết luận thì Chưa kiểm. Gap đã xác định, như nhánh thiếu expected result, là Không đạt ở phạm vi ảnh hưởng dù lint cấu trúc đạt. |

## Cách trình bày

Đặt một anchor tường minh trong E03 cho Use Case và các anchor riêng cho bước/nhánh/kết quả cần dẫn. Giữ nhãn ổn định qua revision nếu cùng nghĩa. Ví dụ, ở bước chọn đối tượng, “Actor chọn hồ sơ A; hệ thống hiển thị trạng thái và trường actor được phép xem” kiểm được cả tương tác và phản hồi. Nhánh “hồ sơ đã đổi phiên bản tại bước gửi” cần chỉ rõ phản hồi, dữ liệu giữ lại và đường quay về hoặc kết thúc.

Dùng danh sách bước cho luồng ngắn. Swimlane hoặc BPMN hữu ích khi nhiều phòng ban/hệ thống phối hợp. Đặt quy trình nhiều mục tiêu tại Capability hoặc shared model, dẫn Use Case của Epic chịu trách nhiệm mỗi chặng. Giữ nghĩa chuẩn trong E03 và models được pin. [Review và verdict](../requirements-review-process-and-verdicts.md).

## Inventory, phép kiểm và điều kiện dừng

Inventory có actor/trigger, mỗi step/decision, main/alternate/exception paths, success/failure outcomes và các tình huống rủi ro có disposition. Reviewer dùng nguồn và witness/counterexample tại từng điểm rẽ hoặc ghi dữ liệu. Bước chờ và retry áp dụng có giới hạn hoặc điều kiện dừng. Điều kiện đầu/cuối nhất quán với state, permission, contract và AC. Gap chặn phạm vi vẫn hiển thị trong E16 cùng question, authority, ảnh hưởng và bước xác nhận.
