# Bootstrap CRM Spec Kit cho AI tools

ID: CRM-BOOTSTRAP · CRM Workflow Kit 2.0.1 · 06/11/2026

Điểm vào khi người dùng đưa folder kit và yêu cầu cài vào một repo. AI khảo sát repo, chọn tham số và gọi helper; đường dẫn cài, copy/receipt, config/scaffold và update do helper thực hiện. Không tự dựng wrapper, sửa bản cài hoặc tạo bản nội dung riêng cho mỗi tool.

## Khảo sát trước khi ghi

1. Đọc instruction files áp dụng, config kit nếu có, các skills đã cài và vị trí output/source hiện hành. Đọc [INSTALL](INSTALL.md) cho cơ chế và giới hạn.
2. Xác định tool từ ngữ cảnh người dùng/runtime, không chỉ từ việc một executable tên codex có trong PATH. Chọn rõ codex, antigravity hoặc claude; both vẫn chỉ là hai filesystem adapters Antigravity + Claude như trước.
3. Xác định repo, workstream, spec_root và source refs. Tái dùng config hiện có. Nếu nhiều scope hoặc source authority hợp lý, hỏi phần ảnh hưởng quyết định; không hỏi lại fact đọc được trong repo. Source có nhãn Approved không tự là approval được kit xác minh.
4. Kiểm package có receipt hay không. Bản cũ khác version dùng update từ trusted source; folder cùng tên chưa có ownership cần migration, không ghi đè. Không tự nâng CLI hoặc đổi global instructions/config.

## Cài theo tool

| Tool được chọn | Tham số | Package path | Root instructions |
|---|---|---|---|
| Codex | --agent codex | .agents/skills/crm-spec-kit | Tùy chọn --with-router |
| Antigravity | --agent antigravity | .agents/skills/crm-spec-kit | Giữ hành vi cũ, không sửa root |
| Claude | --agent claude | .claude/skills/crm-spec-kit | Giữ hành vi cũ, không sửa root |
| Hai adapter cũ | --agent both | Hai path trên, deduplicate internal symlink | Giữ hành vi cũ |

Codex và Antigravity chia sẻ một package vật lý. Tên public là crm-spec-kit; nguồn vẫn crm-specification-standard. Không cài thêm crm-specification-standard vào cùng danh sách để tránh skill trùng capability. Cài một package không đồng nghĩa đã kiểm runtime trên tất cả tools nhìn thấy package đó.

Ví dụ chạy từ folder kit, thay placeholders bằng dữ liệu đã xác minh:

```text
python3 scripts/kit.py install --repo <repo-root> --agent codex --workstream p3 --spec-root phase-3/spec --source SRC-FL=phase-3/function-list.md --with-router
python3 scripts/kit.py install --repo <repo-root> --agent codex --workstream p3 --spec-root phase-3/spec --source SRC-FL=phase-3/function-list.md --with-router --apply
python3 scripts/kit.py doctor --repo <repo-root> --agent codex
```

Chạy dry-run, xem plan và conflicts, rồi apply trong scope người dùng đã giao. Không yêu cầu approval lần nữa chỉ vì có dry-run nếu người dùng đã cho cài với các thay đổi đó; conflicts thật hoặc thay đổi ngoài scope cần xử lý riêng.

Root router là tùy chọn riêng, không điều kiện bắt buộc để gọi skill. --with-router chỉ áp dụng Codex: root AGENTS.md chưa có thì tạo; instruction file có sẵn giữ nguyên và in snippet đề xuất, không tự merge. AGENTS.override.md có nội dung được xét trước vì có thể che AGENTS.md; symlink instruction cần kiểm riêng. Agent chỉ áp dụng snippet vào file có sẵn khi việc sửa instructions nằm trong quyền người dùng giao và đã đối chiếu quy tắc repo. Không copy nguyên persona DDD hoặc project phase vào router dùng lại.

Workstream mới mặc định numbered layout; config cũ thiếu layout giữ legacy. Lấy artifact_paths từ context; không đổi folder/pilot khi update package. Nếu user muốn chuyển cấu trúc, dùng plan-layout chỉ đọc theo [layout guide](references/artifact-layout-and-migration.md). Knowledge records mới cần helper 1.7, xem [record guide](references/knowledge-records-and-evidence.md).

## Smoke test và handoff

Từ package đã cài, sinh prompt cho một target thật:

```text
python3 scripts/kit.py smoke-prompt crm-check-readiness --repo <repo-root> --agent codex --workstream "<workstream-id>" --target "<story-id>" --target-kind Story --revision "<current-revision>"
```

Helper chỉ sinh prompt và evidence template; không mở phiên mới hoặc chạy workflow. Dùng prompt trong phiên mới của tool được chọn. Ghi tool/version, mode discovery, package/workstream/target/revision và observed output; phân biệt chọn skill thật với agent chỉ đọc SKILL theo đường dẫn. Nếu chưa quan sát phiên mới thì runtime Chưa kiểm. Doctor không đọc CLI version để tự kết luận desktop discovery.

Handoff gồm package/config/scaffold, router đã tạo hoặc snippet còn cần review, doctor warnings và runtime evidence/chỗ chưa kiểm. Không tự bắt đầu pilot nghiệp vụ, commit/push hoặc tạo ticket chỉ vì đã cài kit.

## Prompt người dùng có thể dùng lại

> Đọc BOOTSTRAP.md trong folder kit này và cài cho Codex trong repo đang mở, dùng workstream và nguồn tôi chỉ định. Khảo sát trước, dry-run rồi apply trong phạm vi cài đặt; giữ nguyên instructions có sẵn và báo conflicts. Chưa tạo artifact nghiệp vụ.

Platform facts được đối chiếu với [Codex Skills](https://learn.chatgpt.com/docs/build-skills) và [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Các URL là tài liệu tham khảo, không evidence runtime của repo người dùng.
