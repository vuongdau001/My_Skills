# Mẫu Constraint — trạng thái hiện hành

ID: TPL-CONSTRAINT · CRM Workflow Kit 2.4.0 · 16/11/2026

Áp dụng [cấu trúc và current-state policy](../../references/knowledge-records-and-evidence.md#record-current-state) và [standard viết artifact](../../references/artifact-writing-standard.md). Giữ đúng thứ tự mục dưới đây; thay hướng dẫn bằng nội dung thực. Chỉ giữ phiên bản hiện hành, không thêm mục History/Changelog hoặc các statement của revision cũ. Cấp ID bằng next-id cho record mới; cùng vấn đề thì giữ ID và tăng revision. Thiếu dữ liệu ghi rõ; không suy approval từ template đầy đủ.

# <ID> — <Tên nội dung hiện hành>

Một câu statement hiện hành; phần này và metadata phải cùng nghĩa.

| Bối cảnh | Giá trị hiện hành |
|---|---|
| Revision | r1 hoặc revision thực tế |
| State | State đúng loại và evidence hiện có |
| Phạm vi áp dụng | Nghiệp vụ / sản phẩm **hoặc** Dự án / SDLC; chọn một |
| Scope cụ thể | Nội dung/consumer thực sự chịu tác động |
| Owner record | Người được giao; chưa giao ghi Chưa xác định, metadata null |

## 1. Ràng buộc hiện hành và loại

Ghi statement, constraint_type (business, technical, organizational hoặc external theo nội dung) và điều kiện áp dụng. Công nghệ đang cân nhắc không tự thành ràng buộc bắt buộc. Không tạo CST trùng nghĩa với BR/MOD đã có.

## 2. Nguồn, thẩm quyền và hiệu lực

Ghi nguồn pin path/revision/hash, authority và effective_from hiện hành. Confirmed cần đủ evidence, authority và hiệu lực; chưa có thì Proposed theo thực tế. Khi nội dung/hiệu lực đổi, không giữ xác nhận cũ cho statement mới chưa được xác nhận. Giữ source locator thực, không nhúng timeline hoặc toàn bộ nguồn vào record.

## 3. Cách kiểm tuân thủ

Ghi verification_method, evidence cần quan sát và kết quả/hướng xử lý vi phạm còn phải xác nhận. Không tự đặt SLA, exception hoặc authority xử lý vi phạm.

## 4. Phạm vi ảnh hưởng

Dẫn hồ sơ nghiệp vụ/sản phẩm hoặc hồ sơ dự án/SDLC bị giới hạn; typed trace_links theo consumer thực sự. Nêu impact hiện hành, không chép các lần thay đổi scope trước.

## 5. Điểm mở và bước tiếp

Ghi owner, gap, receiver và bước xác nhận/kiểm/review. Retired/Superseded theo thực tế phải xử lý dependency còn dùng; không coi chuyển state là đã đóng blocker. Cùng một ràng buộc thay đổi thì giữ ID, tăng revision và lưu lý do đổi trong Git.

## Metadata

Dùng một block schema 2 cuối file, giá trị khớp nội dung trên. Nếu dùng register: thêm id/kind vào record trong records của metadata Project, giữ một nơi định nghĩa và anchor riêng theo ID. Không sao chép statement cũ hoặc thêm history array. Khi khai cả revision cấp artifact và cấp record, hai giá trị phải khớp.

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "CST-CRM-001",
  "kind": "Constraint",
  "revision": "r1",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Scope cụ thể cần điền",
    "owner": null,
    "applicability": "Nghiệp vụ / sản phẩm",
    "evidence": [],
    "trace_links": [],
    "constraint_state": "Proposed",
    "statement": "Ràng buộc hiện hành cần xác nhận",
    "constraint_type": "technical",
    "verification_method": "Cách kiểm tuân thủ ràng buộc hiện hành",
    "authority": null,
    "effective_from": null
  }
}
```
