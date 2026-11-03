# Mẫu Task triển khai

Mã tài liệu: **TPL-IMPLEMENTATION-TASK-TEMPLATE** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Sao chép phần mẫu để tạo hồ sơ thực tế; không để trống rồi đánh dấu đạt.

**Đọc khi:** Sau khi đọc catalog và các hướng dẫn áp dụng.


## Hướng dẫn sử dụng

Đọc [Task planning và completion](../../references/task-planning-and-completion.md) trước. Chỉ copy phần hồ sơ dưới đây. Trạng thái ban đầu của brief là chưa kiểm; tiêu chí chưa có phải ghi gap, không đánh dấu đạt.

## Hồ sơ Task

| Hạng mục | Nội dung thực tế cần điền |
|---|---|
| Task ID / Jira key / revision | ID thực tế; chưa tạo Jira thì logical ID |
| T01 — Liên kết và mục đích | Epic; Story được phục vụ; BR/AC hoặc đầu ra được giao |
| T02 — Đầu ra và ranh giới | Artifact/kết quả, in/out scope; lý do cần Task thay vì checklist |
| T03 — Đầu vào và phiên bản | Baseline + repo/commit/path/model/contract; environment/quyền |
| T04 — Kế hoạch và constraint | Bước chính, giới hạn, phạm vi AI được phép hỗ trợ |
| T05 — Dependency và bàn giao | Input cần trước khi bắt đầu; owner dependency; người nhận output |
| T06 — Owner, reviewer, timebox | Người thực hiện/kiểm; estimate/capacity; mốc báo nếu vượt dự kiến |
| T07 — Tiêu chí hoàn tất | Điều kiện + phép kiểm + expected result theo output |
| T08 — Evidence và closure | PR/SHA/build/run/log áp dụng; reviewer + receiver + revision + thời điểm |

### Kiểm điều kiện bắt đầu và hoàn tất

| Bước/tiêu chí | Thao tác kiểm | Evidence/ref + revision | Verdict | Reviewer | Gap/owner/due |
|---|---|---|---|---|---|
| DoR hoặc completion criterion thực tế | Cách kiểm đã làm | Ref thực tế, chưa có thì ghi thiếu | Chưa kiểm / Không đạt / Đạt / N/A có lý do | Người được giao | Hành động còn thiếu |

### Kết quả bàn giao

Output version; các tiêu chí đạt/chưa đạt; receiver acceptance; remaining work; impact tới Story; thay đổi cần trả về baseline. Không ghi Story Done từ kết quả Task.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../../references/requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../../references/standards-and-crm-tailoring.md).
