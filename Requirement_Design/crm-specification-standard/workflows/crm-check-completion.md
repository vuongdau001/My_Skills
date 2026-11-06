# Check Completion

ID: **crm-check-completion** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-check-completion`** · Agent: **[Quality Reviewer](../agents/profiles/crm-quality-reviewer.md)**  
Supported targets: Task, Story, Epic, Capability

Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Check Completion: Completion check record và evidence index, findings, missing authority và điều kiện còn thiếu để chốt. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Quality Reviewer chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Target/scope/revision, AC/DoD/policy, build/test/defect/review evidence, child coverage và specialist/PM/Business decisions theo loại target.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ ghi findings/check record; không đổi record nguồn để qua gate. Lint --gate kiểm record obligations, không thay toàn bộ review/DoR hoặc authority.

## Execution Steps

Áp dụng [policy Epic–Use Case](../references/epic-use-case-policy.md). Chốt đúng baseline/scope và đối chiếu evidence cho outcome tích hợp của Use Case trong đợt. Epic done biểu thị phạm vi baseline đã nghiệm thu. Nếu có đợt đang mở, lưu evidence/acceptance cũ và báo delta riêng.

1. Chọn DoD đúng Task/Story/Epic/Capability, không lấy child status thay acceptance tổng thể; kiểm current scope/revision.
2. Theo applicability của target, đối chiếu AC/test matrix/output evidence với đúng baseline/build/config/run; ghi untested/failed/stale, không tự chạy test hoặc giả QA verdict.
3. Kiểm defect severity/disposition theo POL-SEVERITY/POL-QUALITY có hiệu lực; không hạ severity hoặc miễn criterion để qua gate.
4. Task kiểm output/reviewer/receiver; Story kiểm tích hợp và QA/PM closure; Epic/Capability kiểm cross-child acceptance và Business decision.
5. Phân biệt Capability product acceptance với benefit observation sau sử dụng theo authority; mọi phần chưa đo giữ rõ.
6. Ghi kết quả check và conditions còn thiếu cho người có quyền chốt; không tự đóng/mở ticket hoặc sửa approval.

**References đọc theo nhu cầu:**

- [DoR, AC, DoD và thẩm quyền bàn giao](../references/readiness-completion-and-approval-gates.md)
- [Lập kế hoạch, giao và hoàn tất Task](../references/task-planning-and-completion.md)
- [Danh mục nội dung và tiêu chí Capability](../references/capability-specification-catalog.md)
- [Policy dự án: khai báo, phê duyệt và áp dụng vào gate](../references/project-policy-register.md)

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Completion check record và evidence index, findings, missing authority và điều kiện còn thiếu để chốt.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ ghi check record/evidence index; không sửa target, plan, code hoặc approval, không thay Jira state. Record cùng file chỉ sửa section record được giao, giữ target nguyên vẹn.

**Output templates:**

- [Mẫu bản ghi review](../assets/templates/requirements-review-record-template.md)

## Exit & Handoff

Receiver đúng gate: Task reviewer/receiver; Story QA + PM; Epic/Capability Business + PM. Check record không tự là quyết định đóng.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-assess-change](crm-assess-change.md), [crm-report-status](crm-report-status.md)

## Failure & Rework

Task Done nhưng AC tích hợp fail thì Story chưa đủ; CI Pass thiếu QA evidence không đủ. Jira Done mà evidence thiếu phải báo discrepancy, không tự đổi state. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-check-completion kiểm Story này; CI đã Pass nhưng chưa có QA report, hãy ghi rõ phần chưa kiểm và người cần xác nhận.

Kết quả mong đợi: Completion check record và evidence index, findings, missing authority và điều kiện còn thiếu để chốt. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
