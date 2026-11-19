# Revision và tác động thay đổi

ID: CRM-REVISION-IMPACT · CRM Workflow Kit 3.0.0

<a id="workflow-4"></a>

## Revision áp dụng

Consumer tham chiếu target ID, scope, path/locator và revision cụ thể. Working tree là nội dung chưa commit; không tự gọi đó là nội dung đã merge hoặc đã được duyệt.

<a id="workflow-4-1"></a>

## Nguồn hiện hành

Requirement, solution, Story allocation và Prototype có một bản canonical. Dùng commit reference khi cần truy xuất nội dung cũ; không tạo package snapshot song song.

<a id="workflow-4-2"></a>

## Phạm vi đã được xét

Review và approval phải chỉ đúng scope/revision. Thiếu authority hoặc evidence thì ghi Chưa kiểm. Nội dung rõ không tự chứng minh authority đã chấp thuận.

<a id="workflow-4-3"></a>

## Phụ thuộc

Shared model/policy và consumer được nối bằng typed references. Giữ ID nguồn. Một Epic không mặc định tương ứng một Bounded Context.

<a id="workflow-5"></a>

## Đầu vào thực thi

Story đọc Epic Use Case, BR/AC/contracts, allocation, Prototype khi áp dụng và findings hiện hành. Không yêu cầu một Baseline package, receipt hoặc PM merge gate do kit tự đặt.

<a id="workflow-5-1"></a>

## Review trước nhận việc

BA/Dev/QA review phần phù hợp; Business/PM authority theo policy dự án. Agent không giả chữ ký, không gộp các authority vào lint PASS.

<a id="workflow-5-2"></a>

## Tham chiếu từ Story

Story ghi parent/derived-from/depends-on/verifies với ID, revision và locator phù hợp. Khi bàn giao, thêm commit/build refs nếu thực tế đã có; không tự bịa SHA.

<a id="workflow-6"></a>

## Từ đặc tả đến thực thi

Làm rõ Capability/Epic → solution và Story allocation → review → kiểm readiness → bàn giao triển khai. Không tự tạo ticket, merge hoặc thay status vì đã soạn xong tài liệu.

<a id="workflow-14"></a>

## Thay đổi và revalidation

crm-assess-change so delta với nội dung hiện hành, truy consumer và chỉ rõ evidence mất hiệu lực. Khi được giao author, cập nhật bản canonical rồi review lại phần ảnh hưởng. Giữ ID cùng mục tiêu, tăng revision; lịch sử và rationale qua Git. Không tự giữ old approval cho new behavior.

Các anchor workflow-* được giữ để truy nguồn bản standard gốc; policy hiện hành ở nội dung 3.0.0 này. Xem [hồ sơ hiện hành](current-state-and-history.md).
