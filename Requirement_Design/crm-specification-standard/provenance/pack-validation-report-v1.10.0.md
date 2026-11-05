# Kiểm chứng CRM Workflow Kit 1.10.0

ID: CRM-VALIDATION-V110 · 05/11/2026

## Thay đổi cần kiểm

Thêm standard viết artifact dùng chung cho mọi dự án, loại hồ sơ và 13 function. Root/protocol/workflow/context và registry dẫn cùng một nguồn chuẩn. Cập nhật 15 template hiện có, thêm mẫu artifact chung; giữ catalog IDs/anchors, knowledge schema 2 và evidence/approval semantics.

Báo cáo score Markdown dùng ý chính trước, bảng ngắn, rationale/evidence riêng và metadata footer. Không đổi phép tính, score policy v2, JSON schema hoặc gate. Existing project artifacts/scoped instructions không bị tự rewrite bởi update package.

## Trạng thái kiểm chứng

- Structural validator PASS: 105 Markdown documents, 157 manifest entries, 5 agent profiles, 13 workflow functions; historical source archive/migration refs giữ hợp lệ.
- Skill validator PASS.
- Full regression suite: 147 tests PASS trong 48,964 giây trên disposable projects. Sau chỉnh cách trình bày giới hạn/tổng hợp Markdown và bổ sung kiểm report footer qua lint, scoring suite 28 tests PASS trong 7,884 giây.
- Ba behavior tests mới PASS: cả 13 function nạp cùng standard đúng content/hash mà không ghi project; full/explicit reference không nạp trùng; metadata footer giữ evidence/trace và gate chặn Proposed Decision.
- Đối chiếu metadata của bốn knowledge templates với bản trước: schema/fields/states giữ nguyên. Catalog F01–F08/E01–E16/S01–S12/T01–T08 còn đủ; các historical anchors được validator đối chiếu.

Kết quả này kiểm kit/tooling, chưa là Business approval, full semantic review, runtime discovery hoặc bằng chứng mọi bản cài đã cập nhật. Logs kiểm chứng được giữ trong execution của lượt thay đổi; package update giữ receipt/backup theo INSTALL.

## Giới hạn

Behavior tests kiểm standard được chuyển vào context, dedup/full mode, đọc metadata footer và giữ unresolved dependency gate. Chúng không chứng minh mọi nội dung do model sinh ra sẽ luôn dễ đọc; tác giả/reviewer vẫn phải áp standard và đối chiếu đúng scope/revision.

Không tạo readability score/gate số học, không tự cấp DoR/DoD/Business approval, không thay đổi source product hoặc historical records. Không có multi-agent/independent review hoặc runtime discovery mới.
