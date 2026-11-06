# Mẫu quyết định nghiệp vụ/kỹ thuật

ID: TPL-DECISION · CRM Workflow Kit 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Đọc [knowledge records](../../references/knowledge-records-and-evidence.md). Cấp ID bằng next-id; giữ null nếu chưa có owner/thời điểm.


## Nội dung cần quyết định

Nêu một câu hỏi/lựa chọn rõ, scope/revision và context có nguồn. Tách nội dung đề xuất với quyết định authority đã chọn.

## Phương án và đánh đổi

Mỗi phương án có điều kiện, lợi ích/bất lợi. Ghi rationale và consequences của phương án được đề xuất/chọn; chưa chọn thì giữ Pending/Proposed.

**Phạm vi áp dụng** · Nghiệp vụ / sản phẩm hoặc Dự án / SDLC. Ghi rõ quyết định điều chỉnh hành vi sản phẩm hay cách thực hiện/bàn giao. [Cách phân loại](../../references/knowledge-records-and-evidence.md#record-applicability).

## Authority, evidence và ảnh hưởng

Ghi người phụ trách record và người có thẩm quyền quyết nội dung đó, cùng thời điểm và evidence khi có thật. Approved/Rejected cần authority, decided_at có timezone và nguồn pin đúng revision. Nối trace đến hồ sơ nghiệp vụ hoặc hồ sơ SDLC thực sự sử dụng quyết định.

## Lịch sử và bước tiếp

Khi thay quyết định: giữ record cũ Superseded, nối superseded-by; record mới nối supersedes, nêu scope/rationale. Không cấp lại ID hoặc sao approval cũ cho statement mới. Người soạn cập nhật consumers rồi review lại; reviewer không tự sửa target.

## Nếu dùng register

Đưa record vào records của metadata Project schema 2, bổ sung id/kind; không giữ đồng thời hai nơi định nghĩa. Dùng anchor ổn định khi cần dẫn mục.


<details>
<summary>Metadata mẫu — thay bằng giá trị thật</summary>

```crm-spec-kit
{
  "schema_version": 2,
  "artifact_id": "DEC-CRM-001",
  "kind": "Decision",
  "references": [],
  "record": {
    "revision": "r1",
    "scope": "Phạm vi cần xác nhận",
    "evidence": [],
    "trace_links": [],
    "owner": null,
    "decision_state": "Proposed",
    "statement": "Lựa chọn cần được quyết định",
    "context": "Vấn đề và nguồn cần giải quyết",
    "options": "Các lựa chọn và trade-off cần review",
    "rationale": "Căn cứ của phương án đề xuất",
    "consequences": "Tác động tích cực, tiêu cực và trung lập",
    "authority": null,
    "decided_at": null
  }
}
```

</details>
