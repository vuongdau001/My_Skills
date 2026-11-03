# Artifact Metadata and Lint

ID: **CRM-ARTIFACT-LINT** · CRM Workflow Kit 1.5.0 · 03/11/2026

## Purpose

Cho helper kiểm được vocabulary/ID/links bằng dữ liệu có cấu trúc, không regex mọi câu văn rồi kết luận semantics. Mỗi artifact mới có tối đa một JSON block [theo mẫu](../assets/templates/artifact-metadata-template.md). File legacy chưa có block vẫn được audit explicit fields/links và được cảnh báo; không bắt rewrite dữ liệu cũ tự động.

Metadata schema_version=1; kind là Feature/Epic/Story/Task/Review/Baseline/Report/Pilot/Project/Decision/Requirement/Model/TestCase/TestRun. artifact_id và defined_ids là các **định nghĩa** thuộc PREFIX-CRM-NNN; nhắc ID trong nội dung không thành definition. Cùng một ID trong artifact_id và defined_ids cùng file đếm một lần; hai file định nghĩa cùng ID là lỗi. Một file có thể chứa nhiều BR/AC, khai báo defined_ids rõ ràng.

work_status chỉ dùng cho Epic/Story/Task với đúng status của từng loại. Feature chỉ ở tài liệu, không được tự nhận Jira status. review_verdict: Đạt/Không đạt/Chưa kiểm/N/A; N/A cần na_reason và authority/evidence vẫn do người review xác nhận. decision_state: Pending/Proposed/Approved/Superseded. Approval trong metadata chỉ là khai báo, lint không chứng nhận có thẩm quyền.

references chứa repo-relative-from-artifact links, giống Markdown links; kiểm file/anchor, chặn absolute/escaping paths. HTTP/HTTPS/mailto không được truy cập khi lint. Mọi dữ liệu này vẫn phải qua Q01–Q07/authority khi áp dụng.

## Controlled Fields and Legacy

Ngoài metadata, helper kiểm các dòng explicit `Status:`, `Decision state:`, `Verdict:` và các controlled columns/property rows tương ứng trong bảng Markdown đơn giản ngoài code fence. Reason sau verdict phải tách bằng khoảng trắng/dấu câu; `Đạt-một-phần` không phải Đạt. Không rà mọi từ Đạt trong prose/test examples như một verdict. Heading chính bắt đầu bằng ID, property “Feature ID” và cột “Definition ID”/typed ID được audit như definitions; cột chung “ID” có thể là tham chiếu, chỉ cảnh báo cần khai báo ownership, không tự coi là definition; trường hợp nhiều layout/escaped table phức tạp vẫn cần metadata hoặc human review. Với table/format legacy khác, báo chưa kiểm metadata nếu không có schema; đừng coi lint valid là chứng minh mọi ô Markdown đúng vocabulary.

ID trùng được kiểm ở định nghĩa, không phải số lần tham chiếu. next-id scan cả các ID được nhắc và ledger để tránh cấp lại ID cũ, nhưng đó không là phép kiểm duplicate definitions. Namespace theo project config hiện là CRM; mã nguồn như SRC-FL/L01/VR-CUS-* là source refs, không tự đổi thành REQ.

Tag [INFERRED] kèm question là quy ước binding tùy chọn. Nếu workstream có `require_question_for_inferred: true`, mỗi dòng tag cần Q-CRM-NNN cùng dòng; việc câu hỏi tồn tại/đúng authority vẫn cần review. Không ép quy tắc này lên mọi project nếu chưa được chọn.

## Exit and Limits

ERROR trả exit 1; WARN cho legacy/missing structured coverage. `semantic_approval: false` luôn hiện. Không sửa artifact tự động. Lint lỗi thì tác giả sửa đúng nguồn và chạy lại; check/review workflows chỉ ghi record và đề xuất correction.

Sources/config/kit không tự trở thành writable chỉ vì helper đọc được. Path config và ID reservation là repo-owned tooling records; spec outputs tuân write boundary workflow. Không có hook Git/Jira/CI tự động trong bản này.
