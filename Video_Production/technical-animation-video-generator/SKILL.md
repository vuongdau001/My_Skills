---
name: technical-animation-video-generator
description: >-
  Quy trình đầu-cuối tạo video animation giải thích kiến thức kỹ thuật (mặc định 9:16 cho
  Reels/TikTok/Shorts) bằng Remotion (React/TypeScript) + giọng thuyết minh tiếng Việt miễn phí
  (edge-tts) + Vietsub khớp từng câu. Kích hoạt khi user yêu cầu: "tạo video giải thích [chủ đề]",
  "làm animation giải thích cơ chế X", "tạo video Remotion", "video ngắn dạy kỹ thuật",
  "explainer video". Gồm: phương pháp Thực tế trước → Kỹ thuật sau (không chồng lấn), mô phỏng
  cơ chế (gói tin chạy đúng thứ tự, không kiểu slide), chuyển tiếp 3 tầng, linter kịch bản,
  TTS theo từng cue, QA khung hình từng beat, báo cáo phần đã/chưa xác minh. Có template
  Remotion và script Python đã kiểm chứng.
---

# Technical Animation Video Generator

Ý tưởng → Kịch bản (Thực tế → Kỹ thuật) → Fact-check → TTS + .srt → Remotion → QA khung hình → MP4.

Đúc kết từ dự án *Evolution of Authentication* (10/2026). Mọi con số và lỗi trong skill này là số đo và lỗi thật.

## 7 nguyên tắc bắt buộc

1. **Một thế giới ví dụ xuyên suốt.** Chọn 1 bối cảnh đời thường (ngân hàng, sân bay, bệnh viện…)
   cho cả video. Mục tiêu: người ít nền tảng hiểu *vấn đề là gì → vì sao cơ chế giải quyết được →
   đánh đổi gì*. Bản chất cơ chế quan trọng hơn chi tiết giao thức.
2. **Tách tuyệt đối 2 pha.** `mode: "real"` chỉ có hình và từ ngữ đời thường, **0 thuật ngữ IT**.
   `mode: "tech"` là sơ đồ kỹ thuật + **1 Mapping Bar** (vật đời thường ➔ khái niệm kỹ thuật).
3. **Đối xứng 1:1.** Mọi cơ chế và giới hạn ở pha tech phải được kể trước ở pha real. Ví dụ đời thường
   không được mâu thuẫn tính chất kỹ thuật (sai: số thứ tự tăng dần cho Session ID). Xem references/01 §3.
4. **Mô phỏng, không trình chiếu.** Pha real/tech dựng bằng `MNode` + `MLink` + `MPacket` (di chuyển
   đúng thứ tự xử lý) + `MStore`/`MVerdict` (đổi trạng thái). Người xem phải hiểu được *kể cả khi tắt tiếng*.
   `StageCard` chỉ dùng cho bridge/outro/summary. Xem references/02.
5. **Ít chữ, Vietsub khớp từng câu.** Nhãn sân khấu ≤ 4 từ. Mỗi cue ≤ 64 ký tự (≤ 2 dòng).
   **1 cue = 1 file audio**, nên Vietsub khớp tuyệt đối. `tts` bám sát `sub`, chỉ khác phát âm thuật ngữ.
6. **Chuyển tiếp 3 tầng.** (a) Bridge đầu mỗi chương: *giới hạn của phương pháp trước → câu hỏi* dẫn vào
   phương pháp sau. (b) Chỉ báo `1. Thực tế ➔ 2. Kỹ thuật` + Mapping Bar. (c) Hoạt họa theo cue qua `T(cueIdx, frac)`.
7. **Thuật ngữ tiếng Việt sáng nghĩa.** Không dịch từng chữ ("mã thông báo"), không Hán-Việt tối nghĩa
   ("bản rõ", "chuyển mã", "phi trạng thái"). Mô tả bản chất + giữ từ khóa gốc. Bảng: references/01 §5.

## Quy trình 8 bước

### Bước 0. Intake
Hỏi (ask_question) những gì brief chưa có: chủ đề + mục tiêu học (người xem hiểu được gì), đối tượng,
**thời lượng mục tiêu mỗi tập & nền tảng**, tỉ lệ khung hình, giọng nam/nữ, style tham khảo, thế giới ví dụ.
Báo trước: cách "thực tế → kỹ thuật" dài **gấp ~2 lần** giải thích thẳng (~3 chương / tập 120s).

### Bước 1. Khởi tạo project (chỉ dùng runtime có sẵn, xem skill `use-local-runtime`)
```bash
SK=~/.gemini/config/skills/technical-animation-video-generator
cp -R $SK/templates/remotion-project <workspace>/<slug> && cp $SK/scripts/*.py <workspace>/<slug>/tools/
cd <workspace>/<slug> && pnpm install          # cài cục bộ (pnpm có sẵn; không có thì npm install)
python3 -m venv tools/.venv && tools/.venv/bin/pip install edge-tts   # venv cục bộ, KHÔNG pip global
```
`pnpm install` và `pip install` cần mạng, nên chạy với BypassSandbox. Template đã có `public/.gitkeep`.

### Bước 2. Kịch bản + fact-check (`content/script.json`)
- Schema, cấu trúc bridge/real/tech/outro, ngân sách thời lượng: **references/01**.
- Lập **bảng Đối xứng 1:1** và **ma trận phủ yêu cầu** (mỗi ý trong brief ↔ id cue).
- Fact-check từng cue theo **references/03** (10 bẫy thật đã gặp).
- `tools/.venv/bin/python3 tools/lint_script.py content/script.json` → phải ra `No lint problems.`
  (exit 1 nếu lỗi; báo cả khi ước tính vượt `targetSec`).

### Bước 3. Cổng duyệt duy nhất: user duyệt kịch bản
Trình bày bảng: Cảnh | Sân khấu | Vietsub + thời lượng ước tính từng tập (số của linter).
Vượt mục tiêu thì đề xuất chia series hoặc cắt, nêu rõ được/mất. Không tự hạ chuẩn trong im lặng.

### Bước 4. TTS theo từng cue
```bash
tools/.venv/bin/python3 tools/generate_audio.py --part 1 --voice nam   # BypassSandbox: cần speech.platform.bing.com
```
- Cache theo `sha1(voice|rate|tts)`: sửa lời là tự tạo lại, lời cũ giữ nguyên.
- Offline thì tự fallback `say -v Linh` (.m4a). Giọng kém hơn, nên **chạy lại khi có mạng** trước khi bàn giao.
- Đọc **thời lượng thật** in ra. Vượt mục tiêu thì quay lại Bước 2.
- Output: `src/manifest-part1.json`, `out/<slug>-part1.srt`, `public/audio/cues/*`.

### Bước 5. Dựng cảnh Remotion
- Mỗi beat real/tech = 1 component trong `src/scenes/stages.tsx`, đăng ký vào `STAGES` theo `beat.id`.
  Ví dụ mẫu `demo_real`/`demo_tech` (Session) dùng toàn primitives. Bridge/outro do `BeatScene` lo.
- Thêm tập 2: chạy `--part 2`, import `manifest-part2.json` vào `EPISODES` trong `src/Root.tsx`.
- Font: dùng font hệ thống (đã cấu hình trong `tokens.ts`), không tải Google Fonts lúc render
  (từng gặp `ERR_CONNECTION_CLOSED` khi render nhiều tab).
- `./node_modules/.bin/tsc --noEmit` phải exit 0 trước khi render.

### Bước 6. QA khung hình từng beat
```bash
tools/.venv/bin/python3 tools/qa_frames.py --part 1 --csv      # 1 frame/cue, lúc cue đã chạy 85%
./node_modules/.bin/remotion still src/index.ts Part1 out/qa/<id>.png --frame=<N> --log=error \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```
- `remotion still`/`render` cần **BypassSandbox** (Chrome cần Mach port, nếu không sẽ lỗi `Permission denied (1100)`).
- Xem từng ảnh bằng view_file. Checklist:
  - [ ] Pha real không có chữ IT; pha tech có Mapping Bar
  - [ ] Có gói tin/trạng thái thể hiện **thứ tự xử lý**, không phải lưới thẻ
  - [ ] Không phần tử nào tràn khỏi canvas 912px; không vùng trống > 30% sân khấu
  - [ ] Vietsub ≤ 2 dòng; cụm highlight không gãy dòng
  - [ ] Một thời điểm chỉ 1 gói tin đang bay; verdict cũ đã ẩn trước khi verdict mới hiện
- **Sửa code thì phải chụp lại ảnh QA** của beat bị ảnh hưởng.

### Bước 7. Render + bàn giao
```bash
./node_modules/.bin/remotion render src/index.ts Part1 out/<slug>-part1.mp4 --concurrency=4 --port=<cổng trống> \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
/usr/bin/afinfo out/<slug>-part1.mp4      # kiểm tra thời lượng (không cần ffmpeg)
```
`--concurrency=6` từng bị timeout khi mở tab, nên dùng 4. ~160s video ≈ 5 phút render trên máy M-series.
Bàn giao: mp4, .srt, ảnh QA, source, và **bảng Đã xác minh / Chưa xác minh** (mẫu trong references/03).

## Tài nguyên
- `scripts/`: `timing.py` (thông số chung + tốc độ đọc đo được 13.3 ký tự/s @ +12%), `lint_script.py`,
  `generate_audio.py`, `qa_frames.py`
- `templates/remotion-project/`: project Remotion đã kiểm chứng (remotion 4.0.242, react 18.3.1, lucide-react 0.460.0)
- `references/01_pedagogy_and_script_schema.md` · `02_mechanism_primitives.md` · `03_fact_check_traps.md`

## Known gaps
- Mới có primitives cho luồng request/response, ghi/gạch sổ, ✔/✖. Chưa có primitive cho mật mã
  (ký/kiểm chữ ký, cặp khóa) hay so sánh nhiều phương án, nên tự dựng thêm theo cùng phong cách khi cần.
- Chuyển cảnh real→tech hiện là fade + Mapping Bar. Hiệu ứng "vật đời thường biến hình thành khái niệm kỹ thuật"
  (morph) chưa làm.
- Agent không nghe được audio: phát âm thuật ngữ luôn là mục **Chưa xác minh**, cần user nghe thử.
