# Q05 — Truy vết và quản lý phiên bản

Mã tài liệu: **Q05** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Thực hiện phép kiểm có thao tác, evidence và điều kiện kết luận.

**Đọc khi:** Review toàn bộ phải xét phép kiểm này; review riêng chỉ kết luận cho target này.


## Đầu vào, trách nhiệm và kết quả

Đầu vào: target/selected scope/revision, source/authority, model/contract refs và các câu hỏi/findings liên quan. BA/Business xác nhận nghiệp vụ, Dev/TL xác nhận kỹ thuật, QA phản biện và kiểm chứng; chọn reviewer theo target. Owner sửa findings; PM dùng verdict chuyên môn để xét gate, không ký thay expected behavior.

Thực hiện các bước bên dưới và lưu [review record](../../assets/templates/requirements-review-record-template.md). Đạt/Không đạt theo exit criteria của phép kiểm; thiếu input hoặc reviewer ghi Chưa kiểm. N/A chỉ khi phép kiểm không áp dụng cho target đã giới hạn, có reason và reviewer; không dùng N/A để che unknown. Gap chặn scope ngăn bàn giao. [Quy trình verdict](../requirements-review-process-and-verdicts.md).


<a id="spec-3-8"></a>

### Q05 — Kiểm truy vết, phiên bản và khả năng sửa đổi

**Cách kiểm:**

1. Lập danh sách ID thuộc target: need/BR/AC/model/contract và selected scope. Kiểm ID duy nhất, refs resolve được, source/version đúng.
2. Đi ngược từ từng requirement tới nhu cầu/quyết định; đi xuôi tới model/AC/Story và verification condition theo giai đoạn. Kiểm dependency/shared rule theo cả hai chiều.
3. Phân biệt phần kế thừa với delta. Nội dung dùng chung có một nguồn chuẩn; bản sao có thể lệch phải bỏ hoặc thay bằng ref có version.
4. Trước triển khai, liên kết code/run có thể là “chưa có — chưa triển khai”; phải có planned allocation/verification. Sau triển khai, bổ sung PR/SHA/build/test run/verdict thực tế và đối soát baseline được kiểm.
5. Thử impact query bằng tay: đổi BR-X thì xác định được model/Story/test nào phải xem lại? Nếu không, finding chưa đóng. Đổi revision phải invalidate/check lại đúng phạm vi, không gắn kết quả cũ cho version mới.

**Evidence:** RTM/allocation table, ref integrity result, pin commit/selected-scope và một impact walkthrough.

**Đạt khi:** refs phù hợp giai đoạn đều truy được, không có yêu cầu đang thực hiện vô nguồn hoặc không có planned verification, và tìm được đối tượng phụ thuộc khi đổi. **Không đạt khi:** URL tồn tại nhưng trỏ revision khác, hoặc một label được dùng thay tất cả các quan hệ.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
