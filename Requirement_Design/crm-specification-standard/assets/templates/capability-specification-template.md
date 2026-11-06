# Mẫu hồ sơ Capability

Mã tài liệu: **TPL-CAPABILITY** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Mở đầu bằng ID/tên Capability và một đoạn về năng lực, người nhận lợi ích. Dùng bảng hai cột cho revision, bước đang xét và nguồn. Dẫn Work Context cho người soạn, reviewer và người điều phối bàn giao.

Đọc [Capability catalog](../../references/capability-specification-catalog.md); giữ C01–C08. Chỉ soạn đến độ sâu của bước: giao làm rõ, chốt scope Epic, hoàn tất phân tích hoặc acceptance.

Phân bổ mỗi mục tiêu sử dụng vào một Epic–Use Case. Dẫn nguồn và ghi trách nhiệm từng Epic trong hành trình tích hợp ở Capability.

## C01 — Nguồn và vấn đề

Nêu ai gặp nhu cầu/vấn đề gì, source locator và rationale. Giữ source IDs; phân biệt nội dung nguồn với đề xuất.

## C02 — Outcome và cách đánh giá

Mỗi outcome một mục: loại acceptance/lợi ích sau sử dụng, điều kiện quan sát, cách đánh giá, nhóm quan sát, thời gian đo và người phụ trách đo kết quả. KPI có baseline/target/unit nếu được chọn; thiếu thì ghi quyết định Pending.

## C03 — Bên liên quan nghiệp vụ

Ghi nhóm sử dụng, hưởng lợi, chịu tác động hoặc có quyền lợi cần bảo vệ, cùng nhu cầu và tác động quan sát được. Khi một nhóm trực tiếp tham gia Use Case, dẫn đến actor ở Epic tương ứng. Dẫn C08 cho thẩm quyền xác nhận nghiệp vụ và Work Context cho vai trò dự án, review và bàn giao. [Quy ước vai trò](../../references/artifact-writing-standard.md#business-and-sdlc-roles).

## C04 — Phạm vi và ranh giới

Tách nội dung trong phạm vi, Capability phụ thuộc, ngoài phạm vi và điểm chưa quyết. Dẫn ASM ID/revision cùng tác động nếu giả định sai. Phạm vi soạn draft khác cam kết release.

## C05 — Requirement và kiểm soát dùng chung

Dẫn ID/revision của requirements, rule, NFR, data/permission/integration/transition. Dẫn CST ID/revision và evidence hiệu lực. Giữ một nơi định nghĩa và phân bổ controls tới consumer thực sự áp dụng.

## C06 — Phân bổ Epic và dependency

Dẫn kết quả [xác định vị trí lát cắt trong dự án](../../references/source-scope-and-decomposition-checkpoint.md#project-placement). Ghi nguồn phạm vi và revision, locator, Capability/Epic hiện có và các nhóm liền kề đã đối chiếu. Giải thích vì sao cấp cha được chọn, cùng phạm vi, quy tắc dùng chung hoặc tiêu chí nghiệm thu mà nó sở hữu. Nêu điểm khác giữa kết quả của Capability và mục tiêu người dùng của từng Epic trong đợt. Một Epic trong đợt đầu là đủ khi nguồn chứng minh vai trò riêng của cấp cha.

Bảng tra scope unit → Epic/candidate → source/REQ. Giải thích overlap/split; ghi người cung cấp dependency, cam kết/capacity/mốc sơ bộ khi có. Chưa có thì giữ gap.

## C07 — Tình huống nghiệm thu liên Epic

Mỗi tình huống nêu điều kiện, hành vi và kết quả quan sát. Ghi cách kiểm và dependency; chưa coi các ví dụ là test đã thực thi.

## C08 — Quyết định, baseline và bàn giao

Ghi riêng quyết định và người có thẩm quyền xác nhận nghiệp vụ, cùng ID, revision, phạm vi và evidence. Đặt vai trò review, người chốt baseline và người nhận bàn giao ở phần SDLC hoặc dẫn Work Context. Nếu một người kiêm vai trò, ghi từng trách nhiệm. Giữ các câu hỏi và quyết định còn mở đúng nhóm.

## Theo dõi review của từng mục

Dùng index ngắn Item → output/revision → work signal/verdict. Với mỗi mục cần giải thích dài, ghi riêng applicability/reason, reviewer/authority, evidence và gap/owner/due. Work signal không thay verdict. Kết thúc artifact bằng metadata đúng loại, không copy phần hướng dẫn template như nội dung đã đạt.
