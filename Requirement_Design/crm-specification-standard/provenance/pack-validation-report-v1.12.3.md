# Kiểm chứng CRM Workflow Kit 1.12.3

ID **CRM-VALIDATION-V1123** · 06/11/2026

Bản cập nhật đưa phép kiểm chọn cấp và quan hệ cha–con vào checkpoint đã được context mặc định nạp. Workflow, catalog và template dùng chung quy tắc: tìm parent hiện có, giải thích cấp độ, kiểm lặp outcome và giữ control trong Story. Quan hệ một–một có căn cứ và Feature tìm kiếm lớn vẫn được phép. Không đổi schema hoặc thêm approval gate.

## Phạm vi kiểm

Kiểm cấu trúc gói, regression helper, context mặc định và walkthrough các case phân rã. Walkthrough do tác giả tự kiểm; không thay forward-test phiên mới hoặc independent review. 

## Walkthrough của tác giả

Đối chiếu quy tắc với LV01–LV07 trong [acceptance scenarios](../references/pack-acceptance-scenarios.md). Đây là self-check nội dung, chưa có output agent độc lập.

| Case | Quyết định khi áp dụng checkpoint | Giới hạn |
|---|---|---|
| LV01 | Cùng lookup/AC qua ba cấp không có vai trò cha riêng; đề xuất đặt Story vào Epic hồ sơ hiện có, giữ guard quyền. | Review ghi finding, chưa sửa cây dự án. |
| LV02 | Tìm kiếm nhiều nguồn có thể là Feature; cần nêu năng lực, contracts và acceptance để chọn Epic. | Không ép số Epic hoặc invent policy. |
| LV03 | Một Story trong release được phép; hồ sơ Epic giữ model/contract/baseline riêng và dẫn ref. | Không tạo thêm con giả. |
| LV04 | Filter là delta của phạm vi tra cứu hiện có; sizing quyết định bổ sung Story hay thay scope theo change control. | Không tự mở Feature hoặc sửa baseline. |
| LV05 | Hai màn hình cùng hoàn thành một mục tiêu chưa chứng minh hai giá trị bàn giao; giữ lát tích hợp khi chưa có căn cứ tách. | Không suy effort từ số màn hình. |
| LV06 | Tạo Contact và gắn có dependency giữa hai scope; Story gắn giữ auto Active cùng outcome và đọc lại để kiểm chứng. | Use Case có owner/ref; chưa xác nhận policy ngoài input. |
| LV07 | Ba tên là dấu hiệu cần kiểm scope/AC và parent, chưa đủ kết luận sai. | Không cấp verdict cho allocation chưa được đọc. |

Các quy tắc phân biệt được case gom và case tách trong walkthrough. Độ ổn định giữa model/máy và discovery phiên mới vẫn cần forward-test; unit tests không chứng minh điều đó.

## Kiểm công cụ và phạm vi thay đổi

- Structural validator đạt với 114 tài liệu Markdown và 167 manifest entries. Lỗi anchor trong lượt đầu đã được sửa bằng anchor tường minh trước kiểm lại.
- Skill quick validator đạt.
- Context mặc định của define-feature, specify-epic, prepare-stories và review-specification đều chứa nguyên checkpoint mới đúng một lần; không cần full mode hoặc mở link thủ công để thấy quy tắc tối thiểu.
- Không sửa helper/schema; regression hiện có kiểm phân phối toàn bộ checkpoint qua install/context và giữ nguồn chỉ đọc.
- 21 file pilot được đối chiếu hash trước/sau và giữ nguyên. Không sửa allocation, source requirement hoặc cấp approval sản phẩm.
- Regression sau sửa anchor đạt 155/155 test (54.957 giây). Lượt chạy trước sửa anchor thất bại ở package validation; không dùng lượt đó làm evidence đạt.
