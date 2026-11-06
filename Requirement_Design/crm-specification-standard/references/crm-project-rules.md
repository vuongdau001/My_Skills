# Quy ước dự án CRM và ranh giới sử dụng

Mã tài liệu: **CRM-RULES** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Giữ các quy ước chung và cách xử lý nguồn, quyết định, ví dụ.

**Đọc khi:** Bắt đầu mọi yêu cầu CRM; sau đó chỉ đọc tuyến liên quan.

Điểm vào vận hành 1.4: [Start Here](../START-HERE.md), [Workflow Execution Protocol](workflow-execution-protocol.md) và menu trong [root skill](../SKILL.md). Các tiêu chí dưới đây giữ vai trò nguồn chuẩn; workflows hướng dẫn thực hiện và bàn giao.



Epic sở hữu một Use Case user-goal, giữ cặp ID qua các revision của cùng mục tiêu. Phạm vi nghiệm thu được xác định theo baseline của từng đợt. Xem [policy use-case-v1](epic-use-case-policy.md).

## Quy ước hiện hành và cách đọc

Gói này chuẩn hóa **tài liệu quy trình CRM**, không chứng nhận compliance hay phê duyệt requirement sản phẩm. Việc đồng ý dùng quy trình không xác nhận policy trong các ví dụ. Nội dung chuẩn theo phiên bản ở Git; Jira giữ trao đổi, phân công, blocker và evidence links. Quyết định trên Jira làm đổi requirement phải được đưa vào tài liệu Git và review lại trước dùng như baseline.

Capability nằm trong tài liệu trên Epic. **Story đủ DoR có thể triển khai trực tiếp; Task tùy nhu cầu quản lý đầu ra riêng.** Không tạo Task phân tích mặc định và không tạo ticket cho từng bước/lần chạy AI. Chi tiết lựa chọn nằm tại [Phân cấp và phân rã](backlog-hierarchy-and-decomposition.md).

- Soạn Epic: [Catalog Epic](epic-specification-catalog.md) → model áp dụng → review → baseline.
- Soạn Story: [Catalog Story](story-specification-catalog.md) → subset/delta của baseline → AC/test conditions → DoR.
- Giao việc: [Task planning](task-planning-and-completion.md); checklist là lựa chọn mặc định khi không cần quản lý riêng.
- Review: [Quy trình và verdict](requirements-review-process-and-verdicts.md), [inventory/coverage](coverage-inventories-and-traceability.md).
- Chuyển bước: [DoR/DoD/approval](readiness-completion-and-approval-gates.md), [status/tiến độ](jira-status-and-progress-reporting.md).
- Bàn giao/thay đổi: [baseline](baseline-and-change-control.md), [AI/hard gate](ai-handoff-and-hard-gates.md).

Mỗi người có thể kiêm nhiều vai trò, nhưng ghi rõ trách nhiệm của lần xác nhận. Business/PO quyết nội dung nghiệp vụ; BA tổ chức yêu cầu; Dev/TL quyết/xác nhận kỹ thuật; QA phản biện và kiểm chứng; PM chốt scope, capacity và bộ đầu ra. PM không ký thay chuyên môn. AI hỗ trợ các vai trò, không là authority, không tự cấp quyền thao tác bên ngoài.

Đọc ID cùng tên: Q là phép kiểm, D là mô hình, E/S là hạng mục catalog; đây là mã của CRM. Không coi chúng là danh sách nguyên bản của ISO/IREB/ISTQB. Trước khi dùng nguồn cũ, ưu tiên quy ước hiện hành ở phần này và [nguồn/cách điều chỉnh](standards-and-crm-tailoring.md).


<a id="spec-preamble"></a>

### Xuất xứ spec

Nguồn: `CRM_Epic_Story_Specification_Standard_v1.md`, phiên bản 1.1. Metadata gốc nằm trong snapshot; quy trình trong gói này là phiên bản 1.2.0, chưa chứng minh đã cấu hình Jira/Git/CI thật.


<a id="spec-1"></a>

## Nguyên tắc sử dụng

1. **Epic mô tả phạm vi nghiệp vụ và solution tổng thể; Story mô tả chính xác phần hành vi sẽ triển khai.** Story tham chiếu nội dung dùng chung đã khóa của Epic, không chép lại thành một bản khác dễ lệch.
2. Có đủ tiêu đề hoặc AI điền hết template chưa chứng minh nội dung đúng/đủ. Mỗi hạng mục cần output, nguồn, reviewer, kết quả review và phiên bản.
3. Mọi nhóm nội dung trong checklist phải được đánh giá applicability. Nhóm có điều kiện có thể ghi N/A với lý do và người xác nhận; chưa biết không được đổi thành N/A.
4. Mức chi tiết theo phạm vi và rủi ro. Không bắt sửa một nhãn UI phải vẽ BPMN, sequence diagram và state machine mới.
5. Nội dung chuẩn nằm trong bộ yêu cầu + solution được baseline trong Git. Jira Epic giữ trao đổi, owner, readiness và blocker; không tạo Task phân tích mặc định.
6. “State transition” ở tài liệu đặc tả là vòng đời **đối tượng nghiệp vụ** như yêu cầu phê duyệt. Nó khác status Jira `todo/inprogress/resolved/done` của công việc triển khai.
7. Đánh giá “đủ” trong phạm vi được duyệt, trên những mô hình/rủi ro đã xác định; không tuyên bố một checklist hữu hạn chứng minh mọi tình huống có thể xảy ra ngoài đời đã được biết hết.


<a id="workflow-preamble"></a>

### Xuất xứ workflow

Nguồn: `CRM_Requirement_Baseline_Jira_Workflow_v1.md`, phiên bản 1.1. Metadata gốc nằm trong snapshot; quy trình trong gói này là phiên bản 1.2.0, chưa chứng minh đã cấu hình Jira/Git/CI thật.


<a id="workflow-1"></a>

## Mục tiêu và các quy ước đầu vào

Tài liệu trả lời các câu hỏi:

1. Requirement được phân loại và tổ chức ở đâu?
2. Capability, Epic, Story và Task có trách nhiệm quản lý nội dung gì?
3. **Baseline của tài liệu/nội dung nào phải được duyệt và merge vào Git trước khi tạo Story?**
4. AC, DoR và DoD của từng cấp là gì?
5. Ai chuẩn bị, ai review, ai chốt, ai nhận đầu ra?
6. Dùng các status Jira hiện có để theo dõi công việc như thế nào?
7. Dev và QA nhận bộ đầu vào nào để làm việc bằng AI mà không phải tự đoán requirement?


<a id="workflow-1-1"></a>

### Những thông tin đã được người quản lý dự án cung cấp

- Cấu trúc phạm vi: **Capability → Epic → Story**; Task tổ chức thực thi có điều kiện, không bắt buộc dưới Story.
- Capability được quản lý trong tài liệu; Jira bắt đầu từ Epic.
- Jira là nơi trao đổi, quản lý công việc và trạng thái thực thi.
- Git là nơi quản lý nội dung chuẩn có phiên bản sau review/phê duyệt.
- PM review và chốt bộ đầu ra đủ điều kiện tạo công việc con/Story.
- AI skill/API/MCP hỗ trợ đọc, comment và thao tác; phải lưu bằng chứng và có gate kiểm bằng máy.

| Issue type hiện có | Các status được cung cấp |
|---|---|
| Epic | `todo`, `inprogress`, `done`, `cancel` |
| Story | `todo`, `inprogress`, `pending`, `resolved`, `done`, `cancel` |
| Task | `todo`, `inprogress`, `review`, `pending`, `resolved`, `done`, `cancel` |

Các định nghĩa và luồng chuyển dưới đây là cách sử dụng đề xuất cho bộ status đó. Danh sách status chưa chứng minh Jira đã cho phép mọi transition được mô tả.


<a id="workflow-1-2"></a>

### Quan hệ với các tài liệu trước

Tài liệu này ghi lại phương án mới nhất đang thảo luận: **Capability nằm trong tài liệu, phía trên Epic; không yêu cầu issue type Capability trên Jira**. Các ví dụ cũ dùng “Jira Capability” hoặc S0–S3/I0–I3 không phải tên status cần bổ sung vào Jira theo tài liệu này.

Việc đặt Capability trên Epic là quy ước của CRM. Nó khác thứ tự Epic → Capability trong Azure Boards Agile process; phải giải thích quy ước này khi onboarding, không gọi đó là một cấu trúc bắt buộc của Scrum/CMMI.


<a id="workflow-2"></a>

## Định nghĩa: Requirement, AC, DoR, DoD và Baseline

| Khái niệm | Định nghĩa sử dụng | Ví dụ / hệ quả |
|---|---|---|
| Requirement | Nhu cầu, hành vi hoặc ràng buộc mà giải pháp phải đáp ứng | Người không có quyền không được tạo khách hàng |
| Business Rule — BR | Quy tắc nghiệp vụ có ID, nội dung và nguồn quyết định | EX-CUS-BR2 minh họa quy tắc chuẩn hóa MST và phạm vi kiểm trùng |
| Acceptance Criteria — AC | Điều kiện có thể kiểm chứng để chấp nhận hành vi/kết quả của một phạm vi cụ thể | Request không có quyền bị từ chối và không tạo bản ghi |
| Definition of Ready — DoR | Bộ điều kiện để một loại công việc được bắt đầu ở bước đã xác định | Story đủ rõ, có solution, dữ liệu/dependency và người thực hiện trước khi code |
| Definition of Done — DoD | Bộ điều kiện để xác nhận công việc/đầu ra của một loại đối tượng đã hoàn thành | Story đáp ứng AC, review/test đạt, evidence và tài liệu đầy đủ |
| Baseline | Một tập nội dung xác định đã được review/phê duyệt và được định danh bằng phiên bản; thay đổi sau đó phải được kiểm soát | Bộ yêu cầu và solution của lát tạo thủ công thuộc Epic hồ sơ Customer, tại Git commit đã merge |
| Manifest | Danh sách có cấu trúc mô tả phạm vi được chốt và các child dự kiến được phép tạo | Story logical ID, BR/AC thực hiện, dependency và owner |
| Evidence — EVD | Bằng chứng của quyết định, review, thao tác hoặc kiểm chứng thực tế | PR approval, gate receipt, CI run, QA verdict, acceptance record |


<a id="workflow-2-1"></a>

### Cách phân biệt AC, DoR và DoD

Với Story “AM tạo khách hàng thủ công”:

- **AC:** hệ thống phải làm đúng hành vi nào? Ví dụ, dữ liệu hợp lệ được lưu; người không có quyền bị chặn; dữ liệu trùng được xử lý đúng rule.
- **DoR:** team đã đủ điều kiện bắt đầu triển khai chưa? Ví dụ, “trùng” đã được định nghĩa; solution đã review; có dữ liệu test và dependency cần thiết.
- **DoD:** đầu ra đã đủ chất lượng để đóng Story chưa? Ví dụ, các AC được kiểm chứng; code được review; CI/QA đạt; evidence truy được đúng build.

**Có AC chưa có nghĩa đã đạt DoR. Đạt AC chưa tự chứng minh đạt toàn bộ DoD.**

Các bộ DoR/DoD cho Epic và Task trong tài liệu này là quy định điều chỉnh cho dự án. Trong Scrum Guide, DoD chính thức gắn với chất lượng của Increment; không có một bộ DoR/DoD bắt buộc chung cho mọi cấp Epic/Task.


## Tuyến đọc bổ sung của gói 1.3

- [Capability C01–C08](capability-specification-catalog.md): mục tiêu/scope/Epic allocation/acceptance; model chi tiết vẫn ở Epic/shared refs.
- [Policy register](project-policy-register.md): tách chuẩn dùng lại khỏi các giá trị/approval dự án; không tự điền ngưỡng.
- [Loại requirement, ID và trace](requirement-types-identifiers-and-traceability.md): BR là Business Rule; loại nội dung khác cấp backlog.
- [Mapping E/S→Q/D](catalog-check-model-mapping.md): model/trigger/evidence/reviewer cho từng hạng mục.
- [Measurement và roll-up](progress-measurement-and-capability-rollup.md): phân tích, triển khai và nghiệm thu báo riêng.
- [Pilot thực tế](pilot-and-operational-validation.md): cách thử trên hồ sơ thật, chưa phải pilot đã làm.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
