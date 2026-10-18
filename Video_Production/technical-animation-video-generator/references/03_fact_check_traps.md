# 03 — Bẫy độ chính xác (fact-check trước khi chốt kịch bản)

Đi qua từng cue với danh sách này. Ví dụ đều là lỗi **thật** đã gặp ở dự án Evolution of Authentication.

| # | Bẫy | Ví dụ lỗi thật | Cách sửa |
|---|---|---|---|
| 1 | **Ví dụ đời thường mâu thuẫn tính chất kỹ thuật** | "Phiếu số thứ tự B-402" cho Session ID (số tuần tự, đoán được) | "Thẻ khách mã riêng K7X9", và pha tech nói rõ "ngẫu nhiên, khó đoán" |
| 2 | **Nói quá** | "Chặn 100% web giả" | "Web giả không dùng được chữ ký" |
| 3 | **Dẫn chứng chưa chắc** | "Đăng nhập bằng VNeID" như OIDC Provider cho bên thứ ba | Chỉ nêu ví dụ đã chắc (Google). Không chắc thì bỏ |
| 4 | **Bỏ sót cơ chế then chốt** | Nói "chỉ lưu Hash" mà không nói đăng nhập kiểm tra thế nào | Thêm "Server băm mật khẩu vừa gõ, so với Hash đã lưu" |
| 5 | **Lẫn khái niệm cặp đôi** | Encoding ↔ Encryption; Authentication ↔ Authorization; định dạng (JWT) ↔ giao thức (OAuth/OIDC) | Mỗi cặp phải có 1 cue phân biệt rõ |
| 6 | **Chỉ nói giới hạn, quên giá trị** | "OTP vẫn bị lừa" trước khi nói MFA giúp được gì | Thứ tự: giá trị → giới hạn → phương pháp kế tiếp |
| 7 | **Mapping Bar nhắc thứ chưa kể** | mapBar ghi "Máy xay một chiều" nhưng pha real không hề nhắc | Áp dụng bảng Đối xứng 1:1 (references/01 §3) |
| 8 | **Thuật ngữ không chuẩn** | "Khóa riêng" | "Khóa bí mật / Khóa công khai" (thuật ngữ trong văn bản pháp lý về chữ ký số ở VN) |
| 9 | **Trình bày như chuỗi thay thế** | "Passkey thay thế Session" | Tổng kết: các phương pháp *kết hợp* theo tầng |
| 10 | **Tuyên bố thời lượng chưa đo** | Plan ghi "~145s, đúng mục tiêu" trong khi mục tiêu là 120s | Chỉ báo số từ linter/generator; vượt mục tiêu thì nói thẳng |

## Báo cáo bàn giao: tách đã/chưa xác minh

```markdown
| Hạng mục | Trạng thái | Bằng chứng |
|---|---|---|
| MP4 phát được, đúng 1080×1920, 30fps | ✔ Đã xác minh | afinfo + file size |
| Vietsub khớp giọng | ✔ Đã xác minh | 1 cue = 1 mp3, .srt sinh từ cùng timing |
| Khung hình từng beat | ✔ / ✖ | ảnh still theo qa_frames.py (liệt kê beat đã xem) |
| Font sau khi sửa code | ✔ / ✖ | **sửa code → chụp lại still** |
| Phát âm thuật ngữ | ⚠ Chưa xác minh | agent không nghe được audio; cần user nghe thử |
| Hiển thị trên app Reels/TikTok (vùng UI che) | ⚠ Chưa xác minh | đã chừa bottomSafeMargin 180px |
```
