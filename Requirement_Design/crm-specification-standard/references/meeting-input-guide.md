# Xử lý biên bản và nguồn họp

ID: CRM-MEETING-INPUT · CRM Workflow Kit 2.7.0

Biên bản/ghi chú họp là **nguồn đầu vào**, không phải Meeting record trong spec. Không tạo MTG ID, metadata kind Meeting, state hoặc template biên bản đầu ra. Giữ nguồn tại input_root/sources hoặc đường dẫn người dùng chỉ định; không tự viết lại bằng chứng gốc.

## Đường dẫn nguồn và context

Lấy đường dẫn từ `workstreams[].sources` trong `.agents/crm-spec-kit.json`, không suy từ `artifact_paths.project`. Có thể khai một thư mục nguồn: context intake liệt kê các file Markdown bên trong với path/hash riêng, kể cả biên bản mới được bổ sung. File nguồn chưa phải record đã đăng ký; cần đọc nội dung thực tế. Các định dạng khác cần đọc bằng công cụ phù hợp. Không scaffold hoặc ghi vào thư mục nguồn; không tự tạo `01-meetings` trong spec, kể cả khi đọc dự án schema 2 cũ.

Ví dụ config cho workspace CRM Phase 3: `{"id":"SRC-MEETINGS","path":"phase-3/sources/inputs/01-meetings","use":"Biên bản đầu vào để phân loại ASM/DEC/CST"}` trong `sources`; giữ `phase-3/sources` trong `read_only`. Đây là đường dẫn dự án, không hardcode vào helper dùng chung. Chỉ dùng `input_root` khi thực sự cần vùng input writable riêng; không đặt nó trùng nguồn read-only.

## Tiếp nhận nội dung

1. Đọc nguồn thực tế, ghi path/revision/hash và locator cần dùng. Người nói hoặc chữ “đã chốt” trong bản tổng hợp chưa tự chứng minh authority.
2. Điều đang tin nhưng chưa xác nhận → Assumption. Lựa chọn/kết luận có căn cứ xác nhận → Decision. Ràng buộc có nguồn → Constraint. Câu hỏi chưa đủ nội dung giữ là gap, không ép thành record.
3. Tìm record hiện có theo ID và nghĩa trước khi tạo; giữ một nơi định nghĩa, không tạo bản sao từ mỗi cuộc họp. Không có state cho DEC/ASM/CST schema 3.
4. Record/consumer dẫn trực tiếp evidence nguồn bằng path/revision/sha256. Không tạo dependency tới một MTG record trung gian. Với Capability/Epic có thể khai evidence ở metadata cấp artifact; record khai trong record.evidence.
5. Khi gặp Meeting record cũ và được giao migration, chuyển sang vùng nguồn đã chọn; giữ locator cũ nếu hữu ích, bỏ registration metadata trong spec và cập nhật toàn bộ link/evidence/hash. Không xóa bằng chứng hoặc tự coi mọi nội dung nguồn đã được xác nhận.

Assumption được xác nhận thì tạo DEC ID, cập nhật consumers rồi xóa ASM; Decision/Constraint sửa hoặc bỏ theo [mô hình không state](knowledge-records-and-evidence.md). Review/check chỉ ghi phát hiện, không tự chỉnh nguồn hoặc record.
