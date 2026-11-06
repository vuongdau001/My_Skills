# Set Up Project

ID: **crm-setup-project** · CRM Workflow Kit 1.11.0 · 05/11/2026

Function: **`crm-setup-project`** · Agent: **[Delivery Coordinator](../agents/profiles/crm-delivery-coordinator.md)**  
Supported targets: Project  
Đọc [Workflow Execution Protocol](../references/workflow-execution-protocol.md) trước; workflow này là hướng dẫn trong root skill, không phải native slash command hay CLI.

## Purpose & Triggers

Set Up Project: Draft policy register/context, artifact-location map và missing-decision queue; approval để riêng. Dùng khi người dùng yêu cầu công việc này hoặc khi bàn giao từ bước trước đã đủ context. Chỉ xử lý target kinds nêu trên; nếu target không phù hợp, dùng CRM Guide chọn lại workflow, không ép target vào loại khác.

## Participants

Delivery Coordinator chủ trì góc nhìn AI. Quyền nội dung và gate theo [authority](../references/readiness-completion-and-approval-gates.md); Business/BA/Dev/TL/QA/PM xác nhận đúng phần mình. Người thực hiện có thể kiêm vai trò nhưng phải ghi reviewer/authority thực tế; chuyển profile không thành independent review.

## Required Inputs

Nguồn dự án, ràng buộc tổ chức/hợp đồng, vai trò nghiệp vụ, trách nhiệm SDLC, thẩm quyền theo nội dung, vị trí hồ sơ và policy hiện có.

Context chung: target/logical ID, selected scope, input revision/canonical locations, policy refs/effective scope và quyền đọc/sửa. Sources chưa có thì ghi chưa xác định; không bịa commit/Jira key/actor hoặc evidence.

## Input Check

Khi tiếp nhận function list/WBS/estimation/screen list, dùng [checkpoint nguồn scope](../references/source-scope-and-decomposition-checkpoint.md): xác định đơn vị/mục đích nguồn, giữ counts có provenance và gaps. Chưa mặc định inventory nguồn là phân cấp Capability/Epic/Story đã được review.

Đọc target và refs trước khi chỉnh sửa. Đối soát scope/version với request, source/authority và previous records; hỏi lựa chọn khi có nhiều target hợp lý. Ghi input còn thiếu, phần bị chặn, owner nếu biết và next action. Tiếp tục phần độc lập; không tự điền expected behavior/policy để hoàn thiện đầu ra.

Khi có meeting/chat/decision/assumption/constraint ảnh hưởng target, đọc [knowledge records](../references/knowledge-records-and-evidence.md), đối chiếu revision và dependency closure. Lấy nơi ghi từ artifact_paths trong context; [layout policy](../references/artifact-layout-and-migration.md) giữ tương thích config cũ. Chỉ author record trong scope đã giao; không suy discussion hoặc action item thành approval/product Task.

## Execution Steps

Trong intake, phân loại [vai trò nghiệp vụ và trách nhiệm SDLC](../references/artifact-writing-standard.md#business-and-sdlc-roles). Ghi người soạn, reviewer, người chốt bàn giao và thẩm quyền theo từng nội dung trong Work Context. Giữ actor và bên liên quan nghiệp vụ cùng nguồn để bàn giao bước phân tích.

Phân loại Decision, Assumption và Constraint theo [phạm vi áp dụng](../references/knowledge-records-and-evidence.md#record-applicability). Nếu một ghi chú chứa cả yêu cầu sản phẩm lẫn điều kiện SDLC, tách phát biểu và giữ locator nguồn cho từng phần. Dẫn rule sản phẩm đến hồ sơ nghiệp vụ và điều kiện SDLC đến policy hoặc gói bàn giao phù hợp.

Thực hiện [intake hồ sơ đã có](../references/knowledge-records-and-evidence.md#tái-dùng-hồ-sơ-từ-đầu-vào) trước khi soạn policy register. Đọc nguồn và đối chiếu `knowledge_intake` với hồ sơ chuẩn. Dùng lại ID/revision, pin evidence và áp dụng ngay record đã có hiệu lực đúng phạm vi. Ghi phần có điều kiện, nguồn xung đột và việc cần người có thẩm quyền xác nhận.

Ở intake, tìm Prototype/mockup trong Work Context và các vị trí người dùng chỉ định mà bạn có quyền đọc. Nhắc người dùng cung cấp chỉ dẫn, mẫu, link hoặc ví dụ dữ liệu cho Prototype. Ghi candidate/revision và input còn thiếu trong Work Context. Xem [standard Prototype](../references/prototype-workflow-and-epic-gate.md).

0. Nếu có notes/chat/email, pin source evidence; phân loại record, chọn template, ghi scope/owner/gaps và liên kết consumer. Không tạo biên bản giả nếu chỉ có chat, không tự gửi notes.
1. Kiểm nguồn hiện hành, phân biệt quy ước đã duyệt với đề xuất; tìm canonical locations trước khi tạo hồ sơ.
2. Đối chiếu policy register guide để lập các nhóm applicability, owner và missing decisions; không tự đặt severity/SLA/check names.
3. Ghi nguồn requirement, namespace ID, roles/reviewers/backup có thật và phạm vi quyền được giao.
4. Chuẩn bị draft register bằng template; ghi policy state/version/effective scope và gate bị chặn bởi policy Pending.
5. Bàn giao các decision cho Business/TL/QA/PM; ghi điều kiện có thể làm rõ Capability song song.

**References đọc theo nhu cầu:**

- [Policy dự án: khai báo, phê duyệt và áp dụng vào gate](../references/project-policy-register.md)
- [Loại requirement, quy ước ID và truy vết](../references/requirement-types-identifiers-and-traceability.md)
- [Quy ước dự án CRM và ranh giới sử dụng](../references/crm-project-rules.md)

## Outputs

Soạn output theo [standard viết artifact](../references/artifact-writing-standard.md), bao gồm review/check/report/handoff; giữ độ sâu theo mode và write boundary của function.


Draft policy register/context, artifact-location map và missing-decision queue; approval để riêng.

Dùng [Work Context and Handoff Template](../assets/templates/work-context-and-handoff-template.md) để giữ function/target/revision, evidence, gaps, authority và receiver. Có thể ghi section trong hồ sơ hiện hành, không bắt file mới. **Write boundary:** chỉ artifacts trong phạm vi được giao; không product code/test hoặc external mutations.

**Output templates:**

- [Mẫu register policy dự án](../assets/templates/project-policy-register-template.md)

## Exit & Handoff

Hoàn tất chuẩn bị khi nguồn/quy ước/gaps có refs và owner nếu biết. Áp dụng policy vào gate chỉ sau approval đúng authority.

Tách output prepared / review performed / authority approval / actual action confirmed. Thiếu evidence thì verdict đúng phần là Chưa kiểm; có gap/counterexample là Không đạt; N/A cần reason/reviewer. Không dùng workflow complete thay gate verdict. Next function là đề xuất, không là quyền thực hiện bước mới.

**Next functions:** [crm-define-capability](crm-define-capability.md)

## Failure & Rework

Chưa biết repo hoặc authority thì ghi thiếu input; không tạo repo/project policy đã Approved để lấp khoảng trống. Sau correction, đọc lại affected revision và kiểm lại scope liên quan. Giữ old findings/approval/evidence như lịch sử, không tự tái dùng cho nội dung mới. Khi thiếu quyền/tool/access, ghi giới hạn thay vì báo đã làm.

## Usage Examples

> Tôi là PM. Dùng crm-setup-project rà soát tài liệu dự án này và chuẩn bị policy register cùng các quyết định cần chốt.

Kết quả mong đợi: Draft policy register/context, artifact-location map và missing-decision queue; approval để riêng. Record phải chỉ đúng scope/revision, evidence đã xem và phần chưa kiểm. Phản ví dụ cần tránh: kết luận gate/ticket Done chỉ vì agent đã hoàn tất câu trả lời hoặc đổi profile.
