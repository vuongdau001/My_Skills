# Ví dụ finding và phản ví dụ khi review

Mã tài liệu: **EX-REVIEW** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Phân biệt đủ hình thức với đủ điều kiện đặc tả.

**Đọc khi:** Cần mẫu finding hoặc kiểm state coverage có căn cứ.


<a id="spec-3-12"></a>

### Ví dụ kiểm đủ state transition: từ nhận xét tới finding có căn cứ

Dùng shared lifecycle minh họa tại mục [Ví dụ liên kết Epic → Story → model → AC → test condition](project-code-request-specification.md#spec-9): 5 business states và 4 command. Với **operation mới**, inventory có 5 × 4 = 20 cặp state–command:

| State / command mới | submit | approve | reject | cancel |
|---|---|---|---|---|
| Draft | MOD-CRM-001 nếu guard đạt | Denied | Denied | MOD-CRM-004 nếu guard đạt |
| PendingApproval | Denied | MOD-CRM-002 nếu guard đạt | MOD-CRM-003 nếu guard đạt | Denied |
| Approved | Denied | Denied | Denied | Denied |
| Rejected | Denied | Denied | Denied | Denied |
| Cancelled | Denied | Denied | Denied | Denied |

**Reviewer phải làm tiếp, không dừng ở bảng này:**

1. Xác nhận với Business rằng 5 states/4 commands đúng và các terminal state không có reopen/resubmit trong scope.
2. Đối chiếu 4 ô transition với diagram, guard và side effects. 16 ô còn lại phải có rule từ chối và contract/error group, không chỉ bỏ trống.
3. Với MOD-CRM-001, liệt kê guard partitions: đúng/sai auth, role, owner, data, current state/version; thứ tự lỗi theo decision rules. Dùng trường hợp chỉ một điều kiện sai khi cần để không che lỗi.
4. Xét replay riêng với operation đã ghi, không nhập nhằng với submit mới ở PendingApproval. Cùng key/payload, key trùng payload khác, đổi quyền, mất response và hai key cạnh tranh đều có expected result theo applicability.
5. Map các dòng và nhóm guard/failure tới AC/test conditions của scope Story. Story submit chọn cột submit và related guards/replay; approve/reject/cancel có allocation khác. Spec Epic vẫn giữ model chung.
6. Ghi finding theo evidence. Với `F-STATE-01`, bảng và đặc tả đều ghi `PendingApproval × cancel = Denied` và giữ nguyên state. Khi review scope cancel, chỉ ra phần chưa rõ là contract phản hồi cho nhóm từ chối này. Đóng finding khi có contract và AC tương ứng được xác nhận, rồi review lại đúng revision.

**Kết luận được phép:** 20/20 cặp đã có disposition, 4 transition có guard/effect, những nhóm guard/replay/failure áp dụng có outcome và allocation, nguồn/authority đã xác nhận. Đây là coverage của mô hình/đặc tả đã rà, chưa phải 20 test đã chạy hoặc chứng minh mọi tổ hợp toàn hệ thống.

**Chưa được kết luận Đạt nếu:** còn một command chưa xác nhận, ô denied chưa biết response/effect, hoặc chỉ có success paths. Không chấm “có sơ đồ state machine” là đủ.

**Áp dụng ngay vào ví dụ mục [Ví dụ liên kết Epic → Story → model → AC → test condition](project-code-request-specification.md#spec-9):** bỏ expected result ở nhánh dữ liệu sai như [bài tập review](project-code-request-specification.md#spec-9-4). Q02/Q04 có finding tại E03/E14 dù binding và bảng state–command hợp lệ. Ở r2, freshness/hiển thị chưa rõ còn chặn scope đọc trạng thái. Q01 cũng chưa được coi Đạt vì các rule ví dụ chưa có Business authority thật xác nhận. Đây là ví dụ học cách đặc tả/review, không phải một hồ sơ đã được duyệt để triển khai.


<a id="spec-11"></a>

## Ví dụ cách kết luận review đạt hoặc chưa đạt

| Hạng mục | Có nội dung nhưng chưa đạt | Đạt ở mức đặc tả khi |
|---|---|---|
| Flow | Có sơ đồ nhưng mọi lỗi đều tới một nút “Error” | Các nhóm lỗi/alternate quan trọng có expected outcome, owner và postcondition |
| State | Có các state và mũi tên hợp lệ | Biết guards, quyền, forbidden/no-op/replay và effect; diagram/table nhất quán |
| Edge case | Ghi “test double click, timeout” | Có preconditions, điểm thất bại, response/state/data/effects và cách recover |
| Data | Ghi “MST bắt buộc và duy nhất” | Định nghĩa normalize/domain, phạm vi uniqueness, trạng thái/legacy và concurrency liên quan |
| Permission | Ghi “chỉ AM tạo được” | Có ownership/data scope/server enforcement/deny outcomes liên quan |
| AC | Ghi “API hoạt động đúng” | Có input/action/output, source refs và cách kiểm chứng cụ thể |
| Solution | Có tên API/bảng DB | Giải thích delta, constraint, boundary, dependency/risk và đủ feasibility cho scope chọn |
| NFR | Ghi “nhanh và an toàn” | Có tiêu chí/điều kiện đo hoặc control, người xác nhận và phương pháp kiểm |

“Đạt ở mức đặc tả” chỉ xác nhận đầu vào đủ rõ cho bước sau. Nó khác “phần mềm đã đạt AC/DoD”, vốn cần evidence của review/code/test/bản chạy thực tế.


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../standards-and-crm-tailoring.md).
