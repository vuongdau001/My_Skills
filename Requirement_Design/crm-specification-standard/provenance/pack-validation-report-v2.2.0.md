# Kiểm chứng CRM Workflow Kit 2.2.0

Ngày 16/11/2026. Thay đổi: thêm reset sạch toàn dự án theo yêu cầu bỏ toàn bộ artifacts cũ và cấp lại ID từ 001. Không thêm workflow nghiệp vụ; vẫn giữ 13 functions.

## Hành vi đã triển khai

- `kit.py reset --scope project`: dry-run không ghi file; apply cần plan SHA-256 khớp bytes/config/danh sách xóa và giữ allocation/operation locks.
- Xóa artifacts, snapshots/history, review, baseline, score/assessment, Prototype và reservations thuộc output roots. Không tạo archive, namespace theo đợt hoặc persistent reset receipt chứa lịch sử cũ.
- Bảo vệ sources/input_root/read_only/config/kit/instructions. Khai `generated_output_paths` cho outputs ngoài spec_root; output CRM nhận diện được nhưng chưa có ownership chặn trước xóa. Agent vẫn cần khảo sát file không có schema nhận diện.
- ID duy nhất toàn dự án, không reset riêng workstream. Instructions không chiếm số; sau reset từng prefix từ 001. Tiếp tục/sửa bình thường vẫn giữ ID/revision và reservations.
- Cập nhật SKILL/Start Here/INSTALL, policy ID và Setup Project; hướng dẫn doctor/context Setup sau reset, không kế thừa approval/maturity cũ.

## Kiểm đã chạy

- Bộ hồi quy đầy đủ tại thời điểm có 7 test reset đầu tiên: **182 tests, PASS** (`python3 -m unittest discover -s scripts/tests -v`).
- Bộ reset cuối bổ sung kiểm bản cài tự chứa và mọi prefix: **8 tests, PASS** (`python3 -m unittest discover -s scripts/tests -p test_clean_reset.py -v`).
- Reference pack validator: PASS; registry vẫn 13 workflow functions. Chạy lại validator sau khi ghi report này.

Fixtures là repo tạm, gồm nhiều workstream, nguồn BA có ID cao, instructions có ID mẫu, output/history ngoài spec_root, ledger đã reserve; xác nhận khởi tạo lại từ 001 và doctor/lint sau reset. Negative cases kiểm plan stale/thiếu digest, overlap source/read_only/tools/traversal, symlink, lock đang tồn tại và output chưa khai ownership; không xóa dữ liệu khi preflight từ chối.

## Giới hạn

Không reset repo pilot hoặc update bản cài trong repo người dùng. Không sửa Git/Jira/CI; không xóa external backups hoặc nguồn/baseline chỉ đọc. Không test tính nguyên tử khi mất điện hoặc lỗi I/O sau lần xóa đầu tiên; thao tác không có rollback/archive, trường hợp gián đoạn phải kiểm phần còn lại và lập dry-run mới. Locks không ngăn editor/công cụ ngoài hoặc clone khác. Kết quả test không là approval nghiệp vụ/runtime acceptance.
