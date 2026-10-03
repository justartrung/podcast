# 11 — Tool Flow "PODCAST" (đã quan sát 03/10/2026 17:20–17:35)

- URL: https://flow.google.com/project/f37b741b-b3f2-40f8-b490-f23f79b098ed/tool/6dae8db1-89cf-475a-9412-3334f68ebfdd
- Tài khoản: **MINH THƯ (trinhthu.hbl@gmail.com)** — **1.050 credit** (17:30). Khác tài khoản "Quanly Youtube" mà Codex dùng 30/09.
- Mở lần đầu bằng tab mới trong trình duyệt của app Claude: **chạy được ngay**, không gặp "Không chạy được công cụ".
- Truy cập trình duyệt: cần cho phép `flow.google.com` và miền iframe `*.scf.usercontent.goog` (tool chạy trong iframe).

## Giao diện
| Khu | Chi tiết |
|---|---|
| Nhân vật & cài đặt | Ô **Tải ảnh** (chọn từ thư viện Flow → cắt khung 9:16 → upload "Podcast Avatar"); ô **Mô tả giọng nói** (text, mặc định "Nam, ấm áp, trang trọng"); **Mẫu AI**: Omni 1.1 Flash / Veo 3.1 Lite / Veo 3.1 Fast / Veo 3.1 Quality; **Tỉ lệ** 9:16 / 16:9 |
| Kịch bản | Nút **DÁN** (hộp prompt, mỗi đoạn cách 1 dòng trống = 1 cảnh), **THÊM**; mỗi cảnh có ô lời thoại + nút **TẠO VIDEO** |
| Chân | **CHẠY TẤT CẢ CẢNH** (không dùng — tạo liên tục, không kiểm cảnh đầu) |
| Bên phải | Xem trước; **KẾT XUẤT MASTER**: GHÉP VIDEO TỔNG → TẢI VIDEO (.MP4) |

## Hành vi theo mã nguồn (App.tsx)
- Prompt gửi đi: `A professional podcast speaker looking at camera, speaking: "<lời thoại>". Character details: <mô tả giọng>. Realistic lighting and movements. Consistent with previous frame. No extra text, read literally.`
- `firstFrameImageMediaId` = ảnh host đã cắt → khung đầu là ảnh host (giữ ngoại hình).
- **Thời lượng: Omni = 10 giây, Veo = 8 giây.** Không chọn độ phân giải trong tool.
- **Không có bộ chọn giọng/Character voice** — giọng chỉ do **mô tả chữ** quyết định → giọng có thể lệch giữa các cảnh; phải nghe kiểm từng cảnh.
- **Mô tả giọng được "chụp" lúc tải ảnh** → phải nhập mô tả giọng TRƯỚC khi chọn ảnh.
- Lời thoại nằm trong dấu `"` của prompt → trong lời thoại dùng ngoặc kép cong “ ” thay vì `"`.
- Video từng cảnh giữ trong bộ nhớ trang (React state) + lưu thành media Flow (mediaId). Tải về chỉ có nút cho **video tổng sau khi ghép** (`podcast_<timestamp>.mp4`).
- Ghép trong trình duyệt bằng ffmpeg.wasm (nối thẳng, không cắt).

## Giá (bảng chính thức Google, đọc 03/10)
| Model | Giá/lượt |
|---|---|
| Gemini Omni Flash 10 s | 720p **15** · 360p 7 |
| Veo 3.1 Lite (8 s) | 10 (Ultra: 5) |
| Veo 3.1 Fast (8 s) | 20 (Ultra: 10) |
| Veo 3.1 Quality (8 s) | 100 |
Nguồn: https://support.google.com/flow/answer/16526234 — giá có thể đổi; xác nhận bằng chênh lệch số dư trước/sau cảnh 1.

**Phương án MT-0001:** Omni 1.1 Flash, 4 cảnh × 15 = 60 + dự phòng 1 lần tạo lại 15 = **75 ≤ 80**.

## Ảnh host
Tài khoản này **chưa có 1.png–4.png** trong thư viện (chỉ có "Podcast Avatar", "thon x2.png", "chúa.png"… của dự án cũ). Chủ cần tải 4 ảnh từ `D:\PODCAST TU DONG\02-host\` lên (03/10 17:35 đang chờ).
