---
name: crm-specification-standard
description: "Soạn và review đặc tả CRM Capability/Epic/Story, solution, readiness, handoff, completion và change impact; giữ hồ sơ hiện hành, lịch sử qua Git. Không tự triển khai product code hoặc thao tác Git/Jira/CI."
---

# CRM Workflow Kit

Phiên bản **3.0.0**. Một public skill, 10 function nội bộ; không giả lập slash commands.

## Installation and Admin Requests

Cài/nâng cấp đọc [BOOTSTRAP](BOOTSTRAP.md) và [INSTALL](INSTALL.md). Python 3.11+ stdlib helper lấy package root từ script. Dry-run trước apply, giữ config/instructions/spec hiện hữu. Bản cài không sửa trực tiếp; sửa nguồn riêng rồi update. Package doctor không là runtime discovery proof.

## Hồ sơ hiện hành

Đọc [current-state policy](references/current-state-and-history.md): giữ một bản canonical/ID/path theo đối tượng, cập nhật revision; lịch sử qua Git khi được giao commit. Không tạo history/archive/report theo lần chạy. Status/next step trả chat, scoring xuất stdout. Không có Prepare Baseline, Report Status hoặc Run Pilot.

## Route the Request

1. Đọc config .agents/crm-spec-kit.json, chọn workstream/target/revision; đọc AGENTS.md tại spec_root. Chạy kit.py context <function-id> --repo <repo> --workstream <id>. Context bundle gồm workflow/profile/protocol và writing standard; detailed refs đọc theo nhu cầu. Không tự chọn active target toàn cục.
2. Capability dùng CAP-CRM IDs, C01–C08. Epic sở hữu một user-goal Use Case E03 theo [use-case policy](references/epic-use-case-policy.md), E01–E16. Story S01–S12; Task tùy nhu cầu. Một Epic không mặc định là một Bounded Context.
3. Function list/WBS/estimation cần [scope checkpoint](references/source-scope-and-decomposition-checkpoint.md). Giữ ID nguồn, giải thích allocation/parent; không ép một dòng nguồn thành Epic.
4. Author dùng [writing standard](references/artifact-writing-standard.md), [visual review](references/review-visualization-standard.md) khi phù hợp và [metadata](assets/templates/artifact-metadata-template.md). Trả lời tiếng Việt rõ, giữ thuật ngữ tech/DDD và ID. Links có nhãn có nghĩa, heading Unicode NFC; không tạo bản đọc phụ mặc định.
5. DEC/ASM/CST mới theo [knowledge records](references/knowledge-records-and-evidence.md), schema 3 không state; meeting notes chỉ là input. ASM được xác nhận thì chuyển DEC, cập nhật consumer rồi xóa ASM khi được giao. Source không tự là approval.
6. Có UI thì dùng [Prototype](references/prototype-workflow-and-epic-gate.md), đối chiếu spec hai chiều và walkthrough trong scope. Không lấy mockup làm signed contract.
7. Sau author chạy lint. Gate readiness kiểm cấu trúc/evidence closure, không thay authority/semantic/runtime verdict. Review/check chỉ sửa kết quả của mình, không sửa target. Sửa target bằng workflow tác giả riêng.
8. Thay đổi nội dung đã dùng cần crm-assess-change, kiểm consumer/revision/evidence. Chuyển profile vẫn là self-check; không giả independent review, approval, QA hoặc Business acceptance.

## Functions

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

## Status, scoring và reset

Câu hỏi recap/current status/next step dùng [hướng dẫn chung](references/conversational-status-and-next-step.md); không là function riêng, không tự tạo file. [Scoring](references/definition-maturity-scoring.md) đọc assessment hiện hành và tính lại, không cấp Ready. [Reset](references/clean-project-reset.md) chỉ khi user giao bỏ outputs, dry-run và plan digest trước apply; không chạy reset do update kit.

## Commit policy và ranh giới

Khi đã được giao commit, đọc [commit policy](references/commit-message-policy.md), kiểm staged diff, validate message bằng commit_policy.py trước commit và đọc lại message thực tế. Không bypass hook hoặc khai validation chưa chạy. Root router và các adapter phải dẫn cùng policy; hướng dẫn trong skill không tự enforce mọi agent. Hook/CI chỉ khi được giao cấu hình, không ghi đè rule hiện hữu.

Không tự spawn agents, triển khai product code/test runtime, commit/push/merge hoặc thao tác Jira/CI. User authorization rõ được xử lý theo scope riêng; hoàn tất workflow không là quyền làm external action. Phân biệt output prepared, review performed, authority approved và actual action confirmed.

## Registry & Verification

[Manifest](reference-manifest.json) liên kết function → profile → workflow → refs/templates. Chạy scripts/validate_reference_pack.py và regression tests; đó là kiểm chất lượng kit, không là nghiệp vụ pilot dự án hoặc DoR/DoD approval. [Migration](references/artifact-layout-and-migration.md) giữ workstream cũ nguyên khi update; chỉ đổi hồ sơ dự án trong bước migration được giao. [Nguồn](provenance/source-to-reference-migration-map.md) giữ truy vết standard ban đầu; policy 3.0.0 hiện hành được ưu tiên so ví dụ lịch sử.
