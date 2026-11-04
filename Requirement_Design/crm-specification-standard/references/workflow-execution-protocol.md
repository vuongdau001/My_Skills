# Workflow Execution Protocol

ID: **CRM-WORKFLOW-PROTOCOL** · CRM Workflow Kit 1.5.0 · 03/11/2026


## Purpose & Routing

Dùng cho mọi function và agent profile trong kit. Người dùng gọi `crm-specification-standard` bằng ngôn ngữ tự nhiên hoặc nêu function ID. Các ID là tên chức năng nội bộ, chưa là CLI/slash command được cài. [START-HERE](../START-HERE.md) là menu cho member; [registry](../reference-manifest.json) nối function, agent, workflow và tài nguyên.

1. Nhận mục tiêu; phân biệt cần soạn/sửa, review nội dung, check điều kiện, assess impact hay report. Chọn function theo ý định và bước hiện tại, không tự chạy toàn bộ vòng đời.
2. Xác định target/canonical refs, selected scope, revision và baseline. Nếu nhiều target hợp lý, hỏi trước khi chỉnh sửa; không dùng target ngầm từ phiên cũ.
3. Thông báo ngắn function/profile đang dùng, scope và output dự kiến. Nếu có helper context bundle, dùng các phần workflow/profile/protocol đã nạp, không đọc lại toàn chuỗi. Chỉ mở refs/model theo applicability; không tải mọi model.
4. Kiểm required inputs. Tiếp tục phần độc lập khi thiếu input; ghi missing item/authority/owner nếu biết và gate impact. Không invent policy, approval, expected behavior hoặc dữ liệu test.
5. Thực hiện workflow; ghi output/handoff tại artifact hiện hành hoặc nơi user chỉ định. Không tạo competing spec và không tự tạo folder project mới khi chưa biết canonical location.

Câu hỏi recap/status/next step dùng [chế độ hội thoại](conversational-status-and-next-step.md). Recap đã có observed result trong phiên được trả ngay; không bắt full workflow/context hoặc file output. Current status và next step cần đối soát nguồn phù hợp trước khi khẳng định trạng thái hiện hành. Câu hỏi trong nhiệm vụ đang chạy không tự hủy nhiệm vụ hoặc cấp thêm quyền; trả lời ngắn rồi tiếp tục công việc đã được giao.

## Work Context & Resume

Context gồm project/artifact locations, target ID/kind và Jira mapping nếu có, selected scope, input revision/baseline refs, function/mục tiêu, policy versions/authority, quyền đọc/sửa được giao và open questions/findings. User chưa cho project refs thì ghi chưa xác định và tiếp tục phân tích độc lập hoặc hỏi phần chặn.

Không lưu một active Epic/Story toàn cục. Khi resume hoặc đổi người, đọc lại các refs được bàn giao và current revision; so với record trước để phát hiện stale context. Chat history hỗ trợ tìm nguồn, không thay canonical artifacts. Khi đổi target, xác nhận lựa chọn nếu còn mơ hồ, tách record cho target mới, giữ record cũ như lịch sử.

Dùng [context/handoff template](../assets/templates/work-context-and-handoff-template.md) như section trong tài liệu hiện hành hoặc record riêng khi cần. Không bắt sinh file cho mỗi lần chạy. Config workstreams và ID reservations là repo-owned tooling records công khai; không lưu active target toàn cục hoặc hidden state. Các hồ sơ authority/evidence vẫn ở artifacts, không được suy ra từ config.

## Verbs & Write Boundaries

| Verb | Tạo/cập nhật được trong phạm vi được giao | Giới hạn |
|---|---|---|
| setup/define/specify/design/prepare | Draft hoặc artifact canonical phù hợp workflow | Sửa nghĩa sau baseline cần change control; không tự phê duyệt |
| review | Review record/findings và đề xuất remediation | Không tự sửa nguồn đang review; sửa bằng workflow tác giả sau đó, có scope rõ |
| check | Check record/evidence index/findings | Không sửa target, plan, code, policy hay approval; không chuyển status hoặc đóng ticket |
| assess | Impact assessment và đề xuất correction/revalidation plan | Không tự áp dụng thay đổi requirement/baseline đang có hiệu lực |
| report | Report/snapshot derivation và discrepancies | Không sửa Jira status hoặc lấp unknown bằng dữ liệu suy đoán |
| run-pilot | Pilot record/observations trong quyền được giao | Negative cases dùng bản sao; không thao tác phá dữ liệu thật |

Tạo/cập nhật review/check/report record được phép theo nhiệm vụ, kể cả khi target chỉ đọc. Nếu record nằm trong cùng file target, chỉ sửa section record được giao, giữ nguyên nội dung đang đánh giá; nếu không tách được an toàn thì trả record riêng. Read-only request trả kết quả trong chat. Không tự commit/merge/publish/post comment/tạo ticket. Bộ kit không tự viết product code hoặc chạy runtime test; có thể đọc evidence/code theo quyền đã giao.

## Output & Handoff

Mọi run ghi: function/profile; target/scope/input revision; artifacts được tạo/sửa/kiểm; thao tác và witness/evidence; findings/missing decisions + owner/due nếu có; kết quả kiểm scoped; approvals có thật và phần còn thiếu; receiver/next function/reason; actions chưa thực hiện. Ghi loại revision: input commit hoặc working revision, không bịa SHA cho draft.

Độ sâu tỷ lệ với yêu cầu: recap có thể là một đoạn observed result; không ép toàn bộ fields thành form hoặc điền N/A dài dòng trong chat. Khi cần persistence, lưu checkpoint tối thiểu ở mốc có output đáng kể trong vùng ghi đã giao, dẫn source/revision thay vì tạo competing state. Status read-only không tự sửa artifact/checkpoint; dùng handoff/report riêng nếu target đang được pin hoặc baseline.

Phân biệt bốn sự kiện: output đã chuẩn bị, review đã thực hiện, authority đã phê duyệt, hành động thực tế đã xác nhận. Checklist đầy không thay approval. Có approval chưa chứng minh Git đã merge; có merge chưa chứng minh đúng toàn scope được duyệt nếu chưa đối soát.

## Review & Gate Semantics

Áp dụng [review protocol](requirements-review-process-and-verdicts.md) và [gate/authority](readiness-completion-and-approval-gates.md), không tạo verdict/status Jira mới. Đạt/Không đạt/Chưa kiểm/N/A chỉ cho target/check/scope/revision đã xét. Workflow hoàn thành việc lập record không làm gate Đạt.

Full specification review xét catalog áp dụng và Q01–Q07; focused review giới hạn rõ. Task review dùng T01–T08/SMART, không ép toàn bộ Epic catalog. Thiếu authority hoặc input ghi Chưa kiểm đúng phần; có counterexample/gap ghi Không đạt. Không lấy trung bình để bù gap chặn. [Policy](project-policy-register.md) bắt buộc còn Pending thì gate liên quan chưa đủ điều kiện.

Tác giả chuyển profile để tự kiểm vẫn là self-check. Chỉ ghi independent/human review khi có reviewer/lần đánh giá/evidence thực tế. Không tự spawn reviewers hoặc mô phỏng danh tính. AI kết luận nội dung không thay QA runtime verdict, PM closure hay Business acceptance.

Check structural/ref có thể dùng công cụ; semantic comparison là thao tác agent/reviewer; expected result và approval cần đúng authority. Validator của kit chỉ kiểm tài liệu kit, không phải validator DoR/DoD dự án. Hard gate cần thực thi tại Git/Jira/CI như [đặc tả gate](ai-handoff-and-hard-gates.md).

## Failure, Rework & Next Function

- Thiếu nguồn/meaning/authority: dùng crm-define-feature hoặc crm-specify-epic theo target; hỏi quyết định chặn.
- Thiếu solution/feasibility/contract: crm-design-solution; sửa requirement nếu có impact phải qua crm-assess-change khi đã baseline.
- Sai Story allocation/brief Task: crm-prepare-stories. Task tùy chọn; readiness check không tự tạo Task để bù thiếu input.
- Stale approval/evidence: xác định revision mới, impact và phần cần review/test lại; giữ lịch sử, không tự sao chép Pass.
- Sau correction: chạy lại check/review liên quan; không auto nâng kết quả từ việc tác giả nói đã sửa.
- Next function là đề xuất, không tự cho phép thực thi hoặc xác nhận approval. Có đủ input thì có thể bỏ qua các bước đã được chứng minh, không bắt replay toàn quy trình.

## Installation Tooling and Artifact Checks — 1.5

[Installation guide](../INSTALL.md) định nghĩa package/config separation, filesystem adapters và giới hạn doctor. [Artifact metadata/lint](artifact-metadata-and-lint.md) giúp bắt cấu trúc/vocabulary/ID/links; không thay Q01–Q07 hoặc gate authority. Dùng context bundle khi có Python, references mở rộng theo nhu cầu. Sau ghi artifact chạy lint và nêu cảnh báo legacy/coverage chưa kiểm. Helper có thể tạo scaffolds/config/ID reservation đúng quyền; không merge, commit/push, thay shared instructions hoặc Jira states.
