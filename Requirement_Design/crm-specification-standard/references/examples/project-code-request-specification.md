# Ví dụ đặc tả yêu cầu mở mã dự án

Mã tài liệu **EX-PROJECT-CODE** · CRM Workflow Kit 2.0.0

Ví dụ đào tạo giả định. Các quyết định, mốc nghiệm thu và evidence minh họa dưới đây dùng để tập review.

## Từ nguồn đến quyết định BA

**Nguồn EX-SRC-PC r1.** “Người đề nghị mở mã điền thông tin, lưu nháp và gửi để người được phân công xét duyệt. Người xét có thể chấp thuận hoặc từ chối. Cần xử lý bấm gửi lại khi mạng chập chờn.” Chức năng cấp mã thật thuộc hệ thống lân cận.

| Câu hỏi BA | Quyết định minh họa |
|---|---|
| EX-Q1. Người đề nghị nhận kết quả gì khi gửi? | EX-D1. Cùng request ID chuyển PendingApproval, xuất hiện trong hàng đợi Approver, có audit và một ý định thông báo. Tạo nháp để hoàn thành việc gửi thuộc cùng mục tiêu trong ví dụ. |
| EX-Q2. Ai được gửi và ai được xét? | EX-D2. Requester có quyền và sở hữu draft. Approver được phân công, khác creator. Reject cần lý do. |
| EX-Q3. Hai lần gửi hoặc lỗi giữa chừng xử lý thế nào? | EX-D3. Chỉ một lần chuyển state. Cùng key và payload trong cửa sổ 24 giờ trả kết quả cũ nếu còn quyền. Lỗi trước commit không ghi một phần. Sau commit, worker gửi nền và có thể retry độc lập. |
| EX-Q4. Hủy có phải mục tiêu riêng? | EX-D4. Đóng một draft đã lưu để dừng đề nghị là mục tiêu riêng của Requester. Đóng màn hình khi đang chuẩn bị gửi chỉ là nhánh hủy thao tác. |

### Phân bổ dưới Capability Quản lý Project Code

| Epic / Use Case | Actor và kết quả | Quan hệ |
|---|---|---|
| EPIC-CRM-001 · Gửi yêu cầu mở mã dự án để chờ duyệt | Requester đưa request hợp lệ vào PendingApproval | Hồ sơ E01–E16 bên dưới |
| EPIC-CRM-002 · Xét duyệt yêu cầu mở mã dự án | Approver ghi một quyết định Approved hoặc Rejected | Nhận request PendingApproval từ Epic gửi |
| EPIC-CRM-003 · Đóng yêu cầu nháp không còn cần | Requester đánh dấu draft Cancelled để dừng xử lý | Dùng chung lifecycle và quyền sở hữu |

Capability giữ hành trình gửi → xét duyệt → chuyển giao cho nơi cấp mã. Một Epic kỹ thuật “xây worker thông báo” được phân bổ thành Task dưới Epic gửi, có links đến Story submit và Epic xét duyệt nếu chúng dùng đầu ra. Chia theo nút Lưu/Gửi hoặc màn hình List/Form chia nhỏ một mục tiêu. Gom gửi và xét duyệt vì cùng entity làm mất ranh giới trách nhiệm. Approve và Reject là hai kết cục của mục tiêu xét duyệt trong ví dụ này.

### Shared model ProjectCodeRequest r1

| ID | Command | Guard | Outcome khi hợp lệ |
|---|---|---|---|
| MOD-CRM-001 | Submit | Draft, owner có quyền, dữ liệu đúng, version hiện hành | PendingApproval, tăng version, ghi audit và notification intent |
| MOD-CRM-002 | Approve | PendingApproval, assigned Approver khác creator, version hiện hành | Approved, tăng version, audit decision |
| MOD-CRM-003 | Reject | Guard xét duyệt như Approve, có lý do | Rejected, tăng version, audit decision |
| MOD-CRM-004 | Cancel draft | Draft, owner có quyền, version hiện hành | Cancelled, tăng version, audit decision |

State gồm Draft, PendingApproval, Approved, Rejected và Cancelled. Với operation mới, mọi cặp state–command ngoài bảng bị từ chối và giữ dữ liệu. Replay submit đã commit là truy kết quả của cùng operation sau khi kiểm quyền hiện tại. Ba Epic dẫn shared model r1 cùng EX-D2 cho ownership/segregation of duties.

## E01 Mục tiêu và phạm vi

**EPIC-CRM-001 · Gửi yêu cầu mở mã dự án để chờ duyệt.** Requester muốn đưa đề nghị hợp lệ vào hàng đợi để Approver có thể xử lý. Hệ thống quản lý draft, quyền, submit, hàng đợi và notification intent. Người đề nghị, Approver và kênh gửi thông báo nằm ngoài boundary nghiệp vụ của hệ thống.

Use Case ở cấp user-goal bao gồm chuẩn bị/mở draft, gửi, sửa dữ liệu, xử lý từ chối và phục hồi. Đợt r1 bàn giao các đường đi submit qua màn hình và đọc receipt trong CRM, gồm bảo đảm durable intent. Duyệt, đóng draft và cấp mã nằm ngoài Use Case. Gửi thông báo thật qua worker theo scope Task phụ thuộc. Đợt r2 bổ sung luồng đọc trạng thái nộp sau mất kết nối kéo dài.

## E02 Actor và quyền lợi

Requester là actor chính, cần biết request đã vào hàng đợi và có thể thử lại an toàn. Approver là actor hỗ trợ nhận request được phân công. Audit/control owner cần một dấu vết cho mỗi lần chuyển trạng thái. Kênh thông báo nhận intent tối thiểu cần thiết. EX-D2 xác định ranh giới bảo vệ hồ sơ giữa các actor.

## E03 Use Case

**Gửi yêu cầu mở mã dự án để chờ duyệt.** Use Case thuộc EPIC-CRM-001. Trigger là Requester chọn bắt đầu đề nghị mới hoặc tiếp tục một draft. Precondition là CRM đã cung cấp entry point và Requester có ngữ cảnh đăng nhập để bắt đầu. Hệ thống kiểm lại authentication/authorization, ownership, state, version và dữ liệu tại bước gửi.

### FLOW01 Luồng chính

#### STP01 Chuẩn bị

Requester tạo hoặc mở draft. CRM hiển thị request ID, version và trường có thể sửa. Draft chưa vào hàng đợi.

#### STP02 Gửi

Requester gửi draft. CRM kiểm quyền hiện tại theo E07, kiểm replay rồi kiểm state/version và dữ liệu theo E04–E06. Request chưa đổi khi còn đang kiểm.

#### STP03 Ghi

CRM cập nhật Draft → PendingApproval cùng version, audit, notification intent và kết quả operation trong một commit theo E09/E13.

#### STP04 Nhận kết quả

CRM hiển thị receipt cùng request ID, PendingApproval và version mới. Approver được phân công có thể thấy request ở hàng đợi theo quyền. Kết thúc tại [OK](#out01-ok).

### Nhánh tại điểm rẽ

#### B01 Dừng chuẩn bị

**Điểm rẽ:** STP01. Requester đóng form. CRM giữ draft đã lưu và yêu cầu xác nhận bỏ thay đổi chưa lưu nếu có. Kết thúc tại [Giữ nguyên](#out02-giữ-nguyên).

#### B02 Thiếu quyền hoặc hết phiên

**Điểm rẽ:** STP02. CRM từ chối và áp dụng disclosure theo E07. Kết thúc tại [Giữ nguyên](#out02-giữ-nguyên).

#### B03 Dữ liệu sai

**Điểm rẽ:** STP02. CRM trả lỗi theo trường, giữ giá trị đang nhập tại form trong phiên hợp lệ. Requester sửa rồi quay lại bước STP02. Nếu dừng, kết thúc tại [Giữ nguyên](#out02-giữ-nguyên).

#### B04 Xung đột

**Điểm rẽ:** STP02 hoặc STP03. Operation mới dùng version cũ, state sai, thua race tại commit hoặc cùng key khác payload thì nhận conflict. CRM giữ dữ liệu hiện hành. Requester đọc lại theo quyền rồi quay bước STP01 nếu hồ sơ vẫn Draft và muốn gửi. Nếu dừng, kết thúc tại [Giữ nguyên](#out02-giữ-nguyên).

#### B05 Timeout và retry

**Điểm rẽ:** STP02 hoặc STP04. Sau khi kiểm quyền, cùng key/payload trong 24 giờ trả receipt cũ nếu đã commit, tới [OK](#out01-ok). Nếu chưa có kết quả ghi, thử lại luồng kiểm của bước STP02. Nếu hết cửa sổ hoặc còn chưa rõ trạng thái, dùng quyền đọc hiện hành để kiểm receipt/hàng đợi trước khi tạo operation mới. Hết retry mà chưa đối soát thì kết thúc tại [Chờ đối soát](#out03-chờ-đối-soát).

#### B06 Lỗi lưu trước commit

**Điểm rẽ:** STP03. CRM trả lỗi có thể thử lại, rollback toàn bộ thay đổi của operation. Kết thúc tại [Giữ nguyên](#out02-giữ-nguyên) hoặc quay bước STP02 theo retry policy.

#### B07 Gửi thông báo nền chậm hoặc lỗi

**Điểm rẽ:** Sau STP03. CRM giữ đúng một durable intent và request PendingApproval. Worker xử lý recovery riêng. Kết thúc tại [OK](#out01-ok).

### Kết quả cuối và bảo đảm tối thiểu

#### OUT01 OK

Cùng request ID, một lần tăng version, một audit và một durable intent. Receipt và hàng đợi phản ánh PendingApproval theo quyền.

#### OUT02 Giữ nguyên

Operation bị chặn/hủy/lỗi không làm thay đổi dữ liệu nghiệp vụ hoặc sinh audit thành công hay intent. Thay đổi của actor khác vẫn được giữ. Dữ liệu ngoài quyền được bảo vệ.

#### OUT03 Chờ đối soát

CRM báo chưa xác định kết quả tại client. Trạng thái bền vững chỉ có commit trọn vẹn hoặc không commit. Actor đọc lại sau khi có kết nối và còn quyền; dùng cùng key trong cửa sổ hỗ trợ.

## E04 State

Áp dụng MOD-CRM-001 r1 và disposition mặc định trong [shared model](#shared-model-projectcoderequest-r1). Concurrent submit đánh giá guard tại commit. MOD-CRM-002–004 r1 thuộc các mục tiêu lân cận.

## E05 Business rules

BR-CRM-101 dẫn EX-D1 và shared transition. BR-CRM-102 dẫn EX-D2 cho quyền và ownership. BR-CRM-103 dẫn EX-D3 cho replay sau quyền, commit nguyên tử và notification nền. Khi nhiều lỗi cùng xuất hiện, E09 dùng thứ tự auth → resource/ownership → replay → state/version → dữ liệu → commit.

## E06 Dữ liệu

`requestId` do CRM cấp. `expectedVersion` là số nguyên được so tại commit. `projectName` bắt buộc, 1–100 Unicode code points sau trim. `idempotencyKey` bắt buộc, tối đa 64 ASCII ký tự, scope theo principal + request + command. Fingerprint dùng payload và version kỳ vọng. Result lưu 24 giờ theo EX-D3.

## E07 Quyền

Requester có quyền và là owner mới đọc/sửa/gửi draft. Hết phiên trả 401. Draft ngoài scope được che theo cùng 404 với hồ sơ không tồn tại. Actor thấy hồ sơ nhưng thiếu quyền gửi nhận 403. Approver đọc hàng đợi theo assignment. Replay phải kiểm quyền ở request hiện tại.

## E08 UI và Prototype

SCR-PC-LIST dẫn [bước chuẩn bị](#stp01-chuẩn-bị). SCR-PC-EDIT dẫn [gửi](#stp02-gửi), [dữ liệu sai](#b03-dữ-liệu-sai) và [xung đột](#b04-xung-đột). SCR-PC-RECEIPT dẫn [receipt](#stp04-nhận-kết-quả) và [timeout/retry](#b05-timeout-và-retry). Prototype demo có fixture cho từng nhánh E14. Ví dụ manifest dùng refs như `EPIC-CRM-001#b05-timeout-và-retry` trong allocation `EPIC-CRM-001 / r1 / initial-submit`. Baseline thật cần bundle runnable và walkthrough pin bytes.

## E09 Contract

Contract EX-PC-SUBMIT r1 nhận requestId, expectedVersion, projectName và key. Thành công trả receipt và version; replay trả cùng kết quả. Validation 422 theo trường, conflict 409, lỗi trước commit trả lỗi server có thể thử lại. Hàng đợi đọc PendingApproval sau commit theo cùng ID. Worker đọc intent theo contract EX-PC-NOTIFY r1 và kiểm soát replay độc lập.

## E10 Ngoại lệ và tình huống biên

Rà [dừng](#b01-dừng-chuẩn-bị), [quyền](#b02-thiếu-quyền-hoặc-hết-phiên), [dữ liệu](#b03-dữ-liệu-sai), [concurrency](#b04-xung-đột), [timeout/replay](#b05-timeout-và-retry), [lỗi trước commit](#b06-lỗi-lưu-trước-commit) và [lỗi sau commit](#b07-gửi-thông-báo-nền-chậm-hoặc-lỗi). Kiểm cả session mất quyền giữa hai lần retry, key trùng payload khác và crash ở ranh giới audit/intent.

## E11 NFR và kiểm soát

Giả định p95 submit tối đa 800 ms với 20 submit đồng thời trên môi trường kiểm thử tương đương cấu hình release. Đo response API riêng khỏi notification nền. Audit có request ID, principal, operation ID và transition. Kiểm một audit thành công mỗi operation.

## E12 Migration và vận hành

Ví dụ dùng module mới và dữ liệu mới nên không backfill. Ops kiểm hàng đợi intent lỗi, đối soát request ID và operation trước replay. Nếu tắt release, giữ dữ liệu đã commit, ngừng nhận operation mới và dùng runbook drain/restore được duyệt.

## E13 Solution và dependency

TL đề xuất optimistic version guard và transaction ghi state/audit/intent/result, kiểm bằng fault injection. Approver queue và worker là consumer của outputs được version hóa. Task kỹ thuật notification có owner Epic gửi; Story submit và Epic xét duyệt dẫn dependency khi dùng worker. Cấp mã thật bàn giao theo interface của Capability.

## E14 Acceptance Criteria và test conditions

| AC | Scenario/outcome E03 | Test condition và planned evidence |
|---|---|---|
| AC-CRM-101 | [Receipt](#stp04-nhận-kết-quả) → [OK](#out01-ok) | Draft hợp lệ qua List/Form/Receipt, cùng ID; đối chiếu response, queue, audit và intent. |
| AC-CRM-102 | [Thiếu quyền](#b02-thiếu-quyền-hoặc-hết-phiên) → [Giữ nguyên](#out02-giữ-nguyên) | Hết phiên, sai quyền và khác owner; xác nhận phản hồi/disclosure và dữ liệu giữ nguyên. |
| AC-CRM-103 | [Dữ liệu sai](#b03-dữ-liệu-sai) → sửa hoặc giữ nguyên | Kiểm 0/101 ký tự bị từ chối, 1/100 được chấp nhận sau trim. |
| AC-CRM-104 | [Version/state sai](#b04-xung-đột) → giữ nguyên | Draft stale và từng state khác Draft với operation mới. |
| AC-CRM-105 | [Retry](#b05-timeout-và-retry) → OK hoặc chờ đối soát | Mất response sau commit, cùng key, khác payload, mất quyền và hết cửa sổ. So version/audit/intent. |
| AC-CRM-106 | [Hai operation cạnh tranh](#b04-xung-đột) → một OK | Hai key trên cùng version, một commit và một conflict. |
| AC-CRM-107 | [Lỗi gửi nền](#b07-gửi-thông-báo-nền-chậm-hoặc-lỗi) → OK | Worker tạm dừng; đọc PendingApproval và một intent bền vững. |
| AC-CRM-108 | [Lỗi lưu](#b06-lỗi-lưu-trước-commit) → giữ nguyên | Fault injection tại boundary ghi, đối chiếu mọi record trước/sau. |
| AC-CRM-109 | [Dừng chuẩn bị](#b01-dừng-chuẩn-bị) → giữ nguyên | Đóng form có thay đổi chưa lưu, kiểm xác nhận và đọc lại draft. |

Test conditions dự kiến. TestRun, walkthrough và nghiệm thu dùng evidence riêng theo revision/scope.

## E15 Phân bổ Story

| Story candidate | Use Case và lát bàn giao | Controls, dependency và phần còn lại |
|---|---|---|
| STORY-CRM-001 · Gửi draft qua CRM | EPIC-CRM-001 r1, [bước STP01](#stp01-chuẩn-bị) tới [bước STP04](#stp04-nhận-kết-quả) và toàn bộ nhánh r1 ở E14 | Quyền, data, concurrency, retry, atomicity và kiểm receipt/queue tích hợp. Phụ thuộc hợp đồng queue và Task notification. |
| STORY-CRM-002 · Đọc trạng thái nộp sau mất kết nối kéo dài | EPIC-CRM-001 r2, delta từ [Chờ đối soát](#out03-chờ-đối-soát) | Dùng cùng ID, quyền và trạng thái bền vững; cần read contract và kiểm không lộ hồ sơ. Phân bổ r2, không đếm lại STORY-CRM-001. |

## E16 Policy, revision, baseline và thay đổi

| Đợt minh họa | Scope và trạng thái | Evidence và review |
|---|---|---|
| BASE-CRM-001 · r1 | `initial-submit`, giả định đã nghiệm thu, Epic done ở mốc này | Snapshot r1, manifest/walkthrough r1, AC-CRM-101–109 và nghiệm thu EVID-PC-R1. |
| BASE-CRM-002 · r2 | `submission-status`, baseline draft. Change EX-CHG-01 giả định đã được chấp nhận để làm; Epic mở lại inprogress theo workflow. | Giữ EPIC-CRM-001 và các anchor E03 còn cùng nghĩa. Review lại timeout, quyền đọc, contract, UI và AC của delta. Pin evidence commit r1 để tái dùng cho invariant giữ nguyên, chạy lại phép kiểm tích hợp chịu tác động. |

Câu hỏi EX-Q5 của r2. Mốc freshness và cách hiển thị “đang đối soát” chờ Product, TL và QA xác nhận. Báo riêng phạm vi r1 đã nghiệm thu và r2 đang bổ sung. Block minh họa metadata của snapshot r1 bên dưới.

### Bài tập review

Xóa câu về dữ liệu và điểm kết thúc ở nhánh [Dữ liệu sai](#b03-dữ-liệu-sai), giữ nguyên heading/binding. Lint cấu trúc vẫn có thể đạt. Reviewer ghi finding Q02/Q04 ở E03/E14, dẫn nhánh cụ thể và yêu cầu expected result trước khi cấp verdict cho scope đó.

<details>
<summary>Metadata minh họa của r1</summary>

```crm-spec-kit
{
  "schema_version": 1,
  "kind": "Epic",
  "artifact_id": "EPIC-CRM-001",
  "revision": "r1",
  "work_status": "done",
  "epic_policy": "use-case-v1",
  "use_case": {"level": "user-goal", "locator": "#e03-use-case"},
  "defined_ids": [
    "BR-CRM-101", "BR-CRM-102", "BR-CRM-103",
    "AC-CRM-101", "AC-CRM-102", "AC-CRM-103", "AC-CRM-104", "AC-CRM-105",
    "AC-CRM-106", "AC-CRM-107", "AC-CRM-108", "AC-CRM-109"
  ]
}
```

</details>
