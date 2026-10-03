# 09 — Lỗi đã biết & cách xử lý

## L1. Flow tool báo "Không chạy được công cụ" ⚠️ LƯU Ý CAO
- **Biểu hiện:** mở đúng URL tool, khung giữa hiện "Không chạy được công cụ. Bạn có muốn Tác nhân ứng dụng thử khắc phục…" với nút *Sửa lỗi* / *Tải lại* (ảnh gốc: `07-bang-chung/flow-character-tool-loi.jpg`). Có lúc khung studio trống.
- **Nguyên nhân (theo chủ, 03/10):** lỗi phía trình duyệt Codex/ChatGPT giữ tab hỏng — **không phải tool Flow hỏng**.
- **Cách xử lý đã hiệu quả (chủ làm thủ công):** đóng hẳn tab đó → mở **tab mới** → dán lại URL tool → thử lại vài lần → tool mở được.
- **Quy trình cho Claude:**
  1. Gặp lỗi → **không bấm "Sửa lỗi"** (nút này gọi tác nhân Flow sửa code tool — trước đây nó tự thêm thư viện ngoài phạm vi; có thể làm đổi tool).
  2. Đóng tab lỗi, mở tab mới, vào lại URL tool. Chờ tải xong hẳn.
  3. Thử tối đa 3 lần, mỗi lần cách ~30–60 giây.
  4. Vẫn lỗi → dừng, báo chủ kèm ảnh chụp, nhờ chủ mở thủ công 1 lần; **không** tạo media, **không** đổi sang tool khác.
  5. Ghi lần gặp lỗi + số lần thử vào nhật ký phiên để theo dõi tần suất.
- **Phòng ngừa:** không dùng lại tab Flow cũ từ phiên trước; luôn mở tab mới đầu mỗi lượt sản xuất. Trước khi tạo, tải clip đạt về ngay vì state của tool nằm trong trình duyệt (reload có thể mất).

## L2. Dữ liệu cảnh trong tool có thể mất khi tải lại
- Tool giữ cảnh/video trong bộ nhớ trình duyệt (React state). Tải mỗi clip đạt về máy và ghi hash ngay, trước khi reload/đóng tab.

## L3. Đường dẫn cũ trong `kiem-ke.json`
- Trỏ `D:\_CHUYEN NGHE TRADE_\PODCAST TU DONG\...` — thư mục đã chuyển về `D:\PODCAST TU DONG`. Dùng đường dẫn mới.

## L4. Tải video từ Flow rơi vào ổ C
- Tải xuống (mục Video → chuột phải → Tải xuống → 720p) lưu vào `C:\Users\ADMIN\Downloads`; đôi khi file ở dạng `<uuid>.tmp` nhưng đã đầy đủ (kiểm bằng ffprobe 10,006 s).
- Xử lý: chép sang `D:\PODCAST VAN HANH\san-xuat\<tập>\clip-goc\`, nhận diện cảnh bằng ASR, rồi xóa bản trong Downloads (chỉ xóa file vừa tải).

## L5. ffmpeg treo / chạy quá 3 phút
- Nguyên nhân 03/10: `apad` + `-shortest` trong filter_complex không kết thúc; các lần timeout để lại tiến trình ffmpeg chiếm CPU.
- Xử lý: không dùng `apad`; sau timeout chạy `ps aux | grep [f]fmpeg | awk '{print $2}' | xargs -r kill`.

## L6. Mỗi lần tải trang Flow phải xin quyền
- Trình duyệt app Claude hỏi chủ cho phép mỗi lần mở trang `flow.google.com` (và miền iframe `*.scf.usercontent.goog`). Nhờ chủ chọn "luôn cho phép" để giảm hỏi lại.
