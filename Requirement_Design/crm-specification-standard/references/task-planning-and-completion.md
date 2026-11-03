# Lập kế hoạch, giao và hoàn tất Task

Mã tài liệu: **CRM-TASK** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Chọn Task có điều kiện và kiểm đầu ra thực thi.

**Đọc khi:** Cần phân công/theo dõi riêng hoặc đầu ra kỹ thuật dùng chung.


## Task là tùy chọn, kế hoạch thực hiện vẫn cần

Đọc [bảng quyết định checklist/Task](backlog-hierarchy-and-decomposition.md) trước khi tạo ticket. Task thường thuộc Epic và liên kết Story; không giả định Jira standard Task nằm dưới Story. Không tạo bộ Task cố định REQ/DESIGN/DEV/TEST cho mọi Story.

**Đầu vào:** phạm vi được giao, baseline/contract liên quan, output dự kiến, dependency và ủy quyền phân rã. **Đầu ra:** brief và evidence của Task; với công việc nhỏ chỉ cần checklist trong Story. **Người kiểm:** reviewer/người nhận theo loại output; PM chỉ cần chốt từng Task khi chưa ủy quyền hoặc có thay đổi scope/cam kết đáng kể.

## Nội dung Task và cách kiểm — T01–T08

| ID/tên | Nội dung | Reviewer kiểm đến đâu là đủ |
|---|---|---|
| <a id="t01"></a>T01 — Liên kết và mục đích | Story/Epic, requirement/AC liên quan | Đi ngược được tới nhu cầu/đầu ra được giao; giải thích việc bỏ Task ảnh hưởng gì |
| <a id="t02"></a>T02 — Đầu ra và ranh giới | Artifact/kết quả, phần không làm | Nhận diện được output và phạm vi; so với các Task khác để loại chồng/gap |
| <a id="t03"></a>T03 — Đầu vào và phiên bản | Baseline, contract, repo/module, environment | Mở được đúng revision, đủ quyền; không dùng “latest” chưa xác định |
| <a id="t04"></a>T04 — Kế hoạch và constraint | Các bước chính, constraint kỹ thuật/quyền | Đủ bắt đầu mà không tự quyết requirement; không ép giả mã chi tiết |
| <a id="t05"></a>T05 — Dependency và bàn giao | Điều kiện bắt đầu, người nhận output | Xác nhận input sẵn; người nhận biết contract và tiêu chí nhận |
| <a id="t06"></a>T06 — Owner, reviewer và timebox | Người thực hiện/kiểm, estimate/timebox/capacity | Có khả năng thực hiện; biết mốc báo vượt dự kiến và hành động xem lại |
| <a id="t07"></a>T07 — Tiêu chí hoàn tất | Phép kiểm + expected result cho output | Có cách phát hiện output sai; loại “đã implement” không có phép kiểm |
| <a id="t08"></a>T08 — Evidence và closure | PR/commit/build/test/log áp dụng, reviewer/receiver verdict | Evidence đúng artifact/revision; người nhận xác nhận, không có blocker bị che |

Đây là catalog CRM cụ thể hóa **SMART Tasks** của [Bill Wake](https://xp123.com/invest-in-good-stories-and-smart-tasks/): Specific→T02/T04; Measurable→T07/T08; Achievable→T03/T05/T06; Relevant→T01; Time-boxed→T06. SMART là checklist chất lượng, không phải framework SDLC riêng.

## Các bước review Task

1. Áp dụng bảng quyết định để chứng minh cần ticket riêng. Nếu không, giữ các bước trong checklist Story.
2. Đọc brief T01–T08; thử xác định input và output mà không hỏi người viết. Nêu counterexample nếu phạm vi hoặc expected result còn nhiều nghĩa.
3. So Task với Story/baseline: không tự thêm quyền/rule/contract. Delta hành vi quay về change control; gap requirement chặn phần liên quan.
4. Kiểm SMART, dependency, khả năng thực hiện và ai nhận. Ghi missing items, owner, due; không dùng một approval để thay input đang thiếu.
5. Khi đóng, thực hiện phép kiểm đầu ra dưới đây, review đúng revision, ghi receiver acceptance. Timebox hết chỉ kích hoạt xem lại kế hoạch, không là bằng chứng Done.

**Verdict:** Đạt khi đủ tiêu chí của bước đang xét và evidence; Không đạt khi có counterexample/gap; Chưa kiểm khi thiếu input hoặc reviewer; N/A chỉ cho tiêu chí điều kiện không áp dụng với lý do/reviewer. Gap chặn output ngăn bắt đầu hoặc đóng Task tương ứng.

**Task Done không làm Story Done.** Story phải kiểm chứng AC tích hợp trên build xác định. Task test execution chỉ chứng minh phần test được giao; Task automation phải có assertion có ý nghĩa và expected result xác nhận độc lập với code do AI tạo.

PoC có thể kết luận phương án không khả thi mà vẫn hoàn tất Task nếu thí nghiệm và báo cáo đáp ứng brief. Chỉ hết timebox mà chưa có evidence/giải thích thì chưa đạt completion. Nghiên cứu nhỏ vẫn nằm trên Epic; không tạo Spike mặc định.


<a id="workflow-10"></a>

## DoR và DoD của Task theo loại đầu ra

Task thuộc backlog triển khai: tạo phần mềm, test, script, cấu hình hoặc bằng chứng kiểm chứng cần thiết. Không mặc định tạo Task `[REQ]`, `[DESIGN]`, `[TEST-DESIGN]` để theo dõi hoạt động làm rõ Epic.

Chỉ tạo Task khi có output cụ thể, owner và nhu cầu giao/theo dõi riêng. Story nhỏ có thể được triển khai trực tiếp, không cần sinh Task cho đủ hình thức. Viết unit test, review code hay cập nhật tài liệu thuộc nghĩa vụ của công việc khi phù hợp; không tự động tạo ticket cho từng thao tác.


<a id="workflow-10-1"></a>

### DoR dùng chung: `todo` → `inprogress`

- [ ] Có mục tiêu và một đầu ra cụ thể.
- [ ] Có Epic/Story hoặc phạm vi được giao để tham chiếu.
- [ ] Có input/phiên bản cần dùng và quyền truy cập.
- [ ] Có owner, reviewer/người nhận đầu ra, estimate/thời hạn và capacity.
- [ ] Có tiêu chí hoàn tất và phương pháp kiểm tra.
- [ ] Dependency cho bước bắt đầu đã sẵn sàng.
- [ ] Công việc nằm trong kế hoạch được PM xác nhận hoặc trong phạm vi phân rã đã được ủy quyền.


<a id="workflow-10-2"></a>

### DoD dùng chung

- [ ] Đã tạo đúng đầu ra được giao và đáp ứng tiêu chí hoàn tất.
- [ ] Reviewer phù hợp đã kiểm tra; các finding chặn đã được xử lý.
- [ ] Đầu ra có version/source/evidence và liên kết đúng Epic/Story.
- [ ] Người nhận xác nhận đủ để sử dụng; actual/remaining work được cập nhật.

Không yêu cầu PM đóng từng Task thông thường nếu quyền xác nhận Task đã được phân công. PM vẫn chốt bộ đầu ra tổng hợp ở cổng tạo Story và đóng Story/Epic.


<a id="workflow-10-3"></a>

### DoD bổ sung theo đầu ra triển khai

| Đầu ra của Task | Đầu ra bắt buộc để Done | Reviewer / người nhận |
|---|---|---|
| Code/API/UI | Code được review/merge theo policy, các kiểm tra liên quan đạt, tích hợp đúng contract, output liên kết Story và code version | Peer/TL; Story owner/QA |
| Automated tests | Expected result được xác nhận, assertion có ý nghĩa, trace BR/AC, script chạy đạt trong môi trường/CI quy định | QA/technical reviewer phù hợp |
| Kiểm thử Story | Các case được giao đã chạy; kết quả, build/data/config refs, Bug/retest và verdict được ghi | QA reviewer/Test Owner; PM nhận verdict tổng hợp |
| Migration/config/CI hoặc hạ tầng hỗ trợ | Artifact/script/config đúng phạm vi; kiểm chứng trên môi trường quy định; có log/đối soát/khôi phục theo rủi ro | Technical reviewer, QA, IT/Data Steward theo nội dung |

Các dòng trên là nhóm đầu ra để chọn tiêu chí, không phải các issue type mới hay bộ Task bắt buộc cho mọi Story. Task Done không tự làm Story Done: Story còn phải được tích hợp và kiểm chứng theo toàn bộ AC/DoD.


<a id="workflow-10-4"></a>

### Hoạt động refinement và trường hợp nghiên cứu độc lập

Làm rõ requirement, phân tích solution và testability được quản lý bằng readiness/output/review trên Epic. Effort vẫn ghi trên Epic hoặc work package tương ứng; PM cấp capacity và theo dõi thời hạn, không để effort biến mất vì không có Task.

Nghiên cứu nhỏ xử lý trong hoạt động phân tích Epic. Chỉ tạo Task kỹ thuật/spike độc lập khi thật sự cần timebox và đầu ra riêng như PoC, benchmark hoặc script thử nghiệm để ra quyết định. Khi đó PM chốt kế hoạch, TL xác nhận brief/tiêu chí và quyền/dữ liệu; không bắt biết trước solution. Kết quả là evidence/khuyến nghị, không tự được tính là Story hay Feature hoàn thành.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
