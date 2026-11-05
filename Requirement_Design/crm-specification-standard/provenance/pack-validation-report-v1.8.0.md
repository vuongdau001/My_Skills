# Kiểm chứng CRM Workflow Kit 1.8.0

ID: CRM-VALIDATION-V18 · 05/11/2026

## Phạm vi và contract

Thêm helper score read-only và module stdlib kit_scoring.py; guideline, assessment template và routing qua hai workflow hiện có. Không thêm public skill/function/slash command, không đổi metadata schema hay cấu hình dự án, không sửa gate/approval/state. Assessment là JSON record riêng pin target và evidence, policy crm-definition-v1.

Score tính theo từng target/scope/item, hoặc toàn assessment inventory. Catalog obligations tách canonical requirements; không phải % requirement đúng hoặc % giao sản phẩm. Unknown applicability không được loại lặng lẽ; Unknown levels tạo khoảng điểm; N/A có kiểm soát; duplicate và stale pin bị từ chối. Mức 3 có declaration/evidence review/checks; helper không xác thực chuyên môn hay authority. Blocker không được bù bằng điểm; không blocker cũng không tự Ready.

## Kiểm chứng

Bộ 133 filesystem/CLI regression tests PASS (43,592 giây) trong repo tạm, gồm arithmetic, bounds, focused filters, Unknown/N/A, đủ catalog, level sai kiểu, stale target/evidence, path traversal, sai identity, level 3 thiếu review/self-check, content blocker, approval blocker, rollup canonical riêng, duplicate, scope/revision collisions, installed-package command và read-only preservation. Structural validator PASS (101 Markdown documents, 152 manifest entries, 13 functions), skill quick validation PASS và diff whitespace PASS trước rollout; kết quả execution được nêu trong phản hồi và logs.

Ví dụ tính và fixture reviewer trong tests là dữ liệu giả định, không phải review hay approval sản phẩm. Khi smoke trên p3 thật chỉ tạo skeleton Unknown tại stdout/temp; không tự gán điểm, sửa spec hoặc rewrite record cũ. Profile switching không là independent review. Chưa có hiệu chỉnh inter-rater với BA/Dev/QA thật; chưa có ngưỡng Ready, custom weights hoặc đánh giá NLP semantics tự động.
