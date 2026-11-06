# Kịch bản nghiệm thu bộ tài liệu

Mã tài liệu: **CRM-PACK-ACCEPTANCE** · Gói CRM 1.3.1 · 03/11/2026

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


## Kịch bản bổ sung cho gói 1.3

| ID | Tình huống | Kết quả bắt buộc | Tuyến đọc |
|---|---|---|---|
| AT17 | Critical/Major hoặc required checks chưa có policy được duyệt | Gate phụ thuộc chưa thể đạt; giữ missing authority/decision | Policy → gate |
| AT18 | Business requirement bị gán BR; NFR bị ép chỉ ở Epic | BR giữ nghĩa Business Rule; dùng REQ/type và applies_to theo scope | ID/type guide |
| AT19 | Outcome muốn giảm thời gian xử lý nhưng chưa có dữ liệu sau go-live | Tách product acceptance/benefit observation theo authority; không tự ghi benefits đạt | Feature catalog |
| AT20 | E07 quyền phụ thuộc state và có API | Đọc D05 + D02 + D07 và xét Q01–Q07; không miễn Q01/Q05 | Mapping |
| AT21 | 12/14 review đạt, 2 gap chặn | Báo review coverage và blocker; không báo sản phẩm 86% hoàn thành | Measurement |
| AT22 | Không có item áp dụng, còn applicability Unknown, hoặc scope tăng trong kỳ | Zero denominator=N/A; Unknown hiện riêng; scope delta và mẫu số phải giải thích | Measurement |
| AT23 | Task dùng chung, Story cancel nhưng requirement chưa loại khỏi scope | Không đếm effort lặp; giữ scope gap và cancel riêng; không tăng completion giả | Roll-up |
| AT24 | SLA chưa duyệt hoặc review quá hạn | Báo elapsed age/clock; không tự gán SLA, không tự Approved | Policy → report |
| AT25 | Gói có hướng dẫn pilot nhưng chưa có hồ sơ/người tham gia thật | Kết luận chưa pilot; không đánh dấu requirement handoff hoặc hook đã đạt | Pilot procedure |

Dùng [pilot procedure](pilot-and-operational-validation.md) và [record](../assets/templates/pilot-review-record-template.md) khi có input thật. Structural checks không tự đánh giá các quyết định ngữ nghĩa này.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).

## Workflow Kit Acceptance — 1.4.0

Các case WK01–WK15, input fixtures, quyết định và giới hạn walkthrough nằm ở [Workflow Routing and Handoff Walkthrough](examples/workflow-routing-and-handoff-walkthrough.md). Chúng bao phủ routing, scope, rework, quyền của check workflows, handoff/resume và tính portable; không tự thay pilot thật.

Để review bản phát hành: đọc [Start Here](../START-HERE.md), dùng registry để mở từng function, đối chiếu workflow với case tương ứng; kiểm mỗi function có input/steps/output/receiver/next action, và correction được route về tác giả thay vì check tự sửa target.

## Installation Tooling Acceptance — 1.5

Dùng [INSTALL](../INSTALL.md) để chạy install dry-run/apply trên repo tạm, doctor và fresh-session smoke test theo nền tảng. Các automated tests tại [test_installation_tooling.py](../scripts/tests/test_installation_tooling.py) kiểm filesystem/config/context/lint/ID/update, bao gồm clone sạch và rollback. [Report 1.5](../provenance/pack-validation-report-v1.5.md) ghi kết quả và phần chưa kiểm.

Không suy runtime discovery từ SKILL file tồn tại, không suy semantic approval từ lint, không coi reservation local là global allocation qua nhiều clone. Bản cài cũ chỉ được migration theo ownership/diff được review, không undo toàn file.

## Tình huống checkpoint scope — 1.11

Các tình huống này cần agent/reviewer thực hiện khi đánh giá hành vi; unit tests context không tự chứng minh kết quả semantic. Áp dụng [checkpoint](source-scope-and-decomposition-checkpoint.md).

| Tình huống | Kết quả quan sát cần có |
|---|---|
| Nguồn công bố 12 dòng estimation; có preview, quyền, approval + downstream và hai dòng cùng nhắc một create form. User yêu cầu chia Feature/Epic/Story. | Kiểm số công bố/đối soát riêng, nhận ra đơn vị không đồng đều và overlap; không tạo 12 Story mặc định; có rationale nhóm và mapping fragment/shared contract, gaps giữ nguyên. Không đòi luôn phải có ít hơn 12 nhóm. |
| User đề nghị gom import/export vì đều dùng file; actor/quyền, error semantics và acceptance còn khác hoặc chưa biết. | Không coi tên kênh là đủ căn cứ. Giữ phương án có điều kiện hoặc hỏi quyết định ảnh hưởng; lý do chọn/tách truy được. Không tự cấp Approved/Ready. |
| User chỉ hỏi tiến độ; có số dòng nguồn và allocation draft nhưng chưa có evidence review. | Trả status có nguồn/revision và giới hạn; phân biệt số dòng với scope đã baseline/Ready. Không tự tạo file, rewrite allocation hoặc chạy lại full decomposition. |
| Có review allocation đúng revision; chỉ một rule thay đổi trong Epic. | Xét delta/impact, tái dùng evidence còn hiệu lực và chỉ kiểm phần liên quan; không bắt làm lại toàn inventory. |
| Một ví dụ dùng ID đã cấp cho Customer–Contact nhưng gán nghĩa “Tiếp nhận khách hàng mới”. | Phân biệt ví dụ và hồ sơ dự án. Đối chiếu cùng case qua cây phân rã, walkthrough và manifest. Giữ ID nguồn. |
| Bảng ProjectCodeRequest ghi Denied cho cancel khi PendingApproval, nhưng finding báo thiếu kết quả. | Đối chiếu guard, disposition, contract, AC và finding. Ghi gap contract nếu có, giữ hành vi từ chối đã được mô tả. |

## Chọn cấp và quan hệ cha–con — 1.12.3

Dùng input dưới cho phiên mới với kit và context workstream tối thiểu. Khi forward-test, chỉ đưa cột input cho agent; reviewer giữ cột kết quả để đánh giá. Lưu output, revision kit, context thực nạp và kết luận theo từng case. Không so khớp nguyên văn tên; đánh giá quyết định và rationale. Các test helper chỉ chứng minh phân phối checkpoint, chưa chạy agent.

| ID | Input | Kết quả quan sát cần có |
|---|---|---|
| LV01 | Dự án có Feature Quản lý Customer, Epic Hồ sơ Customer. Đề xuất thêm Feature Tra cứu Customer → Epic Tra cứu hồ sơ từ Customer List → Story Tìm Customer theo quyền. Cả ba scope/AC cùng một lookup theo tên và quyền xem hiện có. Review phương án. | Nhận ra outcome trùng và entry point/guard chưa đủ tạo hai cha mới. Đề xuất đặt Story vào cây hiện có; giữ kiểm quyền trong AC. Chỉ ghi findings, không sửa allocation trong review. |
| LV02 | Sản phẩm cần tìm kiếm Customer trên nhiều nguồn, tìm cơ bản/nâng cao, lưu truy vấn và quản trị nguồn tìm kiếm; có consumer, contract, phạm vi nghiệm thu riêng. Đề xuất phân cấp. | Cho phép Feature tìm kiếm khi có rationale tương quan năng lực khác, Epic theo phạm vi chung và Story theo delta có ích. Không áp lệnh cấm từ khóa Tra cứu hoặc ép vào Customer–Contact. |
| LV03 | Epic có model/contract và hồ sơ baseline riêng; release này chỉ chọn một Story. Chưa có nhu cầu đã xác nhận cho Story khác. | Không bịa con hoặc reject chỉ vì một–một; giải thích vai trò hồ sơ cha, selected scope và refs kế thừa. |
| LV04 | Yêu cầu bổ sung filter trạng thái cho danh sách Customer đã có Epic tra cứu. Chỉ author phần thay đổi. | Tìm parent, đề xuất delta trong Epic hiện có và xét sizing có cần Story riêng không; không dựng Feature mới hoặc phân rã lại cả CRM. Giữ policy quyền hiện có. |
| LV05 | Nguồn có hai màn hình preview/detail nhưng người dùng chỉ đạt mục tiêu xác định đúng hồ sơ khi dùng cả hai; chưa có lợi ích độc lập hay sizing. | Không mặc định hai Story theo screen; giữ lát tích hợp hoặc candidate có điều kiện, nêu gap thực. Không invent value/sizing để tách. |
| LV06 | Có Epic hồ sơ và Epic quan hệ Customer–Contact. Hành trình tạo Contact rồi gắn vào Customer; thao tác gắn phải tự Active theo rule đã xác nhận. Chọn Use Case và Story. | Phân biệt hành trình xuyên Epic với Use Case/Story; giữ owner/model và dependency tạo Contact. Gắn + auto Active cùng outcome, đọc lại thuộc verification. Không tách kiểm quyền/activation thành Story rời để bỏ control. |
| LV07 | Chỉ có ba tên Feature Tra cứu, Epic Tra cứu từ List, Story Tìm theo quyền; chưa có nội dung hoặc cây hiện hành. Hỏi cách chia có sai không. | Nêu dấu hiệu lặp nghĩa và cần scope/AC/parent để kết luận; không tuyên bố chắc chắn sai từ tên, không tự phê duyệt allocation. |
