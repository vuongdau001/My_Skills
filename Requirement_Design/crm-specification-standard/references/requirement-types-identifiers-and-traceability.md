# Loại requirement, quy ước ID và truy vết

Mã tài liệu: **CRM-IDENTIFIERS** · Gói CRM 1.3.1 · 03/11/2026

**Đọc khi:** ghi nhận nguồn/yêu cầu, tạo model/AC, phân bổ sang backlog hoặc đổi scope. **Đầu vào:** nhu cầu/constraints, glossary, scope và authority. **Đầu ra:** requirement register, ID ổn định và quan hệ truy vết đúng phiên bản.

Use Case user-goal có MOD ID do đúng một Epic sở hữu trong defined_ids. Trace target dùng ID, path có locator E03 và revision của Epic. Giữ ID qua revision và pin evidence cũ khi mở baseline mới. [Policy Epic–Use Case](epic-use-case-policy.md).

## Loại nội dung không phải cấp ticket

| Loại | Thông tin phải làm rõ và cách kiểm | Nơi duy trì nguồn chuẩn/phạm vi áp dụng | Authority và evidence |
|---|---|---|---|
| Business | Vấn đề/cơ hội, kết quả mong muốn, đối tượng hưởng lợi, cách đánh giá; nếu là KPI có baseline/target/method/window hoặc decision pending | Capability hoặc register dùng chung; có thể liên nhiều Capability/Epic | Business/Sponsor theo quyền; source/rationale và phương pháp xác nhận outcome |
| Stakeholder | Bên liên quan nghiệp vụ, hoàn cảnh, nhu cầu, kết quả có thể xác nhận và xung đột giữa các nhóm | Capability/Epic hoặc register chung; Story cụ thể hóa phần hành vi | Đại diện và người có thẩm quyền xác nhận nhu cầu đó, cùng ví dụ/read-back và cách xử lý xung đột |
| Functional | Điều kiện/trigger, action, outcome, quyền/state/data/error áp dụng | Epic/shared models, Story chọn subset/delta | Business chốt nghĩa, TL feasibility, QA testability; model/AC/test conditions |
| Non-functional | Quality/control, scope, điều kiện đo/inspection, threshold hoặc chuẩn bắt buộc, owner | Shared requirement hoặc Capability/Epic/Story theo phạm vi thật | Business/control/TL tùy nội dung; measurement/control method và evidence yêu cầu |
| Transition | Thay đổi để chuyển sang giải pháp mới: data mapping, reconcile, cutover/restore, điều kiện chuyển giao | Capability/Epic migration/operations; triển khai qua Story/Task phù hợp | Data/Ops/Business/TL; mapping, tiêu chí đối soát/khôi phục/nghiệm thu |

Mỗi requirement có `type` từ năm loại trên và `applies_to` theo scope thực tế. Không buộc Business chỉ ở Capability hay NFR chỉ ở Epic. Một rule/model hỗ trợ nhiều requirement; một requirement phân bổ nhiều Story. Không tạo requirement record trùng chỉ vì nó được dùng ở nhiều cấp.

## Chất lượng Business và Stakeholder requirement

Business: đối chiếu source → vấn đề → outcome; hỏi ai nhận lợi ích và điều gì cho thấy đạt. Outcome định lượng có đơn vị, baseline quan sát hoặc kế hoạch thu thập, target được authority chốt, population/window/method. Outcome định tính có điều kiện chấp nhận quan sát được hoặc phương pháp đánh giá rõ. Không ép mọi outcome thành KPI số và không invent target.

Với Stakeholder requirement, xác định bên liên quan nghiệp vụ, người đại diện, hoàn cảnh, nhu cầu và ví dụ đáp ứng hoặc phản ví dụ; yêu cầu Dev/QA diễn giải lại. Khi hai nhóm muốn kết quả trái nhau, ghi conflict/authority và đóng decision trước bàn giao scope bị ảnh hưởng.

Cả hai áp dụng Q01–Q07 như các requirement khác, không chỉ Q01. Q04 được thực hiện bằng phương pháp đánh giá phù hợp cấp độ, không ép mọi business outcome thành API assertion. [Capability catalog](capability-specification-catalog.md) phân biệt nghiệm thu sản phẩm và đánh giá lợi ích sau sử dụng.

## Quy ước ID cho hồ sơ mới

Dùng dạng `PREFIX-CRM-NNN` (NNN là số có ít nhất ba chữ số; cấp số duy nhất trong namespace prefix của dự án). ID không mang version, parent hoặc ý nghĩa có thể thay đổi; version là trường riêng. ID đang tồn tại được giữ nguyên nếu duy nhất và truy vết được; không đổi hàng loạt chỉ để khớp cách viết mới.

| Namespace/prefix | Đối tượng | Quy tắc |
|---|---|---|
| REQ | Requirement với type riêng | Cả Business/Stakeholder/Functional/NFR/Transition dùng REQ; type không phải cấp ticket |
| BR | Business Rule | **Không dùng BR cho Business Requirement**; BR có source requirement/decision |
| AC | Acceptance criterion | Có scope/parent refs, điều kiện và expected result; liên requirement/model |
| MOD | Model hoặc model item | Ghi kind: flow/state/transition/data/permission/UI/contract…; item có ID đầy đủ hoặc local ID dưới model ID |
| DEC | Quyết định | Người quyết, nguồn, reason, version/scope bị ảnh hưởng |
| MTG | Meeting/workshop/chat/email record | Ghi đúng event type; source evidence, participants và action items, không tự thành approval |
| ASM | Assumption | Căn cứ, owner/cách xác minh, revision, kết quả và scope bị ảnh hưởng nếu sai |
| CST | Constraint | Ràng buộc có source/authority, scope/hiệu lực và cách kiểm; không thay BR/MOD data constraints đã có |
| BASE | Baseline manifest | Selected scope, refs/commit và approval; không dùng làm code SHA |
| CAP / EPIC / STORY / TASK | Logical work/scope object | Jira key là mapping riêng; Task chỉ khi cần |
| TC / RUN | Test case / test run | TC liên AC/requirement; RUN pin testcase/build/config/environment |

Các mã C01/E01/S01/T01/Q01/D01 của **bộ chuẩn** là checklist IDs, không là ID requirement CRM. Policy category IDs như POL-SEVERITY và mã finding cũng không thuộc namespace requirement/model. Jira key do Jira cấp, không ép thành logical ID.

**Ví dụ cú pháp ID.** Dùng định dạng bên dưới và lấy số từ workstream khi lập hồ sơ thực: AC-CRM-001 (acceptance tạo khách hàng), BR-CRM-002 (business rule), MOD-CRM-001 (kind: transition), MOD-CRM-101 (kind: decision rule). Domain và loại model nằm ở metadata/title, không thay đoạn CRM trong ID. Các số là minh họa, không quy định dải số riêng theo domain.

Quy tắc giữ ID cũ áp dụng cho hồ sơ dự án đã tồn tại hoặc snapshot lịch sử, không dùng làm lý do giữ mẫu hướng dẫn sai quy ước. Nếu gặp `TR-`, `DAT-`, `PM-`, `DR-`, `SCN-` trong nguồn cũ: khai báo kind tương ứng transition, data, permission, decision rule, scenario; không hiểu PM là Project Manager hay TR là Transition requirement. Không đổi ID dự án thật chỉ để khớp ví dụ mới; duy trì mapping khi cần chuyển đổi có kiểm soát.

## Record và quan hệ tối thiểu

Meeting/Decision/Assumption/Constraint mới dùng [schema-2 knowledge records](knowledge-records-and-evidence.md). Giữ source locators cũ; register không tạo duplicate definitions. Thư mục dùng [layout policy](artifact-layout-and-migration.md), ID không đổi theo thứ tự folder hoặc parent.

Mỗi requirement: ID/title, type, statement hoặc canonical ref, source/rationale, authority, applies_to, version/decision state, verification method và allocation refs. Mỗi model item: ID/kind/definition + parent model revision + source requirement/rule. Mỗi allocation: source ID/revision → target ID/revision + nghĩa quan hệ (refines/implements/verifies/applies-to) và selected scope.

Kiểm từ nguồn đến giao hàng: need/decision → REQ/BR → model → Story/AC → planned test condition → TC → RUN/build/evidence. Quan hệ nhiều-nhiều được giữ; không ép một AC cho mỗi ô model và không coi requirement là ticket. Trước code chưa có RUN thì ghi chưa đến giai đoạn, không bịa run.

## Các phép kiểm bắt buộc

1. Tìm trùng ID trong namespace; mở từng ref và kiểm kind/version đúng. URL tồn tại nhưng sai revision vẫn không đạt.
2. Đi ngược tới source/authority và đi xuôi tới allocation/verification phù hợp giai đoạn. Gap phải có owner và gate impact.
3. Với shared requirement, kiểm các Story cùng dùng canonical ref, không mỗi nơi một bản sửa độc lập.
4. Khi split/merge requirement, tạo ID mới cho nghĩa mới, giữ old ID với quan hệ supersedes/split-into và decision; cập nhật impact/links. Không tái sử dụng ID đã bỏ.
5. Đổi cách phân bổ Epic/Story không tự đổi ID requirement. Thay nghĩa phải có revision/decision và review ảnh hưởng; không silently reclassify để né kiểm.
6. Người nhận thử impact query: đổi một BR thì tìm được models/Stories/tests cần xem lại. Không tìm được thì Q05 chưa đạt.

**Đạt:** định danh/meaning/source/version và trace phù hợp bước đều resolve, không duplicate hoặc orphan chặn. **Chưa kiểm:** thiếu register/source. **Không đạt:** xung đột kind/ID, stale pin hoặc mất allocation. BA quản lý register; authority quyết nghĩa; TL/QA kiểm allocation/verification; PM chốt scope.

Liên quan: [Q05](checks/traceability-and-versioning.md), [phân rã](backlog-hierarchy-and-decomposition.md), [nguồn](standards-and-crm-tailoring.md). Cấu trúc ID trên là quy ước CRM, không phải chuẩn bắt buộc của IREB hay Jira.

## Allocation Tooling — 1.5

`kit.py next-id` gợi ý ID từ tất cả workstreams và reservation ledger; chỉ --reserve --owner --apply mới giữ số trong checkout hiện tại. Local lock không giải quyết cấp số giữa các clone; cần reconcile/central allocator trước merge. Lint phân biệt definition với reference bằng [artifact metadata](artifact-metadata-and-lint.md), đồng thời audit các heading/property/ID columns rõ ràng của legacy. Q-CRM-NNN có thể dùng cho câu hỏi project binding đã chọn, khác Q01 check IDs. Không đổi ID nguồn hoặc cấp lại số đã bỏ.
