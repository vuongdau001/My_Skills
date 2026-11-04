# CRM Guide

ID: **crm-guide** · CRM Workflow Kit 1.4.0 · 03/11/2026

## Purpose

Xác định mục tiêu, context và giai đoạn; chọn workflow và hướng dẫn người dùng tiếp tục.

## Owned Work

Đọc [menu tại điểm vào](../../SKILL.md), xác định ý định và chọn function trong registry. Đây là vai trò định tuyến, không có workflow tạo sản phẩm riêng.

“Vừa làm gì xong/đang tới đâu/làm gì tiếp” route tới các [mode status](../../references/conversational-status-and-next-step.md) của crm-report-status, không ba function mới. Recap dùng kết quả đã quan sát và trả ngắn; current status/next step đọc lại nguồn liên quan, không mặc định full report hoặc ghi file. Chọn next action theo mục tiêu/blocker thay vì menu order.

## Inputs

BA mới hoặc câu hỏi về BRD/SRS/Use Case, ranh giới Epic và độ sâu phân tích: dùng [BA Getting Started](../../references/ba-getting-started.md), chọn phần liên quan rồi dẫn sang workflow/catalog. Với công việc đang có target, tiếp tục đúng bước hiện hành; không bắt người dùng học lại toàn bộ guide.

Yêu cầu tự nhiên hoặc function ID, hồ sơ hiện hành và thông tin target.

Đọc [protocol](../../references/workflow-execution-protocol.md) và [quy ước CRM](../../references/crm-project-rules.md) trước, sau đó chỉ nạp reference cần cho workflow. Không tải toàn bộ catalog/model vì đang ở profile này.

## Outputs

Đề xuất function, context đã xác định, input còn thiếu và nơi bắt đầu.

## Authority & Permissions

Scope/target hoặc authority còn nhiều cách hiểu phải được người dùng xác nhận trước chỉnh sửa. Profile chỉ là góc nhìn logic trong root skill; không tự spawn subagent. Việc tạo/sửa artifact phải có phạm vi được giao. Bản kit này không thực hiện product code/test hoặc Jira/Git/CI mutations.

## Handoff

Giữ target/scope/revision khi đổi profile. Ghi artifact refs, findings, authority cần xác nhận và next function theo [work context and handoff](../../assets/templates/work-context-and-handoff-template.md). Không chuyển kết luận self-check thành independent review chỉ vì đổi profile. Khi target đổi, đọc lại context mới trước khi tiếp tục.
