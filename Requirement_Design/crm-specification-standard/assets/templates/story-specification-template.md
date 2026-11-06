# Mẫu hồ sơ Story

Mã tài liệu: **TPL-STORY-SPECIFICATION-TEMPLATE** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Mở bằng ID/tên và một câu actor → outcome. Dùng bảng context ngắn cho parent/revision, baseline, người nhận việc và trạng thái evidence. Đọc [Story catalog](../../references/story-specification-catalog.md).

<a id="spec-10-2"></a>

Ghi Use Case nguồn, scenario/step hoặc delta, dependency và phạm vi ngoài Story. Trace `parent` tới Epic và `derived-from` tới MOD ID với path#locator và Epic revision.

## S01 — Định danh và baseline

ID, Epic/Capability, selected scope và pinned baseline/revision. Có thể là section trong Epic nếu là một nơi nội dung chuẩn; không duy trì spec trùng.

## S02 — Actor và outcome

Nêu delta bàn giao so với phạm vi Epic, parent hiện có và control bắt buộc đi cùng. Nếu đang đổi allocation, ghi rationale cấp/parent theo checkpoint. Tên màn hình, role hoặc một bước Use Case chưa đủ chứng minh Story riêng.

Người dùng nhận kết quả gì; in/out scope cụ thể và phần không nhận.

## S03 — Điều kiện và kết quả

Trigger/preconditions; success/failure postconditions, quyền/state/data áp dụng.

## S04 — Luồng được chọn

Steps và alternate/exception; delta so với parent/shared model có ref rõ.

## S05 — Rule và transition

Selected BR/transition/decision IDs, revision; N/A phải có reason/authority.

## S06 — Dữ liệu và permission

Subset và delta của data/validation/permission; không bỏ control chung để slice có vẻ độc lập.

## S07 — UI/API và solution

Với Story có UI, dẫn Screen ID, Scenario ID, entrypoint và walkthrough từ đúng baseline Epic. Ghi BR/AC/contract áp dụng cho từng scenario.

Screen/query/contract/solution refs hiện hành; ranh giới implementation. Chưa có contract thì ghi gap.

## S08 — Edge cases và kiểm soát

Selected errors/edges/NFR/transition impacts hoặc N/A có reason; expected outcomes đủ để kiểm.

## S09 — Acceptance Criteria

Mỗi AC một mục khi dài: điều kiện → thao tác → kết quả → source/BR/model refs → gap.

## S10 — Test approach

Planned conditions, fixture/data/environment, kênh quan sát và oracle; chưa ghi runtime Pass khi chưa có run.

## S11 — Kế hoạch và phụ thuộc

Owners/reviewers, dependency, estimate/capacity, questions. Chọn checklist hoặc Tasks theo nhu cầu output/giao việc, không bắt có Task.

## S12 — DoD, approval và thay đổi

Policy/version, approval/change refs và scope. Đóng Story cần QA verdict/PM closure/evidence theo gate, không suy từ Task Done.

## Review và điều kiện nhận việc

Từng S item giữ applicability, output/revision, source/authority, owner/reviewer, verdict/evidence, work signal và gap/due. Index để tra; phần giải thích dài ghi ở mục tương ứng.

Trước nhận việc: kiểm DoR, Dev/QA read-back và PM planning. Bàn giao QA cần code/review/CI/build/environment/evidence thực tế; đóng Story cần AC/coverage đã chạy, defects/disposition, QA verdict và PM closure. Không lấy số item có nội dung thành % sản phẩm.

Theo [coverage](../../references/coverage-inventories-and-traceability.md#spec-7-1) và [review/gate](../../references/requirements-review-process-and-verdicts.md). Kết thúc bằng metadata đúng kind, không đổi ID nguồn để khớp ví dụ.
