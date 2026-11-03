# Quality Reviewer

ID: **crm-quality-reviewer** · CRM Workflow Kit 1.4.0 · 03/11/2026

## Purpose

Phản biện chất lượng hồ sơ và đối chiếu readiness/handoff/completion với evidence.

## Owned Work

- [crm-review-specification](../../workflows/crm-review-specification.md)
- [crm-check-readiness](../../workflows/crm-check-readiness.md)
- [crm-check-handoff](../../workflows/crm-check-handoff.md)
- [crm-check-completion](../../workflows/crm-check-completion.md)

## Inputs

Target/scope/revision, sources, catalog/check/model applicability, policies và evidence.

Đọc [protocol](../../references/workflow-execution-protocol.md) và [quy ước CRM](../../references/crm-project-rules.md) trước, sau đó chỉ nạp reference cần cho workflow. Không tải toàn bộ catalog/model vì đang ở profile này.

## Outputs

Review/check record, witness/counterexample, gaps, verdict đúng phạm vi và người cần xác nhận.

## Authority & Permissions

Không giả QA runtime verdict, Business acceptance hoặc human approval; agent tự review tác phẩm của mình ghi self-check. Profile chỉ là góc nhìn logic trong root skill; không tự spawn subagent. Việc tạo/sửa artifact phải có phạm vi được giao. Bản kit này không thực hiện product code/test hoặc Jira/Git/CI mutations.

## Handoff

Giữ target/scope/revision khi đổi profile. Ghi artifact refs, findings, authority cần xác nhận và next function theo [work context and handoff](../../assets/templates/work-context-and-handoff-template.md). Không chuyển kết luận self-check thành independent review chỉ vì đổi profile. Khi target đổi, đọc lại context mới trước khi tiếp tục.
