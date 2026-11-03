# Mẫu hồ sơ Epic

Mã tài liệu: **TPL-EPIC-SPECIFICATION-TEMPLATE** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Sao chép phần mẫu để tạo hồ sơ thực tế; không để trống rồi đánh dấu đạt.

**Đọc khi:** Sau khi đọc catalog và các hướng dẫn áp dụng.


<a id="spec-10"></a>

## Mẫu cấu trúc hồ sơ để sử dụng


<a id="spec-10-1"></a>

### Epic specification

```text
Epic ID / Jira key / Feature ref / revision
E01 Context, goal, scope và Epic acceptance
E02 Actors, glossary, entities và invariants
E03 Business flows/use cases với IDs, main/alternate/exception
E04 Lifecycle: state definitions + transition/command disposition
E05 BR catalogue + decision rules/table
E06 Data dictionary, validation, normalization và boundaries
E07 Permission/data-scope matrix
E08 UI/UX refs và states liên quan, hoặc N/A có lý do
E09 API/integration/sequence refs, hoặc N/A có lý do
E10 Exception/edge catalogue và expected outcomes
E11 NFR/control và acceptance methods, hoặc N/A có lý do
E12 Migration/operations impact, hoặc N/A có lý do
E13 Solution/dependency/feasibility
E14 Epic AC, planned coverage và test approach
E15 Story candidates, allocation, dependencies và estimate
E16 Questions/decisions/applicability/review + baseline manifest
```


## Applicability và review record của hồ sơ

Đọc [Catalog Epic](../../references/epic-specification-catalog.md). Giữ các ID E01–E16; nội dung có thể là delta hoặc ref pinned, không buộc mỗi mục một file. Không điền giả định như quyết định đã xác nhận.

| Item ID + tên | Applicability/reason | Output ref + revision | Source/authority | Owner/reviewer | Verdict/evidence | Gap/owner/due |
|---|---|---|---|---|---|---|
| Hạng mục được xét | Áp dụng hoặc N/A có xác nhận | Nội dung cụ thể | Nguồn quyết định | Người chịu trách nhiệm | Chưa kiểm / Không đạt / Đạt / N/A | Phần cần xử lý |

### Context và phạm vi bàn giao

Target/logical ID/Jira key; Feature/Epic refs; selected scope/in-out; baseline ID + repo/commit/paths; áp dụng model/BR/AC IDs; delta so với parent; constraints/dependencies; nguồn/authority; chuyên môn review; PM decision đúng revision; version sau merge.

### Questions và decisions

| ID | Vấn đề/nguồn | Lựa chọn/tác động | Authority | Có chặn scope nào? | Owner/due | Decision/ref/revision |
|---|---|---|---|---|---|---|
| Câu hỏi thực tế | Điều chưa biết | Không tự chọn policy | Người được quyết | Phần bị ảnh hưởng | Người theo dõi | Pending cho tới khi có quyết định |

### Acceptance và verification

Dùng [mẫu AC và coverage](../../references/coverage-inventories-and-traceability.md#spec-7-1). Mỗi AC có source/conditions/action/expected/observation. Planned test condition khác test đã chạy. Sau triển khai bổ sung build/config/run/verdict, không ghi Pass trước evidence.


### Story manifest và readiness của Epic

| Logical Story ID | Outcome / in-out scope | BR/model/AC allocation | Dependency/estimate | Owner dự kiến | Readiness/gap |
|---|---|---|---|---|---|
| Candidate thực tế | Hành vi kiểm chứng được | ID/ref pinned | Điều kiện + effort cơ sở | Người được giao | Evidence hoặc missing input |

Mỗi nhóm requirement/solution/testability có owner, due, reviewed revision, blocker và evidence. Chọn phạm vi baseline, không gọi toàn Epic Done từ việc đủ điều kiện sinh Story.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../../references/requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../../references/standards-and-crm-tailoring.md).
