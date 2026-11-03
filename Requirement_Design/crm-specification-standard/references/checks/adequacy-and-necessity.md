# Q01 — Đúng nhu cầu và sự cần thiết

Mã tài liệu: **Q01** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Thực hiện phép kiểm có thao tác, evidence và điều kiện kết luận.

**Đọc khi:** Review toàn bộ phải xét phép kiểm này; review riêng chỉ kết luận cho target này.


## Đầu vào, trách nhiệm và kết quả

Đầu vào: target/selected scope/revision, source/authority, model/contract refs và các câu hỏi/findings liên quan. BA/Business xác nhận nghiệp vụ, Dev/TL xác nhận kỹ thuật, QA phản biện và kiểm chứng; chọn reviewer theo target. Owner sửa findings; PM dùng verdict chuyên môn để xét gate, không ký thay expected behavior.

Thực hiện các bước bên dưới và lưu [review record](../../assets/templates/requirements-review-record-template.md). Đạt/Không đạt theo exit criteria của phép kiểm; thiếu input hoặc reviewer ghi Chưa kiểm. N/A chỉ khi phép kiểm không áp dụng cho target đã giới hạn, có reason và reviewer; không dùng N/A để che unknown. Gap chặn scope ngăn bàn giao. [Quy trình verdict](../requirements-review-process-and-verdicts.md).


<a id="spec-3-4"></a>

### Q01 — Kiểm đúng nhu cầu và sự cần thiết

**Câu hỏi cần trả lời:** requirement này thể hiện đúng điều được cần/được quyết định chưa, và có thuộc phạm vi được giao không?

**Các bước reviewer thực hiện:**

1. Từ từng BR/AC/constraint, mở parent need hoặc decision/source đã dẫn; kiểm nguồn có authority và còn hiệu lực cho scope này.
2. Ghi mục đích của requirement: nếu bỏ nó thì mục tiêu/control nào không đáp ứng? Nếu không giải thích được, yêu cầu BA làm rõ rationale thay vì tự kết luận cần thiết.
3. Business đọc lại bằng một ví dụ thành công và phản ví dụ/từ chối, chốt expected result; QA/Dev đối chiếu cách hiểu. Với yêu cầu kỹ thuật/control, đúng technical/control authority xác nhận.
4. Tách requirement nghiệp vụ khỏi lựa chọn thiết kế. Nếu một công nghệ/giải pháp là constraint bắt buộc, ghi nguồn/authority của constraint; nếu chỉ là phương án, chuyển sang solution/rationale.
5. Khi nguồn/nhóm stakeholder mâu thuẫn, ghi conflict và người phân xử; không chọn ý kiến cuối cùng trong comment làm chân lý.

**Evidence:** link nguồn/parent, rationale, ví dụ + phản ví dụ, authority/verdict đúng revision; conflict đã đóng.

**Đạt khi:** mỗi yêu cầu trong target có rationale/source được chấp nhận, đúng scope và có authority xác nhận nghĩa/expected result. **Không đạt khi:** chỉ có nhãn Approved, chỉ có BA/AI tự suy ra hành vi hoặc chưa giải quyết xung đột.

**Ví dụ:** rule “người tạo được tự duyệt” không Đạt chỉ vì được diễn đạt rõ. Business/control owner phải xác nhận có cho tự duyệt hay không và phạm vi nào; kết quả đó mới làm cơ sở model/quyền/AC.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
