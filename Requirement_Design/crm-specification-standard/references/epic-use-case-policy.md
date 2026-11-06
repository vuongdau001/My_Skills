# Epic và Use Case ở cấp mục tiêu sử dụng

Policy **use-case-v1** · CRM Workflow Kit 2.0.0

Mỗi Epic sở hữu đúng một Use Case ở cấp `user-goal`. Epic giữ phạm vi nghiệp vụ, các mô hình áp dụng, acceptance và kế hoạch bàn giao. E03 đặc tả hành vi của mục tiêu ấy. Dùng [D01](models/business-flows-and-use-cases.md) để soạn hành vi và [catalog Epic](epic-specification-catalog.md) để hoàn thiện E01–E16.

## Chọn ranh giới

- **Mục tiêu có giá trị.** Nêu actor chính và kết quả có ý nghĩa với họ. Actor có thể là người hoặc hệ thống bên ngoài. Trigger có thể là thao tác, sự kiện hoặc lịch chạy.
- **Boundary rõ.** Nêu hệ thống chịu trách nhiệm đến đâu, actor nào ở ngoài và hệ thống lân cận trao đổi gì với nó.
- **Các đường đi phục vụ cùng mục tiêu.** Luồng chính, thay thế và ngoại lệ giải thích đạt hoặc không đạt mục tiêu ra sao. Approve và Reject có thể là hai kết quả của cùng mục tiêu xét duyệt. Nhiều màn hình, API và lần tương tác có thể phục vụ một Use Case.

Validation, kiểm quyền và lưu là bước, rule hoặc subflow dùng chung khi phục vụ một mục tiêu lớn hơn. Hai mục tiêu độc lập trên cùng entity có hai Epic. Mô tả hành trình qua nhiều mục tiêu tại Capability hoặc mô hình quy trình liên Epic. Giữ lifecycle, rules và contract dùng chung ở nguồn canonical. Công việc kỹ thuật cần theo dõi riêng là Task có một Epic chịu trách nhiệm, có link tới từng Story/Epic sử dụng đầu ra.

## Danh tính, phạm vi và evidence

Giữ Epic ID và Use Case ID cho cùng mục tiêu qua các revision. E01 tách **boundary hệ thống**, **phạm vi hành vi của Use Case** và **phạm vi bàn giao của đợt đang xét**. E03 mô tả các đường đi đã biết, đánh dấu nhánh ngoài đợt và gap cần authority. E15 phân bổ theo scenario/bước hoặc delta, giữ controls và kết quả của lát cắt. E14 giữ cách kiểm outcome tích hợp.

Mỗi đợt dùng scope, revision và baseline riêng. `done` gắn với phạm vi baseline đã nghiệm thu. Change đã được chấp nhận cho cùng mục tiêu có thể mở lại Epic theo workflow cho phép và tạo revision/phạm vi mới. Giữ baseline, approval và evidence cũ theo revision; lập danh sách phần bị tác động, phụ thuộc cần review lại và rationale nếu tái dùng evidence. Mục tiêu độc lập mới dùng cặp ID mới và ghi quan hệ với scope trước đó. Khi nhiều đợt chạy đồng thời, báo riêng từng baseline, dùng một hồ sơ Epic hiện hành và snapshot đã pin cho từng đợt. Ghi phần giao nhau để không đếm lại Story hay coverage đã nghiệm thu.

## Metadata và kiểm tra

Trong metadata schema 1 hoặc 2 của Epic, khai `epic_policy: "use-case-v1"` và một object `use_case` có `id`, `level: "user-goal"`, `locator`. ID thuộc namespace `MOD`, xuất hiện đúng một lần trong `defined_ids` của Epic. Locator là anchor HTML tường minh, duy nhất trong hồ sơ và nằm trong mục E03. Dùng các anchor ổn định cho bước, nhánh, kết quả và scenario. Revision của Use Case là revision của Epic.

- Story dùng `parent` đến Epic và `derived-from` đến MOD ID, với path/anchor và revision của phạm vi áp dụng. Dùng `depends-on` cho dependency và `verifies` cho đối tượng được kiểm. AC trong Epic dẫn locator E03 tại E14, kèm điều kiện kiểm và evidence. Artifact xác minh độc lập dùng trace ID/path/revision.
- Prototype giữ Epic ID/revision/scope trong allocation. Mỗi scenario thuộc allocation dẫn `MOD-CRM-…#locator` tới bước hoặc nhánh E03 trong refs. Bundle và walkthrough phải được pin theo đúng phạm vi.
- Lint draft nhận diện legacy và kiểm cấu trúc. Gate baseline/readiness yêu cầu chuyển đổi Epic legacy trong scope, gồm Epic truy được qua trace closure của target. Kiểm trùng ID trên mọi spec_root hiện hành. Lưu snapshot lịch sử ngoài các spec_root được cấu hình; dẫn bằng evidence pin, giữ một hồ sơ hiện hành cho mỗi ID. Lint kiểm declarations. Reviewer kiểm mục tiêu, boundary, nhánh, kết quả và coverage bằng evidence E01–E03/E14–E16.

## Chuyển đổi hồ sơ đang mở

1. Kiểm kê mọi spec_root hiện hành theo config, xác nhận trạng thái/revision/baseline và inventory consumers. Ghi riêng hồ sơ thiếu nguồn xác nhận trạng thái.
2. Giữ Epic ID khi mục tiêu nghiệp vụ cũ tiếp tục. Bổ sung một MOD ID cho Use Case hoặc giữ MOD ID đã đại diện đúng mục tiêu. Nếu Epic chứa nhiều mục tiêu, lập crosswalk mục tiêu → Epic/Use Case → Story/AC/dependency/Prototype. Chỉ giữ ID cũ cho mục tiêu kế thừa có căn cứ. Nếu chưa xác định được mục tiêu kế thừa, lưu revision cũ làm lịch sử và ghi mapping tới các ID mới. Với Epic thuần kỹ thuật, chuyển scope thành Task, xác định Epic owner và các consumer.
3. Tạo revision mới cho hồ sơ hiện hành. Pin bản cũ với baseline/evidence của nó trước khi thay đổi. Review lại phạm vi chịu tác động và hạ trạng thái review phần thiếu evidence mới. Giữ câu hỏi chưa quyết cùng phạm vi ảnh hưởng và authority.
4. Chạy lint và gate theo target. Ghi disposition từng Epic, trace nào chuyển, evidence nào giữ hoặc cần review lại. Nếu inventory rỗng, ghi số 0 và kiểm quy trình bằng fixture. Package rollback và khôi phục artifact là hai thao tác riêng. Dùng backup/receipt cho package, snapshot/revision/crosswalk cho artifact.

[Xem ví dụ Project Code](examples/project-code-request-specification.md).
