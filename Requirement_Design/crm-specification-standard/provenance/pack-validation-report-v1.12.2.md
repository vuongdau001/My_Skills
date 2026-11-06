# Kiểm chứng CRM Workflow Kit 1.12.2

ID **CRM-VALIDATION-V1122** · 05/11/2026

Bản cập nhật thống nhất các ví dụ Customer–Contact qua phân rã, baseline và bàn giao. Mã đào tạo tách khỏi ID dự án. Mẫu minh họa Use Case ở E03, Story chọn kết quả bàn giao, Task liên kết khi có đầu ra riêng và cách pin Prototype nếu gate áp dụng.

Bộ ví dụ ProjectCodeRequest làm rõ allocation cho draft, submit, quyết định và cancel. Sơ đồ và bảng dùng cùng guard. Finding về cancel phân biệt hành vi từ chối đã rõ với contract lỗi còn thiếu. Verification của submit giữ phạm vi ghi notification intent. Mẫu lệnh dùng target và đường dẫn từ Work Context.

## Kiểm trước khi phân phối

- Kiểm cấu trúc gói và chạy bộ regression tests của helper.
- Đối chiếu cây phân rã, walkthrough và manifest theo cùng case.
- Kiểm guard, allocation, case biên và phạm vi notification trong ProjectCodeRequest.
- Kiểm layout và scope của Prototype mẫu, sau đó dùng update dry-run để xác định các file thay đổi.

Bản nguồn đạt kiểm cấu trúc cho 113 tài liệu Markdown và 166 manifest entries. Bộ regression chạy 155 test và đạt. Đối chiếu nội dung gồm case Customer–Contact, phạm vi baseline, các nhánh ProjectCodeRequest, manifest Prototype và đường dẫn lệnh scoring.
