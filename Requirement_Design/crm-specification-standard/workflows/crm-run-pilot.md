# Run Pilot

ID: **crm-run-pilot** · CRM Workflow Kit 1.4.0 · 03/11/2026

Function: **`crm-run-pilot`** · Agent: **[Delivery Coordinator](../agents/profiles/crm-delivery-coordinator.md)**  
Supported targets: Project, Epic, Story  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Run Pilot: Pilot record hoặc kế hoạch + missing inputs nếu chưa thể chạy; observed results, findings và corrections có scope rõ. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Delivery Coordinator chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Mục tiêu pilot, scope thật hoặc fixture được chỉ rõ, participants/authority, sources/revisions, policies, quyền và evidence locations.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

## Execution Steps

1. Chọn bước/quy mô pilot theo procedure; ghi human participants/quyền chưa có, không biến giả định thành người đã review.
2. Chọn scenarios có căn cứ: missing input, permission/state conflict, stale approval, Story không Task, change sau baseline và reporting.
3. Đi qua các workflow cần thử, giữ input/revision/expected decision và record observed action/evidence; gọi rõ khi chỉ walkthrough trên fixture.
4. Negative cases dùng bản sao; không sửa/hủy dữ liệu thật. Chưa có code/build thì chỉ kiểm requirement/governance handoff, không ghi runtime Pass.
5. Ghi findings/corrections và thời gian/câu hỏi/rework quan sát được; không tự đặt SLA từ số đo một lần.
6. Tổng hợp phần đã thử/chưa thử cho PM/authority, xác định correction/retest và cập nhật kit chỉ khi có phạm vi thay đổi được giao.

**References đọc theo nhu cầu:**

- [Pilot quy trình bằng Epic và Story thực tế](../references/pilot-and-operational-validation.md)
- [Kịch bản nghiệm thu bộ tài liệu](../references/pack-acceptance-scenarios.md)
- [Workflow Execution Protocol](../references/workflow-execution-protocol.md)

## Outputs

Pilot record hoặc kế hoạch + missing inputs nếu chưa thể chạy; observed results, findings và corrections có scope rõ.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ artifacts trong phạm vi được giao; không product code/test hoặc external mutations.

**Output templates:**

- [Mẫu ghi nhận pilot và quyết định áp dụng](../assets/templates/pilot-review-record-template.md)

## Exit & Handoff

Kết luận pilot chỉ cho bước có evidence thực tế, authority xác nhận theo procedure. Không có input/participants thì chưa pilot, không báo thành công.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-review-specification](crm-review-specification.md), [crm-report-status](crm-report-status.md)

## Failure & Rework

Không gọi mô phỏng chat là independent review hoặc hard gate integration test; giữ các phần chưa kiểm rõ ràng. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-run-pilot lập và ghi nhận pilot requirement handoff cho Epic này; nếu thiếu người hoặc nguồn thật, chỉ rõ phần chưa thể thử.

Kết quả mong đợi: Pilot record hoặc kế hoạch + missing inputs nếu chưa thể chạy; observed results, findings và corrections có scope rõ. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
