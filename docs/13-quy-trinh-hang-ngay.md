# 13 — Quy trình chạy hằng ngày (1 tập/ngày, đăng 19:30)

Áp dụng từ 04/10/2026 theo quyết định chủ 03/10 18:11–18:21 (`docs/08`). Mỗi ngày một phiên (scheduled task hoặc chủ ra lệnh) làm **trọn 1 tập** và **hẹn đăng 19:30 cùng ngày** (nếu đã quá 19:10 thì hẹn 19:30 ngày kế tiếp còn trống).

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
5. Tải clip: Flow project → mục **Video** → chuột phải → Tải xuống → **720p** → file vào `C:\Users\ADMIN\Downloads` (có thể `.tmp`) → chép vào `D:\PODCAST VAN HANH\san-xuat\MT-xxxx\clip-goc\`, nhận cảnh bằng ASR, đổi tên `canh0K_lanL.mp4`, **xóa bản ở Downloads**.
6. Cảnh lỗi → tạo lại tối đa 1 lần/cảnh, tổng ≤ 80 credit. Ghi `ledger.json`.

## 3. Hậu kỳ (≈ 10 phút) — `D:\PODCAST VAN HANH\cong-cu\hauky.py`
Chạy với `PYTHONPATH="$HOME/mnt/PODCAST VAN HANH/cong-cu/pylib"`:
1. `analyze <tap>` → xem lặng/ASR → viết `cat-dung/manifest.json` (đệm 0,15–0,25 s, rút lặng >0,7 s còn ~0,45 s, giữ 0,6 s cuối).
2. `cut <tap>` → `asr <tap>` (kiểm đủ lời) → viết `phu-de/kich-ban-cue.json` (≤ ~38 ký tự/cue) → `srt <tap>` (khớp ≥ 0,9).
3. `render <tap> <thumbnail.png> <san-sang-dang/MT-xxxx>` (≈ 1 phút; timeout → kill ffmpeg thừa, `docs/09` L5).
4. QA: khung 29 = thumbnail, khung 30 = nội dung; 0–1 s im lặng; phụ đề ≤ 2 dòng đủ dấu; decode không lỗi; ≤ 90 s. Ghi `qa/qa-MT-xxxx.json`. Viết `caption.txt` (hook + 2–3 câu + câu hỏi + 4 hashtag, không CTA theo dõi).
5. Bản cho Facebook ≤ 10 MB nếu đăng qua Claude in Chrome (xem bước 4): render thêm `final-fb.mp4` bitrate ~2,2 Mbps.

## 4. Hẹn đăng (≈ 5 phút)
Meta Business Suite (`business.facebook.com/latest/composer/?asset_id=1239630805911166`) → **Create post** (không dùng Create reel riêng):
1. Post to = Chuyện đời cùng Minh Thư. Dán caption vào Text.
2. Add photo/video → chọn `final.mp4`:
   - **Claude in Chrome đã kết nối:** dùng `file_upload` vào ô input file (≤ 10 MB → dùng `final-fb.mp4`).
   - **Chưa có:** nhờ chủ chọn file trong hộp thoại Windows (trình duyệt app Claude không chọn file được).
3. Schedule → bật Set date and time → ngày → ô giờ: bấm phần giờ, phím ↑ (số không gõ được), bấm phần phút, ↑ tới 30 → **Schedule**.
4. Xác minh: Content → **Scheduled** có bài, đúng giờ, Public. Ghi `tap/MT-xxxx.md`.
5. Nếu làm được nhiều tập/ngày → **hỏi chủ** đăng hết hay 1/ngày; thừa thì xếp ngày sau (mỗi ngày 1 bài 19:30).

## 5. Sau 19:30 (phiên kế tiếp)
Content → Published: kiểm bài đã đăng, ghi số liệu vào `nghien-cuu/so-lieu-page-*.md`, cập nhật trạng thái `da-dang-xac-minh`.

## 6. Báo chủ + GitHub
Báo theo `templates/bao-cao-tap.md`. Cập nhật STATUS, tap, nhật ký, commit + push.
