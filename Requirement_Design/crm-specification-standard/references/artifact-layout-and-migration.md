# Layout và migration hồ sơ

ID: CRM-LAYOUT · CRM Workflow Kit 3.0.0

Lấy path từ context artifact_paths, không hard-code số thư mục trong workflow.

## Workstream mới

```text
00-project/
  02-decisions/
  03-assumptions/
  04-constraints/
01-capabilities/
02-epics/
03-stories/
04-tasks/
05-reviews/
06-prototypes/
```

Workstream mới có layout_version: 3, record_schema_version: 3 và prototype_gate: true. Nếu tắt prototype_gate mà không override prototypes thì helper không scaffold category này. Legacy layout dùng các tên không đánh số: capabilities, epics, stories, tasks, reviews, prototypes và 00-project.

## Workstream hiện hữu

Config thiếu layout tiếp tục là legacy; config thiếu layout_version giữ vị trí Prototype numbered cũ là 09-prototypes. Update/install không tự đổi config, rename thư mục, xóa dữ liệu hoặc rewrite scoped instructions. Layout version chỉ nhận 2 hoặc 3; migration có chủ đích mới chuyển lên 3. DEC/ASM/CST schema cũ vẫn đọc; update không chuyển business records sang schema mới.

Không còn keys baselines, reports, pilot trong artifact_paths. Config override các key đã bỏ cần được chủ repo đối soát và bỏ trước nâng cấp; helper báo lỗi rõ, không đoán vị trí thay thế. Các thư mục cũ vẫn nằm nguyên và doctor cảnh báo để migration riêng.

Các override còn lại phải là thư mục tương đối bên trong spec_root, không overlap nguồn, read_only, tool directory hoặc category khác. Không dùng symlink để vượt boundary.

## Plan migration

Chạy kit.py plan-layout --repo <repo> --workstream <id> --to numbered. Helper chỉ trả candidate config (layout_version 3), moves, link rewrites, pin impacts và blockers; không có apply flag. Tên ổn định và ID giữ nguyên khi nghĩa không đổi.

Migration riêng phải kiểm file còn dùng trong category đã bỏ, inbound links, revision/hash và kết quả review bị ảnh hưởng. Dữ liệu cũ không tự được archive. Đối chiếu [current-state policy](current-state-and-history.md) và [impact workflow](../workflows/crm-assess-change.md). Sau migration chạy doctor/lint và đánh giá lại evidence đúng scope.
