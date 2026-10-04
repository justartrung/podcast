# 08 — Quyết định của chủ (sổ ghi, mới nhất ở trên)

Quyết định ở đây **ưu tiên hơn** mọi tài liệu trong `ban-sao-goc/` (hệ thống Codex 30/09). Trích nguyên văn, có ngày giờ.

## 2026-10-03 18:11–18:21 — Duyệt MT-0001; đăng bài trên Page; tự làm + đăng 1 tập/ngày 19:30
> "duyệt , bạn mở facebook trên app claude và bảo mình đăng nhập bằng tay , sau đó tạo caption và set lịch đăng ( lúc 19h30 hằng ngày)"
> "hẹn đăng qua meta business suite( trên facebook) , tự làm + đăng 1 tập/ngày ( lịch 19:30). Trong trường hợp 1 ngày làm được 3,4 cái video thì hỏi chính tôi nếu muôn đăng tất cả lên hay vẫn đăng 1 video/ngày. Nếu đăng 1 video/ngày và vẫn thừa mấy video còn lại thì đăng dồn ngày hôm sau. Tôi đã đăng nhập facebook rồi"
> "tôi bảo tạo bài đăng trên trang chứ không phải chỉ một mình reel, vì khi tạo bài đăng trên trang thì có option đăng lên reel luôn"

**Áp dụng (thay quyết định 17:00 về lịch):**
1. **MT-0001 đã được chủ duyệt** → hẹn đăng 19:30 hôm nay.
2. **Cách đăng:** Meta Business Suite → **Create post** (bài viết trên Page, KHÔNG dùng "Create reel" riêng) → bật tùy chọn chia sẻ thành Reel nếu có → **Schedule** (Set date and time).
3. **Lịch hằng ngày:** Claude **tự làm + đăng 1 tập/ngày, hẹn 19:30** (giờ VN).
4. Nếu trong 1 ngày làm được 3–4 video → **hỏi chủ**: đăng tất cả hay vẫn 1 video/ngày.
5. Nếu 1 video/ngày mà còn thừa video → **xếp sang các ngày sau**, mỗi ngày 1 bài lúc 19:30 ("đăng dồn ngày hôm sau" = hàng chờ, không đăng nhiều bài cùng ngày).
6. Chủ tự đăng nhập Facebook bằng tay trong trình duyệt app Claude (đã làm 18:15).

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

## 04/10/2026 01:19 — GitHub do chủ nhắn Claude push
> "à thôi, khi nào lịch nào đó set up được đăng lên thì tôi sẽ nhắn cho bạn để bạn push lên github"
- Không gắn repo vào tác vụ 13:47. Tác vụ vẫn commit theo mốc trong phiên của nó; push 403 → lưu `git bundle` vào `D:\PODCAST VAN HANH\bang-chung\` (docs/13 mục 6).
- Khi chủ nhắn (sau khi một tập đã hẹn lịch), phiên Claude có quyền push: nạp các bundle chưa push (fast-forward) → push main; nếu không có bundle thì đối chiếu Business Suite Scheduled + file trên D: rồi ghi bù.

## 04/10/2026 14:34 — Lời nói tự nhiên + trang phục host mới
> "tôi muốn update thêm quần áo host ( mẫu quần áo tối sẽ tải cho bạn ) và có 1 thứ tôi cần update là nội dung nói ( câu từ ) video nên được giống người và tự nhiên nhất, cần bạn update cái này, có thể là thêm repo viết lách câu từ nào đó trong github"
- Lời nói: bộ quy tắc `docs/14-loi-noi-tu-nhien.md`, áp dụng từ MT-0005; tập đã hẹn giữ nguyên.
- Trang phục host: chờ chủ gửi mẫu (tối 04/10) → quy trình `docs/12`.
