# Mẫu pilot và quyết định áp dụng

Mã tài liệu: **TPL-PILOT** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Nêu mục tiêu, bước cần kiểm và kết quả scoped nếu đã quan sát. Theo [pilot procedure](../../references/pilot-and-operational-validation.md); chưa có evidence giữ Chưa kiểm.

## Bối cảnh thử

Pilot ID/date; Feature/Epic/Story/target refs; scope/revision; nguồn/policy/version; participants/roles và quyền được cấp. Nêu môi trường thật/bản sao, phần không kiểm.

## Từng scenario

Mỗi scenario một mục:

- **Input/setup:** context/version, môi trường và người thực hiện/reviewer.
- **Kết quả mong đợi:** decision/rule ref trước khi thử.
- **Quan sát:** action/decision thực tế và evidence; chưa chạy thì ghi chưa kiểm.
- **Kết luận:** verdict/finding scoped, owner/due và correction/retest.

## Dữ liệu đo và giới hạn

Thời gian tìm context/review, câu hỏi thiếu input, rework/bước lặp, nguồn đo và clock. Ngưỡng chưa chốt không tự là SLA.

## Bàn giao PM/authority

Ghi scope/version đủ evidence, findings chặn, phần chưa kiểm, corrections/owners/due và phạm vi thử lại. Pilot tài liệu chưa chứng minh hook Jira/CI hoặc sản phẩm; Story Done cần evidence sản phẩm riêng. Thêm metadata Pilot cuối file.
