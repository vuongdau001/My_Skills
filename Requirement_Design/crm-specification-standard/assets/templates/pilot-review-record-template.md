# Mẫu ghi nhận pilot và quyết định áp dụng

Mã tài liệu: **TPL-PILOT** · Gói CRM 1.3.1 · 03/11/2026

Đọc [pilot procedure](../../references/pilot-and-operational-validation.md). Đây là mẫu; mọi kết quả chưa có evidence giữ Chưa kiểm.

Pilot ID/date; mục tiêu và bước được kiểm; Feature/Epic/Story refs; selected scope/revision; nguồn/authority; participants/roles; policy refs/versions; quyền thao tác được cấp; môi trường thực hay bản sao; phần không kiểm.

| Scenario/bước | Input/version | Người thực hiện/reviewer | Expected decision + rule ref | Observed action/decision | Evidence | Verdict/finding | Correction/retest |
|---|---|---|---|---|---|---|---|
| Trường hợp thực tế | Context đúng version | Không giả authority | Tiêu chí trước khi thử | Chưa kiểm nếu chưa làm | Ref thật | Đạt/Không đạt/Chưa kiểm/N/A reason | Owner/due |

Dữ liệu quan sát: thời gian tìm context/review, câu hỏi do thiếu input, rework, bước lặp; nguồn đo và clock. Ngưỡng chưa được chốt không tự biến thành SLA.

Kết luận PM/authority: bước nào đủ evidence, scope/version áp dụng, findings chặn, phần chưa kiểm, corrections/owners/due và phạm vi cần thử lại. Pilot hồ sơ không đồng nghĩa hook Jira/CI đã được kiểm; Story Done cần evidence sản phẩm riêng.
