# Mẫu hồ sơ Feature

Mã tài liệu: **TPL-FEATURE** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Mở đầu bằng ID/tên Feature và một đoạn về năng lực, người nhận lợi ích. Dùng bảng hai cột cho revision, bước đang xét, sources, Business/BA/PM owners và policy/approval thực có.

Đọc [Feature catalog](../../references/feature-specification-catalog.md); giữ F01–F08. Chỉ soạn đến độ sâu của bước: giao làm rõ, chốt scope Epic, hoàn tất phân tích hoặc acceptance.

## F01 — Nguồn và vấn đề

Nêu ai gặp nhu cầu/vấn đề gì, source locator và rationale. Giữ source IDs; phân biệt nội dung nguồn với đề xuất.

## F02 — Outcome và cách đánh giá

Mỗi outcome một mục: loại acceptance/lợi ích sau sử dụng, điều kiện quan sát, cách đánh giá, population/window, owner. KPI có baseline/target/unit nếu được chọn; thiếu thì ghi quyết định Pending.

## F03 — Bên liên quan và trách nhiệm xác nhận

Tách nhóm sử dụng khỏi người review/phê duyệt. Dùng bảng ngắn vai trò → trách nhiệm. Tên người, người thay thế và hạn chưa có thì ghi thiếu.

## F04 — Phạm vi và ranh giới

Tách nội dung trong phạm vi, capability phụ thuộc, ngoài phạm vi và điểm chưa quyết. Phạm vi soạn draft khác cam kết release.

## F05 — Requirement và kiểm soát dùng chung

Dẫn ID/revision của requirements, rule, NFR, data/permission/integration/transition. Giữ một nơi định nghĩa và phân bổ controls tới consumer thực sự áp dụng.

## F06 — Phân bổ Epic và dependency

Bảng tra scope unit → Epic/candidate → source/REQ. Giải thích overlap/split; ghi người cung cấp dependency, cam kết/capacity/mốc sơ bộ khi có. Chưa có thì giữ gap.

## F07 — Tình huống nghiệm thu liên Epic

Mỗi tình huống nêu điều kiện, hành vi và kết quả quan sát. Ghi cách kiểm và dependency; chưa coi các ví dụ là test đã thực thi.

## F08 — Quyết định, baseline và bàn giao

Liệt kê decision/question, authority và scope bị ảnh hưởng. Dẫn baseline/review/approval đúng revision nếu có; ghi receiver và bước tiếp. Epic Done chưa tự Feature Accepted.

## Theo dõi review của từng mục

Dùng index ngắn Item → output/revision → work signal/verdict. Với mỗi mục cần giải thích dài, ghi riêng applicability/reason, reviewer/authority, evidence và gap/owner/due. Work signal không thay verdict. Kết thúc artifact bằng metadata đúng loại, không copy phần hướng dẫn template như nội dung đã đạt.
