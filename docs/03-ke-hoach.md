# 03 — Kế hoạch (PLAN)

Đánh dấu `[x]` khi xong **và có bằng chứng**. Cập nhật mỗi phiên. Giai đoạn sau chỉ mở khi giai đoạn trước đạt cổng.

## Giai đoạn 0 — Nền quản lý dự án ✅ (03/10/2026)
- [x] Đọc toàn bộ `D:\PODCAST TU DONG` (chỉ đọc)
- [x] Tạo repo GitHub, cấu trúc thư mục, bản sao văn bản hệ thống gốc
- [x] Viết mô tả hiểu dự án (`docs/01`) để chủ duyệt
- [ ] **Chủ xác nhận** `docs/01-hieu-du-an.md` đúng / sửa chỗ sai
- [ ] Chủ trả lời câu hỏi mở `docs/06-cau-hoi-mo.md` (ưu tiên Q1–Q4)

## Giai đoạn 1 — Chuyển giao "đầu não" sang Claude
- [ ] Thử built-in browser / Claude in Chrome: mở được Page Facebook dưới danh tính Page (chủ đăng nhập)
- [ ] Chốt môi trường hậu kỳ (Q3): ffmpeg + faster-whisper chạy ở đâu; thử lại trên fixture
- [ ] Chốt nơi lưu media sản xuất mới (Q2) — không ghi vào thư mục gốc nếu chưa được phép
- [ ] Viết lại checklist "ledger credit" + "chống đăng trùng" dạng file trên GitHub (thay `quan-ly.py` ghi vào D:)

## Giai đoạn 2 — Tool video (nút thắt chính)
- [ ] **Nhận tool video từ chủ** (link/hướng dẫn)
- [ ] Mở tool, xác nhận chạy được (không còn "Không chạy được công cụ")
- [ ] Ghi lại thật: model, giây/cảnh, giá x1, credit còn, cách dán thoại, cách chọn ảnh host
- [ ] Tìm bộ chọn **giọng** (Character voice): nghe mẫu nữ Bắc, ghi tên/ID
- [ ] Lập phương án ngân sách MT-0001 ≤ 80 credit (gồm 1 lần tạo lại)

## Giai đoạn 3 — Tập thử MT-0001 (pilot) — cổng quan trọng nhất
- [ ] Tạo cảnh 1 → nghe/xem → đạt
- [ ] Tạo các cảnh còn lại (4 cảnh dự kiến), tải clip, ghi hash + mã lượt
- [ ] Cắt ghép theo audio thật → ASR → nghe sửa → SRT → burn phụ đề
- [ ] Chèn thumbnail 1 s, dịch audio/SRT +1 s
- [ ] **Claude QA** đủ 13 mục, gắn SHA-256 master → báo chủ kèm bản xem trước
- [ ] Đăng Page slot 19:30 → mở permalink, phát được, chụp màn hình → `da-dang-xac-minh`
- [ ] Ghi kết quả chọn ảnh bìa Facebook (được/không)

## Giai đoạn 4 — Tìm nội dung viral có phương pháp
- [ ] Áp dụng `docs/07-phuong-phap-tim-viral.md` (baseline kênh, 2 lần đo tăng trưởng)
- [ ] Vòng research 2: đo lại 12 nguồn vòng 1 để có tăng trưởng thật + nguồn mới
- [ ] Cập nhật kho ý tưởng `nghien-cuu/kho-y-tuong.md` (≥ 10 ý sẵn sàng)

## Giai đoạn 5 — Lô 10 tập + lịch tự động (chỉ sau pilot)
- [ ] Lập 10 tập (MT-0002 … MT-0011), ảnh xoay theo số tập, không trùng mâu thuẫn liền kề
- [ ] Tạo scheduled task 19:30 VN; ghi id, điều kiện (máy bật, app mở, phiên còn hạn, STOP tắt)
- [ ] **Chạy thử 1 lượt lịch thật** từ đầu đến xác minh bài → mới gọi là "lịch hoạt động"
- [ ] Báo cáo tuần: số tập đã đăng, chỉ số bài, bài học

## Giai đoạn 6 — Mở rộng (sau khi Facebook ổn định)
- [ ] TikTok, YouTube Shorts (đăng lại cùng master, caption riêng từng nền tảng)
- [ ] Đo hiệu quả bài đăng (view, giữ chân, chia sẻ) → đưa ngược vào chấm điểm ý tưởng

## Rủi ro chính
| Rủi ro | Ứng phó |
|---|---|
| Tool video tiếp tục lỗi | Dừng, báo chủ; không tự đổi tool khác |
| Giọng không nhất quán giữa cảnh/tập | Khóa giọng bằng ID trong tool; nếu không có, báo giới hạn trước khi sản xuất lô |
| Giá credit cao hơn dự kiến | Rút kịch bản trước khi tạo (ít cảnh hơn), không bỏ cảnh giữa chừng |
| Phiên Facebook/Flow hết hạn khi chạy lịch | Dừng lượt đó, báo chủ đăng nhập lại, không đăng bù |
| Máy tắt lúc 19:30 | Bỏ slot, báo; cân nhắc hẹn lịch đăng trong Facebook từ trước |
