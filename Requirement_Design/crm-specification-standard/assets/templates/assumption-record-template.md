# Mẫu Assumption — trạng thái hiện hành

ID: TPL-ASSUMPTION · CRM Workflow Kit 2.4.0 · 16/11/2026

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

## 1. Giả định hiện hành và căn cứ

Ghi một statement cần kiểm, scope và basis có nguồn. Basis chưa chứng minh giả định đúng. Không gộp lựa chọn policy vào một phát biểu giả định đã được xác nhận.

## 2. Cách kiểm chứng

Ghi validation_method, người kiểm chứng, owner theo dõi nếu khác, review_due và evidence cần thu. Chưa được giao người/hạn thì ghi Chưa xác định và null trong metadata. Phương pháp phải kiểm đúng statement/scope hiện hành.

## 3. Kết quả kiểm chứng hiện hành

Ghi kết luận mới nhất, validation_result và evidence của statement hiện tại. Unverified chưa có kết quả thì validation_result null. Validated/Invalidated cần owner, kết quả và evidence; không kể các lần kiểm trước. Retired ghi lý do hiện không còn dùng và dependency cần xử lý, không coi là đã chứng minh đúng. Đổi giả thuyết chưa kiểm lại thì không giữ Validated cũ.

## 4. Ảnh hưởng nếu sai

Ghi if_false, requirement/model/AC/contract hoặc kế hoạch bị ảnh hưởng và hướng xử lý cần đánh giá. Risk acceptance không làm giả định thành Validated.

## 5. Nơi sử dụng và bước tiếp

Dẫn consumer thực sự bằng typed trace_links; gap, receiver và bước refinement/review. Nếu cần authority chọn phương án/policy thì tạo Decision riêng vì khác bản chất, giữ ASM là record riêng với state hiện hành. Lịch sử kiểm/thay đổi nằm trong Git; không đổi kind hoặc dùng ASM ID làm DEC.

## Metadata

Dùng một block schema 2 cuối file, giá trị khớp nội dung trên. Nếu dùng register: thêm id/kind vào record trong records của metadata Project, giữ một nơi định nghĩa và anchor riêng theo ID. Không sao chép statement cũ hoặc thêm history array. Khi khai cả revision cấp artifact và cấp record, hai giá trị phải khớp.

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "ASM-CRM-001",
  "kind": "Assumption",
  "revision": "r1",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Scope cụ thể cần điền",
    "owner": null,
    "applicability": "Nghiệp vụ / sản phẩm",
    "evidence": [],
    "trace_links": [],
    "assumption_state": "Unverified",
    "statement": "Giả định hiện hành cần kiểm chứng",
    "basis": "Căn cứ hiện có, chưa là fact",
    "validation_method": "Cách kiểm đúng statement và evidence cần thu",
    "review_due": null,
    "validation_result": null,
    "if_false": "Ảnh hưởng và hướng đánh giá khi giả định sai"
  }
}
```
