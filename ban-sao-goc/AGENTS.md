# Công xưởng podcast MINH THƯ

Đọc `03-he-thong/cau-hinh-kenh.json`, `03-he-thong/agent-tong.md` và `skills/podcast-minh-thu/SKILL.md` trước khi vận hành. Đây là cấu hình của riêng dự án này.

Yêu cầu người dùng ngày 30/09/2026 ưu tiên hơn tài liệu gốc: chỉ chuyện gia đình; host MINH THƯ; ảnh 1, 2, 3, 4 luân phiên theo số tập, khóa một ảnh suốt tập; không lời chào; CTA theo chủ đề; cắt đoạn thừa và làm phụ đề từ âm thanh thực tế.

Người dùng cho phép tự chọn nội dung, sản xuất bằng đúng tool Flow và đăng vào đúng Page trong cấu hình. Tối đa 80 credit Flow mỗi tập, tính cả tạo lại; không mua credit. Không cần xin lại quyền cho những thao tác này trong phạm vi đã trao.

Chỉ bật lịch 19:30 Asia/Bangkok và xử lý lô 10 sau khi tập thử qua QA và có bằng chứng bài đăng phát được. Không coi cấu hình, kiểm thử phần mềm hoặc ảnh thumbnail là bằng chứng đã sản xuất. Không chạy lô khi chưa vượt cổng tập thử.

Dùng trình duyệt qua công cụ cua_repl; người dùng tự đăng nhập, OTP, CAPTCHA. Không lưu bí mật hoặc dùng cookie/token từ trình duyệt qua shell. Không cài thêm thành phần trước khi Phiếu đề xuất được duyệt.

Lệnh kiểm tra trạng thái: `python scripts/quan-ly.py status` với Python bundled trong `03-he-thong/kiem-ke.json`. Agent Tổng là vai trò điều phối của chat đang chạy, không phải tiến trình nền đã được cài. File skill được tham chiếu trực tiếp ở đây; chưa cài skill vào cấu hình Codex toàn máy.
