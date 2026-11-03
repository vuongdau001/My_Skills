# Quy trình review, evidence và điều kiện kết luận

Mã tài liệu: **CRM-REVIEW** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định ai kiểm, kiểm phạm vi nào và được kết luận đến đâu.

**Đọc khi:** Review toàn bộ hoặc một phần Epic/Story.


## Chọn phạm vi review

**Đầu vào:** target/revision/selected scope, baseline/source, catalog applicability và models. **Đầu ra:** [review record](../assets/templates/requirements-review-record-template.md), findings, evidence và verdict có phạm vi; PM dùng để xét gate.

Full review: đánh giá toàn bộ catalog của target, bảy nhóm kiểm dưới đây và các model áp dụng. Targeted review: ghi rõ phép kiểm/model được giao; không nâng kết quả thành PASS cả Epic/Story. Không có source/revision/reviewer thì ghi Chưa kiểm. Đạt một phần không là approval cho phần còn lại.

| Nhóm kiểm | Đọc để thực hiện |
|---|---|
| Q01 — Đúng nhu cầu và sự cần thiết | [Thủ tục kiểm đúng nhu cầu và sự cần thiết](checks/adequacy-and-necessity.md) |
| Q02 — Đầy đủ ở mức yêu cầu và tập yêu cầu | [Thủ tục kiểm đầy đủ ở mức yêu cầu và tập yêu cầu](checks/requirements-completeness.md) |
| Q03 — Nhất quán giữa các mô hình | [Thủ tục kiểm nhất quán giữa các mô hình](checks/cross-model-consistency.md) |
| Q04 — Khả năng kiểm chứng yêu cầu | [Thủ tục kiểm khả năng kiểm chứng yêu cầu](checks/requirements-verifiability.md) |
| Q05 — Truy vết và quản lý phiên bản | [Thủ tục kiểm truy vết và quản lý phiên bản](checks/traceability-and-versioning.md) |
| Q06 — Rõ nghĩa và không mơ hồ | [Thủ tục kiểm rõ nghĩa và không mơ hồ](checks/clarity-and-unambiguity.md) |
| Q07 — Khả thi và sẵn sàng bàn giao | [Thủ tục kiểm khả thi và sẵn sàng bàn giao](checks/feasibility-and-handoff-readiness.md) |

Dùng [inventory/coverage](coverage-inventories-and-traceability.md) để chọn model và mẫu số. Dùng [gate/authority](readiness-completion-and-approval-gates.md) để quyết định bước tiếp theo. Hướng dẫn review xác nhận chất lượng hồ sơ; code/test runtime cần evidence khác.


<a id="spec-3"></a>

## Cách kết luận một hạng mục đã đạt


<a id="spec-3-1"></a>

### Cấu trúc review dùng chung

Mỗi hạng mục E/S trong catalog có bản ghi:

| Trường | Nội dung |
|---|---|
| Applicability | Áp dụng / N/A có lý do và người xác nhận |
| Phạm vi và phiên bản | Epic/Story, phần scope, section/model ID, revision hoặc baseline ref |
| Output | Đường dẫn, section, bảng hoặc mô hình cụ thể |
| Owner / reviewer | Người viết và người có năng lực/quyền xác nhận |
| Review result | Chưa kiểm / Không đạt / Đạt / N/A có lý do; ghi finding và reason |
| Open question | Câu hỏi, tác động, owner, hạn và có chặn scope này không |
| Decision/evidence | Nguồn nghiệp vụ, approval, review comments hoặc record tương ứng |

Các giá trị review này là metadata nội dung, không phải status Jira mới.


<a id="spec-3-2"></a>

### Bảy nhóm kiểm thực hành và phạm vi nguồn tham khảo

| Nhóm kiểm | Cần chứng minh gì? | Ví dụ không đạt |
|---|---|---|
| Q01 — Đúng nhu cầu và cần thiết | Nội dung có nguồn, rationale và đúng authority xác nhận | BA/AI tự quyết ai được duyệt yêu cầu |
| Q02 — Đủ trong scope | Đủ phát biểu đơn lẻ và không bỏ sót phần đã biết của tập yêu cầu; có inventory và disposition | Chỉ có happy path, chưa xét trạng thái sai hoặc quyền sai |
| Q03 — Nhất quán | Các phát biểu/mô hình cùng điều kiện không cho kết quả mâu thuẫn | Flow cho người tạo tự duyệt nhưng permission matrix cấm |
| Q04 — Kiểm chứng được | Có setup/input, expected result và phương pháp quan sát/đo/xét đạt | “Nhanh”, “đúng”, “thân thiện” mà không có điều kiện đo/quan sát |
| Q05 — Truy vết và quản lý phiên bản | Có ID/source/dependency/version và liên kết phù hợp giai đoạn | Story ghi “theo rule hiện tại” nhưng không biết rule nào, version nào |
| Q06 — Không mơ hồ, hiểu được, tách nghĩa rõ | Người đọc độc lập hiểu cùng nghĩa; điều kiện/đơn vị/phạm vi rõ | “AM được sửa hồ sơ nếu phù hợp” nhưng không rõ hồ sơ nào, điều kiện nào |
| Q07 — Khả thi và đúng mức bàn giao | Có cơ sở thực hiện/kiểm chứng trong các constraint được giao | Solution phụ thuộc API/quyền chưa tồn tại nhưng được ghi đã khả thi |

Đây là cách nhóm phép kiểm **do CRM đề xuất**, không phải danh sách “bảy tiêu chí” nguyên bản của một framework. Bản 1.0 chỉ có năm nhãn tổng quát; bản 1.1 tách thêm Q06/Q07 để tránh bỏ qua nghĩa mơ hồ và feasibility.

IREB syllabus mục 3.8 phân biệt tiêu chí cho một requirement với tiêu chí bổ sung cho bộ hồ sơ, gồm cả non-redundant, modifiable và conformant; danh sách là khuyến nghị không mang tính bao trùm mọi hoàn cảnh. Trong CRM, các mặt này được kiểm ở Q03/Q05/Q06 và kiểm cấu trúc; không gọi năm nhãn cũ là toàn bộ chuẩn IREB. [IREB syllabus](https://hub.ireb.org/media/pages/resources/cpre-foundation-level-syllabus/9c084b1cfd-1787039954/cpre_foundationlevel_syllabus_en_v.3.3.0.pdf).

NASA Appendix C.4 đưa các câu hỏi validation cụ thể; ISTQB cung cấp kỹ thuật review/test design và coverage. Các bước, bảng inventory, ngưỡng dừng và ví dụ CRM từ mục [Chuẩn bị review và quy tắc kết luận](requirements-review-process-and-verdicts.md#spec-3-3) trở đi là cách vận dụng của dự án, không phải quy trình sao chép nguyên văn hay kết luận tuân thủ ISO. [NASA](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/), [ISTQB](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf).


<a id="spec-3-3"></a>

### Chuẩn bị review và quy tắc kết luận

**Đơn vị review:** một requirement, một nhóm rule/model hoặc toàn bộ scope được chọn của Epic/Story. Ghi rõ target và revision trước khi kiểm; “review Epic rồi” không xác định được bộ nội dung nào đã được xét.

**Bộ đầu vào:** scope/source register, danh sách actor và authority, nội dung E/S áp dụng, model/contract refs, câu hỏi/quyết định, baseline cha và danh sách delta. Nếu chưa có input cần thiết, ghi `Chưa kiểm — thiếu input`, không ghi Đạt.

**Thực hiện:** owner chuẩn bị inventory; BA/Business, Dev/TL và QA kiểm từ các góc nhìn tương ứng. Người phát hiện ghi finding với vị trí/điều kiện/counterexample; owner sửa; reviewer xác nhận closure. PM xem kết quả/evidence và rủi ro, không thay kết luận của người chuyên môn.

| Kết quả | Khi dùng | Có qua gate không? |
|---|---|---|
| Đạt | Đã làm các bước áp dụng và có evidence đáp ứng exit criteria | Có thể, nếu mọi điều kiện gate khác đủ |
| Không đạt | Có counterexample, thông tin thiếu hoặc kết luận không có cơ sở | Chưa, đối với phần bị ảnh hưởng |
| Chưa kiểm | Chưa review hoặc thiếu input/người có authority | Chưa; không chuyển thành Đạt chỉ vì không thấy lỗi |
| N/A | Phép kiểm/hạng mục thực sự không áp dụng, có lý do và reviewer xác nhận | Chỉ cho đúng phần N/A; không miễn các yêu cầu bắt buộc khác |

**Điều kiện đóng một review target để bàn giao:**

- Mọi phép kiểm áp dụng đã có kết luận Đạt và evidence, không còn ô chưa kiểm/không biết bị che bằng N/A.
- Không còn finding/câu hỏi làm thay đổi expected behavior, quyền, state/data, contract, control bắt buộc hoặc feasibility của scope chọn mà chưa được giải quyết.
- Lỗi biên tập không ảnh hưởng ý nghĩa có thể thành action không chặn với owner/hạn; không gọi finding ngữ nghĩa chưa sửa là Đạt chỉ vì PM chấp nhận thời gian chờ.
- Mọi phần loại khỏi scope/không áp dụng có quyết định và đánh giá dependency; không loại case khỏi inventory chỉ để tỷ lệ coverage đẹp.
- Verdict gắn đúng revision. Delta sau review phải đánh giá tác động và kiểm lại phần liên quan; không tự tái dùng approval cũ cho nội dung mới.

Không tính điểm trung bình giữa các phép kiểm. Q01 sai nghiệp vụ không được bù bằng Q05 có đủ link.


<a id="spec-8"></a>

## Quy trình review: bảo đảm nội dung được xác nhận bởi đúng người

| Bước | Ai làm? | Kiểm gì? | Đầu ra |
|---|---|---|---|
| 1. Xác định applicability | BA với Dev/QA và chuyên gia liên quan | E01–E16/S01–S12 áp dụng đến đâu, model nào cần, tài liệu nào tái sử dụng | Coverage/applicability list; N/A có lý do |
| 2. Discovery | BA/Business, Dev/QA cùng tham gia | Rule/ví dụ/câu hỏi, context và rủi ro; mô hình có đủ nhánh chưa | Draft và decision queue |
| 3. Read-back và phản biện | Dev/TL + QA | Dev giải thích solution; QA đề xuất case sai/biên/đồng thời; BA so với ý nghĩa nghiệp vụ | Findings và sửa mô hình/contract/AC |
| 4. Kiểm chéo | BA + Dev + QA | Cùng action có cùng guard/permission/data/state/error ở flow, model, contract và AC không | Cross-model findings đã xử lý |
| 5. Xác nhận nội dung | Business/technical/control authority | Expected result, rủi ro và constraint đúng thẩm quyền | Specialist verdict đúng revision |
| 6. PM review bàn giao | PM | Đủ output, hết blocker, phân rã hợp lý, baseline scope/manifest và approvals đúng version | Approve/return với lý do |
| 7. Merge và kiểm DoR | Người/service có quyền; Dev/QA nhận | Merge đúng nội dung đã review; Story pin refs; điều kiện thực hiện hiện tại đủ chưa | Baseline receipt, Story refs và DoR result |

Review thực hiện async trên Jira và PR; không cần họp đủ mọi role cho mọi hạng mục. Owner tổng hợp findings, reviewer xác nhận sửa; không coi comment rải rác là đã có kết luận.


<a id="spec-8-1"></a>

### Cổng trước tạo Story và cổng trước code

**Trước tạo Story:** phần Epic được chọn có model/rule/AC/solution/test approach đủ rõ; applicability và câu hỏi chặn đã xử lý; manifest được PM duyệt; bộ hồ sơ đó đã merge.

**Trước code:** Story xác định đúng subset/version, không có delta chưa duyệt; Dev/QA hiểu khớp; các điều kiện DoR còn lại như dữ liệu, dependency, quyền và capacity đã đạt. Có skeleton Story hoặc có AC chưa đủ để qua cổng này.


<a id="spec-8-2"></a>

### Kiểm máy được và phần cần con người

| Máy có thể kiểm cứng khi có dữ liệu/cấu hình tương ứng | Người chịu trách nhiệm xác nhận |
|---|---|
| Required sections/fields, ID duy nhất, ref không gãy, type/enum/schema | Nội dung đúng nhu cầu và thuật ngữ đúng nghĩa |
| Model refs hợp lệ, transition endpoint tồn tại, table/diagram IDs khớp khi có cấu trúc | Mô hình đã bao phủ các tình huống quan trọng; guards/default hợp nghiệp vụ |
| BR/AC/model → Story/test-condition links, unknown/N/A records | Expected result đúng, quyết định đúng quyền và risk scope hợp lý |
| Approval actor/revision/digest và baseline merge/manifest integrity | Solution khả thi, testcase có khả năng phát hiện lỗi và đủ kiểm độc lập |

Không lấy “AI review đạt” hoặc đủ số section làm gate duy nhất. Nội dung này chỉ xác định yêu cầu cho cơ chế kiểm; gói hiện tại chưa cài skill vào runtime hoặc cấu hình hook thực thi.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
