# Design Solution

ID: **crm-design-solution** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-design-solution`** · Agent: **[Solution Architect](../agents/profiles/crm-solution-architect.md)**  
Supported targets: Epic, Story  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Design Solution: Solution/contract draft, rationale, dependency/feasibility record, verification approach và open technical decisions. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Solution Architect chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Requirement/models đúng revision, code/schema/API hiện trạng được phép đọc, constraints/policies và dependency owners.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ author record trong scope đã giao; không suy discussion hoặc action item thành approval/product Task.

## Execution Steps

Sau khi Epic đủ rõ cho scope UI đã chọn, tạo bundle chạy được theo hành trình trong category prototypes của Work Context. Bàn giao từ chính bundle này. Ưu tiên tái dùng file nguồn phù hợp và ghi phần đã giữ hoặc thay đổi. Khi nguồn không dùng được, tạo từ BR/AC, UI contract và Story candidates. Xác nhận với người dùng phần chỉ dẫn/mẫu còn thiếu trước khi hoàn thiện nhánh bị ảnh hưởng. Chỉ ghi HTML/CSS/JS và fixture giả trong category prototypes khi được giao author. Xem [standard Prototype](../references/prototype-workflow-and-epic-gate.md).

1. Đọc yêu cầu và hiện trạng, phân biệt observed behavior với intended behavior; ghi code/contract revisions đã xem.
2. Xác định current→delta, components, interfaces, data/permission/state effects và lựa chọn/rationale.
3. Theo D07/D10 và models liên quan làm rõ contract, failure/timeout/retry/concurrency khi áp dụng; không tự đặt business threshold.
4. Kiểm feasibility bằng nguồn thực tế/evidence đã có, ghi dependency hai đầu và commitments; nếu cần PoC thì đề xuất scope/timebox để người có quyền quyết.
5. Cùng góc nhìn QA mô tả setup/observe/assert khả thi, test data/env cần và phần backend/UI chưa chứng minh.
6. Ghi solution draft/refs vào canonical artifact, phân biệt assumptions/questions với technical approval.

**References đọc theo nhu cầu:**

- [D10 — Solution, phân rã Story và testability](../references/models/solution-and-story-decomposition.md)
- [D07 — Contract API và tích hợp](../references/models/api-and-integration-contracts.md)
- [Mapping Epic/Story với phép kiểm, mô hình và evidence](../references/catalog-check-model-mapping.md)
- [Q07 — Khả thi và sẵn sàng bàn giao](../references/checks/feasibility-and-handoff-readiness.md)

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Solution/contract draft, rationale, dependency/feasibility record, verification approach và open technical decisions.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ artifacts trong phạm vi được giao; không product code/test hoặc external mutations.

## Exit & Handoff

TL/technical authority review; Business xác nhận nếu ảnh hưởng nghĩa; QA xác nhận testability. Bàn giao Story preparation khi scope tương ứng đủ rõ.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-prepare-stories](crm-prepare-stories.md), [crm-review-specification](crm-review-specification.md)

## Failure & Rework

Thiếu API/quyền/evidence feasibility phải ghi gap; không gọi tên công nghệ là đã có solution. Không sửa product code hoặc thực hiện PoC trong workflow này. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-design-solution phân tích solution cho scope này, dựa trên code/contract được cung cấp, ghi feasibility gaps và cách kiểm chứng.

Kết quả mong đợi: Solution/contract draft, rationale, dependency/feasibility record, verification approach và open technical decisions. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
