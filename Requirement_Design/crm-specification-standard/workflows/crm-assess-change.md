# Assess Change

ID: **crm-assess-change** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-assess-change`** · Agent: **[Delivery Coordinator](../agents/profiles/crm-delivery-coordinator.md)**  
Supported targets: Feature, Epic, Story, Task, BaselinePackage, Policy  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Assess Change: Impact assessment, affected artifact/evidence list, missing decisions và correction/revalidation plan. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Delivery Coordinator chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Đề nghị thay đổi/source/reason, current baseline/scope, model/Story/test allocation, evidence và decisions hiện hành.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ author record trong scope đã giao; không suy discussion hoặc action item thành approval/product Task.

## Execution Steps

Kiểm hai chiều từ delta Epic/Story đến Prototype và từ thay đổi Prototype đến Epic/Story. Xác định Screen/Scenario, fixtures, BR/AC, contracts, walkthrough và baseline pins cần cập nhật. Lập plan author/review lại cho phần bị ảnh hưởng. Xem [standard Prototype](../references/prototype-workflow-and-epic-gate.md).

1. Mô tả proposed delta, phân biệt thay what/constraint với cách triển khai; chưa áp dụng vào canonical baseline.
2. Đi theo trace từ requirement/BR/contract/policy tới models/Stories/Tasks/tests/acceptance, tìm scope và evidence bị ảnh hưởng.
3. Phối hợp góc nhìn BA/Dev/QA để ghi tác động behavior, quyền/data/state, feasibility, effort/capacity/mốc và acceptance; không giả sign-off.
4. Chỉ rõ phần cần dừng hoặc revalidation; approval/build/test evidence nào cũ không còn đủ cho revision mới.
5. Lập correction/review/merge/pin-update plan cùng authority/receiver; các bản ghi cũ giữ lịch sử.
6. Bàn giao Business/TL quyết nghĩa, PM quyết scope/resource và các workflow tác giả xử lý khi được phép; không tự sửa requirement/baseline.

**References đọc theo nhu cầu:**

- [Baseline yêu cầu, solution và kiểm soát thay đổi](../references/baseline-and-change-control.md)
- [Loại requirement, quy ước ID và truy vết](../references/requirement-types-identifiers-and-traceability.md)
- [Q05 — Truy vết và quản lý phiên bản](../references/checks/traceability-and-versioning.md)
- [Policy dự án: khai báo, phê duyệt và áp dụng vào gate](../references/project-policy-register.md)

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Impact assessment, affected artifact/evidence list, missing decisions và correction/revalidation plan.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** impact assessment và plan; không tự áp dụng proposed change vào baseline hoặc target.

## Exit & Handoff

Sau authority decision, thực hiện update ở workflow tác giả, review lại và confirmed baseline mới trước resume scope ảnh hưởng.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-define-feature](crm-define-feature.md), [crm-specify-epic](crm-specify-epic.md), [crm-design-solution](crm-design-solution.md), [crm-prepare-stories](crm-prepare-stories.md), [crm-review-specification](crm-review-specification.md)

## Failure & Rework

Không tự đổi mọi Story sang latest commit; không silently bỏ child để làm scope nhẹ hơn hoặc giữ old approval cho new behavior. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-assess-change đánh giá thay đổi rule này sau baseline, liệt kê Story/test/evidence bị ảnh hưởng và bước cần làm lại.

Kết quả mong đợi: Impact assessment, affected artifact/evidence list, missing decisions và correction/revalidation plan. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
