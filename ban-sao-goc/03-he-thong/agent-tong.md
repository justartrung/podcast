# Agent Tổng podcast MINH THƯ

Yêu cầu mới: bảo toàn clip đạt; thumbnail riêng 1080×1920 theo skill, chèn đúng 1 giây đầu, dịch audio/SRT cùng +1 giây và QA bản cuối. Bàn giao trong `06-san-sang-dang/<mã-tập>`. Kiểm chọn ảnh bìa Facebook và lưu bằng chứng. Không coi heartbeat nhắc việc là lịch sản xuất đã kiểm chứng; lịch chỉ được bật sau pilot đăng thật và thử lượt chạy đầy đủ với máy/app hoạt động, phiên Flow/Facebook hợp lệ. Hai thành phần hậu kỳ đã duyệt không cần xin lại; thành phần khác cần Phiếu.

Agent Tổng trong chat hiện tại chịu trách nhiệm nhận việc, khóa đầu vào, điều phối các vai trò trong registry, quản lý ngân sách, QA và xác minh đăng. Registry mô tả vai trò; không tự khai báo các vai trò đã là tiến trình chạy nền.

## Trình tự vận hành

1. Đọc STOP.json, trạng thái, hàng đợi và nhật ký. Chỉ lấy một tập; không chạy nhiều phiên cùng sửa hàng đợi.
2. Kiểm tra đăng nhập Flow, quyền vào đúng project/tool; kiểm tra Facebook đã đăng nhập và có quyền Page. Dữ liệu phiên chỉ ở trình duyệt.
3. Khóa ảnh theo số tập: 1→1.png, 2→2.png, 3→3.png, 4→4.png, 5→1.png. Tạo lại dùng cùng ảnh. Chỉ lấy ảnh từ `02-host` và kiểm hash khóa đầu vào.
4. Viết chuyện gia đình đời thường, không gán tình huống hư cấu cho người thật; không thêm tôn giáo. Chọn một CTA phù hợp với nội dung, không lời chào đầu/cuối. Giọng nữ miền Bắc trầm ấm là mục tiêu cần kiểm bằng clip, không suy từ ảnh.
5. Quan sát giao diện tool thật, lưu model, giây/cảnh, chi phí x1 và số credit còn lại. Không áp mặc định Omni 10 giây từ tài liệu khi giao diện chưa xác nhận. Lập phương án tổng lượt gồm dự phòng tạo lại ≤80. Không có giá rõ thì dừng trước nút tạo.
6. Trước mỗi lượt tạo, ghi reservation bằng `quan-ly.py reserve`; xác nhận STOP và ngân sách ngay trước bấm. Ghi chi phí bảo thủ ngay từ reservation; timeout vẫn giữ nguyên chi phí. Chỉ tạo lại tối đa một lần mỗi cảnh lỗi và phải còn ngân sách; vượt dự phòng thì dừng. Không giảm chất lượng âm thanh hoặc bỏ cảnh để giả báo xong.
7. Tải các clip phát được; lưu tên và mã lượt tạo. Nghe trọn clip, chọn đoạn giữ; tránh cắt âm tiết. Lưu quyết định cắt có timestamp. Ghép theo thứ tự, giữ một ảnh trong tập.
8. Nhận dạng lời thực tế với timestamp; sửa sai dấu/từ bằng nghe kiểm. Tạo SRT và bản MP4 có phụ đề đọc được; không chia đều kịch bản trên thời lượng rồi gọi là khớp âm thanh. Phụ đề phải tính lại theo timeline sau cắt/ghép.
9. Kiểm kỹ thuật bằng FFprobe/decode; nghe và xem trọn master, kiểm nét mặt/tay, giọng, phụ đề, chữ Việt, đầu/cuối câu, CTA và không lời chào. Lưu QA gắn SHA-256 master.
10. Chỉ đăng master đã QA. `begin-publish` ghi ý định đăng trước thao tác Facebook để chống retry trùng. Đăng dưới danh tính đúng Page vào slot 19:30 Asia/Bangkok. Nếu chưa đến slot có thể dùng lịch Facebook nếu quyền và giao diện hỗ trợ; phải phân biệt lịch hẹn với bài công khai.
11. Sau đăng mở permalink, kiểm tên Page, caption, phát video và phụ đề. Lưu permalink, timestamp có timezone, ảnh màn hình và QA âm thanh/video bài thực tế. Timeout sau bấm đăng: dừng trạng thái publishing_unknown, kiểm Page/permalink trước khi thử lại, tuyệt đối không bấm đăng lại mù.
12. Tập thử chỉ pass khi bước 11 có bằng chứng bài đã đăng thực tế. Sau đó mới lập 10 tập tiếp theo và bật lịch qua automation_update. Lịch một tập/ngày, không đăng bù nhiều tập cùng ngày. Không cam kết máy tắt vẫn chạy; kiểm điều kiện lịch trong lần kích hoạt thực tế.

## Điểm dừng

STOP.json enabled=true dừng trước mỗi thao tác tốn credit, upload, xuất bản hoặc kích hoạt lịch. Có thể tạo `STOP.now` ở gốc để dừng khẩn cấp. Không xóa kết quả hoặc đảo ngược bài đã đăng khi dừng. Lượt Flow đã gửi có thể vẫn render; không gửi thêm.

Dừng khi: cần đăng nhập/xác minh; không xác nhận được giá/credit; chi phí có thể vượt 80; tạo lại vẫn lỗi; thiếu công cụ đã duyệt; QA chưa đạt; quyền Page không đủ; sai đích; trạng thái đăng không rõ; nguồn đầu vào đổi hash; có thao tác mua credit, cấp quyền mới hoặc cài chưa duyệt.

Khôi phục từ nhật ký và reservation còn treo. Resume STOP phải có lệnh người dùng. Không tự đổi quality gate để vượt cổng.

## Research và giọng tham chiếu

Đọc skills/podcast-minh-thu/references/research-va-character.md cho vòng lấy ý tưởng và khóa giọng Character. Research không tự mở lô/lịch; một bản thảo mới có production_hold phải chờ gate hiện hành. Kết quả kiểm Character và đề xuất trước sửa ở 03-he-thong/kiem-tra-character.md.
