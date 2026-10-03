# Onboarding khách hàng

## Dữ liệu tối thiểu

Chỉ xác định các mục chưa có: ý tưởng video; ảnh Cameo/avatar có quyền sử dụng; ảnh bối cảnh/sản phẩm; khóa trang phục; số video. Mặc định một ảnh bối cảnh tạo một video.

Không hỏi lại dữ liệu đã có trong tin nhắn, file đính kèm, project hoặc cấu hình đã xác nhận.

## Trình tự lần đầu

1. Mở Google Flow trong trình duyệt được kết nối.
2. Nếu chưa đăng nhập, dừng và yêu cầu khách đăng nhập trực tiếp.
3. Nếu chưa có project phù hợp, tạo project mới theo tên chiến dịch. Nếu khách chưa đặt tên, dùng `TVC - YYYY-MM-DD` và có thể đổi sau khi khách yêu cầu.
4. Nếu chưa có Cameo/avatar, mở khu vực tạo Hình đại diện/Nhân vật và yêu cầu khách hoàn tất quy trình tạo Cameo. Agent không thay khách xác nhận danh tính hoặc thực hiện bước bảo mật.
5. Nếu thiếu ảnh, yêu cầu khách tải lên cuộc trò chuyện hoặc chỉ rõ tệp được dùng.
6. Sau khi đủ Cameo và ảnh, tiếp tục tự động mà không hỏi “có muốn tiếp tục không”.

Nếu thiếu đồng thời nhiều dữ liệu, làm theo thứ tự: đăng nhập/kết nối → kiểm tra và tạo Cameo → nhận brief/ảnh → sản xuất. Không tuyên bố đã kiểm tra Cameo trước khi nhìn thấy project sau đăng nhập.

## Bộ nhớ mỗi khách hàng

Nếu cần bộ nhớ lâu dài, tạo file `references/customers/<customer-slug>.md` từ [customer-config-template.md](customer-config-template.md). Mỗi khách một file riêng; không dùng cấu hình của khách này cho khách khác. Có thể lưu tên/URL project, alias Cameo, tên hiển thị trong Flow, khóa trang phục và cấu hình sản xuất. Không lưu mật khẩu, cookie, OTP, API key, dữ liệu thanh toán hoặc ảnh sinh trắc học ngoài tài sản người dùng chủ động đặt trong Flow.

Sau bước đăng nhập hoặc tạo Cameo thủ công, tự quan sát lại Flow. Nếu không thấy thay đổi do phiên điều khiển bị ngắt, yêu cầu khách báo `đã xong` rồi quan sát lại; không bắt khách lặp toàn bộ brief.
