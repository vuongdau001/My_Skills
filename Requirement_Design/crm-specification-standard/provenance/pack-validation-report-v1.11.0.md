# Kiểm chứng CRM Workflow Kit 1.11.0

ID: CRM-VALIDATION-V111 · 05/11/2026

## Thay đổi

Thêm checkpoint nguồn scope và cách phân rã cho function list/WBS/estimation/screen list. Sáu function setup/define-feature/specify-epic/prepare-stories/review-specification/report-status nạp cùng reference mặc định qua context. Routing, BA guide, Feature catalog và decomposition cùng dẫn một nguồn; không thêm public skill/function, schema hoặc approval gate.

Checkpoint yêu cầu phân biệt đơn vị nguồn với đơn vị bàn giao, rationale theo outcome/model/control/acceptance, mapping nhiều–nhiều và phần dùng chung. Status ngắn giữ write boundary và không tự mở full decomposition. Số nhóm ít hơn, mapping đủ dòng hoặc lint PASS chưa là evidence phân rã hợp lý.

## Kiểm chứng

- Structural validator PASS: 107 Markdown documents, 158 manifest entries, 105 historical source sections, 5 agent profiles và 13 workflow functions.
- Skill validator PASS; git diff --check không có lỗi whitespace.
- Full regression suite: 149 tests PASS trong 50,436 giây trên disposable projects.
- Hai tests mới kiểm sáu context nhận đúng content/hash checkpoint mặc định mà không ghi nguồn/project; bản cài tự chứa nạp cùng resource đúng một lần khi dùng --full và --reference.
- Kiểm context thực tế từ source với workstream p3: crm-define-feature nạp checkpoint mặc định; chưa chạy semantic review dự án bằng kết quả này.

Các acceptance scenarios được bổ sung cho inventory trộn độ lớn/giao thoa, gộp import/export thiếu căn cứ, status ngắn và delta review. Chưa có lượt agent độc lập thực thi các scenario này; không ghi chúng là behavioral acceptance PASS.

## Giới hạn

Unit tests kiểm context delivery, deduplication và read-only behavior, không chứng nhận agent luôn chọn đúng Feature/Epic. Các acceptance scenarios mới cần đánh giá semantic riêng. Chưa có independent review, fresh-session runtime discovery, Windows native smoke test hoặc authority approval mới. Update package không tự rewrite project artifacts, source, DDD/backlog/state hoặc tracker.
