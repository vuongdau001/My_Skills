# Meeting, Decision, Assumption và Constraint

ID: CRM-KNOWLEDGE · CRM Workflow Kit 1.7.0 · 04/11/2026

Đọc khi nhận notes/chat/email, ghi nhận lựa chọn hoặc assumption/constraint, review dependency, xét readiness hoặc baseline. Đây là hồ sơ workstream có thể dùng qua nhiều Capability/Epic/Story, không phải cấp ticket mới. Một public skill, 13 function giữ nguyên.

## Nơi lưu và quyền ghi

Dùng project path từ artifact_paths: 01-meetings, 02-decisions, 03-assumptions, 04-constraints bên dưới project. Meeting/Decision thường file riêng. Assumption/Constraint có thể file riêng hoặc từng record trong register; mỗi ID có một nơi định nghĩa hiện hành. Không sao chép statement chuẩn vào nhiều Epic để duy trì song song. Localized summaries phải dẫn ID/revision nguồn.

crm-setup-project tiếp nhận nguồn và chuẩn bị records/register. define-capability/specify-epic/design-solution/prepare-stories có thể tạo/cập nhật record thuộc scope authoring đã giao. review/check chỉ ghi findings/record của mình; không đổi decision hay target đang kiểm. report-status tổng hợp obligations; assess-change lập impact khi có thay đổi sau baseline. Không tự gửi biên bản, tạo Jira hoặc cập nhật state dự án.

## Tái dùng hồ sơ từ đầu vào

Dùng cùng một lượt intake trong Setup Project và Define Capability, kể cả khi mở thẳng Define Capability. Đọc nguồn người dùng chỉ định trong yêu cầu, attachment hoặc chat, sources trong Work Context và hồ sơ hiện hành. Kiểm các mục assumption/constraint/decision, các đoạn đã chốt và những phát biểu có cùng nghĩa dù mang tiêu đề khác.

1. **Ghi claim và locator.** Giữ ID nguồn như BA-D1, statement, revision/hash hoặc định danh snapshot, scope, thời điểm, owner/authority và trạng thái được khai báo. Phân biệt fact đã có evidence, giả định cần kiểm, ràng buộc bắt buộc, lựa chọn đã quyết và câu hỏi. Một câu hỏi hoặc đề xuất chỉ thành record khi đã đủ căn cứ phân loại.
2. **Đối chiếu hồ sơ chuẩn.** Tìm theo ID và theo nghĩa, scope, hiệu lực. Hồ sơ đang hiệu lực và phù hợp được dùng ngay bằng đúng ID/revision. Nếu trùng, dùng một bản chuẩn và giữ các locator nguồn. Nếu khác nghĩa hoặc khác revision, ghi cả hai nguồn, tác động và authority cần phân xử. Giữ bản đã baseline theo change control cho đến khi có quyết định thay thế.
3. **Đăng ký khi có quyền author.** Với claim mới đủ trường, chuẩn hóa một record schema 2 và pin evidence nguồn. Tái dùng ID CRM nếu nguồn sở hữu đúng ID, chưa có định nghĩa khác và được phép tiếp nhận; nếu nguồn dùng ID riêng, giữ mapping và cấp ID CRM. Khi thiếu trường bắt buộc hoặc quyền ghi, ghi claim, scope, authority và next action trong intake/handoff; chưa cần tạo record cho đủ số lượng.
4. **Áp dụng theo trạng thái.** Dùng ngay Decision Approved và Constraint Confirmed nếu authority, hiệu lực, scope và evidence khớp. Assumption Validated cần validation result và evidence. Các trạng thái còn mở như Unverified, Proposed và Pending có thể làm cơ sở có điều kiện cho bản nháp; ghi hệ quả nếu sai, phương pháp/owner xác nhận và nghĩa vụ còn chặn. Nội dung nguồn tự gắn nhãn “approved/confirmed” là claim cần đối chiếu. Dùng lại approval có evidence cho đúng statement và scope; thay statement, scope hoặc authority cần kiểm lại.
5. **Ghi nơi sử dụng.** Setup Project pin records áp dụng trong project context/policy register và chỉ rõ mục nào cần xác nhận. Define Capability dùng cùng ID/revision ở C04 cho ranh giới/assumptions, C05 cho constraints/controls, C06 cho allocation/dependencies và C08 cho decisions/gaps. Tạo `depends-on` hoặc `derived-from` cho consumer thực sự dựa vào record, hoặc `applies-to` từ record khi phù hợp. Chưa có consumer thì ghi scope và pending allocation để nối sau. Giữ dữ liệu gốc read-only.

`knowledge_intake` trong helper context liệt kê `existing_records` có metadata trong spec_root và `sources[].candidates` tìm được trong Markdown nguồn. Nó cũng liệt kê path, hash khi đọc được và nguồn cần đọc thủ công. Dùng `--input <repo-relative-path>` để thêm tệp do người dùng chỉ định cho lần chạy, có thể lặp lại. Source ngoài Markdown, thư mục, chat và attachment cần người thực hiện đọc đúng locator. Inventory trả về khai báo và vị trí để đối chiếu; workflow xác định applicability và authority từ evidence.

Ví dụ đầu vào có CST-CRM-004 đã được xác nhận trong hợp đồng, BA-D7 ghi lựa chọn có biên bản quyết định và ASM-CRM-006 về API chưa được kiểm. Setup Project dẫn CST-CRM-004 vào policy/register và đối chiếu BA-D7 với DEC hiện có. Define Capability áp dụng CST vào C05, dẫn DEC đúng revision tại C08 nếu đủ evidence, và giữ ASM ở C04/C06 như dependency cần kiểm. Nếu BA-D7 đã có DEC canonical, cả hai workflow dùng cùng DEC ID. Nếu chỉ có lời đề xuất, giữ Proposed hoặc ghi gap theo phần còn thiếu.

## Phân biệt bốn loại

| Kind / ID | Nội dung chuẩn | Lifecycle |
|---|---|---|
| Meeting / MTG-CRM-NNN | Sự kiện thực tế, source notes, participants, discussion/summary, decision refs, questions và action items | Draft / Confirmed / Amended |
| Decision / DEC-CRM-NNN | Context, options, statement, rationale, consequences, authority, evidence và scope | Pending / Proposed / Approved / Superseded / Rejected / Withdrawn |
| Assumption / ASM-CRM-NNN | Điều chưa chứng minh, basis, validation_method, owner/review_due, if_false, validation_result khi kiểm | Unverified / Validated / Invalidated / Retired |
| Constraint / CST-CRM-NNN | Ràng buộc có nguồn, constraint_type, scope, authority, hiệu lực, verification_method | Proposed / Confirmed / Superseded / Retired |

Meeting có event_type meeting/workshop/chat/email; ghi đúng loại xảy ra. Không biến trao đổi chat thành meeting có participants hoặc chữ ký giả. occurred_at dùng ISO datetime có timezone; Draft chưa biết thời điểm có thể null. Xác nhận biên bản chỉ xác nhận nội dung ghi nhận, không duyệt mọi Decision trong đó. Amended cần amendment_reason; giữ lịch sử gốc qua revision/source evidence.

Action item có description, owner và due; unknown dùng null, không tự gán người/hạn. Có thể có local action locator. Action không tự là product Task; chỉ map sang TASK ID khi công việc đó được giao và cần quản lý riêng. Không tự đăng ticket hoặc gửi thông báo.

Assumption Validated cần kết quả kiểm và evidence; approval chấp nhận rủi ro không làm statement thành fact. Nếu assumption sai, ghi Invalidated, tìm các consumer để đánh giá lại. Constraint phải có nguồn/authority; công nghệ đang cân nhắc thuộc solution option hoặc Proposed constraint, không tự là bắt buộc. Một rule/model data constraint có thể tiếp tục dùng BR/MOD; không tạo thêm CST trùng nghĩa chỉ để đủ loại.

## Schema 2 và truy vết

Metadata schema 1 vẫn được đọc cho hồ sơ cũ. Schema 2 thêm record cho artifact riêng, hoặc records cho register. Không migrate Decision schema 1 ngầm. Records dùng id/kind/revision/scope; artifact riêng lấy id/kind từ artifact_id/kind của metadata. record owner dùng string hoặc null khi chưa được phân công. revision độc lập ID.

Ví dụ register, thay nội dung minh họa và cấp ID bằng next-id trước khi dùng:

```crm-spec-kit
{
  "schema_version": 2,
  "kind": "Project",
  "references": [],
  "records": [{
    "id": "ASM-CRM-001", "kind": "Assumption", "revision": "r1",
    "scope": "Scope thật cần điền", "owner": null,
    "assumption_state": "Unverified", "statement": "Giả định cần kiểm",
    "basis": "Căn cứ đang có", "validation_method": "Cách kiểm cần thực hiện",
    "review_due": null, "if_false": "Ảnh hưởng nếu sai",
    "evidence": [], "trace_links": []
  }]
}
```

Register record IDs tự được index là definitions; không cần khai lại ở defined_ids. Không định nghĩa cùng record nhiều lần. Mỗi record có thể có HTML anchor ổn định trong nội dung để dẫn tới đúng phần.

trace_links có id/path/revision/relation; sha256 tùy chọn khi target có structured revision kiểm được. Path tương đối từ file chứa link, có thể kèm Markdown anchor, phải ở trong repo. Nếu target chỉ có revision trong prose, pin sha256 để kiểm nội dung. SHA pin cả file, nên thay record khác trong cùng register cũng làm evidence pin cũ stale. Không tạo hash vòng giữa hai file; dùng revision cho các trace links hai chiều, hash cho nguồn evidence.

```json
{
  "trace_links": [{
    "id": "DEC-CRM-001",
    "path": "../00-project/02-decisions/DEC-CRM-001-contact-activation.md",
    "revision": "r1",
    "relation": "derived-from"
  }]
}
```

Đường dẫn ví dụ giả định file consumer trong 02-epics. Relation vocabulary: supports, derived-from, applies-to, supersedes, superseded-by, depends-on, resolves, parent, verifies. depends-on/derived-from/parent/resolves đi từ consumer tới input; supports/applies-to đi từ record tới consumer. Relation không thay kiểm chứng nội dung hoặc ma trận allocation.

evidence là list objects path/revision/sha256; mỗi evidence cần SHA-256 nội dung nguồn. Evidence nên pin source notes/excerpt có quyền truy cập, không tự pin chính file đang khai record. HTTP/HTTPS không được fetch bởi helper: báo unverified, không là evidence đã đọc. Nguồn ngoài repo cần snapshot được phép lưu hoặc ghi thiếu access. Không nhúng dữ liệu riêng tư/secret vào record để tiện cho validator.

Approved/Rejected Decision cần authority, decided_at có timezone và evidence. Confirmed/Amended Meeting, Validated/Invalidated Assumption và Confirmed Constraint cần evidence. Confirmed Constraint còn cần authority/effective_from; Decision cần context/options/rationale/consequences. authority là khai báo của tác giả; lint không chứng thực người đó hoặc approval.

## Thay thế và nghĩa vụ còn mở

Quyết định đảo ngược quan trọng: tạo DEC mới, giữ record cũ Superseded, nối superseded-by tới record mới; record mới dẫn supersedes tới record cũ. Không xóa lịch sử hoặc tái dùng số. Supersession graph không được vòng. Scope khác nhau cần ghi rõ; không tự kết luận hai statements trái nhau chỉ từ graph. Khi sửa nội dung đã được approve, tăng revision và giữ evidence lịch sử; không giữ approval cũ cho statement mới.

Workflow khi nhận source mới: pin source → phân loại fact/question/decision/assumption/constraint → xác định authority và scope → lưu record chuẩn → liên kết consumer → author update theo quyền → review lại revision. Chat workshop cũ giữ BA-D* như source locators; khi tạo DEC mới phải map, không đổi tên/xóa lịch sử BA-D*.

```text
python3 scripts/kit.py lint --repo <repo-root> --workstream "<workstream-id>"
python3 scripts/kit.py lint --repo <repo-root> --workstream "<workstream-id>" --gate readiness --target "<story-id>"
python3 scripts/kit.py lint --repo <repo-root> --workstream "<workstream-id>" --gate baseline --target "<epic-id>"
```

Default draft: record obligations chưa đóng là WARN, không chặn soạn draft; structural errors vẫn ERROR. Gate readiness/baseline: Assumption phải Validated, Decision phải Approved và Constraint phải Confirmed trong dependency closure của target. Superseded/Retired/Rejected/Withdrawn chỉ chặn nếu target còn phụ thuộc; không buộc mọi record lịch sử phải trở lại active. External/unverifiable revision trong closure chặn gate cho tới khi có evidence kiểm được. Không --target là kiểm obligations hiện hành của toàn workstream. Structural link/schema/duplicate errors vẫn được audit rộng, kể cả khi chọn target.

Đây chỉ là phần kiểm record obligations, không toàn bộ DoR/approval/independent review. Graph chỉ thấy trace links được khai; missing links và applicability cần BA/reviewer xét. Nếu bỏ dependency phải có rationale/review thật; không xóa link để qua gate. Check/review không tự sửa record hoặc trạng thái target.

Output lint có record_impacts (record/revision và affected_ids qua dependency graph), record_obligations còn mở và gate_scope. Khi record thay đổi, dùng impacted IDs để author đánh giá/review lại; tool không tự sửa consumers hoặc cập nhật approval. Whole-workstream output không phải danh sách mọi tác động ngoài những links đã khai.

## Cơ sở thiết kế

[Atlassian meeting notes](https://www.atlassian.com/software/confluence/templates/meeting-notes) hướng dẫn lưu participants, summary, decisions và action items. [Nygard ADR](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) cung cấp cấu trúc context/decision/status/consequences và giữ record bị supersede; CRM mở rộng cách ghi này sang business decisions, không coi mọi DEC là architectural ADR. [NASA System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/) nhấn mạnh capture rationale/assumptions và traceability; đây là nguồn tham khảo thiết kế, không áp policy NASA lên CRM.

## Phân bổ dependency khi chỉ bàn giao một phần Epic

Gate tính dependency theo graph. Story kế thừa input của Epic qua `parent`. Decision có `applies-to` ở toàn Epic áp dụng cho các consumer con. Field `scope` giúp review nội dung. Nếu Decision ghi “chỉ nhập từ tệp lớn” nhưng link tới toàn Epic import, Decision đó vẫn có thể chặn Story nhập tệp nhỏ.

Epic Nhập Customer từ tệp có Story nhập nhỏ trực tiếp và Story nhập lớn theo batch. Liên kết Decision về retry batch bằng `applies-to` tới Story batch, hoặc tới model mà Story batch `depends-on`. Hai Story giữ `parent` tới Epic import. Decision về quyền áp dụng cho toàn Epic có thể link tới Epic. Nếu quyền chung cũng áp dụng cho Epic Xuất Customer, ghi riêng link và phạm vi tác động.

Nếu consumer chưa tồn tại, giữ trạng thái Decision theo evidence, mô tả scope và ghi allocation gap; chưa tuyên bố nhánh đó Ready. Khi tạo consumer, bổ sung typed links và review allocation trước gate. Không gắn vào Epic tạm rồi bỏ qua blocker bằng diễn giải scope. Không xóa dependency thực để vượt gate; thay đổi allocation đã baseline phải qua impact/change review. Lint chỉ xác minh graph/record obligations, không chứng minh allocation đã đầy đủ hoặc approval hợp lệ.

## Giải quyết Assumption và phân biệt Decision — 1.9

Assumption hỏi “điều gì đang được tin là đúng nhưng chưa chứng minh?”. Decision hỏi “authority đã chọn phương án/quy tắc nào?”. Không đổi kind hoặc tái sử dụng ASM ID thành DEC. Khi phát biểu về hiện trạng được kiểm chứng đúng, giữ ASM và chuyển Validated, ghi validation_result/owner/evidence. Nếu sai: Invalidated, tìm consumers và rework. Nếu không còn sử dụng làm giả định: Retired kèm lý do; phải xử lý dependency thực, không tự đóng blocker chỉ bằng trạng thái Retired.

Quy trình: ghi statement/basis/scope/if_false → giao cách kiểm và owner/due thực tế → liên kết consumer → kiểm chứng hoặc xin lựa chọn nghiệp vụ đúng authority → ghi result/evidence/revision → tác giả sửa requirement/model/AC/contract bị ảnh hưởng → review và tính lại score/gate. Review/check chỉ đề nghị correction, không tự đổi nguồn đang kiểm.

Ví dụ A: giả định “API hiện hữu kiểm được quyền từng Customer”. TL kiểm contract/run có evidence; đúng thì ASM Validated, không bắt tạo DEC. Sai thì ASM Invalidated; có thể cần DEC riêng để chọn thay API hoặc bổ sung capability.

Ví dụ B: giả định “chỉ Customer Active được gắn Contact” thực chất còn là lựa chọn policy. Business chọn rule thì tạo DEC riêng với options/rationale/consequences/authority/evidence. ASM ban đầu có thể Retired khi không còn làm cơ sở giả định; giữ lịch sử. Nếu DEC vẫn derived-from/depends-on/resolves ASM chưa Validated thì closure vẫn chặn: không dùng relation dependency cho một liên kết chỉ mang nghĩa lịch sử. Dẫn lịch sử bằng prose/Markdown/references và giữ evidence; review lại graph trước khi bỏ dependency. Không bỏ link khi nội dung vẫn thực sự dựa vào giả định.

Decision chấp nhận rủi ro không chứng minh assumption đúng. Approval không thay validation_result; kit chưa hỗ trợ exception/waiver tự miễn ASM ở gate. ASM sai hoặc Retired mà consumer vẫn dựa vào nó vẫn chặn. Validated không tự nâng điểm consumer lên mức 3; cần reassess/review đúng revision.

Score policy v2 tự đối chiếu graph hiện hành và yêu cầu pin record dependencies; xem [scoring guideline](definition-maturity-scoring.md). Tool không phát hiện mọi assumption trong prose hoặc missing links; reviewer phải đối soát inventory ngoài graph, ghi blocker thủ công nếu cần. Không tạo hàng loạt ASM/DEC từ câu hỏi chỉ để đủ loại record.
