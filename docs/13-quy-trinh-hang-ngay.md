# 13 — Quy trình chạy hằng ngày (1 tập/ngày, đăng 19:30)

Áp dụng từ 04/10/2026 theo quyết định chủ 03/10 18:11–18:21 (`docs/08`). Mỗi ngày một phiên (scheduled task hoặc chủ ra lệnh) làm **trọn 1 tập** và **hẹn đăng 19:30 cùng ngày** (nếu đã quá 19:10 thì hẹn 19:30 ngày kế tiếp còn trống).

## Chạy không hỏi phép — cài đặt một lần (chủ làm)
Chế độ tự duyệt của tác vụ KHÔNG bỏ qua được quyền thư mục/xóa file của Windows và quyền mở trang của trình duyệt. Để lượt 13:47 không dừng:
1. Lần đầu tác vụ hỏi **"Allow this scheduled task to access this folder on every run?"** cho `D:\PODCAST TU DONG`, `D:\PODCAST VAN HANH` (và Downloads) → bấm **Allow** (nhớ cho mọi lần sau).
2. **Chuyển thư mục Downloads của Windows sang ổ D**: File Explorer → chuột phải *Downloads* → Properties → tab **Location** → nhập `D:\PODCAST VAN HANH\tai-ve` → Move → Yes. (Ổ C nhẹ hơn; Claude không cần xin quyền xóa ở ổ C.)
3. Cài **Claude in Chrome**, đăng nhập Facebook trong Chrome, cho phép tiện ích chạy trên `business.facebook.com` (luôn cho phép).
4. Trong trình duyệt app Claude, khi hỏi mở `flow.google.com` / `*.scf.usercontent.goog` / `business.facebook.com` → chọn **luôn cho phép**.
**Claude không bao giờ xóa file** trong lượt tự động (mọi lệnh rm sẽ bật hộp hỏi quyền).

## 0. Kiểm tra trước (dừng & báo chủ nếu thiếu)
- Đọc `STATUS.md`, `docs/04`, `docs/08`, nhật ký mới nhất. STOP tắt?
- Máy chủ đang kết nối (công cụ remote-devices có mặt), thư mục `D:\PODCAST VAN HANH` ghi được.
- Hàng chờ đăng: trong Business Suite → Content → **Scheduled** đã có bài cho 19:30 hôm nay chưa? Có rồi → chỉ làm tập để xếp hàng ngày kế tiếp.
- Số credit Flow ≥ 80 (xem bảng tài khoản). Không mua credit.

## 1. Chọn ý + kịch bản (≈ 15 phút)
- Lấy ý điểm cao nhất còn "Sẵn sàng" trong `nghien-cuu/kho-y-tuong.md`, **không trùng chủ đề đã đăng** (`nghien-cuu/so-lieu-page-*.md`, `tap/`), không trùng mâu thuẫn tập liền trước. Hết ý → chạy 1 vòng research (`docs/07`).
- Viết thoại **4 cảnh × ~24–26 tiếng** (10 s/cảnh Omni), câu 1 = xung đột mạnh (hook 3 giây), không chào, kết bằng 1 câu hỏi CTA. Ghi `tap/MT-xxxx.md`. Ảnh host = ((N−1) mod 4)+1.
- Thumbnail 1080×1920 (tiêu đề IN HOA 2–3 dòng, vàng ánh kim trên đen, footer COACH MINH THƯ) — dựng bằng PIL từ ảnh host (mẫu: `ban-sao-goc/scripts/thumbnail.py`, font có dấu tiếng Việt).

## 2. Tạo video trên Flow (≈ 20 phút, 60–75 credit)
1. Mở **tab mới** trong trình duyệt app Claude → URL tool (`docs/11`). Lỗi "Không chạy được công cụ" → `docs/09` L1.
2. **Nhập mô tả giọng TRƯỚC** khi chọn ảnh: `Female Vietnamese woman, Northern Vietnamese (Hanoi) accent, mature, warm and low voice, calm natural storytelling pace, speaks Vietnamese only`.
3. Tải ảnh → chọn `N.png` → cắt 9:16 toàn ảnh → "Sử dụng vùng này". Model **Omni 1.1 Flash**, 9:16.
4. Dán thoại cảnh 1 (dùng ngoặc kép cong “ ”) → TẠO VIDEO → kiểm số dư giảm 15 → tải về & QA cảnh 1 (ASR đủ lời, F0 nữ ~170–210 Hz, hình khớp ảnh). Đạt → THÊM 3 cảnh, nhập thoại, bấm TẠO VIDEO cả 3. **Không dùng "CHẠY TẤT CẢ CẢNH".**
5. Tải clip: Flow project → mục **Video** → chuột phải → Tải xuống → **720p**. File rơi vào thư mục Downloads của Windows:
   - **Nếu chủ đã chuyển Downloads sang `D:\PODCAST VAN HANH\tai-ve`** (khuyến nghị, xem mục "Chạy không hỏi phép"): file nằm sẵn trong thư mục được cấp quyền → **đổi tên/di chuyển (mv)** sang `san-xuat\MT-xxxx\clip-goc\canh0K_lanL.mp4`. mv trong cùng thư mục được cấp quyền không cần quyền xóa.
   - Nếu Downloads vẫn ở ổ C: chép sang `clip-goc` rồi **KHÔNG xóa** bản ở Downloads (xóa sẽ bật hộp hỏi quyền và làm dừng lượt chạy). Ghi tên file cần dọn vào báo cáo để chủ dọn.
   - File có thể ở dạng `<uuid>.tmp` nhưng đã đầy đủ (ffprobe ~10,006 s) → nhận cảnh bằng ASR.
6. Cảnh lỗi → tạo lại tối đa 1 lần/cảnh, tổng ≤ 80 credit. Ghi `ledger.json`.

## 3. Hậu kỳ (≈ 10 phút) — `D:\PODCAST VAN HANH\cong-cu\hauky.py`
Chạy với `PYTHONPATH="$HOME/mnt/PODCAST VAN HANH/cong-cu/pylib"`:
1. `analyze <tap>` → xem lặng/ASR → viết `cat-dung/manifest.json` (đệm 0,15–0,25 s, rút lặng >0,7 s còn ~0,45 s, giữ 0,6 s cuối).
2. `cut <tap>` → `asr <tap>` (kiểm đủ lời) → viết `phu-de/kich-ban-cue.json` (≤ ~38 ký tự/cue) → `srt <tap>` (khớp ≥ 0,9).
3. `render <tap> <thumbnail.png> <san-sang-dang/MT-xxxx>` (≈ 1 phút; timeout → kill ffmpeg thừa, `docs/09` L5).
4. QA: khung 29 = thumbnail, khung 30 = nội dung; 0–1 s im lặng; phụ đề ≤ 2 dòng đủ dấu; decode không lỗi; ≤ 90 s. Ghi `qa/qa-MT-xxxx.json`. Viết `caption.txt` (hook + 2–3 câu + câu hỏi + 4 hashtag, không CTA theo dõi).
5. Bản cho Facebook ≤ 10 MB nếu đăng qua Claude in Chrome (xem bước 4): render thêm `final-fb.mp4` bitrate ~2,2 Mbps.

## 4. Hẹn đăng (≈ 5 phút)
Meta Business Suite `https://business.facebook.com/latest/composer/?asset_id=1239630805911166` → **Create post** (không dùng Create reel riêng). **Ưu tiên làm bước này trong Chrome qua Claude in Chrome** (có `file_upload`); trình duyệt app Claude không tải file lên được.
1. Post to = Chuyện đời cùng Minh Thư. Bấm vào ô **Text** → dán caption.
2. **Video:** dùng `find`/`read_page` tìm ô `input[type=file]` (đừng bấm nút "Add photo/video" — sẽ mở hộp thoại Windows không điều khiển được) → `file_upload` với `final-fb.mp4` (≤ 10 MB: render lại `-b:v 2200k -maxrate 2500k -bufsize 5000k -b:a 128k`). Chờ ô xem trước bên phải hiện video.
   - Không có Claude in Chrome → nhắn chủ chọn file (chờ ≤ 30 phút), quá thì lưu **Finish later** (Drafts) và báo.
3. **Hẹn giờ 19:30 (cách đã chạy được 03/10):**
   a. Kéo xuống mục **Schedule** → bật công tắc **Set date and time**. Ô ngày mặc định = hôm nay (đổi nếu xếp ngày khác).
   b. Ô giờ hiện `00:00` và báo đỏ — bình thường. **Gõ số không ăn**; chỉ dùng phím mũi tên.
   c. Chụp màn hình, **bấm đúng vào 2 chữ số giờ** (bên trái dấu ":") → nhấn **ArrowUp 19 lần** (hoặc từng lần, chụp kiểm) → phải thấy `19:00`.
   d. **Bấm đúng vào 2 chữ số phút** (bên phải dấu ":"; đừng dùng phím ArrowRight vì hay lỗi và làm tăng nhầm giờ) → **ArrowUp 30 lần** → thấy `19:30`. Nếu giờ bị nhảy thành 20, bấm lại phần giờ → ArrowDown 1.
   e. Chụp màn hình kiểm `19:30`, dòng báo đỏ đã mất, nút **Schedule** (xanh, góc dưới phải) sáng → bấm **Schedule**.
4. Xác minh: toast "successfully scheduled" → Content → **Scheduled**: đúng caption, đúng ngày giờ, Public. Ghi `tap/MT-xxxx.md`.
5. Nhiều tập/ngày → **hỏi chủ** đăng hết hay 1/ngày; thừa thì xếp ngày sau (mỗi ngày 1 bài 19:30).

## 5. Sau 19:30 (phiên kế tiếp)
Content → Published: kiểm bài đã đăng, ghi số liệu vào `nghien-cuu/so-lieu-page-*.md`, cập nhật trạng thái `da-dang-xac-minh`.

## 6. Báo chủ + GitHub
Báo theo `templates/bao-cao-tap.md`. Cập nhật STATUS, tap, nhật ký, commit + push.
