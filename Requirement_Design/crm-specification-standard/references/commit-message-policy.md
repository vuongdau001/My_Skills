# Commit message và cơ chế kiểm tra

ID: CRM-COMMIT-POLICY · CRM Workflow Kit 3.0.0

Policy này chỉ áp dụng khi người dùng đã giao commit. Nó không cấp quyền commit/push hoặc thay policy dự án có thẩm quyền cao hơn.

## Căn cứ và phần mở rộng

Dùng [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) làm nền: type, optional scope, description và breaking change marker/footer. Kit bổ sung scope bắt buộc, header tối đa 100 Unicode characters, trường Why/Validation bắt buộc, không placeholders hoặc mô tả chỉ là update/fix/done. Đó là policy riêng, không là yêu cầu mặc định của chuẩn.

Source máy đọc là assets/installation/commit-policy.json; cùng validator được dùng trước commit, hook và CI. Các type được khai trong file đó; mô tả tiếng Việt hoặc tiếng Anh đều hợp lệ. Scope là thành phần thật (layout, records, scoring) hoặc ID nguồn như EPIC-CRM-013; không tạo ID giả để đủ form.

```text
fix(records): ngăn tái dùng review khi nội dung thay đổi

Why: Review chỉ có hiệu lực với nội dung đã được kiểm.
Validation: Đã chạy regression test cho stale revision; PASS.
```

Ví dụ là dữ liệu minh họa, không là evidence test đã chạy. Why giải thích nguyên nhân/đích đến, Validation nêu kiểm tra thực tế hoặc chưa chạy và lý do. Sửa typo có thể ghi ngắn; không bắt diễn giải dài. Một commit có một mục đích, tránh gộp thay đổi không liên quan. Giữ ID liên quan khi có, không ép mọi commit phải có ticket.

Breaking change dùng ! hoặc BREAKING CHANGE footer, và kit luôn yêu cầu mô tả tác động cùng Migration: cách chuyển đổi. Merge/revert/amend và squash commit cuối cũng phải qua cùng policy; không miễn toàn bộ merge commits. Repo chọn squash/rebase nếu muốn tránh default merge message không đạt.

## Agent preflight

1. Đọc policy và staged diff; chỉ stage scope được giao, không dựa vào tên file để đoán nội dung.
2. Soạn message vào file tạm; chạy scripts/commit_policy.py validate --message-file <file>.
3. Sửa message đến khi đạt; commit bằng --file. Nếu hook/tool không chạy được, báo giới hạn, không tự bypass.
4. Đọc lại git show -s --format=%B HEAD và xác nhận message, scope và kiểm chứng đúng.

Không dùng --no-verify, tắt core.hooksPath, sửa validator/config hoặc forge Validation để qua check. Policy hợp lệ về cấu trúc không chứng minh message đúng với diff hoặc test đã chạy; agent/reviewer phải đối chiếu evidence.

## Local hook

Chạy scripts/commit_policy.py install-hook --repo <repo> để xem plan, thêm --apply để cài khi đã được giao. Helper chỉ cài wrapper commit-msg vào Git hook directory mặc định khi chưa có file. Nó không đổi core.hooksPath hoặc ghi đè hook hiện hữu. Repo đã dùng hook manager cần gọi validator từ hook sẵn có, giữ các check khác.

Kit install/update không tự bật hook. Khi install --apply đã xong và user giao cài hook, gọi helper từ chính bản cài mới. Doctor báo enabled chỉ khi effective hook có đúng nội dung và executable bit của wrapper; custom hook được ghi chưa xác minh. Cần test Git thật trên repo tạm. Chỉ tạo file hook mà chưa xác minh effective path không được gọi là enforced.

Git commit-msg có thể bị bỏ qua bằng --no-verify hoặc cấu hình khác. Xem [Git hooks](https://git-scm.com/docs/githooks#_commit_msg). Agent dùng Git API cũng không chạy local hook. Instructions/hook local không bảo đảm mọi agent tuân thủ.

## CI và nhánh bảo vệ

scripts/commit_policy.py range --repo <repo> --base <base-sha> --head <head-sha> kiểm tất cả commit mới, không chỉ HEAD. Mẫu assets/installation/commit-policy-ci.yml.template cần điều chỉnh package path và pin action versions trước sử dụng. Đây là template, installer không tự bật CI/ruleset.

Đặt check thành required, yêu cầu PR, giới hạn bypass và bảo vệ workflow/policy/validator bằng review phù hợp. Nếu agent có thể sửa cùng validator hoặc có quyền bypass thì không có bảo đảm enforcement. Validate message cuối của squash merge qua policy tương ứng; PR commits đạt không tự chứng minh squash message đạt. CI chỉ báo fail nếu chưa có rule chặn merge. Xem [commitlint CI](https://commitlint.js.org/guides/ci-setup.html) và [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).

Kit dùng validator Python stdlib cho profile Conventional Commits đã công bố để không thêm Node dependency cho mọi project. Đây không phải bản thay thế toàn bộ commitlint; nếu repo đã dùng commitlint, tích hợp quy tắc tương đương vào cơ chế hiện hữu, không cài chồng để hai bộ policy lệch nhau.
