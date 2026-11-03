# D08 — Ngoại lệ và edge cases

Mã tài liệu: **D08** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Cases phát hiện từ flow/state/data/permission/integration và nguồn vận hành
- **Reviewer thực hiện:** Với từng case ghi precondition/trigger/result/risk; kiểm vào AC/model nào; tìm case đặc biệt từ stakeholder/QA
- **Điều kiện dừng ở mức đặc tả:** Không có case trong scope chỉ có tên mà thiếu outcome; không có case bị loại mà thiếu reason/authority; không còn unknown chặn

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d08"></a>

### D08. Exception, edge case và tính nhất quán khi có lỗi

**Khi dùng:** mọi Epic/Story rà các chiều dưới đây; chỉ giữ các case áp dụng, loại trừ có lý do và reviewer.

| Chiều rà soát | Câu hỏi cần quyết | Expected result phải nêu |
|---|---|---|
| Input/domain | Thiếu, sai định dạng, biên, Unicode, null/empty? | Validation, phản hồi và dữ liệu có thay đổi không |
| Permission/data scope | Sai role, khác owner/tenant, quyền vừa bị đổi? | Allow/deny, data exposure và server behavior |
| Business state/order | Action ở state sai, command cũ hoặc out-of-order? | Transition/no-op/deny, state/data cuối |
| Duplicate/retry | Double click, request lặp, mất response sau commit? | Cách nhận biết cùng operation và tránh effect ngoài ý muốn |
| Concurrency/stale | Hai người sửa/duyệt, version cũ? | Ai thành công, conflict, atomicity và dữ liệu cuối |
| Integration | Timeout, downstream lỗi, callback trễ/trùng? | Commit/rollback/compensation/retry và người xử lý |
| Volume/time | Tập rỗng/lớn, giới hạn page/file, timezone/cuối kỳ? | Giới hạn, precision/order, tính nhất quán và cách đo |
| Partial completion | Lưu xong nhưng audit/notification lỗi? | Kết quả nghiệp vụ, pending side effect, recovery/alert |
| Migration/recovery | Dữ liệu legacy sai, restore/restart giữa chừng? | Tolerance, exception/reconcile và cách tiếp tục |
| User interruption | Refresh/back/cancel phiên hết hạn? | Dữ liệu đã/chưa lưu, cảnh báo và khả năng tiếp tục |

Mỗi case có ID, trigger/precondition, expected result, BR/AC refs và risk/priority. “Cần test timeout” chưa là đặc tả đầy đủ. Phải quyết timeout ở đâu, dữ liệu có commit không, caller được retry thế nào và bên nào chịu trách nhiệm recovery.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
