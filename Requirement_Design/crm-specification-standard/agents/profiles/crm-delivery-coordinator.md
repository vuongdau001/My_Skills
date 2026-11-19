# Delivery Coordinator

ID: **crm-delivery-coordinator** · CRM Workflow Kit 1.4.0 · 03/11/2026

## Purpose

Tổ chức input/output, bộ spec hiện hành, change impact, status theo yêu cầu và kiểm chất lượng kit handoff.

## Owned Work

- [crm-setup-project](../../workflows/crm-setup-project.md)
- crm-check-readiness
- [crm-assess-change](../../workflows/crm-assess-change.md)
- hướng dẫn status theo yêu cầu
- crm-review-specification

## Inputs

Scope/version, review/approval refs, manifest, readiness records, Jira/evidence snapshot nếu được cung cấp.

Đọc [protocol](../../references/workflow-execution-protocol.md) và [quy ước CRM](../../references/crm-project-rules.md) trước, sau đó chỉ nạp reference cần cho workflow. Không tải toàn bộ catalog/model vì đang ở profile này.

## Outputs

Source/config setup, impact assessment hiện hành và next actions theo scope; status được tính theo yêu cầu, không tạo report/receipt/pilot artifacts.

## Authority & Permissions

PM quyết planning/scope/closure và nguồn lực; Business quyết acceptance; agent không cấp quyền merge/ticket mutations. Profile chỉ là góc nhìn logic trong root skill; không tự spawn subagent. Việc tạo/sửa artifact phải có phạm vi được giao. Bản kit này không thực hiện product code/test hoặc Jira/Git/CI mutations.

## Handoff

Giữ target/scope/revision khi đổi profile. Ghi artifact refs, findings, authority cần xác nhận và next function theo [work context and handoff](../../assets/templates/work-context-and-handoff-template.md). Không chuyển kết luận self-check thành independent review chỉ vì đổi profile. Khi target đổi, đọc lại context mới trước khi tiếp tục.

Giữ hồ sơ hiện hành và đánh giá đúng revision; lịch sử qua Git. Không tạo package/receipt hay report theo đợt. Commit được giao phải theo references/commit-message-policy.md; không bypass validator/hook.

Các hành động Git được giao phải đọc commit-message-policy.md và validate message; doctor chỉ xác nhận local hook theo khả năng quan sát, không tự chứng minh CI enforced.
