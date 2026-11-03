# DoR, AC, DoD và thẩm quyền bàn giao

Mã tài liệu: **CRM-GATES** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Kiểm điều kiện bắt đầu/hoàn tất của Feature, Epic và Story.

**Đọc khi:** Review chuyển bước; đọc Task guide cho cổng Task.


<a id="workflow-7"></a>

## DoR, AC và DoD của Feature

Feature chỉ ở tài liệu nên các điều kiện dưới đây không tạo thêm status Jira.


<a id="workflow-7-1"></a>

### DoR để bắt đầu làm rõ/phân rã Feature

- [ ] Có Feature ID, nguồn nhu cầu và mục tiêu nghiệp vụ.
- [ ] Có ranh giới sơ bộ và ưu tiên.
- [ ] Có BA owner, Business authority và PM phụ trách.
- [ ] Có Epic/kế hoạch làm rõ dự kiến và nguồn lực tham gia.
- [ ] PM đã chốt phạm vi giao làm rõ; Business xác nhận hướng nghiệp vụ.

Không đòi toàn bộ rule và solution đã chi tiết ở thời điểm này.


<a id="workflow-7-2"></a>

### AC cấp Feature

AC mô tả kết quả nghiệp vụ tổng thể và các luồng liên Epic phải đáp ứng. Ví dụ: khách hàng tạo qua manual và import đều tuân thủ cùng quy tắc định danh/phân quyền đã chốt.


<a id="workflow-7-3"></a>

### Hoàn tất phân tích Feature và DoD bàn giao Feature là hai mốc

| Mốc | Điều kiện |
|---|---|
| Hoàn tất phân tích/phạm vi được khóa | Toàn bộ phạm vi hiện hành đã có yêu cầu, solution, AC và kế hoạch Epic/Story được duyệt tại các baseline tương ứng; không còn câu hỏi chặn |
| Feature Accepted — hoàn tất bàn giao nghiệp vụ | Đủ Epic/phạm vi hiện hành hoàn thành; AC tổng thể và luồng liên Epic đạt; Business nghiệm thu; tài liệu hiện hành cập nhật; vấn đề còn lại được xử lý đúng quyền |

Khóa một phần Feature để làm trước không được báo thành hoàn tất phân tích toàn Feature hoặc Feature Accepted.


<a id="workflow-8"></a>

## DoR, AC và DoD của Epic


<a id="workflow-8-1"></a>

### DoR để bắt đầu làm rõ Epic: `todo` → `inprogress`

- [ ] Có liên kết tới Feature và phạm vi Epic được PM chốt cho làm rõ.
- [ ] Có mục tiêu, actor và ranh giới sơ bộ.
- [ ] Có BA, Dev/solution owner, QA và Business authority được chỉ định.
- [ ] Có input/source và khả năng truy cập thông tin cần thiết.
- [ ] Có kế hoạch làm rõ từng hạng mục, owner, reviewer và thời gian thực hiện trên Epic.

**Epic được `inprogress` ngay khi bắt đầu phân tích, không phải đợi bắt đầu code.**


<a id="workflow-8-2"></a>

### Điều kiện Epic được phép sinh Story thực thi

Đây là cổng bàn giao requirement → development của phần scope được chọn:

- [ ] Bộ hồ sơ tại mục [Bộ hồ sơ phải review và merge trước khi tạo Story](baseline-and-change-control.md#workflow-5) đã đủ cho phần được chọn.
- [ ] Đã review các hạng mục E01–E16 của [chuẩn đặc tả](epic-specification-catalog.md); phần áp dụng có output/verdict, N/A có lý do và người xác nhận.
- [ ] Không còn câu hỏi chặn, bao gồm các rule dùng chung có tác động.
- [ ] Business/BA xác nhận nội dung; Dev/TL xác nhận solution; QA xác nhận testability theo applicability.
- [ ] Story candidates có outcome, BR/AC, scope, dependency và estimate; đã review cách chia.
- [ ] PM đã chốt manifest và bộ đầu ra trên đúng revision.
- [ ] **PR chứa bộ yêu cầu + solution + manifest của phần scope được chọn đã merge vào Git.**
- [ ] Có baseline ID, artifact refs, commit và approval refs để ghi vào Story.

Epic vẫn `inprogress` sau khi đạt cổng này. Đạt điều kiện tạo Story không có nghĩa Epic đã Done và không thay DoR Story.


<a id="workflow-8-3"></a>

### AC cấp Epic

AC mô tả kết quả tổng thể của phần phạm vi Epic. Ví dụ, luồng tạo manual phải bảo đảm kiểm quyền, validation, xử lý trùng và kết quả lưu/phản hồi nhất quán, kể cả khi được triển khai qua nhiều Story.

AC Epic không được chỉ viết “mọi Story đã Done”; cần chỉ ra kết quả nghiệp vụ phải quan sát được.


<a id="workflow-8-4"></a>

### DoD để đóng Epic: `inprogress` → `done`

- [ ] Toàn phạm vi Epic hiện hành đã được khóa; không còn phần chưa làm rõ bị bỏ sót.
- [ ] Tất cả Story cần thiết để đáp ứng phạm vi đã `done`.
- [ ] Các Task cần thiết đã hoàn thành; không chỉ đóng ticket để làm đẹp báo cáo.
- [ ] AC Epic và các luồng liên Story được kiểm chứng.
- [ ] Không còn lỗi chặn; vấn đề được hoãn có owner, quyết định và thời hạn hợp lệ.
- [ ] Business có thẩm quyền xác nhận nghiệm thu Epic trên scope/build được định danh.
- [ ] Tài liệu nghiệp vụ/kỹ thuật hiện hành đã cập nhật theo phần mềm thực tế.
- [ ] Có acceptance/evidence links; PM chốt kết quả và báo cáo.

Nếu Feature chỉ có một Epic và đủ cùng phạm vi, có thể dùng một phiên/bản ghi nghiệm thu cho cả hai, ghi rõ các đối tượng được nghiệm thu. Không cần hai nghi lễ trùng nội dung.


<a id="workflow-9"></a>

## DoR, AC và DoD của Story


<a id="workflow-9-1"></a>

### DoR để bắt đầu triển khai: `todo` → `inprogress`

- [ ] Story liên kết đúng Epic, Feature và baseline ID/commit.
- [ ] Các hạng mục S01–S12 của [Catalog Story](story-specification-catalog.md) có nội dung cụ thể hoặc ref hợp lệ; không sao chép làm lệch baseline Epic.
- [ ] Outcome, trong/ngoài scope rõ; BR/AC và ví dụ có expected result.
- [ ] Solution/contract/UI/data refs phù hợp phạm vi, còn hiệu lực.
- [ ] Dev và QA đã đọc, hiểu khớp; không còn câu hỏi chặn.
- [ ] Dependency phải có trước khi bắt đầu đã sẵn sàng; dependency cho bước sau có cam kết/kế hoạch rõ và không chặn công việc đang nhận.
- [ ] Có dữ liệu/môi trường/quyền cần cho bước thực hiện; điều kiện kiểm thử phía sau có owner và lịch sẵn sàng.
- [ ] Có Dev owner, QA owner, estimate và capacity được xác nhận.
- [ ] Có test approach, policy chất lượng và reviewer cần thiết.
- [ ] PM chốt kế hoạch triển khai, không có blocker còn hiệu lực.

Story có thể đã được tạo nhưng chưa đạt DoR: giữ `todo`, ghi missing items/owner/due. Chưa có `Ready` status thì dùng checklist hoặc nhãn để hiển thị; quyết định gate phải dựa vào evidence, không chỉ nhãn.


<a id="workflow-9-2"></a>

### AC của Story

AC phải mô tả điều kiện và kết quả có thể quan sát/kiểm chứng. Ví dụ giả định:

| AC | Điều kiện / thao tác | Kết quả mong đợi |
|---|---|---|
| AC-CRM-001 | AM có quyền, gửi dữ liệu hợp lệ không trùng | Tạo đúng một hồ sơ và trả kết quả xác định |
| AC-CRM-002 | Request không có quyền tạo | Bị từ chối; không phát sinh hồ sơ |
| AC-CRM-003 | MST trùng theo rule/phạm vi trạng thái được duyệt | Không tạo hồ sơ trùng; phản hồi theo contract |

Nếu cần ngưỡng hiệu năng hoặc định nghĩa cụ thể về chuẩn hóa/trùng, chúng phải được chốt trong rule/NFR; không để AI tự chọn.


<a id="workflow-9-3"></a>

### Điều kiện Dev bàn giao QA: `inprogress` → `resolved`

- [ ] Code phù hợp baseline và AC của Story.
- [ ] Peer/TL review cần thiết đã đạt trên đúng revision.
- [ ] Unit/API/permission tests và required CI checks đạt theo [POL-CHECKS — Required checks](project-policy-register.md#pol-checks) và [POL-QUALITY](project-policy-register.md#pol-quality), có ref/version được dự án phê duyệt và evidence đúng revision/build; skipped/not-run không tính Pass.
- [ ] Build đã được deploy vào môi trường nhận QA; smoke đạt.
- [ ] Có baseline, code SHA, build/config/environment và hướng dẫn kiểm tra liên quan.
- [ ] QA nhận được bộ bàn giao và dữ liệu/slot kiểm thử cần thiết.

Đây là mốc Dev hoàn tất để QA kiểm chứng, **chưa phải DoD của toàn Story**.


<a id="workflow-9-4"></a>

### DoD đóng Story: `resolved` → `done`

- [ ] Tất cả AC trong phạm vi Story đã được kiểm chứng.
- [ ] Test matrix được duyệt đã thực hiện, kết quả đạt trên build xác định.
- [ ] Không còn Critical/Major mở, phân loại theo [POL-SEVERITY — Phân loại ảnh hưởng lỗi](project-policy-register.md#pol-severity) và điều kiện đóng theo [POL-QUALITY — Chất lượng và completion](project-policy-register.md#pol-quality); cả hai phải có ref/version và phê duyệt có hiệu lực trong register dự án. Không hạ severity để qua gate.
- [ ] Minor/known issue còn lại được phân loại theo [POL-SEVERITY](project-policy-register.md#pol-severity), có đánh giá tác động và quyết định xử lý đúng thẩm quyền theo [POL-QUALITY](project-policy-register.md#pol-quality), cùng ref/version/decision evidence của dự án.
- [ ] Code, migration/config và tài liệu liên quan hoàn tất trong phạm vi Story.
- [ ] Evidence truy được baseline → code/review/CI → build → test/defect/verdict.
- [ ] QA xác nhận Pass đúng baseline/build còn hiệu lực.
- [ ] PM hoặc người được ủy quyền chốt bộ đầu ra đủ điều kiện đóng Story.

Các link POL ở checklist dẫn tới định nghĩa nhóm policy trong bộ chuẩn. Hồ sơ Story phải bổ sung ref/version của policy **thực tế đã được dự án phê duyệt**; link tới hướng dẫn này không tự thay approval. Thiếu policy bắt buộc thì chưa đủ điều kiện đóng.

Không bắt Business nghiệm thu từng Story; Business nghiệm thu Epic/Feature. Nếu QA Pass nhưng chưa có PM closure, Story vẫn `resolved`, ghi rõ đang chờ PM và thời điểm chờ.


<a id="workflow-12"></a>

## Ai review và ai có quyền chốt?

| Đối tượng / quyết định | Người chuẩn bị | Người xác nhận nội dung | Người chốt chuyển bước |
|---|---|---|---|
| Khung Feature, Epic và kế hoạch phân tích | BA + PM | Business và leads theo phạm vi | PM trong thẩm quyền; vượt quyền trình Sponsor |
| Rule/AC nghiệp vụ | BA | Business có thẩm quyền; Dev/QA phản biện | Business quyết nội dung; PM kiểm đủ điều kiện bàn giao |
| Solution/contract | Dev | Peer/TL theo rủi ro; QA review testability | Technical authority xác nhận; PM không ký thay kết luận kỹ thuật |
| Baseline trước tạo Story | BA điều phối, Dev/QA bổ sung | Các reviewer theo scope/delta | PM chốt manifest và output; merge theo quyền Git |
| DoR Story và kế hoạch triển khai | Dev + QA | Leads xác nhận dependency/capacity khi cần | PM chốt planning |
| DoD Task | Task owner | Reviewer/người nhận được giao | Người được phân công; không mặc định PM cho mọi Task |
| Story `done` | Dev + QA cung cấp evidence | QA xác nhận AC/test; Dev hoàn tất nghĩa vụ kỹ thuật | PM hoặc backup được ủy quyền chốt output |
| Epic/Feature nghiệm thu | BA + QA tổng hợp | Business xác nhận kết quả | PM chốt hồ sơ/roll-up; Business giữ quyền nghiệm thu |

Reviewer được chọn theo loại thay đổi và rủi ro. Nội dung không đổi có thể dùng xác nhận còn hiệu lực, với scope/version rõ; N/A phải có lý do và người chịu trách nhiệm. Không tự bỏ review bắt buộc để tăng tốc.

PM có queue review, thời hạn và backup được ủy quyền. Có thể review theo batch, nhưng quyết định phải riêng cho từng target/revision. Quá hạn không tự trở thành phê duyệt.


## Phân biệt nghĩa DoR/DoD và cách dùng gate

DoR bắt đầu phân tích Epic khác DoR bắt đầu triển khai Story. AC mô tả kết quả cụ thể; DoR xác định điều kiện vào bước; DoD xác định chất lượng/evidence khi hoàn tất. DoD trong [Scrum Guide](https://scrumguides.org/scrum-guide.html) gắn với Increment; checklist hoàn tất Epic/Task ở CRM là điều chỉnh quản trị, không là ba DoD bắt buộc do Scrum quy định.

**Input kiểm gate:** target/scope/revision, các review records, blocker/dependency, authority/ủy quyền và evidence của bước đó. **Output:** gate decision với bước được phép, revision, reviewer/approver, evidence và reason. Đủ dữ liệu mới xét nội dung; thiếu input hoặc authority không được đi tiếp. Không lấy điểm trung bình bù cho một phép kiểm ngữ nghĩa không đạt.

PM chốt scope/manifest Story; cho phép phân rã Task trong phạm vi đã ủy quyền. Task thường do reviewer/receiver đóng; đổi scope/cam kết/dependency đáng kể phải trình lại PM. Xem [Task DoR/DoD](task-planning-and-completion.md#workflow-10), [status](jira-status-and-progress-reporting.md) và [hard gates](ai-handoff-and-hard-gates.md).


## Đầu vào policy và nội dung Feature

Feature dùng [catalog F01–F08](feature-specification-catalog.md) và [template](../assets/templates/feature-specification-template.md) theo bước đang xét. Hoàn tất bàn giao sản phẩm khác đánh giá lợi ích sau sử dụng; điều kiện nghiệm thu có hiệu lực phải được Business xác nhận.

Mọi gate đọc [policy register](project-policy-register.md) được dự án duyệt, đúng ID/version/scope. Severity Critical/Major/Minor, required checks, risk-based coverage và thời hạn review phải có định nghĩa tương ứng trước khi dùng làm căn cứ. Thiếu policy bắt buộc = chưa đủ điều kiện đánh giá gate, không tự đặt ngưỡng. SLA quá hạn không tự Approved; priority không thay severity. Quy tắc không còn Critical/Major mở ở DoD Story vẫn giữ; không dùng policy chưa duyệt hoặc waiver ngầm để bỏ tiêu chí này.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
