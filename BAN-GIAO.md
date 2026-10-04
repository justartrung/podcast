# BÀN GIAO DỰ ÁN — Podcast "Chuyện đời cùng Minh Thư"

> **Dành cho Claude ở tài khoản mới.** Đóng gói toàn bộ dự án tới **04/10/2026 15:00 (+07:00)**: dự án là gì, luật, tài nguyên, trạng thái, quy trình làm video trên Google Flow, hậu kỳ, hẹn đăng Facebook, chạy tự động, lỗi đã biết, và việc phải thiết lập lại trên tài khoản mới.
> Nguồn sự thật đầy đủ là repo GitHub **`justartrung/podcast`** (công khai). File này là bản tóm tắt chi tiết; khi có mâu thuẫn, **`STATUS.md` + `docs/08` trong repo (bản mới nhất) thắng**.
> Người viết: Claude (tài khoản cũ), phiên 03/10 16:44 → 04/10 15:10. **Mục tiêu số 1 của chủ: chạy tự động hoàn toàn, không phải bấm duyệt — xem mục 10b.**

---

## 0. Cách dùng file này (cho chủ)
1. Ở tài khoản Claude mới, tạo **Project "PODCAST"**, tải file này vào phần tài liệu của Project. Dán mục **"Project instructions"** ở cuối file (Phụ lục C) vào ô hướng dẫn của Project.
2. Mở phiên làm việc mới, gắn repo **`justartrung/podcast`** (quyền push), liên kết máy tính (app Claude desktop), rồi nhắn: *"Đọc BAN-GIAO.md và CLAUDE.md trong repo, rồi làm mục 11 — thiết lập lại trên tài khoản mới."*
3. **Trước khi tài khoản mới chạy tự động: tắt tác vụ hằng ngày ở tài khoản cũ** (mục 11.1) để không làm 2 tập/ngày, tốn credit đôi, đăng trùng.

---

## 1. Tóm tắt 1 phút
- **Kênh:** Page Facebook **"Chuyện đời cùng Minh Thư"** (`facebook.com/chuyendoicungminhthu`). Video dọc 9:16, ~30–35 giây, nữ host "Minh Thư" (ảnh AI) kể **chuyện gia đình** (vợ chồng, mẹ chồng–nàng dâu, nuôi con, việc nhà), giọng nữ Hà Nội trầm ấm, có phụ đề, kết bằng 1 câu hỏi.
- **Claude là "đầu não giao việc" duy nhất** (thay Codex): tìm ý → viết thoại → tạo video trên **Google Flow** (tool riêng "PODCAST") → tải clip → hậu kỳ **FFmpeg + faster-whisper** (cắt lặng, phụ đề, thumbnail 1 s) → tự QA 13 mục → **hẹn đăng 19:30 qua Meta Business Suite** → xác minh → báo chủ → ghi GitHub.
- **Nhịp:** **1 tập/ngày, đăng 19:30**. Chạy tự động mỗi ngày **13:47** bằng tác vụ định kỳ (scheduled task) gắn với máy tính của chủ.
- **Đã có:** MT-0001 đã đăng (03/10). MT-0002/0003/0004 đã hẹn 04/10, 05/10, 06/10 19:30. Flow còn **860 credit**.
- **Chủ:** Tuấn Anh — giao việc bằng câu ngắn, tiếng Việt, muốn **tự động hoàn toàn**, không phải bấm duyệt.

---

## 2. Cách làm việc với chủ
- Trả lời **tiếng Việt, ngắn gọn**, tự suy ra đủ phạm vi từ câu lệnh ngắn. Không giải thích kỹ thuật thừa.
- Chủ muốn tự động hoàn toàn; chỉ nhắn chủ **đúng 1 việc cần làm** khi bị chặn (đăng nhập, mở Chrome…).
- **Không bao giờ báo "xong / đã đăng / viral" khi chưa có bằng chứng** (file phát được, thấy trong Scheduled/Published, số liệu).
- Quyết định của chủ ghi **nguyên văn** vào `docs/08-quyet-dinh-cua-chu.md` (ưu tiên hơn tài liệu gốc).
- Cuối mỗi phiên: cập nhật `STATUS.md`, `tap/MT-xxxx.md`, `nhat-ky/YYYY-MM-DD.md`, commit + push tiếng Việt.

---

## 3. Luật cứng (không được vi phạm) — đầy đủ ở `docs/04-quy-tac-cung.md`
1. **`D:\PODCAST TU DONG` chỉ đọc** — không sửa/xóa/ghi đè. Chủ: *"Tuyệt đối không tự ý sửa dự án trong file gốc folder, chỉ chỉnh sửa trên github khi có update hay đóng góp ý kiến"*. Góp ý sửa gốc → `de-xuat/`.
2. **Chỉ ghi vào `D:\PODCAST VAN HANH`.** Mọi tải về/cài đặt để **ổ D** — *"ổ C tôi đầy"*.
3. **Không xóa file** trong lượt tự động (lệnh `rm` bật hộp hỏi quyền → lượt chạy dừng). Dùng `mv`; file cần dọn thì ghi vào báo cáo cho chủ.
4. **Không mua credit. ≤ 80 credit/tập gồm cả tạo lại**, tối đa 1 lần tạo lại/cảnh. Thấy giá thật trên giao diện mới bấm tạo.
5. Không nhập mật khẩu/OTP/CAPTCHA, không đọc cookie/token. Chủ tự đăng nhập.
6. Chỉ đăng vào đúng Page "Chuyện đời cùng Minh Thư".
7. **1 tập/ngày, hẹn 19:30.** Làm được 3–4 tập/ngày → hỏi chủ đăng hết hay 1/ngày; thừa → xếp ngày sau (mỗi ngày 1 bài).
8. Nội dung: **chỉ chuyện gia đình**, tình huống hư cấu minh họa; không tôn giáo, không tư vấn y tế/pháp lý/tài chính; **không lời chào, không cảm ơn, không hẹn gặp**; **1 CTA** là câu hỏi theo chủ đề; không sao chép/reup; **không trùng chủ đề đã đăng/đã hẹn**.
9. Một tập = một ảnh host, khóa suốt tập.
10. Flow báo **"Không chạy được công cụ"** → **không bấm "Sửa lỗi"**; đóng tab, mở tab mới, thử ≤ 3 lần; vẫn lỗi thì báo chủ.
11. Chủ nói **"DỪNG"** → dừng mọi thao tác tốn credit/đăng, `STATUS.md` STOP = BẬT.

---

## 4. Tài nguyên & tài khoản
| Mục | Giá trị |
|---|---|
| Page Facebook | "Chuyện đời cùng Minh Thư" — `facebook.com/chuyendoicungminhthu` |
| Meta Business Suite | `asset_id=1239630805911166` · Composer: `https://business.facebook.com/latest/composer/?asset_id=1239630805911166` · Scheduled: `https://business.facebook.com/latest/posts/scheduled_posts?asset_id=1239630805911166` · Lịch: `https://business.facebook.com/latest/content_calendar?asset_id=1239630805911166` |
| Google Flow tool "PODCAST" | `https://flow.google.com/project/f37b741b-b3f2-40f8-b490-f23f79b098ed/tool/6dae8db1-89cf-475a-9412-3334f68ebfdd` |
| Tài khoản Flow | **MINH THƯ (trinhthu.hbl@gmail.com)**, gói PRO. Số dư 04/10 ~14:40: **860 credit** |
| Giá Flow | **Omni 1.1 Flash, 10 giây/cảnh = 15 credit** (xác nhận thật bằng chênh số dư). 4 cảnh = 60/tập |
| Máy tính chủ | Windows, tên máy `tuan-anh`. Thư mục đã cấp: `D:\PODCAST TU DONG` (chỉ đọc), `D:\PODCAST VAN HANH` (ghi). Downloads của Windows đã chuyển sang `D:\PODCAST VAN HANH\tai-ve` |
| Trình duyệt cho Flow | **Trình duyệt trong app Claude desktop** (built-in browser) — đã đăng nhập Gmail MINH THƯ |
| Trình duyệt cho Facebook | **Claude in Chrome** trong **hồ sơ Chrome riêng tên "PODCAST"** (không đăng nhập Gmail; chỉ Facebook) — tách khỏi các hồ sơ Gmail khác của chủ |
| GitHub | `justartrung/podcast` (public), nhánh `main` |
| Ảnh host | `D:\PODCAST TU DONG\02-host\1.png … 4.png` (đã tải lên thư viện Flow) |
| Model whisper | `D:\PODCAST TU DONG\08-cong-cu\models\models--Systran--faster-whisper-small\snapshots\536b0662742c02347bc0e980a01041f333bce120` (HuggingFace bị chặn — chỉ dùng bản này) |

---

## 5. Trạng thái hiện tại (04/10/2026 15:00)
| Tập | Chủ đề (ý) | Ảnh | Trạng thái | Ghi chú |
|---|---|---|---|---|
| MT-0001 | Khi câu hỏi nhỏ thành lời trách | 1 | **Đã đăng** 03/10 19:30 (chủ xác nhận) | ~6 giờ: reach 217, views 271, 1 reaction |
| MT-0002 | Có chìa khóa, có nên tự vào? (I03) | 2 | **Đã hẹn 04/10 19:30** | master sha256 `9c289d45…` |
| MT-0003 | Ai phải nhớ mọi việc trong nhà? (I02) | 3 | **Đã hẹn 05/10 19:30** | `c0c0af01…`, 60 credit |
| MT-0004 | Một giờ nghỉ, sao khó đến vậy? (I04) | 4 | **Đã hẹn 06/10 19:30** | `b05b3a1f…`, 60 credit |
| **MT-0005** | **chưa làm** — ý mới (research) | 1 | Lượt 05/10 13:47 → hẹn **07/10 19:30** | Thoại theo `docs/14` (lần đầu) |

- **Kho ý tưởng** (`nghien-cuu/kho-y-tuong.md`): I01–I04 đã dùng; chỉ còn **I05 (Tết — để tháng 12–1)** → lượt tới phải **research ý mới** (`docs/07`).
- **Số liệu Page** (`nghien-cuu/so-lieu-page-2026-10-03.md`): baseline ~300–470 reach/bài; bài 26/09 *"ANH KHÔNG NGOẠI TÌNH… SAO VẪN ĐÒI LY HÔN?"* reach 1.833 (~4–6× baseline) → **hook xung đột vợ chồng mạnh** hiệu quả nhất.
- Page **đã có bài cũ** (Codex/chủ đăng 23/09–01/10) cùng chủ đề MT-0001 và chủ đề "giúp bố mẹ / vợ buồn" (I01) — tránh lặp.
- **Credit Flow**: 1.050 (03/10) → 930 → 870 (sau MT-0003) → **920 trước MT-0004** (tăng 50 qua đêm, chưa rõ lý do — có thể gói cộng định kỳ, cần đối chiếu) → 860.
- **Đang chờ chủ:** gửi mẫu quần áo host (mục 9); Q4 (repo có chuyển private?); Q7 (TikTok/YouTube).

---

## 6. Kiến trúc kỹ thuật (cách Claude chạm tới mọi thứ)
```
Phiên Claude (cloud)
 ├─ Shell trên máy chủ  = device_bash  → thực chất là MÁY ẢO LINUX (Ubuntu 22.04, 2 CPU, 3 GB RAM)
 │     thư mục gắn: $HOME/mnt/PODCAST TU DONG (chỉ đọc), $HOME/mnt/PODCAST VAN HANH (ghi), $HOME/mnt/Downloads
 │     có sẵn FFmpeg 4.4.2 (libass), Python3, PIL; faster-whisper nằm ở D:\PODCAST VAN HANH\cong-cu\pylib
 ├─ Trình duyệt trong app Claude (mcp__remote-devices__Claude_Browser__*) → Google Flow
 ├─ Claude in Chrome (mcp__claude-in-chrome__*), hồ sơ Chrome "PODCAST" → Business Suite (tải video lên, hẹn giờ)
 ├─ device_stage_files: chép file từ D: vào phiên (/mnt/user-data/uploads/...) — cần cho file_upload và cho git bundle
 └─ GitHub: repo justartrung/podcast (push từ phiên có gắn repo quyền push)
```
Lưu ý môi trường:
- Thư mục gắn **không cho xóa** (cần xin quyền) và `pip --target` hỏng → faster-whisper được cài bằng cách **giải nén wheel thủ công** vào `cong-cu\pylib`. Chạy với `PYTHONPATH="$HOME/mnt/PODCAST VAN HANH/cong-cu/pylib"`.
- Mỗi lệnh device_bash tối đa ~180 s, **không chạy nền được** (nohup bị giết) → chia việc thành bước nhỏ chạy tiền cảnh.
- PyPI dùng được; HuggingFace bị chặn.

### Thư mục vận hành `D:\PODCAST VAN HANH`
```
cong-cu\        hauky.py, thumbnail_tap.py, pitch.py, pylib\ (faster-whisper), wheels\
tai-ve\         = thư mục Downloads của Windows (Flow tải về rơi vào đây; có cả file riêng của chủ — không đụng)
host\           ảnh host mới (5.png…); host\trang-phuc\ (mẫu quần áo), host\trang-phuc\da-dung\
san-xuat\MT-xxxx\
   clip-goc\    canh01_lan1.mp4 … (clip gốc Flow, ghi sha256)
   cat-dung\    phan-tich.json, manifest.json, noi-dung.mp4
   phu-de\      asr.json, kich-ban-cue.json, noi-dung.srt
   qa\          qa-MT-xxxx.json, frames\
   thumb\       thumbnail.png
   ledger.json  sổ credit
san-sang-dang\MT-xxxx\   final.mp4, final-fb.mp4 (≤10 MB), thumbnail.png, caption.txt, subtitles.srt
da-dang\        sau khi đăng (permalink, ảnh chụp)
bang-chung\     ảnh chụp + git bundle chưa push (podcast-MT-xxxx-chua-push.bundle)
```
Bản sao script trong repo: `cong-cu/hauky.py`, `cong-cu/thumbnail_tap.py`, `cong-cu/pitch.py` (bản trên D: là bản chạy).

---

## 7. Quy trình 1 tập (chi tiết — bản chính thức: `docs/13-quy-trinh-hang-ngay.md`)

### Bước 0 — Kiểm trước
- Đọc `STATUS.md`, `docs/04`, `docs/08`, `docs/13`, `docs/14`, nhật ký mới nhất. STOP tắt?
- Máy chủ kết nối; `D:\PODCAST VAN HANH` ghi được.
- **Khung trình duyệt trong app Claude phải đang HIỆN** (ẩn → chụp màn hình Flow timeout, thao tác không ăn → nhắn chủ bấm **Ctrl+Shift+B**).
- Claude in Chrome: `list_connected_browsers` phải có 1 trình duyệt Windows (cửa sổ Chrome PODCAST đang mở).
- **Business Suite → Scheduled**: xem các ngày đã có bài → hẹn tập mới vào **19:30 ngày sớm nhất còn trống**. Có bài trên Scheduled mà GitHub chưa ghi → ghi bù trước.
- Có clip/bài nháp dở của tập trước (`san-xuat`, Drafts) → làm tiếp, không tạo lại. Số tập mới = số lớn nhất trong `tap/` và `san-xuat/` + 1.
- Credit ≥ 80.

### Bước 1 — Chọn ý + viết thoại (~15 phút)
- Lấy ý "Sẵn sàng" điểm cao nhất trong `nghien-cuu/kho-y-tuong.md`, không trùng chủ đề đã đăng/đã hẹn, không trùng mâu thuẫn tập liền trước. Hết ý → 1 vòng research (`docs/07`): tìm chủ đề gia đình đang được bàn nhiều, viết **kịch bản gốc** (không chép lời).
- **4 cảnh × 22–26 tiếng** (10 giây/cảnh). Khung: **cảnh/câu nói thật có xung đột (hook 3 giây) → vì sao đau → "thử nói thế này" → câu hỏi CTA**.
- **Bắt buộc theo `docs/14-loi-noi-tu-nhien.md`** (mục 8 dưới đây) + tự chấm 5 tiêu chí ≥ 4.
- Ghi `tap/MT-xxxx.md` (thoại, ảnh, slot, CTA, topic_key, bảng tự chấm). Đánh dấu ý trong kho. **Commit mốc (a).**
- Thumbnail: `python3 cong-cu/thumbnail_tap.py <ảnh host> <out.png> "DÒNG 1" "DÒNG 2" "DÒNG 3"` → 1080×1920, nền đen, tiêu đề IN HOA vàng ánh kim 2–3 dòng ở trên, ảnh host ở giữa, footer "COACH MINH THƯ" (font DejaVu Serif Bold, đủ dấu tiếng Việt). Lưu `san-xuat\MT-xxxx\thumb\thumbnail.png`.

### Bước 2 — Tạo video trên Flow (~20–30 phút, 60 credit)
Tool là app React chạy trong iframe (`*.scf.usercontent.goog`). Prompt mà tool gửi đi:
`A professional podcast speaker looking at camera, speaking: "<thoại>". Character details: <mô tả giọng>. Realistic lighting and movements. Consistent with previous frame. No extra text, read literally.` — khung đầu = ảnh host (`firstFrameImageMediaId`).
1. Mở **tab mới** trong trình duyệt app Claude → URL tool. Lỗi "Không chạy được công cụ" → đóng tab, tab mới, ≤ 3 lần (không bấm "Sửa lỗi").
2. **Nhập mô tả giọng TRƯỚC khi chọn ảnh** (mô tả bị "chụp" lúc chọn ảnh). Mặc định tool là "Nam, ấm áp, trang trọng" → thay bằng:
   `Female Vietnamese woman, Northern Vietnamese (Hanoi) accent, mature, warm and low voice, calm natural storytelling pace, speaks Vietnamese only`
3. `resize_window` 1280×720 (khung hẹp thì hộp chọn ảnh không vẽ ra) → **Tải ảnh** → chọn `N.png` trong thư viện Flow → cắt **9:16 toàn ảnh** → "Sử dụng vùng này". Mẫu AI **Omni 1.1 Flash**, tỉ lệ **9:16**.
4. Dán thoại cảnh 1 — trong thoại dùng **ngoặc kép cong “ ”** (ngoặc thẳng `"` làm vỡ prompt) → **TẠO VIDEO** → kiểm số dư giảm 15 → tải về, QA cảnh 1 (ASR đủ lời, F0 giọng nữ ~170–215 Hz, hình khớp ảnh). Đạt → **THÊM** 3 cảnh, nhập thoại, bấm TẠO VIDEO từng cảnh. **Không dùng "CHẠY TẤT CẢ CẢNH".** Không có bộ chọn giọng — giọng chỉ do mô tả chữ, phải nghe/đo từng cảnh.
5. **Tải clip** (state của tool nằm trong trình duyệt — tải ngay): thư viện project → mục **Video** → chuột phải → **Tải xuống → 720p**; hoặc mở trang edit từng video → "Tải nội dung nghe nhìn xuống" → 720p. File rơi vào `tai-ve` (có khi tên `<uuid>.tmp` nhưng đầy đủ, ffprobe ≈ 10,006 s) → **nhận cảnh bằng ASR** → `mv` sang `san-xuat\MT-xxxx\clip-goc\canh0K_lanL.mp4`, ghi sha256.
6. Cảnh lỗi (thiếu lời, sai giọng, méo mặt) → tạo lại tối đa 1 lần/cảnh, tổng ≤ 80. Ghi `ledger.json` + `tap/` (số dư trước/sau). **Commit mốc (b).**

### Bước 3 — Hậu kỳ (~10 phút) — `D:\PODCAST VAN HANH\cong-cu\hauky.py`
```bash
cd "$HOME/mnt/PODCAST VAN HANH"
export PYTHONPATH="$HOME/mnt/PODCAST VAN HANH/cong-cu/pylib"
T=san-xuat/MT-xxxx
python3 cong-cu/hauky.py analyze $T      # silencedetect -35dB + ASR từng clip → cat-dung/phan-tich.json
# viết cat-dung/manifest.json: segments [{file, sha256, start, end}], cuts_reviewed_against_audio=true
#   đệm 0,15–0,25 s quanh lời; khoảng lặng >0,7 s rút còn ~0,45 s; giữ 0,6 s cuối
python3 cong-cu/hauky.py cut $T          # → cat-dung/noi-dung.mp4 (1080×1920, 30 fps, libx264 crf18, AAC 192k)
python3 cong-cu/hauky.py asr $T          # → phu-de/asr.json (kiểm đủ lời)
# viết phu-de/kich-ban-cue.json: chữ KỊCH BẢN chia cue ≤ ~38 ký tự (phụ đề theo kịch bản, không theo ASR)
python3 cong-cu/hauky.py srt $T          # difflib căn từng từ kịch bản vào timestamp ASR → noi-dung.srt (khớp ≥ 0,9)
python3 cong-cu/hauky.py render $T $T/thumb/thumbnail.png san-sang-dang/MT-xxxx
```
- `render` = 1 lần filter_complex: thumbnail **đúng 30 khung (1 s)** nối trước nội dung; phụ đề burn (DejaVu Sans Bold, FontSize 10, Alignment 2, MarginV 70, ≤ 2 dòng); audio `adelay=1000`; SRT dời +1 s → `subtitles.srt`. Không dùng `apad` (treo). Timeout → `ps aux | grep [f]fmpeg | awk '{print $2}' | xargs -r kill`.
- Cao độ giọng: `python3 cong-cu/pitch.py <clip>` (tự tương quan, F0 Hz).
- **Bản cho Facebook ≤ 10 MB** (giới hạn `file_upload`):
  `ffmpeg -i final.mp4 -c:v libx264 -preset fast -b:v 2200k -maxrate 2500k -bufsize 5000k -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart final-fb.mp4` (~9 MB cho 33 s).
- **QA 13 mục** → `qa/qa-MT-xxxx.json`: family_content · host_consistency · no_greeting · topic_cta · complete_speech · cuts_reviewed · subtitle_audio_sync · technical (decode không lỗi, H.264/AAC) · full_watch_listen (ASR + F0 + khung hình) · thumbnail_vietnamese_and_face · intro_exact_one_second (**khung 29 = thumbnail, khung 30 = nội dung**, 0–1 s im lặng) · post_intro_audio_subtitle_sync · delivery_bundle_complete. Ghi sha256 master.
- `caption.txt`: hook + 2–3 câu ngắn + câu hỏi + 4 hashtag (`#ChuyenDoiCungMinhThu #ChuyenGiaDinh` + 2 theo chủ đề) + "(Câu chuyện minh họa.)"; không CTA theo dõi. **Commit mốc (c).**

### Bước 4 — Hẹn đăng trên Business Suite (Claude in Chrome)
Dùng **Create post** (không dùng "Create reel" riêng — chủ: *"tạo bài đăng trên trang chứ không phải chỉ một mình reel, vì khi tạo bài đăng trên trang thì có option đăng lên reel luôn"*). Video dọc tự thành Reel.
1. `tabs_context_mcp{createIfEmpty:true}` → `navigate` composer URL (mục 4). Post to = Chuyện đời cùng Minh Thư.
2. **Tải video (cách đã chạy được):** trang không có sẵn `input[type=file]`; nút "Add photo/video" tạo input tạm rồi mở hộp thoại Windows (Claude không điều khiển được). Chặn trước bằng `javascript_tool`:
   ```js
   if (!window.__origClick) window.__origClick = HTMLInputElement.prototype.click;
   HTMLInputElement.prototype.click = function () {
     if (this.type === 'file') {
       this.id = 'claude-file-input';
       this.style.cssText = 'position:fixed;top:0;left:0;width:200px;height:40px;opacity:1;z-index:99999';
       if (!this.isConnected) document.body.appendChild(this);
       return;
     }
     return window.__origClick.call(this);
   };
   ```
   → bấm **"Add photo/video"** (nếu bấm bằng ref không tạo ô file thì bấm bằng tọa độ) → kiểm `document.querySelectorAll('input[type=file]').length === 1` → `find` "file input" lấy ref.
   → `file_upload` **không nhận đường dẫn `D:\...`** → trước đó `device_stage_files` file `D:\PODCAST VAN HANH\san-sang-dang\MT-xxxx\final-fb.mp4`, dùng `stagedPath` `/mnt/user-data/uploads/PODCAST VAN HANH/san-sang-dang/MT-xxxx/final-fb.mp4`.
   → chờ "Uploading media" → "Processing media" → xem trước có video + dòng "Publish your video as a reel". **Đừng chạy vòng chờ JS dài** (làm treo tab) — dùng `wait` vài giây rồi chụp.
3. Bấm ô **Text** → dán caption.
4. **Hẹn giờ:** kéo xuống **Schedule** → bật **Set date and time** → chọn ngày (mặc định hôm nay). Ô giờ báo đỏ là bình thường. **Gõ số không ăn — chỉ dùng phím mũi tên:** bấm đúng vào **2 chữ số giờ** → `ArrowUp` tới **19** → bấm đúng vào **2 chữ số phút** (không dùng ArrowRight — hay lỗi, làm nhảy giờ) → `ArrowUp` tới **30** → chụp kiểm `19:30`, dòng đỏ mất → bấm **Schedule** (xanh, góc dưới phải).
5. **Xác minh:** toast "successfully scheduled" → trang Scheduled có đúng caption, đúng ngày, 19:30, Public (có thể hiện "Processing…" một lúc).
6. Đóng tab. Tab composer chưa đăng có thể bật hộp "Rời trang?" làm treo tiện ích → xóa media trước hoặc chạy `window.addEventListener('beforeunload', e => e.stopImmediatePropagation(), true)` rồi mới `tabs_close_mcp`.
- Không có Chrome → nhắn chủ mở cửa sổ Chrome PODCAST (chờ ≤ 30 phút), quá thì **Finish later** (Drafts) và báo. **Commit mốc (d)** + STATUS + nhật ký.

### Bước 5 — Sau 19:30 / lượt hôm sau
Business Suite → Published: kiểm bài hôm trước đã lên, ghi reach/views vào `nghien-cuu/so-lieu-page-*.md`, lấy permalink, trạng thái `da-dang-xac-minh`.

### Bước 6 — Báo chủ + GitHub
Báo theo `templates/bao-cao-tap.md`:
```
**[MT-XXXX] <Tiêu đề>** — ✅ Đã hẹn/đăng & xác minh / ⚠️ Cần anh xử lý / ❌ Dừng
- Lịch/bài: <ngày 19:30 hoặc permalink>
- Video: <giây>, ảnh host <n>, giọng F0 <Hz>, phụ đề khớp <tỷ lệ>
- Credit: <dùng>/80 (tạo lại <n>) — còn <số dư>
- QA: 13/13 — master sha256 <8 ký tự>
- GitHub: commit cuối <hash> — đã push / nằm trong bundle
- Cần anh: <1 việc hoặc không>
- Tiếp theo: <tập kế tiếp, slot>
```
**GitHub:** commit theo từng mốc (a)(b)(c)(d), push thẳng **`main`** (đừng để tác vụ tạo nhánh `claude/…`). Push lỗi 403 (phiên không có repo/quyền) → thử lại 1 lần → `git bundle create "$HOME/mnt/PODCAST VAN HANH/bang-chung/podcast-MT-xxxx-chua-push.bundle" main` và báo chủ. Phiên có quyền push nạp bundle: `device_stage_files` bundle → `git fetch <bundle> 'refs/heads/*:refs/remotes/bundle/*'` → kiểm fast-forward → `git merge --ff-only bundle/main` → push. (Chủ quyết 04/10 01:19: *"khi nào lịch nào đó set up được đăng lên thì tôi sẽ nhắn cho bạn để bạn push lên github"*.)

---

## 8. Viết lời nói tự nhiên — `docs/14-loi-noi-tu-nhien.md` (áp dụng từ MT-0005)
Chủ (04/10 14:34): *"nội dung nói (câu từ) video nên được giống người và tự nhiên nhất"*.
- Nghe như **chị Minh Thư (~40 tuổi, Hà Nội) kể cho người quen**, không như đọc bài. Host xưng *mình* (hoặc kể ngôi ba *chị/anh*), gọi người xem *bạn*.
- 12 quy tắc: câu ngắn 5–14 tiếng; **mở bằng cảnh/câu nói thật** (*“Em ơi, cái điều khiển đâu?”*); chi tiết đời thường cụ thể; trích lời người nhà bằng “ ”; tiểu từ *nhé, đấy, mà, thôi, chứ, cơ, à, nhỉ, đâu* (1–2/cảnh); từ khẩu ngữ (*nói ra* thay *chia sẻ*, *cãi nhau* thay *xung đột*, *lo* thay *đảm nhận*, *thấy* thay *cảm thấy*); **cấm mẫu "giọng AI"** (*không chỉ… mà còn*, *không phải để… mà để*, *điều quan trọng là*, *chính là*, *hãy cùng*, *hành trình, kết nối, thấu hiểu, giá trị, trân trọng*, liệt kê bộ ba, câu kết châm ngôn); xen câu ngắn/dài, được câu cụt; kể không giảng, gợi 1 việc làm được tối nay; dấu câu = nhịp thở (không ba chấm, gạch ngang, ngoặc đơn, chữ số, viết tắt, tiếng Anh); 22–26 tiếng/cảnh; CTA trả lời được bằng 1 dòng.
- **Tự chấm 5 tiêu chí (mỗi cái ≥ 4/5) trước khi tạo video:** có cảnh/câu nói thật trong 3 giây đầu · nghe như nói · không còn mẫu cấm · có chi tiết cụ thể · CTA trả lời được 1 dòng.
- Ví dụ: *"Nghỉ ngơi không chỉ là được ngồi yên…"* → *"Ngồi yên mà tai vẫn phải nghe gọi, đầu vẫn phải nhớ hộ cả nhà, thì đâu gọi là nghỉ, đúng không?"*

---

## 9. Ảnh host & trang phục — `docs/12-them-anh-host.md`, `host/README.md`
- Vòng xoay: **tập N → ảnh ((N−1) mod 4) + 1** (1→1, 2→2, 3→3, 4→4, 5→1…). Ảnh 1: áo blouse kem, quần be, tóc ngắn nâu, sofa da nâu, studio gỗ, micro bên trái.
- Thêm ảnh: chủ chép `5.png…` vào `D:\PODCAST VAN HANH\host\`, tải lên thư viện Flow, nhắn *"Thêm host <file> — <thêm vào vòng xoay | thay ảnh N | chỉ dùng cho MT-xxxx> — áp dụng từ MT-xxxx"*. Claude ghi sha256 + mô tả vào `host/README.md`, ghi `docs/08`.
- **Đổi trang phục tự động — CHƯA BẬT.** Đề xuất: chủ thả ảnh mẫu quần áo vào `D:\PODCAST VAN HANH\host\trang-phuc\`; lượt hằng ngày lấy mẫu cũ nhất → tạo trong Flow **ảnh host mới giữ nguyên mặt/tóc/bối cảnh, mặc bộ đó** → QA mặt giống, không méo, 9:16 → lưu `host\N.png` + sha256 → `mv` mẫu sang `trang-phuc\da-dung\` → dùng cho tập. Credit tạo ảnh tính vào trần 80. **Trước khi bật:** thử với mẫu đầu tiên chủ gửi (giá thật, độ giống mặt), gửi ảnh cho chủ duyệt, rồi đổi STATUS thành "BẬT". Khi chưa bật: lượt tự động không dùng thư mục này, chỉ báo chủ nếu thấy mẫu.

---

## 10. Lỗi đã biết & cách xử lý
| # | Lỗi | Xử lý |
|---|---|---|
| L1 | Flow "Không chạy được công cụ" | Không bấm "Sửa lỗi"; đóng tab, mở tab mới, ≤ 3 lần; vẫn lỗi → báo chủ |
| L2 | Clip trong tool mất khi tải lại trang | Tải mỗi clip đạt về ngay, ghi sha256 |
| L3 | Hộp chọn file của Windows | Không bấm thường; chặn bằng JS ghi đè `HTMLInputElement.prototype.click` (mục 7 bước 4) |
| L4 | `file_upload` từ chối `D:\…` | `device_stage_files` → dùng `/mnt/user-data/uploads/…` |
| L5 | ffmpeg treo / quá 3 phút | Bỏ `apad`; kill ffmpeg thừa |
| L6 | Trình duyệt hỏi quyền mở site | Chủ chọn "luôn cho phép" (flow.google.com, *.scf.usercontent.goog, business.facebook.com) |
| L7 | Khung trình duyệt app Claude bị ẩn → chụp timeout, thao tác không ăn | Nhắn chủ **Ctrl+Shift+B** |
| L8 | Hộp chọn ảnh của Flow không hiện | `resize_window` 1280×720 |
| L9 | Ô giờ Business Suite không nhận gõ số; ArrowRight làm nhảy giờ | Bấm thẳng phần giờ/phút + ArrowUp/Down |
| L10 | Tab composer treo "Processing media" | Do vòng chờ JS dài — bỏ tab, làm lại bằng `wait` ngắn |
| L11 | Đóng tab composer → hộp "Rời trang?" làm treo tiện ích | Xóa media hoặc chặn `beforeunload` trước khi đóng |
| L12 | Xóa file trong thư mục gắn → hộp hỏi quyền làm dừng lượt tự động | Không xóa; dùng `mv`; báo chủ dọn |
| L13 | Tác vụ định kỳ push GitHub 403 | Bundle trên D: → phiên có quyền push nạp & push (mục 7 bước 6) |
| L14 | App Claude vẫn tải về ổ C sau khi đổi Downloads | Khởi động lại app Claude |
| L15 | ASR nghe nhầm (chọn/trọn, Giúp/Rút…) | Phụ đề luôn lấy chữ kịch bản, chỉ dùng timestamp ASR |

---

## 10b. CHẠY TỰ ĐỘNG HOÀN TOÀN — chủ không phải bấm "Allow" / duyệt gì
Chủ (03/10 22:32, 23:34): *"nó sẽ làm tự động mà không cần hỏi phê duyệt đúng không, tại tôi muốn làm tự động hoàn toàn lúc 13:47"* · *"tôi muốn cho phép được phê duyệt tất cả mà không cần hỏi allow lại"*.
Lượt chạy thử 03/10 bị dừng vì nhiều loại hộp hỏi khác nhau. **Mỗi loại có cách xử lý riêng** — chế độ "tự duyệt" của tác vụ chỉ bỏ được loại 1; các loại còn lại phải cài một lần hoặc tránh bằng cách làm:

| # | Hộp hỏi / chỗ phải bấm | Cách bỏ | Ai làm, khi nào |
|---|---|---|---|
| 1 | Duyệt từng thao tác của Claude (chạy lệnh, mở trang…) | Tác vụ đặt **tự duyệt / Automatically approve** (permission mode = auto). Nếu app tạo tác vụ ở chế độ "hỏi" → vào cài đặt tác vụ bật "Automatically approve" | Chủ, 1 lần khi tạo tác vụ |
| 2 | "Allow this scheduled task to access this folder on every run?" (`D:\PODCAST TU DONG`, `D:\PODCAST VAN HANH`) | Bấm **Allow** → nhớ cho mọi lần sau | Chủ, 1 lần ở lượt chạy đầu |
| 3 | Hỏi quyền **xóa file** | **Không bao giờ xóa** trong lượt tự động; dùng `mv`; file rác ghi vào báo cáo | Claude (luật) |
| 4 | Hỏi quyền **thư mục mới** | Không xin thư mục mới; Downloads đã chuyển vào `D:\PODCAST VAN HANH\tai-ve` (Properties → Location) nên clip tải về nằm sẵn trong thư mục đã cấp | Chủ đã làm 03/10; Claude (luật) |
| 5 | Trình duyệt app Claude hỏi mở site | Chọn **"luôn cho phép"** cho `flow.google.com`, `*.scf.usercontent.goog`, `business.facebook.com` | Chủ, 1 lần/site |
| 6 | Tiện ích Claude in Chrome hỏi quyền trên site | Cho phép **luôn** trên `business.facebook.com` (cài đặt tiện ích → quyền site) | Chủ, 1 lần |
| 7 | Hộp chọn file Windows khi tải video lên Facebook | Chặn bằng JS + `file_upload` (mục 7 bước 4) — không cần người chọn file | Claude |
| 8 | Ô giờ hẹn đăng / nút Schedule | Claude tự đặt 19:30 bằng phím ↑ (mục 7 bước 4) | Claude |
| 9 | Push GitHub | Gắn repo `justartrung/podcast` vào tác vụ → tự push. Chưa gắn được → bundle trên D:, chủ nhắn Claude push (việc tay duy nhất còn lại) | Chủ gắn 1 lần nếu giao diện cho phép |

**Không bỏ được bằng cài đặt — chủ giữ hằng ngày trước 13:47:** máy bật, không ngủ · app Claude mở, **khung trình duyệt đang hiện** (Ctrl+Shift+B) · **cửa sổ Chrome PODCAST mở** · Flow (Gmail MINH THƯ) và Facebook **còn đăng nhập** (hết phiên thì chủ đăng nhập lại — Claude không nhập mật khẩu/OTP).
Khi bị chặn ở bất kỳ điểm nào: Claude làm hết phần còn lại, lưu Drafts nếu cần, và nhắn chủ **đúng 1 việc**.
Ở tài khoản mới: các mục 1, 2, 5, 6 phải bấm lại **một lần** (xem mục 11 bước 2, 4, 5, 6).

---

## 11. THIẾT LẬP LẠI TRÊN TÀI KHOẢN MỚI (checklist)
Những thứ **không** tự sang tài khoản mới: tác vụ định kỳ, liên kết máy tính, đăng nhập tiện ích Claude in Chrome, kết nối GitHub, bộ nhớ/Project của tài khoản cũ. Những thứ **vẫn còn** (nằm trên máy/tài khoản khác): repo GitHub, mọi file trên D:, đăng nhập Facebook trong Chrome PODCAST, tài khoản Flow, Business Suite.

1. **Tài khoản CŨ — tắt tác vụ hằng ngày** "Podcast Minh Thư — làm & hẹn đăng 1 tập/ngày" (`trig_016kmh28YVBq6Egve1K2mdny`, 13:47) — trong app Claude (tài khoản cũ) → Scheduled/Routines → tắt công tắc. **Bắt buộc** trước khi bật tác vụ ở tài khoản mới.
2. **App Claude desktop:** đăng nhập tài khoản mới → liên kết máy tính → cấp quyền 2 thư mục `D:\PODCAST TU DONG` và `D:\PODCAST VAN HANH` (chọn Allow cho mọi lần).
3. **GitHub:** kết nối GitHub (tài khoản `justartrung`) trong tài khoản Claude mới; phiên làm việc gắn repo `justartrung/podcast` **quyền push**.
4. **Claude in Chrome:** trong **cửa sổ Chrome hồ sơ PODCAST**, bấm tiện ích Claude → đăng xuất tài khoản cũ → đăng nhập tài khoản mới; cho phép **luôn** trên `business.facebook.com` (mục 10b #6). Kiểm bằng `list_connected_browsers`.
5. **Trình duyệt trong app Claude:** mở Flow URL — nếu bị đưa về trang giới thiệu thì chủ đăng nhập lại Gmail **trinhthu.hbl@gmail.com**; chọn "luôn cho phép" các site (L6). Mở thử Business Suite cũng được nhưng đăng bài dùng Chrome.
6. **Tạo lại tác vụ hằng ngày** (scheduled task) ở tài khoản mới:
   - Tên: `Podcast Minh Thư — làm & hẹn đăng 1 tập/ngày`
   - Lịch: `CRON_TZ=Asia/Ho_Chi_Minh 47 13 * * *` (13:47 mỗi ngày)
   - **Cần máy tính** (requires local device = có), **tự duyệt — Automatically approve** (bắt buộc, xem mục 10b), thông báo đẩy khi xong
   - Model: chủ chọn **Sonnet 5.5** để tiết kiệm (đổi trong app)
   - **Gắn repo `justartrung/podcast`** vào tác vụ nếu giao diện cho phép (Edit → Select repositories) → tác vụ tự push được, khỏi bundle
   - Prompt: **nguyên văn Phụ lục A**
   - Lần chạy đầu sẽ hỏi quyền thư mục → chủ bấm **Allow** (nhớ cho mọi lần sau)
7. **Chạy thử 1 lần** ("Run now") → kiểm: tập mới đúng số, thoại theo `docs/14`, ≤ 80 credit, hẹn đúng ngày trống 19:30, GitHub có commit (hoặc bundle).
8. Ghi vào `docs/08` + nhật ký: ngày chuyển tài khoản, tác vụ mới (id), tác vụ cũ đã tắt.

**Điều kiện trước 13:47 mỗi ngày (chủ):** máy bật · app Claude mở, **khung trình duyệt đang hiện** · **cửa sổ Chrome PODCAST đang mở** · Flow và Facebook còn đăng nhập.

---

## 12. Việc tiếp theo & câu hỏi mở
1. 05/10 13:47 → **MT-0005** (ảnh 1), hẹn **07/10 19:30**, research ý mới + thoại theo `docs/14`.
2. Thử đổi trang phục khi chủ gửi mẫu (mục 9).
3. Ghi permalink + số liệu MT-0001…0004 sau khi lên.
4. Đối chiếu vì sao credit Flow tăng 870 → 920.
5. Hỏi mở: **Q4** repo public → có chuyển private? (nếu private, tác vụ không clone công khai được — phải gắn repo); **Q7** TikTok/YouTube (chưa làm).
6. `docs/09` L4 cũ ghi "xóa bản trong Downloads" — đã bỏ, dùng L12.

---

## Phụ lục A — Prompt tác vụ hằng ngày (nguyên văn, bản 04/10 14:52)
```
Bạn là đầu não của dự án podcast "Chuyện đời cùng Minh Thư". Nhiệm vụ lần chạy này: làm TRỌN 1 tập mới và HẸN ĐĂNG lúc 19:30 (giờ Việt Nam) lên Facebook Page "Chuyện đời cùng Minh Thư", rồi báo chủ bằng tiếng Việt. Chạy hoàn toàn tự động, không chờ chủ duyệt.

0. GHI GITHUB THEO TỪNG MỐC, KHÔNG ĐỢI CUỐI: repo justartrung/podcast (nếu chưa có trong phiên thì add_repo access "push" nếu có công cụ; nếu không thì clone bản công khai). Làm việc và PUSH THẲNG LÊN NHÁNH main (không tạo nhánh claude/). Commit tiếng Việt NGAY sau mỗi mốc: (a) chốt ý + kịch bản (tap/MT-xxxx.md trạng thái kich-ban + bảng tự chấm docs/14, kho ý tưởng đánh dấu đang dùng); (b) tạo xong clip (ledger credit + số dư Flow trước/sau); (c) QA xong (sha256, đường dẫn file); (d) hẹn lịch xong (ngày giờ, xác minh Scheduled) + STATUS.md + nhat-ky/YYYY-MM-DD.md. Push lỗi (403) thì thử lại 1 lần, rồi làm theo docs/13 mục 6: git bundle vào D:\PODCAST VAN HANH\bang-chung\podcast-MT-xxxx-chua-push.bundle (cập nhật sau mỗi mốc) và ghi rõ trong báo cáo cho chủ (chủ sẽ nhắn Claude push).

1. Đọc: STATUS.md → docs/04-quy-tac-cung.md → docs/08-quyet-dinh-cua-chu.md → docs/13-quy-trinh-hang-ngay.md (làm ĐÚNG từng bước, nhất là mục "Chạy không hỏi phép", bước 4.2 tải video và 4.3 hẹn giờ) → docs/14-loi-noi-tu-nhien.md (BẮT BUỘC khi viết thoại và caption: 12 quy tắc, danh sách cấm, tự chấm 5 tiêu chí đều ≥ 4 mới được tạo video) → nhật ký mới nhất.
2. Luật cứng: KHÔNG sửa/xóa gì trong D:\PODCAST TU DONG (chỉ đọc). Chỉ ghi vào D:\PODCAST VAN HANH. TUYỆT ĐỐI KHÔNG XÓA FILE nào (không rm) và không xin quyền thư mục mới — chỉ dùng thư mục đã được cấp. File Flow tải về nằm ở Downloads của Windows (D:\PODCAST VAN HANH\tai-ve): mv sang san-xuat\MT-xxxx\clip-goc; không đụng file riêng của chủ. Không mua credit, ≤80 credit/tập gồm tạo lại. Không nhập mật khẩu/OTP. Chỉ chuyện gia đình, không lời chào, 1 CTA theo chủ đề. Không trùng chủ đề đã đăng hoặc đã hẹn. Nếu đã có clip/bài nháp MT-xxxx dở từ lượt trước thì làm tiếp, không tạo lại. Số tập mới = số lớn nhất trong tap/ và san-xuat/ trên D: cộng 1. Hết ý "Sẵn sàng" phù hợp mùa → chạy 1 vòng research (docs/07) trước.
2b. Ảnh host: theo vòng xoay ((N−1) mod 4)+1. Đổi trang phục tự động (docs/12 mục cuối) chỉ làm khi STATUS.md ghi "BẬT"; nếu đang "CHƯA BẬT" mà thư mục D:\PODCAST VAN HANH\host\trang-phuc\ có ảnh mẫu → không dùng, chỉ ghi vào báo cáo cho chủ.
3. Trước khi làm: Business Suite → Content → Scheduled (https://business.facebook.com/latest/posts/scheduled_posts?asset_id=1239630805911166). Hẹn vào 19:30 của ngày sớm nhất CHƯA có bài (mỗi ngày tối đa 1 bài). Nếu Scheduled có bài mà GitHub chưa ghi → ghi bù trước.
4. Flow: dùng trình duyệt built-in của app Claude, mở tab mới; nếu khung trình duyệt bị ẩn (ảnh chụp timeout) → nhắn chủ bấm Ctrl+Shift+B; trước khi chọn ảnh host thì resize_window 1280×720. Đăng Facebook: dùng Claude in Chrome (cửa sổ hồ sơ Chrome "PODCAST", đã đăng nhập FB) — docs/13 bước 4.2: (a) mở composer Create post; (b) javascript_tool ghi đè HTMLInputElement.prototype.click để input type=file được gắn vào trang thay vì mở hộp thoại Windows; (c) bấm "Add photo/video"; (d) find "file input" lấy ref; (e) device_stage_files file D:\PODCAST VAN HANH\san-sang-dang\MT-xxxx\final-fb.mp4 (≤10 MB) rồi file_upload với stagedPath /mnt/user-data/uploads/... (đường dẫn D:\ trực tiếp bị từ chối). Đặt ngày + giờ theo đúng docs/13 bước 4.3 rồi bấm Schedule và xác minh trong Content → Scheduled. Xong thì đóng tab (tránh hộp "Rời trang?").
5. Nếu thiếu đăng nhập, máy không kết nối, Chrome chưa mở, hoặc một bước bị chặn: làm hết phần còn lại có thể làm, lưu bài ở Drafts nếu cần, lưu GitHub (push hoặc bundle), và nhắn chủ đúng 1 việc cần làm. Không đăng bù.
6. Kiểm bài ngày hôm trước trong Published, ghi số liệu. Lưu GitHub lần cuối. Báo chủ ngắn theo templates/bao-cao-tap.md (ghi rõ commit cuối và đã push hay đang nằm trong bundle).
```

## Phụ lục B — Quyết định quan trọng của chủ (trích nguyên văn; đầy đủ ở `docs/08`)
- 03/10 16:44 — *"Tuyệt đối không tự ý sửa dự án trong file gốc folder, chỉ chỉnh sửa trên github khi có update hay đóng góp ý kiến"*
- 03/10 17:00 — *"điều kiện mở lịch k cần thiết, chỉ cần làm video, xét chất lượng và đăng… chỉ làm lô tập nếu tôi yêu cầu."* · *"Bạn sẽ thay codex điều phối hết nhé"*
- 03/10 17:12 — *"tải cái gì thì tải trong ổ D nhé, ổ C tôi đầy"* · tập đầu chủ xem trước, ổn định thì tự đăng.
- 03/10 18:1x — *"hẹn đăng qua meta business suite… tự làm + đăng 1 tập/ngày ( lịch 19:30). Trong trường hợp 1 ngày làm được 3,4 cái video thì hỏi chính tôi… Nếu đăng 1 video/ngày và vẫn thừa mấy video còn lại thì đăng dồn ngày hôm sau"*
- 03/10 18:21 — *"tôi bảo tạo bài đăng trên trang chứ không phải chỉ một mình reel…"*
- 03/10 22:32 — muốn **tự động hoàn toàn lúc 13:47**, không phải duyệt; dùng Sonnet 5.5 để tiết kiệm.
- 03/10 23:48 — Chrome riêng hồ sơ **PODCAST** (chủ có nhiều Gmail).
- 04/10 01:19 — *"khi nào lịch nào đó set up được đăng lên thì tôi sẽ nhắn cho bạn để bạn push lên github"*
- 04/10 14:34 — lời nói *"giống người và tự nhiên nhất"* → `docs/14`; sẽ gửi mẫu quần áo host.
- 04/10 14:47 — đổi trang phục tự động qua thư mục `host\trang-phuc\` (chờ thử).

## Phụ lục C — Project instructions gợi ý (dán vào Project ở tài khoản mới)
```
Bạn là đầu não giao việc của podcast "Chuyện đời cùng Minh Thư" (Page Facebook). Quy trình: tìm chủ đề gia đình đang được quan tâm → viết thoại tự nhiên → tạo video trên tool Google Flow "PODCAST" → tải clip, hậu kỳ FFmpeg/phụ đề trên ổ D → tự QA → hẹn đăng 19:30 qua Meta Business Suite → xác minh → báo chủ → ghi GitHub. Mỗi phiên: đọc repo GitHub justartrung/podcast (BAN-GIAO.md, CLAUDE.md, STATUS.md trước). Trả lời tiếng Việt, ngắn gọn; chủ giao việc bằng câu ngắn, tự suy ra đủ phạm vi. Không sửa D:\PODCAST TU DONG; chỉ ghi D:\PODCAST VAN HANH; không xóa file; không mua credit (≤80/tập); không báo xong khi chưa có bằng chứng.
```

## Phụ lục D — Bản đồ repo
| Đường dẫn | Nội dung |
|---|---|
| `CLAUDE.md` | Hướng dẫn đọc đầu phiên + luật quan trọng nhất |
| `STATUS.md` | Trạng thái, hàng đợi tập, việc tiếp theo |
| `BAN-GIAO.md` | File này |
| `docs/01` | Hiểu dự án (kênh, host, giọng, nội dung) |
| `docs/02` | Quy trình vận hành tổng |
| `docs/03` | Kế hoạch theo giai đoạn |
| `docs/04` | Quy tắc cứng |
| `docs/05` | Bản đồ thư mục gốc `D:\PODCAST TU DONG` |
| `docs/06` | Câu hỏi mở (Q4, Q7 còn mở) |
| `docs/07` | Phương pháp tìm nội dung viral |
| `docs/08` | Quyết định của chủ (nguyên văn) |
| `docs/09` | Lỗi đã biết |
| `docs/10` | Thư mục vận hành D: + môi trường hậu kỳ |
| `docs/11` | Tool Flow: giao diện, mã nguồn, giá |
| `docs/12` | Thêm ảnh host, đổi trang phục |
| `docs/13` | **Quy trình hằng ngày** (chính) |
| `docs/14` | **Lời nói tự nhiên** |
| `tap/MT-xxxx.md` | Từng tập: thoại, ledger, QA, đăng |
| `nghien-cuu/` | Kho ý tưởng, số liệu Page |
| `host/README.md` | Bảng ảnh host + sha256 |
| `cong-cu/` | Bản sao hauky.py, thumbnail_tap.py, pitch.py |
| `templates/` | Mẫu báo cáo, tập mới, research, phiên mới |
| `de-xuat/` | Góp ý sửa hệ thống gốc (chờ chủ duyệt) |
| `nhat-ky/` | Nhật ký từng phiên |
| `ban-sao-goc/` | Bản sao văn bản hệ thống gốc 03/10 (chỉ đọc) |
