# Mapping Epic/Story với phép kiểm, mô hình và evidence

Mã tài liệu: **CRM-MAPPING** · Gói CRM 1.3.1 · 03/11/2026

**Đọc khi:** soạn/review một hạng mục Epic/Story hoặc định tuyến agent. **Đầu vào:** target, scope/revision, applicability và delta so với baseline. **Đầu ra:** danh sách model/check cần thực hiện, evidence và reviewer; không tự cấp verdict từ bảng mapping.

## Cách dùng

1. Chọn dòng E/S dưới đây. Model được liệt kê là tuyến bắt đầu; điều kiện ở cột trigger quyết phần áp dụng. Đọc cả model liên quan khi delta tạo tác động ngoài dòng đó.
2. Full review đánh giá **cả Q01–Q07** cho target: Q01 đúng nguồn/nhu cầu; Q02 đầy đủ; Q03 nhất quán; Q04 kiểm chứng; Q05 truy vết; Q06 rõ nghĩa; Q07 khả thi. Không dùng mapping để miễn một check. [Thao tác từng check](requirements-review-process-and-verdicts.md).
3. Mỗi dòng phải chứng minh: source/authority (Q01), inventory/disposition (Q02), đối chiếu cùng điều kiện (Q03), expected/observation (Q04), refs/version/impact (Q05), read-back/glossary (Q06), điều kiện thực hiện/kiểm chứng (Q07). Dùng output cụ thể của dòng làm input; không đòi bảy báo cáo lặp riêng nếu một record đủ evidence.
4. Review riêng ghi check/model và scope đã kiểm; các phần khác là chưa xét, không tự kết luận cả Story Đạt. N/A cần reason/reviewer, unknown không là N/A.
5. Dòng không cần model riêng vẫn phải kiểm source/AC/allocation/approval. Task dùng SMART/T01–T08, không tự ép đủ E/S/Q/D; Feature dùng F01–F08 và model theo scope.

## Mapping hạng mục sang model và evidence

| Hạng mục | Model cần xem | Điều kiện áp dụng | Evidence để reviewer kiểm | Owner / reviewer |
|---|---|---|---|---|
| E01 — Mục tiêu, nguồn, scope | Không bắt model riêng; dùng refs và inventory của target | Luôn xét nguồn/rationale/acceptance; thiếu authority chặn scope | Source + in/out + phương pháp acceptance | BA / Business + PM |
| E02 — Actor, thuật ngữ, đối tượng | [D04 — Từ điển dữ liệu và validation](models/data-dictionary-and-validation.md); [D05 — Quyền và phạm vi truy cập dữ liệu](models/permissions-and-data-access.md) | Có data/entity hoặc ownership; glossary luôn cần | Glossary + actor/entity refs, read-back | BA / Business + Dev |
| E03 — Flow/use case | [D01 — Flow nghiệp vụ, use case và swimlane](models/business-flows-and-use-cases.md); [D08 — Ngoại lệ và edge cases](models/exceptions-and-edge-cases.md) | Hành vi và nhánh lỗi; sơ đồ tùy độ phức tạp | Path inventory → postconditions/scenarios | BA / Business + Dev/QA |
| E04 — Vòng đời nghiệp vụ | [D02 — Vòng đời và chuyển trạng thái nghiệp vụ](models/business-state-transitions.md); [D05 — Quyền và phạm vi truy cập dữ liệu](models/permissions-and-data-access.md); [D08 — Ngoại lệ và edge cases](models/exceptions-and-edge-cases.md) | Action phụ thuộc state hoặc có lifecycle | State×command disposition + guard/effects | BA + Dev / Business + QA |
| E05 — Business rules | [D03 — Business rules và bảng quyết định](models/business-rules-and-decision-tables.md) | Rules luôn có nguồn; decision table khi nhiều điều kiện | Domains/rules/default/overlap + witness | BA / Business + Dev/QA |
| E06 — Dữ liệu/validation | [D04 — Từ điển dữ liệu và validation](models/data-dictionary-and-validation.md); [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md) | Data delta; D07 nếu truyền qua interface | Field/relationship/domain + boundary/outcomes | BA + Dev / Business + QA |
| E07 — Quyền/phạm vi dữ liệu | [D05 — Quyền và phạm vi truy cập dữ liệu](models/permissions-and-data-access.md); [D02 — Vòng đời và chuyển trạng thái nghiệp vụ](models/business-state-transitions.md); [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md) | D05 luôn xét quyền; D02 nếu phụ thuộc state; D07 nếu giao tiếp | Allow/deny partitions + source và enforcement refs | BA + Dev / Business/control + QA |
| E08 — UI/trải nghiệm | [D06 — Hành vi UI và trạng thái tương tác](models/ui-behavior-and-interaction-states.md); [D04 — Từ điển dữ liệu và validation](models/data-dictionary-and-validation.md); [D05 — Quyền và phạm vi truy cập dữ liệu](models/permissions-and-data-access.md); [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md) | Có UI delta; đối chiếu contract/data/quyền liên quan | UI state walkthrough + server outcomes | BA/UX / Business + Dev/QA |
| E09 — Integration/contract | [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md); [D08 — Ngoại lệ và edge cases](models/exceptions-and-edge-cases.md) | Có giao tiếp/sự kiện hệ thống; thứ tự/phục hồi liên quan | Success/failure/timeout/duplicate + commit boundary | Dev/TL / counterpart + QA |
| E10 — Ngoại lệ/edge cases | [D08 — Ngoại lệ và edge cases](models/exceptions-and-edge-cases.md) | Luôn rà các chiều; đọc thêm model phát sinh case | Case inventory + expected result/authority loại trừ | QA + BA/Dev / authority nội dung |
| E11 — NFR/control | [D09 — NFR, migration và vận hành](models/nonfunctional-migration-and-operations.md) | Đánh giá impact; model khi obligation áp dụng | Metric/control + method/threshold/workload | TL/QA + BA / Business/control |
| E12 — Migration/vận hành | [D09 — NFR, migration và vận hành](models/nonfunctional-migration-and-operations.md); [D04 — Từ điển dữ liệu và validation](models/data-dictionary-and-validation.md); [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md) | Có chuyển dữ liệu/vận hành; D04/D07 theo tác động | Mapping/reconcile/recovery + acceptance | Migration/Ops / Data authority + QA |
| E13 — Solution/dependency | [D10 — Solution, phân rã Story và testability](models/solution-and-story-decomposition.md); [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md) | Solution/feasibility; D07 nếu có contract | Delta/rationale + dependency commitment/reality check | Dev / TL + QA |
| E14 — AC/coverage | Không bắt model riêng; dùng refs và inventory của target | Mọi model áp dụng cần allocation verification | AC/source + inventory → planned test condition | BA + QA / Business + Dev |
| E15 — Phân rã Story | [D10 — Solution, phân rã Story và testability](models/solution-and-story-decomposition.md) | Phân bổ scope sang Story | Outcome/BR/AC allocation + INVEST/dependency | BA + Dev + QA / PM |
| E16 — Decision/review/baseline | Không bắt model riêng; dùng refs và inventory của target | Mọi scope bàn giao | Findings/approval đúng revision + manifest | BA điều phối / authority + PM |
| S01 — Định danh và baseline | Không bắt model riêng; dùng refs và inventory của target | Mọi Story; refs đúng subset/revision | Baseline receipt + ref/impact check | BA/Dev / PM |
| S02 — Outcome/scope | Không bắt model riêng; dùng refs và inventory của target | Mọi Story; value và ranh giới | Source/outcome + INVEST/scope allocation | BA / Business + Dev/QA |
| S03 — Trigger/pre-postconditions | [D01 — Flow nghiệp vụ, use case và swimlane](models/business-flows-and-use-cases.md); [D02 — Vòng đời và chuyển trạng thái nghiệp vụ](models/business-state-transitions.md); [D04 — Từ điển dữ liệu và validation](models/data-dictionary-and-validation.md); [D05 — Quyền và phạm vi truy cập dữ liệu](models/permissions-and-data-access.md) | D01 cho hành vi; state/data/quyền khi có điều kiện | Setup → event → success/failure result | BA + Dev / QA + Business |
| S04 — Flow subset/delta | [D01 — Flow nghiệp vụ, use case và swimlane](models/business-flows-and-use-cases.md); [D08 — Ngoại lệ và edge cases](models/exceptions-and-edge-cases.md) | Steps/nhánh thuộc scope Story | Pinned steps + alternate/exception outcomes | BA / Dev + QA |
| S05 — Rule/state/decision subset | [D03 — Business rules và bảng quyết định](models/business-rules-and-decision-tables.md); [D02 — Vòng đời và chuyển trạng thái nghiệp vụ](models/business-state-transitions.md) | BR áp dụng; D02 nếu có state-dependent behavior | BR/decision/transition refs + denied behavior | BA + Dev / Business + QA |
| S06 — Data/permission | [D04 — Từ điển dữ liệu và validation](models/data-dictionary-and-validation.md); [D05 — Quyền và phạm vi truy cập dữ liệu](models/permissions-and-data-access.md) | Data/quyền của hành vi; kế thừa có pin | Fields/domains/allow-deny + negative/boundary | BA + Dev / QA + authority |
| S07 — UI/API/solution | [D06 — Hành vi UI và trạng thái tương tác](models/ui-behavior-and-interaction-states.md); [D07 — Contract API và tích hợp](models/api-and-integration-contracts.md); [D10 — Solution, phân rã Story và testability](models/solution-and-story-decomposition.md) | Chọn theo UI/interface/delta thực tế | Contracts/errors/side effects + feasibility | Dev/UX / TL + QA |
| S08 — Edge/NFR/transition impact | [D08 — Ngoại lệ và edge cases](models/exceptions-and-edge-cases.md); [D09 — NFR, migration và vận hành](models/nonfunctional-migration-and-operations.md) | Rà mọi chiều; D09 khi control/transition áp dụng | Selected cases + NFR method/threshold | QA + Dev / Business/control |
| S09 — AC/examples | Không bắt model riêng; dùng refs và inventory của target | Mỗi AC gắn model/rule áp dụng | Setup/action/expected/observation + examples | BA + QA / Business |
| S10 — Verification approach | Không bắt model riêng; dùng refs và inventory của target | Mọi Story; đọc các model tạo test conditions | Risk-based conditions/data/env/oracle | QA / Dev + authority expected |
| S11 — Ownership/dependency/estimate | [D10 — Solution, phân rã Story và testability](models/solution-and-story-decomposition.md) | Điều kiện thực hiện, feasibility/capacity | Owners/commitments/estimate rationale | Dev + QA / TL + PM |
| S12 — Completion/approval/change | Không bắt model riêng; dùng refs và inventory của target | Policy/approval áp dụng cho Story | Policy versions + DoD/evidence plan + decision | BA/Dev/QA / PM |

## Ví dụ kiểm E07 — Quyền

Input: rule quyền, actor/resource/state, flow, server contract và AC cùng revision. D05 là model chính; thêm D02 nếu quyền thay đổi theo state, D07 khi có API.

- Q01: mở source và authority quyết quyền; AI suy ra quyền từ UI không đủ.
- Q02: liệt kê actor×action×resource/condition, có allow/deny và lý do nhóm/loại.
- Q03: đi cùng tình huống creator approve hồ sơ Pending qua flow/state/permission/contract/AC; mọi nơi phải cho kết quả tương thích.
- Q04: QA nêu setup sai role/sai owner/sai state và quan sát response, state/data/effects.
- Q05: pin policy/model refs và tìm mọi Story/test bị ảnh hưởng khi đổi rule.
- Q06: xác định “của mình” là creator hay current owner; Dev/QA read-back cùng nghĩa.
- Q07: xác minh cách enforce/observe khả thi; quyền/test data cần thiết có kế hoạch phù hợp gate.

Evidence có source, inventory, comparison, verification sketch, refs, read-back và feasibility; cùng một record có thể phục vụ nhiều check. Mọi finding chặn được giải quyết trước gate. Dùng [mẫu review](../assets/templates/requirements-review-record-template.md).
