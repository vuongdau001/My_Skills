# Phân cấp và phân rã Capability, Epic, Story, Task

Mã tài liệu: **CRM-DECOMPOSITION** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Chọn đúng đơn vị yêu cầu và cách tổ chức công việc.

**Đọc khi:** Phân rã scope, review Story hoặc quyết định có cần Task.


## Quyết định phân cấp

Nếu đầu vào là inventory chức năng, WBS hoặc bảng estimation, áp dụng [checkpoint nguồn scope](source-scope-and-decomposition-checkpoint.md) để phân biệt đơn vị nguồn với đơn vị bàn giao, thử ranh giới nhóm và tìm phần giao thoa. Cùng tên object/file hoặc giảm số nhóm chưa đủ chứng minh allocation tốt hơn.

**Đầu vào:** Capability scope/source, mô hình/acceptance Epic, constraints/dependency và khả năng thực hiện của team. **Đầu ra:** Story manifest có scope allocation; quyết định checklist/Task có lý do. **Review:** Business/BA + Dev/TL + QA; PM chốt manifest và kế hoạch.

```text
Capability (tài liệu Git): năng lực và phạm vi tổng thể
└── Epic: một Use Case user-goal + models áp dụng + acceptance tổng thể
    ├── Story: một hành vi/kết quả kiểm chứng được
    │   └── Checklist thực hiện hoặc Task liên kết khi cần
    └── Task kỹ thuật dùng chung: một Epic owner, liên kết Story/Epic sử dụng
```

**Requirement không đồng nghĩa với ticket.** Rule, data requirement, permission, NFR và constraint có ID riêng; nhiều Story có thể cùng tham chiếu. Task không tạo một lớp yêu cầu nghiệp vụ mới.

| Cấp | Cần trả lời | Ranh giới hoàn thành |
|---|---|---|
| Capability | Cần năng lực gì, tại sao và phạm vi nào? | Acceptance năng lực trên các Epic |
| Epic | Phạm vi nghiệp vụ vận hành và được nghiệm thu thế nào? | Kết quả tổng thể + luồng liên Story |
| Story | Actor/hệ thống làm được hành vi cụ thể nào sau phần triển khai này? | Hành vi tích hợp đáp ứng AC và DoD |
| Task | Ai tạo đầu ra cụ thể nào để phục vụ triển khai? | Đầu ra đạt tiêu chí và được người nhận chấp nhận |

Trong Jira mặc định, Story và Task là hai loại công việc cùng cấp dưới Epic; Subtask là cấp dưới. Vì chưa khảo sát cấu hình thật, mặc định kế hoạch dùng **Task thuộc Epic + issue link tới Story**, không giả lập parent Story cho một standard Task. Ghi Story key và quan hệ công việc trong ticket/receipt để kiểm được; không tự thêm link type hay custom field. Task dùng chung liên kết mọi Story tiêu thụ. Nếu dùng Subtask về sau phải xác nhận workflow/reporting tương ứng trước. [Atlassian — work types](https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-types/).

Áp dụng [checkpoint chọn cấp và quan hệ cha–con](source-scope-and-decomposition-checkpoint.md#level-selection) trước khi tạo hoặc đổi cây: tìm parent hiện có, đối chiếu Capability ngang hàng, giải thích vai trò riêng của mỗi cấp và delta bàn giao. Không dùng số lượng con làm tiêu chí chọn cấp.

## Phân rã Epic thành Story theo hành vi

1. Xác nhận scope/acceptance và các mô hình dùng chung. Dẫn Use Case nguồn, liệt kê scenario/steps, actors, rules, conditions và các kết quả có thể bàn giao.
2. Chọn lát cắt theo hành vi, biến thể nghiệp vụ, kênh hoặc mức khả năng khi vẫn có kết quả hữu ích và kiểm chứng được. Không lấy frontend/backend/test làm Story mặc định.
3. Gán BR/model/AC cho từng Story. Kiểm không sót rule bắt buộc và không tính phạm vi hai lần. NFR/quyền/atomicity cần cho hành vi phải đi cùng nó.
4. Dùng Example Mapping để làm rõ rules → examples → questions. Khi chưa biết expected result, ghi câu hỏi/authority; không tự sinh Gherkin để che quyết định chưa có.
5. Review INVEST theo bảng dưới, dependency và capacity. Story quá lớn về kết quả nghiệp vụ phải tách Story; Task chỉ chia công việc, không làm Story lớn trở thành nhỏ.
6. Business xác nhận expected behavior, TL xác nhận solution, QA xác nhận testability; PM chốt scope/manifest sau các phép kiểm. [Baseline và change control](baseline-and-change-control.md) quy định thời điểm merge/tạo Jira Story.

| INVEST | Thao tác kiểm | Chưa đạt/cần xem lại khi |
|---|---|---|
| Independent | Liệt kê dependency và thử đổi thứ tự thực hiện; ghi lý do dependency không bỏ được | Dependency ẩn hoặc không có owner/contract; không đòi zero dependency |
| Negotiable | Tách outcome/constraint bắt buộc khỏi lựa chọn triển khai; ghi cơ chế change sau baseline | Khóa tùy tiện mọi chi tiết code hoặc tự đổi rule đã duyệt |
| Valuable | Nêu actor/người nhận và kết quả; minh họa một tình huống sử dụng | Chỉ có tên component, DB hoặc công đoạn |
| Estimable | Dev/QA ước lượng từ scope/model/dependency; chỉ rõ unknown tác động lớn | Dùng số ước lượng để che feasibility chưa biết |
| Small | Team xét khả năng code + tích hợp + kiểm chứng trong một Sprint | Chỉ code vừa Sprint, phần kiểm chứng để Sprint sau |
| Testable | QA viết setup/action/expected/observation từ AC | Kết quả phải hỏi lại hoặc tự đặt rule/ngưỡng |

INVEST là heuristic chất lượng Story, không thay [Q01–Q07 và review chuyên môn](requirements-review-process-and-verdicts.md). Cách tách theo giá trị tham khảo [Agile Alliance](https://agilealliance.org/glossary/story-splitting/); INVEST/SMART từ [Bill Wake](https://xp123.com/invest-in-good-stories-and-smart-tasks/); Example Mapping từ [Cucumber](https://cucumber.io/blog/bdd/example-mapping-introduction/).

## Chọn checklist hay Task

| Tình huống | Quyết định |
|---|---|
| Story nhỏ; owner điều phối được; không có nhu cầu theo dõi/bàn giao riêng | Checklist trong Story, không tạo Task |
| Nhiều phần việc cần owner/trạng thái/bàn giao riêng | Task liên kết Story; mỗi Task có đầu ra, reviewer và completion criteria |
| Có migration/pipeline/artifact dùng chung | Một Task kỹ thuật dưới Epic; links tới các Story cần nó |
| Story chứa nhiều kết quả, quá lớn cho Sprint | Tách Story trước; không chỉ đẻ Task |
| Chưa rõ rule/quyền/AC/expected outcome | Refinement và chặn scope bị ảnh hưởng; Task không sửa được thiếu requirement |
| PoC/benchmark thật sự cần timebox và evidence riêng | Task nghiên cứu được lập kế hoạch; output là kết quả/thí nghiệm/khuyến nghị, tách khỏi nghiệm thu Capability |
| AI có nhiều bước/lần chạy | Execution plan/log trong công việc; không tự động biến thành ticket |

Ghi quyết định theo mẫu: `Story/Epic — checklist hoặc Task — lý do — đầu ra/owner — dependency — approval/ủy quyền`. Cặp Dev–QA cùng làm một Story không tự động buộc tạo Task; chỉ tạo nếu có nhu cầu quản lý riêng.

**Gate phân rã Đạt:** scope allocation truy được, INVEST đã xét, các câu hỏi chặn đã đóng, không bỏ control bắt buộc, PM chốt đúng revision. Thiếu đầu vào: Chưa kiểm; có gap hoặc chồng scope: Không đạt. Không cần Task không phải là N/A cho việc lập kế hoạch thực hiện.


<a id="workflow-3"></a>

## Phân loại và phân cấp requirement


<a id="workflow-3-1"></a>

### Phân loại theo bản chất nội dung

| Loại | Cần mô tả gì? | Ví dụ CRM |
|---|---|---|
| Business requirement | Kết quả tổ chức muốn đạt | Cải thiện độ tin cậy của dữ liệu khách hàng |
| Stakeholder requirement | Nhu cầu của người/nhóm liên quan | AM cần biết khách hàng đã tồn tại và người đang phụ trách |
| Functional requirement | Hành vi hệ thống phải thực hiện | Kiểm tra quyền, phát hiện trùng, lưu và phản hồi |
| Non-functional requirement — NFR | Chất lượng/ràng buộc có cách kiểm chứng | Hiệu năng, bảo mật, tính sẵn sàng hoặc khả năng phục hồi với điều kiện đo rõ |
| Transition requirement | Điều kiện chuyển sang giải pháp mới | Mapping, làm sạch, migration và đối soát dữ liệu |

Đây là các loại nội dung, không phải năm tầng ticket. Một NFR hoặc rule dùng chung có thể áp dụng cho nhiều Epic/Story; các đối tượng đó tham chiếu cùng ID và phiên bản.


<a id="workflow-3-2"></a>

### Phân cấp theo phạm vi và công việc

| Cấp | Định nghĩa trong CRM | Nội dung cần quản lý | Nơi quản lý |
|---|---|---|---|
| Capability | Phạm vi chức năng nghiệp vụ tổng thể cần theo dõi xuyên suốt | Mục tiêu, scope, yêu cầu dùng chung, danh sách Epic, AC cấp Capability và tiêu chí nghiệm thu tổng thể | Tài liệu Git |
| Epic | Một mục tiêu sử dụng thuộc Capability, có đúng một Use Case ở E03 | Hồ sơ yêu cầu/solution, owner/readiness từng hạng mục, phương án Story, dependency và nghiệm thu Epic | Jira Epic liên kết tài liệu Git |
| Story | Một lát cắt hành vi có kết quả quan sát và kiểm chứng được | Outcome, phạm vi, BR/AC, solution refs, dependency, estimate và DoR/DoD | Jira Story tham chiếu baseline Git |
| Task | Công việc triển khai, kiểm chứng hoặc hỗ trợ kỹ thuật có đầu ra cụ thể, cần giao/theo dõi riêng | Owner, input, output, reviewer, tiêu chí hoàn tất và evidence | Jira Task |

Ví dụ đào tạo mở rộng case [Customer–Contact trong BA Getting Started](ba-getting-started.md#walkthrough). Các mã `EX-*` là mã tham chiếu trong ví dụ. Khi lập hồ sơ thực, lấy ID từ workstream.

```text
EX-C1  Capability · Quản lý Customer và Contact
├── EX-E2  Epic candidate · Tạo Customer thủ công
│   ├── E03  Use Case · Tạo Customer thủ công
│   └── EX-S2  Story candidate · AM tạo hồ sơ hợp lệ trong phạm vi đã chọn
│       Kế hoạch thực hiện · Tích hợp UI và API, rồi kiểm chứng theo AC
├── EX-E3  Epic candidate · Nhập Customer từ tệp
└── EX-E1  Epic candidate · Gắn Contact có sẵn vào Customer
    ├── E03  Use Case · Gắn Contact có sẵn
    └── EX-S1  Story candidate · Gắn Contact New/Inactive và quan sát kết quả Active theo quyền
```

`EX-E2` phục vụ tạo một hồ sơ thủ công. `EX-S2` nhận lát tạo hợp lệ cùng các kiểm quyền, validation và xử lý trùng. `EX-E3` phục vụ import tệp theo batch với mapping và lỗi theo dòng. Export theo quyền là mục tiêu độc lập nếu nằm trong Capability; dẫn privacy và data models dùng chung.

Use Case mô tả hành vi ở E03 và thuộc đúng một Epic theo [use-case-v1](epic-use-case-policy.md). Story xác định phần hành vi sẽ giao. Các đầu ra của refinement như requirement, solution và testability được theo dõi ngay trên Epic.

Nếu có công việc API cần bàn giao riêng và Jira dùng standard Task cùng cấp Story, cấu trúc ví dụ là:

```text
Epic EX-E2
├── Story EX-S2
└── Task · Bàn giao API tạo Customer đã review và kiểm thử
    Liên kết issue → Story EX-S2
```

Không bắt mọi Epic phải có nhiều Story hoặc mọi Story phải có nhiều Task. Chỉ phân rã khi giúp giao việc, review hoặc kiểm chứng rõ hơn.


## Nguồn nội dung bổ sung trước phân rã

Capability giữ [C01–C08](capability-specification-catalog.md) để xác định outcome/scope và Epic allocation. [Loại requirement và ID](requirement-types-identifiers-and-traceability.md) quy định canonical source, authority và trace; không cố định loại requirement vào một tầng backlog. [Mapping E/S→Q/D](catalog-check-model-mapping.md) dẫn tới các thao tác review. Task tiếp tục là tùy chọn; thêm catalog Capability/policy không làm phát sinh tầng ticket mới.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
