# Workflow Routing and Handoff Walkthrough

ID: **EX-WORKFLOW-WALKTHROUGH** · CRM Workflow Kit 1.4.0 · 03/11/2026

## Method & Limits

Đây là walkthrough bàn giấy do tác giả kit thực hiện, dùng input giả định và đối chiếu quy tắc trong workflow/protocol. Không chạy một model/router độc lập, không có human authority dự án, không truy cập Jira/Git/CI và không chạy test sản phẩm. Bảng ghi quyết định rút ra khi áp dụng hướng dẫn; không phải benchmark agent tự động hoặc pilot thật.

Với mỗi input: chọn function từ mục tiêu, đọc Input Check/Execution/Exit/Failure, ghi quyết định và output phải có. Nhận diện các phần thiếu evidence thay vì tự điền. Kết quả khớp được ghi trong report 1.4; các case là fixture, không policy/approval thật.

## Scenario Records

<a id="wk01"></a>

### WK01 — Vague Feature Intake

- **Input fixture:** BA có mô tả “cần tiếp nhận khách hàng”; chưa có Business authority hoặc target Feature rõ.
- **Selected function/profile:** crm-define-feature.
- **Observed decision in desk walkthrough:** CRM Guide xác định nhu cầu ở mức Feature, không chọn check-readiness hay tự tạo Story. Output draft giữ source/authority là gap; chưa tự đặt rule.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-define-feature.md](../../workflows/crm-define-feature.md), [START-HERE.md](../../START-HERE.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk02"></a>

### WK02 — Solution Request

- **Input fixture:** User nêu target EPIC-CRM-901 và yêu cầu so sánh solution với contract/code được cho phép đọc.
- **Selected function/profile:** crm-design-solution.
- **Observed decision in desk walkthrough:** Chọn Solution Architect, đọc requirement/current revisions, tạo delta/feasibility; không tự sửa product code.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-design-solution.md](../../workflows/crm-design-solution.md), [crm-solution-architect.md](../../agents/profiles/crm-solution-architect.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk03"></a>

### WK03 — Focused Permission Review

- **Input fixture:** User chỉ yêu cầu kiểm quyền; flow nói creator approve được, permission matrix cùng điều kiện nói deny.
- **Selected function/profile:** crm-review-specification.
- **Observed decision in desk walkthrough:** Focused review có Q03 counterexample; Không đạt cho phần mâu thuẫn, không kết luận toàn Story. Record self-check nếu cùng tác giả.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-review-specification.md](../../workflows/crm-review-specification.md), [cross-model-consistency.md](../../references/checks/cross-model-consistency.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk04"></a>

### WK04 — Approved but Not Merged

- **Input fixture:** Package scope/reviews/PM decision có refs tại draft r7; chưa có merge receipt/commit đã xác nhận.
- **Selected function/profile:** crm-prepare-baseline.
- **Observed decision in desk walkthrough:** Package được chuẩn bị và approval được ghi riêng; thiếu confirmed merge, chưa tạo baseline receipt hợp lệ hoặc cho phép Jira Story thực thi.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-prepare-baseline.md](../../workflows/crm-prepare-baseline.md), [baseline-and-change-control.md](../../references/baseline-and-change-control.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk05"></a>

### WK05 — Story Without Task

- **Input fixture:** Story có checklist thực hiện và inputs DoR được cung cấp; không có Task tickets.
- **Selected function/profile:** crm-check-readiness.
- **Observed decision in desk walkthrough:** Không coi thiếu Task là blocker; kiểm các điều kiện còn lại và evidence trước verdict. Đây không tự chứng minh mọi DoR thật đã đạt.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-check-readiness.md](../../workflows/crm-check-readiness.md), [task-planning-and-completion.md](../../references/task-planning-and-completion.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk06"></a>

### WK06 — Switch Target Mid-session

- **Input fixture:** Record trước EPIC-CRM-901/r7; request mới có hai Epic khả dĩ và chưa chỉ rõ sửa cái nào.
- **Selected function/profile:** CRM Guide.
- **Observed decision in desk walkthrough:** Hỏi target trước chỉnh sửa, không ghi vào Epic cũ; sau xác nhận tạo context riêng và đọc revision mới.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [workflow-execution-protocol.md](../../references/workflow-execution-protocol.md), [crm-guide.md](../../agents/profiles/crm-guide.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk07"></a>

### WK07 — Stale Approval

- **Input fixture:** Target draft r8 đã thay quyền; approval chỉ cho r7.
- **Selected function/profile:** crm-prepare-baseline.
- **Observed decision in desk walkthrough:** Giữ approval r7 như lịch sử, không tính cho r8; xác định scope phải impact/review lại.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-prepare-baseline.md](../../workflows/crm-prepare-baseline.md), [workflow-execution-protocol.md](../../references/workflow-execution-protocol.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk08"></a>

### WK08 — Changed Rule After Baseline

- **Input fixture:** BR trong BASE-CRM-901 được đề nghị đổi; có links tới model, Story và test.
- **Selected function/profile:** crm-assess-change.
- **Observed decision in desk walkthrough:** Tạo affected-artifact/evidence list và correction/revalidation plan; không tự áp dụng vào canonical baseline hoặc pin mọi Story sang latest.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-assess-change.md](../../workflows/crm-assess-change.md), [baseline-and-change-control.md](../../references/baseline-and-change-control.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk09"></a>

### WK09 — CI Pass, QA Missing

- **Input fixture:** Story có CI Pass đúng SHA, chưa có QA run/verdict và PM closure.
- **Selected function/profile:** crm-check-completion.
- **Observed decision in desk walkthrough:** Ghi CI evidence đã có nhưng QA/closure Chưa kiểm; chưa đủ điều kiện đóng Story; không tự chạy test lấp evidence.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-check-completion.md](../../workflows/crm-check-completion.md), [readiness-completion-and-approval-gates.md](../../references/readiness-completion-and-approval-gates.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk10"></a>

### WK10 — Same Author, New Profile

- **Input fixture:** Cùng phiên tác giả tự chuyển Requirements Analyst sang Quality Reviewer để rà draft.
- **Selected function/profile:** crm-review-specification.
- **Observed decision in desk walkthrough:** Ghi self-check; không thêm tên reviewer độc lập hoặc human approval giả.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [workflow-execution-protocol.md](../../references/workflow-execution-protocol.md), [crm-review-specification.md](../../workflows/crm-review-specification.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk11"></a>

### WK11 — Done Status, Missing Evidence

- **Input fixture:** Jira snapshot ghi Done nhưng evidence QA/acceptance không được cung cấp.
- **Selected function/profile:** crm-report-status.
- **Observed decision in desk walkthrough:** Báo discrepancy và dữ liệu chưa xác minh, không tự sửa Jira hoặc suy evidence từ status. Có thể đề xuất check-completion.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-report-status.md](../../workflows/crm-report-status.md), [progress-measurement-and-feature-rollup.md](../../references/progress-measurement-and-feature-rollup.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk12"></a>

### WK12 — Check Handoff Is Not Repair

- **Input fixture:** Target Story bàn giao có review/CI refs nhưng chưa có deploy/smoke evidence. User chỉ giao check.
- **Selected function/profile:** crm-check-handoff.
- **Observed decision in desk walkthrough:** Tạo check record và gap; không sửa code/spec/plan, không chuyển resolved.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-check-handoff.md](../../workflows/crm-check-handoff.md), [workflow-execution-protocol.md](../../references/workflow-execution-protocol.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk13"></a>

### WK13 — Resume from Handoff

- **Input fixture:** Người nhận có target/scope/r7, artifact refs và next action; current source là r8.
- **Selected function/profile:** CRM Guide.
- **Observed decision in desk walkthrough:** Đọc current refs, báo mismatch trước tiếp tục; không cần toàn bộ chat và không tự tái dùng r7 verdict.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [work-context-and-handoff-template.md](../../assets/templates/work-context-and-handoff-template.md), [workflow-execution-protocol.md](../../references/workflow-execution-protocol.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk14"></a>

### WK14 — Portable Copy

- **Input fixture:** Copy riêng kit sang thư mục khác; không cài BMAD hoặc runtime skills.
- **Selected function/profile:** Root skill.
- **Observed decision in desk walkthrough:** Markdown links/registry/validator vẫn resolve trong copy. Cơ chế gọi native command chưa được xác nhận; cần yêu cầu agent đọc root SKILL.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [START-HERE.md](../../START-HERE.md), [test_workflow_registry.py](../../scripts/tests/test_workflow_registry.py).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

<a id="wk15"></a>

### WK15 — Missing Pilot Participants

- **Input fixture:** Có procedure nhưng chưa có Epic thật/participants/authority hoặc quyền.
- **Selected function/profile:** crm-run-pilot.
- **Observed decision in desk walkthrough:** Chỉ chuẩn bị kế hoạch và missing input; không ghi pilot thành công hay test hook đã chạy.
- **Artifacts:** record trong scenario này; không sửa target hoặc thực hiện external action.
- **Rule evidence:** [crm-run-pilot.md](../../workflows/crm-run-pilot.md), [pilot-and-operational-validation.md](../../references/pilot-and-operational-validation.md).
- **Handoff:** người nhận đọc target/scope/current revision và thực hiện next action theo protocol; không tự cấp approval.

## Concrete Handoff Record — Missing QA Evidence

Function: crm-check-completion; profile: Quality Reviewer; target: STORY-CRM-901, scope submit; input revision: fixture r7, baseline BASE-CRM-901. Đây chỉ là fixture, không có commit/approval thật.

| Điều kiện | Evidence trong fixture | Kết quả bàn giấy | Receiver/action |
|---|---|---|---|
| CI đúng SHA | Fixture nêu có CI Pass; không truy cập run thật | Có input khai báo, chưa xác minh external run | Dev cung cấp run/build refs để đối soát |
| QA AC/test matrix | Không có report/run/verdict | Chưa kiểm, không tự coi Pass | QA cung cấp kết quả đúng baseline/build |
| PM closure | Không có decision | Chưa kiểm | PM chốt khi đủ điều kiện |

Output prepared: check record này. Review performed: desk self-check của tác giả kit. Authority approval: chưa có. Actual closure/action confirmed: chưa có. Next action: bổ sung evidence và chạy lại crm-check-completion; receiver QA/PM theo gate. Không sửa target, không chuyển status, không bịa runtime test.

Liên quan: [Work Context and Handoff](../../assets/templates/work-context-and-handoff-template.md), [Protocol](../workflow-execution-protocol.md).
