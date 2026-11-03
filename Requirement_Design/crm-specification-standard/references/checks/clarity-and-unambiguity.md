# Q06 — Rõ nghĩa và không mơ hồ

Mã tài liệu: **Q06** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Thực hiện phép kiểm có thao tác, evidence và điều kiện kết luận.

**Đọc khi:** Review toàn bộ phải xét phép kiểm này; review riêng chỉ kết luận cho target này.


## Đầu vào, trách nhiệm và kết quả

Đầu vào: target/selected scope/revision, source/authority, model/contract refs và các câu hỏi/findings liên quan. BA/Business xác nhận nghiệp vụ, Dev/TL xác nhận kỹ thuật, QA phản biện và kiểm chứng; chọn reviewer theo target. Owner sửa findings; PM dùng verdict chuyên môn để xét gate, không ký thay expected behavior.

Thực hiện các bước bên dưới và lưu [review record](../../assets/templates/requirements-review-record-template.md). Đạt/Không đạt theo exit criteria của phép kiểm; thiếu input hoặc reviewer ghi Chưa kiểm. N/A chỉ khi phép kiểm không áp dụng cho target đã giới hạn, có reason và reviewer; không dùng N/A để che unknown. Gap chặn scope ngăn bàn giao. [Quy trình verdict](../requirements-review-process-and-verdicts.md).


<a id="spec-3-9"></a>

### Q06 — Kiểm không mơ hồ và một nghĩa chấp nhận rõ

**Cách kiểm:**

1. Rà các từ/điều kiện có nhiều nghĩa: “hợp lệ”, “phù hợp”, “nhanh”, “tất cả”, “hiện tại”, “v.v.”, “và/hoặc”, “nếu cần”. Mỗi từ phải được định nghĩa hoặc thay bằng rule/giá trị/constraint có ref.
2. Chốt actor, đối tượng, phạm vi quantifier, đơn vị, timezone, normalization, thứ tự priority và thời điểm áp dụng. Không để “khách hàng trùng” vừa nghĩa cùng tên vừa nghĩa cùng MST ở hai nơi.
3. Tách các nghĩa độc lập thành ID có thể review/verify riêng. Một constraint nguyên tử như transaction phải ghi state + audit nhất quán có thể chứa nhiều effect; không tách máy móc làm mất invariant.
4. Cho Dev và QA diễn giải độc lập cùng requirement bằng một ví dụ. So phần điều kiện/expected result; nếu khác nhau, hỏi source/authority và sửa diễn đạt, không chỉ ghi “đã trao đổi miệng”.
5. Kiểm template/naming/section phù hợp và nội dung hiểu được với người dùng hồ sơ. Sửa typo/alias nếu làm thay đổi nghĩa hoặc refs.

**Evidence:** glossary/normalized statement, clarification decision, read-back của người nhận và finding closure.

**Đạt khi:** các điểm có thể gây cách hiểu khác đã được giải quyết; người nhận có thể mô tả cùng hành vi/giới hạn từ hồ sơ. **Không đạt khi:** chỉ đồng ý “đã hiểu” mà Dev/QA đưa expected result khác nhau.

**Ví dụ:** “AM sửa được hồ sơ của mình” phải xác định “của mình” là creator hay current owner, các state được sửa, field nào và xử lý ownership đổi giữa chừng nếu áp dụng.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
