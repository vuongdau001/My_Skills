# Bản đồ chuyển nội dung nguồn sang gói CRM

Gói 1.2.0 giữ snapshot nguyên bản hai MD 1.1 trước khi thay trang gốc thành điều hướng. Nguồn toàn vẹn và hash từng section có trong [manifest](../reference-manifest.json); [snapshot ZIP](original-epic-story-standard-and-workflow-v1.1.zip) là lịch sử, không là policy hiện hành.

Các section được giữ nội dung và chuyển liên kết. Metadata cũ thay bằng trạng thái gói; quy ước Task cập nhật theo quyết định người dùng. Bảng inventory §3.11 chuyển các dòng chi tiết về từng model D01–D10; coverage giữ index. §12 nguồn đặc tả đổi thành hướng dẫn pilot vì gói đã được tạo. Các bổ sung hierarchy/Task/gate/examples ghi rõ là CRM tailoring.

| Nguồn / section | Nội dung | Vị trí hiện hành | Cách chuyển |
|---|---|---|---|
| spec §preamble | Thông tin kiểm soát tài liệu nguồn | [Mở nội dung](../references/crm-project-rules.md#spec-preamble) | source-metadata-archived-current-metadata-replaced |
| spec §1 | Nguyên tắc sử dụng | [Mở nội dung](../references/crm-project-rules.md#spec-1) | retained-and-relinked |
| spec §2 | Cơ sở chuẩn và cách áp dụng | [Mở nội dung](../references/standards-and-crm-tailoring.md#spec-2) | retained-and-relinked |
| spec §3 | Cách kết luận một hạng mục đã đạt | [Mở nội dung](../references/requirements-review-process-and-verdicts.md#spec-3) | retained-and-relinked |
| spec §3.1 | Cấu trúc review dùng chung | [Mở nội dung](../references/requirements-review-process-and-verdicts.md#spec-3-1) | retained-and-relinked |
| spec §3.2 | Bảy nhóm kiểm thực hành và phạm vi nguồn tham khảo | [Mở nội dung](../references/requirements-review-process-and-verdicts.md#spec-3-2) | retained-and-relinked |
| spec §3.3 | Chuẩn bị review và quy tắc kết luận | [Mở nội dung](../references/requirements-review-process-and-verdicts.md#spec-3-3) | retained-and-relinked |
| spec §3.4 | Q01 — Kiểm đúng nhu cầu và sự cần thiết | [Mở nội dung](../references/checks/adequacy-and-necessity.md#spec-3-4) | retained-and-relinked |
| spec §3.5 | Q02 — Kiểm đầy đủ ở hai mức | [Mở nội dung](../references/checks/requirements-completeness.md#spec-3-5) | retained-and-relinked |
| spec §3.6 | Q03 — Kiểm nhất quán giữa các phát biểu và mô hình | [Mở nội dung](../references/checks/cross-model-consistency.md#spec-3-6) | retained-and-relinked |
| spec §3.7 | Q04 — Kiểm khả năng kiểm chứng | [Mở nội dung](../references/checks/requirements-verifiability.md#spec-3-7) | retained-and-relinked |
| spec §3.8 | Q05 — Kiểm truy vết, phiên bản và khả năng sửa đổi | [Mở nội dung](../references/checks/traceability-and-versioning.md#spec-3-8) | retained-and-relinked |
| spec §3.9 | Q06 — Kiểm không mơ hồ và một nghĩa chấp nhận rõ | [Mở nội dung](../references/checks/clarity-and-unambiguity.md#spec-3-9) | retained-and-relinked |
| spec §3.10 | Q07 — Kiểm khả thi và đúng mức bàn giao | [Mở nội dung](../references/checks/feasibility-and-handoff-readiness.md#spec-3-10) | retained-and-relinked |
| spec §3.11 | Cách xác định mẫu số và điều kiện dừng theo loại hồ sơ | [Mở nội dung](../references/coverage-inventories-and-traceability.md#spec-3-11) | single-model-index-and-denominator-guidance-detail-in-models |
| spec §3.12 | Ví dụ kiểm đủ state transition: từ nhận xét tới finding có căn cứ | [Mở nội dung](../references/examples/review-findings-and-counterexamples.md#spec-3-12) | retained-and-relinked |
| spec §3.13 | Mẫu record review để member thực hiện nhất quán | [Mở nội dung](../assets/templates/requirements-review-record-template.md#spec-3-13) | retained-and-relinked |
| spec §4 | Epic cần làm rõ những hạng mục nào? | [Mở nội dung](../references/epic-specification-catalog.md#spec-4) | retained-and-relinked |
| spec §5 | Story cần đầy đủ những hạng mục nào? | [Mở nội dung](../references/story-specification-catalog.md#spec-5) | retained-and-relinked |
| spec §6 | Hướng dẫn chi tiết cho từng loại mô hình/hồ sơ | [Mở nội dung](../references/coverage-inventories-and-traceability.md#spec-6) | empty-source-heading-replaced-by-model-index-at-preserved-anchor |
| spec §D01 | Flow, use case và swimlane | [Mở nội dung](../references/models/business-flows-and-use-cases.md#spec-d01) | retained-and-relinked |
| spec §D02 | State transition và vòng đời nghiệp vụ | [Mở nội dung](../references/models/business-state-transitions.md#spec-d02) | retained-and-relinked |
| spec §D03 | Business rules và decision table | [Mở nội dung](../references/models/business-rules-and-decision-tables.md#spec-d03) | retained-and-relinked |
| spec §D04 | Data dictionary, validation và ranh giới dữ liệu | [Mở nội dung](../references/models/data-dictionary-and-validation.md#spec-d04) | retained-and-relinked |
| spec §D05 | Permission matrix và phạm vi dữ liệu | [Mở nội dung](../references/models/permissions-and-data-access.md#spec-d05) | retained-and-relinked |
| spec §D06 | UI/UX và quan hệ với contract | [Mở nội dung](../references/models/ui-behavior-and-interaction-states.md#spec-d06) | retained-and-relinked |
| spec §D07 | API/integration contract và sequence | [Mở nội dung](../references/models/api-and-integration-contracts.md#spec-d07) | retained-and-relinked |
| spec §D08 | Exception, edge case và tính nhất quán khi có lỗi | [Mở nội dung](../references/models/exceptions-and-edge-cases.md#spec-d08) | retained-and-relinked |
| spec §D09 | NFR, migration và điều kiện vận hành | [Mở nội dung](../references/models/nonfunctional-migration-and-operations.md#spec-d09) | retained-and-relinked |
| spec §D10 | Solution, decomposition và testability | [Mở nội dung](../references/models/solution-and-story-decomposition.md#spec-d10) | retained-and-relinked |
| spec §7 | AC, scenario và kiểm tra coverage trước khi bàn giao | [Mở nội dung](../references/coverage-inventories-and-traceability.md#spec-7) | retained-and-relinked |
| spec §7.1 | Mẫu AC có thể kiểm chứng | [Mở nội dung](../references/coverage-inventories-and-traceability.md#spec-7-1) | retained-and-relinked |
| spec §7.2 | Chuỗi truy vết và bảng coverage | [Mở nội dung](../references/coverage-inventories-and-traceability.md#spec-7-2) | retained-and-relinked |
| spec §7.3 | Kiểm theo từng loại coverage | [Mở nội dung](../references/coverage-inventories-and-traceability.md#spec-7-3) | retained-and-relinked |
| spec §8 | Quy trình review: bảo đảm nội dung được xác nhận bởi đúng người | [Mở nội dung](../references/requirements-review-process-and-verdicts.md#spec-8) | retained-and-relinked |
| spec §8.1 | Cổng trước tạo Story và cổng trước code | [Mở nội dung](../references/requirements-review-process-and-verdicts.md#spec-8-1) | retained-and-relinked |
| spec §8.2 | Kiểm máy được và phần cần con người | [Mở nội dung](../references/requirements-review-process-and-verdicts.md#spec-8-2) | retained-and-relinked |
| spec §9 | Ví dụ liên kết Epic → Story → model → AC → test condition | [Mở nội dung](../references/examples/project-code-request-specification.md#spec-9) | retained-and-relinked |
| spec §9.1 | Epic: Gửi và xét duyệt yêu cầu mở mã dự án | [Mở nội dung](../references/examples/project-code-request-specification.md#spec-9-1) | retained-and-relinked |
| spec §9.2 | Business state và transition | [Mở nội dung](../references/examples/project-code-request-specification.md#spec-9-2) | retained-and-relinked |
| spec §9.3 | Story: Owner gửi draft để chờ duyệt | [Mở nội dung](../references/examples/project-code-request-specification.md#spec-9-3) | retained-and-relinked |
| spec §9.4 | Vì sao ví dụ này rõ hơn một Story chỉ có mô tả? | [Mở nội dung](../references/examples/project-code-request-specification.md#spec-9-4) | retained-and-relinked |
| spec §10 | Mẫu cấu trúc hồ sơ để sử dụng | [Mở nội dung](../assets/templates/epic-specification-template.md#spec-10) | retained-and-relinked |
| spec §10.1 | Epic specification | [Mở nội dung](../assets/templates/epic-specification-template.md#spec-10-1) | retained-and-relinked |
| spec §10.2 | Story specification | [Mở nội dung](../assets/templates/story-specification-template.md#spec-10-2) | retained-and-relinked |
| spec §11 | Ví dụ cách kết luận review đạt hoặc chưa đạt | [Mở nội dung](../references/examples/review-findings-and-counterexamples.md#spec-11) | retained-and-relinked |
| spec §12 | Các quyết định cần thống nhất trước khi thiết kế skill | [Mở nội dung](../references/pack-acceptance-scenarios.md#spec-12) | updated-to-pilot-guidance-after-pack-creation |
| workflow §preamble | Thông tin kiểm soát tài liệu nguồn | [Mở nội dung](../references/crm-project-rules.md#workflow-preamble) | source-metadata-archived-current-metadata-replaced |
| workflow §1 | Mục tiêu và các quy ước đầu vào | [Mở nội dung](../references/crm-project-rules.md#workflow-1) | retained-and-relinked |
| workflow §1.1 | Những thông tin đã được người quản lý dự án cung cấp | [Mở nội dung](../references/crm-project-rules.md#workflow-1-1) | retained-and-relinked |
| workflow §1.2 | Quan hệ với các tài liệu trước | [Mở nội dung](../references/crm-project-rules.md#workflow-1-2) | retained-and-relinked |
| workflow §2 | Định nghĩa: Requirement, AC, DoR, DoD và Baseline | [Mở nội dung](../references/crm-project-rules.md#workflow-2) | retained-and-relinked |
| workflow §2.1 | Cách phân biệt AC, DoR và DoD | [Mở nội dung](../references/crm-project-rules.md#workflow-2-1) | retained-and-relinked |
| workflow §3 | Phân loại và phân cấp requirement | [Mở nội dung](../references/backlog-hierarchy-and-decomposition.md#workflow-3) | retained-and-relinked |
| workflow §3.1 | Phân loại theo bản chất nội dung | [Mở nội dung](../references/backlog-hierarchy-and-decomposition.md#workflow-3-1) | retained-and-relinked |
| workflow §3.2 | Phân cấp theo phạm vi và công việc | [Mở nội dung](../references/backlog-hierarchy-and-decomposition.md#workflow-3-2) | retained-and-relinked |
| workflow §4 | Baseline của cái gì? | [Mở nội dung](../references/baseline-and-change-control.md#workflow-4) | retained-and-relinked |
| workflow §4.1 | Câu phải dùng trước khi tạo Story | [Mở nội dung](../references/baseline-and-change-control.md#workflow-4-1) | retained-and-relinked |
| workflow §4.2 | Phân biệt ba tập nội dung được chốt ở ba thời điểm | [Mở nội dung](../references/baseline-and-change-control.md#workflow-4-2) | retained-and-relinked |
| workflow §4.3 | Phạm vi của một baseline | [Mở nội dung](../references/baseline-and-change-control.md#workflow-4-3) | retained-and-relinked |
| workflow §5 | Bộ hồ sơ phải review và merge trước khi tạo Story | [Mở nội dung](../references/baseline-and-change-control.md#workflow-5) | retained-and-relinked |
| workflow §5.1 | Cấu trúc lưu trữ đề xuất | [Mở nội dung](../references/baseline-and-change-control.md#workflow-5-1) | retained-and-relinked |
| workflow §5.2 | Ví dụ manifest trước khi tạo Story | [Mở nội dung](../references/baseline-and-change-control.md#workflow-5-2) | retained-and-relinked |
| workflow §6 | Quy trình từ Feature đến Story thực thi | [Mở nội dung](../references/baseline-and-change-control.md#workflow-6) | retained-and-relinked |
| workflow §7 | DoR, AC và DoD của Feature | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-7) | retained-and-relinked |
| workflow §7.1 | DoR để bắt đầu làm rõ/phân rã Feature | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-7-1) | retained-and-relinked |
| workflow §7.2 | AC cấp Feature | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-7-2) | retained-and-relinked |
| workflow §7.3 | Hoàn tất phân tích Feature và DoD bàn giao Feature là hai mốc | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-7-3) | retained-and-relinked |
| workflow §8 | DoR, AC và DoD của Epic | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-8) | retained-and-relinked |
| workflow §8.1 | DoR để bắt đầu làm rõ Epic: `todo` → `inprogress` | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-8-1) | retained-and-relinked |
| workflow §8.2 | Điều kiện Epic được phép sinh Story thực thi | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-8-2) | retained-and-relinked |
| workflow §8.3 | AC cấp Epic | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-8-3) | retained-and-relinked |
| workflow §8.4 | DoD để đóng Epic: `inprogress` → `done` | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-8-4) | retained-and-relinked |
| workflow §9 | DoR, AC và DoD của Story | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-9) | retained-and-relinked |
| workflow §9.1 | DoR để bắt đầu triển khai: `todo` → `inprogress` | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-9-1) | retained-and-relinked |
| workflow §9.2 | AC của Story | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-9-2) | retained-and-relinked |
| workflow §9.3 | Điều kiện Dev bàn giao QA: `inprogress` → `resolved` | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-9-3) | retained-and-relinked |
| workflow §9.4 | DoD đóng Story: `resolved` → `done` | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-9-4) | retained-and-relinked |
| workflow §10 | DoR và DoD của Task theo loại đầu ra | [Mở nội dung](../references/task-planning-and-completion.md#workflow-10) | retained-and-relinked |
| workflow §10.1 | DoR dùng chung: `todo` → `inprogress` | [Mở nội dung](../references/task-planning-and-completion.md#workflow-10-1) | retained-and-relinked |
| workflow §10.2 | DoD dùng chung | [Mở nội dung](../references/task-planning-and-completion.md#workflow-10-2) | retained-and-relinked |
| workflow §10.3 | DoD bổ sung theo đầu ra triển khai | [Mở nội dung](../references/task-planning-and-completion.md#workflow-10-3) | retained-and-relinked |
| workflow §10.4 | Hoạt động refinement và trường hợp nghiên cứu độc lập | [Mở nội dung](../references/task-planning-and-completion.md#workflow-10-4) | retained-and-relinked |
| workflow §11 | Ý nghĩa từng status Jira và quy tắc chuyển | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-11) | retained-and-relinked |
| workflow §11.1 | Epic | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-11-1) | retained-and-relinked |
| workflow §11.2 | Story | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-11-2) | retained-and-relinked |
| workflow §11.3 | Task | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-11-3) | retained-and-relinked |
| workflow §11.4 | Dùng `pending`, trả sửa và `cancel` | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-11-4) | retained-and-relinked |
| workflow §11.5 | Status `resolved` khác trường Resolution của Jira | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-11-5) | retained-and-relinked |
| workflow §12 | Ai review và ai có quyền chốt? | [Mở nội dung](../references/readiness-completion-and-approval-gates.md#workflow-12) | retained-and-relinked |
| workflow §13 | Bàn giao baseline cho người và AI như thế nào? | [Mở nội dung](../references/ai-handoff-and-hard-gates.md#workflow-13) | retained-and-relinked |
| workflow §13.1 | Sau merge, trước và sau tạo ticket | [Mở nội dung](../references/ai-handoff-and-hard-gates.md#workflow-13-1) | retained-and-relinked |
| workflow §13.2 | Bộ context tối thiểu cho Dev/QA/AI | [Mở nội dung](../references/ai-handoff-and-hard-gates.md#workflow-13-2) | retained-and-relinked |
| workflow §13.3 | Gate kiểm bằng máy | [Mở nội dung](../references/ai-handoff-and-hard-gates.md#workflow-13-3) | retained-and-relinked |
| workflow §14 | Thay đổi sau baseline | [Mở nội dung](../references/baseline-and-change-control.md#workflow-14) | retained-and-relinked |
| workflow §15 | Theo dõi Requirement Backlog và Development Backlog | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-15) | retained-and-relinked |
| workflow §15.1 | Requirement Backlog | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-15-1) | retained-and-relinked |
| workflow §15.2 | Development Backlog | [Mở nội dung](../references/jira-status-and-progress-reporting.md#workflow-15-2) | retained-and-relinked |
| workflow §16 | Ví dụ đi hết một vòng: baseline cụ thể của phần manual | [Mở nội dung](../references/examples/baseline-to-delivery-walkthrough.md#workflow-16) | retained-and-relinked |
| workflow §16.1 | Feature và Epic | [Mở nội dung](../references/examples/baseline-to-delivery-walkthrough.md#workflow-16-1) | retained-and-relinked |
| workflow §16.2 | Đầu ra phân tích và solution | [Mở nội dung](../references/examples/baseline-to-delivery-walkthrough.md#workflow-16-2) | retained-and-relinked |
| workflow §16.3 | PR phải chứa gì? | [Mở nội dung](../references/examples/baseline-to-delivery-walkthrough.md#workflow-16-3) | retained-and-relinked |
| workflow §16.4 | Sau merge và khi triển khai | [Mở nội dung](../references/examples/baseline-to-delivery-walkthrough.md#workflow-16-4) | retained-and-relinked |
| workflow §17 | Checklist trước khi áp dụng | [Mở nội dung](../references/pack-acceptance-scenarios.md#workflow-17) | retained-and-relinked |
| workflow §18 | Tài liệu tham khảo | [Mở nội dung](../references/standards-and-crm-tailoring.md#workflow-18) | retained-and-relinked |

## Điều chỉnh mapping trong gói 1.3

Giữ nguyên ZIP/hash và 105 section nguồn. `spec-3-11` nay dẫn tới hướng dẫn xác định mẫu số cùng bảng model duy nhất; các inventory/procedure/exit criteria vẫn ở D01–D10. `spec-6` dẫn ngay tới bảng chọn model, thay heading rỗng. ID/anchor cũ vẫn resolve; manifest ghi disposition mới. Bổ sung Feature/policy/mapping/measurement/ID/pilot là CRM tailoring ngày 03/11/2026, không được gán ngược là nội dung nguồn 1.1.

## Hiệu chỉnh ví dụ và policy refs — 1.3.1

Các ví dụ đang dùng đã chuyển sang PREFIX-CRM-NNN, gồm logical IDs, BR/AC và MOD với kind rõ; mọi ref/path trong ví dụ được cập nhật cùng nhau. Customer AC dùng AC-CRM-001 đến 003; submit AC dùng AC-CRM-101 đến 108 để không trùng namespace. Transition items dùng MOD-CRM-001 đến 004; decision-rule items dùng MOD-CRM-101 đến 109. Đây là đổi định danh ví dụ, không đổi hành vi và không áp dụng lên ID Jira hoặc hồ sơ CRM thật. Snapshot 1.1 và source hashes giữ nguyên; mã cũ vẫn có thể thấy trong lịch sử.

Checklist DoD Story dẫn trực tiếp POL-SEVERITY/POL-QUALITY; Dev handoff dẫn POL-CHECKS/POL-QUALITY. Các link là hướng dẫn chọn policy, còn gate cần ref/version/approval policy dự án thật.
