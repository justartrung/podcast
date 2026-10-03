# STATUS — Trạng thái hiện tại

> **Đọc file này đầu tiên mỗi phiên.** Cập nhật cuối mỗi phiên.
> Cập nhật lần cuối: **2026-10-03 18:25 (+07:00)** — Claude, phiên 1.

## Tổng quan
| Mục | Giá trị |
|---|---|
| Đầu não | **Claude — duy nhất**, thay Codex điều phối toàn bộ (chủ xác nhận 03/10 17:00) |
| Cách chạy | **Theo lệnh của chủ**: mỗi lệnh = 1 tập trọn quy trình (video → QA → đăng → xác minh → báo). Không cổng pilot. Lô nhiều tập / lịch định kỳ **chỉ khi chủ yêu cầu** |
| STOP | Tắt |
| Giai đoạn hiện tại | **3**: MT-0001 đã làm xong video + QA → **chờ chủ duyệt bản xem trước** rồi đăng Facebook |
| Tool video | Flow `…/project/f37b741b-b3f2-40f8-b490-f23f79b098ed/tool/6dae8db1-89cf-475a-9412-3334f68ebfdd` |
| Thư mục ghi | `D:\PODCAST VAN HANH` (`docs/10`). Mọi tải về để ổ D (ổ C đầy) |
| Duyệt đăng | Tập đầu: **chủ xem trước**. Ổn định rồi → Claude tự đăng |
| Tập đã đăng | 0 — MT-0001 sẵn sàng đăng (60 credit, 0 tạo lại) |

## Đang chặn (blockers)
1. **Chờ chủ xem & duyệt MT-0001** (`D:\PODCAST VAN HANH\san-sang-dang\MT-0001\final.mp4`).
2. Facebook: chưa kiểm phiên đăng nhập Page trong trình duyệt của app Claude (sẽ kiểm khi đăng).

✅ 03/10: tool Flow chạy ngay; giá thật 15 credit/cảnh 10 s; 4 cảnh đạt lần đầu; hậu kỳ (cắt, phụ đề, thumbnail 1 s) chạy được trên D:.

## Hàng đợi tập
| Mã | Tiêu đề | Ảnh | Trạng thái | File |
|---|---|---|---|---|
| MT-0001 | Khi câu hỏi nhỏ thành lời trách | 1.png | **`da-qa` — chờ chủ duyệt** | [tap/MT-0001.md](tap/MT-0001.md) |
| MT-0002 | Giúp bố mẹ, sao vợ lại buồn? | 2.png | `kich-ban` — chờ lệnh, cần rút về 4 cảnh | [tap/MT-0002.md](tap/MT-0002.md) |

## Tài nguyên đã biết
- Flow: tài khoản **MINH THƯ (trinhthu.hbl@gmail.com)**, gói PRO; 1.050 → còn ~990 credit sau MT-0001. Giá thật Omni 1.1 Flash 10 s = **15 credit**. Giới hạn 80/tập.
- Facebook: Page "Chuyện đời cùng Minh Thư" — đã đăng nhập & chuyển danh tính Page (30/09). Chưa thử đăng.
- Hậu kỳ: `D:\PODCAST VAN HANH\cong-cu\hauky.py` (bản sao `cong-cu/hauky.py`): analyze → cut → asr → srt → render. FFmpeg 4.4.2 (shell Linux) + faster-whisper trên D:.

## Việc tiếp theo
1. Chủ duyệt MT-0001 → Claude đăng Page "Chuyện đời cùng Minh Thư" (kiểm danh tính Page, thử chọn ảnh bìa), mở permalink xác minh, lưu bằng chứng `da-dang\MT-0001`.
2. Sau khi chủ xác nhận quy trình ổn định → tự đăng các tập sau.
3. Còn chờ: Q4 (repo private?), Q7 (TikTok/YT), Q8 (footer thumbnail, giờ đăng).

## Lịch sử phiên
- 2026-10-03: Khởi tạo repo; chủ quyết định bỏ cổng pilot, chạy theo lệnh, Claude thay Codex → [nhat-ky/2026-10-03.md](nhat-ky/2026-10-03.md)
