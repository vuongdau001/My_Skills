# Assumption Record Template

ID: TPL-ASSUMPTION · CRM Workflow Kit 1.7.0 · 04/11/2026

Đọc [quy tắc record/evidence](../../references/knowledge-records-and-evidence.md). Đây là mẫu draft minh họa, chưa là record dự án. Cấp ID thật bằng next-id; thay scope/nội dung bằng nguồn đã đọc, giữ null nếu chưa có người hoặc thời điểm. Không nâng trạng thái để lấp template.

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "ASM-CRM-001",
  "kind": "Assumption",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Phạm vi cần xác nhận",
    "evidence": [],
    "trace_links": [],
    "owner": null,
    "assumption_state": "Unverified",
    "statement": "Giả định cần kiểm chứng",
    "basis": "Căn cứ hiện có, chưa là fact",
    "validation_method": "Phương pháp kiểm và evidence cần thu",
    "review_due": null,
    "if_false": "Các scope bị ảnh hưởng nếu giả định sai"
  }
}
```

## Nội dung và nguồn

Ghi source locator/excerpt có quyền truy cập; tách fact, diễn giải, câu hỏi và quyết định. Evidence dùng path tương đối, revision và SHA-256 nguồn. Không đặt secret hoặc transcript riêng tư vào repo ngoài quyền đã có.

## Scope và handoff

Liên kết Feature/Epic/Story/rule bị ảnh hưởng bằng trace_links. Ghi receiver, missing authority/evidence và next function phù hợp. Sau thay đổi, tăng revision và review lại consumer; không tái dùng approval sai revision.

## Dùng trong register

Có thể chuyển object record thành một phần tử records trong metadata Project schema 2, bổ sung id và kind vào phần tử; không giữ đồng thời hai nơi định nghĩa ID. Giữ anchor ổn định nếu người dùng cần link tới record cụ thể.
