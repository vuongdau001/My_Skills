# CRM Workflow Kit 2.1.0 — Truy vết Use Case qua Epic

Ngày kiểm 06/11/2026.

## Thay đổi phát hành

Mỗi Epic cấp một `EPIC-CRM-*` ID. Metadata `use_case` ghi level và locator E03. Story, AC, Prototype và gói bàn giao dùng Epic ID, revision và anchor khi truy vết hành vi. Anchor thuộc file Epic. Namespace MOD tiếp tục dành cho model và model item. [Policy Epic–Use Case](../references/epic-use-case-policy.md).

Lint đọc binding MOD đã có và ghi cảnh báo để áp dụng quy ước mới khi chỉnh revision. Cơ chế pin và truy vết evidence của revision cũ vẫn dùng được. [Metadata và lint](../references/artifact-metadata-and-lint.md).

## Kiểm chứng

| Phép kiểm | Kết quả |
|---|---|
| Validator package | Đạt. 118 tài liệu Markdown, 171 mục registry, 105 mục nguồn lịch sử, 5 profiles và 13 workflow functions. |
| Unit/integration suite | 175 test đạt. |
| Epic và Story | Metadata schema 1/2 đọc được binding chỉ có level và locator. Story dẫn Epic ID tới anchor E03. Lint phát hiện anchor thiếu, anchor ngoài E03, revision cũ và Epic ID trùng xuyên workstream. |
| Prototype | Scenario pin Epic ID, anchor và revision của allocation. Test kiểm anchor sai, revision cũ và evidence walkthrough đúng scope. |
| Binding đã cấp MOD ID | Story và Prototype tiếp tục đọc được trace đúng revision. Lint cảnh báo định dạng cũ và vẫn kiểm ownership, anchor cùng ID trùng. |
| Cài thử 2.1.0 trên repo tạm | Doctor đạt. Context nạp mẫu Epic mới. Story cùng lúc dùng `parent` tới file Epic và `derived-from` tới anchor E03. Readiness lint đạt với revision đúng và bắt lỗi revision cũ. |

Phạm vi kiểm gồm cấu trúc, trace và tương thích của tooling trên bản cài thử. [Ca kiểm UL01–UL03](../references/pack-acceptance-scenarios.md).
