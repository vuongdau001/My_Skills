# Mẫu Assumption không state

ID: TPL-ASSUMPTION · CRM Workflow Kit 2.7.0

Đọc [mô hình record](../../references/knowledge-records-and-evidence.md). Mỗi ID một nội dung hiện hành. Không có trường state, không thêm timeline; metadata ở cuối.

# ASM-CRM-001 — Tên nội dung

Điều chưa được xác nhận.

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
  "artifact_id": "ASM-CRM-001",
  "kind": "Assumption",
  "revision": "r1",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Phạm vi áp dụng",
    "statement": "Điều chưa được xác nhận",
    "owner": null,
    "evidence": [],
    "trace_links": [],
    "basis": "Căn cứ hiện có, chưa chứng minh đúng"
  }
}
```
