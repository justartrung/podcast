# STATUS — Trạng thái hiện tại

> **Đọc file này đầu tiên mỗi phiên.** Cập nhật cuối mỗi phiên.
> Cập nhật lần cuối: **2026-10-03 17:10 (+07:00)** — Claude, phiên 1 (khởi tạo + cập nhật quyết định của chủ).

## Tổng quan
| Mục | Giá trị |
|---|---|
| Đầu não | **Claude — duy nhất**, thay Codex điều phối toàn bộ (chủ xác nhận 03/10 17:00) |
| Cách chạy | **Theo lệnh của chủ**: mỗi lệnh = 1 tập trọn quy trình (video → QA → đăng → xác minh → báo). Không cổng pilot. Lô nhiều tập / lịch định kỳ **chỉ khi chủ yêu cầu** |
| STOP | Tắt |
| Giai đoạn hiện tại | **1–2**: chờ chủ gửi tool video + trả lời Q1–Q4 |
| Tập đã đăng | 0 (0 clip, 0 credit dùng) |

## Đang chặn (blockers)
1. **Chưa nhận tool video** từ chủ (Q1). Lỗi cũ "Không chạy được công cụ" là do **tab trình duyệt Codex**, không phải tool hỏng → mở bằng tab mới, thử vài lần (`docs/09-loi-da-biet.md`).
2. **Giá credit / giây mỗi cảnh / model / giọng nữ Bắc** chưa quan sát thật trên tool.
3. **Nơi lưu media mới** (Q2) và **môi trường hậu kỳ** (Q3) chưa chốt.

## Hàng đợi tập
| Mã | Tiêu đề | Ảnh | Trạng thái | File |
|---|---|---|---|---|
| MT-0001 | Khi câu hỏi nhỏ thành lời trách | 1.png | `cho-tool` (kịch bản 4 cảnh + thumbnail + caption xong) | [tap/MT-0001.md](tap/MT-0001.md) |
| MT-0002 | Giúp bố mẹ, sao vợ lại buồn? | 2.png | `kich-ban` — chờ lệnh, cần rút về 4 cảnh | [tap/MT-0002.md](tap/MT-0002.md) |

## Tài nguyên đã biết
- Flow: tài khoản hiển thị "Quanly Youtube", **1.050 credit** (quan sát 30/09). Giới hạn 80/tập gồm tạo lại.
- Facebook: Page "Chuyện đời cùng Minh Thư" — đã đăng nhập & chuyển danh tính Page (30/09). Chưa thử đăng.
- Hậu kỳ: FFmpeg 9.0.2 + faster-whisper small (bản Windows trong `08-cong-cu`), test fixture đạt.

## Việc tiếp theo
1. Chủ gửi tool video → Claude mở bằng **tab mới**, ghi giá/model/giọng.
2. Chủ trả lời Q2 (nơi lưu media), Q3 (hậu kỳ), Q4 (repo private?), Q6 (tự đăng hay xem trước), Q8 (giờ đăng).
3. Khi chủ ra lệnh → sản xuất MT-0001 trọn quy trình.

## Lịch sử phiên
- 2026-10-03: Khởi tạo repo; chủ quyết định bỏ cổng pilot, chạy theo lệnh, Claude thay Codex → [nhat-ky/2026-10-03.md](nhat-ky/2026-10-03.md)
