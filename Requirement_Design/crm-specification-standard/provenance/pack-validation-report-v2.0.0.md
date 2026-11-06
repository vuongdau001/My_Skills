# Kiểm chứng CRM Workflow Kit 2.0.0

| Thông tin | Giá trị |
|---|---|
| Phạm vi | Kit nguồn và kiểm thử phát hành trên repo tạm |
| Nhánh local | `codex/crm-spec-kit-v2`, tạo từ `8102405` (1.12.3) |
| Phiên bản nguồn | 2.0.0, policy Epic `use-case-v1`, cấp Capability |
| Ngày kiểm | 06/11/2026 |

## Kết quả kiểm thử

| Phép kiểm | Kết quả |
|---|---|
| Validator package | Đạt. 116 tài liệu Markdown, 169 mục registry, 105 mục nguồn lịch sử, 5 profiles và 13 workflow functions |
| Unit/integration suite | 172 test đạt. Bao gồm Capability/CAP/C01–C08, intake khai báo, từ chối tên cũ, Epic policy, locator E03, duplicate xuyên workstream, Story/Prototype stale, assessment Epic legacy và workflow context |
| Cài mới trên repo tạm | Dry-run và apply đạt. Doctor đạt với receipt 2.0.0. Scaffold tạo `01-capabilities`. Bản cài cấp `CAP-CRM-001`, nạp đúng context và scoring tạo C01–C08 |
| Intake từ bản cài | Setup Project và Define Capability trực tiếp trả cùng inventory. Candidate từ source giữ trạng thái khai báo và tách khỏi hồ sơ đã đăng ký. Hash nguồn giữ nguyên |
| Epic gate fixture | Epic legacy bị chặn khi trình readiness. Sau khi thêm đặc tả và binding minh họa, lint readiness cấu trúc đạt. Context nạp policy, D01 và mẫu Epic |
| Update/khôi phục package | Suite kiểm dry-run, swap, drift, backup và rollback khi lỗi trên repo tạm. Phương án phát hành Capability dùng cài mới trên workstream sạch |
| Soát ví dụ theo tình huống | List/Form/Receipt chung một mục tiêu gửi. Gửi và xét duyệt là hai Epic. Approve/Reject cùng Use Case xét duyệt. Task dùng chung có owner/consumers. Hai đợt minh họa giữ cặp ID và evidence theo baseline. Fixture bỏ expected result vẫn qua lint cấu trúc, bài tập review yêu cầu finding E03/E14 |

## Phạm vi CRM

Lần đối chiếu trước khi đổi tên Capability nhận diện một Epic đang mở, `EPIC-CRM-002` revision `p3-prototype-intake-r1`. Artifact và bản cài CRM giữ nguyên trong lượt làm kit. Discovery trong phiên mới, walkthrough của p3 và approval nghiệp vụ chưa được xác minh.

## Tái chạy

```sh
python3 -B scripts/validate_reference_pack.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts/tests -v
```

[Policy Epic–Use Case](../references/epic-use-case-policy.md) · [Cài mới](../INSTALL.md) · [Tái dùng hồ sơ đầu vào](../references/knowledge-records-and-evidence.md#tái-dùng-hồ-sơ-từ-đầu-vào)
