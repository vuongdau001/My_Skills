---
name: feature-spec-design
description: Phát triển ý định feature thành đặc tả nghiệp vụ, use case, scenario và UX Flow có nguồn và assumption rõ ràng. Dùng khi khám phá hoặc chỉnh requirement; dừng trước FE preview và thiết kế chi tiết màn hình.
---

# Feature Specification & UX Flow

Biến yêu cầu sơ khai thành đầu vào đủ rõ để người hoặc AGY thiết kế và validate. Viết tiếng Việt; giữ technical identifiers và ID ổn định. Áp dụng RAVE như phương pháp phân tích, không như quota tài liệu hoặc số vòng.

## Ranh giới

- Sở hữu ý định → mô hình nghiệp vụ → use case/scenario → UX Flow.
- Chỉ đọc code/UI để hiểu hiện trạng. Không tạo FE preview, sửa product code hoặc thiết kế pixel/control chi tiết trong workflow này.
- User có thể giao quyền tự quyết. Trong quyền đó, chọn phương án có cơ sở, ghi assumption và ảnh hưởng; không giả owner approval.
- Chỉ hỏi khi không có kết quả mong muốn đủ cơ sở, nguồn yêu cầu xung đột, hoặc cần mở rộng scope/quyền. Tiếp tục phần không phụ thuộc câu trả lời.
- Không suy ra quyền publish, launch AGY, commit, push, deploy hay cập nhật tracker từ việc tạo đặc tả.

## Workflow

Đọc [specification-and-decisions.md](references/specification-and-decisions.md) để dùng record và tiêu chí kiểm tra.

1. **Ground & discover.** Đọc instructions, quyết định trước, code/UI và journey liên quan. Ghi business goal, actor, capability, entity, scope và kết quả thành công. Hành vi code là hiện trạng đã quan sát, không tự động là luật sản phẩm mong muốn.
2. **Challenge.** Tìm actor thiếu, thuật ngữ mơ hồ, luật xung đột, permission/lifecycle gap và dependency. Phân biệt fact, quyết định, assumption và unresolved; ghi nguồn cụ thể.
3. **Model.** Dựng entity lifecycle, valid/invalid transitions, actor được phép, pre/postconditions và invariant. Dùng state diagram/bảng quyền khi giúp giải thích; không ép mọi entity phải có diagram.
4. **Explore.** Tạo use case theo mục tiêu actor và scenario từ model. Với từng capability quan trọng xét happy, alternative, edge/boundary, exception, permission, state, concurrent, duplicate/idempotency, consistency, recovery/cancellation. Ghi N/A kèm lý do khi không áp dụng; không nhân scenario cho biến thể cùng hành vi.
5. **UX Flow.** Mô tả điểm vào, dữ liệu cần thấy, bước/action, screen responsibility, outcome, navigation và recovery theo actor. Xác định trạng thái nào phải xuất hiện; để layout, copy chi tiết và cách triển khai FE cho bước validate.
6. **Desk validate & refine.** Tìm lỗi từ góc nhìn business owner, end user, BA, QA, security/data integrity và operations/support; một lượt review có thể bao phủ nhiều góc nhìn. Kiểm tra completeness, consistency, testability, traceability và counterexample. Sửa nguồn gốc rồi kiểm tra phần bị ảnh hưởng. Không gọi simulated walkthrough là observed browser behavior.

Dừng phân tích khi không còn gap blocking và lượt tiếp theo không tạo phát hiện có ý nghĩa. Nếu hết nguồn lực trước đó, ghi rõ phần chưa đạt; không đổi acceptance để đạt trạng thái cuối.

## Nội dung hiện hành

Mặc định dưới `docs/features/<feature-slug>/`:

- `SPEC.md`: mục tiêu, scope, actor/capability/entity, business rules, lifecycle/permissions, requirement, use case/scenario, acceptance và NFR liên quan.
- `UX_FLOW.md`: journey, navigation, screen responsibilities, data/status/outcome và recovery, liên kết scenario.
- `DECISIONS.md`: nguồn quyết định, assumption, lịch sử và impact links.

Tôn trọng đường dẫn user giao và tài liệu hiện hành; không tạo bản competing spec. Feature nhỏ có thể ghép các nhóm vào một file. Trang đầu chỉ rõ nơi chứa từng nhóm, revision và trạng thái. Không cần file handoff, dashboard hay machine schema riêng; phase RAVE không bắt buộc có file riêng.

## Kết thúc

- `UX_FLOW_READY_FOR_VALIDATION`: các luồng quan trọng có expected result, permission và recovery; record có nguồn/assumption; không còn mâu thuẫn blocking. Active assumption được phép nếu có quyết định trong quyền được giao và expected behavior rõ.
- `BLOCKED`: còn quyết định/dependency khiến không thể xác định hành vi cần thiết hoặc chưa hoàn tất tiêu chí readiness. Ghi blocker, affected IDs, phần đã hoàn thành và bước gỡ.

Báo đường dẫn nội dung, revision, trạng thái, assumption quan trọng và phần chưa xác minh. Đây là đầu vào cho `feature-spec-design-validate`, chưa phải design PASS. Người tiếp nhận không cần skill/tool riêng của Codex để đọc hoặc thực hiện.
