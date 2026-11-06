# Kết quả kiểm tra cập nhật CRM 1.3.0

Ngày: 03/11/2026. Agent triển khai thực hiện kiểm cấu trúc và walkthrough tài liệu. Đây không phải forward-test độc lập, pilot với member/authority thật hoặc kiểm hệ thống Jira/CI.

## Thay đổi đã kiểm

Bổ sung Feature F01–F08, policy register/template, loại requirement và ID/trace, mapping 16 Epic + 12 Story items, measurement/Feature roll-up, mẫu báo cáo và pilot procedure/record. Sửa bảng coverage trùng, bỏ heading rỗng nhưng giữ anchor lịch sử. Entry routes và hai trang điều hướng đã cập nhật; Task vẫn tùy chọn. Ngưỡng/severity/SLA/required-check values của dự án chưa được tự điền hay tự phê duyệt.

## Kiểm tự động

- Current package structure: PASS {"markdown_documents": 52, "manifest_entries": 98, "source_sections": 105}
- Portable copy: PASS
- Missing F08 detected: PASS
- Missing E07 mapping detected: PASS
- Broken model link detected: PASS
- Lost historical anchor detected: PASS
- Both navigation pages resolve: PASS
- Skill frontmatter/entrypoint qua `quick_validate.py`: đạt.
- `git diff --check`: đạt cho các thay đổi được theo dõi.
- Manifest/source archive: đủ 105 section nguồn và đúng hash; ZIP nguồn 1.1 không thay đổi.

## Walkthrough cập nhật

Đã đọc và đối chiếu các quy tắc sau với [acceptance scenarios](../references/pack-acceptance-scenarios.md). Kết luận “khớp” chỉ nói hướng dẫn có câu trả lời nhất quán cho tình huống; không nói một agent khác hay Jira đã chạy thành công.

| Scenario | Kết quả theo tài liệu | Evidence quy tắc | Kết luận |
|---|---|---|---|
| AT17 — Thiếu policy | Policy bắt buộc Pending chưa cho gate đạt; không tự đặt ngưỡng | [Policy](../references/project-policy-register.md), [gate](../references/readiness-completion-and-approval-gates.md) | Khớp |
| AT18 — Type/ID nhầm | BR là rule; REQ có type và applies_to; không ép NFR vào Epic | [ID/type](../references/requirement-types-identifiers-and-traceability.md) | Khớp |
| AT19 — Outcome chưa đo | Product acceptance khác benefit observation; ràng buộc hợp đồng/authority vẫn giữ | [Feature](../references/capability-specification-catalog.md) | Khớp |
| AT20 — E07 phụ thuộc state/API | D05/D02/D07 có trigger và evidence; Q01–Q07 không được miễn | [Mapping](../references/catalog-check-model-mapping.md) | Khớp |
| AT21 — Review coverage | 12/14 là coverage review; gap E05/E07 vẫn chặn, không là % sản phẩm | [Measurement](../references/progress-measurement-and-capability-rollup.md) | Khớp |
| AT22 — Mẫu số/unknown/change | Zero=N/A; unknown riêng; scope delta phải giải thích, không xóa mẫu số ngầm | [Measurement](../references/progress-measurement-and-capability-rollup.md) | Khớp |
| AT23 — Task/cancel | Shared Task tính một lần; cancel không tự loại requirement khỏi scope | [Roll-up](../references/progress-measurement-and-capability-rollup.md) | Khớp |
| AT24 — SLA | Chưa có ngưỡng chỉ báo age/clock; quá hạn không tự approval | [Policy](../references/project-policy-register.md), [report template](../assets/templates/progress-report-template.md) | Khớp |
| AT25 — Chưa pilot | Hướng dẫn và mẫu không là evidence đã thử thật; phạm vi chưa kiểm được ghi riêng | [Pilot](../references/pilot-and-operational-validation.md) | Khớp |

Regression walkthrough: AT01 (Story không Task), AT04 (baseline một phần), AT06 (Task Done không bằng Story Done), AT12 (state matrix đầy nhưng còn unknown) vẫn giữ điều kiện cũ; bổ sung policy/Feature không thay các nguyên tắc này. Các kiểm tra lịch sử khác xem [report 1.2](pack-validation-report.md); không ghi nhận lại như đã chạy mới toàn bộ.

## Phần còn cần dữ liệu dự án thật

Chưa tạo Project Policy Register đã được authority phê duyệt trong repo CRM, chưa pilot Epic/Story thật, chưa khảo sát/cấu hình tenant Jira/Git/CI và chưa cài skill vào runtime. Không có business acceptance, QA runtime Pass hoặc số liệu lợi ích/tiến độ thực tế được tạo bởi lần cập nhật này. Các ngưỡng chưa biết được thể hiện là quyết định cần chốt, không phải giá trị mặc định.

## Kiểm hiệu chỉnh 1.3.1 — 03/11/2026

- Chuẩn hóa ID/path trong ví dụ theo PREFIX-CRM-NNN; không còn các ID cũ cụ thể trong references/templates. Jira keys và snapshot nguồn không đổi.
- Đối chiếu refs MOD/AC trong ví dụ submit với bảng định nghĩa và refs transition của ví dụ finding: đạt. Logical paths của manifest và walkthrough minh họa khớp nhau.
- Checklist Critical/Major có ref trực tiếp POL-SEVERITY và POL-QUALITY; yêu cầu ref/version/approval dự án vẫn giữ. Required checks có POL-CHECKS/POL-QUALITY.
- Validator gói: đạt (52 Markdown, 98 entries, 105 section nguồn); quick_validate: đạt. Link/anchor policy mới resolve.
- Đây là kiểm biên tập và cấu trúc; không bổ sung pilot/approval dự án hay runtime evidence.
