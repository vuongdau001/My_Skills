# Report Status

ID: **crm-report-status** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-report-status`** · Agent: **[Delivery Coordinator](../agents/profiles/crm-delivery-coordinator.md)**  
Supported targets: Project, Feature, Epic  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Report Status: Progress report tách readiness, delivery, acceptance và blocker, có snapshot/mẫu số/source refs. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Delivery Coordinator chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Scope revision/allocation, readiness records, baseline receipts, Jira/evidence snapshot và clock/SLA policies nếu có.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

## Execution Steps

1. Chốt snapshot time/timezone, source/query refs và scope revision; dữ liệu chưa lấy được ghi Unknown.
2. Tổng hợp analysis/solution/testability theo E/S items, tách work signal khỏi verdict, giữ gaps/unknown/N/A và reviewed revision.
3. Tính baseline coverage theo scope units, Story delivery theo status + evidence và acceptance coverage theo phương pháp hiện hành.
4. Đối soát logical IDs/Jira mappings, không cộng Task hai lần, resolved/cancel không là delivered; giải thích scope delta/estimate coverage.
5. Tính review/blocker age theo clock, threshold chưa duyệt chỉ báo age; nêu discrepancy status/evidence.
6. Xuất report có nguồn tái tính, blockers/owner/next actions và uncertainty; không sửa Jira hoặc suy approval từ báo cáo.

**References đọc theo nhu cầu:**

- [Đo tiến độ phân tích, triển khai và tổng hợp lên Feature](../references/progress-measurement-and-feature-rollup.md)
- [Status Jira và tiến độ phân tích, triển khai](../references/jira-status-and-progress-reporting.md)
- [Policy dự án: khai báo, phê duyệt và áp dụng vào gate](../references/project-policy-register.md)

## Outputs

Progress report tách readiness, delivery, acceptance và blocker, có snapshot/mẫu số/source refs.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** report; không sửa status/source data để số liệu khớp mong muốn.

**Output templates:**

- [Mẫu báo cáo tiến độ Requirement và Development](../assets/templates/progress-report-template.md)

## Exit & Handoff

PM/owners kiểm số liệu theo scope; report không cho phép chuyển gate. Gaps hoặc câu hỏi cần review được route về workflow tương ứng.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-review-specification](crm-review-specification.md), [crm-assess-change](crm-assess-change.md)

## Failure & Rework

Zero denominator=N/A, Unknown phải hiện riêng; không gọi review coverage là % sản phẩm. Thiếu tenant access không lấy snapshot cũ làm hiện tại. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-report-status tổng hợp Feature tại snapshot này; tách readiness, delivery, acceptance và báo dữ liệu chưa xác minh.

Kết quả mong đợi: Progress report tách readiness, delivery, acceptance và blocker, có snapshot/mẫu số/source refs. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
