# 08 — Quyết định của chủ (sổ ghi, mới nhất ở trên)

Quyết định ở đây **ưu tiên hơn** mọi tài liệu trong `ban-sao-goc/` (hệ thống Codex 30/09). Trích nguyên văn, có ngày giờ.

## 2026-10-03 17:12 — Tool video, nơi lưu, FFmpeg, duyệt tập đầu
> "https://flow.google.com/project/f37b741b-b3f2-40f8-b490-f23f79b098ed/tool/6dae8db1-89cf-475a-9412-3334f68ebfdd Đây là link dự án làm video podcast, khi bạn mở flow tôi sẽ đăng nhập vào bằng gmail…"
> "Video làm ra khi có phụ đề và cắt dựng ffmeg sẽ được lưu ở ổ D (bạn tự đặt tên thư mục), sau khi video được lưu trên ổ D … sẽ được đăng tự động lên facebook (cũng do tự bạn làm)."
> "phần cắt dựng và phụ đề chạy trên ffmeg (bạn tải hộ tôi cũng được), bộ công cụ trên máy là bản windows."
> "khi chất lượng đạt thì tôi muốn kiểm tra tập đầu trước khi đăng. Sau đó khi quy trình ổn định thì tự động đăng (tải cái gì thì tải trong ổ D nhé, ổ C tôi đầy)"

**Áp dụng:**
1. **Tool video hiện hành:** Flow project `f37b741b-b3f2-40f8-b490-f23f79b098ed`, tool `6dae8db1-89cf-475a-9412-3334f68ebfdd`. Thay cho tool `10a20665…` (project `286e14cd…`) trong `cau-hinh-kenh.json` gốc. Chủ tự đăng nhập Gmail.
2. **Thư mục làm việc mới:** `D:\PODCAST VAN HANH` (do chủ tạo, Claude được cấp quyền). Thư mục gốc `D:\PODCAST TU DONG` vẫn chỉ đọc.
3. **Hậu kỳ bằng FFmpeg** + phụ đề từ audio (faster-whisper, dùng lại model small đã có trong `08-cong-cu/models`, chỉ đọc).
4. **Mọi tải về/cài đặt để trên ổ D**, không dùng ổ C.
5. **Tập đầu tiên: chủ xem trước khi đăng.** Sau khi quy trình ổn định → Claude tự đăng Facebook từ thư mục bàn giao.

## 2026-10-03 17:00 — Bỏ cổng pilot, chạy theo lệnh; Claude thay Codex
> "điều kiện mở lịch k cần thiết, chỉ cần làm video, xét chất lượng và đăng, bắt đầu quy trình theo câu lệnh, không cần làm liên tục 10 lô video đăng dần, chỉ làm lô tập nếu tôi yêu cầu."
> "tool flow báo không chạy được công cụ bởi vì lỗi codex của chat gpt, khi tôi xoá tab đó và mở thủ công tab mới thì sau vài lần thử nó cũng mở được và codex tiếp tục làm việc (lỗi này khá là lưu ý, khi bạn bàn giao hy vọng không gặp lỗi này). Bạn sẽ thay codex điều phối hết nhé"

**Áp dụng:**
1. **Bỏ cổng tập thử (pilot gate).** MT-0001 là tập bình thường, không phải điều kiện mở khóa gì.
2. **Chạy theo lệnh:** chủ ra lệnh → Claude chạy trọn 1 tập: research/chọn ý → kịch bản → tạo video → hậu kỳ → **Claude QA** → đăng → xác minh → báo cáo.
3. **Lô nhiều tập chỉ làm khi chủ yêu cầu.** Không tự lập lô 10, không tự bật lịch đăng định kỳ.
4. **Lỗi "Không chạy được công cụ" của Flow** là do trình duyệt của Codex, không phải tool hỏng. Cách xử lý đã biết: đóng tab đó, mở tab mới thủ công, thử lại vài lần → xem `docs/09-loi-da-biet.md`.
5. **Claude là đầu não duy nhất**, thay Codex điều phối toàn bộ (trả lời Q5). Không chạy song song Codex trên cùng tài khoản để tránh đăng trùng/tiêu credit trùng.

Các luật khác vẫn giữ: ≤ 80 credit/tập gồm tạo lại, không mua credit, thấy giá thật mới tạo, QA đủ bằng chứng trước khi đăng, chống đăng trùng, chỉ chuyện gia đình, không lời chào, không sửa thư mục gốc D:.
