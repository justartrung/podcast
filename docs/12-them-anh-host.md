# 12 — Thêm / thay ảnh host

## Chủ làm
1. Chép ảnh vào `D:\PODCAST VAN HANH\host\` — tên số tiếp theo (`5.png`, `6.png`…). Ảnh dọc, rõ mặt, ánh sáng đều, không chữ/logo.
2. Tải đúng ảnh đó lên thư viện Flow (dự án PODCAST): tool → Tải ảnh → **Tải nội dung lên** (cần chọn file trên Windows).
3. Nhắn Claude theo mẫu:
   `Thêm host <tên file> — <cách dùng> — áp dụng từ tập MT-xxxx`
   Cách dùng: `thêm vào vòng xoay` · `thay ảnh N` · `chỉ dùng cho tập MT-xxxx` · `cho ảnh N nghỉ`

## Claude làm
1. Xem ảnh: rõ mặt, không méo, không chữ; hợp tỷ lệ 9:16 (cắt khung không mất đầu/cằm).
2. Tính SHA-256, ghi mô tả trang phục/bối cảnh vào `host/README.md`.
3. Kiểm ảnh có trong thư viện Flow (tìm theo tên file).
4. Cập nhật quy tắc xoay trong `host/README.md` **có ngày + tập bắt đầu áp dụng**; tập đã làm/đã đăng giữ ảnh cũ.
5. Ghi quyết định vào `docs/08-quyet-dinh-cua-chu.md`, nhật ký, commit.

## Quy tắc
- Một tập = một ảnh, khóa suốt tập (cả khi tạo lại).
- Ảnh gốc `D:\PODCAST TU DONG\02-host\1–4.png` không sửa; ảnh mới chỉ để ở `D:\PODCAST VAN HANH\host\`.
- Đổi vòng xoay không áp ngược cho tập đã có kịch bản/clip trừ khi chủ nói.

## Đổi trang phục tự động (đề xuất 04/10/2026 — **chờ thử lần đầu** trước khi bật)
Chủ không cần tự làm ảnh host mới hay đặt tên file:
1. Chủ thả ảnh **mẫu quần áo** (chụp/tải về, 1 bộ/ảnh, tên gì cũng được) vào `D:\PODCAST VAN HANH\host\trang-phuc\`. Có thể kèm 1 dòng trong tên file nếu muốn dùng cho chủ đề nào (vd `ao-dai-tet.jpg`).
2. Mỗi lượt hằng ngày: nếu `trang-phuc\` còn mẫu chưa dùng → lấy mẫu cũ nhất → trong Flow tạo **ảnh host mới = ảnh host theo vòng xoay (giữ nguyên mặt, tóc, bối cảnh) + mặc bộ đó** → QA (mặt giống ảnh gốc, tay/cổ không méo, không chữ/logo, 9:16) → lưu `host\N.png` + sha256 vào `host/README.md` → dời mẫu sang `trang-phuc\da-dung\` (mv, không xóa) → dùng cho tập.
3. Không có mẫu mới → dùng ảnh theo vòng xoay như cũ.
4. Credit tạo ảnh tính vào trần 80/tập; thấy giá thật mới bấm. QA mặt không đạt sau 1 lần tạo lại → dùng ảnh cũ, báo chủ.
Trước khi bật: Claude thử với mẫu đầu tiên chủ gửi (giá, độ giống mặt), gửi ảnh cho chủ duyệt.
