# Mẫu context và handoff

ID: **TPL-WORK-CONTEXT** · CRM Workflow Kit 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Một đoạn nêu việc được giao hoặc output đang bàn giao. Dùng [protocol](../../references/workflow-execution-protocol.md); có thể là section trong hồ sơ hiện hành.

## Bối cảnh cần biết

| Thông tin | Giá trị thực |
|---|---|
| Project/workstream/locations | Canonical refs và artifact_paths |
| Function/profile/target | Logical ID/kind, Jira mapping riêng và mục tiêu |
| Scope/revision/baseline | In/out, nguồn/pins, policy version/authority |
| Quyền và gaps | Vùng được đọc/sửa; câu hỏi/finding, owner/due nếu biết |

## Kết quả và evidence

Tách bốn sự kiện: output được chuẩn bị, review đã thực hiện, authority đã duyệt, hành động thực tế đã xác nhận. Mỗi sự kiện ghi scope/revision, evidence/actor và phần còn thiếu; không dùng approval làm bằng chứng đã merge.

Nêu artifact tạo/sửa/kiểm, thao tác/witness, findings, verdict scoped và mode self-check/human/independent thực tế. Evidence phải đúng revision/build.

## Người nhận và bước tiếp

Ghi receiver, next function/lý do, input cần đọc lại, correction/action, owner/due và điều kiện bắt đầu. Khi resume so current revision; đổi target thì lập context mới.

Recap ngắn dùng [chế độ hội thoại](../../references/conversational-status-and-next-step.md), không bắt đủ form hoặc tạo file. Checkpoint chỉ lưu khi được yêu cầu/bàn giao hoặc có mốc authoring đáng kể; không chép cả chat, lưu active target toàn cục hay sửa baseline để ghi recap.

Nếu là artifact riêng, thêm một metadata block cuối file đúng loại. Không biến bản handoff thành approval hoặc competing state/backlog.
