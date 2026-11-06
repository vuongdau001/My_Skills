# Mẫu hồ sơ Epic

Mã tài liệu: **TPL-EPIC-SPECIFICATION-TEMPLATE** · Gói CRM 2.0.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

ID/tên Epic và một đoạn về mục tiêu. Bảng context ngắn: Capability, selected scope, revision/baseline, sources, owners và bước hiện tại. Đọc [Epic catalog](../../references/epic-specification-catalog.md).

<a id="spec-10"></a>

## Cách dùng mẫu

Giữ E01–E16 và điền sâu theo scope đang xét. Mỗi mục có nội dung hoặc ref đúng revision; có thể thêm mục con, không ép một dòng checklist thay toàn bộ model.

<a id="spec-10-1"></a>

## E01 — Bối cảnh, mục tiêu và phạm vi

Giải thích vì sao scope thuộc Capability này và cần Epic riêng so với Epic lân cận. Nêu model/control/acceptance chung, delta dự kiến của Story và rationale gom/tách theo checkpoint. Nếu chỉ có một Story, giải thích vai trò hồ sơ Epic; không chép lại cùng một outcome/AC để lấp cấp.

Ghi mục tiêu duy nhất ở cấp user-goal và outcome có ý nghĩa với actor. Tách boundary hệ thống, hành vi đầy đủ của Use Case và selected scope của đợt. Ghi exclusions, các nhánh làm sau và cách nghiệm thu outcome.

## E02 — Actor, thuật ngữ và domain model

Ghi actor chính, actor hỗ trợ, stakeholder và quyền lợi cần bảo vệ. Định nghĩa object/identity và invariants; chỉ rõ authority/owner, không suy role label là quyền cụ thể.

## E03 — Use Case

<a id="use-case"></a>

**MOD ID, tên và mục tiêu.** Ghi trigger, preconditions và actor thực hiện. Dùng [D01](../../references/models/business-flows-and-use-cases.md).

### Luồng chính

Mỗi bước có locator tường minh, chủ thể, tương tác và phản hồi quan sát. Dẫn state, BR, data và permission đúng ID/revision ở E04–E07.

### Nhánh thay thế và ngoại lệ

Mỗi nhánh có locator, bước gốc, điều kiện, hành vi, điểm quay lại hoặc outcome kết thúc. Xét hủy, timeout, retry, concurrency và partial failure khi áp dụng. Với phần chưa rõ, ghi question, tác động và authority.

### Kết quả cuối

Ghi success, failure và bảo đảm tối thiểu về dữ liệu, quyền, trạng thái và side effects. Gắn locator để E10/E14/E15 dẫn lại.

## E04 — Trạng thái và chuyển trạng thái

Định nghĩa state và command disposition; tách guard tại thời điểm thao tác với invariant liên tục.

## E05 — Business Rules

Mỗi BR có statement/điều kiện/kết quả và REQ/decision/source refs. Bảng chỉ giữ index ngắn; rule dài dùng mục riêng.

## E06 — Dữ liệu và validation

Dictionary/type/boundary, normalization, null/default/uniqueness và fields bắt buộc; chưa biết thì ghi gap, không tự đặt schema.

## E07 — Permission và data scope

Lập ma trận actor × action × state × field/context, cùng ví dụ/negative case. Ghi allow/deny/visibility đã chốt và điểm còn thiếu.

## E08 — UI/UX và trạng thái tương tác

Dẫn bước/nhánh E03, Screen/Scenario IDs, UI contract, inventory và binding tới Prototype/walkthrough đúng selected scope. Ghi N/A có reason, contract và người xác nhận khi scope không tác động UI. Xem [mẫu bundle](prototype-bundle-template.md).

## E09 — API và tích hợp

Dẫn step/scenario E03, contract ID/revision, input/output, permission, error, sequence/consistency, retry/idempotency, read-back/freshness và side effects. Không đặt endpoint/DTO giả.

## E10 — Ngoại lệ và tình huống biên

Mỗi case dẫn nhánh và kết quả E03, cùng rule/gap. Ghi disposition cho các chiều rủi ro đã rà.

## E11 — NFR và yêu cầu kiểm soát

Ghi workload/measurement/control, threshold nếu authority chọn, policy refs và acceptance method. Unknown chưa là N/A.

## E12 — Migration và vận hành

Ghi applicability, mapping/cutover/reconcile/restore và dữ liệu/owner cần; chưa khảo sát thì nêu thiếu input.

## E13 — Solution, dependency và feasibility

Nêu options/trade-offs/constraints, contract của hai đầu và evidence khả thi. Giữ solution/authority pending nếu chưa xác nhận.

## E14 — AC và planned verification

Mỗi AC dùng điều kiện → thao tác → kết quả → truy vết/gap. Dẫn scenario và outcome E03 tới test condition/setup/observation/evidence; tách planned coverage khỏi TestRun thật.

## E15 — Story candidates và allocation

Mỗi candidate nhận MOD ID và revision, scenario/bước hoặc delta, outcome, BR/model/AC, controls và dependency. Ghi phần còn lại và phép kiểm tích hợp. Link + activation nếu cùng outcome không tự tách thành API/UI Stories. Chưa đủ gate thì giữ candidate.

## E16 — Applicability, quyết định và baseline

Ghi policy use-case-v1, scope/revision/baseline, phần đã nghiệm thu, questions/decisions, review và manifest. Giữ mục áp dụng/Unknown/N/A có reason; chỉ dẫn approval/merge khi có evidence.

## Review, kế hoạch và bàn giao

Với từng item, giữ applicability/reason, output/revision, source/authority, owner/reviewer, work signal, verdict/evidence, gap/due và bước tiếp. Có thể dùng index ngắn rồi chi tiết từng item; không ép vào bảng bảy cột.

Theo [coverage/AC](../../references/coverage-inventories-and-traceability.md#spec-7-1), nối scope → rule/model → AC → planned verification. Phân biệt analysis/solution/testability; thiếu input không được chấm Đạt. [Review/gate](../../references/requirements-review-process-and-verdicts.md) và PM manifest/baseline vẫn áp dụng trước tạo Story. Kết thúc bằng metadata đúng loại.

<details>
<summary>Metadata mẫu, thay ID và revision bằng giá trị đã cấp</summary>

```crm-spec-kit
{
  "schema_version": 1,
  "kind": "Epic",
  "artifact_id": "<epic-id>",
  "revision": "<epic-revision>",
  "review_verdict": "Chưa kiểm",
  "epic_policy": "use-case-v1",
  "use_case": {"id": "<mod-id>", "level": "user-goal", "locator": "#use-case"},
  "defined_ids": ["<mod-id>"]
}
```

</details>
