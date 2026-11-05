# Mẫu giả định cần kiểm chứng

ID: TPL-ASSUMPTION · CRM Workflow Kit 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Đọc [knowledge records](../../references/knowledge-records-and-evidence.md). Cấp ID bằng next-id; giữ null nếu chưa có owner/thời điểm.


## Giả định và căn cứ

Một statement có scope; basis là căn cứ hiện có, chưa là fact. Ghi source locator và evidence pin revision/hash.

## Kế hoạch kiểm chứng

Validation method, người kiểm/owner, review_due và evidence cần thu; chưa gán người/hạn giữ null.

## Nếu giả định sai

Nêu if_false, consumer áp dụng và ảnh hưởng tới requirement/model/AC/contract. Khai trace_links đúng nhánh; chưa dùng prose scope để né dependency.

## Kết quả và bàn giao

Validated/Invalidated cần validation_result, owner và evidence đúng statement/scope. Giữ ASM khi kiểm chứng; không bắt tạo DEC. Retired phải nêu vì sao không còn dùng và xử lý dependency, không coi là chứng minh đúng. Cần chọn policy/phương án thì tạo DEC riêng và giữ history; risk acceptance không làm ASM Validated.

Xem [lifecycle chi tiết](../../references/knowledge-records-and-evidence.md#giải-quyết-assumption-và-phân-biệt-decision--19). Ghi receiver và bước refinement/review lại.

## Nếu dùng register

Đưa record vào records của metadata Project schema 2, bổ sung id/kind; không giữ đồng thời hai nơi định nghĩa. Dùng anchor ổn định khi cần dẫn mục.


<details>
<summary>Metadata mẫu — thay bằng giá trị thật</summary>

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

</details>
