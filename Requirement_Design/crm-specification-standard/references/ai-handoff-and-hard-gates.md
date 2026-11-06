# Bàn giao context cho AI và đặc tả hard gate

Mã tài liệu: **CRM-HANDOFF** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Quy định đầu vào, evidence và điều kiện cho kiểm máy sau này.

**Đọc khi:** Chuẩn bị AI execution hoặc thiết kế hook/API/MCP; chưa cấu hình hệ thống thật.


<a id="workflow-13"></a>

## Bàn giao baseline cho người và AI như thế nào?


<a id="workflow-13-1"></a>

### Sau merge, trước và sau tạo ticket

1. Git ghi nhận commit chứa tập nội dung đã duyệt; service/người phụ trách xác nhận PR/approval đúng revision và kết quả merge.
2. Đọc baseline manifest từ commit đó, không đọc nhánh đang bị sửa tiếp.
3. Tạo Story theo logical ID và scope được PM duyệt.
4. Ghi mapping logical ID → Jira issue key vào execution receipt/Jira, không bắt sửa lại baseline chỉ để thêm key vừa sinh.
5. Trên Story ghi Capability/Epic, baseline ID, repo/path/commit, selected BR/AC, solution/test refs và các approval links.
6. Dev/QA xác nhận nhận đúng bộ đầu vào; bổ sung việc còn thiếu để đạt DoR trước triển khai.


<a id="workflow-13-2"></a>

### Bộ context tối thiểu cho Dev/QA/AI

```text
Jira Story / Epic / Capability refs:
Baseline ID:
Repo + commit + paths:
Selected scope / ngoài scope:
BR-ID / AC-ID / shared rule refs:
Solution / API / data / UI contract refs:
Test approach / data / environment requirements:
Dependency / owner / reviewer / authority:
DoR / DoD / quality policy:
Phạm vi AI được phép sửa và action được phép thực hiện:
```

AI có thể đọc nguồn, nháp code/test, tìm mâu thuẫn và ghi comment theo quyền được giao. AI phải trả câu hỏi khi thiếu nội dung ảnh hưởng hành vi; không tự xác nhận rule, giả lập QA Pass hoặc ghi cờ PM approval.


<a id="workflow-13-3"></a>

### Gate kiểm bằng máy

| Hành động | Điều kiện máy cần kiểm |
|---|---|
| Merge bộ baseline | Schema/ref hợp lệ; required review đúng revision; PM approval/authority theo policy |
| Tạo Story | Baseline đã merge, child nằm trong manifest, input refs đúng; idempotency/reconciliation chống tạo trùng |
| `todo` → `inprogress` | DoR evidence còn hiệu lực; owner, dependency/capacity và approval đúng phạm vi |
| Story → `resolved` | Review/CI, deploy/smoke và build refs đạt; đã có bộ bàn giao QA |
| Story → `done` | QA verdict và DoD evidence đúng baseline/build; không có lỗi chặn; PM closure hợp lệ |
| Epic → `done` | Đủ scope, coverage/child completion và Business acceptance; PM chốt roll-up |

Máy kiểm cấu trúc, quyền và bằng chứng đã mã hóa; người có thẩm quyền xác nhận tính đúng của nội dung. Nhãn `dor-ready` hay comment “AI PASS” không tự thay gate.

Danh sách status và template không tự tạo hard gate. Cần khảo sát transition, quyền/bypass và Git/CI để cấu hình validator/service thích hợp. Automation chạy sau khi tạo ticket chỉ hậu kiểm được việc đã xảy ra.

Khi API timeout không biết đã tạo ticket hay chưa: đối soát logical ID/idempotency key rồi mới retry. Evidence/approval service không sẵn sàng thì giữ pending/không chuyển gate; fallback thủ công chỉ khi có policy, authority và evidence tương đương.


## Hợp đồng hard gate để triển khai sau

Đây là **đặc tả yêu cầu cho cơ chế kiểm**, không phải hook đã cài. Script `validate_reference_pack.py` chỉ kiểm gói tài liệu, không chứng nhận DoR/DoD, không gọi Jira/Git/CI.

| Điểm chặn | Evidence cần đối chiếu | Khi thiếu/sai |
|---|---|---|
| Trước merge baseline | Required reviews/PM decision cùng revision hoặc content digest; schema/refs | Không cho merge theo policy đã cấu hình |
| Trước tạo Story | Commit đã merge; logical child trong approved manifest; scope refs; receipt chống trùng | Không tạo; timeout thì reconcile trước retry |
| Trước bắt đầu Story/Task | DoR record đúng scope/revision; owner/dependency/ủy quyền | Giữ trạng thái trước đó; ghi missing input/action |
| Trước bàn giao Dev → QA | Code/review/required CI; build/config/env; deploy/smoke và handoff receipt | Không chuyển `resolved` |
| Trước Story Done | QA/test evidence đúng baseline/build; defects và PM closure | Không đóng; evidence cũ chỉ là lịch sử |
| Trước Epic Done | Scope hiện hành, child/acceptance coverage, Business acceptance | Không đóng nếu còn gap |

Thiết kế hook sau này phải kiểm **ngay tại điểm thực thi** (required check/branch protection/transition validator hoặc service có quyền thực thi phù hợp). Comment bot và automation chạy sau hành động là hậu kiểm, không phải hard gate. Khảo sát mọi đường bypass/UI/API trước khi cam kết hiệu lực.

Evidence record tối thiểu: target ID, selected scope, baseline/revision hoặc artifact digest, action/check, actor và vai trò/ủy quyền, thời điểm, outcome, evidence URI, superseded-by khi thay đổi. Kết quả code/test thêm code SHA, build, environment/config/test-run refs. Chỉ lưu refs/metadata phù hợp quyền; không nhúng secret hay dữ liệu khách hàng vào comment/log.

AI/skill/API/MCP phải nhận scope action được cho phép trong phiên làm việc. Tài liệu này không tự cấp quyền post comment, tạo ticket, chuyển trạng thái hay merge. Khi được phép: đọc pinned source + Jira context; so revision; thực hiện action; đọc lại/đối soát; lưu receipt gồm actor/tool/action/target/revision/outcome. Khi kết quả chưa chắc do timeout, không retry mù. Không giả mạo PM approval, human review hay QA Pass.

Approval/evidence đổi hoặc hết hiệu lực thì kiểm lại scope ảnh hưởng. Không tự nối một approval cũ vào content mới. Nếu service kiểm không sẵn sàng, không tự đi qua gate; dùng fallback chỉ khi policy/authority/evidence tương đương đã được phê duyệt. Đây là quy tắc vận hành mục tiêu, chưa xác nhận cấu hình thật.


## Policy refs trong context và gate evidence

Bổ sung policy IDs/versions/effective scope, requirement/model kind và các [ID/trace](requirement-types-identifiers-and-traceability.md) vào context bàn giao. [Policy register](project-policy-register.md) là nguồn định nghĩa checks/severity/risk/authority/clock. Service kiểm không được coi Pending/Proposed như Approved hoặc skipped check như Pass. Thay policy phải impact/review lại scope phụ thuộc; không dùng latest policy ngầm. Gói này cung cấp template và quy tắc, chưa tạo register đã phê duyệt trong repo CRM hoặc cấu hình hook thật.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
