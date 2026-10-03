# Tool Flow đã quan sát

Đúng tool `806639af-776e-492e-afc8-368d5d4ce4c0`, dự án `f37b741b-b3f2-40f8-b490-f23f79b098ed`, tên giao diện PODCAST CHUYÊN NGHIỆP. Đăng nhập Google thành công.

Khung sử dụng báo “Không chạy được công cụ”; tải lại không khắc phục ngay. Đã dùng nút Sửa lỗi do Flow cung cấp, giao diện gửi chẩn đoán “Applet failed to compile with the following error: uj Please fix.” tới tác nhân sửa tool. Chưa gửi yêu cầu tạo clip. Phải kiểm kết quả sửa và giá trước khi sản xuất.

Đã đọc phần App.tsx qua tab Mã của giao diện (không gọi SDK trực tiếp). Các chi tiết hữu ích cho lần vận hành:

- Mặc định giọng trong code là Nam, ấm áp, trang trọng; cần đổi thành giọng nữ miền Bắc TRƯỚC khi chọn/crop ảnh, vì mô tả giọng được chụp vào cấu hình character lúc nạp ảnh.
- Mặc định model Omni 1.1 Flash, 9:16. Code đặt Omni 10 giây, Veo 8 giây. Đây là quan sát code phiên bản hiện tại, chưa chứng minh model gọi thành công hay giá.
- Tool có thao tác DÁN chia dòng trống thành cảnh và THÊM. Không dùng CHẠY TẤT CẢ để tránh bỏ qua ledger và việc kiểm cảnh đầu. Gửi từng cảnh x1 sau khi ghi reservation.
- Code state giữ cảnh/video trong React; chưa thấy bằng chứng lưu bền vững. Tải clip đạt ngay và ghi hash/mã lượt vào dự án trước reload, không tin lời trợ lý cũ rằng đã lưu bền vững.
- Không có chi phí credit trong phần code đã đọc. Cần xác nhận giá qua giao diện/dữ liệu chính thức hiện hành trước bấm tạo.
- Tool ghép các cảnh đã có video; phải tự đối chiếu đủ cảnh trước ghép, không coi nút ghép thành công là đủ tập.

Nếu tác nhân sửa cập nhật code, đọc lại các điểm trên; không dựa vào mặc định cũ. Không tự đổi sang tool khác hoặc dùng tài sản cũ trong lưới để thay ảnh 1 đã khóa.

## Chuyển nguồn ngày 30/09/2026

Nguồn hiện hành: project 286e14cd-d1cb-4de6-88d1-d9ee857f90ff, tool 10a20665-c278-4d06-9dbb-32bd4fee681b. Dừng thao tác tool cũ; phần trên là lịch sử. Phiên mới vào được Podcast Chuyên Nghiệp CODEX, gói PRO, 1.050 credit. Studio mở được lần đầu, nhãn ENGINE STATUS OMNI 1.1 FLASH, giọng mặc định nam; chưa xác minh model tạo thực tế, giá x1, giây/cảnh hoặc thoại tiếng Việt. Sau Xong → tài khoản → đóng tài khoản → mở lại tool, khung studio trống. Không gửi tạo/sửa/đăng. Giữ giới hạn 80 credit/tập gồm retry, tài sản và Page đã chốt.
