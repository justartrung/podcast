# Vận hành trong dự án

Agent Tổng đọc AGENTS.md và skill podcast, điều khiển Flow/Facebook qua cua_repl. Các script quản lý trạng thái và hậu kỳ không tự kết nối hoặc đăng Facebook. Chưa có tiến trình nền hoặc lịch hoạt động.

## Công cụ đã duyệt

Python cơ sở lấy từ `kiem-ke.json`; Python hậu kỳ ở `08-cong-cu/python-env/Scripts/python.exe`. FFmpeg/FFprobe portable cũng ghi trong `kiem-ke.json`. Phiếu bổ sung đã được người dùng duyệt qua chat. Môi trường khóa phiên bản trong `08-cong-cu/requirements-lock.txt`; PyAV 16.0.1 đã kiểm tương thích với faster-whisper 1.2.1, không nâng tùy tiện trước tập thử.

Model Whisper small multilingual đã tải và nạp CPU int8; `whisper_model_path` trỏ thư mục snapshot cục bộ. Không cần token HF hoặc API key. Không dùng môi trường bundled để cài dependency mới.

## Lệnh quản lý

Chạy bằng Python đã ghi trong kiem-ke.json:

```text
scripts/quan-ly.py status
scripts/quan-ly.py stop --reason "Người dùng yêu cầu dừng"
scripts/quan-ly.py resume --user-authorized --authorization "Trích lệnh tiếp tục mới nhất của người dùng"
scripts/quan-ly.py enqueue --title "Tên tập"
scripts/quan-ly.py reserve --episode MT-0001 --scene 1 --cost GIÁ_ĐÃ_QUAN_SÁT --generation MÃ_LƯỢT_DUY_NHẤT --price-evidence FILE_CHỨNG_CỨ
scripts/quan-ly.py generation-result --episode MT-0001 --generation MÃ_LƯỢT --result clip_available --evidence FILE_CHỨNG_CỨ
scripts/quan-ly.py qa --episode MT-0001 --file FILE_QA
scripts/quan-ly.py begin-publish --episode MT-0001 --scheduled-at THỜI_ĐIỂM_ISO_19H30_CÓ_TIMEZONE
scripts/quan-ly.py verify-published --episode MT-0001 --file FILE_BẰNG_CHỨNG_BÀI
```

Các giá trị viết hoa trong ví dụ cần thay bằng dữ liệu thực tế; không chạy nguyên mẫu. `generation-result` cho phép kết quả failed hoặc not_submitted, vẫn giữ reservation bảo thủ để không vượt cap. Lượt chưa rõ kết quả không được tự giải phóng ngân sách.

Để dừng ngay, tạo file rỗng `STOP.now` tại gốc hoặc chạy lệnh stop. Chỉ gỡ dừng sau lệnh người dùng. Trước thao tác UI tốn credit hoặc đăng cần đọc STOP một lần nữa. Thao tác đã gửi tới Flow có thể tiếp tục render; không có API hủy nền được xác minh.

## Hậu kỳ

Dùng Python của môi trường riêng:

```text
scripts/hau-ky.py assemble --manifest FILE_CẮT_JSON
scripts/hau-ky.py transcribe --input MASTER_SAU_CẮT --model THƯ_MỤC_MODEL_ĐÃ_TẢI --output TRANSCRIPT_JSON
scripts/hau-ky.py render --input MASTER_SAU_CẮT --transcript TRANSCRIPT_ĐÃ_NGHE_KIỂM --output MASTER_CÓ_PHỤ_ĐỀ
scripts/hau-ky.py check --input MASTER_CÓ_PHỤ_ĐỀ
```

Manifest cắt cần `clips` (file, sha256, keep_start, keep_end), `output`, `cuts_reviewed_against_audio=true` và `reviewer`. Phải nghe nguồn thật mới xác nhận điểm cắt.

Transcript do ASR xuất là bản nháp với audio_reviewed=false. Nghe đối chiếu từng cue, sửa từ và timestamp rồi ghi audio_reviewed=true cùng reviewer. Chỉ render khi hash nguồn còn khớp. `check` xác nhận kỹ thuật và decode; không xác nhận đủ lời, giọng hoặc khớp phụ đề thay cho nghe/xem.

QA/bài đăng theo quality-gate.md. Mỗi phiên bản master đổi hash phải kiểm lại. File trong `09-kiem-thu` là fixture nền xanh và âm sin, không phải podcast, không được dùng để mở khóa tập thử.

## Lịch sau tập thử

Chưa bật automation. Chỉ sau bài tập thử đã công khai, đúng Page, phát được và kiểm phụ đề mới dùng automation_update để tạo lịch gắn chat 19:30 Asia/Bangkok. Lưu id và cấu hình tool trả về, không chỉ đổi enabled trong JSON rồi gọi là có lịch. Lô tiếp theo đúng 10 tập, một slot/ngày, ảnh xoay theo số tập.

Prompt vận hành lịch phải yêu cầu đọc STOP và hàng đợi, kiểm đăng trùng, bảo đảm chỉ một tập/ngày, kiểm cap gồm retry, không mua credit, không tự cài, lưu bằng chứng và chỉ báo thay đổi có ý nghĩa/thành công/lỗi/cần người dùng. Bỏ qua slot lỡ, không đăng bù dồn. Nếu phiên hết hạn, dừng để người dùng đăng nhập. Điều kiện app/máy và múi giờ phải được kiểm trong lúc tạo lịch; lượt chạy thực tế mới chứng minh lịch hoạt động.
# Yêu cầu bàn giao và lịch cập nhật

Tạo thumbnail với Python bundled: `python scripts/thumbnail.py` (MT-0001, ảnh khóa 1). Font Times New Roman Bold đã kiểm dấu tiếng Việt trên ảnh xuất thực tế.

Sau khi cắt, nhận dạng và nghe sửa phụ đề, burn vào bản nội dung; gọi `python scripts/chen-thumbnail.py --input <bản-nội-dung-có-phụ-đề> --thumbnail <thumbnail.png> --srt <SRT-nội-dung> --output 06-san-sang-dang/<mã-tập>/final.mp4`. Công cụ giữ source, thêm 30 frame ở 30 fps kèm 1 giây im lặng, dịch SRT +1 giây. Dùng thư mục bàn giao chưa có SRT để tránh ghi đè. Cần nghe/xem bản cuối; test fixture không thay thế QA tập thật.

Lịch chưa bật. Heartbeat chỉ gọi chat/nhắc việc không đủ chứng minh tự sản xuất và đăng. Cần máy thức, app Codex hoạt động, phiên Flow và Facebook còn quyền, không OTP/CAPTCHA, STOP tắt và credit đủ. Nếu thiếu điều kiện phải dừng và báo, không đăng bù. Sau pilot phải thử một lượt lịch thực sự đến bước tạo/cắt/phụ đề/QA/đăng/xác minh rồi mới báo lịch được kiểm chứng.

