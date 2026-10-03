# Báo cáo kiểm thử hệ thống cục bộ

Ngày 30/09/2026 Asia/Bangkok. Trạng thái tổng: chưa sẵn sàng vận hành trọn luồng.

| Hạng mục | Kết quả thực tế |
|---|---|
| 8 đầu vào | Sao chép và SHA-256 khớp bản gốc |
| Agent Tổng, registry, cấu hình, skill | Đã tạo trong dự án; vai trò chạy trong chat, chưa có daemon |
| Skill | quick_validate.py báo Skill is valid bằng Python môi trường riêng |
| Quản lý ngân sách và hàng đợi | 13 unittest đạt, chạy thư mục tạm, không đổi hàng đợi thật |
| FFmpeg/FFprobe | Bản 9.0.2 chạy được; ZIP GitHub mirror khớp SHA-256 nhà phát hành |
| Cắt/ghép/render phụ đề | Fixture nền xanh/âm sin cắt từ 2 giây thành 1,6 giây, MP4 H.264/AAC 1080x1920 decode đạt |
| Tiếng Việt trên hình | Đã xem PNG subtitle-test-v3.png, chữ có dấu, đọc được, trong lề |
| ASR | Whisper small CPU int8 nạp được; đọc âm thanh fixture, VAD chặn không có lời nói; chưa kiểm độ đúng tiếng Việt bằng audio tập thật |
| Kết nối Facebook | Đăng nhập, chuyển sang Page, giao diện quản lý có bằng chứng ảnh; chưa đăng tập thử |
| Kết nối Flow | Đã đăng nhập và vào đúng URL tool; giao diện báo Không chạy được công cụ/compile uj; đang thử sửa hẹp |
| Credit Flow | Chưa quan sát giá, chưa tạo lượt nào, ledger tập thử 0 credit reserved |
| Tập MT-0001 | Đã vào hàng đợi, khóa hash ảnh 1 và có kịch bản; chưa clip, master, QA hoặc bài đăng |
| Lô 10, lịch 19:30 | Giữ tắt theo cổng tập thử; không có automation id |

13 bài thử gồm: trần đúng 80, chi phí pending không được bỏ, chống đặt chỗ trùng, cap retry, STOP, ảnh đổi hash, cổng pilot và xoay ảnh, cấm đăng thiếu QA, giá không hợp lệ, master đổi hash làm mất QA, ý định đăng chặn retry mù, sai giờ bị chặn, bài hẹn lịch không mở pilot, bằng chứng ngày tương lai không mở pilot.

Giới hạn bằng chứng: fixture chỉ chứng minh đường xử lý file và hiển thị chữ; không chứng minh lời đủ, giọng, nhận dạng, đồng bộ phụ đề hoặc kết quả xuất bản tập thật. Các JSON QA là xác nhận của người/agent sau kiểm thực tế, không thay thế xem/nghe. Trình điều phối hiện dùng công cụ trình duyệt trong chat, chưa phải dịch vụ tự chạy khi app/máy không hoạt động.
# Bổ sung yêu cầu thumbnail và kiểm thử ngày 30/09/2026

Lượt sửa cuối đã kết thúc: tác nhân báo gỡ jszip/ZIP. Đã thử lại chế độ Công cụ; preview vẫn lỗi, bằng chứng `07-bang-chung/flow-mo-lai-van-loi.png`. Không gửi thêm lượt sửa/tạo media; chưa có cơ sở xác định lỗi server. Tool đúng đã giữ mở để tiếp tục khi hoạt động trở lại.

- Cấu hình v2, skill và Agent Tổng cập nhật: giọng Bắc, không chào/cảm ơn/tạm biệt, thumbnail riêng, intro 1 giây, gói bàn giao, bằng chứng Facebook và lịch thực thi thật.
- Đã tạo `06-san-sang-dang/MT-0001/thumbnail.png` 1080×1920 và caption.txt. Dùng ảnh 1 giữ nguyên mặt, tỷ lệ; xem ảnh thực tế, đổi Georgia thiếu glyph sang Times New Roman Bold, dấu tiếng Việt hiện đầy đủ. Chưa có MP4/SRT tập thật.
- FFmpeg/FFprobe đã cài từ nguồn vendor; faster-whisper/model small đã tải và nạp lại CPU int8 offline thành công với av16.0.1. Không cần duyệt lại hai thành phần này.
- Chèn thumbnail trên fixture: output 1080×1920 H.264/AAC, 30 fps, 78 frame/2.6 giây thay vì 48 frame/1.6 giây; frame 29 còn thumbnail, frame 30 bắt đầu nội dung; SRT từ 0.100–1.400 thành 1.100–2.400. Decode toàn file pass. Đây là test kỹ thuật bằng tone và màn xanh, không phải MT-0001 hoặc bằng chứng phụ đề giọng thật.
- 13 test quản lý trạng thái/ngân sách/STOP/chống đăng lặp/gate pilot vẫn pass sau bổ sung QA thumbnail, intro và bàn giao. Sửa output console UTF-8 để status chạy được trên Windows.
- Thoát rồi vào lại đúng Flow tool, đăng nhập ULTRA còn hợp lệ; preview tiếp tục lỗi `Không chạy được công cụ`. Chưa xác định lỗi server hay app. Tác nhân sửa tự bổ sung ZIP/jszip; đã yêu cầu gỡ phần ngoài phạm vi và không tạo media mất credit. Không coi lời tác nhân báo thành công là bằng chứng.
- Facebook vẫn có Manage Page và Reel dưới đúng danh tính Page. Khả năng chọn ảnh bìa, publish và permalink playback chưa kiểm chứng khi chưa có MP4 thật đạt QA.
- Pilot, lô 10 và lịch vẫn chưa đạt cổng. Không có lượt tạo MT-0001 được ghi nhận trong queue; bảo toàn tất cả media có sẵn, không gán clip cũ không rõ nguồn thành pilot.

