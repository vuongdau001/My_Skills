# 01 — Phương pháp sư phạm & Schema `script.json`

## 1. Cấu trúc một video

```
[Hook real → Hook tech]  →  [Bridge 1 → Real 1 → Tech 1]  →  [Bridge 2 → Real 2 → Tech 2] … → [Outro (nếu chia tập) | Summary]
```

- **Hook**: đặt *bài toán gốc* (VD: "HTTP không nhớ bạn là ai") bằng cặp real → tech.
- **Bridge** (`mode: "bridge"`, 1 cue, 3–5s): biến **giới hạn của phương pháp vừa học** thành câu hỏi
  dẫn vào phương pháp sau. Mẫu: *"Nhưng {giới hạn}. {Câu hỏi mở ra phương pháp kế}?"*
  - VD thật: "Nhưng Request sau, Server lại quên bạn. Gửi lại mật khẩu sao?" → Basic Auth
  - "Gửi mật khẩu liên tục quá rủi ro. Chỉ trình một lần được không?" → Session
  - "Nhưng hàng trăm Server cùng tra một kho thì sao?" → JWT
- **Real** (`mode: "real"`): 2–3 cue. Kể *vấn đề → cách thế giới thực xử lý → đánh đổi*. 0 thuật ngữ IT.
- **Tech** (`mode: "tech"`): 2–4 cue. Câu đầu nối ý ("Sổ khách là Session Store…"), sau đó cơ chế, cuối cùng giới hạn.
- **Outro** (`mode: "outro"`): cliffhanger sang tập sau. `stage[0]` = tên tập, `stage[1]` = "A · B · C".
- **Summary** (`mode: "summary"`): bảng so sánh + "kết hợp, không thay thế".

## 2. Schema

```jsonc
{
  "slug": "authentication-evolution",   // tên file output: out/<slug>-part1.mp4/.srt
  "title": "...",
  "fps": 30, "width": 1080, "height": 1920,
  "ttsRate": "+12%",                     // edge-tts rate; tốc độ đo được: tools/timing.py
  "targetSec": 120,                      // thời lượng mục tiêu MỖI TẬP (từ brief của user)
  "authoringRules": {
    "cueSubMaxChars": 64,                // 2 dòng trên 9:16 ở font 38px
    "stageLabelMaxWords": 4,
    "realModeForbiddenTerms": ["HTTP", "Server", "Cookie", "Token", "..."]  // mở rộng theo chủ đề
  },
  "scenes": [{
    "id": "scene3", "act": "2 · GHI NHỚ ĐĂNG NHẬP", "title": "Session & Cookie",
    "part": 1,                           // BẮT BUỘC ghi rõ (mặc định = 1)
    "beats": [{
      "id": "s3_tech",                   // = key trong STAGES registry
      "mode": "tech",                    // real | tech | bridge | outro | summary
      "stage": ["Browser", "Server", "Session Store"],   // nhãn trên sân khấu (≤4 từ) — tài liệu cho QA
      "mapBar": { "real": "Thẻ khách · Sổ khách", "tech": "Cookie (Session ID) · Session Store" },  // chỉ tech; số cặp phải khớp
      "cues": [{
        "sub": "Sổ khách là Session Store; thẻ khách là Cookie chứa Session ID.",  // Vietsub ≤64 ký tự
        "tts": "Sổ khách là kho lưu phiên. Thẻ khách là cúc-ki chứa mã phiên.",    // lời đọc, bám sát sub
        "hl":  ["Session Store", "Cookie"]                                           // phải là chuỗi con của sub
      }]
    }]
  }]
}
```

## 3. Quy tắc Đối xứng 1:1 (real ↔ tech)

Trước khi chốt kịch bản, lập bảng cho mỗi chương:

| Ý ở pha tech (kể cả giới hạn) | Tình huống tương ứng đã kể ở pha real |
|---|---|
| Session Store trên Server | Sổ khách ở quầy |
| Cookie chứa Session ID **ngẫu nhiên** | Thẻ khách **mã riêng K7X9** (không dùng số thứ tự tăng dần!) |
| Xóa session → đăng xuất ngay | Gạch sổ → thẻ vô hiệu |
| Mọi request phải tra store | Quầy nào cũng phải tra cùng cuốn sổ |

Ô trống ở cột phải = phải sửa kịch bản. Mapping Bar chỉ được chứa các cặp có trong bảng.

## 4. Ma trận phủ yêu cầu (brief ↔ cue)

| Ý bắt buộc trong brief | Cue thể hiện |
|---|---|
| "JWT là định dạng token, không phải giao thức" | s4_tech cue3 |
| "Base64 không phải mã hóa, cần HTTPS" | s2_tech cue1 |

Mọi ý trong brief phải có ít nhất 1 cue. Bản v4 của dự án auth từng bỏ sót ý JWT vì không có bảng này.

## 5. Thuật ngữ & phiên âm TTS

| Hiển thị (`sub`) | Đọc (`tts`) | Tránh |
|---|---|---|
| HTTP / HTTPS / API / JWT / OTP | H T T P / H T T P S / A P I / J W T / O T P | — |
| Cookie / Token / Session | cúc-ki / tô-kần / sét-sần (hoặc "phiên") | "mã thông báo" |
| Payload / Header | pây-lốt / hét-đơ | — |
| OAuth 2.0 / Passkey | O-Auth hai chấm không / Pát-ki | — |
| Base64 | Base sáu tư | "mã hóa Base64" |
| Plaintext | dạng chữ gốc | "bản rõ" |
| Encoding ≠ Encryption | đổi định dạng ≠ mã hóa | "chuyển mã" |
| Stateless / Stateful | không lưu trạng thái / có lưu trạng thái | "phi trạng thái" |
| Private / Public Key | khóa bí mật / khóa công khai | "khóa riêng" |
| Challenge | đề bài ngẫu nhiên | "chuỗi thách thức" |

Lưu ý: chữ cái đánh vần ("H T T P") làm chậm giọng đọc, đã tính vào tốc độ đo trong `timing.py`.

## 6. Thời lượng

- Cách "thực tế → kỹ thuật" dài **gấp ~2 lần** giải thích thẳng. Báo user ngay từ đầu.
- Ngân sách mỗi chương ≈ bridge 4s + real 10–15s + tech 12–20s ≈ 30–40s, nên **~3 chương/tập 120s**.
- Linter ước tính bằng đúng thông số của generator (sai số ~1% trên dự án auth: 164s ước tính vs 163.6s thực tế).
- Vượt `targetSec` thì đề xuất chia tập hoặc cắt, nêu rõ được/mất. Đừng tự hạ chuẩn trong im lặng.
