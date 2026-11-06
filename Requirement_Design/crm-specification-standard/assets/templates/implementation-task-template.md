# Mẫu Task triển khai

Mã tài liệu: **TPL-IMPLEMENTATION-TASK-TEMPLATE** · Gói CRM 1.10.0 · 05/11/2026

Áp dụng [standard viết artifact](../../references/artifact-writing-standard.md). Đây là mẫu; thay hướng dẫn bằng dữ liệu thực, giữ gap khi thiếu input. Không suy approval từ việc điền đủ mục.

Một đoạn nêu output của Task và giá trị với Story/Epic. ID/Jira mapping/revision ghi trong context ngắn; chưa có Jira giữ logical ID.

Chỉ tạo khi có nhu cầu giao output thực tế; đọc [Task planning](../../references/task-planning-and-completion.md).

## T01 — Mục đích, Epic và Story liên kết

Ghi Epic quản lý Task và Story tiêu thụ đầu ra theo quan hệ đã xác nhận trong Jira. Nếu Task dùng chung, liệt kê các Story liên kết. Dẫn BR/AC hoặc đầu ra được giao.

## T02 — Đầu ra và ranh giới

Artifact/kết quả, in/out scope và vì sao cần Task thay vì checklist.

## T03 — Đầu vào và phiên bản

Baseline/repo/commit/path/model/contract cùng environment/quyền thực có.

## T04 — Kế hoạch và constraint

Các bước chính, giới hạn và phạm vi AI được phép hỗ trợ.

## T05 — Dependency và bàn giao

Input cần trước khi bắt đầu, người cung cấp và người nhận output.

## T06 — Người thực hiện và timebox

Owner/reviewer, estimate/capacity, mốc báo khi vượt dự kiến.

## T07 — Tiêu chí hoàn tất

Điều kiện → phép kiểm → expected result theo output.

## T08 — Evidence và closure

PR/SHA/build/run/log áp dụng; reviewer/receiver, revision và thời điểm thực.

## Kiểm bắt đầu/hoàn tất và handoff

Với từng tiêu chí, ghi thao tác kiểm, expected/observed, evidence/ref/revision, verdict/reviewer và gap/owner/due. Bảng chỉ làm index nếu nội dung dài.

Ghi phiên bản output, tiêu chí đã/chưa đạt, receiver acceptance, việc còn lại và impact tới Story/baseline. Task Done không tự Story Done. Kết thúc bằng metadata Task hợp lệ.
