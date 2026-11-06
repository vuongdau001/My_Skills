# Checkpoint nguồn scope và cách phân rã

ID: **CRM-SCOPE-CHECKPOINT** · CRM Workflow Kit 1.11.0 · 05/11/2026

Dùng khi tiếp nhận function list, WBS, bảng estimation, screen list; khi tạo/sửa allocation Feature/Epic/Story; hoặc khi review/báo tiến độ dựa vào các đơn vị đó. Mục tiêu là giữ đủ scope và giải thích được ranh giới bàn giao, trước khi dùng số đếm để đưa ra kết luận.

## Áp dụng đúng độ sâu

Checkpoint này là phần kiểm của workflow hiện có, không thêm function hoặc một approval gate mới. Authoring thực hiện phần kiểm áp dụng trước khi đề nghị chốt allocation. Review ghi findings, không sửa target. Status chỉ đọc evidence đúng revision và nêu phần chưa kiểm; không tự chia lại scope hoặc tạo report file khi người dùng chỉ hỏi tiến độ.

Nếu đã có kết quả kiểm hiện hành, dẫn lại scope/revision và kiểm delta thay vì làm lại toàn bộ. Recap hẹp hoặc Task-only không thay allocation thì không cần lập inventory mới. Thiếu thông tin vẫn có thể soạn candidates và làm rõ phần độc lập; chưa kết luận allocation đã đạt hoặc scope đã hoàn tất.

<a id="level-selection"></a>

## Chọn cấp độ và kiểm quan hệ cha–con

Phần này là quy tắc tối thiểu khi tạo hoặc thay allocation, được nạp trong context mặc định. Áp dụng theo phạm vi nhiệm vụ; không chạy lại toàn cây cho sửa đổi cục bộ không đổi ranh giới.

1. **Tìm vị trí trước khi tạo cấp mới.** Đọc Feature/Epic hiện có và quy ước cấp độ của workstream. Chọn nơi nhận yêu cầu hoặc ghi candidate/gap nếu chưa có. Phạm vi của prompt hay một release không tự thành phạm vi Feature. Khi chưa có cây, đề xuất khung năng lực và ghi rõ là phương án; không tự sinh cả cây ngoài phạm vi được giao.
2. **Feature giữ năng lực nghiệp vụ có ranh giới tương đối ổn định.** Nêu người hưởng lợi, outcome tổng thể và in/out scope. Đối chiếu với các Feature ngang hàng về trách nhiệm, không ép bằng nhau về effort/số Epic. Không chọn cấp chỉ theo tên CRUD, màn hình, dòng estimation hoặc độ dài tài liệu. Quy ước của dự án có evidence được ưu tiên; khi chưa có, nêu giả định cấp độ thay vì tự coi đã chốt.
3. **Epic giữ phạm vi cần đặc tả và nghiệm thu chung.** Nêu outcome, model/rule/contract liên quan, trách nhiệm sở hữu và acceptance. Cùng entity/UI chưa đủ để gom; khác entry point, role hoặc kênh chưa đủ để tách. So với Epic lân cận để tránh phân bổ trùng và dependency bị che.
4. **Story chọn phần thay đổi bàn giao được.** Nêu actor/consumer, kết quả hữu ích, hành vi trong scope và cách quan sát, rồi xét sizing/dependency của team. Query/read-only là kết quả hợp lệ. Quyền, validation, lỗi và NFR bắt buộc đi cùng lát cắt. Một nhánh Use Case hoặc một màn hình chưa tự đủ lý do tách Story.
5. **Kiểm ba cấp có lặp cùng nghĩa không.** So nội dung, không chỉ tên: Feature bổ sung ranh giới năng lực/acceptance gì; Epic bổ sung phạm vi model/contract/nghiệm thu gì; Story chọn delta bàn giao nào? Nếu ba cấp chỉ đổi tên cùng một hành vi hoặc thêm tên màn hình/điều kiện quyền, ghi finding và đề xuất đặt lại vào cây hiện có. Không mở rộng scope hoặc bịa thêm con để hợp thức hóa cây.
6. **Cho phép quan hệ một–một có căn cứ.** Không bắt Feature có nhiều Epic hay Epic có nhiều Story. Khi một–một, giải thích vai trò riêng của hồ sơ cha, chẳng hạn phạm vi release hiện chỉ chọn một lát hoặc hợp đồng/baseline cần quản lý riêng. Kế thừa bằng ref, tránh chép ba bộ AC giống nhau. Chưa có căn cứ thì giữ candidate và nêu thông tin cần làm rõ; không tự bỏ tầng bắt buộc của dự án.

Ghi kết quả ngay trong F04/F06, E01/E15 hoặc Story manifest, tùy cấp đang sửa. Với nhóm mới/đổi ranh giới, cần có **cấp/parent được chọn → lý do chọn cấp → phần model/control/acceptance chung → delta bàn giao → căn cứ gom/tách và gap**. Chỉ cần giải thích phương án khác ở ranh giới còn tranh luận; không bắt thêm file, schema hoặc approval gate. Review kiểm nội dung rationale, không đánh dấu đạt vì đã điền cột.

Use Case là mô hình actor goal, trigger, pre/postconditions và main/alternate/exception flows ở E03 hoặc shared model được tham chiếu. Nó không là tầng giữa Epic và Story, không có quan hệ 1–1 bắt buộc với Epic/Story. Khi phân bổ một Use Case qua nhiều Story/Epic, chỉ rõ scenario/subset, nơi sở hữu model/control và kiểm kết quả tích hợp. Một hành trình xuyên Epic cần dependency/acceptance liên Epic; không nhân bản Use Case thành nhiều nguồn chuẩn.

### Phản ví dụ và ngoại lệ

`Feature: Tra cứu Customer → Epic: Tra cứu hồ sơ từ Customer List → Story: Tìm Customer trong phạm vi quyền` là **dấu hiệu cần review**, không phải lỗi có thể kết luận từ tên. Nếu cả ba chỉ mô tả cùng một truy vấn, điểm vào List và guard quyền không đủ chứng minh ba phạm vi khác nhau. Ưu tiên đặt Story vào Epic hồ sơ/tra cứu thuộc Feature quản lý Customer hiện có; chỉ đề xuất sửa, không tự rewrite baseline trong review.

Trong một dự án có Feature “Quản lý Customer và Contact”, Epic tra cứu riêng có thể hợp lý nếu query semantics, data scope, field visibility và nghiệm thu tạo thành phạm vi cần quản lý chung. Nếu chỉ là lookup đơn giản dùng trong quản lý hồ sơ, có thể đặt Story trong Epic hồ sơ. Preview/detail chỉ tách Story khi từng phần có giá trị và khả năng bàn giao riêng; nếu không giữ cùng lát cắt. Kiểm quyền vẫn đi cùng từng hành vi.

Ngược lại, sản phẩm có năng lực tìm kiếm nhiều nguồn, nhiều kiểu truy vấn và quản trị truy vấn có thể dùng Feature “Tìm kiếm thông tin khách hàng”. Phải chứng minh ranh giới năng lực và quan hệ với Feature khác. Không cấm tên “Tra cứu”, không bắt mọi CRM dùng Feature Customer–Contact, không lấy số Story/Epic làm ngưỡng đúng sai.

## Đọc đúng đơn vị nguồn

- Ghi source locator/revision, mục đích của danh sách và ý nghĩa đơn vị được đếm. Phân biệt số nguồn công bố với số đã tự đối soát; nếu chưa đọc được bảng đầy đủ thì nói rõ. Khi kiểm đếm, xét record logic, ID trùng/thiếu và dòng bảng lỗi; giữ witness thay vì âm thầm sửa nguồn.
- Phân loại phần nội dung cần tổ chức: năng lực/outcome, hành vi, màn hình/query, rule/control, integration hoặc technical enabler. Một dòng có thể chứa nhiều loại; không bắt ép một nhãn duy nhất cho cả dòng.
- Không chuyển mặc định một dòng/leaf thành một Epic, Story hoặc requirement chuẩn. Số dòng estimation chưa là effort bằng nhau, mẫu số tiến độ hay evidence baseline approval. Nhãn Must/Should giữ theo nguồn, chưa tự thành cam kết release.

## Thử ranh giới nhóm trước khi chốt allocation

Áp dụng [phân cấp CRM](backlog-hierarchy-and-decomposition.md) và [Feature F04–F07](feature-specification-catalog.md). Với mỗi nhóm đề xuất, người đọc cần hiểu outcome/actor, phần model/rule dùng chung, phạm vi nghiệm thu và dependency có người nhận hoặc gap. Số nhóm ít hơn hay tên đồng nhất hơn chưa chứng minh cách chia tốt hơn.

Với ranh giới còn có thể tranh luận, ghi lý do chọn và điều kiện sẽ làm thay đổi cách gom/tách. Không cần tạo nhiều phương án cho mọi nhóm đã rõ. Đặc biệt:

| Tình huống | Căn cứ cần xét |
|---|---|
| Import/export hoặc cùng màn hình/object | Cùng file, UI hay entity chưa đủ để gom Epic. Xét actor, model/control, error semantics, acceptance và khả năng baseline độc lập. |
| Lookup và mutation | Có thể cùng phạm vi hồ sơ, nhưng read contract, privacy và outcome truy vấn vẫn phải được phân bổ. Không gộp chỉ để giảm số Epic. |
| Integration hoặc chức năng xuyên Feature | Chỉ nhóm độc lập khi có consumer/outcome, contract và acceptance rõ. Giữ sender, receiver, failure/recovery và verification áp dụng; việc nhỏ có thể chỉ cần Task. |
| Lifecycle và side effect | Giữ kết quả nghiệp vụ và control bắt buộc trong lát cắt; không tách theo API/UI/DB/test để che dependency hoặc lỗi giữa các bước. |
| Feature/Epic so với DDD | Phân cấp phạm vi không tự xác lập Bounded Context, Aggregate hoặc architecture approval. Tham chiếu DDD đúng revision khi áp dụng. |

Ví dụ: import Contact có mapping, duplicate và lỗi theo dòng; export có filter, privacy và giới hạn volume. Chỉ ghi “đều xử lý file” thì chưa đủ căn cứ gom. Có thể giữ chung khi phạm vi dữ liệu/control và acceptance thực sự phù hợp; nếu cần owner/baseline riêng thì đề xuất tách và nêu lý do. Xem thêm [BA guide, chọn phạm vi Epic](ba-getting-started.md#walkthrough).

## Truy vết và giao thoa

Giữ mapping nhiều–nhiều từ source tới selected scope. Một dòng chứa nhiều trách nhiệm có thể được phân bổ bằng các fragment/locator cục bộ, giữ nguyên ID nguồn. Với từng phần giao thoa, ghi nơi sở hữu rule/command/read contract và nơi sử dụng nó; đánh dấu phần chưa có owner hoặc chưa được phân bổ.

Gán một owner chính cho mỗi dòng chỉ giúp đối soát inventory. Nó chưa chứng minh mọi fragment/control đã có nơi nhận hoặc không bị tính effort hai lần. Đi qua các giao điểm thực tế: entry point so với hành vi được mở, approval so với downstream integration, quyền dùng chung, activation và retry/partial failure. Giữ gap về contract trùng/chưa rõ, không tự chọn kết quả nghiệp vụ để khép bảng.

Khi gom/tách allocation đã có: giữ identity/ID cho cùng nghĩa, lập crosswalk và đối chiếu consumers/pins. Thay nghĩa sau baseline đi qua change control. Không sửa nguồn sản phẩm, DDD, backlog hay state ngoài quyền được giao.

## Evidence tối thiểu và kết luận

Ghi trong artifact/allocation hoặc review/report phù hợp với nhiệm vụ; không bắt thêm file hay schema mới. Evidence cần đủ để truy lại:

1. Source/revision, loại đơn vị và số công bố/đã đối soát nếu báo số.
2. Ranh giới nhóm và rationale, gồm điểm còn có thể thay đổi.
3. Mapping, phần dùng chung, gaps/unallocated và trách nhiệm chưa được nhận.
4. Phạm vi đã kiểm, revision, tác giả/reviewer thực tế và quyết định/approval còn thiếu.

Phân biệt **đếm đúng nguồn**, **đã đề xuất allocation**, **đã review cách phân rã**, **authority đã chốt**. Chưa có evidence thì ghi Chưa kiểm đúng phần; có overlap/control gap thì ghi finding theo [review protocol](requirements-review-process-and-verdicts.md). Đủ mapping hoặc lint PASS chưa xác nhận semantic coverage hay DoR.

Khi báo status, có thể nói “nguồn công bố N dòng estimation; cách phân rã chưa được review”. Chỉ dùng coverage trên đơn vị đã định nghĩa, có phạm vi và evidence phù hợp; không gọi tỷ lệ số dòng thành tỷ lệ sản phẩm hoàn thành. Route correction về crm-define-feature, crm-specify-epic hoặc crm-prepare-stories theo cấp bị ảnh hưởng, thay vì sửa allocation trong lượt report/check.
