# Mẫu register policy dự án

Mã tài liệu: **TPL-POLICY** · Gói CRM 1.3.1 · 03/11/2026

Đọc [hướng dẫn policy](../../references/project-policy-register.md). Copy vào repo dự án; đây là mẫu trống, không phải policy CRM đã duyệt. Dùng Pending cho quyết định chưa có, không tự điền ngưỡng. Các nhóm policy phải xét nằm trong hướng dẫn, không tạo bản thứ hai của định nghĩa tại đây.

## Kiểm soát register

Project/scope; repo/path; revision; policy owner; ngày hiệu lực; nguồn tổ chức/hợp đồng; người duyệt; decision/approval refs. Baseline nào đang tham chiếu register? Nhóm nào còn Pending, chặn gate nào?

| Policy ID + tên | Version/effective scope | Nội dung hoặc ref pinned | Phương pháp đánh giá/inputs | Authority + approval evidence | Decision state | Gate bị ảnh hưởng | Gap/owner/due |
|---|---|---|---|---|---|---|---|
| ID từ policy guide | Chưa chốt nếu chưa biết | Giá trị/định nghĩa/ranh giới cần quyết | Dữ liệu và phép kiểm | Không giả tên/ngày duyệt | Pending/Proposed/Approved/Superseded | Gate cụ thể | Việc cần quyết |

## Chi tiết mỗi policy

Mục đích; applicability; định nghĩa và ví dụ ở ranh giới; threshold nếu cần; cách tính/đơn vị/clock; input/output; owner; reviewer/authority; evidence; cách xử lý thiếu/failed/skipped; quyết định; hiệu lực; impact khi thay đổi. Trường không áp dụng cần reason/authority.

## Ngoại lệ nếu policy cho phép

Policy/version và điều khoản; scope/revision bị ảnh hưởng; lý do/tác động; biện pháp bù; điều kiện không được miễn; authority và decision ref; thời hạn; owner xem lại; gate result riêng. Chưa phê duyệt ngoại lệ thì không coi như đã được miễn.
