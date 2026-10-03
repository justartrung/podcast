# 03 — Kế hoạch (PLAN)

Đánh dấu `[x]` khi xong **và có bằng chứng**. Cập nhật mỗi phiên. Giai đoạn sau chỉ mở khi giai đoạn trước đạt cổng.

## Giai đoạn 0 — Nền quản lý dự án ✅ (03/10/2026)
- [x] Đọc toàn bộ `D:\PODCAST TU DONG` (chỉ đọc)
- [x] Tạo repo GitHub, cấu trúc thư mục, bản sao văn bản hệ thống gốc
- [x] Viết mô tả hiểu dự án (`docs/01`) để chủ duyệt
- [ ] **Chủ xác nhận** `docs/01-hieu-du-an.md` đúng / sửa chỗ sai
- [x] Chủ quyết định: bỏ cổng pilot, chạy theo lệnh, Claude thay Codex (`docs/08`, 03/10 17:00)
- [ ] Chủ trả lời câu hỏi mở còn lại `docs/06-cau-hoi-mo.md` (Q1–Q4, Q6–Q8)

## Giai đoạn 1 — Chuyển giao "đầu não" sang Claude
- [ ] Thử built-in browser / Claude in Chrome: mở được Page Facebook dưới danh tính Page (chủ đăng nhập)
- [x] Chốt môi trường hậu kỳ (Q3): FFmpeg trong shell Linux của Claude, faster-whisper cài vào D: (`docs/10`)
- [x] Cài faster-whisper vào `D:\PODCAST VAN HANH\cong-cu`, thử ASR + burn phụ đề tiếng Việt
- [x] Chốt nơi lưu media: `D:\PODCAST VAN HANH` (Q2)
- [x] Chủ tạo thư mục `D:\PODCAST VAN HANH`, Claude được cấp quyền
- [ ] Viết lại checklist "ledger credit" + "chống đăng trùng" dạng file trên GitHub (thay `quan-ly.py` ghi vào D:)

## Giai đoạn 2 — Tool video (nút thắt chính)
- [x] **Nhận tool video từ chủ**: Flow tool `6dae8db1…` (03/10 17:12)
- [x] Chủ đăng nhập Gmail trong trình duyệt của app Claude
- [x] Mở tool bằng **tab mới** (lỗi "Không chạy được công cụ" là do tab Codex — `docs/09`), xác nhận chạy được
- [x] Ghi lại thật: model, giây/cảnh, giá x1, credit còn, cách dán thoại, cách chọn ảnh host
- [x] Giọng: tool không có bộ chọn giọng → dùng mô tả chữ; kiểm bằng ASR + cao độ (F0 ~172–208 Hz, ổn định)
- [x] Lập phương án ngân sách MT-0001 ≤ 80 credit (gồm 1 lần tạo lại)

## Giai đoạn 3 — Tập đầu tiên MT-0001 (chạy khi chủ ra lệnh)
> 03/10: bỏ cổng pilot — đây là tập bình thường, không mở khóa gì.
- [x] Tạo cảnh 1 → nghe/xem → đạt
- [x] Tạo các cảnh còn lại (4 cảnh dự kiến), tải clip, ghi hash + mã lượt
- [x] Cắt ghép theo audio thật → ASR → nghe sửa → SRT → burn phụ đề
- [x] Chèn thumbnail 1 s, dịch audio/SRT +1 s
- [x] **Claude QA** đủ 13 mục, gắn SHA-256 master
- [ ] **Chủ xem & duyệt tập đầu**
- [ ] Đăng Page (giờ theo lệnh của chủ) → mở permalink, phát được, chụp màn hình → `da-dang-xac-minh`
- [ ] Ghi kết quả chọn ảnh bìa Facebook (được/không)

## Giai đoạn 4 — Tìm nội dung viral có phương pháp
- [ ] Áp dụng `docs/07-phuong-phap-tim-viral.md` (baseline kênh, 2 lần đo tăng trưởng)
- [ ] Vòng research 2: đo lại 12 nguồn vòng 1 để có tăng trưởng thật + nguồn mới
- [ ] Cập nhật kho ý tưởng `nghien-cuu/kho-y-tuong.md` (≥ 10 ý sẵn sàng)

## Giai đoạn 5 — Vận hành theo lệnh (thường xuyên)
- [ ] Mỗi lệnh của chủ → 1 tập trọn quy trình → báo cáo
- [ ] **Chỉ khi chủ yêu cầu:** làm lô nhiều tập (ảnh xoay theo số tập, không trùng mâu thuẫn liền kề) và/hoặc tạo lịch đăng định kỳ (scheduled task; chạy thử 1 lượt thật trước khi gọi là hoạt động)
- [ ] Báo cáo tổng hợp khi chủ hỏi: số tập đã đăng, chỉ số bài, bài học

## Giai đoạn 6 — Mở rộng (sau khi Facebook ổn định)
- [ ] TikTok, YouTube Shorts (đăng lại cùng master, caption riêng từng nền tảng)
- [ ] Đo hiệu quả bài đăng (view, giữ chân, chia sẻ) → đưa ngược vào chấm điểm ý tưởng

## Rủi ro chính
| Rủi ro | Ứng phó |
|---|---|
| Tool video báo "Không chạy được công cụ" | Không bấm Sửa lỗi; đóng tab, mở tab mới, thử ≤ 3 lần; vẫn lỗi → báo chủ (`docs/09`) |
| Giọng không nhất quán giữa cảnh/tập | Khóa giọng bằng ID trong tool; nếu không có, báo giới hạn trước khi sản xuất lô |
| Giá credit cao hơn dự kiến | Rút kịch bản trước khi tạo (ít cảnh hơn), không bỏ cảnh giữa chừng |
| Phiên Facebook/Flow hết hạn giữa chừng | Dừng, báo chủ đăng nhập lại, không đăng bù |
