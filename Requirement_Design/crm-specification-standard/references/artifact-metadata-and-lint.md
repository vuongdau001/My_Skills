# Artifact Metadata and Lint

ID: **CRM-ARTIFACT-LINT** · CRM Workflow Kit 1.5.0 · 03/11/2026

Epic schema 1/2 có thể khai `epic_policy: "use-case-v1"` và đúng một `use_case` với MOD ID, level user-goal và locator tường minh trong E03. Epic phải khai MOD ID trong defined_ids. Lint nhận diện legacy, kiểm uniqueness toàn repo và chặn Epic legacy thuộc scope baseline/readiness. Trace MOD ID dẫn anchor E03 và revision của Epic. Xem [policy Epic–Use Case](epic-use-case-policy.md).

## Purpose

Cho helper kiểm được vocabulary/ID/links bằng dữ liệu có cấu trúc, không regex mọi câu văn rồi kết luận semantics. Mỗi artifact mới có tối đa một JSON block [theo mẫu](../assets/templates/artifact-metadata-template.md). File legacy chưa có block vẫn được audit explicit fields/links và được cảnh báo; không bắt rewrite dữ liệu cũ tự động.

Metadata schema_version=1 tiếp tục được đọc. Schema 2 thêm Meeting/Assumption/Constraint và structured Decision records theo [knowledge records](knowledge-records-and-evidence.md). kind cũ là Capability/Epic/Story/Task/Review/Baseline/Report/Pilot/Project/Decision/Requirement/Model/TestCase/TestRun. artifact_id, defined_ids và IDs của records là definitions thuộc PREFIX-CRM-NNN; nhắc ID trong nội dung không thành definition. Cùng ID trong artifact_id/defined_ids cùng file đếm một lần; record lặp trong register hoặc hai file định nghĩa cùng ID là lỗi. Một file có thể chứa nhiều BR/AC với defined_ids, hoặc nhiều knowledge records với records.

work_status chỉ dùng cho Epic/Story/Task với đúng status của từng loại. Capability chỉ ở tài liệu, không được tự nhận Jira status. review_verdict: Đạt/Không đạt/Chưa kiểm/N/A; N/A cần na_reason và authority/evidence vẫn do người review xác nhận. decision_state: Pending/Proposed/Approved/Superseded/Rejected/Withdrawn. Approval trong metadata chỉ là khai báo, lint không chứng nhận có thẩm quyền.

references chứa repo-relative-from-artifact links, giống Markdown links; kiểm file/anchor, chặn absolute/escaping paths. HTTP/HTTPS/mailto không được truy cập khi lint. Mọi dữ liệu này vẫn phải qua Q01–Q07/authority khi áp dụng.

trace_links kiểm target ID có definition đúng file, relation, revision và optional content hash; evidence schema 2 cần revision/hash. Kind schema 1 Decision không bị ép field mới. --gate readiness/baseline tăng unresolved record obligations thành ERROR trong closure của --target; không --target là whole-workstream hiện hành. Structural checks vẫn rộng. Lint không tìm được mọi missing trace link, không đánh giá nội dung đúng hoặc chạy full DoR. Layout inference dùng artifact_paths và cả hai tên thư mục chuẩn, xem [layout](artifact-layout-and-migration.md).

## Presentation của Markdown

Theo [standard viết artifact](artifact-writing-standard.md), Markdown mới đặt một metadata block cuối file; details/summary là tùy chọn, code fences không indent. Helper đọc block theo dữ liệu bất kể ở đầu hay cuối để giữ tương thích legacy. Không thêm HTML vào JSON/config/assessment; không thêm hard gate về độ dài câu/số cột. Lint kiểm cấu trúc, không chứng nhận readability hoặc semantics.

## Controlled Fields and Legacy

Ngoài metadata, helper kiểm các dòng explicit `Status:`, `Decision state:`, `Verdict:` và các controlled columns/property rows tương ứng trong bảng Markdown đơn giản ngoài code fence. Reason sau verdict phải tách bằng khoảng trắng/dấu câu; `Đạt-một-phần` không phải Đạt. Không rà mọi từ Đạt trong prose/test examples như một verdict. Heading chính bắt đầu bằng ID, property “Capability ID” và cột “Definition ID”/typed ID được audit như definitions; cột chung “ID” có thể là tham chiếu, chỉ cảnh báo cần khai báo ownership, không tự coi là definition; trường hợp nhiều layout/escaped table phức tạp vẫn cần metadata hoặc human review. Với table/format legacy khác, báo chưa kiểm metadata nếu không có schema; đừng coi lint valid là chứng minh mọi ô Markdown đúng vocabulary.

ID trùng được kiểm ở định nghĩa, không phải số lần tham chiếu. next-id scan cả các ID được nhắc và ledger để tránh cấp lại ID cũ, nhưng đó không là phép kiểm duplicate definitions. Namespace theo project config hiện là CRM; mã nguồn như SRC-FL/L01/VR-CUS-* là source refs, không tự đổi thành REQ.

Tag [INFERRED] kèm question là quy ước binding tùy chọn. Nếu workstream có `require_question_for_inferred: true`, mỗi dòng tag cần Q-CRM-NNN cùng dòng; việc câu hỏi tồn tại/đúng authority vẫn cần review. Không ép quy tắc này lên mọi project nếu chưa được chọn.

## Exit and Limits

ERROR trả exit 1; WARN cho legacy/missing structured coverage. `semantic_approval: false` luôn hiện. Không sửa artifact tự động. Lint lỗi thì tác giả sửa đúng nguồn và chạy lại; check/review workflows chỉ ghi record và đề xuất correction.

Sources/config/kit không tự trở thành writable chỉ vì helper đọc được. Path config và ID reservation là repo-owned tooling records; spec outputs tuân write boundary workflow. Không có hook Git/Jira/CI tự động trong bản này.
