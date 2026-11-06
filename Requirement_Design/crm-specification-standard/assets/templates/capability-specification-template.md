# Mẫu hồ sơ Capability

Mã tài liệu: **TPL-CAPABILITY** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Mở đầu bằng ID/tên Capability và một đoạn về năng lực, người nhận lợi ích. Dùng bảng hai cột cho revision, bước đang xét, sources, Business/BA/PM owners và policy/approval thực có.

Đọc [Capability catalog](../../references/capability-specification-catalog.md); giữ C01–C08. Chỉ soạn đến độ sâu của bước: giao làm rõ, chốt scope Epic, hoàn tất phân tích hoặc acceptance.

Phân bổ mỗi mục tiêu sử dụng vào một Epic–Use Case. Dẫn nguồn và ghi trách nhiệm từng Epic trong hành trình tích hợp ở Capability.

## C01 — Nguồn và vấn đề

Nêu ai gặp nhu cầu/vấn đề gì, source locator và rationale. Giữ source IDs; phân biệt nội dung nguồn với đề xuất.

## C02 — Outcome và cách đánh giá

Mỗi outcome một mục: loại acceptance/lợi ích sau sử dụng, điều kiện quan sát, cách đánh giá, population/window, owner. KPI có baseline/target/unit nếu được chọn; thiếu thì ghi quyết định Pending.

## C03 — Bên liên quan và trách nhiệm xác nhận

Tách nhóm sử dụng khỏi người review/phê duyệt. Dùng bảng ngắn vai trò → trách nhiệm. Tên người, người thay thế và hạn chưa có thì ghi thiếu.

## C04 — Phạm vi và ranh giới

Tách nội dung trong phạm vi, Capability phụ thuộc, ngoài phạm vi và điểm chưa quyết. Dẫn ASM ID/revision cùng tác động nếu giả định sai. Phạm vi soạn draft khác cam kết release.

## C05 — Requirement và kiểm soát dùng chung

Dẫn ID/revision của requirements, rule, NFR, data/permission/integration/transition. Dẫn CST ID/revision và evidence hiệu lực. Giữ một nơi định nghĩa và phân bổ controls tới consumer thực sự áp dụng.

## C06 — Phân bổ Epic và dependency

Nêu quy ước cấp độ đang dùng, Capability ngang hàng đã đối chiếu và lý do năng lực này cần Capability riêng. Dẫn evidence hiện có hoặc ghi giả định. Với nhóm mới/đổi ranh giới, áp dụng checkpoint chọn cấp: parent/cấp, model/control/acceptance chung, delta bàn giao và rationale gom/tách. Kiểm cha–con lặp nghĩa; quan hệ một–một cần vai trò riêng, không bịa thêm con.

Bảng tra scope unit → Epic/candidate → source/REQ. Giải thích overlap/split; ghi người cung cấp dependency, cam kết/capacity/mốc sơ bộ khi có. Chưa có thì giữ gap.

## C07 — Tình huống nghiệm thu liên Epic

Mỗi tình huống nêu điều kiện, hành vi và kết quả quan sát. Ghi cách kiểm và dependency; chưa coi các ví dụ là test đã thực thi.

## C08 — Quyết định, baseline và bàn giao

Dẫn DEC ID/revision, authority và evidence cho scope áp dụng. Liệt kê câu hỏi và quyết định còn mở. Dẫn baseline/review/approval đúng revision nếu có; ghi receiver và bước tiếp. Epic Done chưa tự Capability Accepted.

## Theo dõi review của từng mục

Dùng index ngắn Item → output/revision → work signal/verdict. Với mỗi mục cần giải thích dài, ghi riêng applicability/reason, reviewer/authority, evidence và gap/owner/due. Work signal không thay verdict. Kết thúc artifact bằng metadata đúng loại, không copy phần hướng dẫn template như nội dung đã đạt.
