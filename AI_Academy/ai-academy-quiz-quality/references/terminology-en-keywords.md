# Terminology: English keywords (TERM-EN-01)

Reference glossary for rule TERM-EN-01 in [quiz-authoring-and-review.md](quiz-authoring-and-review.md) and [review-gates.md](review-gates.md). Left column: Vietnamese wording found in lessons or proposed as a first-use gloss. Middle column: the English keyword to use in theory, stems, options, and explanations.

## How to use

- Use the English keyword. An optional short Vietnamese gloss may follow it once per independent reading unit (theory page; each quiz item, because runtime samples items randomly): `specification (đặc tả)`.
- Prefer the ISTQB Glossary / CTFL v4.0.1 form for testing terms and GS1 for supply-chain identifiers; otherwise record the finding as "TERM-EN-01, no authority source".
- Never write "nghiệp vụ" alone; pick `business rule`, `business requirement`, `domain`, `business stakeholder`, `domain expert`, or `Business Analyst (BA)`.
- Where a cell lists alternatives (`a / b`), choose one per track and use it consistently.
- Extend this file per track (e.g. DDD, HCD, AI) as lessons are reviewed; keep grouping by domain, not by lesson.

Seeded from the Testing track (16 lessons, 2026-10). Additional tracks append their own domain groups.

## Business, domain and roles

| Vietnamese wording | English keyword | Note |
|---|---|---|
| nghiệp vụ / quy tắc nghiệp vụ | business rule / business requirement / domain | phải chọn cụ thể |
| người dùng cuối | end user |  |
| bên liên quan | stakeholder |  |
| nhu cầu nghiệp vụ / nhu cầu người dùng | stakeholder needs / user needs | không dùng "nghiệp vụ" đứng một mình |
| người dùng nghiệp vụ | business stakeholder / end user | chọn theo vai trò thật |
| bug nghiệp vụ | missing/incorrect business rule |  |
| rủi ro nghiệp vụ | business risk / product risk |  |
| hiểu biết nghiệp vụ | domain knowledge |  |
| người có quyền phê duyệt | approval authority / authorized stakeholder |  |
| người ra quyết định | decision maker |  |
| ngữ cảnh domain | domain context |  |

## Warehouse / logistics domain (GS1 where applicable)

| Vietnamese wording | English keyword | Note |
|---|---|---|
| người vận hành kho, người quản lý vận hành kho | warehouse operator / Warehouse Manager |  |
| số lượng đặt hàng tối thiểu | MOQ (minimum order quantity) |  |
| số lô, lô hàng | batch/lot | GS1 |
| mã vạch | barcode (GTIN) | GS1 |
| cam kết dịch vụ | SLA |  |
| bảo hành / chế tài | warranty / penalty |  |
| hạn dùng | expiry date | GS1 "expiration date"; dùng một tên thống nhất |
| lấy hàng trong kho | picking |  |
| hàng giữ chỗ | reserved stock |  |
| đồng bộ tồn kho | inventory synchronization |  |
| giữ chỗ tồn kho | inventory reservation |  |
| bán vượt tồn | overselling |  |
| chênh lệch tồn kho | inventory discrepancy |  |
| độ dự phòng trong lịch | schedule slack |  |
| kiểm kê | stocktaking / inventory count |  |
| đối soát | reconciliation |  |
| xuất kho | outbound processing / goods issue |  |
| số tồn / lượng tồn hiện có | on-hand inventory quantity |  |
| báo cáo kiểm kê | inventory count report |  |
| phiếu xuất hàng | goods issue document |  |
| đơn vị lưu kho | stock keeping unit (SKU) |  |
| nhập kho | inbound receiving / goods receipt |  |
| dòng tồn kho | inventory record |  |
| tồn kho âm | negative inventory |  |
| hàng mùa vụ | seasonal item |  |
| hàng dễ vỡ | fragile item |  |
| loại/ký pháp barcode | barcode symbology |  |
| bộ phân tích barcode | barcode parser |  |
| chữ số kiểm tra | check digit |  |
| tải dữ liệu QR | QR payload |  |

## Defects and failures

| Vietnamese wording | English keyword | Note |
|---|---|---|
| khiếm khuyết, sai sót | defect | ISTQB (error/defect/failure) |
| ngụy biện vắng bóng lỗi | absence-of-defects fallacy | ISTQB principle 7 |
| nguyên lý tập trung lỗi | defect clustering | ISTQB principle 4 |
| gỡ lỗi, công cụ gỡ lỗi | debugging, debugger | CTFL §1.1.2 |
| phiếu lỗi, phiếu báo cáo khiếm khuyết | defect report | CTFL §5.5 |
| vòng đời khiếm khuyết | defect lifecycle / defect management |  |
| sự sai lệch, điểm bất thường | anomaly (chưa phân loại) / failure (hành vi sai quan sát được) |  |
| lỗi do con người | error | error → defect → failure |
| ngoại lệ hệ thống | exception (system exception) |  |
| lỗi do yêu cầu bị bỏ sót | defect of omission |  |
| che giấu defect | defect masking |  |
| tỷ lệ phát hiện defect | defect discovery rate |  |
| mức độ nghiêm trọng / mức độ ảnh hưởng | severity |  |
| mức độ ưu tiên sửa | priority / fix priority |  |
| cách làm tạm / cách vòng | workaround |  |
| trạng thái defect | defect status |  |
| phân loại defect | defect classification |  |
| người đang xử lý phiếu | defect owner / current owner |  |
| bản sửa | fix |  |
| ma trận quyền | permission matrix / access-control matrix |  |
| buổi phân loại defect | defect triage meeting |  |
| tóm tắt defect | Defect Summary |  |
| xu hướng defect | defect trend |  |
| tốc độ sửa defect | defect fix rate |  |
| tỷ lệ defect lọt production | escaped-defect ratio / defect escape rate |  |
| tỷ lệ phát hiện defect trước release | defect detection percentage |  |
| mật độ defect | defect density |  |
| lỗi cú pháp | syntax error |  |
| lỗi/fail giả do test | flaky failure |  |
| sở hữu chất lượng | quality ownership |  |
| defect do khách hàng báo | customer-reported defect |  |
| người nhận việc sửa | action owner |  |
| lỗi lọt sau release | escaped defect |  |
| tỷ lệ defect thoát ra production | defect escape rate |  |
| tỷ lệ phát hiện defect | defect detection percentage (DDP) |  |
| nhóm release/defect cùng nguồn | release cohort / defect cohort |  |
| tuổi defect critical đang mở | open critical-defect age |  |

## Test techniques and exploratory testing

| Vietnamese wording | English keyword | Note |
|---|---|---|
| độ bao phủ mã nguồn | code coverage | ISTQB coverage |
| giá trị biên | boundary value | ISTQB |
| phân vùng tương đương | equivalence partitioning |  |
| phân tích giá trị biên | boundary value analysis |  |
| kiểm thử khám phá | exploratory testing |  |
| kỹ thuật kiểm thử hộp đen | black-box test technique |  |
| kỹ thuật kiểm thử hộp trắng | white-box test technique |  |
| độ bao phủ nhánh | branch coverage |  |
| độ bao phủ câu lệnh | statement coverage |  |
| phần tử bao phủ | coverage item |  |
| phân vùng tương đương hợp lệ | valid equivalence partition |  |
| phân vùng tương đương không hợp lệ | invalid equivalence partition |  |
| phân vùng kề | adjacent partition |  |
| giá trị kế cận gần nhất | closest neighbor |  |
| dữ liệu rời rạc/danh mục | discrete data / enumeration |  |
| kỹ thuật bảng quyết định | decision table testing |  |
| bảng quyết định | decision table |  |
| bảng quyết định đầy đủ | full decision table |  |
| quy tắc trong bảng quyết định | decision rule |  |
| tổ hợp khả thi | feasible combination |  |
| tổ hợp bất khả thi | infeasible combination |  |
| ký hiệu điều kiện không ảnh hưởng | don’t care (`-`) |  |
| rút gọn bảng quyết định | decision table minimization |  |
| kiểm thử chuyển đổi trạng thái | state transition testing |  |
| biểu đồ trạng thái | state diagram |  |
| bảng trạng thái | state table |  |
| trạng thái nguồn | source state |  |
| trạng thái đích | target state |  |
| sự kiện kích hoạt | event |  |
| điều kiện bảo vệ | guard condition |  |
| chuyển đổi hợp lệ/bất hợp lệ | valid/invalid transition |  |
| đường chuyển đổi hợp lệ | valid transition path |  |
| bao phủ tất cả trạng thái | all states coverage |  |
| bao phủ chuyển đổi hợp lệ | valid transitions coverage |  |
| bao phủ toàn bộ chuyển đổi | all transitions coverage |  |
| bao phủ chuỗi N chuyển đổi | N-switch coverage |  |
| phiên kiểm thử có quản lý | session-based testing session |  |
| tờ mục tiêu kiểm thử | test charter |  |
| biên bản phiên | session sheet |  |
| ghi chú phiên | session notes |  |
| họp tổng kết phiên | debrief / debriefing |  |
| điều tra và báo cáo defect | bug investigation and reporting |  |
| chuẩn bị phiên | session setup |  |
| khám phá ngoài charter | opportunity testing / off-charter testing |  |
| chỉ số phân bổ Test–Bug–Setup | TBS metrics |  |
| kỹ thuật dựa trên kinh nghiệm | experience-based test technique |  |
| tour kiểm thử | test tour |  |
| tour khu vực ít dùng | Back Alley Tour |  |
| thao tác sai thứ tự | Wrong Turn |  |
| tour hành vi trái thông thường | Antisocial Tour |  |
| khả năng tái hiện | reproducibility |  |

## Reviews and shift-left

| Vietnamese wording | English keyword | Note |
|---|---|---|
| kiểm thử dịch trái / kiểm thử sớm | shift-left testing |  |
| khả năng kiểm thử | testability |  |
| đánh giá khả năng kiểm thử yêu cầu | requirements testability review |  |
| review không chính thức | informal review |  |
| review có author dẫn | walkthrough |  |
| review kỹ thuật | technical review |  |
| thanh tra chính thức | inspection |  |
| người dẫn review | review leader |  |
| người điều phối review | moderator / facilitator |  |
| người ghi biên bản review | scribe / recorder |  |
| chỉ số review | review metrics |  |
| review mã | code review |  |

## Risk

| Vietnamese wording | English keyword | Note |
|---|---|---|
| rủi ro | risk |  |
| khả năng xảy ra rủi ro | risk likelihood |  |
| tác động/hậu quả của rủi ro | risk impact |  |
| mức độ rủi ro | risk level |  |
| ma trận rủi ro | risk matrix |  |
| rủi ro sản phẩm | product risk |  |
| rủi ro dự án | project risk |  |
| rủi ro tồn dư | residual risk |  |
| phân tích rủi ro sản phẩm | product risk analysis |  |
| nhận diện rủi ro | risk identification |  |
| đánh giá rủi ro | risk assessment |  |
| kiểm soát rủi ro | risk control |  |
| giảm thiểu rủi ro | risk mitigation |  |
| giám sát rủi ro | risk monitoring |  |
| chấp nhận rủi ro | risk acceptance |  |
| chuyển giao rủi ro | risk transfer |  |
| kế hoạch dự phòng | contingency plan |  |
| chấp nhận rủi ro tồn dư | residual-risk acceptance |  |

## Planning, reporting, metrics and quality culture

| Vietnamese wording | English keyword | Note |
|---|---|---|
| tiêu chí chấp nhận / tiêu chí nghiệm thu | acceptance criteria | ISTQB glossary; dùng một tên duy nhất |
| kiểm thử tích hợp | integration testing | ISTQB |
| báo cáo kiểm thử | test report | ISTQB |
| họp hồi tưởng | retrospective |  |
| nguyên nhân gốc rễ | root cause analysis (RCA) |  |
| lưu trữ ngoại tuyến | offline storage |  |
| môi trường vận hành (theo nghĩa sử dụng thật) | operational environment | dùng `production` khi nói môi trường triển khai |
| chiến lược test | test strategy |  |
| tích hợp liên tục | continuous integration (CI) |  |
| báo cáo hoàn tất testing | test completion report |  |
| phạm vi testing | test scope |  |
| bản kế hoạch testing | Test Plan |  |
| cửa bắt đầu | entry criteria |  |
| cửa kết thúc | exit criteria / test completion criteria |  |
| phạm vi trong/ngoài | in-scope / out-of-scope |  |
| giả định | assumption |  |
| ràng buộc | constraint |  |
| phụ thuộc | dependency |  |
| đường găng | critical path |  |
| mốc | milestone |  |
| suất người | staffing allocation / test resource allocation |  |
| quyết định phát hành | release decision |  |
| báo cáo tiến độ testing | test progress report |  |
| báo cáo trạng thái testing | test status report |  |
| tóm tắt điều hành | Executive Summary |  |
| tóm tắt thực thi test | Test Execution Summary |  |
| tỷ lệ thực thi test | test execution rate |  |
| tỷ lệ pass | pass rate |  |
| tỷ lệ fail | fail rate |  |
| chu kỳ testing | test cycle |  |
| khoảng thời gian quan sát | observation window |  |
| độ bão hòa testing | test saturation |  |
| văn hóa chất lượng | quality culture |  |
| cách tiếp cận cả nhóm | whole team approach |  |
| ủy thác chất lượng | quality delegation |  |
| hậu kiểm không đổ lỗi | blameless postmortem |  |
| kỹ thuật năm câu hỏi tại sao | 5 Whys |  |
| định luật Goodhart | Goodhart’s Law |  |
| Định nghĩa Sẵn sàng | Definition of Ready |  |
| Định nghĩa Hoàn thành | Definition of Done |  |
| cửa chất lượng | quality gate |  |
| tiêu chí hoàn tất testing | test completion criterion |  |
| việc làm sau postmortem | postmortem action item |  |
| mẫu số của metric | metric denominator |  |
| chỉ báo sớm | leading indicator |  |
| chỉ báo muộn | lagging indicator |  |
| chỉ số phù phiếm | vanity metric |  |
| chỉ số dẫn đến hành động | actionable metric |  |
| thao túng/tối ưu sai metric | metric gaming |  |
| thời gian phục hồi của một incident | time to restore |  |
| thời gian phục hồi trung bình | mean time to restore (MTTR) |  |
| ngưỡng metric | metric threshold |  |
| mục tiêu metric | metric target |  |
| chỉ dẫn không ràng buộc | guideline |  |
| điều kiện thoát | exit criterion |  |
| sự cố production | production incident |  |
| code do AI sinh | AI-generated code |  |
| test do AI sinh | AI-generated test |  |
| implementation được sinh | generated implementation |  |
| quyền quyết định chất lượng | quality decision authority |  |

## Testing fundamentals, levels and types; software engineering

| Vietnamese wording | English keyword | Note |
|---|---|---|
| đặc tả, bản đặc tả | specification | ISTQB glossary |
| kiểm thử | testing / test |  |
| kiểm thử hồi quy | regression testing | ISTQB |
| kiểm thử đơn vị | unit testing (component testing) | ISTQB dùng component testing |
| kiểm thử hệ thống | system testing | ISTQB |
| kiểm thử tự động | test automation / automated tests |  |
| kịch bản kiểm thử, ca kiểm tra | test case / test scenario |  |
| bộ kiểm thử | test suite | ISTQB |
| bản dựng | build |  |
| bản phát hành, phát hành | release |  |
| môi trường vận hành thực tế | production |  |
| mã nguồn, mã lệnh | source code / code |  |
| lập trình viên | developer |  |
| nghịch lý thuốc trừ sâu | pesticide paradox ("tests wear out" trong CTFL v4) |  |
| kiểm thử toàn diện | exhaustive testing | ISTQB principle 2 |
| tái cấu trúc | refactoring |  |
| giám sát vận hành | monitoring |  |
| Thẩm tra / Thẩm định | Verification / Validation | CTFL §1.1; mnemonic "build the thing right / right thing" chỉ là mnemonic |
| kiểm thử xác nhận | confirmation testing | CTFL §2.2.3 |
| kiểm thử tĩnh / động | static testing / dynamic testing | CTFL §1.1, Ch.3 |
| phân tích tĩnh | static analysis |  |
| thử nghiệm cảm tính, thử ngẫu nhiên | ad hoc testing | trung tính, không hạ thành "không phải testing" |
| kết quả kỳ vọng / kết quả thực tế | expected result / actual result |  |
| đối tượng kiểm thử | test object |  |
| cơ sở kiểm thử | test basis |  |
| thực thi kiểm thử | test execution |  |
| môi trường kiểm thử | test environment |  |
| phân tích phạm vi mã thay đổi / tác động | impact analysis | CTFL §2.2.3 |
| tính độc lập (khách quan) của kiểm thử | independence of testing | CTFL FL-1.5.3 |
| sản phẩm công việc | work product |  |
| tài liệu đặc tả chức năng | functional specification (FSD) |  |
| đặc tả yêu cầu | requirements specification |  |
| kiểm thử chấp nhận / nghiệm thu | acceptance testing |  |
| test bị hao mòn/mất dần hiệu quả | tests wear out |  |
| ưu tiên test case | test case prioritization |  |
| dữ liệu test | test data |  |
| cơ chế xác định expected result | test oracle |  |
| bài toán xác định expected result | oracle problem |  |
| công sức test | test effort |  |
| sản phẩm phục vụ testing | testware |  |
| môi trường tiền production | staging environment |  |
| kiểm thử khả dụng | usability testing |  |
| kiểm thử hiệu năng | performance testing |  |
| kiểm thử bảo mật | security testing |  |
| kiểm thử tải | load testing |  |
| kiểm thử tuân thủ quy định | regulatory compliance testing |  |
| kiểm thử chức năng | functional testing |  |
| kiểm thử phi chức năng | non-functional testing |  |
| hành vi được đặc tả | specified behavior |  |
| cấu trúc nội bộ | internal structure |  |
| độ phân giải cảm biến | sensor resolution |  |
| tính dư thừa của bộ test | test-suite redundancy |  |
| lỗ hổng đặc tả | specification gap |  |
| mâu thuẫn yêu cầu | requirements contradiction |  |
| thiết kế và thực thi test | test design and execution |  |
| test condition | test condition |  |
| dữ liệu ban đầu cho test | seed data |  |
| chiều sâu testing | test thoroughness |  |
| khả năng/năng lực testing còn lại | remaining test capacity |  |
| hạng mục/phiên bản được test | test item |  |
| mục tiêu testing | test objective |  |
| nhánh cá nhân | development branch |  |
| chuỗi Unicode | Unicode string |  |
| trạng thái bị chặn | Blocked |  |
| chưa thực thi | Not Run |  |
| điều kiện test hiện tại | test conditions |  |
| tranh chấp truy cập đồng thời | race condition |  |
| giàn chạy test | test harness |  |
| kiểm thử chấp nhận người dùng | user acceptance testing (UAT) |  |
| hành trình người dùng | user journey |  |
| đường người dùng quan trọng | critical user journey |  |
| kiểm tra kiểu | type checking |  |
| kiểu dữ liệu | data type |  |
| cổng build | build gate |  |
| trang trí giao diện | UI cosmetics |  |
| ánh xạ sai trường | incorrect field mapping |  |
| đường chạy thuận lợi | happy path |  |
| câu lệnh kiểm tra kết quả | assertion |  |
| trường hợp biên | edge case |  |
| thời gian phục hồi sau failed deployment | failed deployment recovery time |  |
| test oracle độc lập | independent test oracle |  |
| giám sát của con người | human oversight |  |
| bằng chứng truy vết | traceability evidence |  |
