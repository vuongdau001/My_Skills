# Đánh giá mức hoàn thiện phân tích và lệnh score

ID: CRM-SCORING · CRM Workflow Kit 1.9.0 · 05/11/2026

Đọc khi hỏi “Story này được bao nhiêu điểm?”, “E07 rõ tới đâu?”, “Epic nào còn thiếu?” hoặc cần tổng hợp mức hoàn thiện requirements đã nhận diện. Dùng crm-review-specification để chuẩn bị assessment; crm-report-status để tổng hợp. Đây là helper CLI, không thêm workflow hay slash command. [Template](../assets/templates/definition-assessment-template.md).

## Mô hình và ý nghĩa

Ba lớp: catalog coverage (có nội dung), definition maturity (đặc tả/xác nhận tới đâu), gate (được chuyển bước chưa). Không dùng điểm để thay review verdict, approval, baseline, DoR hoặc runtime acceptance. Q01–Q07 giữ verdict riêng; không lấy trung bình để bù sai nghiệp vụ bằng đủ links.

| Mức | Rubric | Evidence |
|---|---|---|
| 0 | Hạng mục áp dụng nhưng chưa có nội dung thực chất | present=false; rationale chỉ rõ thiếu gì; target được pin |
| 1 | Đã nhận diện/có draft, còn gap ảnh hưởng nghĩa/coverage | present=true; nội dung/source/model refs; rationale và blockers |
| 2 | Đặc tả đủ cho selected scope và bước đang xét, đã tự kiểm; chưa đủ review xác nhận | Evidence có locator; không còn content blocker đã khai báo; self-check không tự lên 3 |
| 3 | Reviewer chuyên môn/độc lập đã xác nhận các checks áp dụng đúng revision | Review mode, reviewer, pinned evidence; Q01–Q07 disposition Đạt hoặc N/A có rationale |

Unknown dùng level=null, không đổi thành 0. Applicability là applies/na/unknown. N/A chỉ cho hạng mục Epic có điều kiện E04/E08/E09/E11/E12, với rationale, reviewer và evidence xác nhận. Không đánh N/A toàn mục bắt buộc, toàn mục Feature/Story hay canonical requirement; nội dung kế thừa vẫn là applies và dẫn ref/delta. Đây là lựa chọn bảo thủ được giữ từ policy v1 sang v2. Applicability Unknown chưa được chốt thì chỉ số tổng thể null, không lặng lẽ bỏ khỏi mẫu số.

Mức 2/3 không cho phép blocker category=content. Approval hoặc delivery blocker có thể tồn tại dù nội dung đã rõ; vẫn báo gate=blocked. Không có blocker chỉ cho gate=not_assessed, tuyệt đối không tự Ready. Reviewer/authority là khai báo cần kiểm chứng qua workflow; helper chỉ kiểm byte/hash, không xác thực người ký hoặc tính đúng của lời khai.

## Cách tính và các đơn vị

Policy cố định crm-definition-v2, equal weights: D=100×sum(level)/(3×N), N là số đơn vị applies. Với level Unknown: cận dưới đóng góp 0, cận trên đóng góp 3. Đây là khoảng điểm trên inventory đã biết, không phải khoảng tin cậy thống kê hay % requirement đúng/effort/value. N=0 cho null, không 100%. Báo thêm assessed/N, confirmed/N, presence, N/A, Unknown, blockers và scope revision.

Epic dùng đủ E01–E16, Story đủ S01–S12, Feature đủ F01–F08. Không được xóa dòng chưa rõ; dùng Unknown. --item chỉ lọc kết quả sau validation toàn assessment. Mỗi hạng mục có mức dựa vào rubric và các Q áp dụng, không bắt tạo 16×7 file riêng.

Khi review canonical requirement, chọn parent Feature/Epic/Story làm workflow target và ID requirement làm focused scope; không thêm supported target hoặc function mới. Helper score riêng nhận kind Requirement.

Canonical Requirement dùng một item definition cho REQ/BR/MOD ID đã khai báo ở metadata artifact_id hoặc defined_ids. Không lấy trung bình bảy Q; một content gap làm cả definition chưa đạt mức 2. Một file chứa nhiều requirement phải khai báo từng ID; evidence locator chỉ đúng nội dung đang chấm.

Rollup catalog_obligations cộng các nghĩa vụ catalog theo target/scope, không là số requirements hoặc % dự án hoàn thành. Rollup canonical_requirements chỉ dùng inventory REQ/BR/MOD riêng, mỗi ID một lần dù nhiều Story sử dụng. Hai ledger không cộng vào nhau. Không lấy trung bình điểm Epic khác kích thước; số tổng catalog là chỉ số các obligations trong inventory, không là effort/value. Cross-Epic/shared-control gaps phải có assessment/blocker riêng, không suy từ điểm từng file.

Inventory revision/scope/complete là khai báo phạm vi đã chọn, không chứng minh đã discovery toàn dự án. Không tự tìm mọi requirement trong prose. Nếu inventory chưa đủ, ghi complete=false và trình bày rõ phần chưa nhận diện/phân bổ; complete=true cũng không được helper chứng nhận. So hai kỳ phải giữ policy, unit/granularity và giải thích scope added/removed/split/merged; không so hai điểm khi mẫu số khác mà thiếu scope delta. V1 chưa tự tính trend/delta.

## Schema tối thiểu và chống stale

Root JSON: schema_version=1, policy, workstream, snapshot ISO có timezone, inventory={revision,scope,complete}, targets=[...]. Target: id, kind, path, revision, sha256, scope, items. Mỗi item: id, applicability, present (true/false/null), level (0..3/null), rationale, evidence, blockers; tùy mức thêm review/na_confirmation. References đều là repo-relative POSIX, không phải relative từ assessment. Evidence cần path/revision/sha256/locator; file phải tồn tại trong repo và hash hiện hành khớp. Không fetch URL. Target phải ở spec_root và ID được định nghĩa đúng artifact. Revision metadata nếu có phải khớp; nếu legacy không có thì revision chỉ là nhãn người đánh giá khai báo, SHA pin bytes hiện tại.

Khi nội dung nguồn, target hoặc review evidence đổi, helper từ chối tính bằng pin cũ: reassess phần bị ảnh hưởng, tạo snapshot mới và giữ record cũ như lịch sử. Không refresh hash mù để giữ điểm. Duplicate target+scope, mixed revisions cùng ID và canonical requirement lặp bị từ chối. Scope khác nhau của cùng Epic là nghĩa vụ review khác nhau; không gọi là requirement mới.

Blockers: [{id,reason,category}], category content/approval/delivery. Cùng blocker dùng chung giữ ID ổn định; report đếm unique ID. Evidence/reference có thể pin source/read-only, nhưng không được sửa nguồn để tạo điểm. Review/check chỉ ghi record đánh giá, không sửa target.

## Lệnh dùng thực tế

Gọi từ repo root, chọn paths từ config; ví dụ dưới giả định workstream p3 có layout legacy. Từ source kit thay prefix bằng scripts/kit.py và --repo bằng repo đích. Helper mặc định in stdout; --output chỉ lưu báo cáo Markdown mới theo quy tắc bên dưới.

Tạo inventory Unknown đủ 12 mục cho một Story (thay ID/path/revision/scope thật):

```sh
python3 .agents/skills/crm-spec-kit/scripts/kit.py score --repo . --workstream p3 --init --artifact phase-3/spec/stories/STORY-CRM-001-customer-list.md --target STORY-CRM-001 --kind Story --revision p3-pilot-r1 --scope customer-list > phase-3/spec/reports/story-001-assessment.json
```

Shell redirection là thao tác ghi riêng trong vùng được giao; chọn tên file mới, không ghi đè record cũ. Skeleton chỉ pin target và để Unknown, không chấm bằng số heading. Agent/BA đọc source/catalog/model/Q, ghi rationale/evidence/levels có căn cứ. Gom nhiều skeleton bằng cách ghép targets vào một root inventory thống nhất; mỗi ID/scope/revision theo schema trên. Để chấm từng Epic, tạo tương tự --kind Epic và đúng ID/path.

```sh
# Một Story
python3 .agents/skills/crm-spec-kit/scripts/kit.py score --repo . --workstream p3 --assessment phase-3/spec/reports/assessment.json --target STORY-CRM-001 --format markdown
# Một Epic
python3 .agents/skills/crm-spec-kit/scripts/kit.py score --repo . --workstream p3 --assessment phase-3/spec/reports/assessment.json --target EPIC-CRM-001
# Một mục trong scope của Epic
python3 .agents/skills/crm-spec-kit/scripts/kit.py score --repo . --workstream p3 --assessment phase-3/spec/reports/assessment.json --target EPIC-CRM-001 --scope manual --item E07
# Toàn inventory, hai ledger tách riêng
python3 .agents/skills/crm-spec-kit/scripts/kit.py score --repo . --workstream p3 --assessment phase-3/spec/reports/assessment.json
```

--target không kèm --scope trả tất cả scopes của ID đó. --item cần --target; focused result không là full artifact score. Nếu một assessment chứa nhiều target, tất cả pins/catalog được kiểm kể cả khi chỉ lọc một target; muốn snapshot độc lập dùng assessment riêng. JSON là mặc định; --format markdown giúp đọc. Exit 0 nghĩa tính hợp lệ, không là Ready/PASS nghiệp vụ; exit 2 là input/pin không hợp lệ.

## Ví dụ diễn giải và vận hành

Ví dụ giả định: 14 hạng mục Epic applies, 2 N/A xác nhận; 8 mức 3, 3 mức 2, 2 mức 1, 1 Unknown → D=76,19–83,33, assessed=13/14, confirmed=8/14. Hai blocker quyền/failure vẫn chặn gate. Có đủ 14 section không chứng minh 14 hạng mục rõ.

AI có thể đề xuất mức 0–2 từ evidence và findings. Chỉ ghi mức 3 khi thực sự có review record đáp ứng rubric; đổi profile không thành specialist/independent approval. Mỗi lần sửa target cần assessment revision mới. Kết quả scoring bổ sung cho review record, không đổi schema metadata hay status Jira và không sửa sprint/state.

Trước dùng để đặt ngưỡng, pilot BA/Dev/QA chấm cùng một mẫu, so mức lệch, sửa rubric và đóng băng scoring policy. V1 không có custom weights, ngưỡng Ready, trend engine hay NLP tự phán semantics.

## Nguồn và tailoring

[INCOSE GtWR v4](https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf) và [IIBA quality criteria](https://www.iiba.org/contentassets/1dc6a35dff8c46ff85c6cb6b916b7ea3/9-quality-criteria-for-requirements.pdf) làm nền chất lượng; [CII PDRI](https://www.construction-institute.org/pdri-overview) gợi ý cách lượng hóa scope definition; [QUS](https://link.springer.com/article/10.1007/s00766-016-0250-x) tham khảo chất lượng Story. Thang 0–3, công thức, policy, schema và hành vi CLI là tailoring CRM, không phải chuẩn chấm điểm do các tổ chức trên chứng nhận. Trọng số/ngưỡng PDRI xây dựng không được bê sang CRM.

## Dependency integration và báo cáo Markdown — 1.9

Policy hiện hành crm-definition-v2 (schema JSON vẫn 1) tái dùng lint readiness record graph cho từng target; mọi ASM/DEC/CST trong closure được pin ở record_dependencies bằng id/kind/state/revision/path/sha256/unresolved. --init lấy snapshot thực rồi thêm items=null. Meeting không bị biến thành nghĩa vụ approval. Policy v1 bị từ chối khi tính: tạo skeleton v2, đối chiếu scope/pins và reassess, không chỉ đổi tên policy hoặc copy điểm cũ.

Mỗi record dependency có thể khai items là danh sách E/S/F IDs hoặc definition, kèm allocation={rationale,reviewer,evidence}. Mapping này cần người đánh giá xem nội dung, helper không suy từ scope bằng chữ. Evidence allocation cũng cần path/revision/hash/locator. N/A không được dùng cho mục đang chịu unresolved dependency. Record đã resolve không bắt mapping để cap, nhưng vẫn phải pin để thay đổi state/statement/source không lặng lẽ giữ điểm.

ASM không Validated, DEC không Approved hoặc CST không Confirmed trong closure tạo blocker content tự động. Điểm đề xuất 2/3 của mục đã map bị cap xuống effective=1; điểm 0/1 không được tăng, Unknown giữ Unknown. Tool giữ declared_level và score_adjustments để giải thích, không sửa assessment nguồn. Focus vào mục khác vẫn có thể có điểm cao nhưng target dependency gate vẫn blocked. Không trừ điểm cố định theo số assumptions.

Unresolved record chưa map ảnh hưởng (items=null) làm effective levels Unknown và suppress chỉ số của target/ledger, thay vì đoán hạ mọi mục hoặc cho điểm đầy đủ. BA phải phân bổ ảnh hưởng với rationale/evidence. Không được bỏ record khỏi snapshot: thay closure, state, revision, nội dung hoặc evidence stale đều cần regenerate/reassess; không refresh hash mù. Dependency audit có lỗi structural/evidence khác record-obligation thì dừng tính để xử lý lint. Cùng record trong register thay byte cũng invalidate pin; giữ lịch sử cũ.

Đây là conservative policy cho dependency còn unresolved. Dù chỉ chờ ký một DEC, tool không đoán đã có authority cho nghĩa; muốn tách approval-only khỏi content cần review/policy riêng, không đổi state để né cap. Các blocker approval/delivery độc lập ở assessment vẫn được giữ riêng như trước. Tool chỉ biết typed links đã khai, không thấy mọi assumption/question trong prose. Đọc và ghi blocker thủ công cho queue cũ/thiếu allocation.

Báo cáo Markdown gồm bảng tổng hợp từng artifact/scope, điểm đề xuất và điểm sau dependency check, bảng từng item, rationale, evidence pins, automatic adjustments, unresolved records, blockers và next actions. Điểm đề xuất không là điểm được công nhận. Báo cáo focused không thành full artifact score. Phần explain không tự tạo Business decision hoặc reviewer authority.

```sh
python3 .agents/skills/crm-spec-kit/scripts/kit.py score --repo . --workstream p3 --assessment phase-3/spec/reports/assessment-v2.json --format markdown --output phase-3/spec/reports/definition-score-2026-11-05.md
```

Không --output thì chỉ stdout như trước. Có --output chỉ ghi file .md mới bên trong reports theo config, không ghi đè file có sẵn, không sửa spec/assessment. Chọn filename snapshot mới khi chạy lại; --output chỉ dùng --format markdown, không dùng --init. Report được helper lưu với metadata Report schema 1, reference tới assessment và review_verdict Chưa kiểm; có thể ghi assessment_context để hiện rõ self-check/người thực hiện, không tự thành independent review hoặc approval. Không viết thêm vào target đang chấm. Đây là cập nhật record đánh giá, không là task/sprint event.
