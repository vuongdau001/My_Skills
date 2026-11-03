# D10 — Solution, phân rã Story và testability

Mã tài liệu: **D10** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Components/delta/contracts, assumptions/dependencies; BR/AC → Story allocation
- **Reviewer thực hiện:** Read-back solution và tác động, kiểm reality/dependency; thử đi từ rule đến Story/verification
- **Điều kiện dừng ở mức đặc tả:** Không có gap scope/assumption chặn; feasible cho scope chọn; các Story không bỏ rule bắt buộc hoặc tính scope trùng

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d10"></a>

### D10. Solution, decomposition và testability

**Trường tối thiểu:** hiện trạng, delta/components/interfaces, phương án/rationale, contract refs, assumptions/risk, dependency owners và evidence feasibility; phương án Story có outcome, scope, BR/AC/model refs và estimate.

**Review đủ:** Dev/TL đọc lại rule bằng solution cụ thể; BA xác nhận hiểu khớp; QA nêu cách setup/observe/assert. Không cần thiết kế mọi dòng code trước baseline. Nếu chưa chứng minh được điều kiện quan trọng, ghi câu hỏi/blocker hoặc thực hiện nghiên cứu có timebox; không dùng từ “solution checked” để che giả định.

INVEST hỗ trợ review cách chia Story; nó không xác nhận toàn bộ model/contract đúng hoặc tự chứng minh Story đã đạt DoR.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
