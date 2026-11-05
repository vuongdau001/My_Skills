# Mẫu báo cáo tiến độ Requirement và Development

Mã tài liệu: **TPL-PROGRESS** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Mở bằng kết quả chính: scope đang ở đâu, blocker nào quan trọng và hành động tiếp theo. Dùng [measurement](../../references/progress-measurement-and-feature-rollup.md); đây là Full report, không ép lên recap/status/next step trong chat.

## Phạm vi và snapshot

Project/Feature/selected scope/revision; ngày giờ/timezone; người lập/xác minh; nguồn trạng thái/query snapshot (Jira hoặc state theo dự án); baseline/manifest và policy/version. Dữ liệu chưa lấy được ghi Unknown; so kỳ cần cùng scope hoặc giải thích delta.

## Phân tích và thiết kế

Index ngắn target/E/S item → work signal → review verdict/gap → next action. Chi tiết dài tách theo target: applicability, output/revision, evidence, owner/reviewer, due/blocker. Tách analysis/solution/testability.

Ghi R_pass/R_app, N/A, applicability Unknown, open blocking findings và phần chưa rõ. Review coverage không là % sản phẩm hoàn thành.

## Baseline và phạm vi Feature

Mapping scope unit/outcome → Epic → baseline/commit; Full/Partial/Chưa có/Chưa xác minh. Ghi shared-rule refs và gap/change. Nêu B/M full units, phần chưa phân bổ và scope thêm/bỏ/split/merge cùng decision refs.

## Development và blocker

Theo Story: status/evidence, Ready/chưa Ready, delivered theo DoD, resolved đang QA/chờ closure và discrepancy. Effort ratio chỉ khi cùng đơn vị, đủ estimate và có coverage/snapshot; Task chỉ giải thích workload/dependency, không đếm lại Story output.

Mỗi blocker: ID/target, owner, opened-at, age/clock, threshold policy hoặc Chưa chốt, next action/escalation và người/hạn. Không đặt SLA khi chưa có policy.

## Acceptance, dự báo và hành động tiếp

Ghi Epic/Feature AC đã kiểm/chưa kiểm/fail với build/evidence, luồng liên Epic và Business acceptance. Lợi ích sau sử dụng đo theo kế hoạch riêng.

Forecast dựa remaining scope, dependency, capacity theo vai trò và uncertainty, không suy ngày từ % review. Chọn hành động cụ thể, người nhận và điều kiện; không tự sửa Jira/state. Thêm metadata Report cuối file.
