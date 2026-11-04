# Thứ tự thư mục và chuyển layout

ID: CRM-LAYOUT · CRM Workflow Kit 1.7.0 · 04/11/2026

Đọc khi cài mới, chọn vị trí ghi hoặc chuyển cấu trúc tài liệu. Cấu trúc áp dụng chung mọi adapter; không phụ thuộc Codex UI.

## Layout và ID

Workstream mới mặc định layout numbered:

```text
spec/
  00-project/
    01-meetings/
    02-decisions/
    03-assumptions/
    04-constraints/
  01-features/
  02-epics/
  03-stories/
  04-tasks/
  05-reviews/
  06-baselines/
  07-reports/
  08-pilot/
```

Số ở folder là thứ tự đọc theo nhóm, không priority hoặc tiến độ. File dùng ID ổn định, ví dụ EPIC-CRM-002-contact-relationships.md; không thêm số thứ tự thứ hai. Story có thể đổi parent mà giữ ID. Cây thư mục phẳng theo loại; hierarchy và dependency nằm ở allocation/trace_links, không suy từ số hoặc tên file. Task chỉ được tạo khi có nhu cầu giao việc thật.

Config schema 1 tiếp tục được đọc. Workstream thiếu layout được hiểu là legacy, dùng 00-project/features/epics/stories/tasks/reviews/baselines/reports/pilot. Install lại hoặc update package không tự thêm field, đổi path hoặc rewrite hồ sơ của workstream cũ. --layout legacy chọn tên thư mục cũ cho workstream mới; loại hồ sơ schema 2 vẫn được hỗ trợ bởi kit 1.7.

Workstream mới ghi layout và record_schema_version=2. Field artifact_paths tùy chọn override theo category; mọi giá trị là path POSIX tương đối từ spec_root, không overlap, không ẩn/tool directory hoặc thoát repo. Ví dụ cấu hình workstream:

```json
{
  "id": "p3",
  "title": "CRM Phase 3",
  "spec_root": "phase-3/spec",
  "layout": "numbered",
  "record_schema_version": 2,
  "artifact_paths": {"reports": "07-reports"},
  "sources": [],
  "read_only": []
}
```

Helper context trả artifact_paths đã resolve trong workstream. Dùng map này khi ghi; không hardcode epics hoặc 02-epics trong workflow. Lint nhận cả hai tên chuẩn và custom map để migration không làm mất cảnh báo metadata. Doctor kiểm scaffold theo config, không suy layout từ số lượng thư mục tồn tại. Không chạy helper 1.5/1.6 cho config numbered hoặc hồ sơ schema 2; dùng package đã nâng lên 1.7 trên từng adapter.

## Migration chỉ lập kế hoạch

```text
python3 scripts/kit.py plan-layout --repo <repo-root> --workstream p3 --to numbered
```

Lệnh này chỉ đọc, không có --apply. Output gồm moves, candidate_config, link_rewrites gợi ý, locator/hash impacts, historical records, blockers và snapshot_sha256 của input/config. Path/ID/hash là dữ liệu, không approval. Custom artifact_paths được bỏ khỏi candidate khi chuyển về một preset; config thật không đổi. Destination có sẵn hoặc symlink cần kiểm riêng, không merge/overwrite tự động.

Các gợi ý link không phải parser hoàn chỉnh cho prose, scripts, HTML hoặc mọi định dạng nguồn. Trước khi chuyển thực tế:

1. Lưu plan; đối chiếu scope và inbound refs ngoài spec_root. Chỉ thực hiện khi user đã giao migration, không coi yêu cầu update package là quyền chuyển hồ sơ.
2. Xác định snapshots/records đang pin revision/hash/path nào. Giữ bản lịch sử đúng byte tại path cũ hoặc archive có mapping được review; không rewrite receipt/approval cũ và không tạo hai definition hiện hành cùng ID trong spec_root.
3. Di chuyển bản hiện hành và sửa refs/config theo thay đổi thực tế. File có ref đổi sẽ đổi hash; lập revision mới và đánh giá lại evidence/approval bị ảnh hưởng. Với baseline phải dùng change control; không tự cấp lại approval.
4. Chạy lại plan trên input mới nếu có thay đổi, rồi doctor/lint và checks của project. Rebaseline scope bị ảnh hưởng chỉ khi đủ authority/evidence. Dùng snapshot read-only ngoài vùng artifact hiện hành nếu cần tránh duplicate definitions.

Không có automatic migration trong bản 1.7. Planner giúp chuẩn bị thay đổi review được, không cam kết baseline cũ còn hiệu lực sau khi move/rewrite. [Baseline/change control](baseline-and-change-control.md) tiếp tục áp dụng.
