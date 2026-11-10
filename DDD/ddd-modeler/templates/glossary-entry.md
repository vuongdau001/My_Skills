# Template: Glossary Entry

**File:** `docs/bounded-contexts/<bc-name>/glossary/<term>.md` — ATOMIC: 1 file per term

```markdown
---
term: "[Term]"
contexts: ["Context1"]
type: entity | aggregate-root | value-object | enum | status | role | role-variant | process | mechanism | constraint | domain-service   # đồng bộ rule G2
conflict_severity: 🔴 | 🟠 | 🟡 | ⚪
source: "[SRS §X.Y]"
aliases: []                          # Mỗi alias PHẢI kèm [VERIFIED: src1, src2] hoặc [UNVERIFIED]
values_count:                        # BẮT BUỘC cho type: enum có liệt kê values
---
# [Term]

## Định nghĩa (Definition)
[Ý nghĩa chính xác của khái niệm trong Bounded Context này — ≤ 2 câu]

## Bounded Context
**[BC Name]**

## Thuộc tính quyết định (Key Attributes)
<!-- CHỈ identity-defining OR business-behavior-changing. Omit section nếu không cần. -->

| Thuộc tính | Vai trò nghiệp vụ |
|:--|:--|
| [attr] | [Identity / Lifecycle / Invariant / …] |

## Quy tắc Nghiệp vụ (Business Rules)
1. …

## Vòng đời (States/Lifecycle)
<!-- nếu có -->

## Phân biệt với Các Khái niệm Liên quan (Disambiguation)
| Hay bị nhầm | Khác ở đâu |
|:--|:--|
| … | … |

## Từ nguy hiểm cần tránh (Dangerous Terms) ⚠️
| ❌ Không dùng | Lý do |
|:--|:--|
| … | … |

## Câu hỏi mở (Open Questions) ❓
<!-- nếu có -->
```

> Glossary = Ubiquitous Language. Không liệt kê full schema/UI fields. Chi tiết section theo rule G1 — `ddd-validator/rules/glossary.md`.
