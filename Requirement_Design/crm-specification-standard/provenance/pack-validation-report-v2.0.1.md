# CRM Workflow Kit 2.0.1 — Xác định vị trí lát cắt trước khi soạn Capability

Ngày kiểm 06/11/2026.

## Thay đổi phát hành

Define Capability đối chiếu nguồn phạm vi cấp dự án, cây hiện hành và nhóm liền kề trước khi đề xuất Capability mới, cấp CAP ID hoặc ghi C01–C08. Lát cắt thuộc mục tiêu người dùng được đặt dưới Capability cha hiện có hoặc ứng viên. Khi thiếu căn cứ, workflow trả phần phân tích và giữ phương án ở mức ứng viên. C06 ghi nguồn/revision, nhóm đã đối chiếu và vai trò riêng của cấp cha.

Bộ ví dụ phân biệt phản ví dụ lặp mục tiêu tra cứu, cách đặt lát cắt P3 và trường hợp năng lực tìm kiếm độc lập. [Checkpoint](../references/source-scope-and-decomposition-checkpoint.md#project-placement) · [Ca kiểm](../references/pack-acceptance-scenarios.md).

Chuẩn viết và template phân biệt actor nghiệp vụ, bên liên quan nghiệp vụ, vai trò dự án và thẩm quyền theo nội dung. Decision, Assumption và Constraint ghi phạm vi Nghiệp vụ / sản phẩm hoặc Dự án / SDLC trong phần đọc được. Intake, C03/E02/E07 và review cùng dùng quy ước. Giữ schema, ID, trạng thái và cơ chế trace. [Quy ước vai trò](../references/artifact-writing-standard.md#business-and-sdlc-roles) · [Phạm vi áp dụng](../references/knowledge-records-and-evidence.md#record-applicability).

## Kiểm chứng

| Phép kiểm | Kết quả |
|---|---|
| Validator của reference pack | Đạt. 117 tài liệu Markdown, 170 mục registry, 105 mục nguồn lịch sử và 13 workflow functions. |
| Unit/integration suite | 172 test đạt. |
| Context của bản cài thử | `crm-define-capability` nạp workflow và checkpoint có `project-placement` trong context mặc định. Có thể đọc context ở revision `p3-reset-r1` trước khi xác định CAP ID. |
| Phiên Codex mới cho PL01 | Đạt kỳ vọng phân loại trên bản sao P3. Kết quả và đối chiếu hành động ở dưới. |
| PL02 và PL03 | Đã thêm vào danh mục ca kiểm. Phiên Codex kiểm vị trí lát cắt dùng PL01. |
| Context phân loại vai trò | Setup Project, Define Capability, Specify Epic và Review Specification đều nạp quy ước vai trò. Setup Project và Define Capability nạp thêm hướng dẫn phạm vi record. |
| Phiên Codex mới cho RL01–RL03 | Đạt kỳ vọng trên repo tạm với dữ liệu giả lập. Metadata mẫu DEC/ASM/CST giữ nguyên. |

## Quan sát phiên Codex mới

Chạy CLI đi kèm ChatGPT, `codex-cli 0.166.0-alpha.6`, session `01a1afe2-2208-7f52-bcca-da93b4024237`. Bản sao P3 giữ Function List đầy đủ, cấu hình và hồ sơ Setup Project. Cây Capability/Epic chỉ có marker scaffold. Cài ứng viên 2.0.1 và đối chiếu receipt snapshot `7d8d6040c5c3e21369c127bec86d908feb12c863122333fbe0053f5b4f2c797c`. Phiên mở SKILL.md ở package trong bản sao và chạy context helper của package. Phép kiểm quan sát hành vi sau khi mở kit.

**Prompt tái hiện**

> Dùng skill $crm-spec-kit của repo này và workflow crm-define-capability cho workstream p3, revision p3-reset-r1. Hãy soạn riêng lát cắt Customer List, Preview và Detail. Người có quyền cần tìm đúng Customer từ danh sách, xem trước và mở chi tiết, với quyền xem bản ghi và trường dữ liệu được áp dụng xuyên suốt. Dùng các nguồn của workstream trong cấu hình dự án và thực hiện đầu ra phù hợp theo workflow.

**Phân loại quan sát được**

Capability ứng viên “Quản lý hồ sơ Customer và Contact” chứa Epic ứng viên “Tra cứu Customer theo quyền”. Phiên dùng `CC-A` làm locator workshop, với Use Case “Xác định đúng Customer và xem thông tin được phép”. Kết quả dừng ở Epic/Use Case.

Phiên dùng SRC-FL (09/10/2026) với L01, L67, phần đọc L02 và quyền xuyên suốt ở L82. Cấp cha được đối chiếu với L03–L05, liên kết, import/export, BA-D1 và W5. L68 được giữ ở luồng Takeover liền kề. Các kết quả này dùng để kiểm phân loại.

**Đối chiếu hành động**

- Nhật ký lệnh ghi chạy context và đọc nguồn. Phiên không gọi `next-id CAP`, cấp CAP ID hoặc ghi C01–C08.
- Snapshot đường dẫn và SHA-256 trước/sau của 494 mục trong repo thử trùng nhau. Hai thư mục Capability/Epic vẫn chỉ có marker.
- Phiên ghi một file `crm-p3-cap-context.txt` trong thư mục tạm của hệ điều hành để đọc context. Runner lưu stdout JSONL và phản hồi riêng bên ngoài repo thử.

## Quan sát phiên Codex về vai trò

Phiên chỉ đọc `01a1afec-49d8-7ba0-870d-ca0de4850812` nạp context của bốn workflow từ bản cài ứng viên. Dữ liệu giả lập dùng một quản lý Sales vừa duyệt yêu cầu trong CRM vừa được giao ký xác nhận nghiệm thu, một ghi chú ghép rule che email với yêu cầu QA trước handoff và một draft dùng biên bản bàn giao để phê duyệt rule quyền.

| Ca | Kết quả quan sát |
|---|---|
| RL01 | C03 ghi bên liên quan nghiệp vụ. E02/E03 ghi actor duyệt, E07 ghi quyền runtime. Người ký nghiệm thu và QA reviewer có trách nhiệm và evidence riêng ở C08, E16 hoặc Work Context. |
| RL02 | Tách rule che email thuộc sản phẩm khỏi điều kiện QA thuộc SDLC. Hai phát biểu cùng dẫn nguồn nhưng có phạm vi và thẩm quyền riêng. |
| RL03 | Ghi ba findings về gán PM làm actor thiếu tương tác, dùng chữ ký bàn giao sai phạm vi và đưa điều kiện QA vào Use Case. Giữ thẩm quyền rule và kết quả chạy QA ở trạng thái cần xác minh. |

Kết quả được trả trong phản hồi của phiên. Repo thử giữ scaffold và dữ liệu mẫu.

Source diff để review ở working tree. Phạm vi ghi của đợt này gồm kit nguồn và bản sao kiểm thử.
