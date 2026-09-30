# Specification records and readiness checks

Dùng hướng dẫn này khi tạo hoặc chỉnh đặc tả. Chỉ thêm trường và bảng đem lại traceability hoặc thay đổi quyết định; không tạo mục rỗng để đủ khuôn.

## ID ổn định

Dùng ID ngắn, duy nhất trong feature và không tái sử dụng sau khi mục bị bỏ:

- `ACT-###`: actor
- `CAP-###`: capability
- `ENT-###`: entity
- `BR-###`: business rule hoặc invariant
- `REQ-###`: requirement
- `UC-###`: use case
- `SCN-###`: scenario
- `AC-###`: acceptance criterion
- `DEC-###`: quyết định
- `ASM-###`: assumption đang hoạt động
- `UNR-###`: câu hỏi hoặc xung đột chưa giải quyết

Giữ ID khi đổi tên. Khi supersede một mục, đánh dấu trạng thái và liên kết ID thay thế thay vì xóa dấu vết.

## Phân loại record

Mỗi phát biểu quan trọng phải thuộc một loại rõ ràng:

| Loại | Ý nghĩa | Cần ghi |
|---|---|---|
| Fact | Điều được quan sát hoặc xác nhận từ nguồn | Nguồn, thời điểm hoặc revision nếu dễ thay đổi |
| Decision | Lựa chọn đã được người có quyền quyết định | Owner, ngày, rationale, alternatives, impact |
| Assumption | Điều tạm coi là đúng để tiếp tục | Cơ sở, risk nếu sai, cách/owner xác minh |
| Unresolved | Thiếu thông tin hoặc xung đột chưa thể quyết định | Blocker hay non-blocker, affected IDs, next step |

Code, UI và dữ liệu hiện tại chỉ chứng minh hành vi đang tồn tại. Nếu dùng chúng làm căn cứ cho desired behavior, ghi rõ đây là quyết định hoặc assumption, không nâng thành fact nghiệp vụ.

## Nguồn và decision record

Ưu tiên link hoặc đường dẫn cụ thể: user instruction/turn, issue hoặc policy URL, file và dòng/revision, màn hình và trạng thái quan sát, log hoặc dữ liệu có timestamp. Không dùng các nhãn mơ hồ như “theo code” hoặc “theo trao đổi”.

Một decision/assumption record hữu ích gồm:

```markdown
### DEC-001 — <tiêu đề>
- Status: proposed | accepted | superseded
- Source/owner: <nguồn hoặc người có quyền>
- Date/revision: <YYYY-MM-DD hoặc revision>
- Context: <vấn đề cần quyết định>
- Decision: <expected behavior đã chọn>
- Rationale: <vì sao>
- Alternatives: <phương án đáng kể đã loại>
- Impact: <REQ/BR/UC/SCN/UX Flow bị ảnh hưởng>
- Supersedes/superseded by: <ID nếu có>
```

Với assumption, thay `Decision` bằng `Assumption`, đồng thời ghi `Risk if false` và `Validation owner/next step`. Không ghi user hoặc owner đã duyệt nếu chưa có bằng chứng.

## Requirement và scenario tối thiểu

Requirement phải mô tả hành vi quan sát hoặc kết quả nghiệp vụ, có actor/phạm vi áp dụng, điều kiện và liên kết nguồn. Tránh khóa implementation khi business rule không yêu cầu.

Mỗi scenario cần đủ để desk validate và chuyển thành test:

```markdown
### SCN-001 — <mục tiêu hoặc biến thể>
- Links: UC-001, REQ-001, BR-001
- Actor/permission: <ai và quyền cần có>
- Preconditions/state: <điều kiện và trạng thái ban đầu>
- Trigger: <sự kiện bắt đầu>
- Steps: <tương tác hoặc biến đổi nghiệp vụ chính>
- Expected result: <kết quả và trạng thái cuối quan sát được>
- Failure/recovery: <phản hồi, retry, cancel hoặc rollback>
- Source/assumption: <ID hoặc link>
```

Acceptance criterion phải xác minh được và truy ngược đến requirement/scenario. Một criterion không nên gộp nhiều hành vi độc lập khó chẩn đoán.

## Lifecycle và quyền

Với entity có trạng thái, ghi:

- trạng thái khởi tạo và terminal;
- transition hợp lệ, trigger, actor và guard;
- transition bị cấm và expected response;
- side effect, consistency boundary và khả năng retry/rollback;
- hành vi khi request trùng, đồng thời hoặc đến sai thứ tự nếu có rủi ro.

Với quyền, kiểm tra cả khả năng nhìn thấy dữ liệu, thực hiện action và quan sát kết quả; không đồng nhất “không thấy control” với “không được phép ở backend”.

## Traceability check

Kiểm tra theo cả hai chiều:

1. Goal → capability → requirement/business rule → use case/scenario → UX Flow → acceptance.
2. Mỗi bước, trạng thái và outcome trong UX Flow phải có requirement/scenario hoặc assumption/decision làm căn cứ.

Đánh dấu orphan, contradiction và missing coverage. Không tạo ma trận riêng nếu link inline đã đủ rõ.

## Readiness check

Chỉ dùng `UX_FLOW_READY_FOR_VALIDATION` khi:

- goal, scope và out-of-scope rõ;
- actor, capability, entity và thuật ngữ cốt lõi nhất quán;
- business rule, lifecycle, permission, pre/postcondition và invariant cần thiết đã xác định;
- luồng quan trọng có happy path và các biến thể rủi ro phù hợp, hoặc có `N/A` kèm lý do;
- UX Flow nêu entry, dữ liệu/trạng thái cần thấy, action, screen responsibility, outcome, navigation và recovery;
- acceptance testable và traceable;
- fact, decision, assumption và unresolved được phân biệt, có nguồn hoặc owner/next step;
- không còn contradiction hoặc unresolved item chặn việc xác định expected behavior.

Dùng `BLOCKED` nếu một tiêu chí thiết yếu chưa thể hoàn tất. Liệt kê blocker, affected IDs, phần vẫn usable và hành động hoặc quyết định cần để gỡ blocker.
