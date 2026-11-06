# Define Capability

ID: **crm-define-capability** · CRM Workflow Kit 1.11.0 · 05/11/2026

Function: **`crm-define-capability`** · Agent: **[Requirements Analyst](../agents/profiles/crm-requirements-analyst.md)**  
Supported targets: Capability

Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Define Capability: Capability C01–C08, source/outcome/scope, acceptance method, Epic candidates và decisions cần authority. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Requirements Analyst chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Nhu cầu/Capability draft, sources, stakeholder/authority, scope/constraints và policy refs hiện có.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Trước khi tạo Capability, đọc cây và quy ước cấp độ hiện có. Áp dụng phần chọn cấp/cha–con của checkpoint tại C04/C06; giải thích vì sao không đặt yêu cầu vào Capability hiện có, nếu đề xuất Capability mới. Không dựng đủ ba cấp từ một prompt nhỏ.

Trước khi đề nghị chốt C04/C06 hoặc sửa nhóm Epic, áp dụng [checkpoint nguồn scope](../references/source-scope-and-decomposition-checkpoint.md). Nêu outcome/model/acceptance làm căn cứ gom/tách và mapping/giao thoa; cùng màn hình, object hay file chưa đủ lý do. Thiếu đầu vào vẫn có thể soạn candidates, ghi phần chưa kiểm.

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ author record trong scope đã giao; không suy discussion hoặc action item thành approval/product Task.

## Execution Steps

Thực hiện [intake hồ sơ đã có](../references/knowledge-records-and-evidence.md#tái-dùng-hồ-sơ-từ-đầu-vào) kể cả khi vào thẳng workflow này. Đối chiếu `knowledge_intake` và nguồn người dùng trước khi dựng scope. Dùng cùng ID/revision đã ghi ở Setup Project. Dẫn Assumption/Constraint/Decision vào C04–C06/C08 theo nơi chúng thực sự ảnh hưởng, đồng thời khai trace links cho dependency áp dụng.

Áp dụng [policy Epic–Use Case](../references/epic-use-case-policy.md). Phân bổ scope theo các mục tiêu sử dụng độc lập. Mỗi Epic candidate có actor, outcome, boundary và đúng một Use Case cấp user-goal. Rà coverage từng fragment nguồn và controls; đặt hành trình qua nhiều mục tiêu tại Capability hoặc shared process, dẫn trách nhiệm từng Epic.

1. Đối chiếu nguồn nhu cầu, vấn đề và người nhận lợi ích; phân biệt fact, proposal, assumption và decision.
2. Làm rõ C01–C08 theo bước đang xét: giao làm rõ, chốt scope Epic, hoàn tất phân tích hoặc acceptance.
3. Phân biệt acceptance sản phẩm và lợi ích đo sau sử dụng; ghi phương pháp/target Pending khi chưa được chốt.
4. Liệt kê shared requirements, in/out scope, Epic allocation, dependency và câu hỏi chặn; dùng model khi thực sự cần.
5. Cập nhật canonical Capability draft và trace; dùng Q01–Q07 để self-check, không tự ghi Business approval.

**References đọc theo nhu cầu:**

- [Danh mục nội dung và tiêu chí Capability](../references/capability-specification-catalog.md)
- [Loại requirement, quy ước ID và truy vết](../references/requirement-types-identifiers-and-traceability.md)
- [DoR, AC, DoD và thẩm quyền bàn giao](../references/readiness-completion-and-approval-gates.md)

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Capability C01–C08, source/outcome/scope, acceptance method, Epic candidates và decisions cần authority.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ artifacts trong phạm vi được giao; không product code/test hoặc external mutations.

**Output templates:**

- [Mẫu hồ sơ Capability](../assets/templates/capability-specification-template.md)

## Exit & Handoff

Bàn giao BA/Business/PM theo gate Capability của bước được xét; có thể tạo scope Epic để làm rõ, chưa suy ra đủ điều kiện code.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-specify-epic](crm-specify-epic.md), [crm-review-specification](crm-review-specification.md)

## Failure & Rework

Outcome/authority chưa rõ thì ghi missing decision; không ép KPI số hoặc baseline toàn Capability trước khi có scope độc lập. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Dùng crm-define-capability làm rõ nhu cầu này, chỉ ra outcome, scope và Epic candidates; giữ các quyết định chưa xác nhận.

Kết quả mong đợi: Capability C01–C08, source/outcome/scope, acceptance method, Epic candidates và decisions cần authority. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
