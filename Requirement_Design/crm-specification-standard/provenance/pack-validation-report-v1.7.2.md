# Kiểm chứng CRM Workflow Kit 1.7.2

ID: CRM-VALIDATION-V172 · 04/11/2026

## Thay đổi và tác động

Patch sau rà tổng thể kit: bảo vệ source/read_only xuyên workstream, so snapshot nội dung khi install lại, backup update ngoài skills discovery, và chẩn đoán metadata controlled value sai kiểu theo từng file. Giữ dependency closure hiện hành; bổ sung hướng dẫn allocation cho partial scope. Measurement/report dùng nguồn trạng thái canonical do project chỉ định.

Config schema 1, layout cũ và hồ sơ nghiệp vụ giữ nguyên khi update package; không migrate hồ sơ sang schema 2. Update bảo toàn receipt và backup; từ chối local drift. Không tạo Business/PM approval từ kết quả tooling.

## Kiểm chứng

- 116 filesystem/CLI regression tests trên repo tạm: kiểm cross-workstream source/read_only cho spec/input roots, content khác dù manifest giống, backup ngoài cả hai adapter skills, update liên tiếp, rollback và symlink backup bị từ chối, lỗi controlled metadata ở nhiều file vẫn tổng hợp.
- Partial-scope scenario: Decision riêng import không chặn Story manual; Decision chung trên Epic vẫn chặn cả các nhánh phụ thuộc. Đây là structural record-obligation check, không phải DoR/authority approval.
- Structural reference validation và skill quick validation chạy riêng trước rollout. Các kết quả cụ thể được ghi trong phản hồi execution và local logs của lượt triển khai.

## BA walkthrough và giới hạn

Tác giả tự đi qua ví dụ Customer–Contact của BA Getting Started: intake nhu cầu; chọn Feature/Epic; guard khác invariant; flow và AC; Story theo outcome; solution/review/baseline; xử lý gap và thay đổi sau baseline. Ví dụ EX-* giữ tính minh họa, không đưa vào source registry hay tạo baseline/approval thật. Phân bổ Decision theo từng nhánh được kiểm bằng regression ở trên.

Đây là author self-check và tooling regression. Chưa có thử nghiệm người dùng BA độc lập, fresh-session runtime discovery, sản phẩm chạy thật hoặc acceptance. Pilot p3 chỉ được lint ở draft gate; không nâng trạng thái Ready. Các report 1.7/1.7.1 mô tả evidence lịch sử của lượt tương ứng, không thay verdict của bản này.
