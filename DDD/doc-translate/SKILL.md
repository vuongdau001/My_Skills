---
name: doc-translate
description: Dùng khi cần dịch một hoặc nhiều file markdown kỹ thuật (DDD/architecture) từ tiếng Anh sang tiếng Việt, theo chuẩn song ngữ nhất quán — giữ nguyên thuật ngữ DDD/tech và named concepts (capability/feature names), thêm ngoặc tiếng Anh chỉ lần đầu xuất hiện cho từ thông thường.
version: 1.2
---

# doc-translate — Skill Definition

## Mô tả
Skill dịch các tài liệu kỹ thuật (Markdown) từ tiếng Anh sang tiếng Việt theo phong cách **song ngữ nhất quán**:
- Nội dung chính bằng tiếng Việt, dễ đọc
- Thuật ngữ chuyên môn giữ nguyên tiếng Anh
- Các từ thông thường được dịch kèm ngoặc Anh **chỉ lần đầu xuất hiện** trong file

## Input
- Một hoặc nhiều file `.md` cần dịch
- Mỗi file được xử lý độc lập (bảng xuất hiện đầu tiên trong từng file = "lần đầu" cho ngoặc)

> Ví dụ trong skill lấy từ dự án CRM (POA/ECQS/Kafka) — thay bằng thuật ngữ của dự án đang dịch.

## Quy tắc Song ngữ Nhất quán

### Quy tắc 1 — Thuật ngữ DDD/Kiến trúc: KHÔNG dịch
Các thuật ngữ sau **luôn giữ nguyên tiếng Anh**, không thêm ngoặc:

| Nhóm | Các term giữ nguyên |
|:--|:--|
| DDD patterns | `Bounded Context`, `Conformist`, `Anti-Corruption Layer`, `Customer-Supplier`, `Open Host Service`, `Published Language`, `Domain Event`, `Aggregate`, `Entity`, `Value Object`, `Repository`, `Domain Service` |
| Integration | `REST API`, `Kafka`, `Debezium`, `CDC`, `JWT`, `LDAP`, `Redis`, `ACL` |
| Tech stack | Tên công nghệ cụ thể: `Spring Boot`, `Vue 3`, `PostgreSQL`, `Docker`, `Kafka`, v.v. |
| Code identifiers | Tên topic, event, field, constant: `ecqs.employee.changes`, `EmployeeDataChanged`, `ACTIVE`, `PLANNED`, v.v. |
| Viết tắt đã định nghĩa | `AMS`, `GL`, `BUL`, `OHS`, `ADR`, `BC`, v.v. |
| Capability/Feature names | Tên gọi của tính năng, khái niệm đã được đặt tên (lấy từ Domain Map/Glossary của dự án). VD (CRM): `Team Management`, `Member Assignment`, `Lead Operations`, `TeamLead Role Assignment Lifecycle`, `Temporal State Machine`, `Reason Tracking`, `Multi-role Union`, `Employee Display Data`, `Data Scope Cascade`, `Warning Flag Engine`, v.v. |

### Quy tắc 2 — Phân biệt "tên gọi" vs "mô tả"

> **Nguyên tắc then chốt:** Nếu cụm từ là **tên gọi đã được đặt** (named concept) cho một capability, feature, hoặc pattern → **giữ nguyên tiếng Anh**. Nếu cụm từ chỉ là **mô tả hành động/trạng thái** chung → dịch sang tiếng Việt.

**Cách phân biệt:**
- Nó có phải là **tên riêng** của một tính năng/concept trong hệ thống không? → Giữ EN
- Nó có xuất hiện như **label/heading** trong tài liệu kiến trúc không? → Giữ EN
- Nó chỉ là **từ thông thường** mô tả chung? → Dịch VN

```
✅ "Team Management (Create/Update/Deactivate)"        ← "Team Management" là tên capability → giữ EN
❌ "Vòng đời nhóm (Create/Update/Deactivate)"          ← dùng Lifecycle sai nghĩa + dịch tên capability → SAI

✅ "Temporal State Machine (PLANNED/ACTIVE/REMOVED)"   ← tên concept → giữ EN
❌ "Máy trạng thái thời gian (PLANNED/ACTIVE/REMOVED)" ← dịch tên concept → SAI

✅ "Multi-role Union"                                   ← tên feature → giữ EN
❌ "Hợp nhất đa vai trò (Multi-role union)"             ← dịch tên feature → SAI

✅ "Reason Tracking"                                    ← tên capability → giữ EN  
❌ "Theo dõi lý do (Reason tracking)"                   ← dịch tên capability → SAI
```

### Quy tắc 3 — Từ thông thường dịch được: ngoặc Anh LẦN ĐẦU, bỏ sau
Format: `tiếng Việt (English)` — chỉ lần đầu từ đó xuất hiện trong file.

Ví dụ áp dụng đúng:
```
✅ "CRM gửi thông tin xác thực (credentials) đã mã hóa RSA → POA xác thực → trả về JWT"
   (lần sau chỉ dùng "xác thực", không lặp ngoặc)

✅ "ECQS phát hành (publish) 4 topics → CRM tiêu thụ (consume)"
   (publish/consume là lần đầu, sau đó dùng "phát hành"/"tiêu thụ" không kèm ngoặc)

❌ "CRM xác thực (validate) → POA xác thực (validate)" — lặp ngoặc = sai
```

### Quy tắc 4 — Tiêu đề Section (Heading): Song ngữ nhất quán
Format: `## Tiếng Việt (English Title)`

```
✅ ## Các Mối Quan Hệ (Relationships)
✅ ## Chi tiết Điểm Tích hợp (Integration Points Detail)
✅ ### Thuật ngữ Cấu trúc (Structural Terms)
❌ ## Relationships  ← không dịch
❌ ## Mối quan hệ    ← thiếu ngoặc Anh
```

### Quy tắc 5 — Tiêu đề Cột Bảng (Table Header): Dịch sang Việt
Cột nào có từ Anh đơn thuần → dịch. Cột nào là technical term → giữ.

```
✅ | Thuật ngữ CRM | Thuật ngữ ECQS | Loại phiên dịch (Translation Type) | Ref |
✅ | Lý do (Rationale) | Giao thức (Protocol) |
✅ | Trình kích hoạt (Trigger) |
❌ | Team |   ← "Team" = technical/org term, giữ nguyên
❌ | Ref |    ← abbreviation, giữ nguyên
```

### Quy tắc 6 — Nhãn Bullet (Bold label): Dịch + ngoặc Anh
Format: `**Tiếng Việt (English):**`

```
✅ - **Đăng nhập (Login):** CRM gửi thông tin xác thực...
✅ - **Đồng bộ (Sync — REST):** CRM gọi ECQS khi cache miss...
✅ - **Bất đồng bộ (Async — Kafka CDC):** ECQS phát hành...
✅ - **Hợp đồng (Contract):** CRM cam kết...
```

### Quy tắc 7 — Mermaid Diagram Labels: Giữ tiếng Anh
Trong Mermaid code blocks (` ```mermaid `), **tất cả labels phải bằng tiếng Anh**. KHÔNG dịch subgraph titles, node labels, hay edge labels sang tiếng Việt.

**Lý do:** Diagram là visual artifact kỹ thuật, người đọc cần nhận diện nhanh qua thuật ngữ chuẩn. Dịch VN trong diagram gây khó hiểu và mất tính nhất quán với code/API.

```
✅ subgraph input ["Input Sources"]
❌ subgraph input ["Đăng nhập"]        ← dịch SAI nghĩa (login ≠ input sources)

✅ subgraph core ["Team Operations"]
❌ subgraph core ["Thao tác Team"]     ← trộn VN/EN vụng

✅ subgraph output ["Downstream Systems"]
❌ subgraph output ["Hệ thống Tiêu thụ"] ← "tiêu thụ" nghe lạ trong context kỹ thuật
```

### Quy tắc 8 — ASCII Art / Non-Mermaid Diagrams: KHÔNG thay đổi
Giữ nguyên 100% nội dung trong code block diagram dạng text/ASCII. Chỉ dịch tiêu đề section bên ngoài.

### Quy tắc 9 — YAML Frontmatter: Dịch các value là câu văn
```yaml
# Giữ nguyên các key, dịch value nếu là câu mô tả
changelog: "v4.0 — C2: Làm rõ phạm vi Conformist."  ✅
type: context-map  ← giữ nguyên (identifier)         ✅
```

### Quy tắc 10 — Nội dung bảng body: Không lặp ngoặc
Nếu cột header đã giải thích (ví dụ `Loại phiên dịch`), các ô trong cột đó dùng tiếng Việt thuần, chỉ thêm ngoặc Anh ở **lần đầu xuất hiện loại đó**:

```
✅ | **Đổi tên (Rename)** | ← hàng 1, lần đầu
✅ | **Đổi tên + Ánh xạ mã (Rename + Code mapping)** | ← hàng 2, loại mới, lần đầu
✅ | **Đổi tên** | ← hàng 3, đã giới thiệu rồi, bỏ ngoặc
```

## Workflow Thực thi

```
1. ĐỌC file gốc toàn bộ trước khi bắt đầu dịch
2. XÁC ĐỊNH danh sách thuật ngữ DDD/tech trong file → đánh dấu "giữ nguyên"
   2b. XÁC ĐỊNH named concepts (capability/feature names) → đánh dấu "giữ nguyên"
       Hỏi: cụm từ này là TÊN GỌI hay MÔ TẢ? Nếu là tên gọi → giữ EN
3. SCAN các từ thông thường sẽ dịch → lập danh sách "lần đầu"
4. DỊCH theo thứ tự từ trên xuống:
   a. YAML frontmatter
   b. Heading (H1, H2, H3...)
   c. Bảng: header trước, body sau
   d. Prose + bullet points
   e. Blockquote
5. MERMAID BLOCKS: giữ nguyên tất cả labels bằng tiếng Anh (Quy tắc 7)
6. KHÔNG đụng vào: code blocks (```) trừ khi trong đó có prose giải thích
7. KIỂM TRA lại: tìm kiếm ngoặc "(English)" bị lặp → xóa lần thứ 2 trở đi
8. GHI FILE (overwrite)
```

## Checklist Trước Khi Hoàn Thành

- [ ] Tất cả heading có format `Tiếng Việt (English)`?
- [ ] Không có từ thông thường nào bị lặp ngoặc Anh quá 1 lần?
- [ ] DDD/tech terms giữ nguyên (không bị dịch nhầm)?
- [ ] **Capability/feature names giữ nguyên EN?** (Team Management, Member Assignment, Reason Tracking, v.v. — không dịch thành "Vòng đời nhóm", "Theo dõi lý do")
- [ ] **Lifecycle dùng đúng nghĩa?** Chỉ dùng cho state/role assignment transitions (VD: SalesTeam State Lifecycle, TeamLead Role Assignment Lifecycle), không dùng để đặt tên Event Group.
- [ ] **Mermaid labels giữ nguyên EN?** (subgraph titles, node labels, edge labels)
- [ ] Diagram/ASCII art không bị thay đổi?
- [ ] YAML frontmatter: key giữ nguyên, value câu văn đã dịch?
- [ ] Nhãn bullet bold có ngoặc Anh?
- [ ] Nội dung kỹ thuật không bị mất sau dịch?

## Ví dụ Tham Chiếu
File đã dịch chuẩn: `docs/context-map.md` (v4.0, dịch 2026-07-05)
