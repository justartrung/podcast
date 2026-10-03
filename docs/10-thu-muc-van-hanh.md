# 10 — Thư mục làm việc `D:\PODCAST VAN HANH`

Nơi Claude **được ghi**. Thư mục gốc `D:\PODCAST TU DONG` vẫn **chỉ đọc** (dùng lại ảnh host, model whisper, tài liệu).

```
D:\PODCAST VAN HANH\
├─ cong-cu\                 ← thư viện Python cho phụ đề (faster-whisper bản Linux, cài bằng pip --target), cache pip
├─ san-xuat\MT-xxxx\        ← làm việc từng tập
│   ├─ clip-goc\            ← clip tải từ Flow (giữ nguyên, ghi hash)
│   ├─ cat-dung\            ← manifest cắt, bản ghép
│   ├─ phu-de\              ← transcript ASR, SRT đã nghe sửa
│   └─ qa\                  ← QA JSON, ảnh khung kiểm, ffprobe
├─ san-sang-dang\MT-xxxx\   ← GÓI ĐĂNG: final.mp4, thumbnail.png, caption.txt, subtitles.srt
├─ da-dang\MT-xxxx\         ← sau khi đăng: permalink.txt, ảnh chụp bài, thời gian đăng
└─ bang-chung\              ← ảnh chụp màn hình Flow/Facebook theo ngày
```

## Luồng tự động đăng
1. Tập đạt QA → gói đầy đủ ở `san-sang-dang\MT-xxxx\`.
2. **Tập đầu (MT-0001): chờ chủ xem và duyệt** → mới đăng.
3. Khi chủ xác nhận quy trình ổn định: Claude tự đăng mọi gói đã đạt QA trong `san-sang-dang\` lên Page, rồi chuyển bằng chứng sang `da-dang\`.
4. Trước khi đăng luôn kiểm `da-dang\` + Page để không đăng trùng.

## Môi trường hậu kỳ (đã kiểm 03/10)
- Shell của Claude trên máy là Linux VM (Ubuntu 22.04, 2 CPU, 3 GB RAM). Đã có sẵn **FFmpeg 4.4.2** (có bộ lọc `subtitles`/libass) — không cần tải.
- faster-whisper 1.2.1: cài vào `D:\PODCAST VAN HANH\cong-cu\` (PyPI truy cập được). **Không cài vào ổ C / máy ảo.**
- Model whisper small: dùng lại bản đã tải `D:\PODCAST TU DONG\08-cong-cu\models\models--Systran--faster-whisper-small\snapshots\536b0662…` (chỉ đọc). HuggingFace bị chặn từ máy ảo nên không tải lại được — bản có sẵn là đủ.
- Font tiếng Việt cho phụ đề/thumbnail: cần kiểm (máy ảo có DejaVu, Liberation, Noto).
- Bản FFmpeg/python-env Windows trong `08-cong-cu` không chạy được trong máy ảo Linux (giữ nguyên, không xóa).
