# Kiểm chứng CRM Workflow Kit 1.9.0

ID: CRM-VALIDATION-V19 · 05/11/2026

## Thay đổi

Score policy crm-definition-v2 tái dùng lint readiness graph ASM/DEC/CST, pin closure/state/revision/hash. Unresolved dependency đã map cap điểm mục bị ảnh hưởng ở 1; không map thì effective Unknown và suppress chỉ số. Declared score giữ để giải thích, không sửa assessment/spec. Focus item không miễn gate target. Resolved/Validated không cần biến ASM thành DEC; record thay đổi cần reassess. Policy v1 không được đổi tên mù để giữ điểm.

Bổ sung --output cho Markdown report mới trong configured reports, không overwrite/thoát boundary. Report có bảng tổng hợp targets, declared/effective, rationale/evidence/blockers và next actions. Mặc định score vẫn chỉ stdout. Không thêm workflow/public skill, không đổi record state/authority, không tạo waiver tự vượt gate.

## Kiểm chứng và giới hạn

144 regression tests PASS (46,987 giây) trên disposable repos, bao gồm old scoring arithmetic, dependency missing/mapping, stale records, Pending Decision/Constraint, ASM Validated/Invalidated/Retired, Approved DEC vẫn phụ thuộc Unverified ASM, focused score và output preservation. Structural validation PASS (102 Markdown documents, 153 entries, 13 functions), skill validation PASS và full tests chạy trước rollout; kết quả nằm trong execution logs của lượt triển khai. Hai sample artifacts EPIC-CRM-001/STORY-CRM-001 được self-check lần lượt 37,50/36,11, gate blocked, không cấp mức 3; report mẫu và assessment JSON mới nằm trong workstream reports.

Ví dụ report thật trên pilot p3 được chuẩn bị bằng self-check riêng, pin artifact/evidence hiện hành và giữ câu hỏi unresolved. Không tạo reviewer người thật hoặc cấp mức 3 giả. Legacy question queue không có typed ASM/DEC/CST links phải được reviewer đọc và ghi blocker thủ công; graph không tự tìm mọi assumption trong prose. Identity/authority vẫn chỉ là khai báo, không được tool chứng thực. Chưa có inter-rater calibration hoặc independent review/runtime discovery.
