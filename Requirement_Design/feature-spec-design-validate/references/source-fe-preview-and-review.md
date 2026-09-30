# Source FE preview and review

Đọc tài liệu này trước khi sửa source FE hoặc kết luận verdict. Áp dụng theo stack và conventions của repository; không thay chúng bằng một preview framework riêng.

## 1. Ghi baseline và phạm vi

Trước khi sửa, ghi trong `REVIEW.md` hoặc working notes:

- input documents, revision hoặc thời điểm đọc;
- baseline commit và branch/workspace hiện tại;
- trạng thái working tree liên quan;
- package/app chứa FE cần sửa và lệnh kiểm tra có sẵn;
- scenario, acceptance và viewport/state nằm trong phạm vi;
- active assumption, blocker và phần chưa xác minh.

Nếu working tree có thay đổi sẵn, phân biệt chúng với thay đổi preview. Không overwrite, discard hoặc đổi checkout chứa công việc của người khác.

## 2. Kiểm tra input trước khi code

Theo trace `goal → rule/requirement → scenario → UX Flow → acceptance`. Mỗi behavior quan trọng phải có nguồn hoặc assumption/decision rõ. Ghi finding nếu gặp:

- requirement và UX Flow mô tả outcome khác nhau;
- acceptance không testable hoặc thiếu precondition;
- permission, lifecycle, failure hay recovery chưa xác định;
- UI đòi dữ liệu/action không tồn tại trong contract dự kiến;
- FE baseline đang biểu diễn luật khác với desired behavior.

Không dùng preview để âm thầm quyết định một contradiction blocking. Có thể tiếp tục các flow không phụ thuộc finding đó.

## 3. Detailed UX record

Trong `UX_DESIGN.md`, mô tả theo screen hoặc state phù hợp với sản phẩm:

```markdown
### <Screen/State ID> — <tên>
- Links: <REQ/BR/SCN/AC/DEC/ASM>
- Entry/preconditions: <điểm vào, actor, permission, state>
- Responsibility: <điều màn hình phải giúp user hiểu hoặc làm>
- Data and visibility: <dữ liệu, status, điều kiện hiển thị>
- Actions and controls: <action, enable/disable rule, confirmation>
- Validation and copy intent: <rule và ý nghĩa; chỉ khóa copy khi cần>
- Outcomes/navigation: <success, next location, persistent feedback>
- Loading/empty/error/recovery: <state và đường tiếp tục>
- Responsive/accessibility: <thay đổi theo viewport, keyboard, focus, label, announcement>
- Backend obligations: <authorization, validation, consistency hoặc side effect chưa được chứng minh>
```

Ghi đủ chi tiết để implementation không phải tự phát minh business behavior, nhưng không biến tài liệu thành bản sao JSX/CSS.

## 4. Preview architecture

Preview phải chạy qua component và app context thật ở mức cao nhất hợp lý:

- sửa hoặc tách component dùng lại cho production thay vì clone thành mockup;
- giữ design tokens, typography, layout, routing/i18n/theme và provider liên quan;
- tách data/action boundary qua typed props, adapter hoặc interface nhỏ;
- đặt fixtures tại development/test boundary, không nhúng mock branch vào business component;
- đặt preview route/entry sau development-only guard hoặc cơ chế preview sẵn có;
- cô lập state switcher, viewport controls và debug labels khỏi UI được review;
- không gọi production mutation hoặc dùng production credentials;
- không tái tạo authorization, transaction hay backend state machine ở client chỉ để demo pass.

Fixture nên thể hiện contract thật dự kiến và cover state theo risk: nominal, loading, empty, long content, many items, validation error, permission denied, stale/conflict, retry/recovery. Không cần tạo mọi biến thể nếu chúng có cùng hành vi; ghi lý do cho phần không áp dụng.

## 5. Cách chạy và nối implementation thật

Ghi ngắn trong `UX_DESIGN.md` hoặc `REVIEW.md`:

- command và route/entry để mở preview;
- fixture hoặc control để vào từng state chính;
- component/data/action seam đã tạo;
- adapter/service/event nào implementation thật phải nối;
- nghĩa vụ backend chưa được preview chứng minh.

Các hướng dẫn này phải dùng được sau khi clone repository, không phụ thuộc lịch sử chat hoặc tool riêng của Codex.

## 6. Operated review

Review bằng cách thực sự vận hành preview trên revision đang đánh giá. Chọn coverage theo rủi ro, tối thiểu xem xét:

- entry và happy path của journey quan trọng;
- validation, permission, empty/error và recovery/cancellation liên quan;
- disabled/pending/success/failure feedback và khả năng tránh duplicate action;
- desktop/mobile và breakpoint có thay đổi hành vi;
- long text, localization, empty/many data nếu có khả năng phá layout hoặc hiểu nhầm;
- keyboard order, focus transition, accessible name, error association và announcement cần thiết;
- consistency với neighboring screens và design system.

Ghi “observed” chỉ cho hành vi đã trực tiếp chạy và nhìn thấy. Static inspection, automated assertions, screenshot hoặc simulated reasoning phải ghi đúng phương pháp của chúng.

## 7. Evidence và revision

Mỗi evidence entry cần đủ để truy lại:

```markdown
### EV-001 — <scenario/state>
- Source revision: <spec/flow/decision revision>
- FE revision: <commit + working-tree marker nếu có>
- Method/environment: <browser/device/viewport, command, fixture>
- Acceptance links: <AC/SCN IDs>
- Observed outcome: <điều thực sự quan sát>
- Result: pass | fail | partial | not-run
- Artifact: <screenshot/test/log path nếu có>
- Limitations: <điều evidence không chứng minh>
```

Screenshot hỗ trợ visual evidence nhưng không tự chứng minh navigation, focus, permission hoặc recovery. Test pass cũng không thay thế review trực tiếp về hierarchy, copy intent và comprehensibility.

Evidence trở thành stale khi behavior, source requirement, fixture contract hoặc component liên quan thay đổi. Invalidate evidence bị ảnh hưởng và chạy lại phạm vi cần thiết trên revision cuối.

## 8. Independent review

Reviewer phải độc lập với tác giả của phần đang được đánh giá và được cung cấp source documents, acceptance, preview instructions cùng revision chính xác. Reviewer tự đối chiếu oracle và vận hành các journey trọng yếu, không chỉ xác nhận checklist của tác giả.

Ghi reviewer identity hoặc vai trò, phạm vi, phương pháp, thời điểm/revision, findings và disposition. Nếu không thể có independent reviewer, verdict tối đa là `NOT_READY`; không mô tả self-review hoặc nhiều persona giả lập là independent review.

## 9. Findings và sửa đúng nguồn

Phân loại finding để tránh sửa triệu chứng:

| Loại | Nơi sửa chính |
|---|---|
| Specification | Specification, rule, scenario hoặc acceptance |
| Assumption/decision | Decisions/Assumptions và các link ảnh hưởng |
| UX design | `UX_DESIGN.md` và flow liên quan |
| FE preview | Source component, adapter, fixture hoặc preview entry |
| Evidence | Cách vận hành, coverage, artifact hoặc revision record |

Mỗi finding ghi severity/blocking, source links, reproduction/observation, expected và disposition. Sau khi sửa, rà lại downstream links, invalidate evidence cũ và rerun các scenario bị ảnh hưởng.

## 10. Verdict check

Chỉ kết luận `DESIGN_VALIDATED` khi tất cả điều sau đúng trên revision cuối:

- blocking acceptance có evidence `pass` và không stale;
- không còn blocking finding hoặc contradiction;
- Specification, UX Flow, UX Design và preview nhất quán;
- preview dùng source FE/component thật, có data/action seam và dev-only entry rõ;
- typecheck/build cùng các check áp dụng đã pass;
- desktop/mobile và state/recovery quan trọng đã được quan sát theo risk;
- independent review hiện hành đã hoàn tất;
- assumption còn active có behavior, rationale, impact và authority rõ;
- limitation và backend obligation chưa được chứng minh vẫn được nêu đúng.

Dùng `NOT_READY` nếu còn defect, check/evidence thiếu, fail hoặc stale, hay chưa có independent review. Dùng `BLOCKED` khi thiếu decision, dependency hoặc permission khiến không thể tiếp tục phần cần thiết; ghi affected IDs, phần đã hoàn thành và cách gỡ.
