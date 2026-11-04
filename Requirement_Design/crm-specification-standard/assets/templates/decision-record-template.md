# Decision Record Template

ID: TPL-DECISION · CRM Workflow Kit 1.7.0 · 04/11/2026

Đọc [quy tắc record/evidence](../../references/knowledge-records-and-evidence.md). Đây là mẫu draft minh họa, chưa là record dự án. Cấp ID thật bằng next-id; thay scope/nội dung bằng nguồn đã đọc, giữ null nếu chưa có người hoặc thời điểm. Không nâng trạng thái để lấp template.

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "DEC-CRM-001",
  "kind": "Decision",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Phạm vi cần xác nhận",
    "evidence": [],
    "trace_links": [],
    "owner": null,
    "decision_state": "Proposed",
    "statement": "Lựa chọn cần được quyết định",
    "context": "Vấn đề và nguồn cần giải quyết",
    "options": "Các lựa chọn và trade-off cần review",
    "rationale": "Căn cứ của phương án đề xuất",
    "consequences": "Tác động tích cực, tiêu cực và trung lập",
    "authority": null,
    "decided_at": null
  }
}
```

## Nội dung và nguồn

Ghi source locator/excerpt có quyền truy cập; tách fact, diễn giải, câu hỏi và quyết định. Evidence dùng path tương đối, revision và SHA-256 nguồn. Không đặt secret hoặc transcript riêng tư vào repo ngoài quyền đã có.

## Scope và handoff

Liên kết Feature/Epic/Story/rule bị ảnh hưởng bằng trace_links. Ghi receiver, missing authority/evidence và next function phù hợp. Sau thay đổi, tăng revision và review lại consumer; không tái dùng approval sai revision.

## Lịch sử thay thế

Nếu thay quyết định cũ, giữ old record Superseded với superseded-by; record mới dẫn supersedes và nêu rationale/scope. Approved cần authority, decided_at và evidence đúng revision, không tự xác nhận từ vai trò agent.
