# Meeting Record Template

ID: TPL-MEETING · CRM Workflow Kit 1.7.0 · 04/11/2026

Đọc [quy tắc record/evidence](../../references/knowledge-records-and-evidence.md). Đây là mẫu draft minh họa, chưa là record dự án. Cấp ID thật bằng next-id; thay scope/nội dung bằng nguồn đã đọc, giữ null nếu chưa có người hoặc thời điểm. Không nâng trạng thái để lấp template.

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "MTG-CRM-001",
  "kind": "Meeting",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Phạm vi cần xác nhận",
    "evidence": [],
    "trace_links": [],
    "meeting_state": "Draft",
    "event_type": "workshop",
    "occurred_at": null,
    "participants": [],
    "summary": "Nội dung ghi nhận từ nguồn thực tế",
    "actions": []
  }
}
```

## Nội dung và nguồn

Ghi source locator/excerpt có quyền truy cập; tách fact, diễn giải, câu hỏi và quyết định. Evidence dùng path tương đối, revision và SHA-256 nguồn. Không đặt secret hoặc transcript riêng tư vào repo ngoài quyền đã có.

## Scope và handoff

Liên kết Feature/Epic/Story/rule bị ảnh hưởng bằng trace_links. Ghi receiver, missing authority/evidence và next function phù hợp. Sau thay đổi, tăng revision và review lại consumer; không tái dùng approval sai revision.

## Decisions, questions và action items

Dẫn DEC/Q/ASM/CST bằng ID và revision. Mỗi action ghi description, owner và due; dùng null nếu chưa được giao. event_type phải đúng workshop/chat/email/meeting đã xảy ra. Confirmed biên bản không tự Approved các Decision.
