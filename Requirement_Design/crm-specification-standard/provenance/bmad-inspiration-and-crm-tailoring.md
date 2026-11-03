# BMAD Inspiration and CRM Tailoring

ID: **CRM-BMAD-TAILORING** · CRM Workflow Kit 1.4.0 · 03/11/2026


## Principles Borrowed

Học cách BMAD tổ chức điểm vào, agent chuyên môn, workflow theo mục tiêu và durable context qua files. [Skills and Agents](https://docs.bmad-method.org/reference/skills-and-agents/) mô tả các cơ chế gọi công việc. [Break Work into Stories and Track It](https://docs.bmad-method.org/plan/break-work-into-stories-and-track-it/) là nguồn tham khảo cho refinement, decomposition, tracking và replan. Các nguồn đã được đọc trong quá trình thiết kế ngày 03/11/2026; kit không yêu cầu tải chúng khi thực hiện workflow.

## CRM Decisions

Các agent IDs/function names trong bản 1.4 do CRM đặt, không là native BMAD commands. Kit dùng một root skill, profiles logic, workflow Markdown và registry tự chứa. Không copy toàn bộ BMAD, không cài runtime và không phụ thuộc resolver/customization của BMAD. [Customization docs](https://docs.bmad-method.org/customize/customize-bmad/) là tham khảo cho khả năng adapter tương lai, chưa là thành phần được triển khai.

F/E/S/T/Q/D, Feature-doc-only trên Epic, Task tùy chọn, baseline yêu cầu+solution+manifest, PM chốt output và các status Jira giữ theo bộ chuẩn hiện có. Kit không sử dụng ticket tree/build status của BMAD làm nguồn tiến độ thứ hai. Quy tắc authority của người thật không đổi khi agent đổi profile.

## Artifact Preservation

Các catalog/check/model/policy và ID/anchors hiện hành được tái sử dụng. Root SKILL được thay thành router; thêm links từ các reference điều phối cần thiết. Snapshot 1.1, source hashes, migration targets và report lịch sử được giữ. Nội dung còn mang version 1.3.x là revision nội dung chuẩn được giữ trong package 1.4.0; version package hiện hành đọc tại manifest/root.

Adapter sau này có thể đưa cùng contracts vào platform khác, nhưng phải giữ nghĩa check/review/prepare, context theo target/revision, source of truth và quyền được giao. Việc triển khai adapter cần nhiệm vụ riêng; repo package không tự cài native skills hoặc external hooks.
