# Standard viết và trình bày artifact CRM

ID: CRM-ARTIFACT-WRITING · CRM Workflow Kit 2.6.0 · 16/11/2026

Standard này áp dụng cho mọi artifact do kit soạn hoặc chỉnh sửa, ở mọi dự án và workstream. Người đọc phải tìm được nội dung chính, hiểu điều kiện/kết quả và biết việc cần làm tiếp. Standard điều chỉnh cách viết; nội dung bắt buộc, quyền và gate vẫn theo catalog/workflow tương ứng.

## Phạm vi áp dụng

Áp dụng cho Capability, Epic, Story, Task; requirement/BR/AC; model, solution, UI/API/read contract; project/source/scope/policy/question registers; Decision/Assumption/Constraint; Review, revision áp dụng, change assessment, Report, TestCase/TestRun, Pilot và handoff.

Markdown dùng chuẩn dưới đây. JSON/config/assessment/evidence giữ schema gốc, không thêm prose hoặc HTML vào dữ liệu máy đọc. Tóm tắt chat dùng cùng nguyên tắc ngôn ngữ và phân biệt evidence nhưng không bắt tạo file hay đủ mọi mục của template.

## 1. Ngôn ngữ và thuật ngữ

Viết câu tiếng Việt đầy đủ: ai làm gì, trong điều kiện nào, kết quả gì. Giữ tên domain/DDD/tech, role, state, field và source IDs khi cần chính xác; giải thích lần đầu nếu người nhận có thể chưa quen.

| Tránh dùng như câu ghi chú | Cách diễn đạt rõ hơn |
|---|---|
| Selected authoring | Phạm vi đang làm rõ |
| Business/BA xác nhận meaning | Business/BA xác nhận ý nghĩa nghiệp vụ |
| QA oracle/testability | QA xác nhận kết quả mong đợi và khả năng kiểm chứng |
| Owner/backup/due | Người phụ trách, người thay thế và thời hạn |
| Canonical UI | Giao diện được chọn làm chuẩn |
| Consumer | Chức năng hoặc nơi sử dụng dữ liệu/contract |

Không dùng dấu `/`, `;` hoặc chuỗi từ tiếng Anh để thay nhiều mệnh đề. Không dịch/đổi hàng loạt Customer, Contact, Aggregate, Active, CURRENT, tên field hoặc ID nguồn. Viết tắt role không tự chứng minh quyền phê duyệt của một cá nhân.

<a id="business-and-sdlc-roles"></a>

### Vai trò nghiệp vụ và trách nhiệm SDLC

Gọi tên vai trò theo việc người đó làm trong ngữ cảnh đang mô tả. Từ `stakeholder` cần nói rõ là bên liên quan nghiệp vụ hay bên liên quan dự án.

| Thuật ngữ | Dùng khi |
|---|---|
| Actor nghiệp vụ | Vai trò của người hoặc hệ thống bên ngoài trực tiếp tương tác với hệ thống trong Use Case. Ghi bước, mục tiêu hoặc đóng góp của actor. |
| Bên liên quan nghiệp vụ | Người hoặc nhóm hưởng lợi, chịu tác động, vận hành nghiệp vụ hoặc có quyền lợi cần bảo vệ. Khi nhóm cũng trực tiếp tương tác với hệ thống, mô tả thêm vai trò actor ở Use Case tương ứng. |
| Bên liên quan dự án và vai trò SDLC | Người hoặc nhóm quan tâm đến phạm vi, tiến độ, nguồn lực hoặc việc bàn giao. Nếu có trách nhiệm cụ thể, ghi vai trò tổ chức, phân tích, triển khai, review, kiểm thử hoặc chốt bàn giao tại Work Context hoặc hồ sơ tương ứng. |
| Người có thẩm quyền xác nhận | Người hoặc nhóm được giao quyền xác nhận một nội dung cụ thể. Ghi nội dung, phạm vi, revision và evidence của lần xác nhận. |

Một người có thể kiêm nhiều vai trò. Ghi từng vai trò với trách nhiệm và evidence riêng. Ví dụ, một quản lý Sales có thể duyệt yêu cầu trong CRM với tư cách actor, rồi tham gia nghiệm thu với tư cách người được giao xác nhận nghiệp vụ. Quyền thao tác trong CRM và quyền ký nghiệm thu có nguồn xác nhận riêng.

Khi dùng `owner`, ghi rõ họ phụ trách dữ liệu, hồ sơ, kiểm chứng giả định, review hay bàn giao. Khi dùng `approval` hoặc `policy`, ghi rõ đó là quyết định trong nghiệp vụ, xác nhận đặc tả/nghiệm thu sản phẩm hay quy tắc SDLC. Với Decision, Assumption và Constraint, ghi [phạm vi áp dụng](knowledge-records-and-evidence.md#record-applicability) trong nội dung đọc được.

## 2. Thứ tự đọc trong mỗi artifact

1. **Tiêu đề:** ID nếu có và tên thể hiện mục đích.
2. **Ý chính:** mục tiêu hoặc kết quả scoped của tài liệu trong một đoạn ngắn.
3. **Bối cảnh cần biết:** target, scope, revision, nguồn, vai trò và trạng thái áp dụng.
4. **Nội dung chính:** các mục của catalog/template; mỗi mục giải quyết một câu hỏi.
5. **Điểm chưa chốt và việc tiếp theo:** ID, phạm vi ảnh hưởng, người cần trả lời và output tiếp theo.
6. **Metadata:** dữ liệu cho helper ở cuối file.

Không biến thứ tự này thành sáu heading trống trong mọi tài liệu. Artifact nhỏ có thể gộp bối cảnh/handoff; artifact dài giữ mục C/E/S/T và thêm mục con theo nội dung. ID và anchor đã được tham chiếu phải được giữ hoặc có mapping khi thay đổi có kiểm soát.

## 3. Đoạn văn, danh sách và bảng

Mỗi đoạn một ý. Dùng đoạn ngắn cho mục đích/lý do/giới hạn; dùng danh sách đánh số cho trình tự, bullet cho nội dung cùng cấp.

| Thông tin | Hình thức nên dùng |
|---|---|
| Vai trò và trách nhiệm | Bảng ngắn, ghi riêng actor, bên liên quan nghiệp vụ, vai trò SDLC và thẩm quyền xác nhận từng nội dung |
| Phạm vi | Tách trong phạm vi, phụ thuộc, ngoài phạm vi và điểm chưa quyết |
| Mapping ID, trạng thái so sánh | Bảng, mỗi ô một thông tin ngắn |
| Rule/AC hoặc câu hỏi có nhiều giải thích | Mỗi ID một mục, dùng nhãn điều kiện/kết quả/gap |
| Evidence/hash dài | Metadata hoặc phần tham chiếu riêng; không lấp bảng nghiệp vụ bằng SHA-256 |

Ưu tiên ít cột; nếu mỗi ô phải chứa cả rule, source, owner, evidence và gap dài thì tách bảng hoặc chuyển sang từng mục. Không đặt giới hạn số cột/dòng như một semantic gate. Dùng heading và bold để phân cấp, không nhấn mạnh toàn đoạn; tránh nested list nếu không cần thứ bậc thật.

## 4. Rule, flow và Acceptance Criteria

Một rule/AC cần cho người đọc tìm được: điều kiện, tác nhân/thao tác, kết quả quan sát, nhánh lỗi/giới hạn và nguồn. Dùng nhãn sau khi phù hợp:

- **Điều kiện:** actor, quyền, trạng thái, dữ liệu và thời điểm áp dụng.
- **Thao tác:** command hoặc hành vi cụ thể.
- **Kết quả:** response, dữ liệu/trạng thái và tác động phụ cần có/không được có.
- **Truy vết:** requirement, BR/model/decision và revision.
- **Chưa chốt:** câu hỏi và phần kết quả chưa có authority xác nhận.

Flow trình bày các bước chính, sau đó tách nhánh thay thế/ngoại lệ. Phân biệt guard tại thời điểm command với invariant phải duy trì liên tục. Không tự chọn outcome, API, DB transaction hay ngưỡng để làm template trông hoàn chỉnh. AC còn thiếu kết quả quan trọng phải được nhận diện là draft/gap.

## 5. Dữ liệu nguồn, đề xuất và phê duyệt

Tách rõ nguồn ghi nhận, suy luận, đề xuất, quyết định nghiệp vụ và approval có evidence. Nêu source locator/revision; suy luận theo quy ước question binding của dự án. Khi nguồn khác nhau, giữ witness và câu hỏi cần authority xử lý.

DEC/ASM/CST schema 3 không state; review_verdict và lifecycle của Epic/Story/Task vẫn theo schema riêng. Không dùng bố cục đẹp, checklist đầy, điểm cao hoặc đổi agent profile để nâng trạng thái. Thiếu owner/due thì ghi chưa được giao hoặc null theo schema; không biến thành N/A nếu chưa có reason/authority.

## 6. Cách tổ chức theo loại artifact

| Nhóm | Nội dung cần để người đọc tra được |
|---|---|
| Capability | Nhu cầu/outcome; bên liên quan nghiệp vụ; phạm vi; requirements chung; Epic allocation; acceptance; quyết định — C01–C08 |
| Epic | Actor/domain terms; flows, state/rules, data/quyền, UI/API, ngoại lệ, NFR/migration, solution, AC, Story candidates và gaps — E01–E16 |
| Story | Actor/outcome; selected scope/model/BR/AC; điều kiện/thất bại; test approach; kế hoạch và DoD — S01–S12 |
| Task | Mục đích, một Epic owner và các Story/Epic sử dụng đầu ra. Đầu ra, ranh giới, inputs, dependency, owner, tiêu chí kiểm và evidence khi đóng — T01–T08 |
| Requirement/BR/AC register | Index ngắn; một mục cho mỗi ID có statement, type nếu áp dụng, source/revision, applies-to, cách kiểm và gap |
| Model/solution/UI/API/read contract | Mục đích và consumers; assumptions/constraints; options/contract; flows/data/quyền/errors; verification và quyết định còn thiếu |
| Project/source/scope/policy register | Bối cảnh; danh mục tra; phạm vi/authority/evidence; tình trạng và câu hỏi; mapping giữ một nơi định nghĩa |
| Question register | Một mục mỗi ID; câu hỏi cụ thể; scope bị ảnh hưởng; người/nhóm cần trả lời; record liên quan |
| Nguồn meeting/chat/email | Đọc tại sources đã cấu hình; giữ locator/evidence, phân loại sang ASM/DEC/CST hoặc câu hỏi mở. Không soạn Meeting record đầu ra hoặc thêm state cho biên bản. |
| Decision | Câu cần quyết và phạm vi áp dụng; context/options/rationale/consequences; authority/state/evidence; ảnh hưởng và bước tiếp |
| Assumption | Statement/basis và phạm vi áp dụng; cách kiểm, người phụ trách và hạn; if-false; kết quả/evidence và consumer cần xem lại |
| Constraint | Ràng buộc, loại và phạm vi áp dụng; nguồn, thẩm quyền và hiệu lực; applies-to; cách kiểm tuân thủ và gaps |
| Review/check | Target/scope/revision; cách kiểm/witness; expected/observed; findings; verdict scoped; closure/receiver |
| revision áp dụng/change assessment | Scope và manifest/version; approvals/evidence; thay đổi/impact; người thực hiện; actual action/merge receipt và việc còn thiếu |
| Assessment | Snapshot/mẫu số/nguồn; kết quả chính; chi tiết theo target; blocker/uncertainty; next actions; tách declared/effective khi có scoring |
| TestCase/TestRun | Input/setup và scope/version; bước/expected; observed nếu đã thực thi; build/config/evidence; verdict và retest |
| Handoff | Đầu ra/revision; đã làm/kiểm/duyệt/thực hiện thực tế; gap; receiver; bước tiếp và điều kiện bắt đầu |

Chọn template cụ thể trong kit; dùng [mẫu artifact chung](../assets/templates/artifact-document-template.md) cho loại chưa có template riêng. Không tạo thêm file chỉ để đủ các nhóm trên, không ép mọi loại artifact theo cùng một form. Catalog vẫn quyết định nội dung bắt buộc.

## 7. Metadata và khả năng đọc bằng công cụ

Với Markdown mới, đặt đúng một block crm-spec-kit ở cuối; có thể dùng details/summary để thu gọn khi viewer hỗ trợ. Viewer không hỗ trợ vẫn đọc được nghiệp vụ trước JSON. Block mở/đóng fence ở đầu dòng, không indent trong HTML.

Schema 1 vẫn dùng cho loại được hỗ trợ; DEC/ASM/CST mới theo schema 3 không state; biên bản chỉ là nguồn đầu vào, không tạo Meeting record. Giữ ID, source locators, evidence hash và typed dependency links. Không thêm prose/HTML vào JSON/config/assessment hoặc đổi schema vì đổi format. [Metadata/lint](artifact-metadata-and-lint.md) định nghĩa hợp đồng máy đọc.

Helper stdout kỹ thuật, JSON và tài liệu nguồn nhập vào được giữ theo hợp đồng gốc. Bản báo cáo Markdown do helper sinh cũng theo thứ tự đọc này; không sửa kết quả tính hoặc evidence cho đẹp.

## 8. Biên tập tài liệu đã có

Áp dụng khi tạo hoặc sửa artifact thuộc scope đã giao. Update package không tự rewrite toàn bộ dự án, source hoặc historical records. Project có template/policy riêng thì giữ requirements được duyệt, chỉ điều chỉnh presentation trong quyền; nêu xung đột cần giải quyết, không tự xóa field bắt buộc.

Khi byte/locator thay đổi: giữ lịch sử có thể truy lại và ghi revision mới, đối chiếu các refs/pins/consumer bị ảnh hưởng và review lại đúng scope. Riêng DEC/ASM/CST áp dụng [current-state policy](knowledge-records-and-evidence.md#record-current-state): file chỉ giữ nội dung/state mới nhất; revision và lý do đổi lưu trong Git, không tạo snapshot/history file để lưu từng lần thay record. Review/check chỉ tạo record, không sửa target đang kiểm. Giữ verdict/approval cũ đúng revision; sửa format không tự cấp lại sign-off.

## 9. Tự kiểm trước khi giao

- Người đọc tìm được ý chính, phạm vi, kết quả và việc tiếp theo mà không tự giải mã chuỗi từ viết tắt?
- Mỗi đoạn/bảng có một mục đích rõ; field/ID không bị mất khi tách bố cục?
- Actor, bên liên quan nghiệp vụ và vai trò SDLC đã được ghi đúng nơi? Người xác nhận có thẩm quyền đúng nội dung và scope?
- Proposal/gap còn được ghi rõ, expected behavior không bị tự điền?
- Rule/model/AC còn cùng nghĩa, source/revision và các controls áp dụng?
- Metadata/reference/ID/record links còn đọc được; lint đã chạy trong phạm vi cần thiết?

Đây là kiểm presentation của tác giả và reviewer, không là DoR/DoD/Business approval. Lint cấu trúc không tự đánh giá độ dễ đọc hoặc tính đúng nghiệp vụ. Không tự thêm readability score hoặc gate số học.

## 10. Minh họa hỗ trợ review và AI tra cứu

Khi soạn hoặc review phần hành vi/điều kiện/quan hệ khó đọc, dùng [CRM-VISUAL-REVIEW](review-visualization-standard.md) để chọn diagram, bảng hoặc ví dụ theo mục đích. Bảng/văn bản có cấu trúc đã đủ rõ thì không cần thêm hình chỉ để đủ số lượng. Quyền, decision logic, dictionary và coverage thường cần matrix hơn diagram.

Minh họa giữ source text/model có thể chỉnh sửa, tên/anchor và context ID/revision/scope, nhãn điều kiện/kết quả và trace tới nội dung chuẩn. Ưu tiên đọc source ngay trong viewer hỗ trợ và giữ mô tả text trong artifact chuẩn; không bắt xuất hoặc lưu thêm file render. Ảnh không là nguồn duy nhất cho requirement mới. Unknown/proposal vẫn dẫn question/authority; không tự lấp hành vi để làm kín hình. Kiểm source/render và semantics riêng; chưa render phải ghi rõ giới hạn. Không tự sửa historical artifacts hoặc nâng gate do bổ sung minh họa.

## 11. DEC/ASM/CST không state

Record mới dùng template schema 3 và [mô hình đơn giản](knowledge-records-and-evidence.md#record-current-state). Giữ nội dung hiện hành, nguồn và nơi sử dụng. Cùng vấn đề thì giữ ID, tăng revision khi sửa. ASM được xác nhận chuyển sang DEC ID, cập nhật mọi consumer rồi xóa ASM. Decision/Constraint hết áp dụng thì cập nhật nơi dùng trước khi bỏ. Không thêm state, bảng lifecycle, timeline hoặc field trạng thái thay thế. Lịch sử qua Git khi được giao; chưa commit thì nói rõ, không tự commit. Các loại artifact khác giữ schema riêng; biên bản là input source, không tạo Meeting record.

## 12. Tham chiếu phải đọc được, không chỉ có mã

Trong prose, bảng review, gap, nhãn diagram và trace hiển thị cho người đọc, dùng **tên ngắn có nghĩa + ID + link**, ví dụ “Kiểm trùng Customer (BR-CRM-027)” hoặc “Xử lý đồng thời và phục hồi (CC-Q06)”. Nhãn phải đúng nội dung target, không suy thêm outcome hoặc approval. AC không có tên thì thêm tiêu đề mô tả kết quả đang kiểm; giữ ID. Với heading links, khi tên đổi phải kiểm và cập nhật fragment/consumer bị ảnh hưởng; HTML anchor legacy chỉ migrate trong scope được giao.

Không dùng mã trần hoặc rút gọn prefix như `CC-Q03/06`, `BR-CRM-027/031`, `B05/B07` để thay lời giải thích. Dùng tên và link riêng, phân cách bằng dấu phẩy, chấm phẩy hoặc từ “và”; khi nhiều tham chiếu làm câu/bảng quá dài, nhóm theo ý nghĩa và dẫn tới index có tên. Luồng/bước/nhánh/kết quả dùng tiền tố FLOW/STP/B/OUT và tên theo [D01](models/business-flows-and-use-cases.md#mã-local-của-luồng-bước-nhánh-và-kết-quả); bước phải ghi STP03 và hành động, không chỉ “03”, và không dùng B03 cho một bước luồng chính. Câu hỏi giữ ID để tìm nhưng nhãn nêu điều cần xác nhận. Giải thích các cụm như “winner/conflict/response” thành yêu cầu nào được tạo, lỗi xung đột và kết quả phản hồi.

ID trong heading định nghĩa, source locator, JSON, API/code và metadata vẫn giữ nguyên theo hợp đồng máy đọc; không đổi ID, field, path hoặc anchor chỉ để viết đẹp. Không bắt dịch các thuật ngữ domain/tech đã được dùng nhất quán. Rationale/điều kiện/kết quả không được thay nghĩa khi biên tập nhãn.

Hồ sơ Markdown mới ưu tiên heading links và không chèn thẻ `<a id="…"></a>` để định vị. Heading chứa ID nghiệp vụ và tên dễ hiểu, viết Unicode NFC; lấy fragment từ heading theo [policy heading links](epic-use-case-policy.md#heading-links-unicode-và-chuyển-đổi). Giữ dấu tiếng Việt; literal Unicode và URL mã hóa UTF-8 được helper kiểm. Heading đổi tên/thứ tự có thể đổi fragment, phải cập nhật links/metadata/consumer đúng scope.

HTML anchor trong hồ sơ cũ vẫn được helper đọc để tương thích. Khi được giao migrate, thay tags và cập nhật link cùng lúc, ghi mapping; không chỉ xóa tag, giấu vào comment hoặc giữ link cũ không có đích. Không tự migrate lịch sử hoặc thêm HTML/PDF phụ để khắc phục viewer. Lint không bảo đảm mọi viewer có cùng thuật toán slug; kiểm viewer cụ thể khi được giao và ghi phần chưa kiểm.

**Một nguồn chuẩn:** Markdown/spec/model hiện hành là nơi đọc và chỉnh sửa nội dung chuẩn. Preview trong viewer không tạo artifact cần duy trì. Chỉ xuất HTML/PDF/ảnh hoặc bản trình bày khác khi người dùng yêu cầu hay scope bàn giao đã giao rõ; bản xuất là derivative theo revision, không thêm definition hiện hành. Không làm gate phụ thuộc việc có file export chỉ vì có diagram/anchor. Mockup/Prototype và test evidence được yêu cầu riêng theo scope/gate hiện hành không phải bản sao tài liệu và giữ nghĩa vụ riêng của chúng.

Self-check/reviewer rà link labels, mã rút gọn, nhãn bước/nhánh và câu đầy slash trong scope được giao; thử tìm đích từ tên rồi kiểm ID/anchor còn khớp. Đây là quy định author/review về readability, không thêm approval gate hoặc tuyên bố lint tự hiểu mọi nhãn. Không tự rewrite tài liệu ngoài scope hoặc các record lịch sử.

## 13. Phân cấp thị giác bằng Markdown thuần

Áp dụng cho mọi artifact trong scope author/correction được giao. Mục tiêu là phân biệt phần chính, nhóm, item và dữ liệu hỗ trợ ngay cả khi viewer làm H3/H4 khá nhỏ. Không thêm CSS/HTML, bản đọc phụ hoặc thay đổi nghiệp vụ để đạt bố cục. Giữ catalog, thứ tự template, ID, state và approval semantics.

### Cấp heading và nhãn

| Cấp | Vai trò | Cách viết |
|---|---|---|
| H1 | Tên tài liệu | Một tiêu đề chính có ID/tên theo loại artifact |
| H2 | Phần chính | Catalog C/E/S/T hoặc các mục bắt buộc của template; giữ E03 ở đầu heading để helper nhận diện |
| H3 | Nhóm nội dung hoặc item trực thuộc phần chính | FLOW, nhóm review, mỗi BR/AC khi cấp cha phù hợp |
| H4 | Item trực thuộc một nhóm | STP, B, OUT, câu hỏi hoặc finding nếu nằm dưới H3 |
| Nhãn trong item | Điều kiện, thao tác, kết quả, người nhận… | Chữ đậm trong danh sách gọn, không tạo heading chỉ để phóng chữ |

Heading của item có ID có thể in đậm cả **mã + tên** bên trong H3/H4, ví dụ `#### **B01 Không có quyền tạo**`; người đọc thấy rõ ranh giới, slug vẫn theo nội dung heading. Không bọc H2 E03 bằng markup làm che prefix mà helper cần nhận diện. Không nhảy cấp để chọn cỡ chữ, không dùng heading cho câu diễn giải bình thường. Heading đã pin không đổi text/fragment chỉ vì thêm nhấn mạnh; nếu thật sự đổi tên phải kiểm/cập nhật consumer theo policy.

### Nội dung chính, điểm mở và truy vết

- Gom các trường cùng cấp trong một item thành danh sách liên tiếp: **Điểm rẽ**, **Điều kiện**, **Thao tác**, **Kết quả**, **Tiếp tục/kết thúc** theo nội dung áp dụng. Không chèn dòng trống giữa các bullet ngắn chỉ để tạo khoảng cách. Nếu một trường chứa nhiều đoạn dài, dùng đoạn/mục riêng thay vì ép cả khối vào bullet.
- Dùng blockquote có nhãn **Chưa chốt**, **Giới hạn** hoặc state thực tế cho phần cần phân biệt với kết quả đã có căn cứ. Không dùng màu hoặc icon làm kênh phân biệt duy nhất; không đổi Proposed/Unknown thành một kết luận đã duyệt. Không đặt mọi đoạn trong blockquote.
- Đặt *Nguồn*, *Truy vết* và thông tin đối chiếu ở cuối item; có thể dùng nhãn nghiêng để bớt cạnh tranh với kết quả chính. Link vẫn có tên có nghĩa, ID và đích đúng. Rationale của quyết định hiện hành, điều kiện và expected result là nội dung chính, không hạ thành ghi chú mờ hoặc bỏ vào metadata.
- Dùng `---` giữa các item dài cùng cấp hoặc các phần chính khi tài liệu dày. Không đặt đường phân cách giữa mọi dòng/bullet hoặc trong bảng; không dùng separator để bù cho cấp heading sai. Đặt dòng trống quanh separator để tránh bị hiểu là setext heading.
- Dùng đoạn ngắn cho câu chuyện, mục tiêu, giải thích và lý do. Chỉ dùng list khi thông tin là các bước, thuộc tính hoặc các điểm song song; không biến toàn bộ văn bản thành checklist.
- Dùng bảng cho so sánh/mapping/matrix. Nếu mỗi ô chứa nhiều câu, nguồn, gap và receiver, chuyển từng ID thành mục có cấu trúc; không nén nội dung để giữ bảng và không đặt giới hạn số cột thành gate nghiệp vụ.
- Metadata nằm cuối theo schema, JSON/config và code fences giữ nguyên hợp đồng. Markdown là nguồn duy nhất; preview bằng viewer không tạo nghĩa vụ xuất/duy trì HTML/PDF.

### Áp dụng theo loại tài liệu

| Loại | Giữ cấu trúc riêng | Khối trình bày phù hợp |
|---|---|---|
| Capability | C01–C08, outcome, allocation, acceptance liên Epic | Mục tiêu bằng đoạn; allocation/matrix bằng bảng; mỗi CAP-AC dài là item rõ điều kiện/kết quả/nguồn |
| Epic/Story | E01–E16 hoặc S01–S12, flow/rule/AC | FLOW/STP/B/OUT và BR/AC có mã/tên nổi; hành vi gọn, gap tách riêng, trace ở cuối |
| Task | T01–T08 và output/verification | Danh sách output, ranh giới, điều kiện hoàn tất và evidence; không suy Done từ checklist đầy |
| DEC/ASM/CST | Thứ tự mục của template và một state hiện hành | Bối cảnh ngắn; statement/rationale/basis/source rõ; blockquote cho phần chưa có authority/validation |
| Review/check | Scope/revision, cách kiểm, observed/evidence và verdict | Mỗi finding/scenario một item; tách expected/observed/gap; không làm nổi verdict như đã có authority khi chỉ self-check |
| Report/handoff/register | Kết quả scoped, nguồn, người nhận và việc tiếp theo | Tóm tắt trước; bảng index ngắn, mục chi tiết cho nội dung dài; status khác action/approval |

Không ép các loại thành cùng một form. Template chuyên biệt quyết định các mục bắt buộc; quy tắc này chỉ điều chỉnh cách nhìn. Khi chỉnh artifact cũ, chỉ format phần được giao, giữ source/historical records và không rebaseline hoặc chuyển state do presentation.

### Self-check và giới hạn công cụ

Người soạn kiểm: ranh giới các item có nhìn thấy được, phần hành vi/expected result khác phần chưa chốt, list có gọn và bảng có cần tách không. So trước/sau để bảo toàn statement, state, ID, link destinations và heading fragments; tăng revision và xử lý consumer pin theo policy khi byte thay đổi. Reviewer ghi witness/locator cụ thể nếu khó đọc hoặc mất nghĩa, không chấm điểm dựa số bullet/separator/diagram. Lint kiểm cấu trúc/link/schema, không chứng nhận bố cục đẹp trên mọi viewer hoặc semantic approval.
