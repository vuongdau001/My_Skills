---
name: feature-spec-design-validate
description: Hoàn thiện thiết kế UX từ specification và UX Flow, dựng preview bằng source FE hiện có rồi validate nghiệp vụ, visual và recovery. Dùng sau bước đặc tả hoặc khi review thiết kế; tạo FE tái sử dụng cho implementation.
---

# Source FE Preview & Design Validation

Nhận specification/UX Flow, hoàn thiện màn hình trên FE của dự án và kiểm tra kết quả với acceptance. AGY hoặc agent khác có thể thực hiện mà không cần tool riêng của Codex.

## Ranh giới và đầu vào

- Tìm Specification, UX Flow, Decisions/Assumptions hiện hành, acceptance, project instructions và FE baseline. Tôn trọng input paths và combined documents; không yêu cầu bản sao mang đúng tên file.
- Phạm vi gồm detailed UX và source FE preview theo quyền task. Dùng branch/workspace user giao; nếu được phép tạo branch thì theo repository convention. Ghi baseline commit; không tự đổi checkout có thay đổi của người khác.
- Preview thay đổi FE, không mặc nhiên cho phép sửa backend/schema, gọi production mutation, publish, commit/push/deploy, launch AGY hoặc đổi tracker.
- Dùng trực tiếp FE stack, component, layout và styling hiện có. Không dựng vanilla HTML/app khác hoặc copy component thành mockup riêng.
- Tự chọn công cụ, fixtures và tổ chức review phù hợp rủi ro. Quyết định UX trong quyền được giao phải ghi căn cứ/assumption; không giả owner approval.

Đọc [source-fe-preview-and-review.md](references/source-fe-preview-and-review.md) trước khi sửa FE hoặc kết luận verdict.

## Workflow

1. **Inspect inputs.** Xác nhận revision/source, goal→rule/requirement→scenario→flow/acceptance. Tìm contradiction, missing behavior và active assumption. Ghi finding trước khi code; cập nhật nguồn trong quyền giao hoặc hỏi decision còn thiếu. Làm tiếp phần không phụ thuộc blocker.
2. **Design detail.** Bổ sung screen/state responsibilities, data/visibility, controls/copy, validation, navigation, loading/empty/error/recovery và responsive/accessibility. Link từng hành vi tới scenario/rule/decision.
3. **Build reusable preview.** Điều chỉnh FE components hiện có, tách props/data/action seam vừa đủ, dùng typed fixture adapter và development-only preview entry. Giữ app context và neighboring layout; cô lập review controls. Không xây lại backend logic để làm fixture pass.
4. **Operate & validate.** Thực hiện các journey/scenario quan trọng bằng preview; kiểm tra state/outcome, negative conditions, khả năng hiểu và đi tiếp. Review trực tiếp desktop/mobile, long/empty/many/error data theo risk. Assertions và screenshots bổ sung visual review, không thay thế nó.
5. **Independent review & repair.** Reviewer độc lập với tác giả phần đánh giá đối chiếu source và quan sát trực tiếp; AGY tự chọn cách tổ chức. Phân loại lỗi spec/assumption/UX/FE/evidence, sửa đúng nguồn, invalidate affected evidence và rerun phạm vi cần thiết.

Không quota rounds/personas/screenshots. Lặp khi có finding có ý nghĩa; đổi phương pháp nếu không tiến bộ. Không hạ acceptance hoặc đổi oracle để đạt PASS. Thiếu nguồn lực/quan sát/reviewer phải giữ rõ phần chưa đạt.

## Đầu ra và verdict

Trong cùng feature document root:

- `UX_DESIGN.md`: detailed screen/state specification, traceability và nghĩa vụ backend còn cần implementation.
- `REVIEW.md`: reviewer, findings/disposition, evidence method, source/FE revision, observed outcomes và verdict.
- Source FE preview, cách chạy ngắn và cách nối data/action thật; ghi ngay trong hai tài liệu trên, không cần file handoff riêng.
- Cập nhật Specification/UX Flow/Decisions khi cần; không duy trì delta thay thế việc sửa nguồn hiện hành. Feature nhỏ có thể ghép nội dung.

`DESIGN_VALIDATED` chỉ khi mọi blocking acceptance được kiểm tra trên revision cuối, không còn finding blocking, input/design/preview nhất quán, typecheck/build áp dụng đã pass, và có independent review hiện hành. Active assumption phải có behavior rõ, căn cứ/impact và nằm trong quyền quyết định được giao.

`NOT_READY` khi còn design defect, missing/failed/stale evidence, check chưa chạy hoặc chưa có independent review. `BLOCKED` khi decision/dependency/permission khiến không thể tiếp tục phần cần thiết; ghi affected IDs và cách gỡ.

Kết luận chỉ áp dụng cho UX và FE đã quan sát. API authorization, idempotency, transactions và external authority vẫn là implementation obligations nếu chưa có proof thật. Báo input/FE revision, verdict, paths, important assumptions, findings còn mở và phần chưa xác minh.
