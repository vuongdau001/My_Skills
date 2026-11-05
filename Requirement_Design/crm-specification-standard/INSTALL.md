# Install and Operate CRM Spec Kit

ID: **CRM-INSTALL** · CRM Workflow Kit 1.10.0 · 05/11/2026

AI được đưa folder kit để tự cài đọc [BOOTSTRAP](BOOTSTRAP.md) trước. Nội dung/workflow dùng chung; filesystem adapters và router tùy chọn xử lý phần tích hợp tool.

## Packaging Contract

Nguồn phát triển là folder `crm-specification-standard`. Bản cài có một package tự chứa tên `crm-spec-kit`; helper thay **chỉ trường name của root SKILL** khi đóng gói. Không có wrapper/vendor hay SKILL lồng thứ hai. Registry, profiles, workflows và chuẩn nằm ngay trong package. Bản cài không được sửa trực tiếp; mọi thay đổi nguồn thực hiện ở upstream rồi update.

Config dự án ở `.agents/crm-spec-kit.json`, nằm ngoài package và do repo sở hữu. Spec artifacts ở spec_root của từng workstream. Receipt `crm-spec-kit-installation.json` ghi version/hash toàn bộ package đã cài; digest kiểm drift, không là chữ ký hoặc chứng nhận nguồn tin cậy.

## Bootstrap

Cần Python **3.11+**, chỉ stdlib, không pip/network. Từ folder nguồn kit đã tải hoặc clone, dùng:

```text
python3 scripts/kit.py install --repo <repo-root> --agent both --workstream p3 --spec-root phase-3/spec --source SRC-FL=phase-3/function-list.md
python3 scripts/kit.py install --repo <repo-root> --agent both --workstream p3 --spec-root phase-3/spec --source SRC-FL=phase-3/function-list.md --apply
python3 scripts/kit.py doctor --repo <repo-root>
```

Lệnh đầu dry-run; lệnh thứ hai mới ghi. `<repo-root>` là argument lúc chạy, không ghi absolute path đó vào config/artifacts. Chọn `--agent codex`, `antigravity`, `claude` hoặc `both`. Mặc định vẫn antigravity; both vẫn Antigravity + Claude, không đổi semantics. Nếu chưa biết repo/spec_root/source thì agent hỏi phần thực sự thiếu sau khi khảo sát; không giới hạn cứng số câu hỏi mà bỏ qua xung đột quyền hoặc scope.

Helper tạo package tại `.agents/skills/crm-spec-kit` cho Codex/Antigravity và/hoặc `.claude/skills/crm-spec-kit` cho Claude. Codex và Antigravity dùng cùng một package, không tạo copy trùng. Mặc định là **copy**, không tạo symlink. Package có .gitattributes giữ LF cho Markdown/JSON/Python và đánh dấu ZIP binary để receipt không lệch chỉ vì Git checkout đổi line ending; vẫn cần smoke test Windows native. Nếu repo đã có symlink nội bộ từ `.claude/skills` tới `.agents/skills`, helper resolve và chỉ cài một lần. Link trỏ ra ngoài repo bị từ chối. Mọi file của package được tìm từ `__file__`, không từ số tầng `../../vendor` hoặc thư mục làm việc.

Để chia sẻ kiểu “copy một folder”, copy **bản đã đóng gói** crm-spec-kit từ installation, gồm cả receipt, vào skills directory repo mới. Có thể chạy scripts/kit.py install ngay từ package đó để tạo config/scaffold; chỉ dùng slash command nếu công cụ đã nhận diện skill. Copy source nguyên bản crm-specification-standard vẫn dùng được bằng cách yêu cầu agent đọc SKILL/INSTALL, hoặc chạy bootstrap ở trên để sinh public package name.

Không chạy install đè lên folder skill chưa có ownership receipt; nếu folder đã có cùng tên, dừng và yêu cầu kiểm tra/migration. Không tự di chuyển bản cài cũ hoặc sửa shared AGENTS/rules có sẵn. Bản cài khác nội dung đóng gói (kể cả cùng version/manifest) phải dùng update; không sửa trực tiếp installation 1.5 để gắn thêm code 1.6.

## Codex và Root Router Tùy Chọn

```text
python3 scripts/kit.py install --repo <repo-root> --agent codex --workstream p3 --spec-root phase-3/spec --source SRC-FL=phase-3/function-list.md --with-router
python3 scripts/kit.py install --repo <repo-root> --agent codex --workstream p3 --spec-root phase-3/spec --source SRC-FL=phase-3/function-list.md --with-router --apply
python3 scripts/kit.py doctor --repo <repo-root> --agent codex
```

Không có --with-router thì không thay root instructions. Flag này chỉ dùng với --agent codex: root AGENTS.md chưa có thì tạo [router ngắn](assets/installation/codex-router.md) trong cùng operation/rollback của install; file có sẵn giữ nguyên, plan in `propose-router-addition` kèm snippet để agent/operator review. Không tự append/merge vào instructions có sẵn. Có exact snippet thì báo unchanged, không tự update nội dung repo khi kit thay template.

AGENTS.override.md không rỗng được xét trước AGENTS.md; helper không tạo router vào file bị override che. Root instruction symlink hoặc path không phải file bị từ chối ở bước opt-in, không theo link để sửa. Router không được tạo vào path source/read_only. Có snippet chưa chứng minh instruction precedence, semantic compatibility hoặc runtime discovery đã đúng. Scope/policy cấp cao hơn vẫn áp dụng. Root router có thể được tool khác cũng đọc AGENTS nhận thấy; vì vậy đây là opt-in repo change cần đối chiếu, không cam kết vô hình với tool khác.

## Config and Scaffold

Mẫu nền: [project config blueprint](assets/installation/project-config.template.json). Mỗi workstream có id/title, spec_root, optional input_root, sources với id/path/use và read_only. Tất cả path là repo-relative POSIX; không `..`, absolute path hoặc symlink thoát repo. spec_root không được chồng tool dirs, source/read_only của bất kỳ workstream nào hoặc spec_root khác. input_root cũng phải tránh mọi source/read_only. Namespace hiện hành là CRM theo bộ chuẩn; không đổi ngầm theo tên domain.

Scaffold mới mặc định numbered: `00-project`, `01-features`, `02-epics`, `03-stories`, `04-tasks`, `05-reviews`, `06-baselines`, `07-reports`, `08-pilot`. Project có các vùng 01-meetings/02-decisions/03-assumptions/04-constraints cho schema-2 records. Chọn --layout legacy khi cần tên cũ cho workstream mới. Workstream thiếu layout vẫn dùng tên cũ; install lại/update không tự migration hoặc thêm record_schema_version vào config cũ. Context trả artifact_paths; có thể override category paths có kiểm boundary/overlap. [Layout và migration](references/artifact-layout-and-migration.md) là quy ước canonical. Có thư mục tasks không có nghĩa phải tạo Task. Mỗi thư mục scaffold có marker .crm-spec-kit-keep để tồn tại sau git clone; không sinh artifact nghiệp vụ giả để lấp thư mục.

Scoped AGENTS/CLAUDE chỉ được tạo khi chưa có; file có sẵn được giữ và báo cần xem xét. Chúng hướng dẫn trong spec_root, không override instruction/policy cấp cao hơn. Mọi adapter vẫn tạo hai scoped files như 1.5 để giữ tương thích; chỉ root router mới là Codex opt-in. Không tự tạo file `.agents/rules` rồi tuyên bố mọi nền tảng sẽ nạp. Các thay đổi config để thêm workstream là cập nhật config kit có chủ đích; config fields/values cũ được giữ.

```text
python3 scripts/kit.py install --repo <repo-root> --workstream p4 --spec-root phase-4/spec --apply
```

Chạy lại install cho stream có sẵn không cần lặp --source/read-only. Muốn sửa config stream hiện tại: edit config của repo một cách có chủ đích rồi doctor; install không silently đổi sources hoặc root.

## Doctor and Fresh-session Check

Doctor kiểm config/boundaries/scaffold/sources, validator, package receipt/hash và git dirty state. Không truyền --agent thì giữ audit cả hai physical copies như 1.5, gồm drift giữa copies và WARN cho adapter không có. Truyền --agent chỉ kiểm adapter(s) được chọn, không cảnh báo thiếu adapter không dùng; selected adapter thiếu là ERROR. Codex/Antigravity chỉ cần scoped AGENTS, Claude chỉ cần scoped CLAUDE; both kiểm cả hai. --agent codex còn báo tình trạng root router tùy chọn; router thiếu/chưa có exact snippet chỉ WARN để review, không tự kết luận instructions sai. Khi cần kiểm drift mọi copies, chạy doctor không --agent.

ERROR dẫn exit 1; WARN không tự làm structural health fail, nhưng `runtime_verified` luôn false vì filesystem presence không chứng minh runtime discovery. Kiểm package sạch không chứng minh authority hoặc requirement đúng.

Sau cài, mở phiên mới trên từng công cụ; xác nhận chỉ một public `crm-spec-kit`, gọi một function, hỏi agent báo package root/workstream/target/revision và mode discovery. Lưu tool/version và observed evidence trong pilot. Đừng ghi discovery PASS từ việc `doctor` tìm thấy SKILL.md hoặc một CLI tên codex có trong PATH. Filesystem adapters được kiểm trên repo tạm; UI discovery và Windows native cần smoke test thật.

Sinh prompt chỉ đọc và evidence template từ package đã cài:

```text
python3 scripts/kit.py smoke-prompt crm-check-readiness --repo <repo-root> --agent codex --workstream p3 --target STORY-CRM-001 --target-kind Story --revision <current-revision>
```

Lệnh nhận một tool, function và explicit target/kind/revision, kiểm managed receipt và sinh [prompt](assets/installation/smoke-test-prompt.md); --format json trả prompt + evidence_template. Không chạy workflow, ghi artifact, mở chat hoặc sửa config. Mode chọn skill thật khác manual đọc SKILL theo path; template giữ runtime_verified=false/verdict Chưa kiểm cho tới khi người kiểm ghi evidence quan sát được. Prompt generation không cấp runtime verification hoặc authority approval.

Source missing là WARN để workflow có thể ghi question và làm phần độc lập. Có file tồn tại không chứng minh source đầy đủ/nghiệp vụ đã xác nhận. Kit không tự giải nén ZIP hoặc chạy executable trong nguồn.

## Context and Workflow

Từ package đã cài, dùng helper bên trong package:

```text
python3 scripts/kit.py context crm-define-feature --repo <repo-root> --workstream p3 --target FEAT-CRM-001 --target-kind Feature --revision working-tree
python3 scripts/kit.py context crm-review-specification --repo <repo-root> --workstream p3 --target STORY-CRM-001 --target-kind Story --revision <revision> --reference Q03 --reference D05
```

Context mặc định gồm workflow, phần profile liên quan, các section protocol bắt buộc và standard viết artifact chung; config được in như dữ liệu, không approval. Tài nguyên chi tiết nằm ở available_references; thêm bằng --reference (entry ID hoặc path nội bộ). --full chỉ để so sánh/debug, không mặc định nạp mọi catalog. --format json cung cấp paths/hashes/character counts. Helper không tự chọn active workstream khi có nhiều stream, không tự đoán target/revision.

Các lệnh đọc doctor/context/lint/smoke-prompt nhận --config <candidate-config.json> để audit migration mà không tạo config trong repo thật; đường dẫn trong config vẫn được kiểm theo --repo.

Sau khi ghi artifact chạy lint; cuối run ghi Handoff theo template hiện có. Admin actions install/doctor/context/lint/next-id/update/smoke-prompt là helper, không thêm function nghiệp vụ vào bộ 13 function IDs.

## Artifact Lint and IDs

Đọc [Artifact Metadata and Lint](references/artifact-metadata-and-lint.md). Lint kiểm cấu trúc metadata/explicit fields và links; không là full semantic review hoặc gate enforcement.

```text
python3 scripts/kit.py lint --repo <repo-root> --workstream p3
python3 scripts/kit.py next-id FEAT --repo <repo-root>
python3 scripts/kit.py next-id FEAT --repo <repo-root> --reserve --owner ba-session-1 --apply
```

next-id không reserve chỉ là gợi ý. Reservation có local lock và ledger ngoài package; scan tất cả workstreams cùng namespace. Không tái dùng ID đã reserve. Lock không bảo đảm uniqueness qua các clone độc lập; reconcile/central allocator và lint trước merge vẫn cần. Q chỉ dùng cho câu hỏi của project binding khi được chọn, khác Q01 checklist của kit.

## Controlled Local Update

Chạy helper từ **folder nguồn riêng**, không từ chính installation sẽ được thay:

```text
python3 scripts/kit.py update --repo <repo-root> --source <trusted-new-kit-folder> --install-path .agents/skills/crm-spec-kit
python3 scripts/kit.py update --repo <repo-root> --source <trusted-new-kit-folder> --install-path .agents/skills/crm-spec-kit --apply
```

Có thể thêm --ref với full commit SHA để export kit subfolder từ một Git checkout local. Không fetch/clone mạng tự động; người vận hành chọn và lấy trusted release trước. Không chạy code/tests của candidate; dùng validator hiện tại kiểm candidate như dữ liệu. Nếu release cần schema/validator mới, dừng và kiểm migration riêng.

Install/update --apply có operation lock theo checkout; lock tồn tại không được tự xóa. Update dry-run báo files/version; apply yêu cầu installation không drift, stage bản mới, validate rồi thay managed package bằng rename. Giữ backup ngoài skills tại `.agents/crm-spec-kit-backups/` để đối chiếu/khôi phục; nếu swap lỗi thì restore. Không đụng config/spec artifacts, không tự cập nhật adapter copy khác; update copy còn lại bằng install-path tương ứng rồi doctor. Có backup trùng installation/snapshot thì dừng để người dùng xử lý có chủ đích. Không tự commit/push.

## Manual Mode

Không có Python: agent có thể đọc workflows và soạn/review theo checklist, tạo thư mục được giao bằng công cụ có sẵn. Phải ghi hash/config/lint/update checks chưa chạy; không báo doctor hoặc auto checks đã đạt. Không đảm bảo hai chế độ có cùng mức kiểm chứng.

## Migrating an Existing Wrapper

1. Inventory package/binding/shared-file diffs; lưu snapshot và xác định ownership. Không undo toàn file người dùng đang sửa.
2. Tách repo values vào config; missing sources/decisions vào work-context, giữ metadata nghiệp vụ.
3. Cài và kiểm package mới trên repo clone/bản sao, chạy doctor/lint và fresh-session discovery.
4. Đối soát source/ID/artifact paths và authority rules; chỉ gỡ đúng đoạn integration cũ sau khi chủ repo xác nhận quy tắc thay thế có hiệu lực.
5. Review diff/backup, chuyển package và refs theo kế hoạch migration được giao. File có sẵn của repo không bị đổi bởi install.

Bản triển khai này kiểm nguồn kit và repo tạm; repo crm-docs đang cài thử được đọc để đối chiếu, chưa bị migration/hoàn tác/commit bởi công cụ này.

Backup update được giữ tại `.agents/crm-spec-kit-backups/<installation-key>-<old-snapshot>` ngoài các thư mục skills; dry-run trả đường dẫn backup trước khi ghi. Mỗi installation có key riêng để không đụng backup adapter khác. Helper từ chối ghi đè backup đã tồn tại và giữ receipt cũ để đối soát/rollback. Backup từ các phiên bản helper cũ có thể nằm cạnh skill; kiểm ownership và di chuyển ra ngoài skills trước runtime discovery, không xóa bản cũ chưa đối soát.

## Definition Maturity Scoring

Đọc [scoring guideline](references/definition-maturity-scoring.md) cho schema/rubric/evidence. Lệnh `score --init` tạo JSON Unknown trên stdout; `score --assessment <repo-relative-json>` tính điểm. `--target <ID>` lọc Epic/Story/Feature/requirement; `--scope <scope>` chọn lát cắt; `--item E07` hoặc S09 tính riêng mục trong target; `--format markdown` in báo cáo. Không có --target thì tổng hợp inventory, tách catalog obligations và canonical requirements. Mặc định không ghi file; --output lưu báo cáo Markdown mới trong reports, không tự chấm semantics. Thay source/target/evidence phải reassess, không refresh hash để giữ điểm. Không tạo Ready hoặc approval dù điểm 100.

## Standard trình bày — 1.10

[Standard viết artifact](references/artifact-writing-standard.md) được nạp cho cả 13 function. Update package không tự rewrite artifact hoặc scoped instructions có sẵn; tác giả áp dụng khi author/correction được giao, giữ revision/evidence lịch sử. Templates schema 2 và Markdown metadata footer vẫn đọc được bởi helper; JSON/config giữ schema gốc.
