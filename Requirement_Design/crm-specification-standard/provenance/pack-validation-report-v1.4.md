# Workflow Kit Validation Report 1.4

Version: **1.4.0** · Date: **03/11/2026**

## Delivered Scope

Một root skill được rút thành router, Start Here cho member, 5 English agent profiles, 13 verb-object workflow contracts, shared execution protocol, context/handoff template và function registry. Các profile là góc nhìn logic, không có BMAD runtime/installer hay multi-agent execution. Chỉ sửa trong crm-specification-standard.

## Automated Checks — Executed

- `validate_reference_pack.py`: đạt, 76 Markdown documents, 123 manifest entries, 105 source sections, 5 agent profiles, 13 workflow functions.
- `quick_validate.py` của skill-creator: đạt frontmatter/name/entrypoint. Đây là công cụ authoring bên ngoài dùng để kiểm; kit runtime không phụ thuộc nó.
- `scripts/tests/test_workflow_registry.py`: 13 tests đạt. Có portable-copy test và negative cases: duplicate/missing/old function, unknown agent/next function, missing profile/workflow, unrouted function, wrong check write boundary, cross-folder dependency, lost historical anchor, unregistered workflow và missing E/S mapping.
- `git diff --check`: đạt; tracked changes đều trong folder kit.
- Mỗi workflow có chín contract sections và dùng function ID mới; menu/registry/refs/next functions resolve.

## Preservation — Executed

- Giữ đủ 55 files trước cập nhật; 7 files thay đổi có chủ đích: `SKILL.md`, `reference-manifest.json`, `references/crm-project-rules.md`, `references/pack-acceptance-scenarios.md`, `references/pilot-and-operational-validation.md`, `references/readiness-completion-and-approval-gates.md`, `scripts/validate_reference_pack.py`.
- Hash của các catalog, model, check, templates cũ và provenance lịch sử được giữ; nội dung chuẩn không bị viết lại. Các reference điều phối chỉ thêm links sang workflows; acceptance scenarios thêm tuyến kiểm mới.
- Toàn bộ original manifest entries, sources và migration records được đối chiếu với version trước và giữ nguyên. Snapshot ZIP/source hashes/105 migration targets vẫn hợp lệ.
- Tài liệu chuẩn giữ content revision 1.3.x; version kit hiện hành 1.4.0 nằm ở manifest/root. Không coi header cũ là một gói runtime khác.

## Workflow Walkthrough — Desk Review

[WK01–WK15](../references/examples/workflow-routing-and-handoff-walkthrough.md) ghi input fixtures, selected function/profile, observed desk decision và rule evidence. Đã đối chiếu các trường hợp: vague Feature, solution request, focused permission contradiction, approval chưa merge, Story không Task, đổi target, stale approval, changed rule, missing QA evidence, self-check, Jira/evidence discrepancy, check không repair, resume khác revision, portable copy và pilot thiếu participants.

Kết quả: các hướng dẫn cho quyết định nhất quán với các gate/authority hiện hành. Với check workflows, output là record/findings và missing conditions; không tự sửa target hay đóng ticket. Story không Task không bị coi là thiếu riêng vì không có Task; mọi điều kiện DoR khác vẫn cần evidence.

Đây là walkthrough của tác giả trên tài liệu/fixture, không phải model evaluation độc lập hoặc đo độ chính xác router. Không ghi nhận human approval hay independent review từ việc đổi profile trong cùng phiên.

## Limits & Remaining Operational Validation

Chưa pilot với Epic/Story/participants thật, chưa truy cập hay cấu hình Jira/Git/CI, chưa chạy test sản phẩm, chưa cài skill vào runtime và chưa tích hợp BMAD. Native slash commands và external mutations không được cung cấp bởi bản này. Validator chỉ kiểm cấu trúc/registry/refs/migration, không kết luận requirement semantics hoặc DoR/DoD dự án.

Khi có pilot thật, dùng [Run Pilot](../workflows/crm-run-pilot.md) và ghi observed evidence theo [protocol](../references/workflow-execution-protocol.md). Nguồn tư tưởng và CRM decisions nằm tại [BMAD Inspiration and CRM Tailoring](bmad-inspiration-and-crm-tailoring.md).
