# Mẫu context và handoff

ID: **TPL-WORK-CONTEXT** · CRM Workflow Kit 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

**Bố cục:** Tóm tắt output và receiver trước; các mục đã soạn/đã kiểm/đã duyệt/đã thực hiện tách rõ. Gap có nhãn và references đặt cuối phần tương ứng. Xem [phân cấp Markdown chung](../../references/artifact-writing-standard.md#13-phân-cấp-thị-giác-bằng-markdown-thuần).

Một đoạn nêu việc được giao hoặc output đang bàn giao. Dùng [protocol](../../references/workflow-execution-protocol.md); có thể là section trong hồ sơ hiện hành.

## Bối cảnh cần biết

| Thông tin | Giá trị thực |
|---|---|
| Project/workstream/locations | Canonical refs và artifact_paths |
| Function/profile/target | Logical ID/kind, Jira mapping riêng và mục tiêu |
| Scope/revision/revision áp dụng | In/out, nguồn/pins, policy version/authority |
| Quyền và gaps | Vùng được đọc/sửa; câu hỏi/finding, owner/due nếu biết |
| Vai trò dự án và thẩm quyền | Người soạn, reviewer, người phụ trách kiểm chứng, người chốt bàn giao và phạm vi thẩm quyền thực tế. Dẫn C03/E02 cho các vai trò nghiệp vụ. |

## Kết quả và evidence

Tách bốn sự kiện: output được chuẩn bị, review đã thực hiện, authority đã duyệt, hành động thực tế đã xác nhận. Mỗi sự kiện ghi scope/revision, evidence, người thực hiện sự kiện và phần còn thiếu; không dùng approval làm bằng chứng đã merge.

Nêu artifact tạo/sửa/kiểm, thao tác/witness, findings, verdict scoped và mode self-check/human/independent thực tế. Evidence phải đúng revision/build.

## Người nhận và bước tiếp

Ghi receiver, next function/lý do, input cần đọc lại, correction/action, owner/due và điều kiện bắt đầu. Khi resume so current revision; đổi target thì lập context mới.

Recap ngắn dùng [chế độ hội thoại](../../references/conversational-status-and-next-step.md), không bắt đủ form hoặc tạo file. Checkpoint chỉ lưu khi được yêu cầu/bàn giao hoặc có mốc authoring đáng kể; không chép cả chat, lưu active target toàn cục hay sửa revision áp dụng để ghi recap.

Nếu là artifact riêng, thêm một metadata block cuối file đúng loại. Không biến bản handoff thành approval hoặc competing state/backlog.

Áp dụng [hồ sơ hiện hành](../../references/current-state-and-history.md): cập nhật vị trí canonical theo target/scope, không tạo file theo lần chạy hoặc timeline. Review/check không tự sửa target; evidence stale phải được đánh giá lại.
