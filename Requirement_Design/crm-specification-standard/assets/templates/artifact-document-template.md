# Mẫu artifact CRM dùng chung

ID: TPL-ARTIFACT-DOCUMENT · CRM Workflow Kit 1.10.0

Dùng [standard viết artifact](../../references/artifact-writing-standard.md) và catalog/schema của loại đang soạn. Mẫu này dành cho loại chưa có template riêng, như source/question register, model/solution hoặc baseline/change record. Chỉ giữ mục áp dụng; không tạo artifact giả để điền mẫu.

## Tiêu đề và ý chính

ID nếu có và tên mục đích. Một đoạn nêu artifact giúp ai làm gì hoặc ghi nhận kết quả scoped nào.

## Bối cảnh cần biết

| Thông tin | Giá trị thực tế |
|---|---|
| Loại / target / scope | Chọn loại schema hỗ trợ và đúng phạm vi được giao |
| Revision / nguồn | Working revision hoặc baseline/source ref có thật |
| Người soạn / review / authority | Ghi đúng vai trò, cá nhân và evidence; thiếu thì nêu rõ |
| Trạng thái | Vocabulary hợp lệ, khác với mức hoàn thiện trình bày |

## Nội dung chính

Chia mục theo câu hỏi người nhận cần trả lời và catalog áp dụng. Dùng đoạn ngắn giải thích; bảng cho so sánh/mapping; danh sách đánh số cho flow. Với từng record/rule/AC dài, dùng một mục riêng thay bảng quá rộng.

## Điểm chưa chốt và bàn giao

Mỗi gap có ID/locator, câu hỏi, phần bị ảnh hưởng và người cần trả lời. Ghi output tiếp theo và điều kiện để bắt đầu, không tự điền approval hoặc actual action.

## Metadata cuối artifact

Thêm một block từ [metadata template](artifact-metadata-template.md), chọn đúng kind/schema. Knowledge records dùng template schema 2 tương ứng. Có thể bọc bằng details/summary; không sao chép ID minh họa hoặc biến template này thành một definition dự án thật.
