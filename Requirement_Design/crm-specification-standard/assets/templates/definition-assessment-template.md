# Mẫu chuẩn bị assessment định lượng

ID: TEMPLATE-DEFINITION-ASSESSMENT · CRM Workflow Kit 1.10.0

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). JSON giữ schema gốc; báo cáo Markdown đọc kết quả chính trước, rationale/evidence chi tiết sau. Không bọc JSON assessment bằng HTML.

Dùng cùng [scoring guideline](../../references/definition-maturity-scoring.md). Tạo JSON hợp lệ/pin hiện hành bằng score --init; không chép hash hoặc reviewer minh họa vào dự án thật.

## Thông tin cần có trong assessment

- Root: `policy: "crm-definition-v2"`, `epic_policy: "use-case-v1"`, snapshot có timezone; workstream; inventory scope/revision; complete=false nếu chưa xác định toàn phạm vi.
- Target: id/kind/path/revision/sha256/scope do --init cấp từ artifact thật; không sửa target khi review.
- Items: giữ đủ catalog, không loại phần chưa rõ. Applicability Unknown cần được quyết; N/A chỉ theo policy và có người xác nhận.
- Rationale: nội dung nào đã rõ, gap nào còn, vì sao chọn mức này ở bước hiện tại; không chỉ “đã có mục”.
- Evidence: path repo-relative, revision, sha256 và locator trỏ section/model/source cụ thể. Pin cả dependencies cần để kết luận; target unchanged không có nghĩa model ngoài nó unchanged.
- Blockers: id/reason/category content hoặc approval hoặc delivery; ghi phần scope chịu ảnh hưởng.
- Mức 3: reviewer, mode specialist/independent; evidence review; checks Q01–Q07 với verdict Đạt/N/A và rationale từng check. N/A của Q cần giải thích applicability; không dùng để bỏ qua kiểm quan trọng. Helper không xác thực danh tính/quyền.

Ví dụ cấu trúc một evidence reference (thay các giá trị bằng dữ liệu thật):

```json
{"path":"spec/reviews/review-r1.md","revision":"review-r1","sha256":"<SHA256 của file thực>","locator":"E07 permission matrix, findings closure"}
```

Ví dụ một item mức 1, sau khi điền evidence thật theo schema:

```json
{"id":"E07","applicability":"applies","present":true,"level":1,
 "rationale":"Có actor/action nhưng còn thiếu data scope được Business xác nhận",
 "evidence":[],
 "blockers":[{"id":"permission-scope","reason":"Chưa quyết quyền truy cập Customer","category":"content"}]}
```

Mảng evidence rỗng ở ví dụ phải được điền trước khi tính; đây là illustration, không là assessment có thể dùng nguyên trạng. Khi xuất Markdown review record, dùng metadata kind Review của kit và dẫn JSON; JSON assessment riêng không phải artifact metadata schema mới.

## Snapshot dependency và báo cáo

Dùng --init của kit 1.9+ để lấy record_dependencies hiện hành; không tự tạo IDs/hash giả. Với record unresolved, map items cần cap, allocation.rationale/reviewer/evidence. items=null giữ Unknown impact và không cấp chỉ số. Sau thay đổi record/evidence, reassess snapshot mới; Validated không tự làm consumer lên 3. Báo cáo --format markdown có declared/effective/rationale/evidence và có thể --output tới file mới trong reports. Không ghi đè record cũ.
