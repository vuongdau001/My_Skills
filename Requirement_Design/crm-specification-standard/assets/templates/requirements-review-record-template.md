# Mẫu bản ghi review

Mã tài liệu: **TPL-REQUIREMENTS-REVIEW-RECORD-TEMPLATE** · Gói CRM 1.2.0 · 02/11/2026

**Mục đích:** Sao chép phần mẫu để tạo hồ sơ thực tế; không để trống rồi đánh dấu đạt.

**Đọc khi:** Sau khi đọc catalog và các hướng dẫn áp dụng.


<a id="spec-3-13"></a>

### Mẫu record review để member thực hiện nhất quán

```text
Review target / selected scope / input revision:
Nguồn/actor/authority đã rà:
Model/requirement inventory version:
Check IDs: Q01..Q07 và D01..D10 áp dụng
Item ID / source ref / output ref:
Thao tác kiểm đã làm / witness hoặc counterexample:
Expected outcome / actual finding trong tài liệu:
Verdict: Đạt | Không đạt | Chưa kiểm | N/A có lý do
Finding ID / severity theo mức chặn / owner / due:
Decision/correction ref / reviewer closure / reviewed revision:
Inventory counts: total / disposed / unknown / missing verification mapping
Gate impact: cho bước nào, phần nào còn bị chặn
```

**Phân biệt kết quả tài liệu với kết quả phần mềm:** trước code, reviewer ghi đối chiếu spec/model, không ghi test runtime Pass. Sau code, test reports/build/verdict là evidence khác. Mọi agent dùng gói này phải giữ ranh giới này; skill không được biến review checklist thành bằng chứng sản phẩm đã hoạt động.


## Bảng kết luận dùng được cho review toàn bộ hoặc một phần

| Target/revision | Check/model ID + tên | Applicability | Inventory/witness | Phép kiểm đã thực hiện | Finding/evidence | Verdict | Reviewer/authority | Gate impact |
|---|---|---|---|---|---|---|---|---|
| Phạm vi cụ thể | Tên rõ, không chỉ số | Áp dụng/N/A + reason | ID và mẫu số | Thao tác thực tế | Ref/version | Chưa kiểm/Không đạt/Đạt/N/A | Người xác nhận | Bước nào còn chặn |

Full hay targeted review; phần chưa xét; summary findings; source conflicts; closure revision; PM decision khi cần. Verdict có giá trị cho target/revision đã xét, không tái sử dụng tự động sau delta. [Quy trình review](../../references/requirements-review-process-and-verdicts.md).


---

**Liên quan:** [Điểm vào gói](../../SKILL.md) · [Review và verdict](../../references/requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](../../references/standards-and-crm-tailoring.md).
