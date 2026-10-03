# 05 — Bản đồ thư mục gốc `D:\PODCAST TU DONG` (≈1,2 GB, 4.673 file)

| Thư mục | Nội dung | Trên GitHub? |
|---|---|---|
| `AGENTS.md` | Điểm vào cho agent: đọc cấu hình kênh, Agent Tổng, skill; tóm yêu cầu 30/09 | ✅ `ban-sao-goc/AGENTS.md` |
| `01-tai-lieu/` | Tài liệu gốc: Cẩm nang Công xưởng Subagent (PDF 15 trang, Phong Menly); Hướng dẫn chạy nhiều tài khoản Codex (docx); skill gốc Podcast Minh Thư (zip, có lời chào – **đã bị thay**); skill Subagent tạo video v1.1 (zip, dành cho TVC **không thoại** – chỉ tham khảo thao tác Flow) | ✅ bản trích văn bản `ban-sao-goc/tai-lieu/` |
| `02-host/` | 4 ảnh host MINH THƯ `1.png`–`4.png` (~2,3 MB mỗi ảnh) | ❌ chỉ hash trong `ban-sao-goc/MEDIA-KHONG-DUA-LEN.tsv` |
| `03-he-thong/` | Bộ não hệ thống: `cau-hinh-kenh.json` (v3), `agent-tong.md`, `quality-gate.md`, `van-hanh.md`, `registry.json`, `trang-thai.json`, `STOP.json`, `kiem-ke.json`, `phieu-de-xuat.md`, `bao-cao-kiem-thu.md`, `flow-tool-da-quan-sat.md`, `kiem-tra-character.md` | ✅ |
| `04-hang-doi/hang-doi.json` | Hàng đợi tập: MT-0001, MT-0002 (đều draft) | ✅ |
| `05-nhat-ky/events.jsonl` | 13 sự kiện 30/09/2026 12:24 → 16:18 | ✅ |
| `06-san-xuat/MT-000x/` | Kịch bản, phương án ngân sách, QA biên tập | ✅ |
| `06-san-sang-dang/MT-0001/` | Gói bàn giao: thumbnail.png, caption.txt, provenance (chưa có final.mp4, srt) | ✅ trừ ảnh |
| `07-bang-chung/` | 17 ảnh chụp màn hình Flow/Facebook + 4 bản dump trang research | ❌ (có thể chứa thông tin người khác) |
| `08-cong-cu/` | FFmpeg 9.0.2 Windows, python-env (faster-whisper 1.2.1, PyAV 16.0.1), model whisper small, hf-cache (~1,1 GB) | Chỉ `requirements-lock.txt` |
| `09-kiem-thu/` | Fixture kiểm thử kỹ thuật (nền xanh, âm sin) — **không phải podcast** | ✅ chỉ json/srt |
| `10-nghien-cuu/` | Research vòng 1 (30/09), danh sách nguồn, kho 5 ý tưởng, lịch sử chủ đề | ✅ |
| `scripts/` | `quan-ly.py` (ledger/STOP/hàng đợi/QA/đăng, 13 test), `hau-ky.py` (cắt/ASR/render/check), `thumbnail.py`, `chen-thumbnail.py`, `cap-nhat-yeu-cau.py` | ✅ |
| `skills/podcast-minh-thu/` | Skill vận hành hiện hành (đã cập nhật yêu cầu 30/09) | ✅ |

**Thứ tự ưu tiên tài liệu khi mâu thuẫn:** yêu cầu mới nhất của chủ trong chat → `AGENTS.md` / `03-he-thong/*` / `skills/` (30/09) → `01-tai-lieu/*` (tài liệu gốc, chỉ tham khảo).
