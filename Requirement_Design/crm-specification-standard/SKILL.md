---
name: crm-specification-standard
description: "Vận hành yêu cầu và backlog CRM theo workflow: làm rõ Feature/Epic/Story và solution, review đặc tả, chuẩn bị baseline, kiểm readiness/handoff/completion, đánh giá thay đổi và báo cáo tiến độ. Dùng để soạn hồ sơ hoặc kiểm điều kiện bàn giao theo chuẩn CRM; không tự triển khai product code hoặc thao tác Jira/Git/CI."
---

# CRM Workflow Kit

Phiên bản **1.4.0**. Một root skill, các agent profiles logic và workflows tự chứa. Người mới đọc [Start Here](START-HERE.md). Đây là repo package; function IDs bên dưới không tự là CLI/slash commands đã cài.

## Route the Request

1. Đọc [CRM Guide](agents/profiles/crm-guide.md) và [Workflow Execution Protocol](references/workflow-execution-protocol.md). Xác định mục tiêu, target, selected scope, revision/baseline và phạm vi quyền được giao.
2. Chọn function theo ý định hoặc ID người dùng nêu. Nếu target/input không phù hợp thì giải thích và chọn lại; nếu nhiều target hợp lý thì hỏi trước chỉnh sửa. Không dùng active target ngầm toàn cục.
3. Thông báo function/profile và output dự kiến; đọc workflow + profile tương ứng, rồi chỉ refs/templates cần cho target. Không tải toàn bộ gói.
4. Thực hiện workflow; kết thúc với artifact refs, findings/evidence, verdict scoped, approvals còn thiếu và receiver/next function. Resume phải đọc lại current revision, không chỉ dựa chat history.

## Functions

| Function | Purpose | Agent |
|---|---|---|
| [crm-setup-project](workflows/crm-setup-project.md) | Set Up Project | Delivery Coordinator |
| [crm-define-feature](workflows/crm-define-feature.md) | Define Feature | Requirements Analyst |
| [crm-specify-epic](workflows/crm-specify-epic.md) | Specify Epic | Requirements Analyst |
| [crm-design-solution](workflows/crm-design-solution.md) | Design Solution | Solution Architect |
| [crm-prepare-stories](workflows/crm-prepare-stories.md) | Prepare Stories | Requirements Analyst |
| [crm-review-specification](workflows/crm-review-specification.md) | Review Specification | Quality Reviewer |
| [crm-prepare-baseline](workflows/crm-prepare-baseline.md) | Prepare Baseline | Delivery Coordinator |
| [crm-check-readiness](workflows/crm-check-readiness.md) | Check Readiness | Quality Reviewer |
| [crm-check-handoff](workflows/crm-check-handoff.md) | Check Handoff | Quality Reviewer |
| [crm-check-completion](workflows/crm-check-completion.md) | Check Completion | Quality Reviewer |
| [crm-assess-change](workflows/crm-assess-change.md) | Assess Change | Delivery Coordinator |
| [crm-report-status](workflows/crm-report-status.md) | Report Status | Delivery Coordinator |
| [crm-run-pilot](workflows/crm-run-pilot.md) | Run Pilot | Delivery Coordinator |

## Operating Rules

- Standards hiện hành nằm tại [quy ước CRM](references/crm-project-rules.md), catalogs/checks/models và [policy guide](references/project-policy-register.md). Workflow điều phối cách dùng, không ghi đè tiêu chí nguồn.
- Không invent policy/expected behavior/approval. Policy bắt buộc Pending thì gate liên quan chưa đủ điều kiện; tiếp tục phần độc lập và nêu missing decision.
- Story đủ DoR có thể dùng checklist, Task tùy nhu cầu. Chuẩn bị plan/brief Task qua crm-prepare-stories; crm-check-readiness chỉ kiểm và đề xuất.
- Review/check chỉ ghi record/findings, không tự sửa source target. Full specification review xét catalog + Q01–Q07; focused review không kết luận toàn target. Task theo T01–T08/SMART.
- Chuyển profile trong cùng phiên là self-check, không tự independent review. Human approval, QA runtime verdict, PM closure và Business acceptance cần evidence đúng authority.
- Tách output prepared, review performed, authority approved và actual action confirmed. Package draft chưa là baseline merged; Task Done không tự Story Done.
- Giữ source/IDs/pinned versions; thay đổi sau baseline qua crm-assess-change trước khi áp dụng correction. Ví dụ trong gói là giả định, không phải policy đã duyệt.
- Không tự spawn multi-agent, triển khai product code/test runtime hoặc thực hiện Jira/Git/CI mutations. Ghi actions chưa làm và giới hạn access. Hard gates thực tế cần cơ chế chặn tại hệ thống tương ứng.

## Registry & Verification

[Manifest](reference-manifest.json) nối function → profile → workflow → refs/templates. [Nguồn và tailoring](references/standards-and-crm-tailoring.md), [BMAD inspiration](provenance/bmad-inspiration-and-crm-tailoring.md), [acceptance scenarios](references/pack-acceptance-scenarios.md) và [report 1.4](provenance/pack-validation-report-v1.4.md) phục vụ đối chiếu.

Chạy `python3 scripts/validate_reference_pack.py` từ folder này hoặc gọi bằng đường dẫn script. Validator kiểm cấu trúc/refs/registry/migration, không cấp DoR/DoD approval hoặc chứng minh phần mềm đạt.
