# Q03 — Nhất quán giữa các mô hình

Mã tài liệu: **Q03** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Thực hiện phép kiểm có thao tác, evidence và điều kiện kết luận.

**Đọc khi:** Review toàn bộ phải xét phép kiểm này; review riêng chỉ kết luận cho target này.


## Đầu vào, trách nhiệm và kết quả

Đầu vào: target/selected scope/revision, source/authority, model/contract refs và các câu hỏi/findings liên quan. BA/Business xác nhận nghiệp vụ, Dev/TL xác nhận kỹ thuật, QA phản biện và kiểm chứng; chọn reviewer theo target. Owner sửa findings; PM dùng verdict chuyên môn để xét gate, không ký thay expected behavior.

Thực hiện các bước bên dưới và lưu [review record](../../assets/templates/requirements-review-record-template.md). Đạt/Không đạt theo exit criteria của phép kiểm; thiếu input hoặc reviewer ghi Chưa kiểm. N/A chỉ khi phép kiểm không áp dụng cho target đã giới hạn, có reason và reviewer; không dùng N/A để che unknown. Gap chặn scope ngăn bàn giao. [Quy trình verdict](../requirements-review-process-and-verdicts.md).


<a id="spec-3-6"></a>

### Q03 — Kiểm nhất quán giữa các phát biểu và mô hình

**Cách kiểm:**

1. Chọn cùng một action và một bộ điều kiện cụ thể: actor, resource/owner, state/version, input và thời điểm/sequence liên quan.
2. Lần theo flow → state/decision → data/permission → contract → AC. Ghi bảng so sánh với ref cho từng output/guard.
3. So các expected result: allow/deny, target state, data mutation, response, audit/notification và recovery. Nếu cùng điều kiện dẫn hai kết quả trái nhau, mở finding.
4. So với parent/shared baseline. Kiểm alias/thuật ngữ, đơn vị/timezone, thứ tự ưu tiên rule và NFR. Hai requirement trùng nghĩa phải hợp nhất hoặc dẫn chung, không giữ hai bản độc lập rồi sửa lệch.
5. Business/technical authority giải quyết conflict; owner cập nhật mọi representation liên quan, reviewer kiểm lại cùng counterexample trước đóng finding.

| Action + điều kiện | Flow ref/result | Rule/state ref/result | Permission/contract ref/result | AC ref/result | Conflict / closure |
|---|---|---|---|---|---|
| Creator tự approve, hồ sơ Pending | … | … | … | … | … |

**Evidence:** cross-model comparison, conflict log và revision sau sửa. **Đạt khi:** các điều kiện áp dụng cho cùng tình huống cho kết quả tương thích; không có contradiction chưa giải quyết. **Không đạt khi:** nguồn nào cũng có chữ “approved” nhưng cho kết quả khác nhau.

**Ví dụ:** flow cho approve, permission cấm creator, AC chỉ nói success. Sửa một câu AC chưa đủ; phải sửa cả flow/guard/contract hoặc quyết định lại policy rồi rà toàn bộ refs.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
