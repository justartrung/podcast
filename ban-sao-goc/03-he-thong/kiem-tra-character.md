# Kiểm tra Character 30/09/2026

Mở đúng tool mới trong phiên hiện tại. Từ Nhân vật vào màn hình Nhân vật mới: các lựa chọn Kẻ lập dị/Nhân vật chuyên nghiệp/Nhân vật biến hóa/Nhân vật quen thuộc/Kẻ phản diện/Nhân vật kỳ ảo là gợi ý tạo nhân vật, không phải giọng mẫu. Thêm từ dự án mở picker PODCAST có 3.png, 4.png, 1.png, 2.png. Chưa quan sát danh sách giọng, tên/ID hoặc nút nghe mẫu. Không kết luận toàn tài khoản không có giọng; chỉ các màn hình truy cập được chưa cho thấy bộ chọn. Không tạo Character mới.

Quay về đúng tool: màn hình “Không chạy được công cụ.”, “Bạn có muốn Tác nhân ứng dụng thử khắc phục vấn đề này không?”, nút Sửa lỗi/Tải lại. Dừng tại bước kiểm chức năng chọn giọng. Không bấm sửa lỗi, không tạo media, không dùng credit. Bằng chứng: 07-bang-chung/character-thanh-phan-hien-co.jpg và flow-character-tool-loi.jpg.

Chưa nghe được mẫu; chưa chọn tên/ID; chưa tạo cảnh thử, chưa QA phát âm/cảm xúc/khẩu hình; chưa xác nhận cách chọn lại. Phải giữ trạng thái chưa kiểm chứng.

## Đề xuất tích hợp trước khi sửa tool

Ưu tiên phục hồi khả năng chạy tool, rồi kiểm chức năng Flow chính thức cho giọng tham chiếu từ Character. Nếu API/chức năng Flow thật hỗ trợ, thêm bộ chọn Character hiện hữu (tên/ID nếu cung cấp), nút phát mẫu có sẵn và hiển thị Character/giọng đã khóa. Truyền tham chiếu giọng thật vào lượt tạo theo khả năng Flow, không thay bằng prompt phong cách. Hiển thị model, giây/cảnh, số output x1 và credit trước tạo. Giữ bộ chọn ảnh host tách khỏi giọng để ảnh luân phiên nhưng giọng không đổi.

Nếu Flow không cung cấp tham chiếu giọng độc lập hoặc Character đồng thời khóa ngoại hình, phải báo giới hạn xung đột với luân phiên bốn ảnh trước triển khai; không giả cam kết giọng nhất quán. Không dùng TTS/model ngoài hoặc giọng tự tạo để vượt chặn. Đề xuất này chưa được triển khai; không cần/cài dịch vụ mới ở vòng này.

Khi truy cập mẫu được: chọn tối đa vài mẫu nữ Việt phù hợp để nghe; ghi tên/ID và đường chọn; tạo một cảnh ngắn dùng ảnh 1 của MT-0001 và câu gốc trong tập, ghi reservation sau xác nhận giá. Tính tất cả thử vào ledger MT-0001, không một ngân sách thử riêng.
