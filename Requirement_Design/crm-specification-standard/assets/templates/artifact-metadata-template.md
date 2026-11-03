# Artifact Metadata Template

ID: **TPL-ARTIFACT-METADATA** · CRM Workflow Kit 1.5.0 · 03/11/2026

Copy block vào artifact mới và thay bằng giá trị thật. Đọc [metadata/lint guide](../../references/artifact-metadata-and-lint.md). Mẫu Feature chưa có review/approval, không phải output dự án đã đạt.

```crm-spec-kit
{
  "schema_version": 1,
  "artifact_id": "FEAT-CRM-001",
  "kind": "Feature",
  "defined_ids": [],
  "review_verdict": "Chưa kiểm",
  "references": []
}
```

Chỉ khai báo field áp dụng: work_status cho Epic/Story/Task; decision_state cho decision/policy có record; na_reason khi review_verdict=N/A. defined_ids ghi các REQ/BR/AC/MOD… được định nghĩa trong file, không liệt kê ID chỉ được dẫn từ nguồn khác. Giữ source/authority/revision/handoff theo templates nội dung hiện hành; JSON block không thay chúng.
