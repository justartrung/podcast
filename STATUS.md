# STATUS — Trạng thái hiện tại

> **Đọc file này đầu tiên mỗi phiên.** Cập nhật cuối mỗi phiên.
> Cập nhật lần cuối: **2026-10-04 01:30 (+07:00)** — Claude, lượt tự động (MT-0003).

## Tổng quan
| Mục | Giá trị |
|---|---|
| Đầu não | **Claude — duy nhất**, thay Codex điều phối toàn bộ (chủ xác nhận 03/10 17:00) |
| Cách chạy | **Tự làm + đăng 1 tập/ngày, hẹn 19:30** (chủ quyết 03/10 18:11). Quy trình: `docs/13-quy-trinh-hang-ngay.md`. Làm được 3–4 tập/ngày → hỏi chủ; thừa → xếp ngày sau |
| STOP | Tắt |
| Lịch tự động | Scheduled task **`trig_016kmh28YVBq6Egve1K2mdny`** — mỗi ngày **13:47** (giờ VN), model Sonnet 5.5, tự duyệt; làm 1 tập + hẹn đăng 19:30; cần máy bật, app Claude mở, Flow/FB còn đăng nhập. Lần đầu: 04/10 13:47 |
| Cài đặt chạy không hỏi phép (`docs/13`) | ✅ đủ 4 bước: Allow thư mục · Downloads → `D:\PODCAST VAN HANH\tai-ve` · Claude in Chrome (hồ sơ Chrome **PODCAST**, đã đăng nhập FB; thử tải video lên composer thành công 04/10 00:0x) · luôn cho phép site |
| Giai đoạn hiện tại | **5 — vận hành hằng ngày**. MT-0001 đã lên Page 03/10 19:30 |
| Tool video | Flow `…/project/f37b741b-b3f2-40f8-b490-f23f79b098ed/tool/6dae8db1-89cf-475a-9412-3334f68ebfdd` |
| Thư mục ghi | `D:\PODCAST VAN HANH` (`docs/10`). Mọi tải về để ổ D (ổ C đầy) |
| Duyệt đăng | MT-0001 chủ đã duyệt (18:11). Từ tập sau Claude tự duyệt & hẹn đăng |
| Tập đã đăng (bởi Claude) | **1** — MT-0001 03/10 19:30 (Reel, Public), chủ xác nhận đã lên. Đã hẹn: MT-0002 04/10 19:30, MT-0003 05/10 19:30 |

## Đang chặn (blockers)
1. ✅ Đã gỡ: tải video lên Facebook bằng Claude in Chrome (chặn hộp thoại + `file_upload` từ file đã stage) — `docs/13` bước 4.2. Lượt chạy thật đầu tiên: 04/10 13:47. Điều kiện: máy bật, app Claude mở, **cửa sổ Chrome PODCAST mở**.
2. ✅ MT-0001 **đã lên Page** (chủ xác nhận 22:29). Phiên 04/10 ghi permalink + số liệu đầu.

⚠️ Page **đã có** bài cùng chủ đề MT-0001 (30/09) và MT-0002 cũ (01/10) do Codex/chủ đăng trước. Chủ chọn vẫn đăng MT-0001 bản mới. MT-0002 cũ hủy. Số liệu: `nghien-cuu/so-lieu-page-2026-10-03.md`.

## Hàng đợi tập
| Mã | Tiêu đề | Ảnh | Trạng thái | File |
|---|---|---|---|---|
| MT-0001 | Khi câu hỏi nhỏ thành lời trách | 1.png | **`da-dang`** 03/10 19:30 (chủ xác nhận) | [tap/MT-0001.md](tap/MT-0001.md) |
| MT-0002 | Có chìa khóa, có nên tự vào? (I03) | 2.png | **`da-hen-lich` 04/10 19:30** (làm ở lượt chạy thử 03/10) | [tap/MT-0002.md](tap/MT-0002.md) |
| MT-0003 | Ai phải nhớ mọi việc trong nhà? (I02) | 3.png | **`da-hen-lich` (60 credit, còn 870)** — hẹn 05/10 19:30 | [tap/MT-0003.md](tap/MT-0003.md) |

## Tài nguyên đã biết
- Flow: tài khoản **MINH THƯ (trinhthu.hbl@gmail.com)**, gói PRO; 1.050 → ~990 sau MT-0001 → ước ~930 sau MT-0002 (chưa đối chiếu số dư). Giá thật Omni 1.1 Flash 10 s = **15 credit**. Giới hạn 80/tập. Còn đủ ~16 tập.
- Facebook: Page "Chuyện đời cùng Minh Thư" — đã đăng nhập & chuyển danh tính Page (30/09). Chưa thử đăng.
- Hậu kỳ: `D:\PODCAST VAN HANH\cong-cu\hauky.py` (bản sao `cong-cu/hauky.py`): analyze → cut → asr → srt → render. FFmpeg 4.4.2 (shell Linux) + faster-whisper trên D:.

## Việc tiếp theo
1. Lượt kế tiếp làm **MT-0004** (ảnh 4, ý I04), hẹn **06/10 19:30**. Flow còn ~870 credit (còn ~14 tập).
2. Số liệu MT-0001 đã ghi (reach 217, views 271 sau ~6 giờ); permalink chưa lấy.
3. **Tác vụ 13:47 không push được GitHub** (403: phiên tác vụ không có repo `justartrung/podcast`, không có công cụ add_repo). **Chủ quyết (04/10 01:19): không gắn repo; mỗi khi một tập đã hẹn lịch, chủ nhắn Claude push** (`docs/08`). Cách làm: tác vụ lưu `git bundle` vào `D:\PODCAST VAN HANH\bang-chung\`; phiên có quyền push nạp bundle rồi push (đã làm 04/10 01:15 với `podcast-MT-0003-chua-push.bundle` → 44a03c9).
4. **Downloads:** Windows đã chuyển Location sang `tai-ve` (file cũ đã sang) nhưng app Claude vẫn tải vào `C:\Users\ADMIN\Downloads` (5 clip MT-0003 còn ở đó) → khởi động lại app Claude để nhận đường dẫn mới. Chủ dọn 5 file .mp4 ở C.
5. Còn chờ: Q4 (repo private?), Q7 (TikTok/YT).

## Lịch sử phiên
- 2026-10-03: Khởi tạo repo; chủ quyết định bỏ cổng pilot, chạy theo lệnh, Claude thay Codex → [nhat-ky/2026-10-03.md](nhat-ky/2026-10-03.md)
