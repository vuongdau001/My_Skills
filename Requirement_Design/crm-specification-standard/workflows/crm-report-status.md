# Report Status

ID: **crm-report-status** · CRM Workflow Kit 1.11.0 · 05/11/2026

Function: **`crm-report-status`** · Agent: **[Delivery Coordinator](../agents/profiles/crm-delivery-coordinator.md)**  
Supported targets: Project, Feature, Epic, Story, Task
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Report Status: Progress report tách readiness, delivery, acceptance và blocker, có snapshot/mẫu số/source refs. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

Nhận cả câu hỏi tự nhiên “vừa làm gì xong?”, “đang tới đâu?”, “nên làm gì tiếp?”. Chọn Recap / Current status / Next step / Full report theo [hướng dẫn hội thoại](../references/conversational-status-and-next-step.md). Recap hẹp dùng observed result đã có; không bắt full context/Jira/coverage, không tự ghi report. Package/install recap giữ admin context, không ép vào cấp ticket sản phẩm.

## Participants

Delivery Coordinator chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Recap cần observed actions/results và output refs của run liên quan. Current status/Next step cần target/scope, current revision và sources liên quan tới claim. Full report mới cần scope allocation, readiness records, baseline receipts, status/evidence snapshot và clock/SLA policies theo applicability; không ép nguồn chưa liên quan lên câu hỏi ngắn.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Khi báo số từ function list/estimation hoặc allocation, áp dụng [checkpoint nguồn scope](../references/source-scope-and-decomposition-checkpoint.md): dẫn nguồn/đơn vị/revision và evidence review của allocation. Nếu chưa kiểm cách phân rã, nói rõ và giới hạn kết luận; không tự dùng dòng nguồn làm % hoàn thành. Status ngắn không tự audit/chia lại toàn scope hoặc sửa target.

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ author record trong scope đã giao; không suy discussion hoặc action item thành approval/product Task.

## Execution Steps

Khi báo mức hoàn thiện Epic có UI, dùng E08 và evidence Prototype theo scope. Nêu Prototype/biên bản nào thiếu hoặc stale và phân biệt điểm đề xuất, điểm hiệu lực và gate DoR. Xem [standard Prototype](../references/prototype-workflow-and-epic-gate.md).

Chọn mode trước. Recap: trả delta đã quan sát, kiểm chứng và giới hạn. Current status: đọc lại canonical revision + state/evidence source project chỉ định; báo discrepancy/Unknown. Next step: chọn một bước chính theo mục tiêu/blocker/dependency, nêu function/target/inputs/điều kiện và lý do. Ba mode ngắn không cần mọi bước tổng hợp số liệu bên dưới. Hỏi status không tự mở scope mới; nếu đang có nhiệm vụ đã được giao thì trả lời rồi tiếp tục phần được phép.

Full report thực hiện các bước:

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
- [Trả lời status ngắn, next step và checkpoint](../references/conversational-status-and-next-step.md)

## Đánh giá định lượng khi được yêu cầu

Đọc [definition scoring guideline](../references/definition-maturity-scoring.md) và dùng [assessment template](../assets/templates/definition-assessment-template.md). Ghi record riêng pin target/scope/revision/evidence; không sửa target đang kiểm. Có thể chấm một hạng mục hoặc toàn catalog; focused score không nâng thành full score. Helper score chỉ tính rubric đã ghi, không chứng nhận semantics, reviewer authority hay Ready. AI self-check không tự xác nhận mức 3. Tổng hợp giữ riêng catalog obligations và canonical requirement IDs, hiện Unknown/N/A/blockers và scope inventory chưa đầy đủ; không báo % requirement đúng hoặc % sản phẩm hoàn thành.

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Trả lời chat ngắn cho Recap/Current status/Next step; Full report tách readiness, delivery, acceptance và blocker, có snapshot/mẫu số/source refs. Không tự sinh file chỉ vì được hỏi status.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) khi cần lưu theo yêu cầu/bàn giao hoặc trong scope authoring đã được giao tại mốc có output đáng kể. Checkpoint dẫn tới source/revision, không thành state/backlog mới; không sửa target đã pin để thêm recap. **Write boundary:** chat hoặc report được giao; không sửa status/source data để số liệu khớp mong muốn.

**Output templates:**

- [Mẫu báo cáo tiến độ Requirement và Development](../assets/templates/progress-report-template.md)

## Exit & Handoff

PM/owners kiểm số liệu theo scope; report không cho phép chuyển gate. Gaps hoặc câu hỏi cần review được route về workflow tương ứng.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** chọn theo blocker/inputs, không thứ tự cố định: [crm-setup-project](crm-setup-project.md), [crm-define-feature](crm-define-feature.md), [crm-specify-epic](crm-specify-epic.md), [crm-design-solution](crm-design-solution.md), [crm-prepare-stories](crm-prepare-stories.md), [crm-review-specification](crm-review-specification.md), [crm-prepare-baseline](crm-prepare-baseline.md), [crm-check-readiness](crm-check-readiness.md), [crm-assess-change](crm-assess-change.md).

## Failure & Rework

Zero denominator=N/A, Unknown phải hiện riêng; không gọi review coverage là % sản phẩm. Thiếu tenant access không lấy snapshot cũ làm hiện tại. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Vừa làm gì xong? Trả ngắn từ observed result, dẫn file và kiểm chứng; không tạo report file.

> STORY-CRM-001 hiện tới đâu? Đọc current revision và evidence; phân biệt draft/Ready/implementation, không roll up toàn Project.

> EPIC-CRM-002 nên làm gì tiếp? Đối chiếu mục tiêu và blockers, đề xuất một bước chính có function/target/inputs, chưa tự mở scope thực hiện mới.

> Dùng crm-report-status tổng hợp Feature tại snapshot này; tách readiness, delivery, acceptance và báo dữ liệu chưa xác minh.

Kết quả mong đợi: Progress report tách readiness, delivery, acceptance và blocker, có snapshot/mẫu số/source refs. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
