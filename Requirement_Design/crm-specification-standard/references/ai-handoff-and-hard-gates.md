# Bàn giao context và enforcement

ID: CRM-AI-HANDOFF · CRM Workflow Kit 3.0.0

<a id="workflow-13"></a>

## Bàn giao từ hồ sơ hiện hành

Dẫn canonical target ID, scope, path/locator, revision và dependency. Nếu đang dùng commit/build cụ thể thì dẫn đúng reference đã xác minh. Không tạo package/receipt/BASE ID để bàn giao. Người nhận đọc lại nguồn và báo phần stale hoặc thiếu access.

<a id="workflow-13-1"></a>

## Trước thực thi

Đối chiếu Story outcome, Epic E03, BR/AC/contract, Prototype và review hiện hành. Kiểm policy/authority, environment/data/access và capacity khi áp dụng. Không bắt merge Git mặc định để được viết Story hoặc xét DoR; yêu cầu merge chỉ áp dụng khi policy dự án đã quyết. Không tự tạo ticket hoặc đoán Jira key.

<a id="workflow-13-2"></a>

## Handoff tối thiểu

Target/scope và revision; source/dependency refs; desired output; findings còn mở; evidence đã xem/chưa kiểm; receiver/authority nếu đã biết. Có thể là câu trả lời chat hoặc section hiện hành được giao, không file checkpoint mới. Không dùng lời AI xác nhận thay human approval hay actual action.

<a id="workflow-13-3"></a>

## Hard gates nằm ở hệ thống thực thi

Instructions không tự chặn Git/Jira/CI. Kit chỉ audit bằng evidence được phép đọc. Muốn enforce cần hook/check/ruleset thật, xác minh đang active và quyền bypass. Commit policy dùng chung validator ở agent preflight/local hook/CI; xem [commit policy](commit-message-policy.md). Kit không tự bật các hệ thống đó.

Dev→QA và Done dựa policy dự án: code/review/CI, build/config/environment, test/defect/verdict đúng revision và thẩm quyền. Stale/skipped/not-run không là PASS. Không suy sản phẩm Done từ spec, lint hoặc code tồn tại.
