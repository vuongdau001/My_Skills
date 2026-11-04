# Layout and Knowledge Records Validation Report 1.7

Version: 1.7.0 · Date: 04/11/2026

## Scope

Numbered layout cho workstream mới, config schema 1 legacy compatibility, optional artifact_paths và read-only plan-layout. Thêm knowledge records schema 2, templates, ID namespaces, pinned typed references, supersession và scoped obligation gate checks. Giữ public skill crm-spec-kit, 13 function, 5 profiles và adapters hiện có. Không migration tự động; không update package/pilot CRM trong lần triển khai standard này.

## Verification

- 110/110 unittest đạt: 71 regression tests và 39 tests mới cho layout/records. Chạy python3 -B -m unittest discover -s scripts/tests -v trên fixture tạm, không thao tác artifact thật của pilot.
- Structural validator đạt: 94 Markdown documents, 145 manifest entries, 105 source sections, 5 profiles, 13 function. Skill-creator quick validation và git diff --check đạt.
- Layout tests kiểm default numbered, legacy config byte preservation, custom path/context/inference, overlap/traversal/symlink, mixed-layout metadata warnings và adapter compatibility. Migration planner kiểm không ghi file, collision/symlink blockers, inbound links, hash/locator/historical impacts, candidate config và snapshot đổi khi binary/inbound source đổi. Planner không có --apply.
- Record tests kiểm bốn kinds và new prefixes, legacy Decision schema 1, register ownership/duplicate IDs, approval fields/evidence, exact revision/ID owner/anchor/hash, nguồn external/escaping, cross-workstream allocation, supersession/missing replacement/cycle, assumption invalidation/risk acceptance và obligation closure/impacted consumers. Target gate không bị assumption hoặc external evidence không liên quan chặn; structural schema/link checks vẫn được audit rộng.
- Bốn fixture regression cũ được điều chỉnh vì workstream mới mặc định numbered: copied bootstrap expectation, hai path ở workstream mới thứ hai, và symlink fixture chọn legacy rõ ràng. Regression helper cũ dùng --layout legacy để tiếp tục kiểm hành vi cũ; update candidate lên 1.7.1. Không thay expected outcome về gate/authority để làm test qua.
- Audit read-only repo CRM hiện có: doctor --agent codex healthy=true, không ERROR; lint p3 kiểm 21 files, issues=[], semantic_approval=false. Cả 1.457 file có sẵn giữ nguyên hash, không thêm file. Bản cài 1.5 và pilot không tự nâng cấp/migrate.
- Dry-run plan-layout trên CRM cho 8 moves, 38 link rewrite suggestions, 4 locator/hash impact paths, 10 historical paths cần bảo toàn và không collision blocker. Những số này là inventory của planner, chưa là đầy đủ parser hoặc migration approval. Không áp dụng candidate config, move, sửa evidence hoặc baseline receipt.

Structural/lint results không chứng minh semantic approval, independent review, runtime discovery, product behavior hoặc external Jira/Git/CI gate enforcement. Planner không có --apply; schema 2 cần helper 1.7, không tuyên bố tool cũ đọc được capability mới.

## Delivery và giới hạn

24 file cũ thay đổi có chủ đích, 10 file thêm. Catalogs/models/checks nghiệp vụ và profiles được giữ; workflows thêm routing record/layout và các bước helper scoped, không đổi authority. Archive nguồn và migration map lịch sử không sửa. Các templates là draft, không record dự án hoặc proof of approval.

Workstream cũ được đọc như legacy khi thiếu layout. Package update không đổi config/artifacts hoặc tự merge scoped instructions. Khi sử dụng hồ sơ schema 2, teammate cần kit/helper 1.7; old helper không được cam kết forward-compatible. Giữ adapter antigravity/claude/both/codex và semantics router opt-in từ 1.6.

Known limits: record graph chỉ biết các links khai báo; thiếu link/applicability cần human review. SHA chứng minh bytes khớp, không chứng minh source có authority hay statement đúng. External URLs không fetch. Planner chỉ lập gợi ý, chưa thực hiện chuyển cấu trúc; migration thật cần thao tác riêng trong phạm vi user giao và revalidation của các revision bị ảnh hưởng. Không commit/push, Jira mutation, product test hoặc runtime discovery được thực hiện.

Hướng dẫn: [layout/migration](../references/artifact-layout-and-migration.md), [knowledge records/evidence](../references/knowledge-records-and-evidence.md), [INSTALL](../INSTALL.md).
