# Bắt đầu với CRM Workflow Kit 3.0.0

Đọc [SKILL](SKILL.md) để chọn đúng function và [BOOTSTRAP](BOOTSTRAP.md) để cài đặt. Kit giữ hồ sơ hiện hành, không tích lũy snapshot/report/pilot; lịch sử qua Git.

## Chọn việc cần làm

| Function | Purpose |
|---|---|
| [crm-setup-project](workflows/crm-setup-project.md) | Set Up Project |
| [crm-define-capability](workflows/crm-define-capability.md) | Define Capability |
| [crm-specify-epic](workflows/crm-specify-epic.md) | Specify Epic |
| [crm-design-solution](workflows/crm-design-solution.md) | Design Solution |
| [crm-prepare-stories](workflows/crm-prepare-stories.md) | Prepare Stories |
| [crm-review-specification](workflows/crm-review-specification.md) | Review Specification |
| [crm-check-readiness](workflows/crm-check-readiness.md) | Check Readiness |
| [crm-check-handoff](workflows/crm-check-handoff.md) | Check Handoff |
| [crm-check-completion](workflows/crm-check-completion.md) | Check Completion |
| [crm-assess-change](workflows/crm-assess-change.md) | Assess Change |

Status và next step dùng [hướng dẫn chung](references/conversational-status-and-next-step.md); không thêm workflow. [BA guide](references/ba-getting-started.md) giúp phân rã scope. [Commit policy](references/commit-message-policy.md) chỉ áp dụng khi được giao commit.

Nguồn → Capability/Epic → solution/Story → review → readiness/handoff/completion theo evidence. Không bắt merge package để được kiểm readiness, không tự Ready từ số điểm. Tất cả authoring dùng [writing standard](references/artifact-writing-standard.md) và [current-state policy](references/current-state-and-history.md).

Nâng từ 2.x: đọc [migration](references/artifact-layout-and-migration.md); update kit không xóa/migrate hồ sơ dự án hoặc bật hook/CI.
