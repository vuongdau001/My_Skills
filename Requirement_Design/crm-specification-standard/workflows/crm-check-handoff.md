# Check Handoff

ID: **crm-check-handoff** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-check-handoff`** · Agent: **[Quality Reviewer](../agents/profiles/crm-quality-reviewer.md)**  
Supported targets: Story  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Check Handoff: Handoff check record scoped theo baseline/build, missing/stale evidence và next actions cho Dev/QA. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Quality Reviewer chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Story/baseline, code/review refs, required CI evidence, build/config/environment, deploy/smoke và QA handoff/data/slot refs.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

## Execution Steps

1. Xác định target Story, baseline scope và code/build/config/environment được bàn giao; mở các evidence refs được phép đọc.
2. Đối chiếu Dev→QA gate: review, POL-CHECKS/POL-QUALITY versions, required tests/CI; skipped/not-run không là Pass.
3. Kiểm deploy/smoke đúng build/môi trường, QA context/data/slot và cách nhận đầu ra; stale evidence ghi riêng.
4. Tách structural/ref checks, semantic comparison và xác nhận cần Dev/QA/authority; không chạy test runtime để tự lấp evidence.
5. Ghi check record, gaps/discrepancies và ai bổ sung; chỉ tạo record, không sửa code/spec hay chuyển Story resolved.

**References đọc theo nhu cầu:**

- [DoR, AC, DoD và thẩm quyền bàn giao](../references/readiness-completion-and-approval-gates.md)
- [Bàn giao context cho AI và đặc tả hard gate](../references/ai-handoff-and-hard-gates.md)
- [Policy dự án: khai báo, phê duyệt và áp dụng vào gate](../references/project-policy-register.md)
- [Status Jira và tiến độ phân tích, triển khai](../references/jira-status-and-progress-reporting.md)

## Outputs

Handoff check record scoped theo baseline/build, missing/stale evidence và next actions cho Dev/QA.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ ghi check record/evidence index; không sửa target, plan, code hoặc approval, không thay Jira state. Record cùng file chỉ sửa section record được giao, giữ target nguyên vẹn.

**Output templates:**

- [Mẫu bản ghi review](../assets/templates/requirements-review-record-template.md)

## Exit & Handoff

Dev cung cấp bộ bàn giao hợp lệ và QA nhận theo gate; đây chưa là DoD toàn Story. Quyền chuyển status vẫn theo workflow dự án.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-assess-change](crm-assess-change.md), [crm-check-completion](crm-check-completion.md)

## Failure & Rework

CI Pass thiếu deploy/smoke/QA receipt vẫn thiếu điều kiện; không dùng build cũ khi Staging đã đổi mà chưa impact assessment. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-check-handoff rà bộ bàn giao Dev→QA này; chỉ ghi evidence thiếu hoặc không khớp, không sửa target.

Kết quả mong đợi: Handoff check record scoped theo baseline/build, missing/stale evidence và next actions cho Dev/QA. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
