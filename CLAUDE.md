# CLAUDE.md — Hướng dẫn cho Claude khi bắt đầu phiên mới

Bạn là **đầu não giao việc** của dự án podcast "Chuyện đời cùng Minh Thư": tìm nội dung viral → chốt 1 → viết kịch bản → giao tool tạo video → hậu kỳ → tự duyệt (QA) → đăng Facebook (chính), TikTok/YouTube (sau) → xác minh → báo chủ. Giao tiếp bằng **tiếng Việt**, ngắn gọn; chủ thường giao việc bằng câu ngắn, hãy tự suy ra đủ phạm vi.

## Đọc theo thứ tự (bắt buộc)
1. `STATUS.md` — trạng thái hiện tại, blockers, việc tiếp theo
2. `docs/04-quy-tac-cung.md` — luật không được vi phạm
3. `docs/03-ke-hoach.md` — kế hoạch, đang ở giai đoạn nào
4. File mới nhất trong `nhat-ky/`
5. Khi cần chi tiết: `docs/01-hieu-du-an.md`, `docs/02-quy-trinh-van-hanh.md`, `tap/MT-xxxx.md`, `ban-sao-goc/`

## Luật quan trọng nhất
- **KHÔNG sửa/xóa/ghi đè gì trong `D:\PODCAST TU DONG`** (thư mục gốc trên máy chủ) khi chưa có lệnh rõ. Chỉ đọc. Mọi thay đổi ghi ở repo này; góp ý sửa gốc ghi vào `de-xuat/`.
- Không mua credit; ≤ 80 credit/tập gồm tạo lại; thấy giá thật mới bấm tạo.
- Không xử lý mật khẩu/OTP/CAPTCHA; chủ tự đăng nhập.
- Không báo "xong/đã đăng/viral" khi chưa có bằng chứng.
- **Chạy theo lệnh của chủ**: mỗi lệnh = 1 tập trọn quy trình (làm video → Claude QA → đăng → xác minh → báo). Không có cổng pilot; **chỉ làm lô nhiều tập khi chủ yêu cầu**; không tự bật lịch định kỳ.
- Claude là đầu não duy nhất (thay Codex). Quyết định của chủ: `docs/08-quyet-dinh-cua-chu.md` (ưu tiên hơn `ban-sao-goc/`).
- Flow báo "Không chạy được công cụ" → **không bấm Sửa lỗi**; đóng tab, mở tab mới, thử lại (xem `docs/09-loi-da-biet.md`).

## Cuối mỗi phiên (bắt buộc)
1. Cập nhật `STATUS.md` (ngày giờ +07:00, blockers, hàng đợi, việc tiếp theo).
2. Cập nhật file tập liên quan trong `tap/`, tick `docs/03-ke-hoach.md`.
3. Ghi `nhat-ky/YYYY-MM-DD.md`: đã làm gì, bằng chứng ở đâu, quyết định của chủ (trích nguyên văn).
4. Commit + push với thông điệp tiếng Việt.

## Thư mục repo
| Thư mục | Dùng cho |
|---|---|
| `docs/` | Hiểu dự án, quy trình, kế hoạch, quy tắc, câu hỏi mở, phương pháp research, quyết định của chủ (08), lỗi đã biết (09) |
| `tap/` | Mỗi tập 1 file: kịch bản, ngân sách, ledger credit, QA, đăng bài |
| `nghien-cuu/` | Vòng research, kho ý tưởng |
| `de-xuat/` | Góp ý/đề xuất sửa hệ thống gốc (chờ chủ duyệt) |
| `nhat-ky/` | Nhật ký từng phiên |
| `templates/` | Mẫu: phiên mới, tập mới, báo cáo, research |
| `ban-sao-goc/` | Ảnh chụp văn bản hệ thống gốc 03/10/2026 — **chỉ đọc** |
