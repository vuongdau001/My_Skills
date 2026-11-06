# Mẫu bundle Prototype

ID **TPL-PROTOTYPE-BUNDLE** · CRM Workflow Kit 1.12.2

Dùng [standard Prototype](../../references/prototype-workflow-and-epic-gate.md) và [standard viết artifact](../../references/artifact-writing-standard.md). ID và giá trị dưới đây chỉ minh họa. Lấy đường dẫn category prototypes từ Work Context. Đặt bundle bàn giao trong thư mục hành trình ngay dưới category này, ví dụ `09-prototypes/contact-create/` cho một scenario tạo Contact độc lập. Dùng tên thư mục ổn định, ghi revision trong hồ sơ và pin bằng manifest cùng walkthrough.

## README.md

- **Hành trình và scope** — Epic ID/revision, đối tượng sử dụng, phần demo và phần giả lập.
- **Chỉ dẫn người dùng** — mục tiêu demo, sample/link/ảnh được cung cấp, câu hỏi hoặc input đang chờ.
- **Nguồn UI** — vị trí của bản đã xem, kể cả file ngoài repo, tệp đính kèm hoặc link. Ghi revision hoặc hash nếu có, phần tái dùng và phần thay đổi.
- **Cách chạy** — entrypoint, fixture, cách mở theo môi trường đã review và giới hạn.
- **Bàn giao** — scenario index, review record và baseline refs khi có.

## scenarios.md

Viết mỗi case thành mục riêng, giữ ID trong manifest.

### SCN-CONTACT-CREATE

- **Actor và dữ liệu** — role, quyền, fixture và state ban đầu.
- **Thao tác** — entrypoint và các bước.
- **Kết quả mong đợi** — UI state và Command/Query/permission outcome theo BR/AC đã xác nhận.
- **Đối chiếu** — Screen ID, MOD ID/locator E03, BR/AC/contract refs và gap ID nếu còn.

## manifest.json

Thay mọi placeholder bằng giá trị từ scope đã đặc tả. Dùng path tương đối từ bundle. Tạo SHA256 từ bytes của scenarios.md và mọi file trong app, screens, assets, fixtures sau khi hoàn thiện nội dung. Trên macOS có thể dùng `shasum -a 256 scenarios.md app/index.html screens/contact-create.html` cho các file của ví dụ này.

```json
{
  "schema_version": 1,
  "entrypoint": "app/index.html",
  "allocations": [
    {"epic_id": "<epic-id>", "epic_revision": "<epic-revision>", "scope": "contact-create", "scenarios": ["SCN-CONTACT-CREATE"]}
  ],
  "screens": [
    {"id": "SCR-CONTACT-CREATE", "path": "screens/contact-create.html"}
  ],
  "scenarios": [
    {"id": "SCN-CONTACT-CREATE", "screens": ["SCR-CONTACT-CREATE"], "refs": ["<mod-id>#create-contact-step", "<business-rule-id>", "<acceptance-id>", "<create-contract-ref>"]}
  ],
  "files": {
    "scenarios.md": "<sha256>",
    "app/index.html": "<sha256>",
    "screens/contact-create.html": "<sha256>"
  }
}
```

## Binding trong Epic

Thêm trường prototype vào block metadata crm-spec-kit đang có. Path manifest và review tương đối từ spec_root. Mỗi revision Epic khai báo binding cho scope hiện trình gate. Baseline package dẫn Epic ID/revision/scope và SHA của file Epic, manifest và walkthrough tương ứng.

```json
{
  "prototype": {
    "applicability": "required",
    "scope": "contact-create",
    "manifest": "09-prototypes/contact-create/manifest.json",
    "review": "05-reviews/contact-create-walkthrough.md"
  }
}
```

Với scope backend không tác động UI, dùng applicability not_applicable, scope, reason và review. Dẫn contract/evidence trong E08 và review. Bản ghi cần verdict N/A và na_reason.
