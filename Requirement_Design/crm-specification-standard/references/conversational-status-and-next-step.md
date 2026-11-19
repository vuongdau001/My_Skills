# Status và next step theo yêu cầu

ID: CRM-CONVERSATIONAL-STATUS · CRM Workflow Kit 3.0.0

Đây là hướng dẫn dùng chung, không là function riêng. Không route sang workflow Report Status.

| Câu hỏi | Cách xử lý |
|---|---|
| Vừa làm gì | Tóm tắt observed actions và kiểm chứng đã có trong lượt; không suy thành current status nếu chưa đọc lại nguồn |
| Đang tới đâu | Đọc canonical target, revision, dependency và nguồn trạng thái hiện hành của dự án |
| Làm gì tiếp | Chọn một bước tháo blocker hoặc tạo output reviewable, giải thích căn cứ và inputs còn thiếu |
| Cần số liệu tổng hợp | Tính tại thời điểm hỏi, khai scope, mẫu số, source refs và Unknown; không lưu report theo kỳ |

Có thể dùng context của workflow áp dụng cho bước tiếp, không cần nạp toàn bộ project để trả recap hẹp. Không suy global active target. Nhiều target hợp lý thì nêu overview và hỏi phần ảnh hưởng quyết định.

Phân biệt draft, review, authority approval, readiness, implementation và acceptance. Không lấy score hoặc số artifact làm % sản phẩm Done. Đối chiếu current evidence; kết quả từ phiên cũ không tự áp dụng cho revision mới. Không bịa capacity, owner hoặc deadline.

Read-only/status trả chat; không tự ghi report/checkpoint/state/ticket. Nếu user yêu cầu xuất bản đọc, thực hiện như artifact export một lần có scope rõ, không tái lập category reports hoặc timeline. Lịch sử qua Git theo [current-state policy](current-state-and-history.md).
