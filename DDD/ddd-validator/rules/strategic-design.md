---
category: Strategic Design
rules: S1-S4
applies_to: [docs/domain-map.md, docs/domain-priority.md]
sources: [Lesson 3.1, Lesson 3.2, Evans Blue Book Ch.1]
---
# Strategic Design Rules (S1-S4)

### S1: Core Domain ≤ 3
- **Nguồn:** Lesson 3.1 — *"Công ty chỉ có ≤3 Core Domains. Core = thứ tạo lợi thế cạnh tranh"*
- **Tại sao:** Nếu >3 → phân tán resource → thua. *"Nếu mọi thứ đều Core → không gì Core"*
- **Checklist:**
  - [ ] Đếm domains đánh dấu 🔴 Core ≤ 3?
  - [ ] Core domain vượt qua Copy Test? ("Đối thủ copy → mất lợi thế?")
  - [ ] Core domain vượt qua Competitive Test? ("10× tốt hơn → khách chọn?")

### S2: Classification dựa trên Business Strategy, không Complexity
- **Nguồn:** Lesson 3.1 — *"Core Domain không phải kỹ thuật quyết định — chiến lược kinh doanh quyết định"*
- **Tại sao:** Domain phức tạp ≠ Core. Auth phức tạp nhưng là Generic. Classify theo complexity → đầu tư sai.
- **Checklist:**
  - [ ] Domain Map có column "Strategic Value" hoặc "Business Differentiation"?
  - [ ] Core domain gắn với competitive advantage hoặc downstream dependency, không chỉ "nhiều BRs"?

### S3: Investment Strategy khác biệt theo Classification
- **Nguồn:** Lesson 3.1 — *"Core → Build in-house, đội giỏi nhất; Supporting → Buy+Customize; Generic → Buy SaaS"*
- **Tại sao:** Build in-house cho Generic = 80% effort cho non-Core → Core chậm.
- **Checklist:**
  - [ ] Core = "Build in-house"?
  - [ ] Supporting = "Build pragmatic / Leverage existing"?
  - [ ] Generic = "Use framework / Buy SaaS"?

### S4: Priority Matrix có tiêu chí Objective
- **Nguồn:** Lesson 3.2 — *"Module đau nhất deploy trước"*
- **Tại sao:** Score subjective → bias → đầu tư sai domain.
- **Checklist:**
  - [ ] Scoring Rubric defined (1=?, 3=?, 5=?)?
  - [ ] Mỗi cell có evidence link (SRS, pain-points)?
  - [ ] Total score dẫn đến classification hợp lý?
