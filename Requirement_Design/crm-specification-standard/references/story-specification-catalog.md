# Danh mục nội dung và tiêu chí đặc tả Story

Mã tài liệu: **CRM-STORY** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Giữ S01–S12; Story đủ bắt đầu triển khai thông qua nội dung và refs.

**Đọc khi:** Soạn/review Story, không viết lại hồ sơ Epic.


<a id="spec-5"></a>

## Story cần đầy đủ những hạng mục nào?

Story có mức chi tiết đủ để Dev/QA triển khai, không phải SRS viết lại toàn Epic. Mỗi phần có thể ghi **delta cụ thể** hoặc **link tới section/model đã baseline**.

| ID | Hạng mục Story | Nội dung cần có | Tiêu chí review |
|---|---|---|---|
| <a id="s01"></a>S01 | Định danh và baseline | Feature/Epic, logical/Jira ID, baseline commit + selected scope | Không trỏ “latest”; xác định chính xác phần được phép làm |
| <a id="s02"></a>S02 | Outcome và scope | Actor, mục tiêu, giá trị, trong/ngoài scope | Một phần hành vi kiểm chứng được; không chỉ là tên màn hình/API |
| <a id="s03"></a>S03 | Trigger và pre/postconditions | Điều kiện bắt đầu, sự kiện/kênh gọi, kết quả sau thành công/thất bại | Test có thể setup dữ liệu/state và biết kết quả cần kiểm |
| <a id="s04"></a>S04 | Flow được chọn | Step IDs từ Epic, alternate/exception trong scope và delta | Không phải suy đoán bước giữa; nhánh kết thúc/phản hồi rõ |
| <a id="s05"></a>S05 | Rule/state/decision subset | BR IDs, transition/decision rule IDs, expected illegal/denied behavior | Quy tắc chung đủ rõ, không tạo biến thể mâu thuẫn Epic; N/A có lý do |
| <a id="s06"></a>S06 | Data và quyền | Fields/schema/normalization/validation, actor-resource constraints liên quan | Biết positive/negative/boundary và quyền truy cập thực tế |
| <a id="s07"></a>S07 | UI/API/contract/solution | Version refs và delta: request/response, error, state changes, side effects | Có đủ contract để code/test, gồm lỗi/đồng thời khi áp dụng |
| <a id="s08"></a>S08 | Edge/NFR/transition impact | Selected cases/controls, thresholds và cách kiểm; chỉ rõ N/A | Không bỏ case bắt buộc vì đang chia Story nhỏ |
| <a id="s09"></a>S09 | AC và ví dụ | AC IDs gắn input/action/expected result, trace BR/model/case | Mọi AC có cách kiểm chứng; không dùng “đúng theo yêu cầu” làm AC |
| <a id="s10"></a>S10 | Verification approach | Test conditions theo rủi ro, test data/environment, oracle và evidence cần | QA xác nhận expected result độc lập; chưa cần mọi script đã viết |
| <a id="s11"></a>S11 | Dependency, ownership, estimate | Dev/QA owners, reviewer, dependency/commitment, estimate/capacity và câu hỏi | Đủ DoR để thực hiện; phần chưa sẵn có kế hoạch nhưng không che blocker |
| <a id="s12"></a>S12 | Completion và change refs | DoD policy áp dụng, approval refs, open decisions và change rules | Biết ai chốt và evidence nào cần để Done; không còn câu hỏi chặn |

**Thời điểm:** trước spawn phải có kế hoạch Story và nội dung baseline đủ rõ cho scope chọn; sau spawn có thể hoàn thiện phân công/dữ liệu/slot/capacity trước DoR. Không dùng “sẽ làm rõ khi code” cho quyết định làm thay đổi hành vi.


## Story đủ để triển khai mà không cần Task

**Đầu vào:** baseline cha, scope chọn, model/contract refs và delta. **Output:** Story spec/AC/test conditions, readiness evidence, checklist thực hiện hoặc Task links. Business/BA xác nhận nghĩa; Dev/TL xác nhận solution; QA xác nhận testability; PM chốt planning.

S01–S02 giữ nguồn/giá trị; S03–S05 hành vi; S06–S07 data/solution; S08–S09 ngoại lệ/AC; S10 kiểm thử; S11–S12 tổ chức/hoàn tất. Link kế thừa phải pin revision và chỉ ra subset, không trỏ toàn bộ một tài liệu rồi để người đọc tự chọn.

1. Dùng [phân rã, Example Mapping và INVEST](backlog-hierarchy-and-decomposition.md) để chọn và làm rõ hành vi.
2. Kiểm catalog và [Q01–Q07](requirements-review-process-and-verdicts.md) với các model áp dụng; giữ inventory/evidence.
3. Dev diễn giải cách đáp ứng, QA diễn giải setup/action/expected; không còn câu hỏi làm đổi hành vi/contract/control hoặc feasibility của scope chọn.
4. Kiểm [DoR Story](readiness-completion-and-approval-gates.md#workflow-9-1): quyền/input cho bước bắt đầu sẵn, dependency các bước sau có owner/cam kết, capacity xác nhận.
5. Ghi kế hoạch thực hiện. Nếu không có nhu cầu giao/theo dõi riêng, checklist đủ; không bắt Task để qua DoR.

Không phải thiết kế mọi dòng code trước. Lựa chọn tổ chức code nội bộ vẫn do Dev trong constraint; quyền nghiệp vụ, lỗi, state, contract chưa quyết không phải chi tiết được tùy ý chọn.

Đầy đủ S01–S12 trên giấy không chứng minh một Story thực tế đã Ready. Chỉ kết luận khi output/evidence/reviewer đúng scope/revision; thiếu input là Chưa kiểm. Dùng [mẫu Story](../assets/templates/story-specification-template.md).


## Mapping, ID và policy cần kiểm

Dùng [mapping theo từng S01–S12](catalog-check-model-mapping.md), [quy ước ID/trace](requirement-types-identifiers-and-traceability.md) và [policy register](project-policy-register.md). Record S11/S12 phải chỉ ra policy version áp dụng, không chỉ ghi “theo policy”. Các quyết định bắt buộc còn Pending chặn gate tương ứng, dù đã có đầy đủ Task. [Measurement](progress-measurement-and-feature-rollup.md) xác định cách báo readiness/delivery mà không đếm lặp.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
