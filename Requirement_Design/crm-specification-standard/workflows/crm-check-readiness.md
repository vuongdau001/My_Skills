# Check Readiness

ID: **crm-check-readiness** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-check-readiness`** · Agent: **[Quality Reviewer](../agents/profiles/crm-quality-reviewer.md)**  
Supported targets: Story, Task  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Check Readiness: DoR check record, evidence/gap list, gate impact và next actions; không thay target hoặc Jira state. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Quality Reviewer chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Target Story/Task, selected scope/revision, baseline refs khi áp dụng, policy/approval evidence, plan/checklist, owners/dependencies/capacity và data/env/access.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ ghi findings/check record; không đổi record nguồn để qua gate. Lint --gate kiểm record obligations, không thay toàn bộ review/DoR hoặc authority.

## Execution Steps

Với Story UI, kiểm đúng Prototype và walkthrough trong baseline đã xác nhận, đối chiếu Screen/Scenario IDs và BR/AC với scope Story. Nếu thiếu hoặc stale, ghi DoR bị chặn và chuyển lại author/baseline theo impact. Khi scope không có UI, dùng disposition và contract từ baseline. Xem [standard Prototype](../references/prototype-workflow-and-epic-gate.md).

Chạy helper lint --gate readiness --target <target-id> với đúng repo/workstream khi có config; ghi record_obligations, record_impacts và stale refs vào check record. Nếu không chạy được thì ghi phần chưa kiểm. Helper chỉ kiểm cấu trúc/declared record dependencies; các điều kiện DoR và authority bên dưới vẫn phải được xét riêng. Không sửa target/record nguồn để đóng findings trong workflow này.

1. Mở canonical refs và xác nhận input revision đúng baseline scope; Task spike dùng brief/output/timebox phù hợp, không ép có solution biết trước.
2. Chọn DoR Story hoặc Task; đối chiếu từng điều kiện với actual evidence, không dựa chỉ Jira todo hoặc label ready.
3. Với Story kiểm S01–S12 và relevant model/check findings còn hiệu lực; với Task dùng T01–T08 và input/output dependency.
4. Kiểm kế hoạch thực hiện hiện có, owners/reviewers/capacity và dependency tại bước bắt đầu; policy bắt buộc Pending thì giữ phần gate chưa đạt.
5. Ghi từng điều kiện Đạt/Không đạt/Chưa kiểm/N/A reason, missing items và owner nếu biết; đề xuất checklist/Task khi cần nhưng không tự tạo/sửa plan.
6. Chỉ rõ receiver và correction workflow; chấp nhận Story không có Task nếu checklist/phần nghĩa vụ liên quan đã đủ.

**References đọc theo nhu cầu:**

- [DoR, AC, DoD và thẩm quyền bàn giao](../references/readiness-completion-and-approval-gates.md)
- [Danh mục nội dung và tiêu chí đặc tả Story](../references/story-specification-catalog.md)
- [Lập kế hoạch, giao và hoàn tất Task](../references/task-planning-and-completion.md)
- [Policy dự án: khai báo, phê duyệt và áp dụng vào gate](../references/project-policy-register.md)

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


DoR check record, evidence/gap list, gate impact và next actions; không thay target hoặc Jira state.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ ghi check record/evidence index; không sửa target, plan, code hoặc approval, không thay Jira state. Record cùng file chỉ sửa section record được giao, giữ target nguyên vẹn.

**Output templates:**

- [Mẫu bản ghi review](../assets/templates/requirements-review-record-template.md)

## Exit & Handoff

Dev/QA xác nhận sẵn sàng, PM chốt planning theo gate; agent record không tự cho phép chuyển todo→inprogress.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-prepare-stories](crm-prepare-stories.md), [crm-design-solution](crm-design-solution.md), [crm-prepare-baseline](crm-prepare-baseline.md)

## Failure & Rework

Thiếu baseline/policy/access thì ghi điều kiện thiếu; không tạo Task hay tự điền rule để làm target Ready. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-check-readiness kiểm Story này theo baseline, ghi evidence từng điều kiện; Story nhỏ hiện chỉ có checklist và không có Task.

Kết quả mong đợi: DoR check record, evidence/gap list, gate impact và next actions; không thay target hoặc Jira state. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
