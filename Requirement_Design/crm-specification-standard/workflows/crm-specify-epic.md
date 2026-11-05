# Specify Epic

ID: **crm-specify-epic** · CRM Workflow Kit 1.11.0 · 05/11/2026

Function: **`crm-specify-epic`** · Agent: **[Requirements Analyst](../agents/profiles/crm-requirements-analyst.md)**  
Supported targets: Epic  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Specify Epic: Epic spec/model inventory, BR/AC refs, question log, applicability và solution/decomposition inputs. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Requirements Analyst chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Feature/selected scope, Epic draft, source/authority, shared models/constraints và current revision.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Nếu scope Epic lấy từ function list hoặc đang đổi ranh giới, áp dụng [checkpoint nguồn scope](../references/source-scope-and-decomposition-checkpoint.md). Đối chiếu các fragment/rule dùng chung với Epic lân cận; ghi gap trước khi coi selected scope đủ rõ. Không cần phân rã lại toàn Feature khi chỉ sửa rule không ảnh hưởng allocation.

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ author record trong scope đã giao; không suy discussion hoặc action item thành approval/product Task.

## Execution Steps

Trước khi viết E08, đọc candidate Prototype/mockup đã có và hỏi người dùng mẫu hoặc chỉ dẫn còn thiếu. So màn hình, trạng thái và quyền với rule/contract. Ghi gap/decision khi hai nguồn khác nhau. Chuyển sang crm-design-solution để hoàn thiện Prototype sau khi scope và expected behavior đủ rõ. Xem [standard Prototype](../references/prototype-workflow-and-epic-gate.md).

1. Chốt scope chọn và source/actor register; rà E01–E16 applicability, chưa biết không ghi N/A.
2. Theo mapping chọn models cần làm rõ; dựng inventory flow/state/rule/data/permission/edge cùng expected results.
3. Đối chiếu source và authority cho các rule; đọc lại bằng ví dụ và counterexample, ghi conflict/question thay vì tự quyết.
4. Gắn AC/verification conditions và scope allocation dự kiến; dùng refs cho shared artifacts, không copy tạo bản khác.
5. Ghi readiness theo item, owners/reviewers/due, solution gaps để giao Solution Architect; self-check Q01–Q07 đúng revision.

**References đọc theo nhu cầu:**

- [Danh mục nội dung và tiêu chí đặc tả Epic](../references/epic-specification-catalog.md)
- [Mapping Epic/Story với phép kiểm, mô hình và evidence](../references/catalog-check-model-mapping.md)
- [Inventory, coverage, AC và truy vết](../references/coverage-inventories-and-traceability.md)

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Epic spec/model inventory, BR/AC refs, question log, applicability và solution/decomposition inputs.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ artifacts trong phạm vi được giao; không product code/test hoặc external mutations.

**Output templates:**

- [Mẫu hồ sơ Epic](../assets/templates/epic-specification-template.md)

## Exit & Handoff

Bàn giao Dev/TL/QA để làm solution/testability và Business xác nhận nghĩa. Epic draft hoàn tất không tự đạt gate sinh Story.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-design-solution](crm-design-solution.md), [crm-review-specification](crm-review-specification.md)

## Failure & Rework

Nếu đã baseline, đề nghị thay nghĩa phải chuyển crm-assess-change trước; unknown ảnh hưởng scope vẫn chặn, dù diagram đầy. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-specify-epic làm rõ Epic này theo E01–E16, ghi model applicability và các câu hỏi chặn.

Kết quả mong đợi: Epic spec/model inventory, BR/AC refs, question log, applicability và solution/decomposition inputs. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
