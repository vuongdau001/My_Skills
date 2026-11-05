# Mẫu record review/check

Mã tài liệu: **TPL-REQUIREMENTS-REVIEW-RECORD-TEMPLATE** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Mở bằng target/scope/revision và mục tiêu review. Nêu full/focused, checks/catalog/model áp dụng, phần chưa xét, người kiểm và mode author self-check/specialist/independent đúng thực tế.

<a id="spec-3-13"></a>

## Input và phạm vi kiểm

Nguồn, actor/authority, inventory/model revision và target hashes; policy/version. Thiếu input/authority nêu rõ. Dùng F01–F08, E01–E16, S01–S12 hoặc T01–T08 đúng loại; full specification review xét Q01–Q07.

## Kết quả từng phép kiểm

Index ngắn: item/check → verdict → finding/evidence. Với từng check dài, trình bày:

- **Điều kiện/phạm vi:** target, inventory và applicability; N/A có reason/authority.
- **Cách kiểm đã làm:** thao tác, witness/counterexample và source locator.
- **Expected/observed:** phân biệt kết quả mong đợi với điều đã thấy trong tài liệu/thực thi.
- **Evidence và kết luận:** refs/revision, verdict scoped, reviewer.
- **Finding:** ID, tác động/gate, owner/due; severity theo policy nếu đã chốt.

## Findings và closure

Mỗi finding một mục có counterexample, correction/decision ref, reviewer closure và revision kiểm lại. Giữ counts total/disposed/Unknown/missing verification theo inventory; không che unknown bằng N/A hoặc tỷ lệ trung bình.

## Kết luận và bàn giao

Ghi scope đã/chưa đủ điều kiện, thiếu approval nào và receiver/next action. Check/review không sửa target hoặc tự đóng ticket. [Review protocol](../../references/requirements-review-process-and-verdicts.md), [mapping](../../references/catalog-check-model-mapping.md) và [policy](../../references/project-policy-register.md) tiếp tục áp dụng.

Trước code, nhận xét spec/model khác runtime test Pass. Sau code, evidence cần đúng build/config/run. Metadata Review chỉ khai báo verdict, không chứng nhận authority.
