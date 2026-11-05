# Mẫu ghi nhận Meeting/chat/email

ID: TPL-MEETING · CRM Workflow Kit 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Đọc [knowledge records](../../references/knowledge-records-and-evidence.md). Cấp ID bằng next-id; giữ null nếu chưa có owner/thời điểm.


## Sự kiện và participants

Ghi loại sự kiện thực (meeting/workshop/chat/email), thời điểm có timezone nếu biết, participants/roles và phạm vi. Draft chưa biết timestamp giữ null; không tạo cuộc họp hoặc chữ ký giả.

## Nội dung đã ghi nhận

Một đoạn tóm tắt, sau đó tách nguồn/facts, discussion và điểm chưa thống nhất. Dẫn excerpt/locator và SHA-256/revision trong evidence.

## Decisions, questions và action items

Dẫn DEC/Q/ASM/CST bằng ID/revision. Mỗi action có description/owner/due; unknown giữ null. Action chưa tự thành product Task. Confirmed biên bản chưa tự Approved mọi Decision.

## Trạng thái xác nhận và bàn giao

Draft/Confirmed/Amended theo evidence; Amended cần amendment_reason và giữ lịch sử. Nêu consumer bị ảnh hưởng, receiver và phần thiếu authority. Không gửi biên bản/tạo ticket tự động.


<details>
<summary>Metadata mẫu — thay bằng giá trị thật</summary>

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

</details>
