# Workflow Execution Protocol

ID: CRM-WORKFLOW-PROTOCOL · CRM Workflow Kit 3.0.0

## Purpose & Routing

Chọn một trong 10 function của [SKILL](../SKILL.md). Status/next step là [hướng dẫn chung](conversational-status-and-next-step.md), không function riêng. Không dùng workflow đã bỏ để tạo package/report/pilot. Khi user đang giao authoring và hỏi status, trả lời ngắn rồi tiếp tục scope đã giao.

## Work Context & Resume

Đọc config, spec_root instructions và canonical artifacts. Context gồm function, workstream, target ID/kind, selected scope, revision hiện hành, nguồn, quyền đọc/sửa và gaps. Không lưu active target hoặc checkpoint theo lượt. Chat chỉ giúp tìm nguồn, không thay nội dung hiện hành.

Nguồn function list/WBS/estimation và allocation áp dụng [scope checkpoint](source-scope-and-decomposition-checkpoint.md). Không biến số dòng nguồn thành số Epic/Story đã được duyệt. Resume đọc lại target/dependency để phát hiện stale evidence; không suy approval từ tracker cũ.

## Verbs & Write Boundaries

| Verb | Được ghi khi được giao | Giới hạn |
|---|---|---|
| setup/define/specify/design/prepare | Artifact canonical hiện hành trong scope | Không tự approve hoặc mở rộng business policy |
| review/check | Kết quả hiện hành theo target/scope, findings và witness | Không sửa source target đang kiểm |
| assess | Impact assessment và correction/revalidation plan hiện hành | Không tự áp dụng proposed change vào spec |

Read-only/status trả chat. Sửa target bằng workflow tác giả riêng khi được giao. Không tự commit/merge/push, post comment, tạo ticket hoặc thao tác CI. Prototype author được ghi HTML/CSS/JS fixture trong category được giao; product code và QA runtime thuộc tuyến khác.

## Review & Gate Semantics

Dùng verdict Đạt/Không đạt/Chưa kiểm/N/A theo target/scope/revision. Full review xét catalog và Q01–Q07; Task dùng T01–T08/SMART. Thiếu input/authority ghi Chưa kiểm; có counterexample/gap ghi Không đạt; N/A có lý do. Không lấy điểm trung bình để bù blocker.

Tự chuyển profile vẫn là self-check, không independent review. Approval, QA verdict, PM closure và Business acceptance phải có evidence thật. Kit lint/validator không thay thẩm quyền hoặc runtime. Readiness kiểm trực tiếp hồ sơ/revision/dependency hiện hành; không có gate chuẩn bị Baseline package hoặc merge bắt buộc mặc định. Policy dự án yêu cầu external action thì kiểm evidence thật.

## Artifact Writing

Áp dụng [writing standard](artifact-writing-standard.md), schema/IDs/catalog và [current-state policy](current-state-and-history.md). Mỗi đối tượng giữ một ID/path; mỗi target/scope review có một kết quả hiện hành. Không tạo file theo đợt/r1/r2 hoặc nối timeline. Lịch sử và lý do qua Git khi commit được giao; không tự commit để giả lập persistence.

Giữ business content rõ trước metadata; tiếng Việt đầy đủ, links có nhãn có nghĩa và heading Unicode NFC. Không thay source/gate semantics bằng format đẹp. Evidence cũ không áp dụng cho target đổi; review lại, không refresh hash để giữ verdict.

## Output & Handoff

Trả output/artifact refs, function/target/scope/revision, observed checks, gaps, missing authority và next action theo độ sâu nhiệm vụ. Không bắt form dài cho recap. Handoff là refs tới dữ liệu hiện hành; không sinh checkpoint/history artifact sau mỗi lượt.

Phân biệt output prepared, review performed, authority approved và actual action confirmed. Khi commit được giao, đọc [commit policy](commit-message-policy.md), inspect staged diff, validate message và kiểm message thực tế sau commit. Không bypass hooks/CI hoặc ghi Validation không có evidence. Không tự bật hook/remote gate chỉ vì vừa author spec.
