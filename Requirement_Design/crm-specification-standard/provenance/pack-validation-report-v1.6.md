# Codex Bootstrap Validation Report 1.6

Version: 1.6.0 · Date: 04/11/2026

## Changes and compatibility contract

Thêm --agent codex dùng chung physical package với antigravity; default antigravity và both = Antigravity + Claude giữ nguyên. Config schema 1, public skill name, 13 functions, 5 logical profiles và catalogs/models/checks nghiệp vụ không đổi.

BOOTSTRAP hướng dẫn agent khảo sát/chọn tham số rồi gọi helper. Root router là Codex opt-in --with-router: chỉ tạo AGENTS.md chưa có, giữ instructions có sẵn và in snippet đề xuất, nhận biết override/symlink/protected paths. Other adapters không tự sửa root. Root AGENTS có thể được tool khác đọc nên opt-in này vẫn cần đối chiếu quy tắc repo, không cam kết vô hình với mọi runtime.

Doctor --agent kiểm adapter được chọn; doctor không --agent giữ all-copy/drift audit cũ. smoke-prompt sinh read-only prompt + evidence template, không mở phiên/model hoặc tự xác nhận discovery.

## Verification

- 71/71 unittest đạt: 47 regression tests trước đó + 24 Codex/bootstrap compatibility tests. Fixture update target đổi từ 1.5.1 sang 1.6.1 để tiếp tục kiểm đúng new-version update; các test cũ còn lại giữ nguyên.
- Structural validator đạt: 87 Markdown documents, 138 manifest entries, 105 source sections, 5 profiles, 13 workflow functions. Skill-creator quick validation đạt.
- Các test mới kiểm byte-identical alias Codex/Antigravity; legacy defaults/both; router opt-in/dry-run/idempotence/preserve-existing/override/symlink/read-only protection; selected doctor và all-copy drift audit; smoke prompt readonly, missing input/kind/receipt và hai adapter khác; internal Claude alias giữ một package.
- Hash audit xác nhận workflows, profiles và toàn bộ references nghiệp vụ giữ nguyên. Sáu file cũ thay đổi có chủ đích: SKILL.md, START-HERE.md, INSTALL.md, reference-manifest.json, scripts/kit.py, scripts/tests/test_installation_tooling.py. Năm file thêm: BOOTSTRAP, hai installation templates, test Codex và report này.
- Bản integration CRM trước đó được kiểm read-only: cả 130 file package/config/router/pilot giữ nguyên hash. Doctor từ nguồn mới với --agent codex đọc được bản cài 1.5 và trả healthy=true; root router tùy biến của repo được báo cần review do không chứa exact snippet mới, không tự sửa hoặc kết luận router sai.

Filesystem tests không chứng minh runtime UI discovery, semantic approval, Windows native hoặc Git/Jira/CI hard gate. smoke-prompt không gọi model hoặc desktop runtime; mọi evidence template giữ runtime_verified=false cho tới khi được xác nhận bằng quan sát thực tế.

## Distribution and migration

Bản cài 1.5 đang có trong repo CRM không bị tự cập nhật; update là tác vụ riêng theo receipt/drift/backup mechanism. Router là repo-owned instructions, không thuộc package update và không tự merge vào file có sẵn. Không commit/push, đổi global config hoặc nâng CLI.

Tham khảo [BOOTSTRAP](../BOOTSTRAP.md) và [INSTALL](../INSTALL.md).
