# 02 — Mechanism primitives (mô phỏng, không trình chiếu)

File: `templates/remotion-project/src/primitives/Mechanism.tsx`. Ví dụ đầy đủ: `src/scenes/stages.tsx`.

## Vì sao

Brief gốc: *"Không làm video kiểu slide PowerPoint… Request và response di chuyển theo đúng thứ tự xử lý…
người xem hiểu cơ chế kể cả khi không có voice-over."* Một lưới thẻ chữ hiện lần lượt **không** đạt yêu cầu này.
Dự án auth (Tập 1 + Tập 2) đã chuyển toàn bộ real/tech sang mô phỏng; summary dùng danh sách hiện dần (cho phép).
Quy tắc bố cục đã kiểm chứng khi QA frame: nhãn node nằm dưới icon (~y+100), nên verdict/chip không đặt trong dải y+40..y+110
của node; chip "vật đang giữ" đặt ≥ y+170 hoặc phía trên node; packet đích đến node dùng x-80 (cạnh node) thay vì tâm;
verdict liên tiếp cùng vị trí phải có `until` trước khi cái sau hiện; chip cố định không được nằm ngang hàng verdict (lệch x).

## Canvas

`<MechStage>`: khung cố định **912 × 880** đặt giữa sân khấu. Mọi primitive dùng toạ độ tuyệt đối trong khung này.
Bố cục đã kiểm chứng (Session): 2 node trên cùng ở y=200 (x=170 và x=742), kho dữ liệu dưới node phải (top=500),
verdict ở giữa (456, 370), ghi chú cuối ở (456, 770). Giữ mọi thứ trong 0..912 (chip rộng ~400px: đặt tâm ≥ 220 và ≤ 690).

## Primitives

| Component | Dùng cho | Props chính |
|---|---|---|
| `MNode` | Tác nhân/hệ thống (Khách, Lễ tân, Browser, Server) | `x, y, icon, label, color, at, active` |
| `MLink` | Đường nối, tự vẽ ra; `glowFrom` để nhấn mạnh (VD "tra store mỗi lần") | `from, to, color, at, glowFrom, glowUntil` |
| `MPacket` | **Request/response/dữ liệu di chuyển** A→B | `from, to, start, end, label, color, icon, mono` |
| `MChip` | Vật được lưu lại (cookie trong browser, thẻ trong tay khách); `struck` khi bị vô hiệu | `x, y, at, until, label, struck` |
| `MStore` | Sổ / Database / Session Store: dòng được **ghi** (`at`) và **gạch** (`strikeAt`) | `rows: [{text, at, strikeAt}]` |
| `MVerdict` | Kết quả ✔/✖ ("Xin chào, An", "401 · Đã đăng xuất") | `x, y, ok, label, at, until` |

Helpers: `usePop(f, at)` (spring), `ease(f, a, b)`, `windowOpacity(f, from, until)`.

## Đồng bộ với lời đọc

Mọi mốc thời gian lấy từ `T(cueIdx, frac)`: frame trong beat tại `frac` (0..1) của cue đó.
Chia mỗi cue thành các nhịp theo **đúng thứ tự xử lý thật**:

```tsx
// cue 0: "Sổ khách là Session Store; thẻ khách là Cookie chứa Session ID."
<MPacket start={T(0, 0)}    end={T(0, 0.22)} label="Đăng nhập" ... />               // 1. request
<MStore rows={[{ text: '9f3a7c… → an', at: T(0, 0.3), strikeAt: T(2, 0) }]} ... />  // 2. server ghi phiên
<MPacket start={T(0, 0.45)} end={T(0, 0.75)} label="Set-Cookie: sid=…" ... />       // 3. response
<MChip   at={T(0, 0.75)} label="sid=9f3a7c…" ... />                                 // 4. browser lưu cookie
```

Quy tắc:
- Một thời điểm chỉ có **1 gói tin đang bay** (dễ theo dõi trên điện thoại).
- Gói tin đi trên đường nối: lệch `±34px` theo trục y để chiều đi và chiều về không đè nhau.
- Verdict cũ phải có `until` trước khi verdict mới hiện.
- Pha `real` dùng cùng primitives nhưng icon/nhãn đời thường (UserRound, Landmark, BookOpen, Ticket, IdCard).

## Khi nào được dùng `StageCard`

Chỉ cho bridge, outro, summary, nơi nội dung là *khái niệm/tóm tắt* chứ không phải *quá trình*.
