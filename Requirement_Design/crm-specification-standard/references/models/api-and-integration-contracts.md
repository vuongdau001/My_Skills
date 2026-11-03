# D07 — Contract API và tích hợp

Mã tài liệu: **D07** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Operations/events, hai đầu contract, commit boundaries; timeout/failure/duplicate/order
- **Reviewer thực hiện:** Diễn tập request thành công, lỗi trước/sau commit và mất response; chỉ rõ retry/recovery owner
- **Điều kiện dừng ở mức đặc tả:** Caller/callee biết response/effects/retry cho từng nhóm lỗi áp dụng; unknown có thể đổi contract không được để qua gate

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d07"></a>

### D07. API/integration contract và sequence

**Khi dùng:** có giao tiếp UI/API/module/hệ ngoài/async. Sequence diagram cần khi thứ tự, callback, commit và retry khó diễn đạt bằng vài bước; không bắt vẽ cho mọi API CRUD đơn giản.

**Trường tối thiểu:** producer/consumer owners, operation/version, request/response/schema, auth/permission, pre/postconditions, error semantics, timeout/retry/idempotency/order, transaction/consistency và backward compatibility liên quan.

**Review đủ:** biết thành công ở điểm nào; timeout trước/sau commit; retry có tạo trùng không; side effects nào được đồng bộ/async; partial failure/recovery và observability; identity/correlation và data classification phù hợp. Các ngưỡng timeout/retry/rate phải được chốt, không để Dev/AI tự chọn như rule nghiệp vụ.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
