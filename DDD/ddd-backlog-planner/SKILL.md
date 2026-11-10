---
name: ddd-backlog-planner
description: Dùng sau khi Phase 4 Validation PASS để tạo Development Backlog có traceability đầy đủ, hoặc khi backlog đã tồn tại và cần đối chiếu code branch/commit với BA baseline + QA evidence để cập nhật implementation status, remaining-work delta, progress report và next execution slice. Khi tạo mới, kế thừa UI Context và confirmed UI Contract Checklist vào story/task AC.
version: 1.2
---

# DDD Backlog Planner

## Chọn mode

- **Generation Mode:** tạo mới/sửa requirement scope, chạy đầy đủ pre-check và Pipeline Steps 1–5.
- **Implementation Reconciliation Mode:** backlog đã tồn tại; human hỏi progress/status sau khi dev code. Không regenerate stories. Đọc code evidence + BA baseline + QA report, rồi chạy Step 6.

## Khi nào kích hoạt
- Sau khi Phase 4 (Validation) PASS — tất cả DDD artifacts đã verified
- Input: `docs/`, `discovery/`, `clarification/`
- Output: `backlog/`

## Pre-checks (PHẢI kiểm tra trước khi bắt đầu)

Các gate 1–4 dưới đây áp dụng cho **Generation Mode**. Với **Implementation Reconciliation Mode**, chỉ yêu cầu backlog hiện hữu, BA baseline xác định được và code/QA evidence có thể kiểm tra; nếu thiếu evidence thì ghi `unverified`, không suy đoán `done`.
1. `validation/validation-report.md` tồn tại VÀ Gate Decision = "UNLOCK Phase 5"
2. `docs/bounded-contexts/*/flows/` không rỗng (V10 đã pass) VÀ có ≥1 read-flow `view-*.md` nếu BC có màn hình đọc (V11 đã pass)
3. `docs/bounded-contexts/*/aggregate-*.md` có Commands table VÀ section `## Query Models (Output)` + `## Projectors` không rỗng (E10, E11 đã pass)
4. **(Chỉ khi dự án có mockup/UI)** `mapping/screen-registry.md` tồn tại VÀ `flows/*.md` có `## UI Context` section — `ui-ddd-mapping` PHẢI chạy trước. Dự án không có UI (API/batch thuần) → ghi `N/A — no UI` vào backlog README và bỏ qua gate này. Với task UI có mockup, `ui-contract-reviewer` PHẢI tạo checklist field-level và không còn P0/P1 `CLARIFICATION_NEEDED` trước khi task vào sprint coding.

> Nếu pre-check 1-3 fail → STOP, thông báo user chạy Phase 4 (đặc biệt E10/E11/V11) trước.
> Nếu pre-check 4 fail → **STOP**: chạy `ui-ddd-mapping` để chốt Screen↔Command/Query, sau đó chạy `ui-contract-reviewer` để xác minh field/action/state và sinh UI AC. Screen mapped nhưng field chưa verified vẫn chưa đủ điều kiện coding.

---

## Pipeline

```
Step 1: Story Extraction
  Event Storm Commands → User Stories
  ↓
Step 2: Example Mapping (BDD)
  Business Rules + Events → Acceptance Criteria (Gherkin)
  ↓
Step 3: Walking Skeleton & Release Slicing
  Stories → Slice 1 (Walking Skeleton) + Slice 2-N (Releases)
  ↓
Step 4: INVEST Quality Gate
  Mỗi story phải đạt 6/6 INVEST criteria
  ↓
Step 5: Traceability Verification
  BR → Story → AC. Command → Story. Hot Spot → Spike. Không orphan.
```

---

## Step 1: Story Extraction

### Input
- `aggregate-*.md` → Commands table (12 columns), `## Query Models (Output)`, `## Projectors`, `## Read Models`
- `flows/*.md` → Command-flows per command + read-flows `view-*.md` per query
- `glossary/*.md` → Terms, attributes, business rules

### Mapping Rules

**[WRITE SIDE]**

| DDD Artifact | → | Backlog Item | Ví dụ |
|:--|:--|:--|:--|
| Command (actor: User) | → | **User Story (Write)** | `CreateTeam` → "Tạo Sales Team" |
| Command (actor: System) | → | **Technical Subtask** | `DeriveBatchStatus` → subtask (batch-status-derivation mechanism) |
| Success Event | → | **AC happy path** | `TeamCreated` → "Then team được tạo" |
| Failure Event | → | **AC error path** | `MemberAlreadyAssigned` → "Then hiện lỗi trùng member" |
| Policy | → | **Subtask** hoặc **AC clause** | `P4: Soft Delete` → subtask |
| Read Model (input) | → | **`Given` precondition** trong Gherkin | "Employee Search" → "Given danh sách employees đang hiển thị" |

**[READ SIDE]** — bắt buộc, KHÔNG được bỏ (chống Write-side bias)

| DDD Artifact | → | Backlog Item | Ví dụ |
|:--|:--|:--|:--|
| Query Model (output) | → | **User Story (Read)** — "Xem danh sách / chi tiết / report" | `GetPaymentMilestoneListQuery` → "Xem danh sách PM + filter" |
| Output Read Model schema | → | **Task R1: Data Model** (thiết kế View/Read table tối ưu đọc) | `PaymentMilestoneListView` → schema task |
| Projector | → | **Task R2: Technical Subtask** (Event Consumer đồng bộ) | `PaymentMilestoneListProjector` → subtask |
| Query API + params/scope | → | **Task R3: Query API** (filter/paging/phân quyền data) | `GET /payment-milestones` → API task |
| Read-flow `view-*.md` | → | nguồn `Given/Then (Read Side)` cho Read Story | `view-payment-milestone-list.md` |
| Business Rule (BR-xx) | → | **Rule** trong Example Mapping | BR-xx → Rule: "[mô tả rule từ Event Storm/Glossary]" |
| ADR | → | **Setup Task** (Sprint 0) | ADR-001 → "Setup Hybrid Delete strategy" |
| Hot Spot ❓ | → | **Spike Story** | "Warning Flag mechanism" → Spike cần test |
| Late Discovery (LD-xx) | → | **Spike Story** | LD-01 "Missing EditPaymentMilestone" → `SP-BL-001` |
| Glossary Entity | → | **Data Model Task** (Sprint 0) | SalesTeam → DB schema |
| UI Context: Screen | → | Field `**Screen:**` trong story | SCR-B02 → `**Screen:** SCR-B02 (filename.html)` |
| UI Context: Entry Point | → | `Given` trong Gherkin | "SCR-B01 → Click Create" → `Given AM đang xem SCR-B01` |
| UI Context: Form Fields | → | Subtask build form + `Given` data input | Contract, Duration → subtasks + Given |
| UI Context: Success Action | → | `Then` happy path | Redirect + Toast → `Then redirect về SCR-B01 + Toast` |
| UI Context: Error Action | → | `Then` error path | Inline validation → `Then inline error per field` |
| Confirmed UI Contract row | → | **UI AC** + QA coverage | `F-03 Unit Price` → `AC-UI-FIELD-03` + TC ID |
| UI Contract gap verdict | → | Delta task / clarification / QA task | `MOCKUP_STALE`, `CODE_DEFECT`, `QA_GAP` |

### Task Breakdown 5 nhóm — mỗi Feature phải đủ 2 nhánh

Cho mỗi feature thay đổi dữ liệu, sinh đủ 5 task (nguồn: read-write-model):

> **[WRITE SIDE]**
> - **W1:** Thiết kế Aggregate Root + logic Command, nhúng Invariants (validation).
> - **W2:** Định nghĩa + publish Domain Event sau khi Command thành công.
>
> **[READ SIDE]**
> - **R1:** Thiết kế schema Read Model / View Table (tối ưu cho đọc của UI).
> - **R2:** Viết Projector / Event Consumer lắng nghe Event → cập nhật Read Model.
> - **R3:** Viết Query API lấy data từ Read Model trả về Frontend (filter/paging/scope).

### Anti-Pattern Self-Check (BẮT BUỘC trước khi chốt backlog)

- ❌ **Chỉ có Command/Event:** Nếu task list của một Feature chỉ có `Create/Update/Delete` + Event mà KHÔNG có task nào chứa `Query`, `View`, `Read Model`, hoặc `Projector` → **tự Reject, quay lại map Read Side (E10/E11 trong aggregate).**
- ❌ **Query đọc Aggregate:** Task R3 KHÔNG được đọc trực tiếp Aggregate Root cho UI phức tạp — phải qua Read Model riêng (R1).
- ✅ Mục tiêu cân bằng: mỗi Core feature có cả nhánh Write (W) lẫn Read (R).

### User Story Format

```markdown
### US-[BC]-[SEQ]: [Tên ngắn]

**As a** [role từ Stakeholder Map],
**I want** [goal — lấy từ Command name],
**so that** [benefit — lấy từ Value Chain / Pain Points].

**Source:** [Command name] | [Flow file] | [BR-xx]
**Screen:** [SCR-xxx] ([filename.html](relative-path)) — bỏ trống nếu ui-ddd-mapping chưa chạy
**Entry Point:** [SCR-parent] → "[Button label]" — bỏ trống nếu chưa có UI Context
**Priority:** [P0/P1/P2] — Core domain = P0, Supporting = P1, Generic = P2
**Estimate:** [S/M/L] — dựa trên Flow complexity
**Slice:** [Walking Skeleton / Release N]
**Dependencies:** [blocked-by: US-xxx, nếu có]
```

### Numbering Convention
- `US-TC-001` → User Story, Team Config BC, #001
- `TT-TC-001` → Technical Task, Team Config BC, #001
- `SP-TC-001` → Spike, Team Config BC, #001

> Prefix lấy từ tên BC (VD: `TC` = crm-team-config, `BL` = payment, `INV` = invoicing) — không hardcode `MI`, chọn theo BC đang lập backlog.

---

## Step 2: Example Mapping (BDD)

### Áp dụng cho TẤT CẢ stories (không chỉ Core)

Với mỗi User Story, tạo Example Mapping:

```markdown
#### Example Mapping

**Rules:**
- [BR-xx]: [Business Rule description]

**Examples (Gherkin):**

```gherkin
Scenario: [Happy path — descriptive name]
  Given [Read Model state — precondition]
  When [Command — user action]
  Then [Success Event — expected outcome]

Scenario: [Error path — rejection name]
  Given [precondition that causes rejection]
  When [same Command]
  Then [Failure Event — error shown]
  And [Recovery action hint]
```

**Questions:** [Hot Spots / Late Discoveries liên quan, nếu có]
```

### Gherkin Guidelines (Given-When-Then mở rộng — có vế Read Side)
- `Given (Read Side)` = màn hình Read Model **input** (lấy từ Event Storm "Read Model" column, Kind=input)
- `When (Write Side)` = Command (lấy từ Event Storm "Command" column)
- `Then (Domain)` = Success/Failure Event (lấy từ Event Storm "Event" columns)
- `Then (Read Side)` = Projector cập nhật **output** Read Model → UI hiển thị data mới (lấy từ `## Projectors` + `## Query Models`)
- Dùng **Ubiquitous Language** từ Glossary — KHÔNG dùng technical terms
- Mỗi Write story PHẢI có ≥1 happy + ≥1 error path; mỗi Read story PHẢI có ≥1 scenario hiển thị đúng + ≥1 scenario filter/empty/phân quyền
- Ví dụ vế Read Side: `Then danh sách PM hiển thị milestone vừa tạo` (chứng minh Projector chạy)

### Nếu ui-ddd-mapping đã chạy: Dùng UI Context làm nguồn Gherkin

Khi flow file có `## UI Context` section, **ưu tiên dùng** UI Context thay vì chỉ dùng Event Storm:

| UI Context Field | → | Gherkin Clause | Ví dụ |
|:--|:--|:--|:--|
| Entry Point | → | `Given [Actor] đang xem [Screen]` | `Given AM đang xem SCR-B01` |
| Pre-load Data (Read Model) | → | `Given [data] đã được load` | `Given danh sách contracts hiển thị` |
| Form Fields + data | → | `Given [Actor] điền [fields]` (khi cần test input) | `Given AM điền Duration=Q1/2026` |
| Submit button / `data-command` | → | `When [Actor] click "[Button]"` | `When AM click "Save"` |
| Success Action (redirect) | → | `Then redirect về [Screen]` | `Then redirect về SCR-B01` |
| Success Action (toast) | → | `And Toast "[message]" hiển thị` | `And Toast "Created successfully"` |
| Error Action (inline validation) | → | `Then inline error tại field [Field]: [error]` | `Then inline error tại Contract: CONTRACT_NOT_ACTIVE` |
| Conditional UI | → | `And [UI state changes]` | `And nút Edit bị disable` |

> **Ghi nhớ**: Gherkin KHÔNG được dùng tên kỹ thuật (table name, API endpoint). Chỉ dùng Ubiquitous Language từ Glossary + Screen ID + Button label từ UI Context.

### UI Contract AC cho Task

Ngoài Gherkin business behavior, mỗi task UI phải nhận AC được sinh từ checklist confirmed:

- `AC-UI-STRUCT`: regions/components bắt buộc.
- `AC-UI-FIELD`: label, control, source, required/default/editable/format.
- `AC-UI-STATE`: actor/status visibility và editability.
- `AC-UI-ACTION`: confirmation, success/error/empty/loading behavior.
- `AC-UI-VISUAL`: viewport, layout constraint, tolerance và dynamic masks.

Không chấp nhận AC “match mockup” nếu không có element-level checklist.

### NFR Acceptance Criteria (BẮT BUỘC)

> Nguồn: Memo project — authz/IDOR và race-condition từng lọt production vì backlog chỉ mô tả happy/error chức năng, không có tiêu chí bảo mật/đồng thời → không có nguồn để sinh test NFR.

Với mỗi story có **API/route** hoặc chạm **resource thuộc về user/tổ chức/data scope**, thêm scenarios:

```gherkin
Scenario: [Security] Chưa đăng nhập không truy cập được
  Given user chưa đăng nhập
  When gọi [command/query]
  Then bị từ chối (401), không lộ data

Scenario: [Security] Không truy cập được resource ngoài phạm vi
  Given user A đã đăng nhập
  And resource thuộc về user/đơn vị B (ngoài data scope của A)
  When user A thao tác trên resource đó
  Then bị từ chối (403/404), data không đổi

Scenario: [Concurrency] Ghi đồng thời không mất dữ liệu   # chỉ khi có shared write
  Given 2 thao tác ghi vào cùng aggregate gần như đồng thời
  When cả hai hoàn tất
  Then không mất update nào (optimistic lock / version check)
```

**Checklist NFR mỗi story (ghi `N/A` kèm lý do nếu không áp dụng):**
- [ ] AuthN (chưa login → 401)
- [ ] AuthZ / data scope (ngoài phạm vi → 403/404)
- [ ] Concurrency (shared write → no lost update)
- [ ] Observability (lỗi được log đủ để trace, không nuốt error)

---

## Step 3: Walking Skeleton & Release Slicing

### Walking Skeleton (Slice 1)
**Định nghĩa:** Thin end-to-end slice xuyên suốt toàn bộ architecture layers.

**Cách chọn:**
1. Lấy Value Chain từ `discovery/value-chain.md`
2. Chọn 1 story MỎI NHẤT từ MỖI phase trong value chain
3. Story phải đi qua TẤT CẢ layers của kiến trúc thực tế (VD: UI → API → Domain → DB; thêm layer đặc thù như AI/Integration nếu kiến trúc có)

**Walking Skeleton PHẢI bao gồm:**
- ≥1 story từ mỗi Core sub-domain
- Setup tasks (Sprint 0): Auth, DB schema, project init
- Chứng minh architecture hoạt động end-to-end

### Release Slicing (Jeff Patton)

| Release | Nội dung | Mục đích |
|:--|:--|:--|
| **Sprint 0** | Setup: project init, DB schema, auth, CI/CD | Infrastructure |
| **Slice 1: Walking Skeleton** | Thin E2E: Create Team → Assign Member → View Team Roster | Prove architecture |
| **Slice 2: Core Complete** | Toàn bộ Core commands + queries, đủ error/recovery paths (VD: Move/Replace Lead, Bulk operations) | Core value delivery |
| **Slice 3: Polish** | Export, report, UI polish, edge cases, NFR hardening | Production ready |

### SPIDR Splitting
Nếu story quá lớn (estimate > L), cắt theo SPIDR:
- **S**pike — Tách phần cần research thành Spike riêng
- **P**aths — Tách happy path vs error paths
- **I**nterface — Tách mobile vs desktop (nếu cần)
- **D**ata — Tách theo subset of data/fields
- **R**ules — Defer complex BR sang sprint sau

---

## Step 4: INVEST Quality Gate

### Checklist cho MỖI story

| # | Criterion | Check | Fail action |
|:--|:--|:--|:--|
| I | **Independent** | Story có thể ship riêng, không blocked bởi story khác? | Tách dependency hoặc ghi rõ `blocked-by: US-TC-xxx` |
| N | **Negotiable** | Story mô tả WHAT (không phải HOW)? | Bỏ implementation details khỏi description |
| V | **Valuable** | User benefit rõ ràng trong "so that" clause? | Rewrite benefit hoặc merge vào story khác |
| E | **Estimable** | Team có đủ info để estimate? Có flow diagram? | Tạo Spike nếu thiếu info |
| S | **Small** | Hoàn thành trong 1 sprint? Estimate ≤ L? | SPIDR split |
| T | **Testable** | Có ≥1 happy + ≥1 error Gherkin scenario? | Thêm AC bằng Example Mapping |

**Minimum pass:** 6/6. Story không đạt → fix trước khi đưa vào backlog.

---

## Step 5: Traceability Verification

### Completeness Checks (trong backlog file)

| Check | Scan | Cross-ref | Severity |
|:--|:--|:--|:--|
| **Mỗi Command → ≥1 Story** | Event Storm commands | backlog stories "Source" field | 🔴 blocking |
| **Mỗi Query (output) → ≥1 Read Story** | `## Query Models` | backlog Read stories "Source" field | 🔴 blocking |
| **Mỗi output Read Model → R1+R2+R3 tasks** | `## Read Models` (Kind=output) + `## Projectors` | backlog tasks | 🔴 blocking |
| **Mỗi screen → Command hoặc Query story** | screen-registry.md | backlog stories | 🔴 blocking |
| **Mỗi confirmed UI row → AC + QA** | UI Contract Checklist | task AC + TC ID | 🔴 blocking |
| **Không unresolved P0/P1 UI clarification** | UI Contract Checklist | verdict/status | 🔴 blocking |
| **Mỗi BR → ≥1 AC** | BC README BR index | backlog stories Gherkin scenarios | 🔴 blocking |
| **Mỗi story có API/resource → NFR checklist** | All stories | NFR scenarios hoặc `N/A` + lý do | 🟠 degrading |
| **Mỗi Hot Spot → Spike** | Event Storm Hot Spots | backlog spikes | 🟠 degrading |
| **Mỗi ADR → Setup Task** | decisions/ ADR files | Sprint 0 tasks | 🟠 degrading |
| **INVEST 6/6** | All stories | INVEST checklist | 🟠 degrading |
| **Walking Skeleton covers E2E** | Value Chain phases | Slice 1 stories | 🟠 degrading |
| **No orphan tasks** | All tasks | Backward trace → story → BR | 🟡 cosmetic |

### Traceability Table Format (trong README.md)

```markdown
## Traceability Matrix

| BR/Command | Story | AC Count | Slice | Status |
|:--|:--|:--|:--|:--|
| BR-xx [mô tả rule, VD: member không trùng trong 1 team] | US-TC-003 | 2 (happy + error) | Skeleton | ✅ |
| BR-xx [mô tả rule khác] | US-TC-007 | 3 | Slice 2 | ✅ |
| CreateTeam (CMD) | US-TC-001 | 2 | Skeleton | ✅ |
| HS-01 [tên Hot Spot từ Event Storm] | SP-TC-001 | — | Spike | ✅ |
| ... | ... | ... | ... | ... |

**Coverage:** [X]/[X] BRs covered | [X]/[X] Commands covered | [X]/[X] Hot Spots covered
```

---

## Step 6: Implementation Reconciliation (post-code)

Khi dev báo đã code hoặc user yêu cầu progress:

1. **Resolve evidence:** kiểm tra feature branch và target branch; map commit/file/API/UI vào task IDs. Xác nhận code đã port/merge hay chỉ tồn tại trên feature branch.
2. **Compare baselines:** dùng BA baseline mới nhất làm requirement hiện hành; dùng QA report mới nhất làm acceptance evidence và ghi rõ report có predates BA delta hay không.
   Nếu phát hiện mockup-vs-code hoặc field correctness chưa xác minh, chạy `ui-contract-reviewer` trước khi tạo delta task.
3. **Separate three dimensions:** traceability coverage, code delivery và acceptance status.
4. **Never equate commit with Done:** code tồn tại nhưng thiếu AC hoặc QA fail → `review`/`needs-update`, không reset về TODO và không đánh Done.
5. **Generate remaining-work delta:** gom theo outcome, không tạo lại toàn bộ feature. Tạo next execution slice gồm delta implementation + regression gate; giữ deferred scope riêng.
6. **Update execution views:** status summary trong `tasks.md`, track rollup, query registry nếu read-side status đổi, historical banner trên pre-code sprint plan (và live `state/` nếu dự án có cơ chế simulation/state tracking riêng).

### Status vocabulary

| Status | Dùng khi |
|:--|:--|
| `todo` | Chưa có implementation evidence |
| `review` | Code exists; chờ BA verification/regression |
| `needs-update` | Code exists; đã xác định BA delta hoặc QA failure |
| `blocked` | Chưa thể triển khai do dependency/decision/deferred scope |
| `done` | DoD hiện hành + BA acceptance + QA evidence đều pass |
| tombstone/removed | Scope bị loại; code dư thừa trở thành cleanup task |

### Progress report tối thiểu

- Baseline code delivered theo track.
- Material implementation remaining.
- Acceptance/retest remaining.
- Deferred/out-of-scope.
- Release decision: GO/NO-GO kèm evidence.

---

## Output Structure

```
backlog/
├── README.md              ← Index + Walking Skeleton definition + Traceability Matrix
├── sprint-0-setup.md      ← Technical setup tasks (ADRs → Tasks, DB schema, Auth)
├── epic-team-management.md    ← Stories: CreateTeam, UpdateTeam, ChangeUnit, DeactivateTeam
├── epic-member-assignment.md  ← Stories: AddMember, UpdateMemberDates, RemoveMember
├── epic-lead-operations.md    ← Stories: ReplaceLead, PromoteToLead
├── epic-member-transfer.md    ← Stories: MoveMember
└── epic-bulk-operations.md    ← Stories: BulkAddMember, BulkMoveMember
```

### File Naming Convention
- `sprint-0-setup.md` — Infrastructure tasks
- `epic-[domain-capability].md` — Stories grouped by sub-domain
- File name dùng **Ubiquitous Language** từ Domain Map

### Sau khi backlog xong: Sprint Plan (tracks + dependency-graph)

Bước tiếp theo (ngoài scope skill này, làm thủ công hoặc bằng prompt riêng) là sinh `sprint-plan/tracks.md` + `sprint-plan/dependency-graph.md` — chia US thành track song song theo dev. Khi làm bước đó, **bắt buộc áp dụng Shared-Screen Foundation Rule**: scan field `**Screen:**` của mọi US, nếu 1 Screen ID bị ≥2 track khác nhau tham chiếu → auto-insert task `TK-<BC>-S0-screen-<SCR-ID>` vào Sprint 0 (skeleton + pinned layout contract, HARD edge tới mọi task track khác dùng screen đó). Lý do: nếu ≥2 dev cùng dựng 1 màn hình song song mà không có skeleton chung → layout drift + merge conflict. Worked example (CRM): `backlog/payment/sprint-plan/` (SCR-B04) và `backlog/invoicing/sprint-plan/` (SCR-I04).

### Epic File Template

```markdown
# Epic: [Domain Capability Name]

**Sub-domain:** [Core/Supporting/Generic]
**Priority:** [P0/P1/P2]
**Slice:** [Walking Skeleton / Release 2 / Release 3]

## Stories

### US-[BC]-[SEQ]: [Story Name]

**As a** [role],
**I want** [goal],
**so that** [benefit].

**Source:** [Command] | [Flow file] | [BR-xx]
**Priority:** P[0/1/2] | **Estimate:** [S/M/L] | **Slice:** [1/2/3]
**Dependencies:** [blocked-by: US-xxx, nếu có]

#### Subtasks
- [ ] [TT-<BC>-xxx]: [Technical task description]
- [ ] [TT-<BC>-xxx]: [Another task]

#### Example Mapping

**Rules:**
- BR-xx: [rule description]

**Examples:**
\```gherkin
Scenario: [Happy path]
  Given [precondition]
  When [action]
  Then [outcome]

Scenario: [Error path]
  Given [precondition causing error]
  When [action]
  Then [error outcome]
\```

---
```

---

## Quality Scorecard

| Metric | Minimum | Target |
|:--|:--|:--|
| Command → Story coverage | 100% | 100% |
| Query (output) → Read Story coverage | 100% | 100% |
| Screen → Command/Query Story coverage | 100% | 100% |
| Confirmed UI rows → task AC coverage | 100% | 100% |
| Confirmed UI rows → QA coverage | 100% | 100% |
| Unresolved P0/P1 UI clarification | 0 | 0 |
| BR → AC coverage | 100% | 100% |
| Hot Spot → Spike coverage | 80% | 100% |
| INVEST pass rate | 90% | 100% |
| Stories with ≥2 Gherkin scenarios | 100% | 100% |
| Stories có API/resource kèm NFR checklist | 100% | 100% |
| Walking Skeleton covers all layers | Yes | Yes |

---

## Integration with DDD Pipeline

```
Phase 0-1: Discovery     ← ddd-discovery
Phase 2: Clarification   ← ddd-questioner
Phase 3: Modeling         ← ddd-modeler
Phase 4: Validation       ← ddd-validator
Phase 5: Documentation    ← ddd-documenter         (song song được với UI Contract Gate)
UI Contract Gate          ← ui-ddd-mapping → ui-contract-reviewer   (nếu có mockup/UI)
Phase 6: Backlog Planning ← ddd-backlog-planner
Phase 7: Implementation   ← (coding)
```

> **Gate G6:** Backlog phải đạt Quality Scorecard minimums trước khi bắt đầu coding (Phase 7). Định nghĩa đầy đủ các gate: `../_shared/references/gates-and-project-state.md`.

## Changelog
| Version | Date | Changes |
|:--|:--|:--|
| 1.0 | 2026-07-11 | Initial: 5-step pipeline, INVEST gate, Example Mapping for all stories, inline traceability. Sources: Jeff Patton, Brandolini, Matt Wynne, BABOK v3, IEEE 29148, SPIDR |
| 1.1 | 2026-07-20 | Read-side coverage: Query→Read Story + Projector→R2 + Read Model→R1 + Query API→R3 mapping; 5-task template (W1-W2-R1-R2-R3); Given-When-Then mở rộng vế Read Side; anti-pattern self-check; ui-ddd-mapping thành mandatory gate (pre-check 4). Traceability + scorecard thêm Query/Screen coverage. Source: read-write-model + Sprint Plan Coverage review |
| 1.2 | 2026-11-10 | Packaging cho My_Skills/DDD: thêm NFR Acceptance Criteria (port từ Memo v1.1) vào Step 2 + traceability + scorecard; pre-check 4 chỉ áp dụng khi có UI, path generic `mapping/`; sửa ví dụ release slicing bị lẫn từ Memo (recording/summarization, layer AI); bỏ link methodology ngoài gói; làm rõ thứ tự Phase 5 ↔ UI Contract Gate |
