# Prepare Stories

ID: **crm-prepare-stories** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-prepare-stories`** · Agent: **[Requirements Analyst](../agents/profiles/crm-requirements-analyst.md)**  
Supported targets: Epic, Story, Task  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Prepare Stories: Story drafts/manifest, allocation/INVEST record, execution checklist hoặc optional Task briefs trong phạm vi được giao. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Requirements Analyst chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Selected Epic scope, requirements/models/AC, solution refs, dependencies, allocation hiện có và quyền phân rã.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

## Execution Steps

1. Nếu target là Epic, tách outcome theo hành vi, phân bổ BR/model/AC; nếu target là Story/Task, tập trung brief/kế hoạch trong scope được giao.
2. Với Story breakdown/draft, dùng INVEST/Example Mapping làm rõ rules/examples/questions; không chia Story mặc định theo frontend/backend/test. Nếu chỉ chuẩn bị Task, dùng SMART/T01–T08 và giữ Story source làm input.
3. Khi chuẩn bị Story, dùng S01–S12 bằng subset/delta có refs đúng revision; candidates trước baseline chưa bịa commit sau merge. Task-only request chỉ hoàn thiện brief T01–T08, không bắt viết lại Story hoặc tạo Story mới.
4. Đối chiếu gaps/overlap, mandatory controls và dependency/capacity theo vai trò; unknown chặn giữ nguyên.
5. Lập implementation checklist trong Story; chỉ chuẩn bị Task T01–T08 khi cần owner/output/handoff riêng. Cần quyền phân rã phù hợp, không tự tăng scope/cam kết.
6. Cập nhật đúng Story manifest/brief candidates khi scope được giao có nội dung đó; Task-only request chỉ cập nhật brief được giao. Bàn giao chuyên môn review, PM chốt scope theo quyền; không tạo Jira Story thực thi.

**References đọc theo nhu cầu:**

- [Phân cấp và phân rã Feature, Epic, Story, Task](../references/backlog-hierarchy-and-decomposition.md)
- [Danh mục nội dung và tiêu chí đặc tả Story](../references/story-specification-catalog.md)
- [Lập kế hoạch, giao và hoàn tất Task](../references/task-planning-and-completion.md)
- [Mapping Epic/Story với phép kiểm, mô hình và evidence](../references/catalog-check-model-mapping.md)

## Outputs

Story drafts/manifest, allocation/INVEST record, execution checklist hoặc optional Task briefs trong phạm vi được giao.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ artifacts trong phạm vi được giao; không product code/test hoặc external mutations.

**Output templates:**

- [Mẫu hồ sơ Story](../assets/templates/story-specification-template.md)
- [Mẫu Task triển khai](../assets/templates/implementation-task-template.md)

## Exit & Handoff

Đầu ra đủ để review khi scope/refs/gaps truy được. Tạo Story thực thi vẫn phải qua PM decision và confirmed Git baseline theo gate.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-review-specification](crm-review-specification.md), [crm-prepare-baseline](crm-prepare-baseline.md)

## Failure & Rework

Story lớn phải chia outcome trước; Task không chữa requirement thiếu. Delta sau baseline chuyển change assessment trước khi sửa nghĩa. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-prepare-stories phân rã scope Epic này; chuẩn bị Story candidates và checklist thực hiện, chỉ đề xuất Task khi cần giao riêng.

Kết quả mong đợi: Story drafts/manifest, allocation/INVEST record, execution checklist hoặc optional Task briefs trong phạm vi được giao. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
