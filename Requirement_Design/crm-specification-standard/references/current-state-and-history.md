# Hồ sơ hiện hành và lịch sử qua Git

ID: CRM-CURRENT-STATE · CRM Workflow Kit 3.0.0

Kit giữ một bản hiện hành cho mỗi đối tượng và tính kết quả có thể suy ra khi được hỏi. Stateless không xóa dữ liệu nghiệp vụ hoặc evidence cần xác minh; nó bỏ state ẩn và bản sao lịch sử do mỗi lần chạy sinh ra.

## Canonical artifacts

- Giữ ID, đường dẫn ổn định và revision hiện hành khi cùng một đối tượng thay đổi. Không tạo thư mục theo đợt hoặc file r1/r2/ngày chạy để giữ bản cũ.
- Review/check/assessment có một vị trí ổn định theo target và scope đánh giá. Thay thế kết quả hiện hành khi thực sự review lại; không nối timeline vào record.
- Lịch sử, delta và lý do qua Git diff/commit khi được giao. File chưa commit chưa có lịch sử Git được bảo đảm; nói rõ giới hạn, không tạo history/archive để giả lập.
- Findings chưa xử lý và questions chưa quyết vẫn là nội dung hiện hành. Không xóa chúng để làm hồ sơ trông hoàn tất.
- Assessment JSON là input đánh giá hiện hành của reviewer; kết quả score được tính lại từ assessment và evidence, chỉ xuất stdout.

## Evidence và approval

Review chỉ có hiệu lực cho target/scope/revision/hash đã xét. Khi target đổi, kết quả cũ không áp dụng cho nội dung mới. Ghi rõ cần đánh giá lại; không đổi hash, ngày hoặc reviewer để giữ verdict. Approval dùng evidence thật từ người/hệ thống có thẩm quyền khi policy dự án yêu cầu; config hay kết quả lint không cấp approval.

Nếu dự án có nhiều phiên bản đang được triển khai đồng thời, consumer dẫn commit/revision cụ thể; Git chứa nội dung cũ. Không thêm bản sao spec để giữ lịch sử. Không thay mọi consumer sang latest commit khi tác động chưa được đánh giá.

## Status và next step

Đọc canonical artifacts, dependency và nguồn trạng thái được dự án chỉ định. Trả recap/current status/next step trong chat; không tạo report, checkpoint hoặc active-target file từ câu hỏi read-only. Unknown giữ Unknown. Số lượng file hoặc điểm maturity không là tiến độ triển khai.

## Retired workflows

Từ 3.0.0 không có nghiệp vụ Prepare Baseline, Report Status hay Run Pilot. Không scaffold các category baselines/reports/pilot, không tạo Baseline/Report/Pilot artifacts hoặc BASE IDs mới. Metadata và ID lịch sử vẫn có thể đọc để migration; chúng không cấp quyền mở lại workflow đã bỏ.

Nội dung requirement, solution, Story allocation, Prototype và review được tham chiếu trực tiếp từ bản canonical. Readiness, handoff, completion và impact assessment giữ chức năng riêng; không bắt chuẩn bị package/receipt hoặc merge Git như một gate mặc định. Dự án có policy được duyệt yêu cầu merge/approval vẫn phải kiểm evidence tương ứng.

## Nâng cấp và migration

Update package chỉ thay managed kit, không xóa/migrate output dự án. Workstream cũ giữ paths hiện có, kể cả 09-prototypes; workstream mới dùng layout_version 3 và 06-prototypes. Chạy plan-layout để xem candidate config, moves và inbound references trước khi migration được giao riêng.

Kiểm inventory các folder đã bỏ, xác định nội dung còn cần trong hồ sơ hiện hành và consumer cần đổi. Không chuyển toàn bộ sang archive khác. File dự án chưa được Git theo dõi cần xử lý preservation rõ ràng trước khi xóa; update không tự commit để thực hiện việc đó.

Package receipt và backup rollback là dữ liệu quản trị cài đặt, không là nghiệp vụ Baseline/Pilot hoặc lịch sử spec. Giữ ngoài runtime skill discovery; không tạo backup theo từng lần author/review.
