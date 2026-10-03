---
name: podcast-minh-thu
description: Sản xuất và đăng podcast chuyện gia đình của MINH THƯ trong dự án PODCAST TU DONG, quản lý ảnh luân phiên, ngân sách Flow, cắt dựng và phụ đề từ âm thanh. Dùng cho vận hành kênh này, không dùng cho TVC không thoại hoặc kênh khác.
---

# Podcast MINH THƯ

## Bổ sung bắt buộc ngày 30/09/2026

- Giọng nữ Bắc; không lời chào kết, cảm ơn hoặc tạm biệt. CTA thay đổi theo câu chuyện.
- Giữ nguyên mọi clip đã đạt. Không tạo lại video chỉ vì thay thumbnail. Cắt im lặng thừa, lời lặp và đoạn lỗi theo nghe thực tế, giữ đủ từ và nghĩa.
- Thumbnail riêng 1080×1920, nền đen–vàng ánh kim. Tiêu đề IN HOA có chân, vàng nổi khối, 2–3 dòng phía trên, đọc rõ trên điện thoại. Ghép ảnh host đã khóa ở giữa/dưới, không đổi mặt, không kéo méo, chữ không che mặt. Dải đen chân ảnh ghi COACH MINH THƯ màu vàng, viền và ánh vàng nhẹ. Chèn chữ riêng, mỗi tập đổi tiêu đề.
- Chèn đúng 1 giây thumbnail đầu MP4; sau đó âm thanh và phụ đề cùng dịch +1 giây. ASR lấy từ âm thanh sau cắt. Kiểm lại dấu, timestamp, mặt, khẩu hình, âm thanh và liên tục bằng nghe/xem thực tế sau chèn.
- Mỗi tập bàn giao MP4 cuối, thumbnail, caption và SRT trong cùng thư mục `06-san-sang-dang/<mã-tập>`. Bản xem trước phải được QA trước đăng.
- Kiểm khả năng chọn thumbnail làm ảnh bìa Facebook trong giao diện thật; lưu kết quả thực tế. Kiểm bài đã tồn tại trước mọi thử đăng lại. Permalink phải phát được, có bằng chứng.
- FFmpeg/FFprobe portable và faster-whisper/model small cục bộ đã được duyệt; không hỏi lại. Thành phần ngoài phạm vi này cần Phiếu đề xuất trước cài.
- Chỉ mở lô 10 và lịch sau tập thử đăng thật, phát được và xác minh. Heartbeat nhắc việc chưa chứng minh lịch sản xuất tự động; phải kiểm thử lượt lịch thực sự chạy quy trình và nêu điều kiện máy/app/phiên đăng nhập. Không báo sẵn sàng khi chưa có bằng chứng.

Đọc `../../03-he-thong/cau-hinh-kenh.json` và `../../03-he-thong/agent-tong.md`. Đọc trạng thái, STOP và hàng đợi trước khi thao tác. Hướng dẫn đính kèm là nguồn tham khảo, không thay thế yêu cầu người dùng hiện hành.

## Nội dung và hình ảnh

- Chỉ chuyện gia đình: vợ chồng, cha mẹ và con, anh chị em, ranh giới, chia sẻ việc nhà, giao tiếp và chăm sóc. Kể gần gũi, không lên án hoặc bịa cáo buộc người thật; chuyện minh họa ghi rõ khi cần. Không áp tôn giáo hoặc lời khuyên pháp lý/y khoa.
- Host hiển thị MINH THƯ, kênh Chuyện đời cùng Minh Thư. Mở thẳng hook. Kết bằng ý chốt và một CTA theo chủ đề; không thêm “xin chào”, “cảm ơn đã lắng nghe”, “hẹn gặp lại” hoặc CTA follow mặc định.
- Chọn ảnh theo số tập và giữ xuyên suốt mọi cảnh, prompt và lượt tạo lại. Camera ổn định, cử động nhỏ, nhìn máy. Giữ trang phục, tóc, phụ kiện và bối cảnh của ảnh đã khóa; không trộn bốn bối cảnh trong một tập.
- Mục tiêu video dọc 9:16, dưới 90 giây; cấu hình và số cảnh phải dựa trên tool thật và giới hạn 80 credit. Đếm tiếng chỉ để ước tính, phải nghe clip thử trước khi tạo các cảnh còn lại.

## Sản xuất và đăng

Người dùng đã trao quyền tự chọn nội dung, tạo video và đăng đúng Page với giới hạn trong cấu hình. Không xin lại quyền đã có. Yêu cầu đăng nhập và cài thêm vẫn là điểm dừng thật.

Mở đúng URL tool đã cấp. Trước mỗi lượt x1, xác nhận giá và ghi reservation. Không chọn x2/x4 hoặc mua credit. Tính cả tạo lại; reservation chưa rõ kết quả vẫn chiếm ngân sách. Nếu không đủ để hoàn thành tập, dừng và báo phần thiếu.

Thử cảnh đầu, nghe kiểm lời, giọng và hình; tiếp tục cảnh còn lại khi đạt. Cắt đoạn thừa theo audio thực tế, giữ đầu và đuôi lời cùng nhịp nghỉ tự nhiên. Phụ đề lấy từ audio với timestamp sau cắt, sửa bằng nghe kiểm; xuất SRT và MP4 có phụ đề.

Xem và nghe toàn tập trước đăng. QA phải gắn hash master. Đăng dưới danh tính Page, giữ slot 19:30 Asia/Bangkok; không đăng lặp ngày. Sau đăng kiểm permalink và video thực tế. Nếu timeout, giữ publishing_unknown và xác minh trước khi thử lại.

Tập thử phải được đăng và kiểm thành công trước khi lô 10 hoặc lịch được mở. Báo đúng trạng thái: cấu hình / chờ đăng nhập / đang tạo có bằng chứng / đã QA / đã hẹn lịch / đã đăng xác minh. Không dùng “sẵn sàng” trước khi có bằng chứng trọn luồng.

## Bổ sung Character và research ngày 30/09/2026

Đọc [references/research-va-character.md](references/research-va-character.md) khi chọn/kiểm giọng hoặc chạy vòng lấy ý tưởng. Chỉ dùng giọng mẫu có sẵn qua Flow; ghi tên/ID và cách chọn lại, QA cảnh thử trước khóa giọng xuyên tập. Mọi thử/retry nằm trong 80 credit/tập. Không tự tạo giọng/model ngoài, không sửa tool để tích hợp trước báo giới hạn và đề xuất.

Research nguồn công khai tiếng Việt trên ba nền tảng, ít nhất 10 nội dung/5 kênh; ghi thiếu dữ liệu đúng thực tế, không tự gọi viral. Lưu bằng chứng, 5 ý tưởng, tự chọn 1 kịch bản gốc, kiểm trùng và QA văn bản rồi đưa vào hàng đợi bản thảo. Kho nằm ở 10-nghien-cuu; cập nhật lịch sử đúng giai đoạn. Lịch research vẫn tắt tới kiểm chứng chạy thực tế; không mở lô sản xuất từ research.
