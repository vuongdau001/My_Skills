# Status Jira và tiến độ phân tích, triển khai

Mã tài liệu: **CRM-TRACKING** · Gói CRM 1.3.1 · 03/11/2026

**Mục đích:** Tách trạng thái Jira khỏi readiness và kết quả nghiệm thu.

**Đọc khi:** Cập nhật công việc, xem blocker hoặc báo cáo tiến độ.


<a id="workflow-11"></a>

## Ý nghĩa từng status Jira và quy tắc chuyển


<a id="workflow-11-1"></a>

### Epic

| Status | Ý nghĩa | Điều kiện chính |
|---|---|---|
| `todo` | Đã được phép ghi nhận phạm vi, chưa bắt đầu làm rõ/thực hiện | Có Capability refs, scope sơ bộ và owner |
| `inprogress` | Đang phân tích, thiết kế, triển khai hoặc kiểm chứng | DoR bắt đầu Epic đạt; các Task/Story cho biết đang ở phần nào |
| `done` | Đã nghiệm thu phạm vi baseline được định danh của Epic | Đạt DoD Epic tại mục [DoD để đóng Epic: `inprogress` → `done`](readiness-completion-and-approval-gates.md#workflow-8-4) |
| `cancel` | Không tiếp tục phạm vi Epic theo quyết định | Có authority/reason và đánh giá tác động tới Capability |

Epic không có `pending`: giữ `inprogress` và ghi blocker/owner/due trên Epic; Task/Story bị chặn dùng `pending`. Epic bị chặn không được kéo sang `done` hoặc `cancel` chỉ để khỏi hiện việc tồn.


<a id="workflow-11-2"></a>

### Story

| Status | Ý nghĩa |
|---|---|
| `todo` | Đã tạo từ baseline hợp lệ; chưa triển khai, có thể chưa đạt DoR |
| `inprogress` | Đang code, viết test, review code, xử lý CI hoặc sửa lỗi |
| `pending` | Bị chặn bởi điều kiện cụ thể; có reason, owner, next action và thời điểm chờ |
| `resolved` | Dev đã bàn giao hợp lệ; đang/chờ QA, xử lý kết luận hoặc chờ PM chốt sau QA Pass |
| `done` | Đạt toàn bộ DoD Story |
| `cancel` | Quyết định không triển khai tiếp, không được coi là hoàn thành requirement |

Luồng thông thường:

```text
todo --DoR đạt--> inprogress --Dev bàn giao đạt--> resolved --DoD đạt--> done
                                    ^               |
                                    +-- cần sửa ----+
```


<a id="workflow-11-3"></a>

### Task

| Status | Ý nghĩa |
|---|---|
| `todo` | Đã giao công việc, chưa bắt đầu |
| `inprogress` | Owner đang tạo đầu ra |
| `review` | Có đầu ra, reviewer đang/chờ kiểm tra |
| `pending` | Bị chặn; có người theo dõi và hành động tiếp theo |
| `resolved` | Review chuyên môn đã đạt, còn một điều kiện bàn giao/xác nhận cuối cụ thể |
| `done` | Đạt DoD Task, người nhận đã xác nhận |
| `cancel` | Dừng công việc theo quyết định hợp lệ |

Luồng thông thường:

```text
todo --DoR đạt--> inprogress --> review --> resolved --> done
                       ^           |
                       +-- sửa ----+
```

Nếu review đã đồng thời đáp ứng DoD và người nhận xác nhận, có thể đi `review → done` khi transition cho phép. Không bắt đi qua `resolved` nếu không có điều kiện chờ thực tế.


<a id="workflow-11-4"></a>

### Dùng `pending`, trả sửa và `cancel`

- `pending` dành cho bị chặn; không dùng thay mọi hàng đợi thông thường. Task chờ review dùng `review`; Story chờ QA/PM sau bàn giao dùng `resolved`.
- Ghi status trước khi bị chặn và điều kiện resume. Khi có quyết định mới, quay về trạng thái phù hợp; đổi rule cần code lại thì về `inprogress`, không quay thẳng `done`.
- Review/test không đạt mà owner có thể sửa ngay: quay `inprogress`; không tự coi mọi rework là blocker.
- `cancel` cần authority/reason và tác động tới scope/estimate/child. Hủy child không tự loại requirement khỏi scope.
- Mở lại Epic/Story đã Done theo workflow cho phép sau khi change được chấp nhận. Với cùng mục tiêu, giữ Epic ID và các anchor E03 còn cùng nghĩa, ghi scope/revision/baseline mới và pin nghiệm thu cũ. Review phần chịu tác động và ghi lý do tái dùng evidence. [Vòng đời Epic](epic-use-case-policy.md).


<a id="workflow-11-5"></a>

### Status `resolved` khác trường Resolution của Jira

Jira còn có trường Resolution, có thể ảnh hưởng báo cáo “đã giải quyết”. Cần kiểm tra category của status, post-functions và cách set/clear Resolution trong workflow thực tế. Với quy ước của tài liệu này, `resolved` chưa được tính Story Done.

Chưa kiểm tra tenant nên tài liệu không khẳng định chỉ đổi cách gọi là báo cáo/hook sẽ tự hoạt động đúng.


<a id="workflow-15"></a>

## Theo dõi Requirement Backlog và Development Backlog


<a id="workflow-15-1"></a>

### Requirement Backlog

Quản lý bằng hồ sơ Capability và Jira Epic, với bảng readiness các hạng mục; không dùng số Task phân tích đã đóng để đo độ rõ requirement. Báo cáo phải cho thấy:

- Capability/Epic nào đã có người làm rõ, ai quyết định nghiệp vụ.
- Requirement/AC đang làm rõ, chờ review hay đã được xác nhận; owner và hạn.
- Solution đang phân tích, chờ review hay đã được xác nhận; owner và hạn.
- QA đã xác nhận testability chưa.
- Câu hỏi/dependency chặn đang chờ ai và bao lâu.
- Phần scope nào đã có baseline yêu cầu + solution hợp lệ; phần nào còn mở.
- PM đã duyệt tạo những Story nào và thực tế tạo được những ticket nào.

Không cần thêm S1/S2/S3 thành Jira status. Độ rõ requirement được xác định từ output, reviewer và baseline evidence, không từ cảm nhận rằng Epic “đã được 70%”.

| Hạng mục trên Epic | Owner | Tín hiệu tiến độ | Đầu ra / xác nhận | Hạn / blocker |
|---|---|---|---|---|
| Requirement và AC | BA | Chưa làm / Đang làm / Chờ review / Đã xác nhận | Spec, decision refs và Business/BA review | Người xử lý và hạn |
| Solution | Dev | Chưa làm / Đang làm / Chờ review / Đã xác nhận | Solution/contract refs và technical review | Người xử lý và hạn |
| Testability | QA | Chưa làm / Đang làm / Chờ review / Đã xác nhận | Coverage/matrix sơ bộ và QA review | Người xử lý và hạn |
| Baseline bàn giao | BA/PM | Chưa trình / Đang review / Đã merge | PR, PM decision và commit/manifest | Người xử lý và hạn |

Các tín hiệu trên là metadata/checklist readiness, không phải Jira status mới. Nếu không có custom field, dùng section thống nhất trong Epic. “Đã xác nhận” phải có người/revision/evidence; Epic vẫn `inprogress` cho đến nghiệm thu. Phần chuẩn đã chốt nằm trong Git; Jira giữ các tín hiệu tiến độ động.


<a id="workflow-15-2"></a>

### Development Backlog

Theo dõi Story và Task triển khai qua các status đã có:

- `todo`: tách đạt/chưa đạt DoR bằng readiness evidence.
- `inprogress`: workload coding/review/CI và remaining effort.
- `pending`: blocker/owner/age/next action.
- `resolved`: Dev đã bàn giao; phân biệt đang QA, chờ retest hoặc chờ PM closure trong thông tin công việc, không tạo thêm status.
- `done`: đủ DoD; không tính `resolved` là Story Done.
- `cancel`: theo dõi riêng, không cộng vào hoàn thành phạm vi.

Capability không có ticket Jira: tài liệu Git giữ scope, rule, Epic links và baseline refs; dashboard/report tổng hợp trạng thái triển khai bằng cách đọc Jira. Không nhập lại thủ công mọi trạng thái Jira vào tài liệu Git.

Ready buffer phải xét effort/capacity theo từng vai trò và dependency; không cộng BA + Dev + QA effort rồi chia riêng capacity Dev. Chưa có capacity thì không gọi là sẵn sàng triển khai.


## Không đếm lặp tiến độ

Story là đơn vị kết quả bàn giao. Task của Story giúp thấy owner, blocker và remaining work; không cộng cả effort/points đã tổng hợp ở Story và chính các Task đó lần nữa. Nếu đo effort ở Task thì Story roll-up từ phần đó, chỉ thêm effort chưa phân bổ có nhãn rõ. Task dùng chung được tính một lần, với dependency tới các Story sử dụng.

Requirement/solution progress được theo dõi bằng output, owner, due, reviewed revision, finding và baseline scope trên Epic. Không tạo Task giả để thay readiness. Epic vẫn `inprogress` sau khi baseline được duyệt. Requirement thực sự đổi sau baseline phải cập nhật Git; comment Jira không tự thay bản chuẩn.

Báo cáo hai chiều: (1) Requirement/solution/testability đang soạn, review, baseline; (2) Story đang dev, bàn giao QA, Done, với Task/blocker liên quan. `resolved` chưa được cộng vào Story Done; `cancel` không phải phạm vi đã bàn giao. Chưa khảo sát tenant nên chưa khẳng định báo cáo Jira đã dùng đúng status category/Resolution.


## Quy tắc đo và mẫu báo cáo

[Đo tiến độ và tổng hợp lên Capability](progress-measurement-and-capability-rollup.md) định nghĩa scope units, review coverage, baseline coverage, delivery, aging và acceptance, gồm unknown/zero denominator/cancel/change scope. Dùng [mẫu báo cáo](../assets/templates/progress-report-template.md). Bốn dòng readiness tổng hợp ở trên phải truy xuống từng E/S item có ID/tên/revision/evidence; không coi nó là toàn bộ dữ liệu review. Ngưỡng SLA/aging theo [policy register](project-policy-register.md), chưa chốt thì chỉ báo age, không tự gán vi phạm.


---

**Liên quan:** [Điểm vào gói](../SKILL.md) · [Review và verdict](requirements-review-process-and-verdicts.md) · [Nguồn và cách điều chỉnh](standards-and-crm-tailoring.md).
