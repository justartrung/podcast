# STATUS — Trạng thái hiện tại

> **Đọc file này đầu tiên mỗi phiên.** Cập nhật cuối mỗi phiên.
> Cập nhật lần cuối: **2026-10-03 18:55 (+07:00)** — Claude, phiên 1.

## Tổng quan
| Mục | Giá trị |
|---|---|
| Đầu não | **Claude — duy nhất**, thay Codex điều phối toàn bộ (chủ xác nhận 03/10 17:00) |
| Cách chạy | **Tự làm + đăng 1 tập/ngày, hẹn 19:30** (chủ quyết 03/10 18:11). Quy trình: `docs/13-quy-trinh-hang-ngay.md`. Làm được 3–4 tập/ngày → hỏi chủ; thừa → xếp ngày sau |
| STOP | Tắt |
| Lịch tự động | Scheduled task **`trig_016kmh28YVBq6Egve1K2mdny`** — mỗi ngày **13:47** (giờ VN) làm 1 tập + hẹn đăng 19:30; cần máy bật, app Claude mở, Flow/FB còn đăng nhập. Lần đầu: 04/10 13:47 |
| Giai đoạn hiện tại | **5 — vận hành hằng ngày**. MT-0001 đã hẹn đăng 03/10 19:30 |
| Tool video | Flow `…/project/f37b741b-b3f2-40f8-b490-f23f79b098ed/tool/6dae8db1-89cf-475a-9412-3334f68ebfdd` |
| Thư mục ghi | `D:\PODCAST VAN HANH` (`docs/10`). Mọi tải về để ổ D (ổ C đầy) |
| Duyệt đăng | MT-0001 chủ đã duyệt (18:11). Từ tập sau Claude tự duyệt & hẹn đăng |
| Tập đã đăng (bởi Claude) | **1** — MT-0001 03/10 19:30 (Reel, Public), chủ xác nhận đã lên |

## Đang chặn (blockers)
1. **Tải video lên Facebook cần chọn file trong hộp thoại Windows** — trình duyệt app Claude không tự chọn được; điều khiển máy tính không với tới hộp thoại của app Claude. Hướng giải: chủ cài **Claude in Chrome** + đăng nhập Facebook trong Chrome → Claude dùng `file_upload` (≤ 10 MB/file). Tạm thời: nhờ chủ chọn file mỗi ngày.
2. ✅ MT-0001 **đã lên Page** (chủ xác nhận 22:29). Phiên 04/10 ghi permalink + số liệu đầu.

⚠️ Page **đã có** bài cùng chủ đề MT-0001 (30/09) và MT-0002 cũ (01/10) do Codex/chủ đăng trước. Chủ chọn vẫn đăng MT-0001 bản mới. MT-0002 cũ hủy. Số liệu: `nghien-cuu/so-lieu-page-2026-10-03.md`.

## Hàng đợi tập
| Mã | Tiêu đề | Ảnh | Trạng thái | File |
|---|---|---|---|---|
| MT-0001 | Khi câu hỏi nhỏ thành lời trách | 1.png | **`da-hen-lich` 03/10 19:30** | [tap/MT-0001.md](tap/MT-0001.md) |
| MT-0002 | (ý mới — đề xuất I03 "Có chìa khóa, có nên tự vào?") | 2.png | `y-tuong` — làm 04/10, đăng 04/10 19:30 | [tap/MT-0002.md](tap/MT-0002.md) |

## Tài nguyên đã biết
- Flow: tài khoản **MINH THƯ (trinhthu.hbl@gmail.com)**, gói PRO; 1.050 → còn ~990 credit sau MT-0001. Giá thật Omni 1.1 Flash 10 s = **15 credit**. Giới hạn 80/tập. Còn đủ ~16 tập.
- Facebook: Page "Chuyện đời cùng Minh Thư" — đã đăng nhập & chuyển danh tính Page (30/09). Chưa thử đăng.
- Hậu kỳ: `D:\PODCAST VAN HANH\cong-cu\hauky.py` (bản sao `cong-cu/hauky.py`): analyze → cut → asr → srt → render. FFmpeg 4.4.2 (shell Linux) + faster-whisper trên D:.

## Việc tiếp theo
1. Sau 19:30 03/10: Content → Published → xác minh MT-0001, ghi số liệu.
2. 04/10: phiên hằng ngày làm MT-0002 (ý I03, ảnh 2) theo `docs/13`, hẹn 19:30.
3. Chủ cài Claude in Chrome (đăng nhập FB trong Chrome) để bỏ bước chọn file tay.
4. Còn chờ: Q4 (repo private?), Q7 (TikTok/YT).

## Lịch sử phiên
- 2026-10-03: Khởi tạo repo; chủ quyết định bỏ cổng pilot, chạy theo lệnh, Claude thay Codex → [nhat-ky/2026-10-03.md](nhat-ky/2026-10-03.md)
