---
description: Pre-flight checklist trước mỗi task trong DDD pipeline
version: 2.0
---

# Pre-Flight Checklist

Agent PHẢI kiểm tra trước mỗi task:

## State Check
1. **Project State:** Đọc `project-state.md` — dự án đang ở Phase nào (0-7)? Gate gần nhất đã pass là gate nào? (format: `.agents/skills/_shared/references/gates-and-project-state.md`)
2. **Artifacts Inventory:** Artifacts nào đã tồn tại trong `docs/`, `mapping/`, `backlog/`?
3. **Pending Questions:** Có câu hỏi P0 / LATE-P0 nào chưa được trả lời trong `clarification/`?

## Phase Gate
4. **Phase Dependency:** Phase hiện tại đã hoàn thành + gate tương ứng (G1-G6) đã Approve chưa? Nếu chưa → không chuyển phase.
5. **P0 Blocker:** Nếu còn P0 question chưa answered → KHÔNG tạo artifacts mới (Phase 3 blocked).

## Skill Selection
6. **Task → Skill mapping:**
   - Nhận/phân tích tài liệu (SRS, BRD, MoM, RFP, API doc, DB schema) → `ddd-discovery`
   - Đặt câu hỏi / ghi Late Discovery → `ddd-questioner`
   - Tạo / sửa DDD artifact → `ddd-modeler`
   - Kiểm tra chất lượng artifact → `ddd-validator`
   - Tạo deliverable (BRD, Technical Overview, Onboarding) → `ddd-documenter`
   - Mapping mockup ↔ Command/Query → `ui-ddd-mapping`
   - Kiểm field/action/state của mockup, sinh UI AC → `ui-contract-reviewer`
   - Tạo backlog / đối chiếu tiến độ code → `ddd-backlog-planner`
   - Vẽ diagram → `mermaid-diagram` · Dịch tài liệu EN→VI → `doc-translate`

## Safety
7. **Extract vs Infer:** Mọi thông tin inferred phải tag `[INFERRED]` và đưa vào clarification queue.
8. **No overwrite:** Không ghi đè artifact đã có mà không hỏi user.
