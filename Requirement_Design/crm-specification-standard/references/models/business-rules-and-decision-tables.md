# D03 — Business rules và bảng quyết định

Mã tài liệu: **D03** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Xác định hồ sơ, inventory và cách kiểm đủ cho mô hình này.

**Đọc khi:** Model áp dụng cho scope hoặc cần review delta của model được kế thừa.


## Inventory, phép kiểm và điều kiện dừng

- **Inventory/đơn vị rà:** Domains của conditions; các rule/tổ hợp khả thi; overlap/default
- **Reviewer thực hiện:** Lập bảng đầy đủ hoặc compact có lý do gộp; so constraint loại trừ và ưu tiên; chọn witness input cho mỗi rule
- **Điều kiện dừng ở mức đặc tả:** Không còn tổ hợp khả thi chưa biết outcome; overlap/default rõ; mỗi rule trong scope có ít nhất một witness hoặc lý do chứng minh infeasible

**Đầu vào:** scope/revision, nguồn/authority, model hiện có và delta. **Evidence:** inventory có ID/disposition, witness/counterexample, output refs, findings và reviewer closure.

Nếu thiếu input ghi **Chưa kiểm**; có gap/mâu thuẫn ghi **Không đạt**; chỉ N/A khi không áp dụng có lý do và reviewer. Mọi gap chặn scope ngăn bàn giao.


<a id="spec-d03"></a>

### D03. Business rules và decision table

**Khi dùng:** mọi rule có ID và nguồn; bảng quyết định cần khi nhiều điều kiện ảnh hưởng kết quả hoặc có ưu tiên/ngoại lệ dễ bỏ sót.

**Trường tối thiểu:** BR ID, source/authority, điều kiện/phạm vi, kết quả, ngoại lệ, priority/default; với decision table có condition domains, rule rows/columns và expected actions.

**Review đủ:** điều kiện được định nghĩa; tổ hợp khả thi trong scope có kết quả; tổ hợp bị loại có constraint chứng minh; rule chồng lấn có priority hoặc cùng kết quả đã xác nhận; có default; ví dụ không mâu thuẫn flow/state/data/permission.

Không cần brute-force mọi tổ hợp toàn hệ thống. Nhóm điều kiện/tối giản phải giữ đúng nghĩa và có lý do; QA/Business xác nhận phần được gộp và residual risk. Bảng mẫu dùng dạng một dòng cho một rule là cách trình bày của CRM, không bắt buộc cùng layout mọi nguồn.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
