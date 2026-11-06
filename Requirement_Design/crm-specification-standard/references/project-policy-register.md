# Policy dự án: khai báo, phê duyệt và áp dụng vào gate

Mã tài liệu: **CRM-POLICY** · Gói CRM 1.3.1 · 03/11/2026

**Đọc khi:** thiết lập dự án, xét DoR/DoD, chọn độ sâu review/test hoặc giải quyết policy còn thiếu. **Đầu vào:** constraints tổ chức/hợp đồng, scope, hệ thống thực tế và authority. **Đầu ra:** register policy được duy trì trong repo dự án, version refs trên baseline/Story và các câu hỏi chưa chốt.

## Phân biệt chuẩn dùng lại và quyết định dự án

Register này ghi policy **Dự án / SDLC** dùng cho review, kiểm thử, baseline và bàn giao. Policy chi phối hành vi hoặc quyền trong CRM thuộc **Nghiệp vụ / sản phẩm** và được dẫn tại Capability, Epic hoặc model áp dụng. Khi một chính sách tổ chức ảnh hưởng cả hai phạm vi, tách các điều khoản áp dụng và giữ liên kết đến nguồn chung. [Phạm vi áp dụng của record](knowledge-records-and-evidence.md#record-applicability).

Gói này quy định **cách khai báo/kiểm policy**, không tự phê duyệt ngưỡng CRM. Copy [mẫu register](../assets/templates/project-policy-register-template.md) vào repo dự án và điền bằng quyết định thật. Repo/đường dẫn dự án chưa xác định phải ghi thiếu input; không ghi policy Approved ngay trong gói chỉ vì người dùng đồng ý cập nhật tài liệu.

Severity, risk, SLA, required checks là các policy khác nhau. Không dùng một con số chung thay cả bốn. Tham chiếu policy phải có ID, version/effective scope và authority; “theo policy dự án” không kèm ref chưa đủ qua gate. Giá trị gợi ý chỉ là Proposed, không có hiệu lực mặc định.

## Các nhóm policy phải đánh giá applicability

| ID/tên | Nội dung phải được quyết định | Authority xác nhận | Gate/hoạt động ảnh hưởng |
|---|---|---|---|
| <a id="pol-severity"></a>POL-SEVERITY — Phân loại ảnh hưởng lỗi | Định nghĩa Critical/Major/Minor theo tác động dữ liệu, an toàn/control, phạm vi người dùng, gián đoạn và khả năng workaround; ví dụ/ranh giới, cách giải quyết tranh chấp | QA lead + Business/control/TL theo tác động | Story/Epic completion, defect triage |
| <a id="pol-priority"></a>POL-PRIORITY — Thứ tự xử lý | Cách kết hợp urgency, dependency và business priority; ai sắp thứ tự | PM/Business | Planning và xử lý lỗi; priority không thay severity |
| <a id="pol-risk"></a>POL-RISK — Đánh giá và mức kiểm | Cách đánh giá tác động/khả năng xảy ra, input/evidence, phân mức; mỗi mức đòi review/model/test nào; ai được xác nhận loại trừ | TL + QA + Business/control authority | Applicability, test approach, gate liên quan |
| <a id="pol-quality"></a>POL-QUALITY — Chất lượng và completion | Quy định defect mở, review/code/test/doc/migration cần có; liên kết severity và risk policy; phần bắt buộc không được miễn | TL/QA/Business; PM chốt áp dụng | Dev handoff, Story/Epic DoD |
| <a id="pol-checks"></a>POL-CHECKS — Required checks | Tên/job ID chính xác, trigger, scope, pass/fail, evidence/build refs, owner; skipped/not-run khác passed | TL + CI owner + QA | Merge/code handoff; kiểm thật cần khảo sát repo/CI |
| <a id="pol-review"></a>POL-REVIEW — Thời hạn review và escalation | Ai nhận queue, mốc bắt đầu/dừng, lịch làm việc/timezone, SLA theo loại review, backup, khi quá hạn báo ai | PM + các reviewer có trách nhiệm | Review queue; quá hạn không tự Approved |
| <a id="pol-blocker"></a>POL-BLOCKER — Theo dõi blocker | Quy tắc mở/đóng, owner, clock, ngưỡng aging, escalation, giữ lịch sử reopen | PM + leads | Báo cáo và điều phối; không đổi nghĩa Jira pending |
| <a id="pol-evidence"></a>POL-EVIDENCE — Bằng chứng và quyền | Nơi lưu, access, retention, ràng buộc evidence với người thực hiện, revision và build; dữ liệu nhạy cảm, quyền đọc và thời điểm hết hiệu lực | Data/security/technical authority | Review/gate/evidence validation |
| <a id="pol-exception"></a>POL-EXCEPTION — Ngoại lệ | Policy nào có thể/không thể miễn, authority, scope/revision, compensating checks, hạn hết hiệu lực, cách xem lại | Authority của policy + PM trong thẩm quyền | Chỉ gate được chỉ rõ; không áp dụng waiver ngầm |

Đây là các nhóm cần làm rõ, chưa là giá trị policy được phê duyệt. Nhóm không áp dụng phải có reason và authority; không có môi trường CI thật không có nghĩa required checks được N/A nếu định bàn giao code.

## Risk-based review phải thực hiện thế nào?

1. Liệt kê các đường/hành vi/control trong scope; xét khả năng mất/sai dữ liệu, truy cập trái quyền, giao dịch không nhất quán, lỗi integration, gián đoạn luồng chính, migration/khôi phục và các nghĩa vụ bắt buộc. Ghi bên liên quan nghiệp vụ chịu tác động và vai trò SDLC phụ trách phép kiểm.
2. Ghi kịch bản lỗi và hệ quả, nhóm bị ảnh hưởng, giả định về tần suất/khả năng, evidence và uncertainty. Không tự đặt điểm khi chưa có cách chấm được duyệt.
3. Áp dụng POL-RISK đã có hiệu lực. Nếu chưa có, vẫn ghi risk facts và câu hỏi; chưa kết luận scope kiểm là đủ để qua gate phụ thuộc policy.
4. Với từng risk, xác định model/check/test condition/verification method và reviewer cần thiết. Dùng [mapping](catalog-check-model-mapping.md); không mặc định “low risk” được bỏ quyền hay AC bắt buộc.
5. Ghi coverage được chọn, residual risk, reason của loại trừ và authority; unknown ngữ nghĩa chặn scope phải được giải quyết, không đổi thành risk accepted để gọi requirement Đạt.

“Đường quan trọng” phải được nhận diện bằng rule/flow/AC ID, lý do tác động và owner xác nhận, không chỉ đánh nhãn. Policy không nhất thiết dùng ma trận số; dù định tính vẫn phải có định nghĩa/ranh giới và ví dụ để reviewer áp dụng nhất quán.

## Các bước kiểm register trước sử dụng

1. Mở policy ref và kiểm nội dung/version/effective date/scope; không chỉ kiểm link tồn tại.
2. Kiểm trạng thái decision: Pending/Proposed/Approved/Superseded cùng evidence và authority. Đây là metadata tài liệu, không là Jira status mới.
3. Đối chiếu policy với constraints cấp cao hơn và gate đang xét; khi mâu thuẫn ghi conflict và đúng authority giải quyết, không tự chọn policy dễ đạt hơn.
4. Kiểm policy có phương pháp đánh giá, dữ liệu đầu vào, người chịu trách nhiệm và expected disposition cho thiếu evidence/failed/skipped.
5. Ghi policy IDs/versions được áp dụng vào review/gate record. Thay policy phải impact review các công việc đang làm; approval/evidence cũ giữ lịch sử, không tự tái sử dụng cho version mới.

**Đạt để áp dụng:** đầy đủ nội dung áp dụng, đúng authority/version, không còn conflict/chỗ trống làm thay đổi kết luận gate. **Chưa kiểm:** không có input/evidence/authority. **Không đạt:** policy mâu thuẫn hoặc không thể áp dụng nhất quán. Policy bắt buộc còn Pending thì gate liên quan chưa thể đạt; tiếp tục công việc độc lập không phụ thuộc nó.

**Ranh giới ngoại lệ:** không hạ severity để qua gate; không dùng AI PASS hoặc SLA hết hạn làm approval; không dùng waiver để đổi expected behavior mà bỏ change control. Nếu yêu cầu bắt buộc đổi, cập nhật baseline và acceptance theo đúng thẩm quyền.

Liên quan: [Gate/authority](readiness-completion-and-approval-gates.md), [AI/hard gates](ai-handoff-and-hard-gates.md), [Nguồn và CRM tailoring](standards-and-crm-tailoring.md).
