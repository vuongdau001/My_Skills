# D09 — NFR, migration và vận hành

Mã tài liệu: **D09** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Control/metric và điều kiện đo; migration/reconcile/recovery obligations
- **Reviewer thực hiện:** Điền verification method, environment/data, threshold/control và owner; thử giải thích điều gì làm fail
- **Điều kiện dừng ở mức đặc tả:** Mọi obligation áp dụng có cách chấp nhận; không dùng “sẽ đo sau” thay ngưỡng/điều kiện chưa được chốt

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d09"></a>

### D09. NFR, migration và điều kiện vận hành

**NFR tối thiểu:** đối tượng/tác vụ, metric, threshold, workload/data volume, environment, thời điểm/cách đo và authority. Bảo mật/audit/retention/restore được diễn đạt bằng control kiểm chứng được, không buộc mọi yêu cầu chất lượng phải là số.

**Migration/transition tối thiểu khi áp dụng:** mapping/source version, Data Steward, quality thresholds, exceptions, trial/reconcile, cutover/rollback và ownership sau bàn giao. **Review đủ:** có người quyết dữ liệu, cách đối soát và điều kiện fail; không dùng “không mất dữ liệu” mà không định nghĩa tập dữ liệu và cách kiểm.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
