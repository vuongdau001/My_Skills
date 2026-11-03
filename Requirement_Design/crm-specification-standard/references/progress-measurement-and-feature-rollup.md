# Đo tiến độ phân tích, triển khai và tổng hợp lên Feature

Mã tài liệu: **CRM-MEASUREMENT** · Gói CRM 1.3.1 · 03/11/2026

**Đọc khi:** PM báo cáo, lập ready buffer hoặc kiểm scope đã bàn giao. **Đầu vào:** scope register/revision, E/S/F review records, baseline receipts, Jira snapshot và acceptance evidence. **Đầu ra:** [báo cáo tiến độ](../assets/templates/progress-report-template.md) có thời điểm, mẫu số, nguồn và gaps.

## Đơn vị đo và dữ liệu nguồn

Giữ riêng ba mặt: phân tích/thiết kế, triển khai, nghiệm thu. Không tạo một “% hoàn thành Feature” trộn ba mặt này. Tài liệu Git giữ scope/policy/baseline; trạng thái động lấy từ Jira cùng snapshot time. Thiếu access/Jira snapshot phải ghi Unknown, không dùng trạng thái cũ như hiện tại.

Scope unit là phần phạm vi có ID, outcome/in-out và Epic nhận trách nhiệm trong Feature allocation, có thể baseline riêng khi thật sự độc lập. Nó không phải issue type mới. Định nghĩa unit trước khi báo cáo; không tách nhỏ unit đã đạt để làm đẹp số. Nếu scope chưa phân rã đủ, báo phần chưa xác định thay vì tuyên bố đã bao phủ toàn Feature. [Mẫu Feature](../assets/templates/feature-specification-template.md).

Readiness record theo từng E01–E16/S01–S12 áp dụng: target + selected scope + revision + item ID/tên + work signal + applicability + review verdict + output/evidence + owner/reviewer + due/blocker. Work signal Chưa làm/Đang làm/Chờ review/Đã xác nhận khác verdict Chưa kiểm/Không đạt/Đạt/N/A. Đã xác nhận phải có verdict/revision/evidence hợp lệ, không suy từ status Jira.

## Chỉ số và cách tính

| Chỉ số | Định nghĩa/cách tính | Cách đọc và điều kiện |
|---|---|---|
| Review coverage | R_pass / R_app; R_app là số hạng mục áp dụng đã xác định; R_pass là phần đã review Đạt đúng revision | Báo riêng N/A và applicability còn Unknown. R_app=0 → N/A, không 100%. Đây là coverage review, không % effort/sản phẩm |
| Gap/blocker | Số finding/câu hỏi chặn còn mở, theo scope/owner; liệt kê E/S IDs | Một blocker quan trọng vẫn chặn gate dù coverage cao; không lấy trung bình |
| Baseline coverage theo unit | Danh sách B/M scope units: B có baseline hợp lệ phủ đúng unit, M là units hiện hành được định nghĩa | Báo số lượng và tên units, không gọi B/M là % giá trị; unit partial chưa vào B, ghi phần đã baseline riêng |
| Story readiness | Số Story chưa bắt đầu có DoR evidence hiện hành; số chưa đạt và nguyên nhân | Không cộng resolved/done vào ready buffer. Nếu có effort/capacity, ghi từng vai trò/đơn vị và dependency |
| Delivery counts | Đếm Story theo todo/inprogress/pending/resolved/done/cancel tại snapshot | Chỉ done có DoD hợp lệ mới là delivered; cancelled theo dõi riêng; không suy QA Pass từ resolved |
| Delivery theo effort, khi dự án dùng | Tổng estimate của Story Done / tổng estimate của Story trong scope hiện hành, cùng phương pháp/đơn vị/team | Tùy chọn, phải ghi estimation snapshot; thiếu estimate → báo coverage thiếu, không cho estimate=0. Không cộng points khác team, không coi là % giá trị |
| Review age / blocker age | Review age = snapshot − lúc gửi đủ input để review; blocker age = snapshot − lúc blocker mở | Mặc định báo elapsed giờ liên tục và timestamp/timezone. Nếu POL-REVIEW/BLOCKER chọn working clock thì dùng calendar đã duyệt, ghi rõ. Chưa có threshold không gán overdue màu đỏ giả |
| Acceptance coverage | Số AC Epic/Feature áp dụng đã kiểm đạt / tổng AC áp dụng của scope revision, kèm unknown và evidence build | Chỉ là coverage acceptance; Feature Accepted còn cần Business quyết định và full scope, không tự suy từ tỷ lệ |

Status Jira và evidence không khớp thì báo discrepancy, không tự sửa ticket hay tính là đã đạt. Unknown scope/applicability/estimate phải hiển thị cạnh chỉ số, không lặng lẽ bỏ khỏi mẫu số. Evidence bị thay revision invalidate thì chuyển về chưa xác nhận cho revision mới.

## Quy tắc tổng hợp lên Feature

1. Chốt Feature revision, scope units/Epic allocation và snapshot time. Liệt kê gaps chưa phân bổ, units partial và thay đổi scope trong kỳ.
2. Với phân tích: tổng hợp readiness theo `(Epic, selected scope, item ID, revision)` và list blocker. Cùng E07 ở hai scope có thể là hai review units; không nhập làm một, cũng không gọi hai lần review là hai requirement.
3. Với baseline: đối chiếu từng scope unit với manifest/commit và shared rules; chỉ full coverage đã duyệt mới vào B. Một unit nhiều baseline refs vẫn đếm một lần.
4. Với triển khai: union logical Story IDs/Jira mappings của Feature, tránh đếm lại cùng Story qua nhiều refs. Task dùng chung chỉ là dependency/effort một lần, không cộng vào số Story delivered. Shared work cross-Feature không nhân effort toàn dự án; nếu chia effort phải có allocation được duyệt.
5. Với nghiệm thu: kiểm AC/luồng liên Epic và quyết định Business. Epic Done không đủ nếu cross-Epic flow hoặc acceptance còn thiếu. Lợi ích sau sử dụng báo riêng, không suy từ Feature Accepted.
6. So kỳ trước: scope added/removed/split/merged, thay estimate và baseline revision phải hiển thị. Không silently giảm denominator khi cancel; chỉ loại khỏi scope hiện hành sau quyết định thay scope hợp lệ, giữ lịch sử và chênh lệch.

Không lấy trung bình phần trăm của các Epic khác kích thước. Mặc định báo counts + trạng thái từng scope. Nếu cần tỷ lệ effort có điều kiện như bảng; trọng số/đơn vị phải được chốt trước và không đổi để làm đẹp báo cáo.

## Ví dụ tính — giả định minh họa

Epic có 16 hạng mục: 14 áp dụng, 2 N/A được xác nhận; 12 hạng mục Đạt, 2 Không đạt tại E05/E07. Báo **12/14 review đạt, 2 N/A, 2 gap chặn**; không báo Epic hoàn thành 86%. Nếu có thêm applicability Unknown phải hiện riêng, không gọi scope đã review đầy đủ.

Feature có 3 scope units được định nghĩa: manual đã baseline đầy đủ; import mới baseline một phần; migration chưa baseline. Báo **1/3 units full baseline**, ghi phần import đã chốt; không nói 33% effort hoặc giá trị.

5 Story trong scope: 2 Done, 1 resolved, 1 inprogress, 1 todo. Báo 2 Story delivered; resolved chờ QA/closure theo evidence. Task kỹ thuật phục vụ 3 Story vẫn chỉ có một record/effort. Tất cả Epic Done nhưng một AC liên Epic chưa kiểm thì Feature chưa Accepted.

## Kiểm báo cáo trước gửi

PM/BA đối soát scope/version/mẫu số; Dev/QA xác nhận evidence và blockers phần mình. Thử truy ngược mỗi số tới danh sách ID; so với kỳ trước; kiểm không đếm lặp/cancel/unknown. Đạt khi số tái tính được và ý nghĩa đúng; thiếu nguồn ghi chưa xác minh, có mismatch ghi finding. Báo cáo không tự cấp quyền chuyển gate.

Liên quan: [Jira/status](jira-status-and-progress-reporting.md), [policy/clock/escalation](project-policy-register.md), [gate](readiness-completion-and-approval-gates.md).
