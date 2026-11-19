# Epic và Use Case ở cấp mục tiêu sử dụng

Policy **use-case-v1** · CRM Workflow Kit 2.5.0

Mỗi Epic sở hữu đúng một Use Case ở cấp `user-goal`. Epic giữ phạm vi nghiệp vụ, các mô hình áp dụng, acceptance và kế hoạch bàn giao. E03 đặc tả hành vi của mục tiêu ấy. Dùng [D01](models/business-flows-and-use-cases.md) để soạn hành vi và [catalog Epic](epic-specification-catalog.md) để hoàn thiện E01–E16.

## Chọn ranh giới

- **Mục tiêu có giá trị.** Nêu actor chính và kết quả có ý nghĩa với họ. Actor có thể là người hoặc hệ thống bên ngoài. Trigger có thể là thao tác, sự kiện hoặc lịch chạy.
- **Boundary rõ.** Nêu hệ thống chịu trách nhiệm đến đâu, actor nào ở ngoài và hệ thống lân cận trao đổi gì với nó.
- **Các đường đi phục vụ cùng mục tiêu.** Luồng chính, thay thế và ngoại lệ giải thích đạt hoặc không đạt mục tiêu ra sao. Approve và Reject có thể là hai kết quả của cùng mục tiêu xét duyệt. Nhiều màn hình, API và lần tương tác có thể phục vụ một Use Case.

Validation, kiểm quyền và lưu là bước, rule hoặc subflow dùng chung khi phục vụ một mục tiêu lớn hơn. Hai mục tiêu độc lập trên cùng entity có hai Epic. Mô tả hành trình qua nhiều mục tiêu tại Capability hoặc mô hình quy trình liên Epic. Giữ lifecycle, rules và contract dùng chung ở nguồn canonical. Công việc kỹ thuật cần theo dõi riêng là Task có một Epic chịu trách nhiệm, có link tới từng Story/Epic sử dụng đầu ra.

## Danh tính, phạm vi và evidence

Giữ Epic ID cho cùng mục tiêu qua các revision. Use Case dùng chung Epic ID và revision. Giữ anchor E03 ổn định khi bước, nhánh hoặc kết quả còn cùng nghĩa. E01 tách **boundary hệ thống**, **phạm vi hành vi của Use Case** và **phạm vi bàn giao của đợt đang xét**. E03 mô tả các đường đi đã biết, đánh dấu nhánh ngoài đợt và gap cần authority. E15 phân bổ theo scenario/bước hoặc delta, giữ controls và kết quả của lát cắt. E14 giữ cách kiểm outcome tích hợp.

Cùng user goal giữ Epic ID/path và cập nhật revision hiện hành; scope thay đổi cần impact assessment và review lại consumer. Consumer triển khai nhiều phiên bản dẫn commit cụ thể trong Git. Không tạo snapshot hoặc bản sao Epic theo đợt. Approval/evidence cũ không tự áp dụng cho revision mới.

## Metadata và kiểm tra

Trong metadata schema 1 hoặc 2 của Epic, khai `epic_policy: "use-case-v1"` và một object `use_case` gồm `level: "user-goal"` và `locator`, ví dụ `#e03-use-case`. Dùng `artifact_id` của Epic và revision của hồ sơ để truy vết Use Case. Hồ sơ mới dùng heading Markdown: `## E03 Use Case` có locator `#e03-use-case`; các luồng/bước/nhánh/kết quả dùng heading có tiền tố FLOW/STP/B/OUT và tên rõ theo [D01](models/business-flows-and-use-cases.md#mã-local-của-luồng-bước-nhánh-và-kết-quả). Locator phải trỏ tới heading E03 hoặc heading con thuộc E03. Không thêm thẻ HTML chỉ để tạo anchor. Hồ sơ cũ dùng explicit HTML anchor vẫn đọc được; chỉ migrate khi được giao và cập nhật toàn bộ consumer bị ảnh hưởng. Namespace `MOD` tiếp tục dùng cho model và model item, ví dụ lifecycle hoặc decision table.

- Story dùng `parent` tới Epic và `derived-from` với cùng Epic ID, path có anchor E03 và revision áp dụng. Dùng `depends-on` cho dependency và `verifies` cho đối tượng được kiểm. AC trong Epic dẫn anchor E03 tại E14. Artifact xác minh riêng dẫn Epic ID, revision và anchor E03 bằng `verifies` khi kiểm hành vi đó.
- Prototype giữ Epic ID, revision và scope trong allocation. Mỗi scenario thuộc allocation dẫn `EPIC-CRM-…#locator` tới bước hoặc nhánh E03 trong refs. Bundle và walkthrough được pin theo đúng phạm vi.
- Lint kiểm Epic ID duy nhất trong các spec_root hiện hành và locator E03 hợp lệ trong từng Epic. Gate readiness kiểm Epic có policy trong closure của target. Reviewer kiểm mục tiêu, boundary, nhánh, kết quả và coverage bằng evidence E01–E03/E14–E16.

Epic đã có `use_case.id` theo mẫu cũ vẫn đọc được với trace MOD và nhận cảnh báo khi lint. Khi chỉnh sang định dạng hiện hành, tạo revision mới và chuyển các trace hành vi đang dùng sang Epic ID, revision và anchor E03. Cập nhật Story, Prototype và verification liên quan theo scope. Giữ ID nguồn và không chuyển verdict cũ sang revision mới; lịch sử qua Git. Lịch sử qua Git, không tạo snapshot file ngoài spec_root.

## Chuyển đổi hồ sơ đang mở

1. Kiểm kê mọi spec_root hiện hành theo config, xác nhận trạng thái/revision/revision áp dụng và inventory consumers. Ghi riêng hồ sơ thiếu nguồn xác nhận trạng thái.
2. Giữ Epic ID khi mục tiêu nghiệp vụ cũ tiếp tục. Bổ sung locator E03 và chuyển các trace áp dụng sang Epic ID, revision và anchor. Nếu Epic chứa nhiều mục tiêu, lập crosswalk mục tiêu → Epic/Use Case → Story/AC/dependency/Prototype. Chỉ giữ ID cũ cho mục tiêu kế thừa có căn cứ. Nếu chưa xác định được mục tiêu kế thừa, dẫn revision cũ trong Git nếu đã commit và ghi mapping tới các ID mới. Với Epic thuần kỹ thuật, chuyển scope thành Task, xác định Epic owner và các consumer.
3. Tạo revision mới cho hồ sơ hiện hành. Xác định consumer và evidence bị ảnh hưởng trước khi cập nhật bản canonical; Git chứa lịch sử đã commit. Review lại phạm vi chịu tác động và hạ trạng thái review phần thiếu evidence mới. Giữ câu hỏi chưa quyết cùng phạm vi ảnh hưởng và authority.
4. Chạy lint và gate theo target. Ghi disposition từng Epic, trace nào chuyển, evidence nào giữ hoặc cần review lại. Nếu inventory rỗng, ghi số 0 và kiểm quy trình bằng fixture. Package rollback và khôi phục artifact là hai thao tác riêng. Dùng backup/receipt cho package, revision/consumer review cho artifact, lịch sử qua Git.

[Xem ví dụ Project Code](examples/project-code-request-specification.md).

## Heading links, Unicode và chuyển đổi

Heading mới dùng chữ thường/hoa theo nội dung và giữ ID nghiệp vụ; ưu tiên dạng `#### B02 Dữ liệu thiếu hoặc sai format`, không cần dấu trang trí giữa ID và tên. Dùng Unicode NFC cho chữ tiếng Việt, giữ nguyên dấu. Fragment theo quy ước GitHub-style của helper: chữ thường, bỏ dấu câu/markup, đổi dấu cách thành dấu gạch ngang và giữ chữ Unicode. URL literal Unicode hoặc mã hóa UTF-8 đều được kiểm sau khi decode và normalize NFC. Không tự bỏ dấu tiếng Việt hoặc đoán slug từ ID ngắn.

Heading phải rõ và tránh trùng khi có thể. Slug trùng được đánh số theo thứ tự toàn file (`-1`, `-2`...), kể cả heading ở ngoài E03; không tính riêng từng section. Dùng ID trong heading giúp phân biệt các bước/rule/câu hỏi nhưng không khiến fragment độc lập với tên. Đổi tên hoặc thứ tự heading phải kiểm/cập nhật inbound links và metadata locator, tăng revision và review pin bị ảnh hưởng. Trace đang pin revision/hash cũ không tự được refresh để hết lỗi.

Khi migrate: kiểm inventory anchor/consumer → lưu mapping old fragment sang heading mới → sửa target và consumer trong scope → lint link/E03 boundary/trace → kiểm viewer được chọn khi có. Bản ghi lịch sử vẫn giữ revision và kết luận cũ; thay link điều hướng tới tài liệu hiện hành phải được ghi rõ trong mapping và không chuyển approval sang revision mới. Không tạo HTML/PDF phụ. Các viewer có thuật toán slug khác nhau có thể cần kiểm thêm; lint theo quy ước kit không chứng nhận mọi viewer hỗ trợ giống nhau.

Căn cứ về section links và đánh số heading trùng: [GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links). NFC và phạm vi lint là tailoring của kit.
