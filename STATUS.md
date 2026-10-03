# STATUS — Trạng thái hiện tại

> **Đọc file này đầu tiên mỗi phiên.** Cập nhật cuối mỗi phiên.
> Cập nhật lần cuối: **2026-10-03 17:20 (+07:00)** — Claude, phiên 1.

## Tổng quan
| Mục | Giá trị |
|---|---|
| Đầu não | **Claude — duy nhất**, thay Codex điều phối toàn bộ (chủ xác nhận 03/10 17:00) |
| Cách chạy | **Theo lệnh của chủ**: mỗi lệnh = 1 tập trọn quy trình (video → QA → đăng → xác minh → báo). Không cổng pilot. Lô nhiều tập / lịch định kỳ **chỉ khi chủ yêu cầu** |
| STOP | Tắt |
| Giai đoạn hiện tại | **1–2**: đã có tool video + nơi lưu; chờ chủ đăng nhập Flow & tạo thư mục `D:\PODCAST VAN HANH` |
| Tool video | Flow `…/project/f37b741b-b3f2-40f8-b490-f23f79b098ed/tool/6dae8db1-89cf-475a-9412-3334f68ebfdd` |
| Thư mục ghi | `D:\PODCAST VAN HANH` (`docs/10`). Mọi tải về để ổ D (ổ C đầy) |
| Duyệt đăng | Tập đầu: **chủ xem trước**. Ổn định rồi → Claude tự đăng |
| Tập đã đăng | 0 (0 clip, 0 credit dùng) |

## Đang chặn (blockers)
1. **Flow chưa đăng nhập** trong trình duyệt của app Claude (đã mở link 17:15, bị chuyển về trang giới thiệu) → chủ đăng nhập Gmail.
2. **Thư mục `D:\PODCAST VAN HANH` chưa có** → chủ tạo, Claude xin quyền.
3. **Giá credit / giây mỗi cảnh / model / giọng nữ Bắc** chưa quan sát trên tool mới.
4. Lỗi "Không chạy được công cụ" nếu gặp → tab mới, thử ≤ 3 lần (`docs/09`).

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
1. Chủ đăng nhập Flow → Claude mở link tool, ghi giá/model/giọng/cách dùng.
2. Chủ tạo `D:\PODCAST VAN HANH` → Claude cài faster-whisper vào đó, thử phụ đề.
3. Sản xuất MT-0001 → chủ xem duyệt → đăng.
4. Còn chờ: Q4 (repo private?), Q7 (TikTok/YT), Q8 (footer thumbnail, gói Flow, giờ đăng).

## Lịch sử phiên
- 2026-10-03: Khởi tạo repo; chủ quyết định bỏ cổng pilot, chạy theo lệnh, Claude thay Codex → [nhat-ky/2026-10-03.md](nhat-ky/2026-10-03.md)
