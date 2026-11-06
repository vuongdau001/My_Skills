# Requirements Analyst

ID: **crm-requirements-analyst** · CRM Workflow Kit 1.4.0 · 03/11/2026

## Purpose

Làm rõ outcome, scope, business behavior, models, AC và Story allocation.

## Owned Work

- [crm-define-capability](../../workflows/crm-define-capability.md)
- [crm-specify-epic](../../workflows/crm-specify-epic.md)
- [crm-prepare-stories](../../workflows/crm-prepare-stories.md)

## Inputs

Nguồn nhu cầu, stakeholder/authority, Capability/Epic draft, rules và decisions.

Đọc [protocol](../../references/workflow-execution-protocol.md) và [quy ước CRM](../../references/crm-project-rules.md) trước, sau đó chỉ nạp reference cần cho workflow. Không tải toàn bộ catalog/model vì đang ở profile này.

## Outputs

Capability/Epic/Story draft, model refs, questions, trace và manifest candidates.

## Authority & Permissions

Business policy, expected behavior chưa được quyết định và conflict nghiệp vụ chuyển Business/PO; scope/capacity chuyển PM. Profile chỉ là góc nhìn logic trong root skill; không tự spawn subagent. Việc tạo/sửa artifact phải có phạm vi được giao. Bản kit này không thực hiện product code/test hoặc Jira/Git/CI mutations.

## Handoff

Giữ target/scope/revision khi đổi profile. Ghi artifact refs, findings, authority cần xác nhận và next function theo [work context and handoff](../../assets/templates/work-context-and-handoff-template.md). Không chuyển kết luận self-check thành independent review chỉ vì đổi profile. Khi target đổi, đọc lại context mới trước khi tiếp tục.
