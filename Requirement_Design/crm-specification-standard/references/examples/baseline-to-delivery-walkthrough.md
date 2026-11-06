# Ví dụ từ baseline đến bàn giao

Mã tài liệu: **EX-BASELINE** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Đi theo một phần scope qua Git/Jira và kiểm chứng.

**Đọc khi:** Cần minh họa quy trình; không coi ID hoặc policy mẫu là dữ liệu thật.


<a id="workflow-16"></a>

## Ví dụ baseline cho lát tạo Customer thủ công

Walkthrough dùng [case Customer–Contact](../backlog-hierarchy-and-decomposition.md#workflow-3-2). Tên, mã `EX-*` và quyết định là dữ liệu đào tạo. Hồ sơ thực cần thay bằng ID và evidence của workstream.


<a id="workflow-16-1"></a>

### Feature và Epic

- `EX-F1` là Feature Quản lý Customer và Contact. `EX-E2` là Epic Quản lý hồ sơ Customer trong ví dụ. Use Case Tạo Customer thủ công nằm ở E03.
- `EX-S2` là Story candidate cho lát tạo thủ công. Khi áp dụng thực tế, manifest giữ logical ID đã cấp. Jira key được ghi vào mapping sau khi tạo issue.
- `EX-E3` nhận phần Import/Export Customer. Có thể tiếp tục làm rõ phạm vi này nếu `EX-S2` đủ độc lập và các control dùng chung đã rõ.
- Giả định PM đã cho phép mở Epic và giao BA, Dev, QA làm rõ requirement, solution và testability. Theo dõi phần việc trên Epic.


<a id="workflow-16-2"></a>

### Đầu ra phân tích và solution

- `EX-CUS-BR1` giới hạn thao tác tạo cho người có quyền. `EX-CUS-BR2` đại diện cho quy tắc chuẩn hóa MST và phạm vi kiểm trùng đã được chốt trong giả định của bài.
- `EX-CUS-AC1` kiểm tạo thành công. `EX-CUS-AC2` kiểm từ chối và giữ nguyên dữ liệu khi thiếu quyền. `EX-CUS-AC3` kiểm từ chối và giữ nguyên dữ liệu khi trùng theo rule.
- Solution kiểm ở server, bao gồm request đồng thời. QA chuẩn bị dữ liệu và cách xác nhận kết quả, gồm kiểm không tạo bản ghi thừa.
- `EX-S2` nhận quyền, validation và xử lý trùng cần cho lát tạo thủ công.


<a id="workflow-16-3"></a>

### PR phải chứa gì?

PR của lát tạo thủ công chứa hoặc dẫn đúng revision của:

1. Scope và controls dùng chung của `EX-F1`.
2. Use Case ở E03, yêu cầu, solution và AC liên quan của `EX-E2`.
3. [Manifest baseline](../baseline-and-change-control.md#workflow-5-2) chỉ liệt kê Story trong lát được duyệt.
4. Contract, NFR và quyết định áp dụng.
5. Với workstream bật [gate Prototype](../prototype-workflow-and-epic-gate.md), pin bundle chạy được, manifest và walkthrough Đạt của đúng scope và revision. Scenario minh họa tạo hợp lệ, thiếu quyền và trùng. Với scope không tác động UI, dẫn evidence N/A được xác nhận.

Business/BA, Dev/TL và QA xác nhận phần chuyên môn liên quan. PM chốt bộ nội dung và manifest trên revision được review. PR merge thành công tạo commit xác định.

Baseline định danh **bộ yêu cầu và solution của lát tạo thủ công tại commit đã merge**. Các lát khác của Epic và phần import tiếp tục theo kế hoạch làm rõ tương ứng.


<a id="workflow-16-4"></a>

### Sau merge và khi triển khai

1. Service đọc manifest từ commit đã merge, tạo Story manual ở `todo` và ghi Jira key vào receipt.
2. Story trỏ tới baseline, selected BR/AC, solution và evidence review.
3. Nếu dữ liệu test cần cho bước triển khai chưa sẵn: chưa đạt DoR, vẫn `todo`, có owner/due chuẩn bị.
4. Đủ DoR và capacity, PM xếp việc; Dev chuyển `inprogress`.
5. Dev thực hiện checklist của Story. Nếu cần đầu ra riêng, phân công Task liên kết và review đầu ra theo brief. Chuyển Story sang `resolved` sau review, CI, deploy, smoke test và bàn giao QA hợp lệ.
6. QA phát hiện bypass quyền: ghi issue, Story về `inprogress` để sửa, rồi qua lại review/CI/deploy/retest.
7. QA Pass + đủ DoD + PM chốt: Story `done`.
8. Epic hồ sơ Customer chỉ `done` khi toàn phạm vi Epic đã được kiểm chứng và Business nghiệm thu. Nếu Epic còn sửa hồ sơ hoặc chuyển trạng thái, các phần đó vẫn phải được đối soát.
9. Feature được nghiệm thu theo phạm vi hiện hành, gồm các luồng liên Epic áp dụng. Story tạo thủ công đã Done là evidence cho lát tương ứng.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
