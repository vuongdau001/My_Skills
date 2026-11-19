# Mẫu register policy dự án

Mã tài liệu: **TPL-POLICY** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

**Bố cục:** Bảng chỉ làm index ngắn; policy dài tách từng ID với applicability/authority/evidence/gap. Không làm Pending trông như Approved. Xem [phân cấp Markdown chung](../../references/artifact-writing-standard.md#13-phân-cấp-thị-giác-bằng-markdown-thuần).

Mở bằng mục đích, phạm vi và tình trạng hiệu lực chung. Ghi project/workstream, revision, owner/authority, nguồn tổ chức/hợp đồng, effective date và revision áp dụng nào dùng register.

Đọc [policy guide](../../references/project-policy-register.md); dùng các POL IDs chuẩn. Không lấy policy của kit/ví dụ làm policy dự án đã duyệt.

## Danh mục tra policy

| Policy ID / tên | Scope và version | Trạng thái / record liên quan |
|---|---|---|
| ID thực từ guide | Phạm vi thực | Pending nếu thiếu quyết định |

Thêm index ngắn cho Assumption, Constraint và Decision lấy từ đầu vào. Ghi ID/revision hiện hành, source locator, scope áp dụng và disposition dùng lại/có điều kiện/cần xác nhận. Dẫn record canonical và giữ câu hỏi còn mở cùng authority.

## Chi tiết từng policy

Mỗi policy một mục:

- **Mục đích/applicability:** nội dung điều chỉnh, định nghĩa và ví dụ ở ranh giới.
- **Phương pháp:** input/output, cách tính, đơn vị/clock, threshold nếu được quyết.
- **Trách nhiệm:** owner, reviewer/authority và ngày hiệu lực.
- **Evidence/quyết định:** refs/version, trạng thái, cách xử lý thiếu/failed/skipped.
- **Ảnh hưởng:** gate bị chặn và impact khi đổi; gap/owner/due.

## Ngoại lệ khi policy cho phép

Ghi điều khoản/version, scope/revision, lý do/tác động, compensating checks, điều kiện không được miễn, authority/decision, expiry và owner xem lại. Chưa duyệt thì chưa được coi đã miễn.

Kết thúc bằng metadata Project/record phù hợp; chưa có approval vẫn giữ Pending.

Áp dụng [hồ sơ hiện hành](../../references/current-state-and-history.md): cập nhật vị trí canonical theo target/scope, không tạo file theo lần chạy hoặc timeline. Review/check không tự sửa target; evidence stale phải được đánh giá lại.
