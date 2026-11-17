# Mẫu Constraint không state

ID: TPL-CONSTRAINT · CRM Workflow Kit 2.7.0

Đọc [mô hình record](../../references/knowledge-records-and-evidence.md). Mỗi ID một nội dung hiện hành. Không có trường state, không thêm timeline; metadata ở cuối.

# CST-CRM-001 — Tên nội dung

Ràng buộc đang áp dụng.

## 1. Nội dung

Ghi statement và scope. Thiếu nội dung/xác nhận thì nêu gap, không tự điền để qua lint.

## 2. Căn cứ và nơi sử dụng

Nguồn/evidence có path, revision và SHA-256; người xác nhận hoặc người kiểm nếu được giao. Dẫn consumer thực sự. Không dựng approval, giờ hoặc nguồn chưa đọc.

## 3. Sửa, chuyển hoặc bỏ

Sửa cùng vấn đề giữ ID và tăng revision. ASM được xác nhận thì chuyển sang DEC ID, cập nhật consumer rồi xóa ASM. Decision/Constraint không còn dùng thì cập nhật nơi tham chiếu trước khi bỏ. Lịch sử qua Git, không tự commit.

## Metadata

```crm-spec-kit
{
  "schema_version": 3,
  "artifact_id": "CST-CRM-001",
  "kind": "Constraint",
  "revision": "r1",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Phạm vi áp dụng",
    "statement": "Ràng buộc đang áp dụng",
    "owner": null,
    "evidence": [],
    "trace_links": [],
    "verification_method": "Cách đối soát nếu cần"
  }
}
```
