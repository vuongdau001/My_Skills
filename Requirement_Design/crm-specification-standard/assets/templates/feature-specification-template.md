# Mẫu hồ sơ Feature

Mã tài liệu: **TPL-FEATURE** · Gói CRM 1.3.1 · 03/11/2026

Đọc [Feature catalog F01–F08](../../references/feature-specification-catalog.md); copy vào repo dự án. Không thêm ticket Feature. Chỉ điền độ sâu cần cho bước hiện tại; mọi giả định/unknown giữ rõ trạng thái.

## Định danh và bước đang xét

Feature ID/title; source refs; canonical repo/path/revision; Business authority; BA/PM owners; bước: giao làm rõ / chốt scope Epic / hoàn tất phân tích / nghiệm thu. Policy refs/versions; selected scope và phần chưa xét.

| Hạng mục | Nội dung hoặc canonical ref/version | Owner/reviewer | Verdict + evidence | Câu hỏi chặn/owner/due |
|---|---|---|---|---|
| F01 — Nguồn và vấn đề | Nguồn, lý do | Người được giao | Chưa kiểm | Gap thực tế |
| F02 — Outcome và cách đánh giá | Outcome + method + condition | Người được giao | Chưa kiểm | Gap thực tế |
| F03 — Stakeholder và authority | Nhóm/đại diện/quyền quyết | Người được giao | Chưa kiểm | Gap thực tế |
| F04 — Phạm vi và ranh giới | In/out/constraints | Người được giao | Chưa kiểm | Gap thực tế |
| F05 — Requirement/control dùng chung | ID/version/applies-to | Người được giao | Chưa kiểm | Gap thực tế |
| F06 — Phân bổ Epic và dependency | Allocation/commitment | Người được giao | Chưa kiểm | Gap thực tế |
| F07 — Acceptance liên Epic | AC/expected/method | Người được giao | Chưa kiểm | Gap thực tế |
| F08 — Quyết định, baseline, nghiệm thu | Scope/revision/approval/evidence | Người được giao | Chưa kiểm | Gap thực tế |

## Outcome và acceptance

| Outcome ID/ref | Loại: acceptance sản phẩm hoặc lợi ích sau sử dụng | Điều kiện đạt/phương pháp | Baseline/target/đơn vị nếu định lượng | Population/window/data source | Owner/authority | Trạng thái quyết định/kết quả |
|---|---|---|---|---|---|---|
| Nguồn thực tế | Phân biệt rõ | Không tự đặt target | Pending nếu thiếu | Kế hoạch thu thập khi chưa đo | Người có quyền | Chưa quyết/chưa đo khác Không đạt |

## Scope allocation

| Scope unit ID | Outcome/in-out ranh giới | Epic nhận trách nhiệm | Shared requirement refs | Dependency + owner | Baseline refs nếu đã có | Gap/change decision |
|---|---|---|---|---|---|---|
| ID ổn định trong Feature | Phạm vi cụ thể | Chưa phân bổ thì ghi gap | IDs/versions | Hai đầu và cam kết | Chưa có không coi đã baseline | Source/reason |

## Quyết định và kết luận

Question/decision IDs; authority; ảnh hưởng scope/acceptance; owner/due; reviewed revision. Kết luận cho đúng bước, không tự coi Epic Done là Feature Accepted. Evidence runtime/build chỉ điền sau khi kiểm thật.
