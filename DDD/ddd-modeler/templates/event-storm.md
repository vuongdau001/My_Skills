# Template: Event Storm

**File:** `docs/bounded-contexts/<bc-name>/aggregate-<name>.md`

```markdown
# Event Storm — [Domain Name]
## Commands
| Command | Actor | Trigger | Read Model | Preconditions | Success Event | Failure Event | Policy |
## Events (Domain Events — past tense)
> Subsections are Event Groups by process/capability, NOT lifecycles/state machines.
### [Process/Capability] Events
| Event | Trigger | Data | Ref |
## Policies (When X → Y)
| Policy | Trigger Event | Action | BR Source |
## Read Models
> Read Model có **2 loại** — PHẢI phân biệt bằng cột `Kind`:
> - `input` = data actor xem **TRƯỚC** khi ra Command (decision-support, vế Given).
> - `output` = data hiển thị **SAU** khi Command thành công (list / detail / report — Query side).
| Read Model | Kind (input/output) | Served by (Query/Projector) | Used before Command | Projected from Event(s) | Data |
## Query Models (Read Side — Output)
> Mỗi màn hình List / Detail / Report / Export PHẢI có 1 Query Model. Query **KHÔNG** đọc trực tiếp Aggregate Root — đọc từ Read Model đã projected (xem Anti-Pattern read-write-model).
| Query | Screen(s) served | Source Read Model | Params (filter/sort/paging) | Access Scope (data-level perm) | Ref |
## Projectors (Read Model Sync)
> Mỗi output Read Model PHẢI có ≥1 Projector đồng bộ từ Domain Event. Không Projector = Read Model không bao giờ cập nhật = màn hình hiển thị data cũ.
| Projector | Listens to Event | Updates Read Model | Sync mode (sync/async) | Ref |
## Pivotal Events
Events đánh dấu ranh giới phase trong business process:
| Pivotal Event | Phase trước | Phase sau | Tại sao quan trọng |
## State Transitions / Lifecycles
Lifecycle chỉ dùng cho state machine hoặc role assignment có transition rõ ràng.
Mỗi transition PHẢI ghi: [trigger: Command/Event | actor: Role | reversible: yes/no]
### [Aggregate] State Lifecycle
### [Entity] Status Lifecycle
### [Role] Assignment Lifecycle
## Recovery Paths
Mỗi failure/rejection event PHẢI có recovery entry:
| Failure Event | Retry Point | Required Action | State After Retry | Ref |
## Hot Spots (❓ unresolved)
## Aggregates (clusters)
## Event Flow Diagram
```

**Dual-Extraction (BẮT BUỘC — chống Write-side bias):**
Mỗi capability PHẢI trích xuất theo **cặp** câu hỏi, không chỉ tìm động từ (Command):
- **Write-side Question:** Hệ thống thực hiện lệnh gì? Invariant nào check? Event nào sinh ra?
- **Read-side Question:** Để ra lệnh đó actor cần nhìn thấy data gì (input Read Model)? Sau khi lệnh xong màn hình nào phải cập nhật (output Read Model + Projector + Query)?

Chuỗi hoàn chỉnh một feature:
```
[Read Model cũ] ─►(kích hoạt)─► [Command] ─► [Aggregate/Rule] ─► [Event] ─►(Projector)─► [Read Model mới] ─► [Query] ─► UI
```
Command đi đôi Query · Aggregate Root đi đôi Read Model (View) · Domain Event đi đôi Projector.

**Khái niệm mới:**
- **Read Model (input):** Actor cần xem dữ liệu gì trước khi ra quyết định issue Command. Không có Read Model = actor quyết định mù.
- **Read Model (output) / Query Model:** Data hiển thị SAU command (list/detail/report). Là first-class deliverable, KHÔNG phải data phụ trợ để validate command. Thiếu = read side "tàng hình", backlog rớt task hiển thị.
- **Projector (Event Handler):** Bộ đồng bộ lắng nghe Domain Event → cập nhật output Read Model. 1 Event có thể fan-out nhiều Projector.
- **Query:** API/read path lấy data từ output Read Model trả về UI. Cấm đọc trực tiếp Aggregate Root cho UI phức tạp.
- **Pivotal Event:** Event thay đổi trạng thái nghiệp vụ (phase transition). Pivotal Events thường là aggregate boundary signals.
- **Event Group:** Nhóm events theo process/capability để dễ đọc (VD: Team Management Events, Member Assignment Events). Event Group KHÔNG phải lifecycle.
- **Lifecycle / State Transition:** Chỉ dùng khi có chuỗi trạng thái/role assignment rõ ràng (VD: SalesTeam ACTIVE → INACTIVE, TeamMember PLANNED → ACTIVE → REMOVED, TeamLead Role Assignment). Không dùng "Lifecycle" để đặt tên nhóm events.
- **Lifecycle Trigger Precision (BẮT BUỘC):** Mỗi arrow trong lifecycle diagram PHẢI ghi `[trigger: Command/Event | actor: Role]`. Lifecycle chỉ ghi state names mà không ghi trigger = FAIL. Đặc biệt với transitions liên quan "đóng băng / immutable / lock" — PHẢI ghi rõ exact trigger point (Pending Approval ≠ Approved ≠ Sent).
- **Recovery Paths (BẮT BUỘC):** Mỗi failure/rejection event PHẢI có recovery path: retry từ đâu? Ai làm? Entity quay về state nào? External system failures (SAP, bank) có recovery riêng biệt (≠ business rejection).

## Event Storm Naming Rules — BẮT BUỘC

1. **Event names:** past tense, business outcome đã xảy ra (`TeamCreated`, `MemberPromotedToLead`).
2. **Command names:** imperative verb (`CreateTeam`, `PromoteMember`).
3. **Event section headings:** dùng process/capability + `Events`, KHÔNG dùng `Lifecycle` trừ khi section mô tả state machine.
   - ✅ `Team Management Events`
   - ✅ `Member Assignment Events`
   - ✅ `Lead Operation Events`
   - ✅ `Bulk Member Operation Events`
   - ❌ `Lead Lifecycle` nếu chỉ liệt kê `LeadReplaced`
4. **Lifecycle section:** tách riêng dưới `## State Transitions / Lifecycles`; lifecycle phải có states/transitions hoặc role assignment transitions.
5. **Role variant:** Nếu concept là role variant của entity (VD: TeamLead = TeamMember với `member_role='TEAM_LEAD'`), dùng `Role Assignment Lifecycle`, không tạo aggregate lifecycle giả.
6. **Flow filenames:** đặt theo process/capability bằng kebab-case; lifecycle chỉ dùng trong filename nếu file thật sự là state lifecycle.
   - ✅ `team-management.md`
   - ✅ `member-assignment.md`
   - ✅ `member-transfer.md`
   - ✅ `lead-operations.md`
   - ✅ `bulk-member-operations.md`
   - ❌ `lead-lifecycle.md` nếu file mô tả Replace/Promote operations
7. **Query names:** `Get<Thing>ListQuery`, `Get<Thing>DetailQuery`, `Export<Thing>Query` — imperative Get/Export + hậu tố `Query`.
8. **Projector names:** `<ReadModel>Projector` (VD: `PaymentMilestoneListProjector`).
9. **Read-flow filenames:** prefix `view-` cho luồng đọc thuần (không sinh Domain Event).
   - ✅ `view-payment-milestone-list.md`
   - ✅ `view-payment-milestone-detail.md`
   - ❌ đặt luồng đọc chung file với command-flow — tách riêng để backlog nhận diện Read Story.
