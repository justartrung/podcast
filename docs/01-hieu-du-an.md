# 01 — Claude hiểu dự án như thế nào

> Tài liệu này để **anh/chị chủ dự án xem và sửa**. Chỗ nào Claude hiểu sai, ghi vào `docs/06-cau-hoi-mo.md` hoặc nhắn trong chat, Claude sẽ cập nhật.
> Nguồn: đọc toàn bộ `D:\PODCAST TU DONG` ngày 03/10/2026 (chỉ đọc, không sửa). Bản sao văn bản ở `ban-sao-goc/`.

## 1. Dự án là gì

**Kênh:** "Chuyện đời cùng Minh Thư" — Page Facebook `facebook.com/chuyendoicungminhthu`.
**Sản phẩm:** video podcast dọc 9:16, dưới 90 giây, một host AI tên **MINH THƯ** (nữ, tóc ngắn nâu, studio gỗ, sofa da, micro bên trái) kể **chuyện gia đình đời thường** — vợ chồng, cha mẹ–con, mẹ chồng–nàng dâu, tiền bạc trong nhà, việc nhà, ranh giới hai bên, giao tiếp.
**Mục tiêu:** một dây chuyền gần như tự động: tìm nội dung đang được quan tâm → chốt 1 chủ đề → viết kịch bản gốc → giao tool tạo video (Google Flow) → hậu kỳ (cắt, phụ đề, thumbnail) → kiểm chất lượng → đăng Facebook đúng lịch (19:30 mỗi ngày) → xác minh bài đăng → báo cáo cho chủ.

**Vai trò của Claude (từ 03/10/2026):** "đầu não giao việc" — điều phối toàn bộ quy trình, tự duyệt và chốt theo quality gate, rồi báo lại chủ. Trước đó vai trò này do **Codex (OpenAI)** đảm nhiệm với tên "Agent Tổng" — toàn bộ hệ thống trong `D:\PODCAST TU DONG` được dựng bởi Codex ngày 30/09/2026 theo cẩm nang "Công xưởng Subagent" của Phong Menly.

## 2. Luật nội dung (yêu cầu của chủ ngày 30/09, ưu tiên hơn mọi tài liệu gốc)

| Luật | Chi tiết |
|---|---|
| Chủ đề | **Chỉ chuyện gia đình**. Không tôn giáo, không tư vấn y tế/pháp lý/tài chính. Tình huống là hư cấu minh họa, không gán cho người thật, không kể đời tư chủ kênh. |
| Mở đầu | Vào thẳng hook — **không lời chào**. |
| Kết | Câu chốt + **một CTA hợp chủ đề** (thường là câu hỏi mở). **Không** "cảm ơn đã lắng nghe", **không** "xin chào/hẹn gặp lại", **không** CTA follow mặc định. (Lưu ý: skill gốc trong `01-tai-lieu/Podcast-Minh-Thu-CTA.zip` bắt buộc có lời chào — **đã bị yêu cầu mới thay thế**.) |
| Host | 4 ảnh `02-host/1..4.png` **xoay theo số tập** (tập 1→ảnh 1, 2→2, 3→3, 4→4, 5→1 …). **Một ảnh khóa suốt một tập**, kể cả khi tạo lại. Kiểm hash SHA-256 trước khi dùng. |
| Giọng | Nữ miền Bắc, trưởng thành, trầm ấm, kể tự nhiên. Chỉ dùng giọng có sẵn trong Flow (Character voice), không clone/TTS ngoài. Phải nghe thử mới khóa. |
| Kịch bản | Viết **gốc**, không chép lời nguồn, không reup. Kiểm không trùng mâu thuẫn với tập liền trước. |
| Video | 9:16, ≤ 90 giây, không nhạc. Cắt im lặng thừa/đoạn lặp/đoạn lỗi theo **âm thanh thật**, không cắt đứt âm tiết. |
| Phụ đề | Làm từ **audio thật sau khi cắt** (faster-whisper) rồi nghe sửa; lệch ≤ 0,25 s. Không chia đều kịch bản theo thời lượng. |
| Thumbnail | 1080×1920, nền đen–vàng ánh kim, tiêu đề IN HOA chữ có chân vàng nổi 2–3 dòng phía trên, ảnh host giữa/dưới (không méo, chữ không che mặt), dải chân "COACH MINH THƯ". **Chèn đúng 1 giây (30 frame @30fps) đầu video**, audio + SRT dịch +1 s. |
| Bàn giao mỗi tập | `06-san-sang-dang/<mã-tập>/` gồm `final.mp4`, `thumbnail.png`, `caption.txt`, `subtitles.srt`. |

## 3. Luật vận hành & ngân sách

- **Flow:** tối đa **80 credit/tập, tính cả tạo lại**; tối đa 1 lần tạo lại mỗi cảnh; **không mua credit**; chỉ tạo x1; phải **thấy giá thật trên giao diện** trước khi bấm tạo (không có giá → dừng). Ghi "reservation" chi phí trước mỗi lượt.
- **Facebook:** được phép đăng vào đúng Page trên, dưới danh tính Page. Chống đăng trùng: ghi ý định đăng trước khi bấm; nếu timeout → trạng thái `publishing_unknown`, kiểm Page trước, **không bấm đăng lại mù**.
- **Lịch:** 1 tập/ngày, 19:30 giờ VN (Asia/Bangkok = UTC+7). Lỡ slot thì bỏ qua và báo, **không đăng bù dồn**.
- **Cổng tập thử (pilot):** Chỉ khi tập thử MT-0001 được **đăng thật, phát được, có permalink + ảnh chụp + QA** thì mới mở **lô 10 tập** và **bật lịch**. Lịch hẹn chưa công khai không tính.
- **STOP:** `03-he-thong/STOP.json` (enabled=true) hoặc file `STOP.now` ở gốc → dừng trước mọi thao tác tốn credit/đăng/bật lịch. Chỉ gỡ STOP khi chủ ra lệnh.
- **Đăng nhập/OTP/CAPTCHA:** chủ tự làm. Không lưu mật khẩu, cookie, token.
- **Cài thêm phần mềm:** phải có "Phiếu đề xuất" được chủ duyệt. Đã duyệt: FFmpeg/FFprobe 9.0.2 portable và faster-whisper 1.2.1 + model small (CPU int8).
- **Không báo "xong/sẵn sàng" khi chưa có bằng chứng thật** (toast render, ảnh thumbnail, cấu hình… đều không phải bằng chứng đã sản xuất).

## 4. Quy trình một tập (12 bước của Agent Tổng — rút gọn)

1. Đọc STOP, trạng thái, hàng đợi, nhật ký. Mỗi lần chỉ lấy 1 tập.
2. Kiểm đăng nhập Flow (đúng project/tool) và Facebook (quyền Page).
3. Khóa ảnh host theo số tập + kiểm hash.
4. Viết kịch bản chuyện gia đình, CTA theo chủ đề, không chào.
5. Mở tool Flow, **ghi lại model, giây/cảnh, giá x1, credit còn**. Lập phương án ≤ 80 credit gồm dự phòng.
6. Ghi reservation → tạo **cảnh 1** → nghe/xem → đạt mới tạo các cảnh còn lại.
7. Tải clip, nghe trọn, chọn đoạn giữ, ghi timestamp cắt, ghép.
8. Nhận dạng lời (ASR) → nghe sửa → SRT → burn phụ đề.
9. Thumbnail + chèn 1 s đầu → kiểm kỹ thuật (FFprobe, H.264/AAC, 9:16, ≤ 90 s) → xem/nghe trọn → QA JSON gắn SHA-256 master.
10. Ghi ý định đăng → đăng Page slot 19:30 (hoặc hẹn lịch Facebook).
11. Mở permalink, kiểm tên Page, caption, phát video/phụ đề, lưu bằng chứng.
12. Tập thử đạt → mới lập lô 10 + bật lịch.

## 5. Vòng tìm nội dung (research)

- Nguồn công khai tiếng Việt trên **Facebook, TikTok, YouTube**; ưu tiên 30–90 ngày gần nhất; mỗi vòng ≥ 10 nội dung từ ≥ 5 kênh.
- Ghi link, kênh, ngày đăng, chỉ số **kèm nhãn rõ** (like ≠ view), mức độ đã xem (cả video / chỉ caption / chỉ chỉ mục).
- **Không được gọi là "viral" nếu chưa có bằng chứng**: phải so với baseline của chính kênh, tuổi bài, và tăng trưởng qua ≥ 2 lần kiểm.
- Chấm điểm 0–5 (phù hợp, tiềm năng, góc mới, bằng chứng) → đề xuất 5 ý tưởng → **tự chọn 1** → viết kịch bản gốc → QA văn bản → đưa vào hàng đợi.
- Vòng 1 (30/09): 12 nội dung / 11 kênh — **chưa nội dung nào xác nhận viral** (thiếu chuỗi tăng trưởng). Chọn I01 → tập MT-0002.

## 6. Trạng thái thật tại thời điểm đọc (dữ liệu dừng ở 30/09/2026 16:18)

| Hạng mục | Trạng thái |
|---|---|
| Tổng | **`not_ready`** — chưa sản xuất được tập nào |
| Tool Flow (project `286e14cd…`, tool `10a20665…`, tên "Podcast Chuyên Nghiệp CODEX") | Đăng nhập được, tài khoản "Quanly Youtube", còn **1.050 credit**, nhưng tool báo **"Không chạy được công cụ"**. Chưa thấy bộ chọn giọng. **Chưa tạo lượt nào, 0 credit đã dùng.** Tool cũ (`806639af…`) đã ngừng dùng. |
| Facebook | Đã đăng nhập, chuyển sang danh tính Page, thấy Manage Page/Reel. **Chưa thử đăng.** |
| Hậu kỳ cục bộ | FFmpeg 9.0.2 + faster-whisper small chạy được; test trên video giả (nền xanh/âm sin) đạt. Chưa thử với giọng thật. |
| MT-0001 "Khi câu hỏi nhỏ thành lời trách" (ảnh 1) | Có kịch bản (bản 6 đoạn + bản rút gọn 4 cảnh), phương án ngân sách 4×15 + 15 dự phòng = 75 credit (giá tham khảo Google, **chưa xác minh trên tool**), thumbnail + caption đã làm. **Chưa có clip.** |
| MT-0002 "Giúp bố mẹ, sao vợ lại buồn?" (ảnh 2) | Kịch bản + QA văn bản đạt. Đang `production_hold` chờ pilot. |
| Lô 10 tập, lịch 19:30, lịch research hàng tuần | **Tắt.** Chưa có automation. |

## 7. Điểm then chốt Claude rút ra

1. **Nút thắt số 1 là tool video.** Mọi thứ khác (kịch bản, hậu kỳ, thumbnail, Facebook) đã sẵn sàng ở mức cấu hình; nhưng Flow tool không chạy nên chưa có clip nào. Anh/chị nói sẽ gửi tool → đây là việc đầu tiên khi nhận.
2. **Hệ thống cũ gắn chặt với Codex** (`cua_repl` để điều khiển trình duyệt, `automation_update` để đặt lịch, Python tại `C:/Users/start/.cache/codex-runtimes/...`). Claude không dùng được các công cụ đó; cần ánh xạ sang công cụ của Claude (xem `docs/02-quy-trinh-van-hanh.md`).
3. **Đường dẫn cũ đã lệch:** `kiem-ke.json` trỏ `D:\_CHUYEN NGHE TRADE_\PODCAST TU DONG\...` nhưng thư mục hiện ở `D:\PODCAST TU DONG`.
4. **Giọng nhất quán xuyên tập** chưa giải được: Flow chưa cho thấy bộ chọn giọng; nếu Character khóa cả ngoại hình thì xung đột với luật xoay 4 ảnh.
5. Quy tắc "không sửa thư mục gốc" của anh/chị → **mọi trạng thái mới, kế hoạch, góp ý sẽ ghi trên GitHub**. Riêng media (clip, master) không đưa lên GitHub được — cần chốt nơi lưu (xem câu hỏi mở).
