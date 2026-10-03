# Điều kiện đạt

Không đạt chỉ bằng prompt, ảnh kết quả, toast render hoặc toast đăng bài. Các bước cần bằng chứng cụ thể.

| Cổng | Bằng chứng |
|---|---|
| Đầu vào | Hash ảnh khóa, số tập, thoại, CTA theo chủ đề, không lời chào |
| Flow | Đúng project/tool; model/giây/x1/giá; ledger tổng kể cả retry ≤80; clip tải được và phát được |
| Hình và giọng | Xem/nghe trọn từng clip và master; cùng ảnh/trang phục/bối cảnh, không méo nặng, lời đủ, một giọng ổn định |
| Cắt | Danh sách đoạn giữ, timestamp; không đứt từ, không đoạn lặp hoặc im lặng thừa; kết không lời chào |
| Phụ đề | Nhận dạng từ audio master sau cắt, timestamp, sửa nghe kiểm; không giả khớp bằng chia đều thoại; lệch đầu/cuối lời mục tiêu ≤0,25 giây |
| Kỹ thuật | FFprobe có audio/video, MP4 H.264/AAC, 9:16, ≤90s, decode không lỗi; phụ đề đọc được đúng dấu và trong lề an toàn |
| Nội dung | Chỉ chuyện gia đình, không bịa đời tư/nguồn; CTA đúng chủ đề |
| Xuất bản | Đúng Page; slot 19:30 Asia/Bangkok; không trùng ngày; permalink, screenshot, timestamp, phát bài thực tế và kiểm phụ đề/âm thanh |
| Tập thử | Master đã QA + bài thực tế đã đăng xác minh. Bài hẹn lịch chưa công khai chưa đạt cổng này |
| Lịch | Chỉ bật sau tập thử; lưu automation id, giờ/timezone, bằng chứng cấu hình; kiểm lượt chạy thực tế để xác nhận khả năng vận hành |

QA JSON lưu trong thư mục tập: `master_sha256`, `checks` gồm `family_content`, `host_consistency`, `no_greeting`, `topic_cta`, `complete_speech`, `cuts_reviewed`, `subtitle_audio_sync`, `technical`, `full_watch_listen`; `evidence_files`; `reviewed_at`; `reviewer`. Mọi check phải true và có file chứng cứ. Agent kiểm thực tế trước khi ký, không tự tạo tất cả true khi thiếu media.

Nếu QA hỏng, sửa đúng cảnh/đoạn; không rerender toàn tập khi không cần. Tối đa một retry mỗi cảnh trong ngân sách; lỗi sau retry dừng tập. Sửa master làm đổi hash phải QA lại.
# Cổng bổ sung trước xuất bản

QA bắt buộc: thumbnail 1080×1920, dấu tiếng Việt/ảnh/mặt đúng; intro đúng 30 frame ở 30 fps (1 giây); audio và SRT cùng dịch +1 giây; nghe/xem toàn bản sau chèn; MP4, thumbnail, caption và SRT đủ trong cùng thư mục 06-san-sang-dang/mã-tập. Thumbnail riêng không phải bằng chứng đã sản xuất tập. Kiểm khả năng chọn ảnh bìa Facebook và ghi nhận kết quả thật. Lịch chỉ đạt khi thử lượt thực sự chạy cả quy trình, không dùng heartbeat nhắc việc để báo đạt.

