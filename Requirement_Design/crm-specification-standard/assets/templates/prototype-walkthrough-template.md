# Mẫu biên bản walkthrough Prototype

ID **TPL-PROTOTYPE-WALKTHROUGH** · CRM Workflow Kit 1.12.0

Dùng [standard Prototype](../../references/prototype-workflow-and-epic-gate.md) và [standard viết artifact](../../references/artifact-writing-standard.md). Ghi biên bản mới trong reviews của workstream. Chỉ pin evidence đã đối chiếu.

## Kết luận và phạm vi

Ghi Epic ID/revision/scope, manifest revision/hash, người thực hiện, reviewer, vai trò, ngày giờ và verdict. Chọn Đạt khi đã walkthrough đủ scenario được phân bổ, đúng expected behavior và đã xử lý findings chặn. Ghi Chưa kiểm khi thiếu quan sát hoặc authority. Ghi Không đạt khi có gap thực tế.

## Kết quả quan sát

| Scenario ID | Fixture và cách chạy | Kết quả quan sát | Kết luận và evidence |
|---|---|---|---|
| SCN-CONTACT-CREATE | Thay bằng entrypoint, role, fixture và môi trường đã dùng | Ghi UI state và contract outcome đã kiểm | Verdict, screenshot/locator hoặc finding ID |

## Findings và bước tiếp theo

Ghi BR/AC/contract hoặc Screen ID bị ảnh hưởng, expected/observed, decision/question ID, owner, người xử lý và phần phải kiểm lại. Đối với N/A, ghi lý do theo scope, evidence đã đối chiếu và người xác nhận. Giữ record đã review theo revision.

## Metadata

Dùng block crm-spec-kit dưới đây với dữ liệu thật. Tính SHA256 Epic sau khi đã ghi binding tới review. Tính SHA256 manifest sau khi đã pin toàn bộ bundle. Thay tất cả placeholders.

```crm-spec-kit
{
  "schema_version": 1,
  "kind": "Review",
  "review_verdict": "Đạt",
  "prototype_walkthrough": {
    "scope": "contact-create",
    "epic_sha256": "<sha256>",
    "manifest_sha256": "<sha256>",
    "reviewer": "<tên và vai trò>",
    "observed_at": "<ISO 8601 có timezone>",
    "observed_scenarios": ["SCN-CONTACT-CREATE"]
  }
}
```

Với N/A, thêm na_reason, dùng review_verdict N/A và bỏ manifest_sha256/observed_scenarios. Scope và epic_sha256 vẫn bắt buộc.
