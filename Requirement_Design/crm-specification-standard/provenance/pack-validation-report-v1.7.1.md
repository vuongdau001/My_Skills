# Conversational Status Validation Report 1.7.1

Version: 1.7.1 · Date: 04/11/2026

## Scope

Thêm guidance cho Recap / Current status / Next step trong crm-report-status, giữ Full report khi cần tổng hợp. Không thêm function/slash command. Routing từ SKILL/CRM Guide/START-HERE; protocol và templates phân biệt chat với checkpoint được giao. Mở supported targets của report-status tới Story/Task để không ép roll-up Project/Epic. Registry next functions phản ánh lựa chọn theo blocker, không quy định thứ tự chạy.

Config/layout/schema/helper implementation và các adapter không đổi từ 1.7.0. Bump version 1.7.1; fixture update candidate dùng 1.7.2 để tiếp tục kiểm package update. Không thay status/state/ticket hoặc tự migrate/update repo CRM.

## Verification

- 110/110 regression tests đạt; không thêm tests chỉ khớp wording của guidance. Update fixture dùng version mới, các expected outcomes về quyền/gate giữ nguyên.
- Structural validator đạt: 96 Markdown documents, 147 manifest entries, 105 source sections, 5 profiles và 13 functions. Skill-creator quick validation và git diff --check đạt.
- Helper context được probe cho cả Project/Feature/Epic/Story/Task: nhận đúng crm-report-status, Delivery Coordinator và reference hội thoại; missing_context=[] cho các arguments được cung cấp. Đây là routing probe, không xác minh artifact của ID minh họa tồn tại hoặc thực thi workflow/model.
- Hash audit xác nhận 1.457 file hiện có trong repo CRM giữ nguyên, không thêm file. Bản cài 1.5.0 và các hồ sơ pilot không tự nâng cấp hoặc đổi instruction.
- Delta so với standard 1.7.0 của đầu lượt này: 11 file sửa, 2 file thêm. Helper implementation, config/layout/schema, catalogs/models/checks và 12 workflow khác giữ nguyên. Guide profile và report-status workflow chỉ bổ sung routing/độ sâu, không thêm người ký hoặc thay quyền.

## Author walkthrough — không phải runtime evaluation

Tác giả đối chiếu các tình huống sau với rule mới. Đây là self-check trên hướng dẫn, không gọi agent độc lập hoặc ghi observed runtime PASS:

| Tình huống | Hành vi hướng dẫn yêu cầu |
|---|---|
| Hỏi vừa làm gì, observed result đã có | Recap ngắn + output/check evidence; không full report, không biến planned action thành done |
| Hỏi Story hiện tới đâu, record cũ khác revision | Đọc current artifact/evidence, nêu discrepancy; không dùng old readiness cho revision mới |
| Epic thiếu quyết định BA hoặc contract | Đề xuất clarify/specify hoặc design theo blocker thực tế; không lấy next function từ menu order |
| Nguồn trạng thái do project chỉ định là state | Đọc đúng source/snapshot; không bắt Jira hoặc tự mutate state khi chỉ hỏi status |
| Hỏi tiến độ giữa nhiệm vụ đã được giao | Trả lời ngắn rồi tiếp tục phần được phép; không tạo permission loop hoặc bỏ nhiệm vụ |
| Status read-only hoặc target đang pin/baseline | Trả chat, không thêm report/checkpoint vào target; lưu handoff riêng khi được giao |
| Không có mẫu số hoặc source access | Báo scope/Unknown đúng phần, không tự đưa % hoàn thành |
| Resume từ checkpoint cũ | Đọc refs và so revision hiện hành rồi tính lại next step; không dùng checkpoint như competing state |

Giới hạn: guidance không tự chạy snapshot queries hoặc ghi checkpoint bằng hook. Runtime/agent adherence, semantic approval và trạng thái sản phẩm chưa được chứng minh bởi structural/tests/context probes. Không commit/push, Jira/CI mutation hoặc tự cập nhật package trong CRM. Người dùng cần update package riêng để nhận hướng dẫn mới ở bản cài.

Hướng dẫn: [status/next step](../references/conversational-status-and-next-step.md), [workflow](../workflows/crm-report-status.md), [handoff template](../assets/templates/work-context-and-handoff-template.md).
