# Mẫu hồ sơ Story

Mã tài liệu: **TPL-STORY-SPECIFICATION-TEMPLATE** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Sao chép phần mẫu để tạo hồ sơ thực tế; không để trống rồi đánh dấu đạt.

**Đọc khi:** Sau khi đọc catalog và các hướng dẫn áp dụng.


<a id="spec-10-2"></a>

### Story specification

```text
S01 IDs + Epic/Feature + pinned baseline/selected scope
S02 Actor/outcome/in-scope/out-of-scope
S03 Trigger + preconditions + success/failure postconditions
S04 Selected flow steps + alternate/exception/delta
S05 Selected BR/transition/decision IDs hoặc N/A có lý do
S06 Data/permission subset và delta
S07 UI/API/contract/solution refs và implementation boundaries
S08 Selected edges/NFR/transition impacts hoặc N/A có lý do
S09 AC IDs + examples + expected observable outcomes
S10 Test conditions, data/environment và oracle/verification method
S11 Owners/reviewers/dependencies/estimate/capacity/questions
S12 DoD policy + approval/change refs
```

Không bắt mọi Story có file riêng: nội dung có thể là section trong Epic baseline và Jira Story trỏ đúng section/commit. Nếu dùng file riêng, phải giữ một nguồn nội dung chuẩn và link rõ, không duy trì hai bản spec khác nhau.


## Applicability và review record của hồ sơ

Đọc [Catalog Story](../../references/story-specification-catalog.md). Giữ các ID S01–S12; nội dung có thể là delta hoặc ref pinned, không buộc mỗi mục một file. Không điền giả định như quyết định đã xác nhận.

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


### Kế hoạch thực hiện

Lựa chọn: checklist trực tiếp hoặc Task liên kết; lý do; owner điều phối; các bước/output/reviewer; dependency/bàn giao; estimate/capacity. Không bắt Task khi Story đủ DoR.

### Kết luận nhận việc và đóng Story

DoR result + scope/revision + Dev/QA read-back + PM planning. Khi bàn giao QA: code/review/CI/build/env/smoke/evidence. Khi đóng: AC/coverage executed + defects/disposition + QA verdict + PM closure. Chưa có evidence thì để Chưa kiểm.


## Policy, ID và trạng thái từng hạng mục

Policy IDs/versions/effective scope; Pending policy + gate impact; source/requirement/model kind theo [ID guide](../../references/requirement-types-identifiers-and-traceability.md). Dùng [mapping](../../references/catalog-check-model-mapping.md) để chọn models/evidence.

Bổ sung work signal (Chưa làm/Đang làm/Chờ review/Đã xác nhận), due và blocker vào mỗi E/S item record; verdict và evidence vẫn ghi riêng. Tổng hợp bằng [mẫu báo cáo](progress-report-template.md); không lấy % item Đạt làm % sản phẩm hoàn thành.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../../references/requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../../references/standards-and-crm-tailoring.md).
