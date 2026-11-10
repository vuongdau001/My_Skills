---
description: Protocol chạy validation sau mỗi artifact — trỏ về bộ rule chuẩn của ddd-validator
version: 2.0
---

# Validation Protocol — Chạy sau mỗi artifact creation

> Bộ rule duy nhất là **`ddd-validator`** (49 rules: 39 quality + 10 structural/cross-BC). File này KHÔNG định nghĩa rule riêng để tránh drift.
> Các rule cũ V1-V7 đã được merge: V1→G4, V2→E3, V3→C1, V4→E4, V6→G3; V5, V7 giữ nguyên trong `ddd-validator/rules/structural.md`.

## Mapping artifact → rule file (incremental, Phase 3)

| Sau khi tạo/sửa... | Load | Rules |
|:--|:--|:--|
| Domain Map / Priority Matrix | `ddd-validator/rules/strategic-design.md` | S1-S4 |
| Glossary file | `ddd-validator/rules/glossary.md` | G1-G11 |
| Event Storm (aggregate-*.md) | `ddd-validator/rules/event-storm.md` + `aggregate-design.md` | E1-E11 + A1-A4 |
| Context Map | `ddd-validator/rules/context-map.md` | C1-C6 |
| ADR | `ddd-validator/rules/adr.md` | R1-R2 |
| Shared Kernel / Big Picture ES | `ddd-validator/rules/structural.md` | XB-1→XB-3 |

## Execution Protocol
```
Sau mỗi artifact creation:
  1. Chạy đúng rule file theo bảng trên (KHÔNG load toàn bộ)
  2. 🔴 blocking fail → STOP, fix trước khi tiến tiếp
  3. 🟠 degrading → ghi Action Item P1, cho qua, fix trước Phase 5
  4. 🟡 cosmetic → ghi Action Item P2
  5. Phase 4: full gate → validation/validation-report.md (template trong ddd-validator)
```
