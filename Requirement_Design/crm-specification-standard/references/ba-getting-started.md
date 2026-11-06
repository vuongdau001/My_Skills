# BA Getting Started — từ nhu cầu đến phần việc có thể bàn giao

ID: CRM-BA-START · Bổ sung onboarding cho CRM Workflow Kit 1.7.1 · 04/11/2026

Đọc khi mới dùng kit, cần chuyển từ BRD/SRS/Use Case sang cách tổ chức Feature/Epic/Story/Task, hoặc chưa biết phân tích tới đâu là đủ. Guide giải thích cách dùng; tiêu chí chính thức vẫn nằm ở các catalog và gate được liên kết. Không cần đọc hết kit trước khi bắt đầu.

Lộ trình: [hiểu khái niệm](#concepts) → [theo ví dụ Customer–Contact](#walkthrough) → [chọn độ sâu](#depth) → [tự thực hành](#practice). Nếu đã có hồ sơ đang làm, vào bước tương ứng trong [START-HERE](../START-HERE.md), không bắt đầu lại từ đầu.

<a id="concepts"></a>

## 1. Ba câu hỏi để hiểu cách tổ chức thông tin

Hãy tưởng tượng người phụ trách kinh doanh nói: “Một người có thể đại diện nhiều công ty. Tôi muốn nhân viên biết đang liên hệ với ai ở từng công ty.” BA cần làm rõ nhu cầu, mô tả hệ thống cần đáp ứng và giúp đội chọn phần việc để bàn giao.

| Câu hỏi | Trục đang xét | Ví dụ |
|---|---|---|
| Yêu cầu nói về điều gì? | Loại requirement | Business, Stakeholder, Functional, Non-functional, Transition |
| Phạm vi nào được tổ chức và bàn giao cùng nhau? | Cấp phạm vi/công việc | Feature, Epic, Story, Task |
| Trình bày thông tin bằng cách nào? | Hồ sơ hoặc mô hình | BRD, SRS, Use Case, decision table, data dictionary |

Một Epic có thể áp dụng nhiều loại requirement và chứa nhiều Use Case. Một SRS có thể tập hợp nội dung từ nhiều Epic. Khi chia lại Story, requirement dùng chung vẫn giữ ID và nguồn chuẩn; cập nhật quan hệ phân bổ thay vì chép thành các bản riêng. Xem [requirement types, ID và traceability](requirement-types-identifiers-and-traceability.md).

IIBA phân loại Business requirements (mục tiêu thay đổi), Stakeholder requirements (nhu cầu của các bên), Solution requirements (Functional và Non-functional), và Transition requirements (phục vụ chuyển từ hiện trạng sang trạng thái mới). [IIBA Core Standard, mục 1.5](https://www.iiba.org/globalassets/standards-and-resources/core-standard/iiba-core-standard.pdf).

Áp dụng vào ví dụ: quản lý nhất quán người liên hệ là mục tiêu cần làm rõ; AM cần biết người đó đại diện công ty nào là nhu cầu stakeholder; cho phép gắn Contact vào Customer là hành vi chức năng. Một ngưỡng phản hồi cần đo là NFR; chuyển đổi dữ liệu quan hệ cũ khi go-live là transition. Các câu này mới minh họa loại thông tin, chưa đủ để coi là requirement đã duyệt.

## 2. Dịch các khái niệm BA sang kit

| Khái niệm quen thuộc | Cách sử dụng trong kit | Giới hạn của mapping |
|---|---|---|
| Business Case | Nguồn cho rationale, outcome và lựa chọn đầu tư của Feature | Feature không tự bao phủ phân tích chi phí/lợi ích và các phương án đầu tư |
| BRD — Business Requirements Document | Nội dung Feature, business/stakeholder requirements, constraints và decisions liên quan là đầu vào biên soạn | Một BRD có thể bao phủ nhiều Feature; không có quy tắc một Feature = một BRD |
| SRS — Software Requirements Specification | Tập hợp requirement từ Epic, shared models/controls và chi tiết/delta liên quan trong Story theo scope/revision | Cần rà coverage và consistency toàn scope; danh sách Story riêng lẻ chưa chứng minh SRS đầy đủ |
| FRD/FSD | Có thể dùng phần đặc tả chức năng của Epic để biên soạn theo template tổ chức | Cần thống nhất nghĩa các tên này trong glossary dự án |
| Use Case Specification | E03 giữ actor goal, trigger, pre/postconditions, main/alternate/exception flows; Story chọn phần áp dụng ở S03–S05 | Use Case và Story không có quan hệ 1–1 bắt buộc |
| Technical Design | Solution/contract refs, đặc biệt E09/E13 và S07 | Phân biệt lựa chọn thiết kế với requirement; BA không tự quyết cơ chế kỹ thuật chưa được chốt |
| RTM — Requirements Traceability Matrix | Các quan hệ source → requirement/rule → model → Story/AC → testcase/evidence | Trace có thể nhiều–nhiều; cần kiểm đúng revision và phần chưa phân bổ |
| Task | Đầu ra thực hiện cần giao/theo dõi riêng, áp dụng T01–T08 | Không tạo thêm một tầng yêu cầu nghiệp vụ; Task tùy nhu cầu |

IIBA giới thiệu BRD với mục tiêu, scope, business requirements và constraints. IREB định nghĩa SRS là requirements specification cho một software system và phân biệt với SyRS. Các mapping trong bảng là diễn giải áp dụng cho CRM. [IIBA — BRD](https://go.iiba.org/free-download-business-requirement-document-BRD-template), [IREB — Glossary](https://cpre.ireb.org/en/downloads-and-resources/glossary).

Muốn bàn giao BRD/SRS, chọn phạm vi và revision, tập hợp nội dung chuẩn cùng references, rà phần thiếu và thực hiện review/approval theo thỏa thuận dự án. Đây là cách biên soạn hồ sơ, không phải tính năng tự xuất tài liệu hoặc chứng nhận tuân thủ ISO của kit. [Nguồn và CRM tailoring](standards-and-crm-tailoring.md) giữ giới hạn áp dụng chuẩn.

Hai điểm cần nhớ khi đọc tài liệu từ dự án khác:

- Kit dùng Feature → Epic → Story; Task/checklist phục vụ triển khai. Azure Boards dùng Epic → Feature → User Story → Task. Jira mặc định đặt Story và Task cùng cấp dưới Epic, Subtask ở cấp dưới. Đừng suy ra parent-child trong công cụ chỉ từ sơ đồ tư duy. [Microsoft](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops), [Atlassian](https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-types/).
- `BR` trong kit là Business Rule; Business Requirement dùng `REQ` với type riêng. Business analysis task trong giáo trình là hoạt động phân tích, không tự thành ticket Task triển khai. [IIBA — BA tasks](https://www.iiba.org/knowledgehub/business-analysis-standard/4-tasks-and-knowledge-areas/introducing-business-analysis-tasks/).

<a id="walkthrough"></a>

## 3. Theo một nhu cầu Customer–Contact đến Story

Toàn bộ EX-* dưới đây là local locators của ví dụ đào tạo, không phải ID dự án được cấp. Các câu trả lời Business là giả định của bài học, không là approval hoặc policy CRM thật. Khi áp dụng vào dự án, dùng source/decision/revision thực tế và giữ câu hỏi chưa trả lời.

### Bước A — Tiếp nhận, hỏi trước những điều làm đổi cách hiểu

Input EX-N1: “Một người có thể đại diện nhiều công ty.” Trước khi vẽ màn hình hoặc chia ticket, BA hỏi:

| Câu hỏi | Câu trả lời giả định cho bài học | Tác động |
|---|---|---|
| Có cần tạo một Contact riêng cho mỗi công ty? | EX-D1: Giữ một Contact identity, liên kết nhiều Customer | Cần mô hình quan hệ; không nhân bản người chỉ để thể hiện công ty |
| Customer nào được gắn thêm Contact? | EX-D2: Customer đích phải Active tại thao tác gắn | Đây là guard của thao tác |
| Contact New/Inactive sẽ thế nào sau khi gắn thành công? | EX-D3: Tự chuyển Active | Gắn và activation nằm cùng kết quả thành công |
| Customer chuyển Inactive sau đó thì sao? | EX-D4: Không tự chuyển Contact Active sang Inactive | Guard lúc gắn không trở thành invariant liên tục |
| Gắn trùng, gắn lại quan hệ cũ và quyền được xử lý thế nào? | EX-Q1: Chưa quyết | Ghi gap ảnh hưởng selected slice, không tự chọn no-op/deny/reopen |

Đầu ra: nguồn trao đổi, những điều đã xác nhận, câu hỏi và phạm vi ảnh hưởng. Dùng [knowledge records](knowledge-records-and-evidence.md) để phân biệt Decision, Assumption, Constraint và nguồn chat/meeting. Nhu cầu được nêu trong chat chưa chứng minh đã có meeting hoặc approval toàn hồ sơ.

Prompt áp dụng, thay các chỗ trong ngoặc bằng dữ liệu thật:

> Dùng crm-setup-project trên workstream [id] để tiếp nhận notes [nguồn/revision]. Phân biệt source facts, quyết định có evidence, assumptions và câu hỏi. Liên kết hồ sơ liên quan; giữ phần chưa xác nhận ở trạng thái phù hợp.

### Bước B — Đặt Feature và chọn một phạm vi Epic

Khi bắt đầu từ function list/WBS/estimation, áp dụng [checkpoint nguồn scope](source-scope-and-decomposition-checkpoint.md) trước khi dùng số dòng làm allocation hoặc báo tiến độ. Giữ nguyên nguồn; số dòng estimation, số Epic candidates và số Story đủ DoR là các thông tin khác nhau.

Trước khi đặt tên, tìm Feature/Epic hiện có và áp dụng [phép kiểm chọn cấp/cha–con](source-scope-and-decomposition-checkpoint.md#level-selection). Cây dưới là ví dụ có điều kiện; không biến mọi yêu cầu tra cứu thành Feature riêng hoặc mọi CRM thành một cây cố định.

Feature candidate EX-F1: “Quản lý Customer và Contact”. BA làm rõ vấn đề, người hưởng lợi, outcome, in/out scope và cách đánh giá. Không tự đặt KPI hoặc thời gian phản hồi để điền đủ ô. Dùng [Feature F01–F08](feature-specification-catalog.md) và `crm-define-feature`.

Epic candidate EX-E1: “Quản lý liên kết Customer–Contact”. Phạm vi này có mô hình quan hệ, rules và acceptance chung. Chốt Epic nào chịu trách nhiệm về hồ sơ Contact và lifecycle trước khi phân bổ phần phụ thuộc. [Cây phân rã mở rộng](backlog-hierarchy-and-decomposition.md#workflow-3-2) đặt thêm nhóm hồ sơ Customer và trao đổi dữ liệu dưới cùng Feature.

Thử ranh giới bằng ba câu hỏi: các hành vi có cùng outcome và mô hình cần hiểu chung không; có thể nghiệm thu phạm vi này rõ ràng không; ai sở hữu những phần nằm ngoài nhưng bắt buộc phải dùng? Epic không mặc định tương đương Bounded Context hay một màn hình.

Một số tình huống để chọn trọng tâm, không phải taxonomy/issue types bắt buộc:

| Phạm vi đang phân tích | Cần chú ý | Khi xem lại cách nhóm |
|---|---|---|
| Tra cứu Customer/Contact | Query semantics, data scope, field visibility, empty/error states | Chỉ nhóm theo màn hình nhưng không có outcome người dùng |
| Tạo/sửa hồ sơ | Validation, duplicate, dữ liệu chung, audit | Chia riêng UI/API/DB thành các Epic cho cùng hành vi |
| Lifecycle | State, command, guard, side effect | Một thao tác trạng thái làm đổi dữ liệu của phạm vi khác nhưng chưa rõ owner |
| Quan hệ Customer–Contact | Identity, cardinality, history, uniqueness | Sửa profile và sửa relation bị trộn, không rõ nguồn dữ liệu chuẩn |
| Import/export | Mapping, lỗi theo dòng/lô, retry, quyền dữ liệu | Gộp vì đều dùng file dù outcome/acceptance khác nhau; chỉ tách khi có lý do thực tế |
| Integration/technical enablement | Consumer, contract, failure, output/quality cần đạt | Việc nhỏ chỉ cần Task/PoC lại được nâng thành Epic |

Import dùng thường xuyên là chức năng sản phẩm; migration một lần để chuyển hệ thống là transition. Permission/NFR dùng chung vẫn áp dụng tại mọi hành vi liên quan, dù có công việc kỹ thuật riêng để hỗ trợ.

### Bước C — Viết flow và liên kết các mô hình cần thiết

Với Use Case “Gắn Contact vào Customer”, BA diễn đạt ngắn:

1. Người dùng chọn hai identity và yêu cầu gắn.
2. Hệ thống kiểm quyền, Customer Active và constraints quan hệ.
3. Nếu hợp lệ, thực hiện gắn và chuyển Contact New/Inactive sang Active.
4. Trả kết quả cho phép người dùng quan sát đúng liên kết theo quyền.

Preconditions gồm các đối tượng tồn tại và dữ liệu đầu vào theo contract. Success postcondition gồm đúng liên kết và Contact Active. Nếu Customer không Active, yêu cầu gắn bị từ chối, không tự đổi Customer để vượt guard. Nhánh trùng/relink, concurrency và lỗi giữa các bước vẫn cần chốt; chưa thể coi bốn dòng trên là đặc tả hoàn chỉnh.

Điểm cần giải thích lại bằng lời: “Customer Active khi gắn” và “Contact phải luôn có Customer Active” là hai quy tắc khác nhau. EX-D4 cho phép Contact giữ Active sau khi Customer chuyển Inactive. Nhầm guard thành invariant sẽ làm sai cả solution và tests.

Chọn model theo câu hỏi cần trả lời: flow cho đường đi; decision table cho tổ hợp điều kiện; state model cho transition; data dictionary cho identity/relation; permission matrix cho ai được làm gì. Dẫn [mapping E/S → model/evidence](catalog-check-model-mapping.md) và [D01 — Use Case](models/business-flows-and-use-cases.md). Diagram hữu ích khi cần nhìn nhánh/phối hợp; không bắt vẽ lại mọi thông tin đã rõ bằng bảng hoặc bước văn bản.

Prompt áp dụng:

> Dùng crm-specify-epic cho [Epic/revision], selected scope [hành vi]. Walkthrough từ trigger tới postcondition; liên kết rules/data/quyền/state. Ghi rõ expected result đã có nguồn và nhánh còn cần Business/TL/QA quyết định.

### Bước D — Chọn Story theo kết quả bàn giao

EX-S1: “Người dùng có quyền gắn Contact New/Inactive vào Customer Active; khi thành công, Contact chuyển Active để sử dụng đầu mối liên hệ đó.”

Story này nhận cả link và activation, cùng guards bắt buộc. “Kiểm trạng thái”, “tạo API” và “viết màn hình” không tự thành ba Story. Use Case giúp hiểu tương tác; Story chọn scope phát triển. Một Use Case có thể được phân bổ qua nhiều Story và một Story có thể sử dụng nhiều phần mô hình. [Agile Alliance — User Stories](https://agilealliance.org/glossary/user-stories/).

Một Story candidate khác có thể nhận gắn Contact đang Active với pháp nhân thứ hai. Gộp/tách còn tùy outcome, constraints và sizing của team; tên khác hoặc một nhánh khác chưa tự chứng minh cần Story riêng. Use-Case 2.0 minh họa cách chia thành các slices để phát triển từng phần có giá trị. [Ivar Jacobson — Use Cases](https://www.ivarjacobson.com/publications/articles/use-cases-ultimate-guide).

AC draft của EX-S1:

| Locator | Điều kiện và thao tác | Kết quả mong đợi / mức đã rõ |
|---|---|---|
| EX-AC1 | Contact New, Customer Active, mọi quyền/constraints đạt; gắn thành công | Đúng hai identity được liên kết, Contact chuyển Active |
| EX-AC2 | Contact Inactive, cùng điều kiện hợp lệ; gắn thành công | Cùng Contact chuyển Active; không tạo Contact khác |
| EX-AC3 | Customer không Active; yêu cầu gắn mới | Không tạo liên kết từ yêu cầu bị chặn, giữ status Contact ban đầu |
| EX-AC4 | Trùng/relink hoặc lỗi giữa link và activation | Expected behavior chi tiết Pending; chưa báo toàn thao tác thành công khi thiếu postcondition |

EX-AC1/2 chưa chứng minh toàn Story đủ rõ: quyền, relation constraints và EX-AC4 còn gap. Có thể tiếp tục refinement; chỉ chọn một phần độc lập khi chứng minh phần đó thực sự không phụ thuộc quyết định chưa có. Không bỏ permission/failure bắt buộc để tạo vẻ Ready.

Trace minh họa: EX-N1 → EX-D3 → rule tự activation → flow gắn → EX-S1 → EX-AC1/2 → test conditions cho New và Inactive. Test run chỉ được bổ sung khi thực thi thật. Dự án dùng IDs/revisions theo [quy ước](requirement-types-identifiers-and-traceability.md), không sao chép EX-* làm registry thật.

### Bước E — Làm rõ solution, review và bàn giao

Dev/TL làm rõ contract và cơ chế đạt postcondition khi lỗi/đồng thời; QA cùng BA xác nhận oracle, test conditions và dữ liệu kiểm. BA không tự chọn DB transaction hay compensation chỉ để khép flow. `crm-design-solution` có thể diễn ra lặp với việc đặc tả và phân rã.

Khi chuẩn bị Story, chọn subset và pin shared model/rule revision; viết delta ở Story. Không sao chép toàn Epic. [Story S01–S12](story-specification-catalog.md) cho biết nội dung cần có; [phân rã/INVEST](backlog-hierarchy-and-decomposition.md) giúp kiểm kích thước và giá trị.

Dev/QA lập kế hoạch: API/data, UI integration, verification có thể là checklist hoặc Task riêng nếu có nhu cầu giao đầu ra. [Ví dụ quyết định Task](examples/decomposition-and-task-decisions.md) giải thích cả hai cách. Task Done chưa chứng minh Story đáp ứng AC tích hợp.

Review ghi findings, tác giả sửa bằng workflow authoring, rồi review lại revision. Chuẩn bị baseline và approval/merge theo [baseline/change control](baseline-and-change-control.md); kiểm DoR theo [gate](readiness-completion-and-approval-gates.md). Tạo draft, review đặc tả, baseline approval, đủ DoR và runtime acceptance là các kết luận riêng. [Walkthrough baseline → delivery](examples/baseline-to-delivery-walkthrough.md) tiếp tục phần sau của bài học.

<a id="depth"></a>

## 4. Phân tích tới đâu là đủ cho bước đang làm?

| Thời điểm | Cần đủ để làm gì? | Phần có thể tiếp tục làm rõ |
|---|---|---|
| Mới nhận nhu cầu | Hiểu vấn đề, source, stakeholders, scope sơ bộ và câu hỏi ưu tiên | Chi tiết flow/solution, acceptance chưa chốt ghi Pending |
| Chọn phạm vi Epic | Có outcome, ranh giới, dependencies và shared controls cần điều tra | Những phạm vi tương lai chưa được chọn có thể giữ draft |
| Chuẩn bị selected slice để baseline | Requirement/model/solution/AC ảnh hưởng lát cắt đủ rõ, review và decisions đúng authority | Phần độc lập ngoài baseline tiếp tục refinement; ghi disposition và impact |
| Nhận Story để triển khai | Có baseline/scope, đủ điều kiện DoR, input/quyền/dependency/capacity tương ứng | Dev quyết chi tiết tổ chức code trong constraints; không tự quyết business behavior còn thiếu |
| Hoàn tất | Có evidence đúng build/revision và acceptance theo gate áp dụng | Lợi ích sau sử dụng được đo theo kế hoạch riêng nếu authority cho phép |

Đây là bảng chỉ đường, không thay gate. Không đòi đóng mọi câu hỏi của cả Feature trước khi làm một scope độc lập. Đồng thời, tất cả yêu cầu áp dụng cho scope được chọn phải được xét: hạng mục “có điều kiện” cần quyết applicability, không tự bỏ vì chưa có thông tin. [Feature theo từng bước](feature-specification-catalog.md), [Epic catalog](epic-specification-catalog.md).

Sau mỗi lượt làm việc, BA nên nói được: “Tôi đang làm target/revision nào; đã làm rõ điều gì; còn quyết định nào chặn phần nào; ai cần trả lời; bước tiếp theo là gì.” Có thể dùng `crm-report-status` để hỏi next step từ hồ sơ hiện hành, không cần tạo report file cho mỗi câu hỏi.

## 5. Nhận ra cách dùng sai và sửa ngay

| Cách làm dễ gặp | Điều cần sửa |
|---|---|
| Feature = BRD, Epic = SRS, Story = Use Case | Mapping nội dung/phạm vi, giữ quan hệ nhiều–nhiều |
| Mỗi bước Use Case hoặc mỗi mục SRS tạo một Story | Chọn outcome có thể bàn giao; controls bắt buộc đi cùng hành vi |
| Điền đủ E01–E16 là Epic đã Ready | Kiểm applicability, chất lượng và evidence theo selected scope/gate |
| Chia Story quá lớn thành nhiều Task rồi coi là Small | Xem lại cách chia hành vi và sizing của team |
| Tạo Task “chốt quyền sau” để cho Story bắt đầu | Ghi câu hỏi/blocker; quyền ảnh hưởng hành vi phải rõ đúng thời điểm |
| Tạo Epic security rồi cho Story export bỏ kiểm quyền | Shared control vẫn áp dụng ở từng consumer |
| Dùng câu trả lời AI làm Decision Approved | Xác minh nguồn, authority và scope; đề xuất vẫn là đề xuất |
| Các test dự kiến đều có tên nên báo QA Pass | Phân biệt coverage dự kiến với kết quả chạy và verdict thật |

<a id="practice"></a>

## 6. Thử tự giải thích và áp dụng

Hãy giải thích bằng lời cho đồng nghiệp: “Feature giữ năng lực và mục tiêu; Epic giữ phạm vi nghiệp vụ và mô hình chung; Story chọn hành vi bàn giao; Task chia việc thực hiện. BRD/SRS tập hợp thông tin cho người nhận; Use Case mô tả cách actor đạt mục tiêu.” Nếu chỉ nhớ tên mà chưa nêu được ví dụ, quay lại EX-S1.

Bài tập chuyển tình huống: Business yêu cầu “Cho AM xuất danh sách Contact theo bộ lọc để chuẩn bị chăm sóc khách hàng.” Chưa biết AM được xem trường nào, có xuất lịch sử hay không và giới hạn dữ liệu. Hãy tự trả lời trước khi xem gợi ý:

1. Ba câu hỏi nào cần ưu tiên và vì sao?
2. Đề xuất một Story outcome, nêu dependency và hai AC candidate.
3. Có cần Task riêng ngay không? Nội dung nào còn chặn baseline/DoR?
4. Nếu nhận được một file SRS hiện có, bạn sẽ tái sử dụng nó thế nào?

Gợi ý đối chiếu: ưu tiên data/field permission, nghĩa filter/current-history và giới hạn volume/output. Story có thể là “AM có quyền xuất Contact trong phạm vi được phép theo bộ lọc được chọn”; AC candidate gồm dữ liệu khớp filter trong scope quyền và không lộ field ngoài quyền, nhưng oracle cụ thể vẫn Pending. Task tùy đầu ra/phân công. Tái sử dụng sections/requirements đúng revision của SRS, rà khoảng trống và phân bổ theo outcome; không tạo một Story cho mỗi chương. Có thể có nhiều cách chia hợp lý, miễn giải thích được giá trị và coverage.

Prompt để bắt đầu trên dự án thật:

> Dùng crm-spec-kit. Tôi là BA, workstream [id], có nguồn [file/revision] và target [ID nếu đã có]. Hãy chọn bước phù hợp, làm phần phân tích trong phạm vi [scope], nêu câu hỏi ưu tiên và lý do. Dẫn lại rule/model có sẵn; giữ những điều chưa xác nhận. Cuối lượt cho biết một bước tiếp theo và input cần có.

Người hướng dẫn có thể dùng bài tập này để quan sát BA tự chọn workflow, tạo draft và chỉ ra gaps. Ghi chỗ BA phải hỏi trợ giúp để cải thiện guide. Structural validation hoặc tác giả tự làm bài không chứng minh onboarding đã được BA độc lập thử thành công.

Khi chỉ triển khai một phần Epic, đối chiếu [cách phân bổ dependency theo scope](knowledge-records-and-evidence.md#phân-bổ-dependency-khi-chỉ-bàn-giao-một-phần-epic). Scope viết bằng chữ không thay typed links mà gate sử dụng.
