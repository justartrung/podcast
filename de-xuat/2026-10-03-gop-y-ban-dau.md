# Góp ý ban đầu sau khi đọc hệ thống gốc — 03/10/2026

Trạng thái: **chờ chủ duyệt**. Chưa áp dụng vào `D:\PODCAST TU DONG`.

## A. Điểm lệch / lỗi thời phát hiện
| # | Ở đâu | Vấn đề | Đề xuất |
|---|---|---|---|
| A1 | `03-he-thong/kiem-ke.json` (`ffmpeg`, `ffprobe`, `asr_python`) | Trỏ `D:\_CHUYEN NGHE TRADE_\PODCAST TU DONG\...` — thư mục đã chuyển sang `D:\PODCAST TU DONG` | Sửa đường dẫn hoặc dùng đường dẫn tương đối từ gốc dự án |
| A2 | `kiem-ke.json` vs `bao-cao-kiem-thu.md` | Một nơi ghi gói Flow **PRO**, nơi kia ghi **ULTRA** | Xác nhận lại trên giao diện Flow |
| A3 | `registry.json` | Agent `flow` = `awaiting_login`, trong khi `kiem-ke.json` báo đã đăng nhập | Đồng bộ trạng thái |
| A8 | `AGENTS.md`, `agent-tong.md`, `quality-gate.md`, `cau-hinh-kenh.json` (schedule, batch) | Còn ghi cổng pilot, lô 10, lịch 19:30 — chủ đã bỏ 03/10 | Khi được phép sửa gốc: cập nhật theo `docs/08-quyet-dinh-cua-chu.md` |
| A4 | `AGENTS.md`, `van-hanh.md`, `agent-tong.md` | Gắn với công cụ Codex (`cua_repl`, `automation_update`, Python codex-runtimes) | Viết phiên bản trung lập/Claude (xem `docs/02-quy-trinh-van-hanh.md`) |
| A5 | `06-san-sang-dang/MT-0001/caption.txt` vs caption trong `kich-ban.md` | Hai bản caption khác nhau; bản bàn giao ngắn, hashtag khác | Chốt 1 bản trước khi đăng (Claude đề xuất dùng bản trong kịch bản, 4 hashtag) |
| A6 | `01-tai-lieu/Podcast-Minh-Thu-CTA.zip` | Skill gốc bắt buộc lời chào + CTA follow — trái yêu cầu 30/09 | Đánh dấu rõ "đã thay thế" để agent không áp nhầm |
| A7 | `08-cong-cu/` | Có 3 bản zip ffmpeg trùng nhau trong `downloads/` (~vài trăm MB) | Có thể dọn khi chủ đồng ý (không tự xóa) |

## B. Đề xuất cải tiến
1. **Một nguồn trạng thái duy nhất:** dùng GitHub (`STATUS.md`, `tap/*.md`) làm sổ chính; thư mục D: chỉ chứa media. Tránh 2 nơi lệch nhau.
2. **Thư mục media riêng** cho phần sản xuất mới (Q2) để không đụng dữ liệu gốc.
3. ~~Hẹn lịch trên Facebook từ trước thay vì phụ thuộc máy bật đúng 19:30~~ — không còn cần vì chủ đã chuyển sang chạy theo lệnh (03/10). Vẫn có thể dùng hẹn lịch Facebook nếu chủ muốn đăng vào giờ cố định.
4. **Research đo 2 lần:** mỗi tuần đo lại nguồn tuần trước để có tăng trưởng thật (xem `docs/07`).
5. **Rút kịch bản về ~100 tiếng/4 cảnh** làm chuẩn mặc định để luôn còn dự phòng tạo lại trong 80 credit (khi giá 15/cảnh).
