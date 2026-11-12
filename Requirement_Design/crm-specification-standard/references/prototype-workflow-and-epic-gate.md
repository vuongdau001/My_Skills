# Prototype trong quy trình Epic

ID **CRM-PROTOTYPE** · CRM Workflow Kit 1.12.2

Một Prototype là bản chạy được để diễn tập hành vi UI trong phạm vi Epic đã đặc tả. E08 ghi UI cần làm, D06 đối chiếu hành vi với contract và walkthrough ghi kết quả quan sát. Gate bàn giao sang Story thực thi yêu cầu ba đầu ra này cho scope có tác động UI.

Với Epic use-case-v1, mỗi scenario trong allocation khai refs dạng `EPIC-CRM-…#locator` tới bước/nhánh E03 của đúng Epic/revision/scope. Một bundle hành trình có thể có nhiều allocation theo Epic. [Policy Epic–Use Case](epic-use-case-policy.md).

## 1. Tìm nguồn trước khi viết đặc tả

- Tìm mockup trong Work Context, spec và các vị trí người dùng chỉ định mà bạn có quyền đọc. Nguồn có thể là file trong hoặc ngoài repo, tệp đính kèm, ZIP, link thiết kế hoặc bản demo. Ghi cách tìm lại nguồn, revision hoặc hash nếu có, khả năng mở và scope của từng candidate. Nếu có nhiều bản hợp lý, hỏi bản nào đang được dùng.
- Ngay ở intake, **nhắc người dùng cung cấp chỉ dẫn và mẫu cho Prototype**. Hỏi ngắn về hành trình cần demo, màn hình/bản thiết kế đang dùng, quy ước UI và ví dụ dữ liệu hoặc tình huống muốn thấy. Cho phép gửi link, file, ảnh, video hoặc mô tả. Nếu đã có nguồn, nêu nguồn tìm thấy và chỉ hỏi phần còn thiếu. Ví dụ: “Mình tìm thấy mockup Contact hiện có. Bạn gửi giúp mẫu hoặc chỉ dẫn cho luồng cần demo, nhất là màn hình nào phải bám sát và tình huống nào cần thể hiện.”
- Mở candidate khả dụng, dùng browser với nguồn tin cậy và fixture giả. Ghi Screen ID, actor, field, action, quyền, validation, trạng thái và hành vi quan sát được. Với ZIP, giữ locator cả archive và member. Nếu chỉ có thể đọc mã tĩnh, ghi rõ phạm vi đã kiểm.
- Đối chiếu với rule và Command/Query/AC. Ghi điểm khác biệt, decision/question ID và owner. Dùng quyết định có thẩm quyền khi cập nhật Epic hoặc Story. Trong lúc chờ mẫu/chỉ dẫn, vẫn lập inventory và làm phần spec độc lập. Khi thiếu input ảnh hưởng expected behavior hoặc thiết kế chính, ghi gap và xin quyết định trước khi hoàn thiện phần bị ảnh hưởng.

## 2. Hoàn thiện Prototype sau khi đặc tả đủ cho scope

Chốt scope, BR/AC, role, quyền và trạng thái cần minh họa trước khi hoàn thiện bản nộp gate. Dùng flow, model/contract và criteria đã rõ để chọn scenario. Chạy lại cả chiều spec → UI và UI → spec.

| Tình trạng nguồn | Cách xử lý |
|---|---|
| HTML/Prototype phù hợp và được phép tái dùng | Tái dùng file và dependency cần thiết trong bundle bàn giao. Ghi locator/revision/hash nguồn, phần giữ và delta. Chạy lại từ entrypoint của bundle. |
| Chỉ một phần phù hợp | Tái dùng phần khả dụng, sửa hoặc làm mới phần còn thiếu theo spec. Ghi disposition theo màn hình hoặc asset. |
| Không có nguồn dùng được | Tạo Prototype chạy được từ Epic, UI contract và Story candidates. Ghi lý do và chỉ dẫn người dùng đã cung cấp hoặc đang chờ. |
| Scope không tác động UI | Ghi E08 N/A với lý do, contract liên quan và người xác nhận. Dùng cùng gate để kiểm evidence N/A. |

Ghi draft HTML/CSS/JS và fixture giả trong vùng prototypes khi được giao author. Giữ nguồn gốc read-only, dùng asset local và tránh account/dữ liệu thật. Reviewer mở bản được chọn, ghi findings và walkthrough trong reviews. Author cập nhật spec/Prototype trong bước riêng. Đối với nội dung đã baseline, bắt đầu bằng crm-assess-change.

## 3. Tổ chức bundle theo hành trình

Đặt bản Prototype chạy được để review và bàn giao trực tiếp trong category prototypes của Work Context. Với layout numbered, đây là thư mục `09-prototypes/` dưới spec_root. Bàn giao từ chính bundle này để người review và baseline cùng tham chiếu một bản.

Mỗi hành trình người dùng có một thư mục ngay dưới category prototypes, đặt tên theo việc người dùng làm và giữ tên ổn định khi lên revision. Chia file theo màn hình bên trong `screens/` và dùng chung entrypoint, assets, fixture cho cả luồng. Ghi phân bổ Epic, revision và scope trong manifest để một hành trình có thể đi qua nhiều Epic. Baseline pin revision và hash của bundle đã review.

Ví dụ layout numbered cho một hành trình tạo Contact. Nếu bundle minh họa cả tạo và gắn, liệt kê scenario và phân bổ cho từng Epic, kể cả khi các scenario dùng chung entrypoint.

```text
09-prototypes/
  contact-create/
    README.md
    manifest.json
    scenarios.md
    app/index.html
    screens/
    assets/
    fixtures/
05-reviews/
06-baselines/
```

- **README.md** ghi phạm vi, nguồn và disposition, cách chạy, giới hạn mô phỏng và cách tới từng scenario. Một Screen ID có một bản canonical cho phạm vi/revision đang dùng. Dùng cùng bundle qua allocation khi nhiều Epic hoặc Story dùng chung màn hình.
- **manifest.json** nối Epic ID/revision/scope → Scenario ID → Screen ID → BR/AC/contract refs. Pin SHA256 của scenarios.md và mọi file trong app, screens, assets, fixtures. Giữ runtime dependencies trong các thư mục này và đóng gói entrypoint chạy được.
- **scenarios.md** ghi actor, fixture, trigger, bước, expected UI và expected contract. Chọn happy path và các nhánh validation/permission/empty/loading/error ảnh hưởng scope. Ghi hành vi giả lập và giới hạn của nó.
- **Walkthrough** nằm trong reviews, ghi revision, cách chạy, người tham gia, kết quả từng scenario, chênh lệch và verdict. **Baseline** pin Epic, manifest, walkthrough và Story allocation đúng revision. Dùng mẫu bundle và walkthrough bên dưới.

## 4. Gate, DoR và scoring

| Bước | Điều kiện và evidence |
|---|---|
| Bàn giao Epic → Story thực thi | Có bundle runnable, walkthrough Đạt đúng scope/revision và findings chặn đã xử lý, hoặc evidence N/A được xác nhận. PM xem cùng baseline package. Gate này diễn ra sau đặc tả. Epic entry DoR cho phép bắt đầu làm rõ trước đó. |
| DoR của Story thực thi | Mở đúng baseline/commit đã xác nhận. Với UI, kiểm Story có Screen/Scenario IDs, BR/AC/contract refs, entrypoint và walkthrough còn áp dụng. Với scope backend dẫn disposition và contract tương ứng. Thiếu hoặc stale thì ghi điều kiện DoR bị chặn. |
| Scoring E08 | Với UI, mức 2/3 yêu cầu walkthrough hiện hành và Prototype đúng scope. Mức 3 vẫn cần specialist/independent review theo rubric. Khi thiếu hoặc stale evidence, điểm hiệu lực E08 tối đa mức 1 nếu đã chấm. E08 N/A thiếu evidence trở thành Unknown. |

BA/Business xác nhận hành vi nghiệp vụ, UX xác nhận trải nghiệm, TL xác nhận Command/Query và feasibility, QA đối chiếu expected outcomes. PM chốt phạm vi baseline theo quy trình hiện hành. Đối chiếu UI Contract hoặc DDD artifacts khi workstream có những hồ sơ này.

Workstream mới bật `prototype_gate: true`. Với workstream cũ, bật rõ trong config khi áp dụng. Chạy `lint --gate baseline --target <EPIC-ID>` hoặc dùng Baseline target có trace dependency đến Epic. Helper kiểm cấu trúc, files/hash, scope và evidence khai báo. Người review cần tự chạy Prototype và kiểm expected behavior. Scoring dùng cùng phép kiểm cho scope E08. Khi Epic, scenario, manifest hoặc runtime file thay đổi, chạy lại walkthrough phần ảnh hưởng và cập nhật pin sau review. Giữ biên bản cũ theo revision.

- [Mẫu bundle Prototype](../assets/templates/prototype-bundle-template.md)
- [Mẫu biên bản walkthrough Prototype](../assets/templates/prototype-walkthrough-template.md)
- [Quy trình baseline](baseline-and-change-control.md)
- [DoR và thẩm quyền bàn giao](readiness-completion-and-approval-gates.md)
- [Scoring](definition-maturity-scoring.md)
