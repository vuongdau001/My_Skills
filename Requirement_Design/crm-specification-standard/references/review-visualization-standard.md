# Minh họa đặc tả để review và tra cứu

ID: **CRM-VISUAL-REVIEW** · CRM Workflow Kit 2.3.0 · 16/11/2026

Áp dụng khi author/correction hoặc review đặc tả, model, solution và UI contract. Mục đích là giúp reviewer thấy hành vi, điều kiện, trách nhiệm và khoảng trống; đồng thời giữ nội dung có thể tìm kiếm và truy vết bằng AI. Dùng cùng [standard viết artifact](artifact-writing-standard.md), catalog và models hiện hành. Không thêm function, schema hoặc gate approval.

## 1. Chọn hình thức theo câu hỏi review

Khi nội dung có nhiều bước/nhánh, tổ hợp điều kiện, trách nhiệm hoặc quan hệ khó đọc, bổ sung hình thức minh họa phù hợp. Với nội dung đơn giản, danh sách có cấu trúc hoặc bảng ngắn có thể đã đủ. Không đặt số lượng diagram tối thiểu cho một artifact và không vẽ lại cùng một model ở nhiều mục.

| Câu hỏi cần trả lời | Hình thức ưu tiên | Khi cần đổi hoặc bổ sung |
|---|---|---|
| Những bước và nhánh nào dẫn tới kết quả? | Flowchart hoặc Activity Diagram + mô tả bước/nhánh | Dùng BPMN khi cần ngữ nghĩa quy trình, sự kiện và phối hợp rõ hơn |
| Ai bàn giao cho ai, chờ gì, hết hạn hoặc gián đoạn ra sao? | BPMN; swimlane cho phân trách nhiệm đơn giản | BPMN có pool/lane, message/event/gateway; số actor không phải điều kiện bắt buộc để chọn BPMN |
| Actor dùng chức năng nào trong boundary nào? | Use Case Diagram hoặc bảng actor–goal–boundary | Diagram này không thay trình tự và nhánh trong E03 |
| Command nào chuyển state, dưới guard nào? | State Diagram + transition/command matrix | Một khởi tạo đơn giản có thể chỉ cần dòng chuyển và ref lifecycle dùng chung |
| Tổ hợp điều kiện nào quyết định kết quả? | Decision table + witness input | Không thay bằng cây flow quá lớn; cân nhắc DMN khi cần quản lý decision model chuẩn |
| Dữ liệu nào liên quan hoặc phụ thuộc dữ liệu nào? | Data dictionary; sơ đồ quan hệ khái niệm khi hữu ích | Chưa có DB/schema thì không trình bày quan hệ như thiết kế lưu trữ đã chốt |
| Ai được làm gì trên dữ liệu nào? | Permission matrix | Cần cả positive/negative cases, scope và quyền cấp trường; diagram actor không thay ma trận quyền |
| Người dùng nhìn thấy và thao tác gì ở mỗi tình huống? | Mockup có chú thích + UI-state table + Prototype theo gate | Một ảnh form mặc định không bao phủ loading/error/empty/disabled/unknown outcome |
| Các thành phần trao đổi gì, vào lúc nào? | Sequence Diagram + contract refs | Hữu ích với callback, commit, timeout, retry, concurrency; không bắt mỗi CRUD có sequence riêng |
| Thiếu dependency nào để thực hiện scope? | Dependency table; graph khi quan hệ nhiều tầng | Graph không tự chứng minh feasibility, owner commitment hoặc kiến trúc đã chọn |
| Nhánh nào được AC/test condition bao phủ? | Coverage matrix | Có link AC chưa chứng minh expected result đủ hoặc đã chạy Pass |
| Đo gì, trong điều kiện nào, đạt khi nào? | Metric/workload/threshold/measurement table | Biểu đồ kết quả chỉ dùng khi có dữ liệu và nguồn; không đặt số giả làm acceptance |

Swimlane là cách phân vùng trách nhiệm, không tự biến flowchart thành BPMN. Mermaid là một lựa chọn viết diagram dạng text, không đồng nghĩa BPMN. Khi gọi sơ đồ là BPMN phải dùng đúng ngữ nghĩa, đặc biệt sequence flow trong process và message flow giữa các participant; sơ đồ giản lược phải ghi rõ loại và giới hạn.

## 2. Áp dụng cho Epic E01–E16

Đây là hướng dẫn chọn cách trình bày, không thay tiêu chí applicability hoặc nội dung của [Epic catalog](epic-specification-catalog.md).

| Mục | Minh họa cần cân nhắc | Điều cần giúp reviewer nhận ra |
|---|---|---|
| E01 | Bảng in/out/dependency; boundary diagram nếu nhiều bên | Ranh giới hệ thống, goal và scope đợt khác nhau |
| E02 | Actor/interactions/interests table; actor diagram khi cần | Actor thực sự tương tác khác nhóm chịu tác động và vai trò SDLC |
| E03 | Tóm tắt → kết quả/bảo đảm → flow tổng quan nếu hữu ích → bước chính → nhánh | Mỗi nhánh có điều kiện, hành vi, quay lại/kết thúc hoặc gap cụ thể; giữ locator ổn định |
| E04 | State diagram + transition matrix, hoặc dẫn shared lifecycle | Guard, denied/no-op và side effects; không kéo lifecycle ngoài scope vào Epic |
| E05 | Decision table khi có tổ hợp điều kiện; ví dụ dữ liệu cho rule dễ hiểu sai | OR/AND, overlap/default/priority và trường hợp chưa xác định |
| E06 | Data dictionary + ví dụ boundary/normalization | Required, empty/null, valid/invalid references và điều còn thiếu |
| E07 | Permission matrix | Principal/action/resource/scope/condition/fields, allow/deny và authority |
| E08 | UI-state table, annotated mockup và Prototype khi đủ điều kiện theo gate | Mỗi trạng thái màn hình khớp E03, rule, quyền và command outcome |
| E09 | Contract inventory + sequence khi thứ tự/giao tiếp khó hiểu | Hai đầu contract, điểm ghi, timeout trước/sau ghi và kết quả chưa xác định |
| E10 | Scenario/risk matrix dẫn nhánh E03; zoom-in diagram cho ca khó | Kết quả dữ liệu/state và recovery; không chỉ liệt kê tên lỗi |
| E11 | Bảng NFR/controls và phương pháp đo | Threshold/workload/authority và dữ liệu đo thực tế |
| E12 | Mapping/reconcile table; cutover/recovery flow khi áp dụng | Nguồn–đích, sai lệch, trách nhiệm và điều kiện phục hồi |
| E13 | Dependency/options table; boundary/dependency graph khi hữu ích | As-Is, phương án To-Be, assumption và phần chưa xác nhận |
| E14 | Scenario/outcome → BR/model → AC → test condition/evidence matrix | Coverage một phần, expected result còn thiếu và planned khác executed |
| E15 | Scenario/slice/outcome/dependency table; Story map khi cần | Giữ controls, phần chưa phân bổ và không đếm trùng |
| E16 | Question/decision/approval register có impact và authority | Source, proposal, quyết định và approval có evidence khác nhau |

Story, Capability và solution tái dùng model đúng scope/revision; không tạo lại đủ các loại minh họa của Epic. Một bảng có thể phục vụ nhiều mục qua ref; đặt nơi định nghĩa chính và dẫn tới đó.

## 3. Hợp đồng đọc bằng người và AI

- **Giữ source có thể chỉnh sửa và tìm kiếm.** Mermaid/PlantUML giữ code; BPMN giữ model như `.bpmn`; bảng giữ dạng text có cấu trúc. Với source cần công cụ riêng, kèm render để review và bản mô tả text về hành vi/điều kiện/kết quả. Không giao ảnh-only cho nội dung yêu cầu mới; ảnh nguồn chỉ đọc được dẫn kèm phần mô tả cần thiết.
- **Ghi danh tính và phạm vi.** Mỗi hình/bảng độc lập có tên hoặc caption/anchor rõ, artifact ID, revision và scope (có thể kế thừa context ngay phía trên trong cùng file). Ghi mục đích và giới hạn nếu chỉ là overview. Không sinh namespace/requirement ID mới cho từng node chỉ để vẽ.
- **Giữ liên kết tới nội dung chuẩn.** Dùng ID/anchor bước, nhánh, outcome, BR/AC/contract đã có. Nếu node chỉ dùng nhãn ngắn, có mapping text gần hình. Giữ anchor qua revision khi cùng nghĩa; trace sang artifact khác phải pin revision theo policy hiện hành.
- **Một nơi định nghĩa nghĩa nghiệp vụ.** Diagram là view của flow/rule/model, dẫn tới nội dung chuẩn để tra chi tiết. Decision table có thể là nơi định nghĩa logic nếu artifact chọn nó làm chuẩn; prose và diagram khác dẫn lại, không duy trì nhiều bản logic độc lập.
- **Giữ evidence và uncertainty.** Phân biệt source, suy luận, proposal và authority approval trong caption/text/legend. Có thể vẽ sketch khái niệm với đoạn chưa xác nhận được đánh dấu và nối question/authority; không tự thêm endpoint, thứ tự kiểm, commit, rollback, retry, role grant, SLA hoặc transition để khép hình.
- **Đọc được khi không thấy màu hoặc render.** Đặt nhãn điều kiện trên cạnh và nhãn outcome/Unknown bằng text; màu không phải kênh duy nhất. Dùng contrast/theme theo dự án, chia overview và zoom-in khi hình quá dày. Caption và phần text phải đủ để tìm nhánh/kết quả khi viewer không hỗ trợ diagram.
- **Metadata giữ schema hiện hành.** Code diagram và chú thích ở phần nội dung; không đặt prose/HTML vào JSON metadata hoặc thêm field/schema không được hỗ trợ. Tách source/render nếu cần nhưng giữ path và revision có thể đối chiếu.

## 4. Các trường hợp dễ minh họa sai

**Unknown không phải False.** Với rule `A OR B`, khi A/B đã xác định là False thì rule không phát hiện match; điều đó chưa chứng minh các guard khác đã đạt. Nếu cả hai chưa đủ bằng chứng để kết luận False thì ghi Unknown/question; khi một vế True, logic OR cho match, còn response khi kiểm tra khác lỗi phải có policy. Không suy default allow hoặc precedence từ bố cục bảng.

**Kết quả ghi khác kết quả đọc.** Với timeout/read failure, minh họa điểm nào có evidence command đã ghi và điểm nào chỉ mất response/quyền đọc. Nếu boundary chưa chốt, đánh dấu unknown và gap; không vẽ mũi tên retry/rollback như lựa chọn đã duyệt.

**Ví dụ không phải evidence thực thi.** Ghi dữ liệu minh họa và giả định áp dụng; kết quả nguồn bảo đảm khác kết quả còn mở. Coverage matrix phải hiện cả các phần AC chỉ bao phủ một phần; chỉ gọi runtime Pass khi có TestRun/evidence đúng scope.

**Policy chưa có không cấm mọi sketch.** Có thể dùng bảng trạng thái, storyboard hoặc sequence khái niệm để hỏi đúng câu; đánh dấu proposal/unknown. Prototype được review và gate vẫn tuân thủ [quy trình Prototype](prototype-workflow-and-epic-gate.md); sketch không thay Screen Contract hoặc approval.

## 5. Author self-check và review

Author kiểm view với nội dung chuẩn: actor, từng bước/nhánh, guard, outcome, side effects và trace có cùng nghĩa; ví dụ có đúng điều kiện và question chưa chốt còn hiện. Với source/render tách file, kiểm chúng cùng revision. Khi có công cụ, parse/render diagram và xem nhãn, nhánh, chữ, đường nối; nếu chưa render, ghi rõ giới hạn, không báo visual QA đã đạt. Trình bày đã render không chứng minh semantics đúng.

Reviewer lần theo một đường thành công và các nhóm nhánh rủi ro áp dụng; thử tổ hợp điều kiện hoặc witness dễ nhầm. Ghi locator, expected/observed và ảnh hưởng khi hình/bảng thiếu nhánh, ngầm thêm quyết định hoặc mâu thuẫn với rule/AC. Dùng Q02/Q03/Q04/Q05/Q06 hiện hành theo phạm vi, không tạo gate/readability score riêng.

Thiếu diagram không tự thành finding nếu bảng/văn bản tương đương đã giải đáp rõ câu hỏi review. Khi nội dung phức tạp vẫn khó lần theo, nêu witness cụ thể và đề xuất hình thức phù hợp. Review/check chỉ ghi findings; sửa target bằng workflow tác giả được giao. Update kit không tự rewrite spec, rebaseline hoặc cấp lại approval.

## Tham khảo ký pháp

[UML của OMG](https://www.omg.org/UML/what-is-uml.htm), [BPMN của OMG](https://www.omg.org/bpmn/), [DMN của OMG](https://www.omg.org/spec/DMN). Các chuẩn giúp phân biệt góc nhìn; lựa chọn và mapping E01–E16 phía trên là tailoring của kit.
