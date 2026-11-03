# Ví dụ từ baseline đến bàn giao

Mã tài liệu: **EX-BASELINE** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Đi theo một phần scope qua Git/Jira và kiểm chứng.

**Đọc khi:** Cần minh họa quy trình; không coi ID hoặc policy mẫu là dữ liệu thật.


<a id="workflow-16"></a>

## Ví dụ đi hết một vòng: baseline cụ thể của phần manual

Toàn bộ tên, ID và quyết định dưới đây là minh họa, chưa phải rule CRM đã được nghiệp vụ phê duyệt.


<a id="workflow-16-1"></a>

### Feature và Epic

- Feature `FEAT-CUS-001`: Tiếp nhận khách hàng mới.
- Epic manual có một Jira key thực tế sau khi tạo; ví dụ minh họa dùng `CRM-101`.
- Epic import làm rõ riêng; chưa cần khóa toàn import mới được làm phần manual độc lập.
- PM đã cho phép tạo Epic manual và phân công BA/Dev/QA làm rõ các hạng mục requirement, solution và testability trên Epic; không tạo Task phân tích mặc định.


<a id="workflow-16-2"></a>

### Đầu ra phân tích và solution

- BR-CUS-01: chỉ người có quyền mới tạo được khách hàng.
- BR-CUS-02: quy tắc chuẩn hóa MST và phạm vi trạng thái phải kiểm trùng đã được Business quyết định.
- AC-CUS-01/02/03: thành công, không quyền và trùng đều có expected result.
- Solution: kiểm ở server để không bypass qua API; có xử lý request đồng thời phù hợp rule.
- QA: có tình huống kiểm chứng, dữ liệu cần chuẩn bị và cách xác nhận không tạo bản ghi thừa.
- Story candidate gồm trọn hành vi tạo manual với quyền/validation/chặn trùng; không đẩy rule an toàn bắt buộc sang một Story sau chỉ để giảm size.


<a id="workflow-16-3"></a>

### PR phải chứa gì?

PR của phần manual chứa hoặc tham chiếu theo version:

1. Section scope/rule chung cần dùng của `docs/features/FEAT-CUS-001.md`.
2. Hồ sơ yêu cầu + solution + AC của manual trong `docs/epics/EPIC-CUS-MANUAL.md`.
3. Manifest `docs/baselines/BASE-CUS-MANUAL-001.yaml`, chỉ liệt kê Story manual đã được duyệt.
4. Contract/UI/NFR dùng chung cần thiết và decision refs.

Business/BA, Dev/TL và QA xác nhận phần chuyên môn liên quan. PM chốt bộ nội dung và manifest trên revision được review. PR merge thành công tạo commit xác định.

**Baseline lúc này là bộ hồ sơ yêu cầu + solution của manual tại commit đó, được định danh `BASE-CUS-MANUAL-001`.** Nó chưa bao gồm code triển khai và không khóa phần import chưa rõ.


<a id="workflow-16-4"></a>

### Sau merge và khi triển khai

1. Service đọc manifest từ commit đã merge, tạo Story manual ở `todo` và ghi Jira key vào receipt.
2. Story trỏ tới baseline, selected BR/AC, solution và evidence review.
3. Nếu dữ liệu test cần cho bước triển khai chưa sẵn: chưa đạt DoR, vẫn `todo`, có owner/due chuẩn bị.
4. Đủ DoR và capacity, PM xếp việc; Dev chuyển `inprogress`.
5. Dev code/unit/API tests; Task code qua review theo tiêu chí. Story chỉ `resolved` sau review/CI/deploy/smoke và bàn giao QA hợp lệ.
6. QA phát hiện bypass quyền: ghi issue, Story về `inprogress` để sửa, rồi qua lại review/CI/deploy/retest.
7. QA Pass + đủ DoD + PM chốt: Story `done`.
8. Epic manual chỉ `done` khi đủ toàn scope và Business nghiệm thu. Nếu đây là Story duy nhất, có thể nghiệm thu ngay khi các điều kiện khác đủ.
9. Feature chưa Accepted nếu Epic import trong scope hiện hành chưa hoàn thành.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
