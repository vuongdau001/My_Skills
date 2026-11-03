# Inventory, coverage, AC và truy vết

Mã tài liệu: **CRM-COVERAGE** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Xác định mẫu số của việc kiểm đủ và tách planned/executed coverage.

**Đọc khi:** Chuẩn bị review completeness, acceptance hoặc impact analysis.


<a id="spec-6"></a>

## Chọn model và lập inventory

**Đầu vào:** selected scope, sources/actors, model/contract revisions, applicability của catalog. **Output:** inventory/disposition, planned verification mapping, gaps và review result. BA/Dev chuẩn bị; QA tìm counterexample; authority xác nhận phần loại trừ.

| Model/hồ sơ | Phép kiểm chi tiết |
|---|---|
| D01 — Flow nghiệp vụ, use case và swimlane | [Inventory, bước kiểm và điều kiện dừng](models/business-flows-and-use-cases.md) |
| D02 — Vòng đời và chuyển trạng thái nghiệp vụ | [Inventory, bước kiểm và điều kiện dừng](models/business-state-transitions.md) |
| D03 — Business rules và bảng quyết định | [Inventory, bước kiểm và điều kiện dừng](models/business-rules-and-decision-tables.md) |
| D04 — Từ điển dữ liệu và validation | [Inventory, bước kiểm và điều kiện dừng](models/data-dictionary-and-validation.md) |
| D05 — Quyền và phạm vi truy cập dữ liệu | [Inventory, bước kiểm và điều kiện dừng](models/permissions-and-data-access.md) |
| D06 — Hành vi UI và trạng thái tương tác | [Inventory, bước kiểm và điều kiện dừng](models/ui-behavior-and-interaction-states.md) |
| D07 — Contract API và tích hợp | [Inventory, bước kiểm và điều kiện dừng](models/api-and-integration-contracts.md) |
| D08 — Ngoại lệ và edge cases | [Inventory, bước kiểm và điều kiện dừng](models/exceptions-and-edge-cases.md) |
| D09 — NFR, migration và vận hành | [Inventory, bước kiểm và điều kiện dừng](models/nonfunctional-migration-and-operations.md) |
| D10 — Solution, phân rã Story và testability | [Inventory, bước kiểm và điều kiện dừng](models/solution-and-story-decomposition.md) |

Một nhóm không áp dụng phải có lý do và reviewer. Chưa biết không phải N/A. Số item có disposition chỉ là coverage trên inventory được xác nhận, không là chứng minh mọi tình huống thực tế. Inventory model và điều kiện dừng được duy trì tại từng file model, tránh hai bảng tiêu chí độc lập.


<a id="spec-3-11"></a>

### Xác định mẫu số trước khi kết luận

Owner lập inventory cụ thể cho target, theo hướng dẫn model ở bảng trên. Chi tiết inventory, thao tác reviewer và điều kiện dừng được duy trì tại từng model để chỉ có một nguồn chuẩn. Dùng [mapping hạng mục → model/evidence](catalog-check-model-mapping.md) để chọn tuyến, rồi áp dụng các check Q01–Q07.

**Mẫu số không phải số dòng trong template.** Tập state/command phải được xác nhận từ nguồn/stakeholder; bảng 100% ô hiện có không chứng minh đầy đủ nếu một command nghiệp vụ chưa được phát hiện. Unknown không được loại khỏi mẫu số mà không báo rõ. Evidence từng item và review đúng scope/revision là điều kiện kết luận.

<a id="spec-7"></a>

## AC, scenario và kiểm tra coverage trước khi bàn giao


<a id="spec-7-1"></a>

### Mẫu AC có thể kiểm chứng

```text
AC-ID:
Source: BR / flow step / transition / decision rule / NFR IDs
Precondition: actor, resource, state/version, dữ liệu và điều kiện môi trường
Action: command/event cụ thể qua kênh nào
Expected:
  - Response / UI / observable result
  - State và dữ liệu thay đổi hoặc không thay đổi
  - Side effects/audit/notification nếu có
  - Behavior khi lỗi, lặp hoặc bị từ chối nếu thuộc AC
Verification: API/UI/data/event/log hoặc phương pháp phù hợp
```

Given/When/Then có thể dùng để diễn đạt; không bắt mọi tổ hợp thành Gherkin dài nếu bảng quyết định rõ hơn. Một AC có thể cần nhiều testcase. Testcase triển khai chi tiết phải giữ trace và expected result, không tạo rule mới.


<a id="spec-7-2"></a>

### Chuỗi truy vết và bảng coverage

```text
Nhu cầu/Feature
  → Epic scope + BR + flow/state/decision/data/permission/NFR
  → Story selected scope + AC
  → Test condition / scenario dự kiến
  → Testcase/script
  → Test run + build + evidence + verdict
```

Đây là các liên kết của cùng công việc, không phải hai bộ requirement độc lập. Story dùng AC của mình để cụ thể hóa phần được chọn từ Epic; Task là cách tổ chức thực hiện, không là nguồn rule mới.

| Model / rule item | Outcome cần kiểm | Story / AC | Test condition dự kiến | Gap / quyết định |
|---|---|---|---|---|
| MOD-CRM-001 submit hợp lệ | Đổi state và ghi đúng một logical operation | Story… / AC… | Test condition ref cần điền | … |
| MOD-CRM-201 (kind: permission) — deny wrong owner | Không đổi state/data; response đúng | Story… / AC… | Test condition ref cần điền | … |
| MOD-CRM-202 (kind: data constraint) — maximum length | Biên hợp lệ và vượt biên | Story… / AC… | Test condition ref cần điền | … |

Trước baseline chỉ có thể xác nhận **planned coverage**, chưa được ghi test đã pass. Khi code/test chạy mới có executed coverage và evidence.


<a id="spec-7-3"></a>

### Kiểm theo từng loại coverage

| Đối tượng | Đơn vị cần kiểm/đếm trong scope | Cách xác nhận đủ để bàn giao |
|---|---|---|
| Flow | Main/alternate/exception path đã xác định | Mỗi đường quan trọng có kết quả và scenario; loop/timeouts có giới hạn/termination được quyết |
| Business state | State, valid transition, denied/guard-fail command và chuỗi rủi ro | Liệt kê tách các tập này; không gọi “đi qua đủ state” là đã xét đủ transition |
| Decision | Các rule/tổ hợp khả thi sau gộp có lý do | Mỗi expected action có case; tổ hợp loại trừ có constraint; overlap/default đã giải quyết |
| Data | Equivalence groups và boundary áp dụng | Có valid/invalid/biên; các tổ hợp cross-field quan trọng không bị bỏ qua |
| Permission | Các nhóm actor/action/resource/condition trong scope | Cả allow/deny, khác owner/state/tenant nếu có |
| NFR/integration | Các control/failure/performance condition liên quan | Có acceptance method, environment/data và authority; chưa có số đo thì chưa tuyên bố đã đạt |
| Requirement/AC | BR/AC được chọn | Không có rule áp dụng mà không biết Story/verification nào thực hiện; không có AC không truy được nhu cầu hoặc quyết định |

QA đề xuất scope/độ sâu kiểm theo risk; Business/TL xác nhận phần nghiệp vụ/kỹ thuật; PM kiểm residual risk và thiếu sót trước chốt. Không yêu cầu mọi đường đi vô hạn hay mọi tổ hợp toàn hệ thống đều được liệt kê. Mọi giảm phạm vi kiểm có lý do và authority, không được dùng để bỏ rule bắt buộc.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
