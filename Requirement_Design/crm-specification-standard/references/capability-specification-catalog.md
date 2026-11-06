# Danh mục nội dung và tiêu chí Capability

Mã tài liệu: **CRM-CAPABILITY** · Gói CRM 1.3.1 · 03/11/2026

**Đọc khi:** tiếp nhận năng lực/phạm vi, phân rã thành Epic, nghiệm thu liên Epic. **Đầu vào:** nhu cầu và source có authority, constraints, các Epic hiện có. **Đầu ra:** Capability brief, scope allocation, phương pháp acceptance và quyết định; dùng [mẫu Capability](../assets/templates/capability-specification-template.md).

Capability chỉ ở Git. Không tạo issue type hay status mới. Không bắt một Capability có nhiều Epic, không viết lại state machine/data/API đã thuộc Epic/shared models; dẫn đúng revision.

| ID/tên | Nội dung cần có | Phép kiểm và điều kiện đủ | Người chuẩn bị/xác nhận |
|---|---|---|---|
| <a id="c01"></a>C01 — Nguồn và vấn đề | Capability ID, source, vấn đề/cơ hội, rationale, sponsor/authority | Đi ngược tới nguồn; giải thích ai gặp vấn đề và vì sao cần scope; không dùng ý kiến AI làm nguồn đã duyệt | BA / Business |
| <a id="c02"></a>C02 — Outcome và cách đánh giá | Kết quả mong muốn, population, phương pháp xác nhận; KPI nếu áp dụng | Reviewer nêu được điều kiện đạt/không đạt; KPI có unit/baseline hoặc kế hoạch đo/target/window/owner; missing target ảnh hưởng gate phải ghi Pending | Business + BA / đúng authority |
| <a id="c03"></a>C03 — Bên liên quan nghiệp vụ | Nhóm sử dụng, hưởng lợi, vận hành hoặc chịu tác động, nhu cầu và quyền lợi | Đối chiếu outcome, tác động và actor liên quan. Dẫn E02 cho actor, C08 cho thẩm quyền xác nhận và Work Context cho trách nhiệm SDLC | BA / Business và leads |
| <a id="c04"></a>C04 — Phạm vi và ranh giới | In/out scope, assumptions/constraints, phạm vi giao từng giai đoạn | Mỗi item được giữ/loại/trì hoãn có quyết định; không loại dependency cần thiết khỏi scope để làm giả readiness | BA + PM / Business |
| <a id="c05"></a>C05 — Requirement/control dùng chung | IDs/versions của rule, NFR, data/permission/integration/transition chung | Tìm Epic/Story áp dụng; không có hai policy trái nhau hoặc control bắt buộc chưa được phân bổ; model chi tiết tham chiếu | BA + TL/QA / authority nội dung |
| <a id="c06"></a>C06 — Phân bổ Epic và dependency | Fragment nguồn → một Epic–Use Case nhận mục tiêu, dependency, owner/capacity/mốc sơ bộ | Đi qua từng scope item: có Epic nhận hoặc gap; tìm trùng/giao thoa và cam kết dependency; không đòi estimate chi tiết mọi Story từ đầu | BA + Dev/QA / PM |
| <a id="c07"></a>C07 — Acceptance liên Epic | Điều kiện nghiệm thu sản phẩm, hành trình liên Epic, data/control chung, phương pháp kiểm | Có expected result/observation cho mỗi AC; luồng giao thoa được phân bổ kiểm; Epic Done không tự thay acceptance Capability | BA + QA / Business, TL phần kỹ thuật |
| <a id="c08"></a>C08 — Quyết định, baseline và nghiệm thu | Revision/scope, quyết định và xác nhận nghiệp vụ, policy SDLC và evidence review/baseline/bàn giao | Không có câu hỏi chặn bị giấu; decision đúng authority/revision; khi bàn giao đủ scope/evidence và Business acceptance | BA điều phối / PM + Business |

Áp dụng [quy ước vai trò](artifact-writing-standard.md#business-and-sdlc-roles) khi lập C03 và C08.

Với C04/C06, dùng [checkpoint nguồn scope](source-scope-and-decomposition-checkpoint.md) khi tiếp nhận inventory hoặc thay allocation. Rationale cần dựa outcome/model/control/acceptance; mapping một owner chính trên mỗi dòng nguồn chưa chứng minh mọi fragment đã được bao phủ.

Khi tạo/đổi C04/C06, áp dụng [checkpoint chọn cấp và quan hệ cha–con](source-scope-and-decomposition-checkpoint.md#level-selection). Đối chiếu năng lực với Capability hiện có; kiểm cha–con lặp nghĩa và giải thích quan hệ một–một nếu có. Rationale thiếu là phần cần làm rõ; cây có outcome trùng nhưng không có vai trò riêng là finding phân rã.

## Cách review theo bước, không đòi đầy đủ quá sớm

1. **Cho phép làm rõ/phân rã:** C01–C04 có khung đủ giao việc, C06 có kế hoạch/owner, C08 ghi authority/questions. C05/C07 còn discovery được ghi rõ. Áp dụng DoR Capability hiện có; không tuyên bố đã đủ để code.
2. **Chốt phạm vi cho Epic:** scope chọn của C01–C08 được làm rõ tương ứng; các shared requirement ảnh hưởng phải có nguồn/quyết định; C06 không có gap allocation bị che. Epic tiếp tục làm chi tiết E01–E16 và baseline trước Story.
3. **Hoàn tất phân tích toàn Capability:** mọi phạm vi hiện hành đều có baseline yêu cầu/solution tương ứng, allocation và acceptance đủ; phần chưa rõ không được lờ đi. Chốt một phần không bằng hoàn tất toàn bộ.
4. **Nghiệm thu Capability:** kiểm C07/C08 và toàn scope theo [gate Capability](readiness-completion-and-approval-gates.md#workflow-7-3). Business xác nhận sản phẩm trên phạm vi/build xác định; PM chốt hồ sơ.

Ở mỗi bước, đánh giá Q01–Q07 cho target; dùng mô hình khi có tác động, không bắt mọi Capability có đủ D01–D10. Applicability/unknown/verdict có evidence và reviewer theo [quy trình review](requirements-review-process-and-verdicts.md). Catalog C là cách áp dụng CRM, không phải mẫu bắt buộc của framework khác.

## Nghiệm thu sản phẩm khác đánh giá lợi ích

C02 ghi riêng (a) kết quả cần có để nghiệm thu sản phẩm, (b) lợi ích cần quan sát sau khi sử dụng. Ví dụ giả định: chứng minh workflow CRM đúng là acceptance sản phẩm; giảm thời gian xử lý thực tế cần observation window, dữ liệu so sánh và business owner sau go-live. Không đặt số phần trăm giả và không báo lợi ích đã đạt chỉ vì Capability Accepted.

Nếu hợp đồng/authority quy định lợi ích là điều kiện nghiệm thu thì ghi rõ và tuân theo; không tự tách để đóng sớm. Nếu được đo sau acceptance, ghi kế hoạch theo dõi và kết quả Pending cho tới khi có dữ liệu. Outcome định tính vẫn phải có phương pháp/điều kiện đánh giá, không dùng “cải thiện trải nghiệm” không thể kiểm chứng.

**Evidence:** source/outcome record, scope allocation/trace, shared refs, acceptance method, reviewed revision và decisions. Thiếu đầu vào = Chưa kiểm; gap/conflict = Không đạt cho bước ảnh hưởng; phần không áp dụng có reason/authority. PM không thay chuyên môn, AI không điền quyết định còn thiếu.
