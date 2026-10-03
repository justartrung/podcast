# 🎙️ Podcast tự động — "Chuyện đời cùng Minh Thư"

Repo quản lý dự án podcast chuyện gia đình, host AI **MINH THƯ**, đăng chính trên Facebook Page [Chuyện đời cùng Minh Thư](https://www.facebook.com/chuyendoicungminhthu).
**Claude** là đầu não điều phối duy nhất (thay Codex từ 03/10/2026). **Tự làm + đăng 1 tập/ngày lúc 19:30**: tìm nội dung viral → chốt → kịch bản → giao tool tạo video → hậu kỳ → duyệt → đăng → xác minh → báo chủ. Lô nhiều tập chỉ khi chủ yêu cầu.

> Dữ liệu gốc (ảnh host, công cụ, bằng chứng) nằm trên máy chủ tại `D:\PODCAST TU DONG` và **không bị chỉnh sửa**. Repo này giữ kế hoạch, trạng thái, góp ý và bản sao văn bản để mọi phiên chat mới đọc được toàn bộ dự án.

## Bắt đầu nhanh
| Muốn biết | Mở |
|---|---|
| Đang ở đâu, bị chặn gì, làm gì tiếp | [STATUS.md](STATUS.md) |
| Claude hiểu dự án thế nào (chủ duyệt) | [docs/01-hieu-du-an.md](docs/01-hieu-du-an.md) |
| Quy trình + ai làm gì | [docs/02-quy-trinh-van-hanh.md](docs/02-quy-trinh-van-hanh.md) |
| Kế hoạch theo giai đoạn | [docs/03-ke-hoach.md](docs/03-ke-hoach.md) |
| Luật cứng | [docs/04-quy-tac-cung.md](docs/04-quy-tac-cung.md) |
| Bản đồ thư mục gốc D: | [docs/05-ban-do-thu-muc-goc.md](docs/05-ban-do-thu-muc-goc.md) |
| **Câu hỏi chờ chủ trả lời** | [docs/06-cau-hoi-mo.md](docs/06-cau-hoi-mo.md) |
| Cách tìm nội dung viral | [docs/07-phuong-phap-tim-viral.md](docs/07-phuong-phap-tim-viral.md) |
| **Quyết định của chủ** (ưu tiên cao nhất) | [docs/08-quyet-dinh-cua-chu.md](docs/08-quyet-dinh-cua-chu.md) |
| Lỗi đã biết & cách xử lý (lỗi tab Flow) | [docs/09-loi-da-biet.md](docs/09-loi-da-biet.md) |
| Thư mục làm việc `D:\PODCAST VAN HANH` | [docs/10-thu-muc-van-hanh.md](docs/10-thu-muc-van-hanh.md) |
| Tool Flow PODCAST: giao diện, mã, giá | [docs/11-tool-flow-podcast.md](docs/11-tool-flow-podcast.md) |
| **Quy trình chạy hằng ngày** | [docs/13-quy-trinh-hang-ngay.md](docs/13-quy-trinh-hang-ngay.md) |
| Thêm / thay ảnh host | [docs/12-them-anh-host.md](docs/12-them-anh-host.md) · bảng ảnh [host/](host/) |
| Các tập | [tap/](tap/) |
| Research & kho ý tưởng | [nghien-cuu/](nghien-cuu/) |
| Góp ý sửa hệ thống gốc | [de-xuat/](de-xuat/) |
| Nhật ký phiên | [nhat-ky/](nhat-ky/) |

## Mở phiên chat mới
Dán câu trong [templates/phien-moi.md](templates/phien-moi.md) vào chat của Project "PODCAST".

## Cấu trúc
```
README.md          ← bạn đang ở đây
CLAUDE.md          ← hướng dẫn cho Claude đầu mỗi phiên
STATUS.md          ← trạng thái sống (cập nhật mỗi phiên)
docs/              ← hiểu dự án, quy trình, kế hoạch, quy tắc, câu hỏi
tap/               ← mỗi tập 1 file (MT-0001.md …)
nghien-cuu/        ← vòng research + kho ý tưởng
de-xuat/           ← góp ý sửa hệ thống gốc (chờ duyệt)
nhat-ky/           ← nhật ký phiên theo ngày
templates/         ← mẫu dùng lại
ban-sao-goc/       ← bản sao văn bản D:\PODCAST TU DONG (03/10/2026, chỉ đọc)
```
