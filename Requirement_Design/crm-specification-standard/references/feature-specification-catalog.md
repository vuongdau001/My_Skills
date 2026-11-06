# Danh mục nội dung và tiêu chí Feature

Mã tài liệu: **CRM-FEATURE** · Gói CRM 1.3.1 · 03/11/2026

**Đọc khi:** tiếp nhận năng lực/phạm vi, phân rã thành Epic, nghiệm thu liên Epic. **Đầu vào:** nhu cầu và source có authority, constraints, các Epic hiện có. **Đầu ra:** Feature brief, scope allocation, phương pháp acceptance và quyết định; dùng [mẫu Feature](../assets/templates/feature-specification-template.md).

Feature chỉ ở Git. Không tạo issue type hay status mới. Không bắt một Feature có nhiều Epic, không viết lại state machine/data/API đã thuộc Epic/shared models; dẫn đúng revision.

| ID/tên | Nội dung cần có | Phép kiểm và điều kiện đủ | Người chuẩn bị/xác nhận |
|---|---|---|---|
| <a id="f01"></a>F01 — Nguồn và vấn đề | Feature ID, source, vấn đề/cơ hội, rationale, sponsor/authority | Đi ngược tới nguồn; giải thích ai gặp vấn đề và vì sao cần scope; không dùng ý kiến AI làm nguồn đã duyệt | BA / Business |
| <a id="f02"></a>F02 — Outcome và cách đánh giá | Kết quả mong muốn, population, phương pháp xác nhận; KPI nếu áp dụng | Reviewer nêu được điều kiện đạt/không đạt; KPI có unit/baseline hoặc kế hoạch đo/target/window/owner; missing target ảnh hưởng gate phải ghi Pending | Business + BA / đúng authority |
| <a id="f03"></a>F03 — Stakeholder và authority | Nhóm hưởng lợi/vận hành/control, nhu cầu, người đại diện và quyền quyết | Đối chiếu actor/output/impact để tìm nhóm bị bỏ sót; conflict có người phân xử và decision | BA / Business và leads |
| <a id="f04"></a>F04 — Phạm vi và ranh giới | In/out scope, assumptions/constraints, phạm vi giao từng giai đoạn | Mỗi item được giữ/loại/trì hoãn có quyết định; không loại dependency cần thiết khỏi scope để làm giả readiness | BA + PM / Business |
| <a id="f05"></a>F05 — Requirement/control dùng chung | IDs/versions của rule, NFR, data/permission/integration/transition chung | Tìm Epic/Story áp dụng; không có hai policy trái nhau hoặc control bắt buộc chưa được phân bổ; model chi tiết tham chiếu | BA + TL/QA / authority nội dung |
| <a id="f06"></a>F06 — Phân bổ Epic và dependency | Scope item → Epic, outcome từng Epic, dependency, owner/capacity/mốc sơ bộ | Đi qua từng scope item: có Epic nhận hoặc gap; tìm trùng/giao thoa và cam kết dependency; không đòi estimate chi tiết mọi Story từ đầu | BA + Dev/QA / PM |
| <a id="f07"></a>F07 — Acceptance liên Epic | Điều kiện nghiệm thu sản phẩm, hành trình liên Epic, data/control chung, phương pháp kiểm | Có expected result/observation cho mỗi AC; luồng giao thoa được phân bổ kiểm; Epic Done không tự thay acceptance Feature | BA + QA / Business, TL phần kỹ thuật |
| <a id="f08"></a>F08 — Quyết định, baseline và nghiệm thu | Revision/scope, policy refs, approvals, open questions, acceptance/evidence refs theo bước | Không có câu hỏi chặn bị giấu; decision đúng authority/revision; khi bàn giao đủ scope/evidence và Business acceptance | BA điều phối / PM + Business |

Với F04/F06, dùng [checkpoint nguồn scope](source-scope-and-decomposition-checkpoint.md) khi tiếp nhận inventory hoặc thay allocation. Rationale cần dựa outcome/model/control/acceptance; mapping một owner chính trên mỗi dòng nguồn chưa chứng minh mọi fragment đã được bao phủ.

Khi tạo/đổi F04/F06, áp dụng [checkpoint chọn cấp và quan hệ cha–con](source-scope-and-decomposition-checkpoint.md#level-selection). Đối chiếu năng lực với Feature hiện có; kiểm cha–con lặp nghĩa và giải thích quan hệ một–một nếu có. Rationale thiếu là phần cần làm rõ; cây có outcome trùng nhưng không có vai trò riêng là finding phân rã.

## Cách review theo bước, không đòi đầy đủ quá sớm

1. **Cho phép làm rõ/phân rã:** F01–F04 có khung đủ giao việc, F06 có kế hoạch/owner, F08 ghi authority/questions. F05/F07 còn discovery được ghi rõ. Áp dụng DoR Feature hiện có; không tuyên bố đã đủ để code.
2. **Chốt phạm vi cho Epic:** scope chọn của F01–F08 được làm rõ tương ứng; các shared requirement ảnh hưởng phải có nguồn/quyết định; F06 không có gap allocation bị che. Epic tiếp tục làm chi tiết E01–E16 và baseline trước Story.
3. **Hoàn tất phân tích toàn Feature:** mọi phạm vi hiện hành đều có baseline yêu cầu/solution tương ứng, allocation và acceptance đủ; phần chưa rõ không được lờ đi. Chốt một phần không bằng hoàn tất toàn bộ.
4. **Nghiệm thu Feature:** kiểm F07/F08 và toàn scope theo [gate Feature](readiness-completion-and-approval-gates.md#workflow-7-3). Business xác nhận sản phẩm trên phạm vi/build xác định; PM chốt hồ sơ.

Ở mỗi bước, đánh giá Q01–Q07 cho target; dùng mô hình khi có tác động, không bắt mọi Feature có đủ D01–D10. Applicability/unknown/verdict có evidence và reviewer theo [quy trình review](requirements-review-process-and-verdicts.md). Bảng F là cách áp dụng CRM, không phải mẫu bắt buộc của framework khác.

## Nghiệm thu sản phẩm khác đánh giá lợi ích

F02 ghi riêng (a) kết quả cần có để nghiệm thu sản phẩm, (b) lợi ích cần quan sát sau khi sử dụng. Ví dụ giả định: chứng minh workflow CRM đúng là acceptance sản phẩm; giảm thời gian xử lý thực tế cần observation window, dữ liệu so sánh và business owner sau go-live. Không đặt số phần trăm giả và không báo lợi ích đã đạt chỉ vì Feature Accepted.

Nếu hợp đồng/authority quy định lợi ích là điều kiện nghiệm thu thì ghi rõ và tuân theo; không tự tách để đóng sớm. Nếu được đo sau acceptance, ghi kế hoạch theo dõi và kết quả Pending cho tới khi có dữ liệu. Outcome định tính vẫn phải có phương pháp/điều kiện đánh giá, không dùng “cải thiện trải nghiệm” không thể kiểm chứng.

**Evidence:** source/outcome record, scope allocation/trace, shared refs, acceptance method, reviewed revision và decisions. Thiếu đầu vào = Chưa kiểm; gap/conflict = Không đạt cho bước ảnh hưởng; phần không áp dụng có reason/authority. PM không thay chuyên môn, AI không điền quyết định còn thiếu.
