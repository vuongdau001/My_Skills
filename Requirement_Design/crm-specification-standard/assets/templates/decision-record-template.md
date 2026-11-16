# Mẫu Decision — trạng thái hiện hành

ID: TPL-DECISION · CRM Workflow Kit 2.4.0 · 16/11/2026

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

## 1. Nội dung quyết định hiện hành

Ghi lựa chọn hiện tại và điều kiện áp dụng. Nếu Pending/Proposed, ghi rõ chưa được authority chọn/duyệt; không gọi là quyết định đã có hiệu lực.

## 2. Bối cảnh và phương án

Ghi context có nguồn và các options/trade-off còn liên quan đến bài toán hiện tại. Đây là các phương án của lần xem xét hiện hành, không liệt kê lịch sử từng lần chọn A/B.

## 3. Căn cứ lựa chọn và hệ quả

**Rationale hiện hành:** vì sao phương án hiện tại phù hợp với mục tiêu và điều kiện áp dụng.

**Consequences:** tác động tích cực, tiêu cực, giới hạn và nghĩa vụ phát sinh. Diễn biến chuyển A → B và lý do thay đổi thuộc commit message/PR description, không đặt ở mục này.

## 4. Thẩm quyền và evidence

Ghi authority, decided_at và nguồn pin path/revision/hash cho statement hiện hành. Approved/Rejected cần authority, thời điểm có timezone và evidence. Chưa có thì null/[] theo schema và giữ state thực tế. Approval của statement cũ không được tái dùng cho statement mới chưa được xác nhận.

## 5. Ảnh hưởng và bước tiếp

Dẫn typed trace_links tới consumer hiện hành, impact cần review, gap, receiver và bước tiếp. Cùng vấn đề đổi lựa chọn thì sửa record này với revision mới. Không tạo record Superseded/new-ID chỉ để giữ lịch sử. Không tự cập nhật consumer hoặc Git ngoài quyền được giao.

## Metadata

Dùng một block schema 2 cuối file, giá trị khớp nội dung trên. Nếu dùng register: thêm id/kind vào record trong records của metadata Project, giữ một nơi định nghĩa và anchor riêng theo ID. Không sao chép statement cũ hoặc thêm history array. Khi khai cả revision cấp artifact và cấp record, hai giá trị phải khớp.

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "DEC-CRM-001",
  "kind": "Decision",
  "revision": "r1",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Scope cụ thể cần điền",
    "owner": null,
    "applicability": "Nghiệp vụ / sản phẩm",
    "evidence": [],
    "trace_links": [],
    "decision_state": "Proposed",
    "statement": "Phương án hiện hành cần xác nhận",
    "context": "Vấn đề và nguồn hiện hành",
    "options": "Các lựa chọn và trade-off còn liên quan",
    "rationale": "Căn cứ của phương án hiện hành",
    "consequences": "Tác động và nghĩa vụ của phương án hiện hành",
    "authority": null,
    "decided_at": null
  }
}
```
