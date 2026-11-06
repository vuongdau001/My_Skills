# Ví dụ phân rã Story và quyết định tạo Task

Mã tài liệu: **EX-DECOMPOSITION** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** So sánh Story trực tiếp, Task liên kết và Task dùng chung.

**Đọc khi:** Review cách chia hoặc onboarding member.


## Phạm vi minh họa

Mọi tên/rule ở đây là giả định để học cách chia. Không có baseline CRM thật được duyệt. [Ví dụ ProjectCodeRequest](project-code-request-specification.md) mô phỏng hai đợt với câu hỏi freshness/hiển thị còn mở ở r2.

Capability **Quản lý Project Code** có các Epic gửi, xét duyệt và đóng nháp. [Bảng phân bổ](project-code-request-specification.md#spec-9-1) ghi mục tiêu, actor, outcome và shared model. Lưu nháp là bước chuẩn bị trong Use Case gửi; Approve/Reject là hai kết cục của Use Case xét duyệt. Kiểm đường đưa request vào hàng đợi trước khi chốt lát Story gửi.

## Story trực tiếp, không Task

Với B, phạm vi gồm tương tác submit, API/data cần cho hành vi, quyền, validation, transition, response và các lỗi/retry/concurrency áp dụng. Giả sử hồ sơ thật đã giải quyết các câu hỏi chặn và qua DoR: một owner điều phối có thể dùng checklist:

- Đọc pinned BR/AC/contract và xác nhận delta solution.
- Triển khai các thành phần cần thiết; viết test theo expected behavior đã duyệt.
- Review, chạy required checks, tích hợp và bàn giao build/config/evidence cho QA.
- QA chạy coverage áp dụng; xử lý findings; PM đóng khi DoD đạt.

Đây là kế hoạch thực hiện, không phải AC. Không phải tạo Task mới được code. Đổi expected outcome trong lúc thực hiện phải quay về change control.

## Cùng Story nhưng có nhu cầu giao việc riêng

Nếu thực sự có các bàn giao riêng, dùng các Task dưới Epic và link `implements / serves Story B` bằng quan hệ thực tế được cấu hình:

| Task đề xuất | Input | Output/tiêu chí đóng | Người nhận |
|---|---|---|---|
| Triển khai submit API và tính nhất quán dữ liệu | Story B + pinned transition/permission/error contract | Code/PR được review, kiểm tra liên quan đạt; evidence state/data/effects theo contract | Story owner/QA |
| Tích hợp UI submit với contract được duyệt | Story B + UI/contract version | Luồng gửi, chờ, lỗi áp dụng được tích hợp; review/test evidence đúng build | Story owner/QA |
| Tự động hóa các kiểm tra retry/concurrency được giao | AC/test conditions và build/test harness | Assertion truy được AC, case chạy đạt và có khả năng phát hiện lỗi; không chỉ snapshot code behavior | QA/technical reviewer |

Mỗi Task điền T01–T08, không sao chép state machine/permission matrix riêng. Các Task có thể hoàn tất nhưng AC tích hợp vẫn fail; Story phải tiếp tục sửa và kiểm chứng. Không bắt tạo ba Task này cho mọi Story.

## Task dùng chung

Một migration bổ sung cấu trúc hỗ trợ versioning cho nhiều Story: một Task thuộc Epic, links tới các Story tiêu thụ. Brief phải có schema/input version, điều kiện dữ liệu, phương án triển khai/khôi phục theo rủi ro, phép đối soát và người nhận. Nếu migration làm đổi nghĩa dữ liệu nghiệp vụ, decision đó phải vào baseline trước; Task không tự quyết mapping. Đóng Task chỉ khi artifact/check/reviewer/receiver đạt; không tự đóng các Story phụ thuộc. Effort tính một lần.

## Phản ví dụ và cách sửa

- “Story tạo DB”, “Story viết API”, “Story viết UI”: hỏi kết quả người dùng/hệ thống nào kiểm chứng được. Nếu chỉ là các lớp của một hành vi, gộp thành Story hành vi rồi cân nhắc Task.
- Một Story lớn quá Sprint với 20 Task: tách outcome nghiệp vụ thành các Story nhỏ có acceptance, không dùng số Task để khẳng định Story đã nhỏ.
- “Task làm rõ quyền approver” để Story submit được Ready: sai nếu quyền chưa rõ ảnh hưởng scope hiện tại. Ghi question/authority/blocker trên hồ sơ yêu cầu; Task không chữa thiếu requirement.
- PoC chứng minh phương án không đủ throughput: Task có thể hoàn tất với evidence hợp lệ và kết luận không khả thi; Story phụ thuộc vẫn chưa Ready, không ghi product acceptance Pass.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
