# Installation Feedback Assessment

ID: **CRM-INSTALL-ASSESSMENT** · CRM Workflow Kit 1.5.0 · 03/11/2026

Ngày 03/11/2026, tác giả đọc bản cài crm-docs: wrapper crm-spec-kit trỏ sang vendor riêng; project-binding chứa Phase 3 paths/sources; có internal symlink Claude skills và các shared-instruction modifications chưa commit. Chỉ đọc để đối chiếu; các file đó không bị chỉnh/undo/commit trong đợt này.

1.5.0 đưa helper/scaffold/config vào nguồn chuẩn và sinh một installed package tự chứa. Không vendor SKILL lồng, không sửa global AGENTS/rules, không bắt symlink. Cấu hình repo ở ngoài package; cập nhật có receipt/drift check/backup. Context tối thiểu thay chuỗi đọc lặp, refs mở rộng theo nhu cầu. Lint có schema cho artifact mới và legacy audit có giới hạn.

Hai phiên cài thử trong feedback là evidence được người dùng cung cấp; không tuyên bố đã replay các model/tool sessions đó. Actual discovery trên Antigravity/Claude/Windows phải kiểm bằng fresh-session smoke test; filesystem tests không thay được runtime proof. Lỗi import CLAUDE/AGENTS thuộc host repo cần scope migration riêng, không được sửa âm thầm bởi installer.

Các assumptions về skill locations/instruction loading dựa trên [Claude Skills](https://code.claude.com/docs/en/skills), [Claude Memory](https://code.claude.com/docs/en/memory) và [Antigravity Skills](https://antigravity.google/docs/skills) đã đọc ngày 03/11/2026. Adapters chỉ bố trí package; không nâng instruction priority và không tự cấp quyền.
