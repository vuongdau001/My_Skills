# Standard viết và trình bày artifact CRM

ID: CRM-ARTIFACT-WRITING · CRM Workflow Kit 1.10.0 · 05/11/2026

Standard này áp dụng cho mọi artifact do kit soạn hoặc chỉnh sửa, ở mọi dự án và workstream. Người đọc phải tìm được nội dung chính, hiểu điều kiện/kết quả và biết việc cần làm tiếp. Standard điều chỉnh cách viết; nội dung bắt buộc, quyền và gate vẫn theo catalog/workflow tương ứng.

## Phạm vi áp dụng

Áp dụng cho Capability, Epic, Story, Task; requirement/BR/AC; model, solution, UI/API/read contract; project/source/scope/policy/question registers; Meeting/Decision/Assumption/Constraint; Review, Baseline, change assessment, Report, TestCase/TestRun, Pilot và handoff.

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
| Vai trò và trách nhiệm | Bảng ngắn, tách người sử dụng khỏi người review/phê duyệt |
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

Giữ vocabulary của schema: Pending, Proposed, Approved, Unverified, Validated, Chưa kiểm… Không dùng bố cục đẹp, checklist đầy, điểm cao hoặc đổi agent profile để nâng trạng thái. Thiếu owner/due thì ghi chưa được giao hoặc null theo schema; không biến thành N/A nếu chưa có reason/authority.

## 6. Cách tổ chức theo loại artifact

| Nhóm | Nội dung cần để người đọc tra được |
|---|---|
| Capability | Nhu cầu/outcome; stakeholder và authority; phạm vi; requirements chung; Epic allocation; acceptance; quyết định — C01–C08 |
| Epic | Actor/domain terms; flows, state/rules, data/quyền, UI/API, ngoại lệ, NFR/migration, solution, AC, Story candidates và gaps — E01–E16 |
| Story | Actor/outcome; selected scope/model/BR/AC; điều kiện/thất bại; test approach; kế hoạch và DoD — S01–S12 |
| Task | Mục đích, một Epic owner và các Story/Epic sử dụng đầu ra. Đầu ra, ranh giới, inputs, dependency, owner, tiêu chí kiểm và evidence khi đóng — T01–T08 |
| Requirement/BR/AC register | Index ngắn; một mục cho mỗi ID có statement, type nếu áp dụng, source/revision, applies-to, cách kiểm và gap |
| Model/solution/UI/API/read contract | Mục đích và consumers; assumptions/constraints; options/contract; flows/data/quyền/errors; verification và quyết định còn thiếu |
| Project/source/scope/policy register | Bối cảnh; danh mục tra; phạm vi/authority/evidence; tình trạng và câu hỏi; mapping giữ một nơi định nghĩa |
| Question register | Một mục mỗi ID; câu hỏi cụ thể; scope bị ảnh hưởng; người/nhóm cần trả lời; record liên quan |
| Meeting/chat/email | Sự kiện và participants thật; nguồn; nội dung ghi nhận; decisions/questions/actions tách riêng; trạng thái xác nhận biên bản |
| Decision | Câu cần quyết; context/options/rationale/consequences; authority/state/evidence; ảnh hưởng và bước tiếp |
| Assumption | Statement/basis; cách kiểm, owner/hạn; if-false; kết quả/evidence và consumer cần xem lại |
| Constraint | Ràng buộc/loại; nguồn/authority/hiệu lực; applies-to; cách kiểm tuân thủ và gaps |
| Review/check | Target/scope/revision; cách kiểm/witness; expected/observed; findings; verdict scoped; closure/receiver |
| Baseline/change assessment | Scope và manifest/version; approvals/evidence; thay đổi/impact; người thực hiện; actual action/merge receipt và việc còn thiếu |
| Report/assessment | Snapshot/mẫu số/nguồn; kết quả chính; chi tiết theo target; blocker/uncertainty; next actions; tách declared/effective khi có scoring |
| TestCase/TestRun/Pilot | Input/setup và scope/version; bước/expected; observed nếu đã thực thi; build/config/evidence; verdict và retest |
| Handoff | Đầu ra/revision; đã làm/kiểm/duyệt/thực hiện thực tế; gap; receiver; bước tiếp và điều kiện bắt đầu |

Chọn template cụ thể trong kit; dùng [mẫu artifact chung](../assets/templates/artifact-document-template.md) cho loại chưa có template riêng. Không tạo thêm file chỉ để đủ các nhóm trên, không ép mọi loại artifact theo cùng một form. Catalog vẫn quyết định nội dung bắt buộc.

## 7. Metadata và khả năng đọc bằng công cụ

Với Markdown mới, đặt đúng một block crm-spec-kit ở cuối; có thể dùng details/summary để thu gọn khi viewer hỗ trợ. Viewer không hỗ trợ vẫn đọc được nghiệp vụ trước JSON. Block mở/đóng fence ở đầu dòng, không indent trong HTML.

Schema 1 vẫn dùng cho loại được hỗ trợ; knowledge records mới theo schema 2. Giữ ID, source locators, evidence hash và typed dependency links. Không thêm prose/HTML vào JSON/config/assessment hoặc đổi schema vì đổi format. [Metadata/lint](artifact-metadata-and-lint.md) định nghĩa hợp đồng máy đọc.

Helper stdout kỹ thuật, JSON và tài liệu nguồn nhập vào được giữ theo hợp đồng gốc. Bản báo cáo Markdown do helper sinh cũng theo thứ tự đọc này; không sửa kết quả tính hoặc evidence cho đẹp.

## 8. Biên tập tài liệu đã có

Áp dụng khi tạo hoặc sửa artifact thuộc scope đã giao. Update package không tự rewrite toàn bộ dự án, source hoặc historical records. Project có template/policy riêng thì giữ requirements được duyệt, chỉ điều chỉnh presentation trong quyền; nêu xung đột cần giải quyết, không tự xóa field bắt buộc.

Khi byte/locator thay đổi: giữ snapshot hoặc lịch sử có thể truy lại, ghi revision mới, đối chiếu các refs/pins/consumer bị ảnh hưởng và review lại đúng scope. Review/check chỉ tạo record, không sửa target đang kiểm. Giữ verdict/approval cũ đúng revision; sửa format không tự cấp lại sign-off.

## 9. Tự kiểm trước khi giao

- Người đọc tìm được ý chính, phạm vi, kết quả và việc tiếp theo mà không tự giải mã chuỗi từ viết tắt?
- Mỗi đoạn/bảng có một mục đích rõ; field/ID không bị mất khi tách bố cục?
- Proposal/gap còn được ghi rõ, expected behavior không bị tự điền?
- Rule/model/AC còn cùng nghĩa, source/revision và các controls áp dụng?
- Metadata/reference/ID/record links còn đọc được; lint đã chạy trong phạm vi cần thiết?

Đây là kiểm presentation của tác giả và reviewer, không là DoR/DoD/Business approval. Lint cấu trúc không tự đánh giá độ dễ đọc hoặc tính đúng nghiệp vụ. Không tự thêm readability score hoặc gate số học.
