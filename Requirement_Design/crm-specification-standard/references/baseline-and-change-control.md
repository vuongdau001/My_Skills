# Baseline yêu cầu, solution và kiểm soát thay đổi

Mã tài liệu: **CRM-BASELINE** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Định danh chính xác nội dung được duyệt và truyền xuống backlog.

**Đọc khi:** Chuẩn bị baseline, tạo Story hoặc thay đổi sau phê duyệt.


<a id="workflow-4"></a>

## Baseline của cái gì?


<a id="workflow-4-1"></a>

### Câu phải dùng trước khi tạo Story

> **Trước khi tạo Story thực thi, phải merge vào Git bộ hồ sơ YÊU CẦU VÀ SOLUTION đã được duyệt của phần phạm vi được chọn trong Epic, kèm kế hoạch phân rã Story được PM chốt.**
>
> Bộ hồ sơ đó gồm mục tiêu/phạm vi, rule, AC, quyết định, solution/contract liên quan, cách kiểm chứng, dependency và manifest Story. Sau merge, bộ hồ sơ tại commit xác định là **baseline đầu vào để tạo Story, development và testing** cho đúng phần phạm vi đó.

Đây không phải baseline của code, không phải chỉ một bản mô tả ticket và không có nghĩa toàn Feature đã phân tích xong.


<a id="workflow-4-2"></a>

### Phân biệt ba tập nội dung được chốt ở ba thời điểm

| Tập nội dung | Đối tượng được chốt | Dùng để làm gì? | Thời điểm |
|---|---|---|---|
| Khung phạm vi Feature / kế hoạch làm rõ | Mục tiêu, ranh giới sơ bộ, Epic dự kiến, owner, authority và kế hoạch làm rõ | PM cho phép tạo Epic và phân công BA/Dev/QA làm rõ các hạng mục | Trước khi bắt đầu làm rõ Epic; chưa đủ để code |
| **Baseline yêu cầu + solution của phạm vi Epic được chọn** | Nội dung chi tiết nêu tại mục [Bộ hồ sơ phải review và merge trước khi tạo Story](baseline-and-change-control.md#workflow-5) và manifest Story | Cho phép tạo Story; cung cấp đầu vào chuẩn cho Dev/QA/AI | Sau review chuyên môn, PM chốt và PR merge |
| Cấu hình/bản bàn giao triển khai | Code, test, config, migration, artifact/build và release manifest | Chứng minh bản được kiểm thử và bàn giao thực tế | Sau triển khai; không thay thế baseline yêu cầu + solution |

Ví dụ: đã chốt khung “Tiếp nhận khách hàng” thì có thể tạo Epic và giao BA/Dev làm rõ. Các hoạt động này có owner, hạn, capacity và đầu ra ngay trên Epic, không cần Story hoặc Task phân tích có trước. Tuy nhiên, chưa có baseline yêu cầu + solution thì chưa được sinh Story thực thi cho phần đó.


<a id="workflow-4-3"></a>

### Phạm vi của một baseline

Mỗi baseline đầu vào triển khai phải ghi rõ:

1. Feature ID và Epic liên quan.
2. Phần scope được chọn; phần ngoài phạm vi hoặc còn làm rõ.
3. Danh sách BR-ID, AC-ID và các requirement/NFR dùng chung được áp dụng.
4. Tài liệu solution/contract/UI/data được sử dụng và phiên bản tương ứng.
5. Các quyết định nghiệp vụ/kỹ thuật làm cơ sở.
6. Manifest Story được phép tạo.
7. Review/approval refs đúng phiên bản; PR và Git commit sau merge.

Một baseline có thể chỉ khóa phần độc lập của Epic. Các rule dùng chung mà phần đó phụ thuộc vẫn phải rõ. Không được “bỏ câu hỏi ra ngoài scope” nếu câu trả lời có thể làm thay đổi phần định triển khai.


<a id="workflow-5"></a>

## Bộ hồ sơ phải review và merge trước khi tạo Story

| Hạng mục trong bộ hồ sơ | Nội dung tối thiểu | Người chuẩn bị / xác nhận |
|---|---|---|
| 1. Định danh và nguồn | Feature/Epic, nguồn nhu cầu, Business authority, owner và tài liệu liên quan | BA; PM/Business xác nhận phạm vi và quyền |
| 2. Mục tiêu và scope | Actor, outcome, trong/ngoài phạm vi; giới hạn phần được khóa | BA + Business |
| 3. Luồng nghiệp vụ | Luồng chính, ngoại lệ, trạng thái và tương tác liên quan | BA; Business chốt; Dev/QA phản biện |
| 4. Rule và dữ liệu | BR-ID, điều kiện, validation, quyền, định danh/chuẩn hóa, trạng thái và xử lý lỗi | BA + Business; Dev kiểm khả thi |
| 5. AC và ví dụ | AC-ID, đầu vào/điều kiện, kết quả mong đợi; happy/negative/boundary/permission theo rủi ro | BA + QA; Business xác nhận expected result |
| 6. NFR và chuyển đổi | Constraint, cách đo, migration/integration/security liên quan; ghi lý do nếu không áp dụng | Dev/TL/QA và đầu mối chuyên môn |
| 7. Quyết định/câu hỏi | Decision refs; câu hỏi chặn đã giải quyết; phần còn mở có owner/hạn và đánh giá tác động | BA giữ hồ sơ; đúng authority chốt |
| 8. Solution | Hiện trạng → delta; thành phần dùng lại/thay đổi; API/data contract, quyền, lỗi/cạnh tranh và rủi ro liên quan | Dev; TL/peer review theo tác động |
| 9. Cách kiểm chứng | Test approach/matrix sơ bộ, dữ liệu/môi trường cần, cách quan sát kết quả và liên kết AC | QA cùng Dev |
| 10. Dependency và điều kiện | Owner hai đầu, contract/version, lead time, việc nào phải sẵn trước code/test | Dev/TL/PM; bên phụ thuộc xác nhận |
| 11. Phân rã Story | Logical ID, outcome, selected BR/AC, scope, dependency, estimate và owner dự kiến | BA + Dev + QA; review INVEST; PM chốt |
| 12. Review và phê duyệt | Ai xác nhận phần nào, revision/digest nào, PR nào và PM decision | Người có thẩm quyền tương ứng |

Không yêu cầu mọi testcase/script chi tiết phải hoàn tất trước baseline. Phải có đủ AC, ví dụ và test approach để xác nhận yêu cầu kiểm chứng được. QA tiếp tục xây chi tiết trong implementation; nếu phát hiện cần đổi expected result thì quay lại quy trình thay đổi.

Tiêu chí nội dung và chất lượng cho từng hạng mục Epic/Story được quy định tại [Chuẩn đặc tả và review Epic/Story](epic-specification-catalog.md). Dùng tài liệu đó để xác định flow, state transition, dữ liệu, quyền, edge case và AC đã đủ rõ hay chưa; có đủ tiêu đề không tự chứng minh đủ nội dung.

[Quy trình review và các phép kiểm Q01–Q07](requirements-review-process-and-verdicts.md) cùng [inventory/coverage](coverage-inventories-and-traceability.md) quy định thao tác, evidence và điều kiện kết luận. PM chỉ chốt bàn giao khi các phép kiểm áp dụng có kết luận/evidence đúng revision, không còn gap/câu hỏi chặn; không dùng nhận xét “đã đủ scope” mà thiếu bảng đối chiếu và source/authority review.


<a id="workflow-5-1"></a>

### Cấu trúc lưu trữ đề xuất

Các đường dẫn dưới đây là cấu trúc đề xuất cho repo dự án, chưa khẳng định đã có repo hoặc các file đó:

```text
docs/
  features/
    FEAT-CRM-001.md                 # Scope Feature, rule chung, Epic refs
  epics/
    EPIC-CRM-001.md              # Yêu cầu + solution + AC của phần manual
  baselines/
    BASE-CRM-001.yaml        # Selected scope, artifact refs, Story manifest
  shared/
    customer-data-contract.md      # Nếu có contract dùng chung cần tách riêng
```

Có thể gộp yêu cầu, solution và manifest thành các section trong một file Epic khi nhỏ. Điều bắt buộc là **xác định được chính xác tập nội dung/phiên bản được duyệt**, không phải tạo thật nhiều file.


<a id="workflow-5-2"></a>

### Ví dụ manifest trước khi tạo Story

```yaml
# Ví dụ minh họa, không phải dữ liệu Jira thực tế.
baseline_id: BASE-CRM-001
feature_id: FEAT-CRM-001
epic_ref: <Jira Epic key đã tồn tại>
scope:
  included: Tạo khách hàng thủ công theo các rule được chọn
  excluded: Import khách hàng
artifact_refs:
  - docs/features/FEAT-CRM-001.md
  - docs/epics/EPIC-CRM-001.md
selected_rules: [BR-CRM-001, BR-CRM-002]
selected_acceptance: [AC-CRM-001, AC-CRM-002, AC-CRM-003]
stories:
  - logical_id: STORY-CRM-001
    outcome: AM tạo hồ sơ hợp lệ, có kiểm quyền và xử lý trùng
    rules: [BR-CRM-001, BR-CRM-002]
    acceptance: [AC-CRM-001, AC-CRM-002, AC-CRM-003]
    solution_ref: docs/epics/EPIC-CRM-001.md#solution
    dependencies: []  # Chỉ rỗng sau khi đã đánh giá
```

- Logical ID có trước khi tạo ticket; Jira issue key có sau khi API/người thực hiện tạo ticket thành công.
- Không buộc manifest phải có Jira key của Story chưa được tạo.
- Approval lấy từ hồ sơ xác thực của PR/review system; một cờ `approved: true` do AI tự ghi không chứng minh đã được duyệt.
- Git commit sau merge được ghi vào receipt/ticket bàn giao. Không bắt file tự chứa SHA của chính commit đang tạo ra nó.


<a id="workflow-6"></a>

## Quy trình từ Feature đến Story thực thi

| Bước | Công việc và đầu ra | Người thực hiện / chốt | Trạng thái Jira liên quan |
|---|---|---|---|
| 1. Chốt khung Feature | Ghi mục tiêu, scope sơ bộ, nguồn, Epic dự kiến, owner, authority và kế hoạch làm rõ | BA chuẩn bị; Business xác nhận hướng nghiệp vụ; PM chốt phân rã ban đầu | Có thể tạo Epic `todo` sau khi được phép |
| 2. Giao việc làm rõ Epic | Ghi owner, hạn, capacity, reviewer và output của requirement, solution, testability trong bảng readiness trên Epic | PM phân công; BA/Dev/QA nhận việc | Epic `inprogress` khi bắt đầu; không tạo Task phân tích mặc định |
| 3. Làm rõ requirement | Luồng, rule, AC, dữ liệu, quyền, câu hỏi và quyết định trên Jira | BA chủ trì; Business quyết; Dev/QA góp ý | Cập nhật readiness/evidence của hạng mục requirement trên Epic |
| 4. Phân tích solution | Đối chiếu code/DB, chốt thiết kế, contract, dependency, rủi ro và estimate | Dev; TL/peer và QA review | Cập nhật readiness/evidence của hạng mục solution trên Epic |
| 5. Review testability và chia Story | Xác nhận expected result/cách kiểm chứng; nháp Story theo outcome; review INVEST | BA + Dev + QA | Chưa tạo Story thực thi; dùng section/manifest nháp trên hồ sơ Epic |
| 6. Chuẩn bị PR baseline | Tổng hợp đủ các hạng mục tại mục [Bộ hồ sơ phải review và merge trước khi tạo Story](baseline-and-change-control.md#workflow-5) vào tài liệu Git/PR | BA điều phối; Dev/QA bổ sung phần chuyên môn | Các hạng mục được reviewer xác nhận; Epic vẫn `inprogress` |
| 7. PM chốt và merge | Review chuyên môn đúng revision, PM duyệt phạm vi và manifest; merge PR hợp lệ | Business/BA/Dev/QA xác nhận theo nội dung; PM chốt; người/service có quyền merge | Epic vẫn `inprogress`; chưa phải Epic Done |
| 8. Tạo Story | Đọc manifest từ commit đã merge, tạo đúng child, ghi baseline refs và đối soát kết quả | Người/service được giao; PM kiểm bàn giao | Story được tạo ở `todo` |
| 9. Kiểm DoR Story | Xác nhận đầu vào còn hiệu lực, dữ liệu/dependency/môi trường, owner và capacity | Dev + QA xác nhận; PM chốt kế hoạch | `todo` chưa Ready hoặc `todo` đạt DoR; chỉ triển khai khi đạt |
| 10. Dev, QA và đóng Story | Code/review/CI → deploy/smoke → QA → PM chốt output theo DoD | Dev, reviewer, QA, người deploy và PM | `inprogress` → `resolved` → `done` |
| 11. Nghiệm thu Epic/Feature | Đối chiếu toàn scope và các luồng liên Story/Epic; cập nhật tài liệu và acceptance record | Business nghiệm thu; BA/QA cung cấp hồ sơ; PM chốt roll-up | Epic `done` khi đạt DoD Epic; Feature nghiệm thu trong hồ sơ tài liệu |

Một bàn giao có sender/receiver, input links, revision, output mong đợi và hạn. Người nhận xác nhận nhận việc hoặc trả thiếu có lý do; im lặng không phải approval.


<a id="workflow-14"></a>

## Thay đổi sau baseline

1. Ghi đề nghị/câu hỏi trên Jira, chỉ rõ baseline, scope và lý do.
2. BA/Dev/QA xác định tác động tới rule, AC, solution, Story/Task, test, effort/lịch và acceptance.
3. PM chỉ rõ phần phải dừng; Story/Task bị chặn dùng `pending`, Epic vẫn `inprogress` với blocker nếu chưa hoàn thành.
4. Business/technical authority quyết nội dung; PM/Sponsor quyết scope/nguồn lực theo quyền.
5. Sửa bộ hồ sơ trong PR mới, review lại phần bị ảnh hưởng và merge baseline mới.
6. Cập nhật pin của các Story bị ảnh hưởng sau phê duyệt; chạy lại gate/test cần thiết rồi resume.

Story pin commit và phạm vi cụ thể. Không tự đổi toàn bộ Story sang “commit mới nhất” khi chỉ phần khác của Epic thay đổi. Phần không ảnh hưởng giữ pin cũ khi có đánh giá tác động được xác nhận.

Acceptance/evidence cũ vẫn là lịch sử cho version cũ; không tự chứng minh scope/build mới đạt. Khi Staging đổi build/config/data trong lúc QA/demo, người deploy phải báo và đánh giá lại phần evidence bị ảnh hưởng.


## Policy/ID và Feature scope trong baseline

Manifest phải dẫn Feature scope/allocation và requirement/model IDs theo [ID/trace](requirement-types-identifiers-and-traceability.md), cùng các [policy versions](project-policy-register.md) áp dụng cho gate/acceptance. Không ghi approval cho policy còn Pending. Thay policy/Feature allocation cần impact analysis như thay rule; baseline từng phần phải truy được scope unit/outcome, không tự báo toàn Feature đã chốt.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
