# Mẫu ràng buộc có nguồn

ID: TPL-CONSTRAINT · CRM Workflow Kit 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Đọc [knowledge records](../../references/knowledge-records-and-evidence.md). Cấp ID bằng next-id; giữ null nếu chưa có owner/thời điểm.


## Ràng buộc và phạm vi

Nêu statement, loại business/technical/organizational/external phù hợp và scope cụ thể. Công nghệ đang cân nhắc chưa tự thành constraint bắt buộc.

## Nguồn và hiệu lực

Source locator, authority và evidence revision/hash. Confirmed cần evidence, authority và effective_from; thiếu thì giữ Proposed theo thực tế.

## Cách kiểm tuân thủ

Verification method, requirements/consumer áp dụng và expected disposition khi vi phạm. Không tạo CST trùng nghĩa với BR/MOD data constraint đang có.

## Ảnh hưởng và bàn giao

Ghi owner, trace_links, gaps và receiver. Khi sửa revision, kiểm lại consumer và approval; không sửa record nguồn trong bước review/check.

## Nếu dùng register

Đưa record vào records của metadata Project schema 2, bổ sung id/kind; không giữ đồng thời hai nơi định nghĩa. Dùng anchor ổn định khi cần dẫn mục.


<details>
<summary>Metadata mẫu — thay bằng giá trị thật</summary>

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

</details>
