# Mẫu bàn giao hai nhánh

## Gemini

Đưa prompt độc lập mỗi cảnh trong khối dễ sao chép. Khi cô nói “tiếp”, xuất cảnh kế tiếp theo kịch bản đã chọn, không tự sáng tác mạch khác. Nếu yêu cầu cả bộ thì xuất đủ các cảnh.

```text
CẢNH {n}/{N} — {vai trò}
Tạo duy nhất một clip dọc 9:16, thời lượng mục tiêu {giây được chọn}.
Ảnh tham chiếu: {ảnh host chuẩn thực sự đính kèm}.
Giữ đúng khuôn mặt, tóc, tuổi, trang phục, phụ kiện và bối cảnh trong ảnh. {Mô tả chính xác các chi tiết nhìn thấy}.
{Nếu có frame cuối thực tế: dùng frame đính kèm làm tư thế mở đầu. Nếu không: bắt đầu tư thế ổn định theo ảnh chuẩn.}
Camera cố định, giữ trọn đầu và cằm, không zoom/chuyển góc. Tay cử động nhỏ, thả lỏng trên gối ở cuối. Nhìn vào máy, biểu cảm tiết chế.
Giọng nữ miền Bắc trầm ấm, cùng sắc thái toàn tập. Host kể cả lời trích dẫn bằng giọng mình, không đổi giọng nam.
Chỉ nói đúng một lần lời sau:
“{lời thoại đã duyệt của cảnh này}”
Vào lời sớm, ngắt tự nhiên, nói rõ không đọc dồn; kết lời có nhịp nghỉ ngắn. Không thêm/lặp lời hay đọc nhãn cảnh.
Khẩu hình khớp tiếng Việt, chi tiết mắt/tóc/vải rõ, da tự nhiên, không biến dạng tay/mặt.
Chỉ giọng kể và âm phòng nhẹ; không nhạc, phụ đề, chữ, người khác hay cảnh minh họa. Không tạo cảnh tiếp theo.
```

Nhắc cô tải ảnh cùng prompt. Prompt là yêu cầu, không bảo đảm hệ thống đáp ứng chính xác thời lượng, giọng hay nhận dạng. Thử cảnh 1 trước.

## App riêng dùng Omni/Veo trên Flow

- Khối A — cấu hình: ảnh host, giọng, tỷ lệ, model và giây theo giao diện đã xác nhận. Mô tả giọng mẫu: “Nữ miền Bắc, trầm ấm, rõ tiếng, kể gần gũi, nhịp tự nhiên, ít ngắt dài; giữ âm sắc và âm lượng giữa các cảnh.” Chỉ dán vào ô mô tả giọng nếu có.
- Khối B — lời thoại: mỗi ô là một writing block hoặc khối sao chép chỉ chứa lời nói. Số cảnh, thời lượng, số tiếng nằm ngoài. Không đưa tiêu đề, chỉ dẫn tay/camera vào trường lời thoại.
- Nếu app có trường hướng dẫn hình ảnh riêng, đưa khóa hình vào đó. Nếu không có, nói rõ phải giữ qua ảnh/cấu hình app, không nhét vào thoại và không bịa nút.
- “Dán kịch bản” không bảo đảm tự tách đúng cảnh; nếu chưa biết định dạng import, hướng dẫn thêm cảnh và dán từng ô.
- Hướng dẫn lần lượt: tải host → cấu hình → thêm ô/dán → thử ô 1 → kiểm tra nói hết, khoảng nghỉ, mặt, miệng, giọng → tạo ô còn lại → kiểm từng clip → sửa ô lỗi → ghép clip đủ theo thứ tự → tải video.
- Điều chỉnh theo clip thử: dư khoảng lặng quá nhiều thì thêm ít lời hoặc giảm thời lượng nếu có; cắt câu thì rút khoảng 2–4 tiếng hay chia thêm cảnh. Không sửa cả bài khi chỉ một ô lỗi.
- Giữ lời giống nhau giữa hai nhánh; thay đổi cách đóng gói, không tự đổi ý nghĩa.
