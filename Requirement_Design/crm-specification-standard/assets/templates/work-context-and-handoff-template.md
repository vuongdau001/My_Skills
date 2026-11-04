# Work Context and Handoff Template

ID: **TPL-WORK-CONTEXT** · CRM Workflow Kit 1.4.0 · 03/11/2026


Dùng theo [protocol](../../references/workflow-execution-protocol.md). Có thể ghép vào hồ sơ hiện hành; đây là mẫu, không phải run/approval thật.

Không bắt dùng đầy đủ cho câu hỏi status ngắn. Theo [chế độ hội thoại](../../references/conversational-status-and-next-step.md), chỉ lưu checkpoint khi cần bàn giao/lưu theo yêu cầu hoặc khi authoring đã được giao đạt mốc output đáng kể. Checkpoint tối thiểu: target/scope và revisions; artifact/source refs + snapshot khi có dữ liệu động; observed result/evidence; gaps; next action/function/lý do/inputs/điều kiện. Không chép toàn chat, không lưu active target toàn cục hoặc sửa baseline chỉ để ghi recap.

## Work Context

| Field | Giá trị thực tế |
|---|---|
| Project / artifact locations | Repo/path hoặc refs đã xác nhận; chưa biết thì ghi thiếu |
| Function / profile / run objective | Function ID, profile và việc được giao |
| Target / kind / Jira mapping | Feature/Epic/Story/Task hoặc policy/package; giữ logical ID và Jira key tách biệt |
| Selected scope / exclusions | Phạm vi lần này, phần chưa xét |
| Input revision / baseline | Commit/ref hoặc working revision; không bịa SHA |
| Policy versions / authority | IDs, effective scope, người có quyền, approvals hiện có |
| Read/write permissions | Artifact/section được sửa; external actions chưa được cấp quyền |
| Open findings / questions | ID, tác động, owner/due, điều kiện chặn |

## Work Result

Artifacts tạo/sửa/kiểm; thao tác thực tế; witness/counterexample; findings; evidence refs đúng revision/build; verdict scoped hoặc Chưa kiểm. Ghi self-check/human/independent review theo thực tế.

| Sự kiện | Đã xác nhận? | Scope/revision | Evidence / actor | Phần còn thiếu |
|---|---|---|---|---|
| Output prepared | Có/Chưa/Chưa xác minh | Target thật | Ref | Gap |
| Review performed | Có/Chưa/Chưa xác minh | Target thật | Reviewer/run ref | Gap |
| Authority approval | Có/Chưa/Chưa xác minh | Target thật | Decision/approval ref | Gap |
| External action confirmed | Có/Chưa/Chưa xác minh/N/A có lý do | Merge/build/handoff nếu thuộc scope | Receipt/version | Gap |

## Next Handoff

Receiver; next function và lý do; input refs phải đọc lại; correction/actions cần làm; owner/due; điều kiện được bắt đầu; actions chưa thực hiện. Khi resume so lại current revision. Khi đổi target, lập context mới thay vì tiếp tục ghi vào target cũ.
