# 02 — Quy trình vận hành (Claude làm "đầu não")

## Sơ đồ tổng

```
 [1] TÌM NỘI DUNG ──► [2] CHỐT 1 Ý ──► [3] KỊCH BẢN ──► [4] GIAO TOOL VIDEO ──► [5] HẬU KỲ
  FB/TikTok/YT          chấm điểm        gốc, CTA          Flow tool (chủ gửi)     cắt, ASR, SRT,
  bằng chứng số liệu    5 ý → chọn 1     không chào        reservation ≤80 credit  thumbnail 1s
                                                                                       │
 [9] BÁO CHỦ ◄── [8] XÁC MINH ◄── [7] ĐĂNG ◄────────── [6] CLAUDE DUYỆT & CHỐT (QA) ◄──┘
  tóm tắt +        permalink,        Page đúng,             quality gate đủ bằng chứng
  link bài         phát được         giờ theo lệnh            gắn SHA-256 master
```

Mỗi mũi tên chỉ đi tiếp khi bước trước **có bằng chứng thật**. Lỗi → sửa đúng chỗ, tối đa 1 lần thử lại, rồi dừng và báo.

## Ai làm gì

| Vai trò (registry gốc) | Ai/Công cụ thực hiện khi Claude điều phối | Ghi chú |
|---|---|---|
| **Agent Tổng** — điều phối, ngân sách, STOP, QA, xác minh | **Claude** trong chat của Project "PODCAST" | Đọc repo này đầu mỗi phiên |
| **Podcast** — chủ đề, thoại, CTA, khóa ảnh | **Claude** (research web + viết) | Theo `ban-sao-goc/skills/podcast-minh-thu/` |
| **Flow** — tạo clip | **Tool video chủ gửi** (hiện là Google Flow tool), Claude thao tác qua **trình duyệt trên máy chủ** (built-in browser của app Claude, hoặc Claude in Chrome) | Chủ tự đăng nhập/OTP |
| **Hậu kỳ** — cắt, phụ đề, kiểm master | Claude chạy FFmpeg + faster-whisper | **Cần chốt môi trường** (xem dưới) |
| **Facebook** — đăng, chống trùng, kiểm permalink | Claude qua trình duyệt trên máy chủ, danh tính Page | Chủ tự đăng nhập |
| **Lưu trạng thái/kế hoạch** | **GitHub repo này** | Không sửa thư mục gốc D: |
| **Kích hoạt** | **Lệnh của chủ** trong chat (mỗi lệnh 1 tập). Lô/lịch định kỳ chỉ khi chủ yêu cầu — khi đó dùng "Scheduled task" của Claude (cần máy bật + app Claude mở + phiên Flow/FB còn hạn) | Mặc định: theo lệnh |

## Ánh xạ công cụ Codex → Claude

| Hệ thống cũ (Codex) | Thay bằng (Claude) | Trạng thái |
|---|---|---|
| `cua_repl` (trình duyệt trong Codex) | Built-in browser của app Claude desktop / Claude in Chrome | Cần thử: mở Flow tool + Page FB. Lỗi tab Flow → `docs/09-loi-da-biet.md` |
| `automation_update` (lịch gắn chat) | Scheduled task của Claude (`create_trigger`, có tùy chọn cần máy tính) | Chỉ tạo khi chủ yêu cầu |
| Python bundled `C:/Users/start/.cache/codex-runtimes/...` | Python trên máy / shell của Claude | Cần kiểm |
| `08-cong-cu/ffmpeg/*.exe`, `08-cong-cu/python-env` (Windows) | Shell Claude trên máy là **Linux VM** — **không chạy được file .exe Windows**. Phương án: (a) cài ffmpeg + faster-whisper trong VM/cloud của Claude (cần Phiếu duyệt), hoặc (b) chủ chạy lệnh trên Windows | **Cần chủ chọn** |
| `scripts/quan-ly.py` (ledger, STOP, chống đăng trùng) | Dùng lại logic, nhưng **trạng thái ghi trên GitHub** (`STATUS.md`, `tap/MT-xxxx.md`) thay vì sửa JSON trong D: | Đề xuất |

## Một lệnh = một tập (mặc định)
Chủ nói kiểu "làm 1 tập" / "làm tập MT-0002" → Claude: (1) chọn ý (từ kho hoặc research mới) → (2) kịch bản → (3) mở tool bằng **tab mới**, xem giá → (4) tạo cảnh 1, nghe/xem → các cảnh còn lại → (5) hậu kỳ → (6) QA 13 mục → (7) đăng → (8) mở permalink xác minh → (9) báo chủ. Dừng giữa chừng chỉ khi: cần đăng nhập/OTP, giá không rõ hoặc vượt 80 credit, tạo lại vẫn lỗi, QA không đạt, tool không mở được sau 3 lần tab mới.

## Giao thức mỗi phiên chat mới

1. Mở repo `justartrung/podcast`, đọc `CLAUDE.md` → `STATUS.md` → `docs/03-ke-hoach.md` → nhật ký mới nhất trong `nhat-ky/`.
2. Nếu cần chi tiết luật: `docs/04-quy-tac-cung.md` và `ban-sao-goc/`.
3. Làm việc. Mọi thay đổi trạng thái → cập nhật `STATUS.md` + file tập trong `tap/` + thêm dòng vào `nhat-ky/YYYY-MM-DD.md`.
4. Góp ý sửa hệ thống gốc → ghi `de-xuat/`, **không tự sửa D:**.
5. Commit với thông điệp tiếng Việt rõ ràng.

## Trạng thái một tập (dùng thống nhất)

`y-tuong` → `kich-ban` → `cho-tool` → `dang-tao` (có bằng chứng lượt tạo) → `hau-ky` → `da-qa` → `da-hen-lich` → `da-dang-xac-minh`
Nhánh lỗi: `loi-cho-xu-ly`, `publishing_unknown`, `huy`.
