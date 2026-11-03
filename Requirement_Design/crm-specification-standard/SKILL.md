---
name: crm-specification-standard
description: Soạn và review yêu cầu CRM, phân rã Epic thành Story, quyết định checklist hay Task, kiểm DoR/DoD và truy vết baseline theo quy trình CRM. Dùng khi chuẩn bị hồ sơ hoặc đánh giá readiness; không tự triển khai sản phẩm hay thao tác Jira/Git thay người dùng.
---

# Chuẩn đặc tả và bàn giao CRM

Đây là gói tài liệu dùng lại cho nhiều agent. Đọc [quy ước CRM](references/crm-project-rules.md) trước, rồi chọn tuyến theo yêu cầu; không tải toàn bộ tài liệu mỗi lần. Quy trình không tự cấp quyền tạo/comment ticket, chuyển trạng thái hay merge. Repo package không đồng nghĩa đã cài vào runtime.

## Chọn tuyến đọc

| Yêu cầu | Đọc theo thứ tự | Đầu ra |
|---|---|---|
| Soạn/review Feature | [F01–F08](references/feature-specification-catalog.md) → [mẫu Feature](assets/templates/feature-specification-template.md) | Outcome/scope/Epic allocation/acceptance đúng bước |
| Thiết lập policy và định danh | [Policy register](references/project-policy-register.md) → [ID và loại requirement](references/requirement-types-identifiers-and-traceability.md) | Register dự án hoặc missing decisions; không tự duyệt ngưỡng |
| Báo cáo tiến độ | [Measurement/roll-up](references/progress-measurement-and-feature-rollup.md) → [mẫu báo cáo](assets/templates/progress-report-template.md) | Readiness, delivery, acceptance riêng; mẫu số và snapshot rõ |
| Pilot quy trình | [Pilot thực tế](references/pilot-and-operational-validation.md) → [pilot record](assets/templates/pilot-review-record-template.md) | Evidence/findings cho bước thật sự được thử |
| Giải thích/phân rã backlog | [Phân cấp và phân rã](references/backlog-hierarchy-and-decomposition.md) → [baseline](references/baseline-and-change-control.md) | Story manifest, rationale, dependency và câu hỏi |
| Soạn/review Epic | [Catalog Epic E01–E16](references/epic-specification-catalog.md) → [model áp dụng](references/coverage-inventories-and-traceability.md) → [mẫu Epic](assets/templates/epic-specification-template.md) | Scope/model/solution/acceptance, applicability và gaps |
| Soạn/review Story | [Catalog Story S01–S12](references/story-specification-catalog.md) → baseline/model cha + delta → [mẫu Story](assets/templates/story-specification-template.md) | Hành vi/AC/test conditions, pinned refs và readiness |
| Lập kế hoạch hoặc giao Task | [Quyết định checklist/Task](references/backlog-hierarchy-and-decomposition.md) → [Task T01–T08](references/task-planning-and-completion.md) → [mẫu Task](assets/templates/implementation-task-template.md) nếu cần | Checklist hoặc brief Task; không sinh ticket hình thức |
| Review toàn bộ Feature/Epic/Story | [Quy trình/verdict](references/requirements-review-process-and-verdicts.md) → catalog target + [mapping E/S](references/catalog-check-model-mapping.md) → bảy check Q01–Q07 → các model áp dụng → [review record](assets/templates/requirements-review-record-template.md) | Findings/evidence/verdict scoped, không ngầm PASS |
| Review một vấn đề | Quy trình/verdict → đúng check/model từ [inventory](references/coverage-inventories-and-traceability.md) | Kết luận đúng phần được kiểm; nêu phần chưa xét |
| Xét gate/tiến độ/thay đổi | [DoR/DoD/approval](references/readiness-completion-and-approval-gates.md) → [Jira/progress](references/jira-status-and-progress-reporting.md) → [change control](references/baseline-and-change-control.md) | Quyết định có evidence hoặc missing items/owner |
| Thiết kế bàn giao AI/hook | [Context và hard gate](references/ai-handoff-and-hard-gates.md) | Yêu cầu cơ chế kiểm; không tuyên bố hook đã cài |

## Quy tắc thực hiện

- Policy bắt buộc chưa được phê duyệt thì gate liên quan chưa đủ điều kiện; không dùng SLA hết hạn, skipped check hoặc “theo policy” không ref làm bằng chứng Đạt.
- Chốt target, selected scope và revision; phân biệt nguồn/decision, assumption, proposal và unknown. Không tự điền policy/ngưỡng còn thiếu.
- Story đủ DoR có thể triển khai trực tiếp. Task chỉ khi cần quản lý output riêng, không là nơi bù requirement thiếu.
- Dùng source → rule/model → Story/AC → planned verification; sau triển khai mới gắn code/build/run/evidence. Giữ một nguồn chuẩn, pin version và chỉ ghi delta.
- Full review phải xét Q01–Q07 và applicability của model; N/A cần lý do/reviewer. Thiếu input là Chưa kiểm, có gap là Không đạt; không trung bình điểm để qua gate.
- Business/technical/QA authority xác nhận chuyên môn; PM chốt output/gate theo quy trình. AI không tự giả approval, QA Pass hoặc evidence runtime.
- Thay đổi nội dung đã duyệt phải impact/review lại đúng phần. Task Done không tự làm Story Done; baseline phần Epic không làm Epic Done.
- Mọi [ví dụ](references/examples/decomposition-and-task-decisions.md) là giả định. Ví dụ [ProjectCodeRequest](references/examples/project-code-request-specification.md) còn câu hỏi chặn, không phải spec Ready.

Trả output phù hợp yêu cầu: scope/revision, artifacts/refs, thao tác kiểm, findings với evidence/counterexample, verdict và next actions/owner. Nếu thiếu authority/input, tiếp tục phần độc lập và nêu quyết định đang chặn; không tự quyết để hoàn thiện template.

## Nguồn và kiểm tra gói

Xem [nguồn và CRM tailoring](references/standards-and-crm-tailoring.md) khi cần lý giải phương pháp. Các mã F/E/S/T/Q/D thuộc gói CRM, không là checklist nguyên bản của một framework. [Manifest](reference-manifest.json) định danh tài liệu; [migration map](provenance/source-to-reference-migration-map.md) truy nguồn; [acceptance scenarios](references/pack-acceptance-scenarios.md) kiểm hành vi mong đợi.

Chạy `python3 scripts/validate_reference_pack.py` từ folder này (hoặc gọi bằng đường dẫn tới script). Kết quả chỉ xác nhận cấu trúc/refs/migration; không cấp approval hay chứng minh spec/phần mềm đạt.

Kết quả: [báo cáo cập nhật 1.3](provenance/pack-validation-report-v1.3.md); [báo cáo lịch sử 1.2](provenance/pack-validation-report.md).
