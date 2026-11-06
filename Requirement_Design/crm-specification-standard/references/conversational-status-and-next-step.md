# Trả lời việc vừa làm, trạng thái hiện tại và bước tiếp theo

ID: CRM-CONVERSATIONAL-STATUS · CRM Workflow Kit 1.7.1 · 04/11/2026

Đọc khi user hỏi bằng ngôn ngữ tự nhiên như “vừa làm gì xong?”, “đang tới đâu?”, “còn thiếu gì?”, “nên làm gì tiếp?”. Dùng chung crm-report-status; không thêm function hoặc slash command. Agent tự chọn cách diễn đạt, chỉ nạp nguồn phù hợp độ sâu của câu hỏi.

## Chọn độ sâu

| Mode | Ý định | Nguồn và đầu ra tối thiểu |
|---|---|---|
| Recap | Việc vừa thực hiện trong run/lượt làm việc gần nhất | Dùng observed actions/tool results đã có; nêu output/file, kiểm chứng và phần chưa thực hiện. Không biến kết quả run cũ thành trạng thái hiện tại |
| Current status | Trạng thái một Project/Capability/Epic/Story/Task tại thời điểm hỏi | Đọc lại canonical artifacts, current revision và status/evidence source liên quan. Tách draft/review/approval/baseline/readiness/implementation/acceptance, nói phần chưa xác minh |
| Next step | Việc nên ưu tiên để đạt mục tiêu hiện tại | Xét mục tiêu + current status + blocker/dependency; đề xuất một bước chính, lý do, function/target, inputs và điều kiện bắt đầu |
| Full report | User cần tổng hợp/so sánh kỳ, coverage, counts hoặc forecast | Dùng progress-report template và measurement policy; snapshot/mẫu số/source refs phải tái kiểm được |

Một câu hỏi có thể cần nhiều mode; trả lời gộp, không lặp bốn báo cáo. Không ép Recap phải có Jira, baseline hoặc estimate chưa liên quan. Current status của một Story không bắt roll up toàn Project. Chỉ dùng bảng/chi tiết khi giúp người đọc ra quyết định.

## Context và nguồn sự thật

Recap hẹp có đủ observed evidence trong phiên có thể trả lời ngay; không bắt chạy helper hoặc nạp full report chỉ để nhắc lại việc đã làm. Nói rõ đây là kết quả run gần nhất nếu không kiểm current state. Không dùng kế hoạch/dự kiến như evidence đã thực hiện. Khi cần đối soát hiện tại, chuyển Current status.

Current status/Next step cần context phù hợp: project/workstream, target/scope, revision đang đọc, snapshot time/timezone khi có dữ liệu động hoặc so kỳ. Có config thì dùng helper context crm-report-status và chỉ mở refs cần thiết. Revision chưa rõ thì đọc để xác định, không bịa baseline SHA. Target rõ từ yêu cầu/việc đang làm thì dùng target đó; resume từ phiên mới phải xác minh checkpoint/current refs, không suy một active Epic ngầm. Nếu nhiều target có thể trả lời khác nhau, có thể đưa overview có scope rõ rồi hỏi phần ảnh hưởng lựa chọn; không hỏi lại fact đã đọc được.

| Claim | Nguồn cần đối chiếu |
|---|---|
| Vừa tạo/sửa/kiểm gì | Tool result/run evidence + artifact refs/revision; chat dùng để xác định ý định và phạm vi |
| Nội dung/scope hiện hành | Artifact canonical, source/decision/allocation và revision; working tree không tự là merged baseline |
| Review/approval/Ready | Review/readiness/authority records pin đúng target/revision; file tồn tại hoặc lint PASS không đủ |
| Delivery/task/sprint | Nguồn trạng thái động do project chỉ định: Jira snapshot hoặc state/engine hiện có; không tự lấy một nguồn chung cho mọi repo |
| Runtime/nghiệm thu | Build/run/acceptance evidence đúng scope; code tồn tại hoặc workflow xong không chứng minh sản phẩm Done |

Tuân project instructions về canonical locations. Chat, handoff và tracker lịch sử là điểm tìm nguồn; không thay trạng thái hiện hành. Nếu sources khác nhau, nêu discrepancy theo revision/thời điểm, không tự sửa dữ liệu để khớp. Thiếu access/evidence ghi Chưa kiểm/Unknown đúng phần; không giả báo cáo current từ snapshot cũ.

Không tạo một % hoàn thành chung khi thiếu scope/mẫu số/phương pháp. Phân biệt “Epic draft đã viết”, “spec đã review”, “baseline đã duyệt/merge”, “Story Ready”, “code triển khai” và “sản phẩm nghiệm thu”. Chỉ khẳng định tầng đã có evidence. Lợi ích sản phẩm không suy từ số artifact hoặc số test tooling.

Khi status dùng function list/estimation hoặc allocation, áp dụng [checkpoint nguồn scope](source-scope-and-decomposition-checkpoint.md). Có thể báo số nguồn công bố cùng provenance và ghi cách phân rã chưa được review; không tự biến câu hỏi status thành một đợt chia lại toàn scope.

## Chọn next step theo điều kiện

Chọn việc giúp tháo blocker hoặc tạo đầu ra có thể review tiếp theo, không lấy thứ tự danh sách function như lệnh phải chạy. Ưu tiên cụ thể trong scope; nếu chưa có dữ liệu để xếp ưu tiên thì nói căn cứ còn thiếu, không bịa capacity/deadline.

| Tình huống đã đối soát | Next function / action đề nghị |
|---|---|
| Chưa rõ nguồn/policy/authority dự án | crm-setup-project cho Project/workstream; ghi source/gap, không tự đặt policy |
| Chưa rõ ranh giới Capability hoặc meaning/rule Epic | crm-define-capability / crm-specify-epic theo target; đưa câu hỏi BA cụ thể |
| Rule/slice đã rõ, thiếu contract/query model/feasibility | crm-design-solution trên Epic với requirement revision và inputs kỹ thuật được phép đọc |
| Cần phân rã Story/brief hoặc sửa allocation | crm-prepare-stories trên Epic/Story/Task phù hợp; chưa đủ thì soạn draft, không tự Ready |
| Nội dung đã chuẩn bị, cần phản biện | crm-review-specification trên đúng revision; findings sửa bằng workflow tác giả |
| Chuẩn bị baseline hoặc xét đủ điều kiện nhận việc | crm-prepare-baseline / crm-check-readiness khi inputs áp dụng có evidence; còn thiếu thì ghi gap |
| Thay nghĩa/scope đã baseline | crm-assess-change trước correction/revalidation bị ảnh hưởng |
| Bước tiếp theo thuộc DDD, sprint/state hoặc external action | Route theo project instructions và quyền hiện có; không ép thành Spec Kit function |

Đề xuất một bước chính với lý do, function/target, input refs cần đọc và điều kiện còn thiếu; có thể thêm một lựa chọn phụ nếu quyết định phụ thuộc mục tiêu user. Không gán owner/due khi chưa được giao, không tự coi recommendation là permission mới. Câu hỏi status không tự mở rộng scope hoặc authorize Jira/state mutations. Nếu một nhiệm vụ đang chạy đã được giao đủ quyền, trả lời status rồi tiếp tục phần đó; không tạo vòng xin phép lại hoặc bỏ nhiệm vụ đang làm chỉ vì user hỏi tiến độ.

## Trả lời và persistence

Mẫu ngắn tùy câu hỏi, không phải ba heading bắt buộc mỗi lần:

```text
Vừa hoàn thành: việc thực tế, file/output và kiểm chứng.
Hiện tại: target/revision đang ở bước nào; blocker hoặc phần chưa xác nhận.
Tiếp theo: một việc ưu tiên + lý do; function/target và input/điều kiện cần.
```

Chỉ cần Recap thì có thể một đoạn. Không điền hàng loạt N/A hoặc catalog để đủ mẫu. Full report vẫn dùng measurement/report template. Kit/package recap theo actual install/validation result thuộc admin context, không bịa Epic/Story hay áp DoR của sản phẩm lên package.

Read-only/status question mặc định trả trong chat, không tự tạo report file, sửa target, checkpoint, state hoặc ticket. Khi user yêu cầu lưu/bàn giao hoặc workflow authoring đã có quyền ghi và vừa đạt một mốc có output đáng kể, ghi checkpoint ở handoff/report được giao; có thể là section hiện có, không cần file cho từng câu hỏi.

Checkpoint tối thiểu: target/scope và input/output revisions; artifact links; observed result/check evidence; open questions/blockers; next function/action + lý do và inputs/điều kiện. Ghi snapshot/source refs đủ để người khác đọc lại, không chép toàn chat. Có thể dùng [handoff template](../assets/templates/work-context-and-handoff-template.md). Checkpoint là index dẫn nguồn, không là backlog/state hoặc approval mới; không lưu active target toàn cục. Không sửa artifact đã pin/baseline chỉ để thêm checkpoint; dùng record riêng trong vùng ghi được giao nếu cần, giữ target/evidence đang kiểm nguyên vẹn.

Khi resume, đọc checkpoint để tìm nguồn rồi so current revisions; nói phần stale hoặc mất access. Next step được tính lại theo nguồn hiện hành, không lặp recommendation cũ khi điều kiện đã đổi.
