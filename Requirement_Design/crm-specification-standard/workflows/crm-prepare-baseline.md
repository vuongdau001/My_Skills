# Prepare Baseline

ID: **crm-prepare-baseline** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-prepare-baseline`** · Agent: **[Delivery Coordinator](../agents/profiles/crm-delivery-coordinator.md)**  
Supported targets: Epic, BaselinePackage  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Prepare Baseline: PM review package/gap list và evidence index; baseline receipt chỉ khi commit/merge đã được xác nhận. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Delivery Coordinator chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Selected scope, requirements/solution artifacts, reviewed revision, Story manifest và specialist/PM approval evidence hiện có; merge receipt nếu đã xảy ra.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

## Execution Steps

1. Lập danh sách đúng bộ yêu cầu + models/contracts/solution + Story manifest cho scope chọn, cùng shared requirements/policy versions.
2. Đối soát reviews/findings/authority với nội dung/revision được trình; record gaps, không tự sửa verdict/approval.
3. Chuẩn bị package trình PM: scope/in-out, allocation, dependency, blockers và decision refs để PM approve/return.
4. Ghi riêng bốn sự kiện output prepared, review performed, authority approval và confirmed merge; không gọi package draft là baseline đã merge.
5. Nếu có receipt thật: mở manifest tại commit đã merge, đối soát approved content/scope và receipt, ghi baseline refs cho Story. Không tự merge hoặc tạo Jira ticket.
6. Bàn giao người có quyền thực hiện bước còn thiếu; sau confirmed baseline mới chuyển readiness cho Story thực thi.

**References đọc theo nhu cầu:**

- [Baseline yêu cầu, solution và kiểm soát thay đổi](../references/baseline-and-change-control.md)
- [DoR, AC, DoD và thẩm quyền bàn giao](../references/readiness-completion-and-approval-gates.md)
- [Policy dự án: khai báo, phê duyệt và áp dụng vào gate](../references/project-policy-register.md)
- [Bàn giao context cho AI và đặc tả hard gate](../references/ai-handoff-and-hard-gates.md)

## Outputs

PM review package/gap list và evidence index; baseline receipt chỉ khi commit/merge đã được xác nhận.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ artifacts trong phạm vi được giao; không product code/test hoặc external mutations.

## Exit & Handoff

Package chuẩn bị xong không thay PM decision. Gate sinh Jira Story chỉ đủ khi specialist/PM approval và confirmed Git merge đúng scope/revision đều có.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-review-specification](crm-review-specification.md), [crm-check-readiness](crm-check-readiness.md)

## Failure & Rework

Có approval nhưng chưa merge thì ghi đang chờ merge. Sai revision hoặc chưa đối soát commit không dùng receipt đó làm baseline hợp lệ. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-prepare-baseline chuẩn bị bộ hồ sơ PM review cho scope này; phân biệt đã review, đã approve và đã merge.

Kết quả mong đợi: PM review package/gap list và evidence index; baseline receipt chỉ khi commit/merge đã được xác nhận. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
