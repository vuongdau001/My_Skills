# Kết quả kiểm tra gói CRM 1.2.0

Ngày: 02/11/2026. Đây là kiểm tra do agent triển khai thực hiện, gồm kiểm tự động và walkthrough tài liệu; không phải forward-test độc lập bằng agent khác hoặc nghiệm thu trên hệ thống CRM thật.

## Kiểm tự động đã thực hiện

- Validator của gói: cấu trúc, ID/catalog, đường dẫn/anchor, manifest và ánh xạ 105 section nguồn đạt.
- Validator `quick_validate.py` của skill-creator: frontmatter/tên/cấu trúc entrypoint đạt.
- Hash snapshot đối chiếu đúng hai nguồn trước khi chuyển trang gốc thành điều hướng.
- Mười inventory/model procedures/exit criteria đã chuyển nguyên nội dung sang D01–D10; kiểm đối chiếu từng cell với snapshot đạt.
- Portable copy in another directory: PASS
- Duplicate manifest ID detected: PASS
- Broken local link detected: PASS
- Broken anchor detected: PASS
- Malformed nested link detected: PASS
- Missing source mapping detected: PASS
- Missing Task template detected: PASS
- Machine-specific path detected: PASS

## Walkthrough nội dung

Đã đối chiếu các tình huống của [acceptance scenarios](../references/pack-acceptance-scenarios.md) với tuyến đọc trong entrypoint và các quy tắc dưới đây. “Khớp” chỉ là kết luận về tính nhất quán của hướng dẫn, không nói rằng một agent hoặc Jira đã thực thi thành công.

| Scenario | Kết quả quan sát từ tài liệu | Evidence quy tắc | Kết luận |
|---|---|---|---|
| AT01 — Story không Task | DoR không đòi Task; hướng dẫn cho phép checklist | [Story](../references/story-specification-catalog.md), [decomposition](../references/backlog-hierarchy-and-decomposition.md) | Khớp |
| AT02 — Thiếu rule chống trùng | Q02 giữ gap chặn; Task không bù thiếu requirement | [Q02](../references/checks/requirements-completeness.md), [Task](../references/task-planning-and-completion.md) | Khớp |
| AT03 — Chia theo FE/BE/test | Review lại outcome; dùng Task khi cần chia lớp kỹ thuật | [Phân rã](../references/backlog-hierarchy-and-decomposition.md) | Khớp |
| AT04 — Baseline một phần Epic | Cho phép scope độc lập, shared rule ảnh hưởng phải rõ | [Baseline](../references/baseline-and-change-control.md#workflow-4-3) | Khớp |
| AT05 — Task đổi quyền/contract | Trả về change control và authority, không tự quyết | [Task](../references/task-planning-and-completion.md), [change](../references/baseline-and-change-control.md#workflow-14) | Khớp |
| AT06 — Task Done, AC fail | Story DoD yêu cầu AC tích hợp và QA evidence | [Story DoD](../references/readiness-completion-and-approval-gates.md#workflow-9-4) | Khớp |
| AT07 — Sai revision | Q05/hard gate kiểm target và version, không chỉ URL tồn tại | [Q05](../references/checks/traceability-and-versioning.md) | Khớp |
| AT08 — Review một model | Targeted review không kết luận toàn bộ | [Review](../references/requirements-review-process-and-verdicts.md) | Khớp |
| AT09 — AI điền đủ template | Thiếu authority không qua Q01/gate | [Q01](../references/checks/adequacy-and-necessity.md) | Khớp |
| AT10 — Migration dùng chung | Một Task nhiều dependency links; effort một lần | [Reporting](../references/jira-status-and-progress-reporting.md) | Khớp |
| AT11 — Portable copy | Sao chép sang đường dẫn khác và chạy validator đạt | Kiểm tự động nêu trên | Đạt cấu trúc; chưa thử mọi agent runtime |
| AT12 — Bảng 20 ô nhưng còn unknown | Ví dụ giữ retention/key limit chưa quyết và authority giả định | [Finding](../references/examples/review-findings-and-counterexamples.md), [spec ví dụ](../references/examples/project-code-request-specification.md) | Khớp |
| AT13 — Sửa copy UI | Applicability có reason; không ép mọi model/sơ đồ | [Epic catalog](../references/epic-specification-catalog.md) | Khớp |
| AT14 — Flow/quyền mâu thuẫn | Q03 có thao tác so cùng điều kiện và đóng finding sau sửa các representation | [Q03](../references/checks/cross-model-consistency.md) | Khớp |
| AT15 — Kế thừa baseline | Story dẫn subset/version, không tạo bản sao rule | [Story catalog](../references/story-specification-catalog.md) | Khớp |
| AT16 — Evidence cũ | Evidence đúng build/revision; delta cần impact/review | [Handoff](../references/ai-handoff-and-hard-gates.md), [change](../references/baseline-and-change-control.md#workflow-14) | Khớp |

## Phần chưa được kiểm bằng lần đóng gói này

Không có pilot trên Epic/Story CRM thật, không có xác nhận authority nghiệp vụ thật, không truy cập tenant Jira/Git/CI và không cấu hình runtime skill/hook. Validator không xác minh HTTP nguồn ngoài, không đo chất lượng yêu cầu hay chạy test sản phẩm. Các giới hạn này được ghi trong entrypoint và tài liệu gate để tránh nhầm chứng cứ.

Snapshot và [migration map](source-to-reference-migration-map.md) là cơ sở audit việc tách tài liệu. Khi sửa quy tắc hoặc routing, chạy lại kiểm cấu trúc và walkthrough các scenario bị ảnh hưởng.
