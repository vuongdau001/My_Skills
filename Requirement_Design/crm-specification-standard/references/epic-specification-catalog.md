# Danh mục nội dung và tiêu chí đặc tả Epic

Mã tài liệu: **CRM-EPIC** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Giữ E01–E16 và dẫn tới phương pháp kiểm chi tiết.

**Đọc khi:** Soạn/review phạm vi Epic được chọn trước phân rã Story.


<a id="spec-4"></a>

## Epic cần làm rõ những hạng mục nào?

**B = phải có nội dung cốt lõi. C = có điều kiện; phải quyết applicability.** Không có nghĩa bắt buộc tạo một file cho mỗi dòng.

| ID | Hạng mục Epic | Output tối thiểu | Tiêu chí đủ để review | Owner / reviewer chính |
|---|---|---|---|---|
| <a id="e01"></a>E01 — B | Mục tiêu, boundary và phạm vi | Một actor goal ở cấp user-goal, nguồn, boundary, hành vi đầy đủ và scope đợt | Outcome có ý nghĩa, các mục tiêu lân cận được phân biệt, in/out và acceptance rõ | BA / Business + PM |
| <a id="e02"></a>E02 — B | Actor, stakeholder và đối tượng | Actor chính/hỗ trợ, stakeholder, quyền lợi, glossary và ownership | Actor/boundary và quyền lợi kiểm được với nguồn, entity và permission matrix | BA / Business + Dev |
| <a id="e03"></a>E03 — B | Một Use Case cấp user-goal | MOD ID, locator, trigger, preconditions, luồng chính, nhánh, kết quả và bảo đảm tối thiểu | Lần theo mọi đường áp dụng tới kết quả quan sát được. Pin models áp dụng. Dùng [D01](models/business-flows-and-use-cases.md) | BA / Business + Dev/QA |
| <a id="e04"></a>E04 — C | Business state/lifecycle | State definitions, transition/command matrix, guards và forbidden behavior | Đủ trạng thái/sự kiện trong scope; biết valid, denied/no-op và side effects; xem [D02 — Vòng đời và chuyển trạng thái nghiệp vụ](models/business-state-transitions.md) | BA + Dev / Business + QA |
| <a id="e05"></a>E05 — B | Rule và tổ hợp quyết định | BR IDs; decision table khi nhiều điều kiện ảnh hưởng kết quả | Có priority/default; không chồng lấn mâu thuẫn hoặc bỏ sót tổ hợp khả thi; xem [D03 — Business rules và bảng quyết định](models/business-rules-and-decision-tables.md) | BA / Business + Dev/QA |
| <a id="e06"></a>E06 — B | Data và validation | Từ điển dữ liệu của đối tượng/delta; source, validation, relationships | Chốt bắt buộc, format, normalization, uniqueness và boundary liên quan; xem [D04 — Từ điển dữ liệu và validation](models/data-dictionary-and-validation.md) | BA + Dev / Business + QA |
| <a id="e07"></a>E07 — B | Quyền và phạm vi dữ liệu | Actor/action/resource/condition matrix; quyền xem/sửa trường nếu có | Biết ai được/không được làm gì trên dữ liệu nào, kiểm tại server; xem [D05 — Quyền và phạm vi truy cập dữ liệu](models/permissions-and-data-access.md) | BA + Dev / Business + security/QA |
| <a id="e08"></a>E08 — C | UI và trải nghiệm | Flow màn hình, Prototype/walkthrough theo scope và bước/scenario E03, input/output/error/empty/loading states | UI phản ánh đúng rule, contract và quyền. Áp dụng [gate Prototype](prototype-workflow-and-epic-gate.md) và [D06 — Hành vi UI và trạng thái tương tác](models/ui-behavior-and-interaction-states.md) | BA/UX / Business + Dev/QA |
| <a id="e09"></a>E09 — C | Integration và contract | Interfaces gắn bước/scenario E03, ownership hai đầu, schema/version/error/retry refs | Chốt failure/timeout/duplicate/order và boundary giao tiếp; xem [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md) | Dev/TL / counterpart + QA |
| <a id="e10"></a>E10 — B | Ngoại lệ và edge cases | Catalogue theo rủi ro, trace case → nhánh/kết quả E03, N/A có lý do | Không chỉ liệt kê tên lỗi; tác động dữ liệu/state/side effect và recovery rõ; xem [D08 — Ngoại lệ và edge cases](models/exceptions-and-edge-cases.md) | QA + BA/Dev / authority tương ứng |
| <a id="e11"></a>E11 — C | NFR/control | Metric, ngưỡng, workload/environment, cách đo; constraint bắt buộc | Có thể kiểm chứng; không dùng ngưỡng tự chọn chưa được duyệt; xem [D09 — NFR, migration và vận hành](models/nonfunctional-migration-and-operations.md) | BA + TL/QA / Business + control owner |
| <a id="e12"></a>E12 — C | Migration/vận hành | Mapping, reconcile, cutover/restore/rollback và support impact | Có data authority, tolerance và tiêu chí chuyển giao liên quan; xem [D09 — NFR, migration và vận hành](models/nonfunctional-migration-and-operations.md) | Migration/Release / Data Steward + Ops/QA |
| <a id="e13"></a>E13 — B | Solution và dependency | Hiện trạng→delta, design/contract refs, assumptions/risk và owner/commitment | Khả thi cho scope chọn; không để dependency chưa xác nhận thành “Ready”; xem [D10 — Solution, phân rã Story và testability](models/solution-and-story-decomposition.md) | Dev / TL/peer + QA |
| <a id="e14"></a>E14 — B | AC, coverage và test approach | Scenario/kết quả E03 → AC → test conditions/evidence | Kiểm outcome tích hợp, nhánh và các controls. Phân biệt planned coverage với kết quả chạy | BA + QA / Business + Dev |
| <a id="e15"></a>E15 — B | Phương án Story | MOD ID/revision, scenario/bước hoặc delta, outcome, dependency và phần còn lại | Các lát giữ controls, không bỏ sót hoặc đếm lặp. Có phép kiểm outcome tích hợp và review INVEST | BA + Dev + QA / PM |
| <a id="e16"></a>E16 — B | Policy, decision, review và baseline | Policy use-case-v1, selected scope/revision/baseline, evidence nghiệm thu trước và open decisions | Evidence pin đúng scope; lịch sử và delta truy được; authority xác nhận phần áp dụng trước handoff | BA điều phối / chuyên môn + PM |

Ví dụ E04 có thể N/A cho sửa copy thuần túy, nhưng không được N/A cho luồng duyệt vì chưa nghĩ ra vòng đời. E08 có thể N/A cho backend-only nếu đã xác nhận không có UI delta. E11/E12 vẫn phải rà tác động, không mặc định bỏ qua vì tên Epic không nói đến NFR/migration.


E01/E15 áp dụng [checkpoint chọn cấp và quan hệ cha–con](source-scope-and-decomposition-checkpoint.md#level-selection) khi tạo/đổi allocation: nêu parent, phạm vi model/acceptance chung và delta từng Story. Entry point, role hay màn hình riêng chưa đủ lý do tạo Epic.

## Dùng catalog để tạo Story

E01–E02 giữ mục tiêu/ranh giới; E03–E05 giữ hành vi dùng chung; E06–E09 dữ liệu/giao tiếp; E10–E12 ngoại lệ/vận hành; E13–E14 solution/kiểm chứng; E15–E16 phân rã/phê duyệt. Nội dung có thể kế thừa qua ref đúng phiên bản; không bắt 16 file riêng.

**Đầu vào:** Capability scope/source, shared models/constraints và selected scope. **Output:** hồ sơ Epic, applicability/coverage, review record và Story manifest. Owner/reviewer theo từng dòng catalog; PM chốt gói sau chuyên môn.

Áp dụng [Q01–Q07](requirements-review-process-and-verdicts.md), [inventory](coverage-inventories-and-traceability.md) và model liên quan để thực hiện tiêu chí, không tick bảng vì đã có tiêu đề. Chưa có input: Chưa kiểm; gap/contradiction: Không đạt; N/A cần reason/reviewer.

Có thể baseline phần độc lập của Epic; shared rule ảnh hưởng scope chọn phải rõ. Phần chưa làm có owner/hạn/impact, không giấu gap bằng cách ghi out-of-scope. Đạt cổng sinh Story không làm Epic Done. [Gate Epic](readiness-completion-and-approval-gates.md#workflow-8-2), [phân rã](backlog-hierarchy-and-decomposition.md), [mẫu Epic](../assets/templates/epic-specification-template.md).


## Định tuyến review và báo cáo

Dùng [mapping E01–E16/S01–S12 → model, evidence và reviewer](catalog-check-model-mapping.md). Từng hạng mục giữ work signal, applicability và verdict tách biệt theo [measurement](progress-measurement-and-capability-rollup.md). Policy/threshold ảnh hưởng kết luận phải dẫn [policy register](project-policy-register.md) đúng version; thiếu quyết định bắt buộc thì chưa qua gate. Capability cha dùng [C01–C08](capability-specification-catalog.md), không chép lại model Epic.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
