# D02 — Vòng đời và chuyển trạng thái nghiệp vụ

Mã tài liệu: **D02** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Tập state × command; guard partitions; replay/stale/concurrency khi áp dụng
- **Reviewer thực hiện:** Điền từng ô thành valid transition/no-op/denied/infeasible có reason; đối chiếu diagram/table/permission; thêm guard-fail conditions
- **Điều kiện dừng ở mức đặc tả:** Mọi ô của tập state–command được chọn có disposition; transitions có target/effect; các guard/exception quan trọng có expected result và verification condition

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d02"></a>

### D02. State transition và vòng đời nghiệp vụ

**Khi dùng:** đối tượng có lifecycle, trạng thái quyết định action được phép, hoặc sự kiện/approval làm thay đổi trạng thái. State nghiệp vụ khác trạng thái màn hình tạm và status Jira.

**Trường tối thiểu:** entity, state ID/name/meaning, initial/terminal states, invariant; transition ID, source, event/command, actor, guard, target, data changes/side effects; hành vi khi guard fail hoặc command không hợp lệ.

| Transition ID | Từ state | Event / actor | Guard | Sang state | Output / side effect | Khi bị từ chối / N/A |
|---|---|---|---|---|---|---|
| TR-… | … | … | … | … | … | … |

**Review đủ:**

- [ ] State có nghĩa khác nhau, có đường đi tới được và invariant rõ; initial/terminal và đường phục hồi đã được xét.
- [ ] Với mỗi state và command trong scope, ghi disposition: transition, no-op/replay, denied hoặc không khả thi có lý do; không để ô trống vì chưa biết.
- [ ] Guard và quyền được tách rõ: đúng role chưa đủ nếu state/ownership không đúng.
- [ ] Ghi kết quả khi nhận command sai thứ tự, lặp, stale hoặc hai command cạnh tranh.
- [ ] Diagram và bảng transition cùng một tập ID/version; nếu khác nhau phải sửa trước review đạt.
- [ ] QA có test condition cho chuyển hợp lệ và những lệnh bị cấm/guard fail theo risk scope; không chỉ kiểm có đi qua từng state.

State diagram và state table giúp nhìn vòng đời từ hai góc. Bảng chi tiết phải giải thích cả hành vi từ chối; chỉ vẽ mũi tên hợp lệ chưa đủ để Dev tự quyết lỗi trả về. Các nguyên tắc mô hình sự kiện/điều kiện và rà transition tham khảo ISTQB; bộ trường/review này là quy định CRM. [ISTQB CTFL, 4.2.4](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf).


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
