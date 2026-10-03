# STATUS — Trạng thái hiện tại

> **Đọc file này đầu tiên mỗi phiên.** Cập nhật cuối mỗi phiên.
> Cập nhật lần cuối: **2026-10-03 17:15 (+07:00)** — Claude, phiên khởi tạo repo.

## Tổng quan
| Mục | Giá trị |
|---|---|
| Sẵn sàng vận hành | ❌ **Chưa** (`not_ready`) |
| STOP | Tắt (theo `STOP.json` gốc 30/09) |
| Đầu não | Claude (từ 03/10/2026). Hệ thống gốc do Codex dựng 30/09/2026 |
| Giai đoạn hiện tại | **0 → 1**: repo xong, chờ chủ duyệt mô tả + trả lời câu hỏi mở |
| Pilot MT-0001 | Chưa sản xuất (0 clip, 0 credit dùng) |
| Lô 10 tập / Lịch 19:30 | Tắt — chờ pilot |
| Lịch research hàng tuần | Tắt |

## Đang chặn (blockers)
1. **Tool video chưa chạy** — Flow tool `10a20665…` báo "Không chạy được công cụ" (30/09). Chủ sẽ gửi tool → xem Q1.
2. **Giá credit / giây mỗi cảnh / model** chưa quan sát thật trên tool.
3. **Giọng nữ Bắc** chưa chọn được (chưa thấy bộ chọn giọng).
4. **Nơi lưu media mới** và **môi trường hậu kỳ** chưa chốt (Q2, Q3).
5. Lịch tự động chưa thể bật (chờ pilot đăng thật + chạy thử lượt lịch).

## Hàng đợi tập
| Mã | Tiêu đề | Ảnh | Trạng thái | File |
|---|---|---|---|---|
| MT-0001 | Khi câu hỏi nhỏ thành lời trách | 1.png | `cho-tool` (kịch bản + thumbnail + caption xong) | [tap/MT-0001.md](tap/MT-0001.md) |
| MT-0002 | Giúp bố mẹ, sao vợ lại buồn? | 2.png | `kich-ban` — giữ chờ pilot | [tap/MT-0002.md](tap/MT-0002.md) |

## Tài nguyên đã biết
- Flow: tài khoản hiển thị "Quanly Youtube", **1.050 credit** (quan sát 30/09 16:04). Giới hạn 80/tập.
- Facebook: Page "Chuyện đời cùng Minh Thư" — đã đăng nhập & chuyển danh tính Page (30/09). Chưa thử đăng.
- Hậu kỳ: FFmpeg 9.0.2 + faster-whisper small (bản Windows trong `08-cong-cu`), test fixture đạt.

## Việc tiếp theo (theo thứ tự)
1. Chủ đọc `docs/01-hieu-du-an.md`, trả lời `docs/06-cau-hoi-mo.md` (Q1–Q4 trước).
2. Chủ gửi tool video → Claude mở thử, ghi giá/model/giọng.
3. Chốt nơi lưu media + môi trường hậu kỳ → chạy pilot MT-0001.

## Lịch sử phiên
- 2026-10-03: Khởi tạo repo, đọc toàn bộ dự án gốc, lập kế hoạch → [nhat-ky/2026-10-03.md](nhat-ky/2026-10-03.md)
