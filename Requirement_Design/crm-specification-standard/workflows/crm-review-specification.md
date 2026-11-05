# Review Specification

ID: **crm-review-specification** · CRM Workflow Kit 1.11.0 · 05/11/2026

Function: **`crm-review-specification`** · Agent: **[Quality Reviewer](../agents/profiles/crm-quality-reviewer.md)**  
Supported targets: Feature, Epic, Story, Task  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Review Specification: Review record, inventory/evidence refs, findings với witness, verdict scoped và correction/handoff actions. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Quality Reviewer chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Target/scope/revision, full hay focused review, source/authority, policy refs, applicability/models và previous findings.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Khi review scope/allocation, dùng [checkpoint nguồn scope](../references/source-scope-and-decomposition-checkpoint.md) để kiểm căn cứ gom/tách và giao thoa bằng witness cụ thể. Có đủ dòng mapping hoặc ít Epic hơn chưa chứng minh phân rã hợp lý. Chỉ ghi findings; focused review không mở rộng thành full audit ngoài nhiệm vụ.

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ ghi findings/check record; không đổi record nguồn để qua gate. Lint --gate kiểm record obligations, không thay toàn bộ review/DoR hoặc authority.

## Execution Steps

Với Epic có UI delta, walkthrough entrypoint của bundle đúng revision theo các scenario đã phân bổ. Đối chiếu E08/D06, BR/AC, quyền và Command/Query. Ghi observed results, findings, reviewer và SHA pins trong reviews. Với backend không UI delta, review evidence N/A. Chuyển findings cho author xử lý trong bước riêng. Xem [standard Prototype](../references/prototype-workflow-and-epic-gate.md).

1. Ghi review scope và input revision trước khi đọc chi tiết; focused request giữ đúng check/model được giao.
2. Full Feature/Epic/Story xét catalog áp dụng và Q01–Q07; Task xét T01–T08/SMART. Dùng mapping để đọc đúng model thay vì nạp tất cả.
3. Thực hiện các bước kiểm trong Q/model; inventory và counterexample phải có dữ liệu cụ thể, không chỉ tick tiêu đề.
4. So cùng action/conditions qua flow/state/permission/data/contract/AC; nêu expected và actual finding trong tài liệu.
5. Ghi evidence/authority closure còn thiếu; xác định self-check hay review độc lập thực sự; không giả tên reviewer.
6. Lập review record có verdict theo phạm vi, finding/gate impact và remediation route. Không tự sửa spec đang review.

**References đọc theo nhu cầu:**

- [Quy trình review, evidence và điều kiện kết luận](../references/requirements-review-process-and-verdicts.md)
- [Mapping Epic/Story với phép kiểm, mô hình và evidence](../references/catalog-check-model-mapping.md)
- [Inventory, coverage, AC và truy vết](../references/coverage-inventories-and-traceability.md)
- [Lập kế hoạch, giao và hoàn tất Task](../references/task-planning-and-completion.md)

**Catalog theo target, chỉ đọc loại đang review:** [Feature F01–F08](../references/feature-specification-catalog.md), [Epic E01–E16](../references/epic-specification-catalog.md), [Story S01–S12](../references/story-specification-catalog.md), [Task T01–T08](../references/task-planning-and-completion.md).

## Đánh giá định lượng khi được yêu cầu

Đọc [definition scoring guideline](../references/definition-maturity-scoring.md) và dùng [assessment template](../assets/templates/definition-assessment-template.md). Ghi record riêng pin target/scope/revision/evidence; không sửa target đang kiểm. Có thể chấm một hạng mục hoặc toàn catalog; focused score không nâng thành full score. Helper score chỉ tính rubric đã ghi, không chứng nhận semantics, reviewer authority hay Ready. AI self-check không tự xác nhận mức 3. Tổng hợp giữ riêng catalog obligations và canonical requirement IDs, hiện Unknown/N/A/blockers và scope inventory chưa đầy đủ; không báo % requirement đúng hoặc % sản phẩm hoàn thành.

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Review record, inventory/evidence refs, findings với witness, verdict scoped và correction/handoff actions.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** review record/findings và remediation suggestions; không tự sửa nguồn đang review.

**Output templates:**

- [Mẫu bản ghi review](../assets/templates/requirements-review-record-template.md)

## Exit & Handoff

Kết luận theo review protocol; focused Đạt không thành full PASS. Người có authority xác nhận nội dung; PM dùng evidence xét bàn giao.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-specify-epic](crm-specify-epic.md), [crm-design-solution](crm-design-solution.md), [crm-prepare-stories](crm-prepare-stories.md), [crm-prepare-baseline](crm-prepare-baseline.md)

## Failure & Rework

Thiếu source/reviewer ghi Chưa kiểm; contradiction/gap ghi Không đạt. Không hạ criterion hoặc N/A unknown để có kết quả đẹp. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-review-specification chỉ kiểm permission của Story này; ghi phần chưa xét và không kết luận toàn Story Ready.

Kết quả mong đợi: Review record, inventory/evidence refs, findings với witness, verdict scoped và correction/handoff actions. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
