# Phiếu đề xuất triển khai podcast MINH THƯ

Ngày 30/09/2026, dự án PODCAST TU DONG. Trạng thái: người dùng đã duyệt hai thành phần cục bộ qua câu trả lời trong chat; đã cài và kiểm thử công cụ cục bộ, model small đã nạp được. Tập thử thực tế chưa chạy vì tool Flow chưa khởi chạy sau đăng nhập.

## Đã có

8 tệp đầu vào đã kiểm hash. Python, Node, thư viện đọc tài liệu và ảnh có sẵn. Trình duyệt tích hợp đã kết nối. Facebook đã đăng nhập và chuyển sang danh tính Page; chưa kiểm thử đăng. Flow đã đăng nhập và mở đúng tool; tool báo lỗi khởi chạy/compile uj, đang thử sửa, chưa xác nhận giá lượt tạo thực tế. Ổ D còn khoảng 31,3 GiB tại lúc kiểm kê.

## Bắt buộc để cắt dựng và phụ đề

1. FFmpeg và FFprobe bản Windows portable, lưu riêng `08-cong-cu/ffmpeg`, không sửa PATH toàn máy. Tải từ nhà cung cấp Windows được trang FFmpeg chính thức dẫn đến; lưu phiên bản, nguồn và kiểm checksum nếu nguồn công bố. Dùng để cắt, ghép, kiểm audio/video và render phụ đề. Phần mềm miễn phí; dung lượng dự kiến vài trăm MB.
2. Một môi trường Python riêng `08-cong-cu/python-env` và `faster-whisper` từ PyPI, model multilingual `small` chạy CPU int8, cache model tại `08-cong-cu/models`. Dùng âm thanh master sau cắt để lấy timestamp; lưu SRT, sửa dấu/từ bằng nghe kiểm. Model tải lần đầu khoảng vài trăm MB; môi trường và cache dự kiến tổng 1–3 GiB. Không gửi âm thanh cho dịch vụ nhận dạng trả phí; không cần API key. Tốc độ và độ đúng tiếng Việt phải đo bằng tập thử, chưa bảo đảm.

Nếu tool Flow thực tế đã có cắt và phụ đề timestamp đúng, kiểm nó trước; chỉ dùng phần bổ sung cần thiết. Không cài HyperFrames, GPU stack hoặc Real-ESRGAN ở giai đoạn này.

Nguồn: https://ffmpeg.org/download.html và https://github.com/SYSTRAN/faster-whisper. Giá/dung lượng nêu trên là ước tính phần mềm cục bộ; credit Flow quản lý riêng và không vượt 80/tập gồm retry.

## Nên có sau tập thử

Một lịch heartbeat gắn chat này, 19:30 Asia/Bangkok, dùng automation_update sau khi tập thử đã đăng và xác minh. Khi chuẩn bị lịch sẽ xác nhận cơ chế múi giờ, điều kiện máy/app và khả năng phiên trình duyệt. Giữ yên khi không có thay đổi; báo khi thành công, lỗi hoặc cần thao tác. Không bật lịch trong lúc đang chờ tập thử.

## Tùy chọn

Không có thành phần tùy chọn cần cài ngay. Không mua credit, không thêm subscription, không tạo tài khoản, không xin API token Facebook ở bước này.

## Kế hoạch kiểm thử thực tế

Tập MT-0001: “Khi câu hỏi nhỏ thành lời trách”, ảnh 1.png xuyên suốt, dự kiến 6 cảnh ngắn; số cảnh/giây chỉ chốt sau khi tool và giá được quan sát. Tổng tạo ban đầu và dự phòng phải ≤80. Nếu giá không cho phép phương án 6 cảnh, rút kịch bản trước khi tạo để vẫn là một tập hoàn chỉnh; không bỏ cảnh ở cuối rồi báo xong.

Tạo thử cảnh 1 → nghe/xem → tạo phần còn lại → cắt đoạn thừa → nhận dạng audio master → sửa và render phụ đề → QA trọn tập → đăng tại slot 19:30 → mở permalink, phát kiểm và lưu bằng chứng. Lô 10 và lịch chỉ mở sau lần đăng thật này; bài hẹn lịch chưa đạt cổng tập thử.

## Quyết định cần người dùng

Duyệt FFmpeg/FFprobe portable và môi trường faster-whisper/model small cục bộ, không phát sinh mua phần mềm. Việc cần duyệt này xuất phát từ yêu cầu “Trình Phiếu đề xuất trước khi cài thêm thành phần” của người dùng. Đăng nhập là thao tác người dùng riêng, không phải duyệt lại quyền sản xuất/đăng đã trao.
