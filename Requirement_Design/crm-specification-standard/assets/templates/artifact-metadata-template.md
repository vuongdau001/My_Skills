# Mẫu metadata artifact

ID: **TPL-ARTIFACT-METADATA** · CRM Workflow Kit 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Nội dung để người đọc nằm trước metadata: tiêu đề, ý chính, context, nội dung nghiệp vụ, gap và handoff. Thêm đúng một block cuối file; có thể thu gọn bằng details khi viewer hỗ trợ.

Mẫu dưới minh họa Feature schema 1. Chọn đúng kind/schema, ID/revision và vocabulary. Không gán work_status cho Feature. Knowledge records mới dùng các template schema 2 riêng.

artifact_id và defined_ids là definitions; references là links tương đối từ artifact. trace_links có ID/path/revision/relation để khai dependency; evidence schema 2 cần hash/revision đúng nguồn. ID trong ví dụ không là ID đã được cấp cho dự án.


<details>
<summary>Metadata mẫu — thay bằng giá trị thật</summary>

```crm-spec-kit
{
  "schema_version": 1,
  "artifact_id": "FEAT-CRM-001",
  "kind": "Feature",
  "revision": "draft-r1",
  "defined_ids": [],
  "review_verdict": "Chưa kiểm",
  "references": []
}
```

</details>
