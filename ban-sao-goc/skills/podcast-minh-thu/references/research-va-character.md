# Quy trình research và giọng Character

## Giọng

Mở flow.tool_url từ cấu hình. Kiểm phiên, mục Nhân vật/Character và các giọng có sẵn tài khoản. Phân biệt Character hình ảnh, mô tả phong cách giọng và giọng tham chiếu có tên/ID. Không coi một ô mô tả “nữ Bắc” là đã dùng giọng mẫu. Ưu tiên nữ tiếng Việt, miền Bắc, trưởng thành, ấm, kể tự nhiên. Nghe các mẫu có sẵn bằng chức năng Flow; ghi tên/ID, cách chọn lại, kết quả nghe và bằng chứng. Không tạo/clone giọng khác hoặc tải model ra ngoài.

Nếu tool chưa có bộ chọn Character/giọng, ghi giới hạn và đề xuất tích hợp trước sửa. Nếu preview lỗi thì dừng, không bấm sửa/tải lại/tạo liên tiếp. Khi có hỗ trợ thực tế, xác nhận model, thời lượng, x1, giá và số dư; tính cả thử trong 80 credit của tập. Ghi reservation trước tạo một cảnh ngắn từ kịch bản tập đang làm; giữ ảnh host khóa. Nghe/xem trọn: dấu và từ tiếng Việt, giọng Bắc, cảm xúc tự nhiên, tốc độ, đầu/đuôi câu và khẩu hình. Chỉ khóa giọng sau QA; giữ cùng giọng qua các cảnh và tập. Ghi mọi thay đổi giọng để kiểm lại, không tự thay thế khi giọng đã chọn mất quyền truy cập.

## Vòng lấy ý tưởng

1. Tìm nguồn công khai tiếng Việt Facebook, TikTok, YouTube; ưu tiên 30–90 ngày gần nhất, nguồn cũ chỉ làm đối chiếu. Không đặt hạn ngạch gần đây bằng cách đoán ngày.
2. Ghi permalink/ảnh gốc bài, kênh, ngày đăng như UI hiển thị, thời điểm kiểm có +07:00, caption/nội dung đọc được và chỉ số có nhãn. Lưu snapshot/screenshot. Không thu dữ liệu riêng tư hoặc tương tác bài.
3. Phân biệt đã xem toàn video, chỉ caption, chỉ metadata/chỉ mục và bị chặn. Hook/CTA chưa nghe phải ghi chưa xác minh. Không đồng nhất like với view. Không gọi viral từ hashtag/tiêu đề; muốn đánh giá phải so với baseline cùng kênh, tuổi bài và tăng trưởng ở ít nhất hai lần kiểm.
4. Nhóm tiền và quyền quyết định, việc nhà, nuôi con, mẹ chồng–nàng dâu, ranh giới hai bên, giao tiếp.
5. Đọc hàng đợi, kho ý tưởng và lịch sử. So sánh cả mâu thuẫn, giải pháp, hook và hình ảnh câu chuyện; loại bản đổi tên nhưng cùng cốt truyện. Không xếp mâu thuẫn gần giống liên tiếp. Lịch sử phân biệt đề xuất/bản thảo/đã sản xuất/đã đăng.
6. Chấm 0–5 cho phù hợp, tiềm năng (ước lượng biên tập), góc mới và bằng chứng. Đề xuất 5 ý tưởng đủ hook, tóm tắt, góc nhìn, thumbnail, CTA, nguồn và điểm. Tự chọn 1 dựa vào chất lượng bằng chứng, sự đa dạng và khả năng kể tử tế.
7. Viết kịch bản gốc; ghi tình huống hư cấu minh họa khi cần. Không sao chép lời thoại, không tải/reup, không gán cáo buộc người thật hoặc đưa tư vấn y tế/pháp lý.
8. QA văn bản: gia đình, không lời chào, CTA chủ đề, khác tập trước, nghĩa rõ và lời đọc tự nhiên. Thời lượng chưa được đo phải ghi ước tính. Đưa một bản thảo vào hàng đợi với ảnh khóa đúng số tập và production_hold nếu pilot/giọng/giá chưa đạt. QA văn bản không thay QA âm thanh/video.
9. Lưu danh-sach-nguon.json, research-YYYY-MM-DD.json/md, kho-y-tuong.json và lich-su-chu-de.json trong 10-nghien-cuu. Cập nhật trạng thái lịch sử sau sản xuất/đăng có bằng chứng.

## Định kỳ

Chạy một vòng khi nhận yêu cầu hoặc trước chọn tập mới trong lượt vận hành hợp lệ. Khi được phép bật lịch thực tế, đề xuất một vòng hàng tuần Asia/Bangkok; giờ cụ thể chưa chốt, không dùng slot đăng 19:30 làm mặc định research. research.schedule.enabled=false cho đến kiểm chứng cơ chế gọi chat chạy đủ vòng với máy thức, app mở, phiên nguồn hợp lệ, không OTP/CAPTCHA và STOP tắt. Không tạo heartbeat hoặc lịch khác trong yêu cầu này. Phần mềm/dịch vụ trả phí/quyền mới cần Phiếu duyệt; không cài trước.
