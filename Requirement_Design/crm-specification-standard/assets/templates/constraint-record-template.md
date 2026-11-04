# Constraint Record Template

ID: TPL-CONSTRAINT · CRM Workflow Kit 1.7.0 · 04/11/2026

Đọc [quy tắc record/evidence](../../references/knowledge-records-and-evidence.md). Đây là mẫu draft minh họa, chưa là record dự án. Cấp ID thật bằng next-id; thay scope/nội dung bằng nguồn đã đọc, giữ null nếu chưa có người hoặc thời điểm. Không nâng trạng thái để lấp template.

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "CST-CRM-001",
  "kind": "Constraint",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Phạm vi cần xác nhận",
    "evidence": [],
    "trace_links": [],
    "owner": null,
    "constraint_state": "Proposed",
    "statement": "Ràng buộc cần xác nhận",
    "constraint_type": "business/technical/organizational/external — chọn loại thật",
    "verification_method": "Cách kiểm tuân thủ",
    "authority": null,
    "effective_from": null
  }
}
```

## Nội dung và nguồn

Ghi source locator/excerpt có quyền truy cập; tách fact, diễn giải, câu hỏi và quyết định. Evidence dùng path tương đối, revision và SHA-256 nguồn. Không đặt secret hoặc transcript riêng tư vào repo ngoài quyền đã có.

## Scope và handoff

Liên kết Feature/Epic/Story/rule bị ảnh hưởng bằng trace_links. Ghi receiver, missing authority/evidence và next function phù hợp. Sau thay đổi, tăng revision và review lại consumer; không tái dùng approval sai revision.

## Dùng trong register

Có thể chuyển object record thành một phần tử records trong metadata Project schema 2, bổ sung id và kind vào phần tử; không giữ đồng thời hai nơi định nghĩa ID. Giữ anchor ổn định nếu người dùng cần link tới record cụ thể.
