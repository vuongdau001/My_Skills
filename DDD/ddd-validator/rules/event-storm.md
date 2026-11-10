---
category: Event Storm
rules: E1-E11
applies_to: [docs/bounded-contexts/*/aggregate-*.md]
sources: [Lesson 4.1, Lesson 4.2, Alberto Brandolini Event Storming, read-write-model dual-extraction]
merged_from: [V2 Event Completeness, V4 Business Rule Traceability]
---
# Event Storm Rules (E1-E11)

### E1: Events Past Tense, Commands Imperative
- **Nguồn:** Lesson 4.1 — *"Event = đã xảy ra, past tense; Command = yêu cầu, imperative, CÓ THỂ bị reject"*
- **Tại sao:** Sai tense = sai semantics = downstream systems phản ứng sai.
- **Checklist:**
  - [ ] Events kết thúc bằng past tense (-ed, -d)?
  - [ ] Commands là imperative verb?
  - [ ] Tên dùng đúng Glossary terms?

### E1b: Event Groups vs Lifecycles Terminology
- **Nguồn:** DDD/Event Storming convention — event list là collection of Domain Events; lifecycle là state/role transition model.
- **Tại sao:** Gọi Event Group là "Lifecycle" gây hiểu nhầm rằng đó là state machine đầy đủ (VD: `Lead Lifecycle` chỉ có `LeadReplaced`).
- **Checklist:**
  - [ ] Subsections dưới `## Events` dùng tên process/capability + `Events`? VD: `Team Management Events`, `Member Assignment Events`, `Lead Operation Events`.
  - [ ] Không dùng `Lifecycle` cho event group nếu không mô tả states/transitions?
  - [ ] Lifecycle thật được tách vào `## State Transitions / Lifecycles`?
  - [ ] Role variant lifecycle ghi rõ là `Role Assignment Lifecycle` thay vì aggregate lifecycle giả?

### E2: Mỗi Command → ≥2 Events (success + failure)
- **Nguồn:** Lesson 4.1 Reflect — *"AllocationRejected CŨNG là event. Mỗi Command → ≥2 events tiềm năng"*
- **Tại sao:** Chỉ model success path = miss toàn bộ error handling.
- **Checklist:**
  - [ ] Mỗi Command có rejection event (hoặc ghi rõ tại sao không cần)?
  - [ ] Rejection event ghi reason_code?
  - [ ] Bulk operations: partial failure documented?

### E3: Core Domain ≥ 15 events
- **Nguồn:** Lesson 4.1 — *"1 Core Domain thường có 15-30 events. <10 → chắc chắn thiếu"*
- **Merged from:** V2 (Event Completeness)
- **Checklist:**
  - [ ] Đếm events trong Core Domain ≥15?
  - [ ] Nếu <15, edge cases nào bị miss?

### E4: Policy = "Whenever Event → then Action"
- **Nguồn:** Lesson 4.2 — *"Policy = nơi business rules sống. Phải VISIBLE"*
- **Merged from:** V4 (Business Rule Traceability) — mỗi policy traceable to BR
- **Checklist:**
  - [ ] Policies đúng format "Whenever [Event] → then [Action]"?
  - [ ] Mỗi policy trace to ≥1 Business Rule?
  - [ ] Preconditions KHÔNG lẫn vào policies (precondition = TRƯỚC command, policy = SAU event)?
  - [ ] Cross-BC policies documented in Context Map, không trong Event Storm?

### E5: Hot Spots ≥ 3 cho Core Domain
- **Nguồn:** Lesson 4.2 — *"0 Hot Spots → chưa đào đủ sâu"*
- **3 loại:** Conflict 💥, Unknown ❓, Tech Debt ⚙️
- **Checklist:**
  - [ ] Core domain ≥3 Hot Spots?
  - [ ] Mỗi Hot Spot có classification?
  - [ ] Ít nhất 2/3 types present (không chỉ toàn Unknown)?
  - [ ] Mỗi Hot Spot có "Decision Owner"?

### E6: Mỗi Command phải có Read Model
- **Nguồn:** Alberto Brandolini — *"A Read Model is the information the actor needs to make a decision"*
- **Tại sao:** Command không có Read Model = Actor quyết định không dựa trên data = UX sẽ phải bịa screen flow.
- **Checklist:**
  - [ ] Mỗi Command trong bảng có cột "Read Model" không trống?
  - [ ] Read Model reference data thực sự tồn tại trong system?
  - [ ] Read Models có entry riêng trong section "## Read Models"?

### E7: Core Domain có ≥ 1 Pivotal Event
- **Nguồn:** Event Storming process discovery — *"Pivotal Events mark business phase transitions"*
- **Tại sao:** Không có Pivotal Event = chưa nhận diện được ranh giới phase → khó split thành bounded contexts sau này.
- **Checklist:**
  - [ ] Section "## Pivotal Events" tồn tại và không trống?
  - [ ] Mỗi Pivotal Event giải thích Phase trước/sau?
  - [ ] Pivotal Events có phải là Aggregate boundary signals không? (ghi nhận, không bắt buộc)

### E8: Recovery Path per Failure Event — lỗi thì retry từ đâu?
- **Nguồn:** Review Correction Log #1 (2026-07-09) — Agent tự suy luận "SAP lỗi → duyệt lại từ đầu (DUL → KTV → KTT)". Thực tế KTT chỉ cần duyệt lại tại bước cuối.
- **Tại sao:** Failure event không có recovery path → agent (và developer) tự giả định retry logic → sai toàn bộ error handling flow. Đây là class of bugs rất khó phát hiện vì "happy path vẫn đúng, chỉ sai khi có lỗi".
- **Checklist:**
  - [ ] Mỗi failure/rejection event trong Events table có entry trong **Recovery Paths** section?
  - [ ] Recovery path ghi rõ: (1) **Retry point** — retry từ step nào? (2) **Required action** — ai làm gì? (3) **State after retry** — entity quay về state nào?
  - [ ] Nếu failure event dẫn đến retry cả flow → ghi rõ "full restart" + rationale (tại sao không retry tại chỗ)?
  - [ ] External system failures (SAP, bank, email) có recovery path riêng biệt (≠ business rejection)?
- **Recovery Path Format:**
  ```
  | Failure Event | Retry Point | Required Action | State After Retry | Ref |
  |:--|:--|:--|:--|:--|
  | SAPSyncFailed | KTT approval step | KTT re-approves | Pending Approval | R-34 |
  | InvoiceRejected | Draft editing | Creator edits & resubmits | DRAFT | R-16 |
  ```
- **Ví dụ lỗi:** *SAP sync failure → agent viết "retry toàn bộ approval chain DUL→KTV→KTT". Thực tế: Invoice vẫn ở bước KTT, KTT chỉ cần click approve lại → gửi SAP lần nữa.*

### E9: State Transition Trigger Precision — chuyển state phải ghi rõ trigger
- **Nguồn:** Review Correction Log #3, #4 (2026-07-09) — Agent sai thời điểm đóng băng Milestone (ghi "sau Approved" thay vì "ngay khi gắn Invoice") và Invoice (ghi "sau Approved" thay vì "ngay khi Pending Approval").
- **Tại sao:** Lifecycle diagram chỉ ghi state names + arrows mà không ghi trigger chính xác → agent (và developer) tự suy luận trigger point → sai timing = sai invariants = data bị sửa khi không nên.
- **Checklist:**
  - [ ] Mỗi arrow/transition trong Lifecycle section có ghi **`[trigger: Command/Event]`**?
  - [ ] Trigger là **event/command cụ thể** (VD: `InvoiceSubmittedForApproval`), KHÔNG phải mô tả mơ hồ (VD: "khi duyệt xong")?
  - [ ] Mỗi transition ghi rõ: (1) **Actor** — ai trigger? (2) **Reversible?** — có thể quay lại state trước không? (3) **Unlock condition** — nếu reversible, điều kiện gì mở lock?
  - [ ] Transitions liên quan "đóng băng / immutable / lock" có ghi rõ **exact trigger point** (Pending Approval ≠ Approved ≠ Sent)?
- **Lifecycle Trigger Format:**
  ```
  DRAFT --[trigger: SubmitForApproval | actor: Creator]--> PENDING_APPROVAL
  PENDING_APPROVAL --[trigger: Approve | actor: KTT]--> APPROVED
  PENDING_APPROVAL --[trigger: Reject | actor: KTT]--> DRAFT (reversible)
  ```
- **Ví dụ lỗi:** *Lifecycle ghi `DRAFT → APPROVED → FROZEN` — thiếu state `PENDING_APPROVAL` ở giữa, nơi Invoice thực sự bị đóng băng. Developer implement lock tại `APPROVED` thay vì `PENDING_APPROVAL` → user vẫn sửa được Invoice đang chờ duyệt.*

### E10: Query Model Coverage — Read side phải là first-class (chống Write-side bias)
- **Nguồn:** read-write-model dual-extraction; Sprint Plan Coverage review (2026-07) — backlog rớt ~41.4 MD Read Models vì Event Storm chỉ model Write.
- **Tại sao:** Query (Xem danh sách / Xem chi tiết / Report) là read-only nên KHÔNG sinh Domain Event → bị lướt qua. Không có Query Model = backlog thiếu API `GET`, Projector và màn hình → thiếu ~40% scope.
- **Severity:** 🟠 degrading (🔴 blocking nếu có screen trong screen-registry không map được sang Command NÀO nhưng cũng không có Query — xem V12).
- **Checklist:**
  - [ ] Section `## Query Models (Output)` tồn tại và KHÔNG rỗng cho mỗi Core Aggregate?
  - [ ] Mỗi màn hình List / Detail / Report / Export có ≥1 Query (`Get<Thing>ListQuery`...)?
  - [ ] Query đọc từ **output Read Model** (không đọc trực tiếp Aggregate Root)?
  - [ ] Query đa điều kiện ghi rõ params (filter/sort/paging) + Access Scope (phân quyền data-level)?
  - [ ] `## Read Models` có ≥1 entry `Kind = output` (không chỉ toàn `input`)?
- **Anti-pattern tự-reject:** Nếu một capability chỉ có `Create/Update/Delete` + Event tương ứng mà KHÔNG có bất kỳ Query/View/Read Model output nào → FAIL, quay lại Step 4.6 (ddd-modeler) làm Dual-Extraction.
- **Ví dụ lỗi:** *`aggregate-payment-milestone.md` chỉ định nghĩa Read Model như data phụ trợ để validate Command, thiếu `GetPaymentMilestoneListQuery` + `GetPaymentMilestoneDetailQuery` → Feature #3 (list+filter, 13.2 MD) và #5 (detail, 21 MD) không có trong backlog.*

### E11: Projector Coverage — output Read Model phải có bộ đồng bộ
- **Nguồn:** CQRS/read-write-model — `Domain Event → Projector → Read Model`.
- **Tại sao:** Output Read Model không có Projector = không bao giờ cập nhật = màn hình hiển thị data cũ (stale) sau khi command đổi state.
- **Severity:** 🟠 degrading.
- **Checklist:**
  - [ ] Section `## Projectors` tồn tại và cover mọi output Read Model?
  - [ ] Mỗi Projector ghi rõ: (1) **Listens to Event** — event nguồn cụ thể; (2) **Updates Read Model** — đích; (3) **Sync mode** — sync/async?
  - [ ] Mỗi output Read Model trace ngược được tới ≥1 Domain Event (cột `Projected from Event(s)` không trống)?
  - [ ] Không có Domain Event nào ảnh hưởng data hiển thị mà thiếu Projector tương ứng?
- **Ví dụ lỗi:** *`PaymentMilestoneCreated` cập nhật summary revenue nhưng thiếu `PaymentMilestoneListProjector` → list view không hiển thị milestone mới cho tới khi restart cache.*
