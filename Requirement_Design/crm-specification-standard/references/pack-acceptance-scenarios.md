# Kịch bản nghiệm thu bộ tài liệu

Mã tài liệu: **CRM-PACK-ACCEPTANCE** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Kiểm tính nhất quán của các tuyến đọc và quyết định.

**Đọc khi:** Kiểm gói sau sửa hoặc pilot bằng hồ sơ thật.


<a id="spec-12"></a>

## Các điểm cần xác nhận khi pilot quy trình

1. Chấp thuận E01–E16 và S01–S12 như bộ kiểm nội dung của dự án, cùng applicability/N/A policy.
2. Chọn mẫu flow/state/decision/data/permission/AC phù hợp; không ép mọi trường hợp có mọi loại sơ đồ.
3. Chỉ định authority theo nội dung, người review và cách chốt expected result.
4. Thống nhất một nguồn chuẩn, pin/ref/ID và planned coverage trước baseline.
5. Thử review một Epic và một Story thực tế bằng bộ tiêu chí này; sửa những phần thiếu hoặc gây effort không có ích.
6. Gói hiện tại định nghĩa tuyến đọc, template và giới hạn kiểm máy. Pilot trên hồ sơ thật để điều chỉnh trước khi tích hợp thao tác Jira/Git/CI.

Thứ tự này giữ trách nhiệm quyết định ở người có thẩm quyền. Skill hỗ trợ đạt một chuẩn đã hiểu rõ; việc sinh đủ section không được dùng để tự xác nhận requirement đúng và đủ.


<a id="workflow-17"></a>

## Checklist trước khi áp dụng

- [ ] Thống nhất định nghĩa Feature/Epic/Story/Task và quyền của từng người.
- [ ] Xác nhận quan hệ Epic–Story–Task thực tế; chọn link nếu không có parent–child phù hợp.
- [ ] Kiểm transition/status category/Resolution field; bảo đảm `resolved` chưa bị tính thành Story Done theo quy ước dự án.
- [ ] Chọn repo/branch/path; có template Feature/Epic và baseline manifest.
- [ ] Phân công BA/Business/Dev/TL/QA/PM, reviewer và backup có ủy quyền.
- [ ] Chốt policy DoR/DoD, test/coverage/severity theo phạm vi; không coi ví dụ trong tài liệu là ngưỡng đã duyệt.
- [ ] Chốt nguồn evidence, quyền và retention; cấu hình required checks/validator/service và các đường bypass.
- [ ] Pilot một Epic nhỏ, có cả đường bình thường và trường hợp thiếu input/đổi rule/API retry.
- [ ] Kiểm người nhận tìm được đúng baseline, hiểu đúng AC, biết ai quyết và không bị kẹt ở vòng approval.


## Acceptance scenarios cho gói 1.2.0

Các scenario sau là walkthrough quy tắc, không là kết quả thử trên Jira thật hoặc forward-test một agent độc lập.

| ID | Input/tình huống | Kết quả bắt buộc | Tuyến kiểm |
|---|---|---|---|
| AT01 | Story nhỏ, mọi DoR evidence hợp lệ, không Task | Cho phép nhận triển khai với checklist | Story catalog → gate Story → decomposition |
| AT02 | Story chưa rõ chống trùng, đã có nhiều Task | Chặn phần liên quan; trả requirement về refinement | Q02/Q07 → baseline change |
| AT03 | Frontend/backend/test được đặt thành ba Story của cùng hành vi | Review lại outcome và chia thành Story hành vi; cân nhắc Task kỹ thuật | Decomposition/INVEST |
| AT04 | Epic chỉ rõ một scope độc lập; shared rules scope đó đã chốt | Có thể baseline scope đó; phần còn lại chưa Ready | Baseline selected scope → Epic gate |
| AT05 | Task cần đổi quyền hoặc contract | Change control và review lại; không tự quyết trong Task | Task T01/T03 → baseline change |
| AT06 | Tất cả Task Done, AC tích hợp fail | Story chưa Done | Task guide → Story DoD |
| AT07 | Story pin revision khác revision được duyệt | Không qua gate cho đến khi đánh giá/đối soát | Q05 → hard gate |
| AT08 | Chỉ review state transition | Verdict scoped; không cả Story PASS | Review process → D02 |
| AT09 | AI điền đủ template, thiếu business authority | Chưa qua gate; nguồn không tự thành quyết định | Q01 → review/gate |
| AT10 | Một migration phục vụ ba Story | Một Task với nhiều dependency links, effort tính một lần | Decomposition → progress reporting |
| AT11 | Copy folder sang môi trường khác | Links/templates/validator chạy trong folder; không cần path cá nhân | Manifest + validator |
| AT12 | 20/20 state-command cells đầy nhưng retention/key policy chưa quyết | Không tự Ready; Q02/Q01 vẫn chặn ví dụ | State finding example → ProjectCodeRequest |
| AT13 | Sửa nhãn UI thuần túy, không business lifecycle delta | Applicability có lý do; không ép mọi model/sơ đồ | Epic/Story catalog → Q02 |
| AT14 | Flow cho creator approve, permission cấm | Q03 finding; sửa và review lại mọi representation liên quan | Cross-model consistency |
| AT15 | Story kế thừa shared rule đúng pinned revision | Dẫn subset/ID; không copy tạo rule riêng | Story catalog → Q05 |
| AT16 | Test hoặc approval cũ của build/revision khác | Không dùng làm evidence Pass cho output mới | Handoff → change control |

**Cách chạy walkthrough:** đọc input và tuyến quy tắc; ghi observed decision, evidence là ref cụ thể, verdict và phần chưa kiểm. Structural validator chỉ kiểm refs/manifest/migration, không tự đánh giá 16 quyết định này. Pilot thực tế cần hồ sơ CRM đã xác định nguồn, đúng authority và cấu hình hệ thống thực tế; không dùng ví dụ thay thế.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
