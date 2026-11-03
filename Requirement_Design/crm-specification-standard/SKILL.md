---
name: crm-specification-standard
description: Soạn và review yêu cầu CRM, phân rã Epic thành Story, quyết định checklist hay Task, kiểm DoR/DoD và truy vết baseline theo quy trình CRM. Dùng khi chuẩn bị hồ sơ hoặc đánh giá readiness; không tự triển khai sản phẩm hay thao tác Jira/Git thay người dùng.
---

# Chuẩn đặc tả và bàn giao CRM

Đây là gói tài liệu dùng lại cho nhiều agent. Đọc [quy ước CRM](references/crm-project-rules.md) trước, rồi chọn tuyến theo yêu cầu; không tải toàn bộ tài liệu mỗi lần. Quy trình không tự cấp quyền tạo/comment ticket, chuyển trạng thái hay merge. Repo package không đồng nghĩa đã cài vào runtime.

## Chọn tuyến đọc

| Yêu cầu | Đọc theo thứ tự | Đầu ra |
|---|---|---|
| Giải thích/phân rã backlog | [Phân cấp và phân rã](references/backlog-hierarchy-and-decomposition.md) → [baseline](references/baseline-and-change-control.md) | Story manifest, rationale, dependency và câu hỏi |
| Soạn/review Epic | [Catalog Epic E01–E16](references/epic-specification-catalog.md) → [model áp dụng](references/coverage-inventories-and-traceability.md) → [mẫu Epic](assets/templates/epic-specification-template.md) | Scope/model/solution/acceptance, applicability và gaps |
| Soạn/review Story | [Catalog Story S01–S12](references/story-specification-catalog.md) → baseline/model cha + delta → [mẫu Story](assets/templates/story-specification-template.md) | Hành vi/AC/test conditions, pinned refs và readiness |
| Lập kế hoạch hoặc giao Task | [Quyết định checklist/Task](references/backlog-hierarchy-and-decomposition.md) → [Task T01–T08](references/task-planning-and-completion.md) → [mẫu Task](assets/templates/implementation-task-template.md) nếu cần | Checklist hoặc brief Task; không sinh ticket hình thức |
| Review toàn bộ Epic/Story | [Quy trình/verdict](references/requirements-review-process-and-verdicts.md) → catalog target → bảy check Q01–Q07 → các model áp dụng → [review record](assets/templates/requirements-review-record-template.md) | Findings/evidence/verdict scoped, không ngầm PASS |
| Review một vấn đề | Quy trình/verdict → đúng check/model từ [inventory](references/coverage-inventories-and-traceability.md) | Kết luận đúng phần được kiểm; nêu phần chưa xét |
| Xét gate/tiến độ/thay đổi | [DoR/DoD/approval](references/readiness-completion-and-approval-gates.md) → [Jira/progress](references/jira-status-and-progress-reporting.md) → [change control](references/baseline-and-change-control.md) | Quyết định có evidence hoặc missing items/owner |
| Thiết kế bàn giao AI/hook | [Context và hard gate](references/ai-handoff-and-hard-gates.md) | Yêu cầu cơ chế kiểm; không tuyên bố hook đã cài |

## Quy tắc thực hiện

- Chốt target, selected scope và revision; phân biệt nguồn/decision, assumption, proposal và unknown. Không tự điền policy/ngưỡng còn thiếu.
- Story đủ DoR có thể triển khai trực tiếp. Task chỉ khi cần quản lý output riêng, không là nơi bù requirement thiếu.
- Dùng source → rule/model → Story/AC → planned verification; sau triển khai mới gắn code/build/run/evidence. Giữ một nguồn chuẩn, pin version và chỉ ghi delta.
- Full review phải xét Q01–Q07 và applicability của model; N/A cần lý do/reviewer. Thiếu input là Chưa kiểm, có gap là Không đạt; không trung bình điểm để qua gate.
- Business/technical/QA authority xác nhận chuyên môn; PM chốt output/gate theo quy trình. AI không tự giả approval, QA Pass hoặc evidence runtime.
- Thay đổi nội dung đã duyệt phải impact/review lại đúng phần. Task Done không tự làm Story Done; baseline phần Epic không làm Epic Done.
- Mọi [ví dụ](references/examples/decomposition-and-task-decisions.md) là giả định. Ví dụ [ProjectCodeRequest](references/examples/project-code-request-specification.md) còn câu hỏi chặn, không phải spec Ready.

Trả output phù hợp yêu cầu: scope/revision, artifacts/refs, thao tác kiểm, findings với evidence/counterexample, verdict và next actions/owner. Nếu thiếu authority/input, tiếp tục phần độc lập và nêu quyết định đang chặn; không tự quyết để hoàn thiện template.

## Nguồn và kiểm tra gói

Xem [nguồn và CRM tailoring](references/standards-and-crm-tailoring.md) khi cần lý giải phương pháp. Các mã E/S/T/Q/D thuộc gói CRM, không là checklist nguyên bản của một framework. [Manifest](reference-manifest.json) định danh tài liệu; [migration map](provenance/source-to-reference-migration-map.md) truy nguồn; [acceptance scenarios](references/pack-acceptance-scenarios.md) kiểm hành vi mong đợi.

Chạy `python3 scripts/validate_reference_pack.py` từ folder này (hoặc gọi bằng đường dẫn tới script). Kết quả chỉ xác nhận cấu trúc/refs/migration; không cấp approval hay chứng minh spec/phần mềm đạt.

Kết quả lần đóng gói: [báo cáo kiểm tra và giới hạn](provenance/pack-validation-report.md).
