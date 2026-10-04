# 13 — Quy trình chạy hằng ngày (1 tập/ngày, đăng 19:30)

Áp dụng từ 04/10/2026 theo quyết định chủ 03/10 18:11–18:21 (`docs/08`). Mỗi ngày một phiên (scheduled task hoặc chủ ra lệnh) làm **trọn 1 tập** và **hẹn đăng 19:30 cùng ngày** (nếu đã quá 19:10 thì hẹn 19:30 ngày kế tiếp còn trống).

## Chạy không hỏi phép — cài đặt một lần (chủ làm)
Chế độ tự duyệt của tác vụ KHÔNG bỏ qua được quyền thư mục/xóa file của Windows và quyền mở trang của trình duyệt. Để lượt 13:47 không dừng (tình trạng 03/10 23:50: **B1–B4 ✅ đủ** (Chrome hồ sơ PODCAST kết nối 03/10 23:56, thử tải video lên thành công)):
1. Lần đầu tác vụ hỏi **"Allow this scheduled task to access this folder on every run?"** cho `D:\PODCAST TU DONG`, `D:\PODCAST VAN HANH` (và Downloads) → bấm **Allow** (nhớ cho mọi lần sau).
2. **Chuyển thư mục Downloads của Windows sang ổ D**: File Explorer → chuột phải *Downloads* → Properties → tab **Location** → nhập `D:\PODCAST VAN HANH\tai-ve` → Move → Yes. (Ổ C nhẹ hơn; Claude không cần xin quyền xóa ở ổ C.)
3. Cài **Claude in Chrome** trong **hồ sơ Chrome riêng "PODCAST"** (không đăng nhập Gmail; tách khỏi các hồ sơ Gmail khác của chủ), đăng nhập Facebook trong hồ sơ đó. Hằng ngày trước 13:47 để cửa sổ Chrome PODCAST mở.
4. Trong trình duyệt app Claude, khi hỏi mở `flow.google.com` / `*.scf.usercontent.goog` / `business.facebook.com` → chọn **luôn cho phép**.
**Claude không bao giờ xóa file** trong lượt tự động (mọi lệnh rm sẽ bật hộp hỏi quyền).

## 0. Kiểm tra trước (dừng & báo chủ nếu thiếu)
- Đọc `STATUS.md`, `docs/04`, `docs/08`, nhật ký mới nhất. STOP tắt?
- Máy chủ đang kết nối (công cụ remote-devices có mặt), thư mục `D:\PODCAST VAN HANH` ghi được. Downloads = `$HOME/mnt/PODCAST VAN HANH/tai-ve` (file Flow tải về rơi vào đây; trong đó có sẵn file riêng của chủ — chỉ đụng file video mới tải).
- **Khung trình duyệt của app Claude phải đang hiện** (ẩn → ảnh chụp Flow timeout, thao tác không ăn; nhắn chủ bấm Ctrl+Shift+B). Hộp chọn ảnh của Flow chỉ vẽ ra khi khung đủ rộng → `resize_window` 1280×720 trước khi chọn ảnh.
- Claude in Chrome: `list_connected_browsers` có trình duyệt không → có thì đăng bằng Chrome; không thì theo nhánh dự phòng ở bước 4.2.
- Có bài/clip MT-xxxx dở từ lượt trước (Drafts, `san-xuat/MT-xxxx/clip-goc`, ledger)? → làm tiếp, không tạo lại.
- Hàng chờ đăng: trong Business Suite → Content → **Scheduled** đã có bài cho 19:30 hôm nay chưa? Có rồi → chỉ làm tập để xếp hàng ngày kế tiếp.
- Số credit Flow ≥ 80 (xem bảng tài khoản). Không mua credit.

## 1. Chọn ý + kịch bản (≈ 15 phút)
- Lấy ý điểm cao nhất còn "Sẵn sàng" trong `nghien-cuu/kho-y-tuong.md`, **không trùng chủ đề đã đăng** (`nghien-cuu/so-lieu-page-*.md`, `tap/`), không trùng mâu thuẫn tập liền trước. Hết ý → chạy 1 vòng research (`docs/07`).
- Viết thoại **4 cảnh × 22–26 tiếng** (10 s/cảnh Omni), câu 1 = cảnh/câu nói thật có xung đột (hook 3 giây), không chào, kết bằng 1 câu hỏi CTA. **Bắt buộc theo `docs/14-loi-noi-tu-nhien.md`** (12 quy tắc + tự chấm 5 tiêu chí ≥ 4 trước khi tạo video). Ghi `tap/MT-xxxx.md` kèm bảng tự chấm. Ảnh host = ((N−1) mod 4)+1.
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
4. QA: khung 29 = thumbnail, khung 30 = nội dung; 0–1 s im lặng; phụ đề ≤ 2 dòng đủ dấu; decode không lỗi; ≤ 90 s. Ghi `qa/qa-MT-xxxx.json`. Viết `caption.txt` theo `docs/14` mục Caption (hook + 2–3 câu + câu hỏi + 4 hashtag + "(Câu chuyện minh họa.)", không CTA theo dõi).
5. Bản cho Facebook ≤ 10 MB nếu đăng qua Claude in Chrome (xem bước 4): render thêm `final-fb.mp4` bitrate ~2,2 Mbps.

## 4. Hẹn đăng (≈ 5 phút)
Meta Business Suite `https://business.facebook.com/latest/composer/?asset_id=1239630805911166` → **Create post** (không dùng Create reel riêng). **Ưu tiên làm bước này trong Chrome qua Claude in Chrome** (có `file_upload`); trình duyệt app Claude không tải file lên được.
1. Post to = Chuyện đời cùng Minh Thư. Bấm vào ô **Text** → dán caption.
2. **Video — cách đã chạy thử thành công 04/10 00:0x (Claude in Chrome, hồ sơ Chrome "PODCAST"):**
   a. `list_connected_browsers` phải có 1 trình duyệt (Windows). `tabs_context_mcp{createIfEmpty:true}` → `navigate` tới URL composer ở trên.
   b. Trang **không có sẵn** `input[type=file]`; nút "Add photo/video" tạo input tạm rồi mở hộp thoại Windows. Chặn hộp thoại bằng `javascript_tool` **trước khi bấm**:
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
   c. `find` "Add photo/video button" → bấm bằng ref. Kiểm `document.querySelectorAll('input[type=file]').length === 1` (accept `.jpg,.png,…,video/*`).
   d. `find` "file input" → lấy ref (hiện dạng `button type="file"` ở góc trên trái).
   e. `file_upload` **chỉ nhận file trong phiên** — đường dẫn `D:\...` bị từ chối. Làm: `device_stage_files` file `D:\PODCAST VAN HANH\san-sang-dang\MT-xxxx\final-fb.mp4` → dùng `stagedPath` (`/mnt/user-data/uploads/PODCAST VAN HANH/san-sang-dang/MT-xxxx/final-fb.mp4`) cho `file_upload`.
   f. Chờ "Uploading media" → "Processing media" → xem trước hiện video, có dòng "Publish your video as a reel" (≈ 15–30 s). Media hiện "1080 × 1920 · 0:30 secs".
   g. `final-fb.mp4` ≤ 10 MB: `ffmpeg -i final.mp4 -c:v libx264 -preset fast -b:v 2200k -maxrate 2500k -bufsize 5000k -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart final-fb.mp4` (MT-0001: 20,3 MB → 8,9 MB).
   - Đóng tab composer chưa đăng có thể bật hộp "Rời trang?" làm treo tiện ích → xóa media (thùng rác) trước, hoặc chạy `window.addEventListener('beforeunload', e => e.stopImmediatePropagation(), true)` rồi mới `tabs_close_mcp`.
   - Không có Chrome → nhắn chủ chọn file (chờ ≤ 30 phút), quá thì lưu **Finish later** (Drafts) và báo.
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
Báo theo `templates/bao-cao-tap.md`. Cập nhật STATUS, tap, nhật ký, commit + push **theo từng mốc**.
- Push bị 403 (phiên không có repo/quyền push): thử lại 1 lần, rồi `git bundle create "$HOME/mnt/PODCAST VAN HANH/bang-chung/podcast-MT-xxxx-chua-push.bundle" main` và báo chủ. Phiên sau có quyền push: `device_stage_files` bundle → `git fetch <bundle> 'refs/heads/*:refs/remotes/bundle/*'` → kiểm fast-forward → `git merge --ff-only bundle/main` → push.
