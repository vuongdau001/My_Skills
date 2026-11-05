# Mẫu hồ sơ Epic

Mã tài liệu: **TPL-EPIC-SPECIFICATION-TEMPLATE** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

ID/tên Epic và một đoạn về mục tiêu. Bảng context ngắn: Feature, selected scope, revision/baseline, sources, owners và bước hiện tại. Đọc [Epic catalog](../../references/epic-specification-catalog.md).

<a id="spec-10"></a>

## Cách dùng mẫu

Giữ E01–E16 và điền sâu theo scope đang xét. Mỗi mục có nội dung hoặc ref đúng revision; có thể thêm mục con, không ép một dòng checklist thay toàn bộ model.

<a id="spec-10-1"></a>

## E01 — Bối cảnh, mục tiêu và phạm vi

Nêu outcome, selected scope, exclusions và acceptance toàn Epic; phân biệt scope hiện tại với các nhánh làm sau.

## E02 — Actor, thuật ngữ và domain model

Định nghĩa object/identity và invariants; chỉ rõ authority/owner, không suy role label là quyền cụ thể.

## E03 — Luồng nghiệp vụ

Index flow/use case; mỗi flow có trigger, main steps và các nhánh thay thế/ngoại lệ có kết quả hoặc question ID.

## E04 — Trạng thái và chuyển trạng thái

Định nghĩa state và command disposition; tách guard tại thời điểm thao tác với invariant liên tục.

## E05 — Business Rules

Mỗi BR có statement/điều kiện/kết quả và REQ/decision/source refs. Bảng chỉ giữ index ngắn; rule dài dùng mục riêng.

## E06 — Dữ liệu và validation

Dictionary/type/boundary, normalization, null/default/uniqueness và fields bắt buộc; chưa biết thì ghi gap, không tự đặt schema.

## E07 — Permission và data scope

Lập ma trận actor × action × state × field/context, cùng ví dụ/negative case. Ghi allow/deny/visibility đã chốt và điểm còn thiếu.

## E08 — UI/UX và trạng thái tương tác

Dẫn screen/UI contract, field/action/state inventory, hoặc N/A có reason/authority. Mockup chưa tự là contract đã ký.

## E09 — API và tích hợp

Dẫn input/output, permission, error, sequence/consistency, retry/idempotency, read-back/freshness và side effects. Không đặt endpoint/DTO giả.

## E10 — Ngoại lệ và tình huống biên

Mỗi case có điều kiện, action, expected outcome và rule/gap; xét concurrency/partial failure/replay khi áp dụng.

## E11 — NFR và yêu cầu kiểm soát

Ghi workload/measurement/control, threshold nếu authority chọn, policy refs và acceptance method. Unknown chưa là N/A.

## E12 — Migration và vận hành

Ghi applicability, mapping/cutover/reconcile/restore và dữ liệu/owner cần; chưa khảo sát thì nêu thiếu input.

## E13 — Solution, dependency và feasibility

Nêu options/trade-offs/constraints, contract của hai đầu và evidence khả thi. Giữ solution/authority pending nếu chưa xác nhận.

## E14 — AC và planned verification

Mỗi AC dùng điều kiện → thao tác → kết quả → truy vết/gap. Ghi test condition/setup/observation; tách planned coverage khỏi TestRun thật.

## E15 — Story candidates và allocation

Mỗi candidate nhận outcome, selected BR/model/AC, dependency, sizing/owner khi có. Link + activation nếu cùng outcome không tự tách thành API/UI Stories. Chưa đủ gate thì giữ candidate.

## E16 — Applicability, quyết định và baseline

Tổng hợp scope/revision, questions/decisions, policy, review và manifest. Giữ mục áp dụng/Unknown/N/A có reason; chỉ dẫn approval/merge khi có evidence.

## Review, kế hoạch và bàn giao

Với từng item, giữ applicability/reason, output/revision, source/authority, owner/reviewer, work signal, verdict/evidence, gap/due và bước tiếp. Có thể dùng index ngắn rồi chi tiết từng item; không ép vào bảng bảy cột.

Theo [coverage/AC](../../references/coverage-inventories-and-traceability.md#spec-7-1), nối scope → rule/model → AC → planned verification. Phân biệt analysis/solution/testability; thiếu input không được chấm Đạt. [Review/gate](../../references/requirements-review-process-and-verdicts.md) và PM manifest/baseline vẫn áp dụng trước tạo Story. Kết thúc bằng metadata đúng loại.
