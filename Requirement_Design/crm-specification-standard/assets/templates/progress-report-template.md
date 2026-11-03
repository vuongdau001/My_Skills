# Mẫu báo cáo tiến độ Requirement và Development

Mã tài liệu: **TPL-PROGRESS** · Gói CRM 1.3.1 · 03/11/2026

Dùng [quy tắc đo/tổng hợp](../../references/progress-measurement-and-feature-rollup.md). Đây là mẫu, không phải báo cáo có dữ liệu thật.

## Phạm vi báo cáo

Project/Feature IDs; scope revision; snapshot date/time/timezone; Jira/query snapshot refs; Git baseline/manifest refs; policy versions (clock, SLA, severity/risk); người lập/xác minh; dữ liệu chưa lấy được. So sánh kỳ trước với cùng scope hoặc giải thích change.

## Phân tích/thiết kế theo hạng mục

| Epic/scope/revision | E/S ID + tên | Applicability | Work signal | Review verdict/evidence | Owner/reviewer | Due/blocker | Next action |
|---|---|---|---|---|---|---|---|
| Scope thực tế | Hạng mục cụ thể | Áp dụng/N/A/Unknown | Chưa làm/Đang làm/Chờ review/Đã xác nhận | Không suy từ work signal | Người được giao | Timestamp/reason | Ai làm gì |

Summary: R_pass/R_app; N/A; applicability Unknown; open blocking findings; phạm vi chưa được làm rõ. Không gọi review coverage là % sản phẩm hoàn thành.

## Baseline và phạm vi Feature

| Scope unit/outcome | Epic | Baseline/commit refs | Full/Partial/Chưa có/Chưa xác minh | Shared rule refs | Gap/change |
|---|---|---|---|---|---|
| Unit có ranh giới | Epic nhận | Refs nếu có | Bằng chứng phạm vi đã phủ | Pinned refs | Phần còn lại |

B/M full baseline units; units chưa xác định/phân bổ; scope thêm/bỏ/split/merge trong kỳ và decision refs.

## Development và blocker

Story counts theo status; Ready/chưa Ready; delivered có DoD evidence; resolved đang QA/chờ closure; discrepancies status/evidence. Effort ratio chỉ khi cùng đơn vị và đủ estimate; ghi estimate coverage và snapshot. Task chỉ để giải thích workload/dependency, không đếm lại đầu ra Story.

| Story/Task ID | Status + evidence | Owner | Blocker/review opened-at | Age + clock | Threshold policy hoặc Chưa chốt | Next action/escalation |
|---|---|---|---|---|---|---|
| ID thực tế | Nguồn snapshot | Người được giao | Timestamp | Cách tính rõ | Không tự gán SLA | Người/hạn |

## Acceptance và dự báo

AC Epic/Feature đã kiểm/chưa kiểm/fail; build/evidence; luồng liên Epic; Business acceptance decision. Lợi ích sau sử dụng: kế hoạch đo/kết quả riêng. Forecast ghi remaining scope, dependency, capacity theo vai trò và uncertainty; không suy ngày hoàn thành từ % review.
