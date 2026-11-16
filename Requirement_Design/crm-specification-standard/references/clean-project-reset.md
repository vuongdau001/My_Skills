# Reset sạch hồ sơ dự án

ID: CRM-CLEAN-RESET · CRM Workflow Kit 2.2.0 · 16/11/2026

“Bắt đầu lại từ đầu”, khi người dùng xác định là bỏ hồ sơ cũ, có nghĩa **xóa sạch đầu ra và trạng thái cấp ID của dự án** rồi chạy Setup Project mới. Không tạo archive, snapshot/history, namespace theo đợt hoặc crosswalk giữ ID cũ. Đây là helper quản trị, không là function nghiệp vụ thứ 14.

## Phân biệt reset với tiếp tục

- Tiếp tục/sửa/review: giữ logical IDs; quản lý revision/evidence như hiện hành. Chạy lại workflow hoặc prompt không tự reset.
- Reset sạch: phải được người dùng giao rõ việc bỏ hồ sơ cũ; xóa đầu ra đã quản lý của **mọi workstream** cùng namespace dự án và reservation ledger. Từng loại ID bắt đầu lại từ 001 sau khi kiểm sạch.
- ID vẫn duy nhất toàn dự án hiện hành. Không có hai bộ hồ sơ cùng ID ở hai “đợt” hoặc hai workstream. ID không phải thứ tự phát triển, ưu tiên hoặc số thứ tự trong từng Capability.

## Xác định đúng phạm vi xóa

Mặc định toàn bộ nội dung `spec_root` của mọi workstream là vùng đầu ra, gồm Project/Meeting/Decision/Assumption/Constraint, Capability/Epic/Story/Task, review, baseline, report/score/assessment, Prototype/pilot, history và các bản sao trong vùng đó. Giữ nguyên instructions `AGENTS.md`, `AGENTS.override.md`, `CLAUDE.md`; đây là instructions, không là hồ sơ nghiệp vụ. Recreate layout và marker rỗng, không phục hồi nội dung cũ.

Đầu ra cũ nằm ngoài `spec_root` phải được khảo sát và khai báo trong config dự án bằng `generated_output_paths`. Chỉ khai nơi đã xác định là đầu ra kit sở hữu; không đưa cả folder trộn nguồn và output vào danh sách. Ví dụ:

```json
{
  "generated_output_paths": [
    "output/old-run/legacy-spec",
    "output/old-run/historical-ids.json"
  ]
}
```

Đây là field cấp root của `.agents/crm-spec-kit.json`; các field hiện có không đổi. Folder và file đều được phép, các đường không được chồng lấn nhau hoặc `spec_root`. Nếu còn manifest/context/report/history khác của kit, cũng phải kê đúng file hoặc folder sở hữu đó. Không chỉ xóa hai đường minh họa rồi tuyên bố toàn bộ đầu ra đã sạch.

Giữ nguyên source BA, source IDs, `input_root`, `read_only`, config, bộ kit và instructions. Input trỏ vào output cũ hiện được dùng làm nguồn vẫn là nguồn bảo vệ; phải phân loại và giải quyết ranh giới với người giao việc trước reset, không đổi nhãn để được xóa. `historical-ids.json` chỉ là output cũ thì phải xóa, không dùng nó để nâng số mới; ID nguồn thật vẫn được giữ và liên kết như nguồn, không tự đăng ký thành ID CRM mới.

Helper chặn đường tuyệt đối/traversal, hidden/tool directories, overlap nguồn/read-only/config/kit, symlink/special files và allocation lock đang tồn tại. Helper tìm các output có thể nhận diện ngoài ownership (Markdown chứa metadata CRM, assessment JSON, historical-ids.json); gặp thì dừng trước xóa và yêu cầu khai ownership hoặc phân loại source. Khảo sát của agent vẫn bắt buộc vì không thể tự nhận diện mọi file đầu ra từ prose/tên tùy ý. Không tự xóa ngoài đường đã khai báo.

## Cách chạy

Sau khi phạm vi đã được giao rõ, agent chuẩn bị cấu hình và dry-run cụ thể, không hỏi lại chỉ vì helper có thao tác xóa. Nếu phạm vi còn mơ hồ, hoàn thành danh sách dự kiến rồi làm rõ phần chưa được giao trước apply.

```sh
python3 .agents/skills/crm-spec-kit/scripts/kit.py reset --repo . --scope project
```

Đọc `output_paths`, `delete_files`, `preserved_instructions` và `plan_sha256` từ stdout. Dừng công việc authoring khác và chạy apply với digest thực, không gõ nguyên placeholder sau:

```sh
python3 .agents/skills/crm-spec-kit/scripts/kit.py reset --repo . --scope project --plan-sha256 <digest-tu-dry-run> --apply
```

Dry-run không ghi file. Apply cần đúng digest hiện tại, dùng operation lock và cùng allocation lock với next-id; thay bytes/config/danh sách sau dry-run thì bị từ chối. Không tự gỡ lock tồn tại; xác định tác vụ/stale lock trước. Không có reset riêng workstream khi ID vẫn duy nhất toàn dự án. Dừng mọi tác giả khác; lock helper không khóa editor hoặc filesystem của công cụ ngoài.

Không lưu plan/receipt chứa ID cũ trở lại spec_root hoặc output mới. Stdout apply chỉ báo phạm vi, số file xóa, instructions giữ lại và next IDs; không tạo archive/backup/reset journal. Helper không sửa Git history, external backups, baseline nằm trong vùng chỉ đọc hoặc hệ thống bên ngoài; những vùng đó không thuộc hồ sơ đầu ra được giao reset.

Nếu lỗi I/O/ngắt tiến trình sau khi bắt đầu xóa, không tuyên bố reset xong và không cố restore từ archive. Sửa nguyên nhân, kiểm lại phần còn lại và chạy dry-run mới; helper chỉ xác nhận thành công sau verification. Local locks không giải quyết đồng thời qua clone độc lập.

## Kiểm sau reset và chạy lại

1. Không còn artifacts cũ trong các vùng xóa; chỉ instructions và scaffold rỗng. Reservation ledger đã bị xóa.
2. `next-id CAP`, `next-id EPIC` và mọi prefix cho kết quả `PREFIX-CRM-001`; instructions không chiếm số. Trong sử dụng bình thường, references trong spec hiện hành và reservation vẫn giữ số theo allocator dự án.
3. `doctor` và `lint` kiểm filesystem/binding/cấu trúc; không chứng minh discovery/runtime hoặc cấp approval.
4. Nạp `context crm-setup-project` rồi đọc nguồn đầu vào, lập hồ sơ mới. Không kế thừa approval, maturity, verdict review, baseline hoặc Task Done cũ. Khi gặp ID CRM trong nguồn lịch sử được giữ như input, ghi nguồn và provenance, không coi nó là artifact hiện hành hoặc lý do bỏ qua số 001.

Reset không tự gọi Setup hoặc tạo artifact giả có ID. Authoring tiếp theo vẫn theo 13 workflows, catalog/gate/authority hiện hành.
