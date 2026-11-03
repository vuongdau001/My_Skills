# Pilot quy trình bằng Epic và Story thực tế

Mã tài liệu: **CRM-PILOT** · Gói CRM 1.3.1 · 03/11/2026

**Đọc khi:** chuẩn bị áp dụng quy trình hoặc cần chứng minh agent/member dùng tài liệu được. **Đầu vào:** một phạm vi Epic thật có nguồn/authority, một vài Story candidates, repo và quyền truy cập được cho phép. **Đầu ra:** [pilot record](../assets/templates/pilot-review-record-template.md), findings/corrections và quyết định áp dụng. Tài liệu này là kế hoạch, chưa phải pilot đã thực hiện.

## Chọn phạm vi và chuẩn bị

PM chọn scope nhỏ nhưng có data/permission hoặc state để kiểm thực tế; có người Business, Dev/TL và QA tham gia. Có thể bắt đầu một Story trực tiếp không Task; chỉ thêm Task khi có đầu ra giao riêng thật. Không chế tạo Story phức tạp để đủ mọi model.

Ghi mục tiêu pilot, source/scope/revision, roles/authority, policy register, nơi trao đổi và evidence. Kiểm các policy cần cho bước đang pilot; policy chưa chốt phải được phát hiện và giữ gate chưa đạt, không tự đặt giá trị để tiếp tục. Chưa được cấp quyền Jira/Git thì chạy review trên hồ sơ, ghi rõ chưa kiểm integration.

## Các bước và tiêu chí quan sát

| Bước | Thực hiện | Evidence/điều kiện đánh giá |
|---|---|---|
| 1 — Nhận nguồn | BA xác định Feature F01–F08 và selected scope Epic | Người nhận truy được nguồn/authority, in/out scope, unknown; không dùng ví dụ làm policy |
| 2 — Soạn/refine | Dùng E/S catalog và mapping; BA/Dev/QA read-back | Reviewer tìm được model/check cần đọc; AC/expected result không phải đoán |
| 3 — Phản biện | Chọn case thật hoặc bản sao thử thiếu input, flow/quyền mâu thuẫn, revision cũ | Finding có witness/evidence/gate impact; không chấm PASS khi thiếu input |
| 4 — Chốt và bàn giao | Review chuyên môn; PM xét scope/manifest; merge/tạo Story chỉ khi có quyền và đủ gate | Trace authority/revision/commit/receipt; nếu chỉ mô phỏng ghi chưa kiểm hành động thật |
| 5 — Thực hiện có điều kiện | Story đủ DoR đi bằng checklist; Task chỉ nếu cần riêng | Không tạo Task hình thức, không mất effort/owner/QA obligations |
| 6 — Đổi yêu cầu | Trên bản sao hoặc change thật được phép, thay một BR/contract | Tìm được models/Stories/tests ảnh hưởng; old approval không tự chứng minh new revision |
| 7 — Báo cáo | PM lập report từ scope/evidence/Jira snapshot | Số tái tính được; gap/unknown hiện rõ; không đếm Task lặp, không resolved=Done |
| 8 — Review pilot | Các vai trò đánh giá finding, effort và điểm cần sửa | PM chốt correction/retest hoặc phạm vi được áp dụng; thiếu evidence không được gọi pilot đạt |

Không cố ý sửa/hủy dữ liệu dự án thật để thử negative case; dùng bản sao fixture. Nếu pilot chưa có code/build thì chỉ kết luận requirement handoff; không ghi Dev handoff/Story DoD/runtime Pass.

## Tiêu chí kết luận

Đạt cho bước được pilot khi: người nhận tìm đúng context/version; reviewer áp dụng cùng tiêu chí cho các tình huống đã chọn; unknown/counterexample chặn đúng phần; phê duyệt đúng authority; báo cáo truy được về ID/evidence; findings chặn đã sửa và kiểm lại. Bất đồng có record và quyết định, không chỉ đồng ý miệng.

Thu thêm thời gian tìm context, thời gian review, số câu hỏi phát sinh do hồ sơ thiếu, rework sau handoff và bước trùng lặp. Chưa có target thì đây là số quan sát để điều chỉnh quy trình, không là SLA được phê duyệt. Cần ghi phạm vi không kiểm, nhất là automation/hook và test runtime.

Sau pilot, sửa ít nhất đủ để giải quyết findings có căn cứ, cập nhật routing/templates/criteria bị ảnh hưởng và chạy lại structural validator + relevant walkthrough. Không mở rộng checklist chỉ để mọi ví dụ đều thành luật chung.
