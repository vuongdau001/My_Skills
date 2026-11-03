# Installation Tooling Validation Report 1.5

Version: **1.5.0** · Date: **03/11/2026**

## Delivered

Bổ sung stdlib helper install/doctor/context/lint/next-id/update, project config blueprint, scoped instruction templates, structured artifact metadata, INSTALL guide và regression tests. Bản cài là một root crm-spec-kit, không wrapper/vendor, không nested SKILL thứ hai. Nguồn vẫn crm-specification-standard; nội dung/config/artifacts của dự án tách khỏi package.

Install/update mặc định dry-run; apply chỉ ghi managed scope, không tự commit/push hoặc sửa global instruction files. Có operation lock, ID reservation local lock, package receipt/integrity, staged local update/backup/rollback. Candidate update được kiểm như dữ liệu bằng validator hiện tại, không chạy executable/tests từ candidate. Không có fetch/clone mạng tự động.

## Executed Automated Checks

- **47 tests đạt:** 13 workflow-registry regression tests và 34 installation-tooling tests.
- Các case gồm: dry-run không ghi; cài copy cho hai adapter; chỉ một SKILL mỗi package; bootstrap từ một folder đã copy; cài lại byte-identical; giữ shared/scoped files có sẵn; từ chối folder không có ownership; internal/external symlink; scaffold escape; read-only/path boundaries; multi-workstream/config preservation; missing sources; compact/expanded context; controlled metadata/table vocabulary; IDs definitions khác refs; duplicate IDs cross-stream; broken links/anchors; optional inferred/question rule; local ID reservations/locks; drift; update dry-run/apply/local modifications/bad candidate/rollback; pinned local Git source; không chạy candidate code; clean clone với core.autocrlf=true.
- Clean-clone test bắt được empty scaffold không được Git giữ và line-ending drift của .gitattributes. Đã thêm scaffold markers và package line-ending rules, chạy lại toàn bộ suite đạt. Đây là Git/filesystem test trên host hiện tại, chưa là Windows native runtime test.
- Structural validator giữ đủ F/E/S/T/Q/D, 13 functions, 5 profiles và 105 source sections. Skill-creator quick validator và git diff whitespace check đạt.

## Context Measurement

Với crm-define-feature trên repo tạm: compact bundle **3 files/sections, 9359 characters**; expanded registry refs **7 files/sections, 37641 characters**. Đây là character count thực tế của một input; không là token benchmark hay đo latency/model accuracy. Compact context yêu cầu agent tiếp tục đọc model/check refs áp dụng, không được bỏ review cần thiết.

## Read-only Audit of Existing Installation

Đã đọc wrapper, binding và pin của bản crm-docs để đối chiếu feedback. Chạy doctor/lint bằng candidate config ngoài repo qua --config, không tạo config hay sửa dữ liệu trong repo thật.

- Legacy lint: **16 Markdown files**, **10 definitions nhận diện rõ**, **0 ERROR**, 4 WARN:legacy-id-ownership, 10 WARN:legacy-metadata.
- Generic ID columns ở bảng liên kết đã được nhận diện là ownership chưa rõ, thay vì tự báo duplicate. Có regression case cho lỗi báo trùng nhầm này. Các ID definitions kiểu mới dùng metadata để kiểm chắc chắn.
- Doctor nhận ra wrapper cũ không có managed receipt và thiếu một số scaffold/scoped instructions; không tự adopt hoặc undo integration cũ. Runtime skill discovery vẫn chưa xác minh.
- Lint valid với WARN legacy không chứng minh mọi ô/tags/authority đúng, không làm Feature Ready hay Approved. Không cập nhật các artifacts legacy trong lần này.

## Preservation

Giữ 80 files trước thay đổi; 6 files nguồn cập nhật có chủ đích: `START-HERE.md`, `SKILL.md`, `reference-manifest.json`, `references/requirement-types-identifiers-and-traceability.md`, `references/pack-acceptance-scenarios.md`, `references/workflow-execution-protocol.md`.

Các catalog/models/checks/provenance lịch sử và snapshot nguồn giữ nguyên hash. 5 file binding/shared-instruction mẫu ở repo cài thử được đối chiếu hash trước/sau và không đổi; các helper audit chỉ đọc. Tracked changes chỉ trong folder nguồn kit.

## Limits and Next Operational Step

Chưa migration bản crm-docs, chưa hoàn tác ba shared files, chưa commit/push, chưa cài vào runtime của người dùng. Antigravity/Claude adapters đã kiểm filesystem; UI discovery, instruction precedence và Windows native vẫn cần fresh-session smoke test có tool/version/evidence thật.

next-id reservation chỉ serialize trong một checkout; clone khác vẫn cần reconcile hoặc central allocator. Manual fallback không có Python không được nhận cùng kết luận hash/lint/doctor. Structural health không thay authority hoặc hard gate Git/Jira/CI. Nguồn update phải được người dùng chọn/tin cậy; integrity receipt không là chữ ký.

Tiếp theo dùng [INSTALL](../INSTALL.md) để review dry-run của repo đích, kiểm các xung đột instruction và migration trong bản sao trước khi chạm bản cài cũ. [Feedback assessment](installation-feedback-assessment.md) ghi phạm vi đã xác minh.
