# 07 — Phương pháp tìm nội dung viral (có bằng chứng)

Mục tiêu: chọn chủ đề **đang được quan tâm thật**, không đoán từ hashtag hay tiêu đề.

## Nguồn & phạm vi
- Facebook (Page/Reels/nhóm công khai), TikTok, YouTube (Shorts + video) — tiếng Việt, chủ đề gia đình.
- Từ khóa gốc: *hôn nhân, vợ chồng, mẹ chồng nàng dâu, tiền trong hôn nhân, giúp bố mẹ, việc nhà, nuôi con, ở riêng, ranh giới, giao tiếp vợ chồng*.
- Ưu tiên bài 30 ngày gần nhất; 30–90 ngày làm đối chiếu; cũ hơn chỉ tham khảo cấu trúc.

## Ghi nhận mỗi nội dung (bảng research)
`ID | nền tảng | kênh | link | ngày đăng (như UI hiện) | thời điểm kiểm (+07:00) | chủ đề | hook (đã nghe / chỉ caption) | xung đột | CTA | chỉ số có nhãn (view/like/comment/share) | mức đã xem | giới hạn`

## Tiêu chí "viral" (phải đạt ≥ 2/3)
1. **Vượt baseline kênh:** chỉ số ≥ 3× trung vị 10 bài gần nhất của chính kênh đó.
2. **Tăng trưởng thật:** đo 2 lần cách nhau ≥ 24 giờ, tăng rõ rệt (ví dụ view +50% hoặc share tăng liên tục).
3. **Tỷ lệ tương tác cao:** (comment + share) / view ≥ 2% hoặc share/like cao bất thường (dấu hiệu người xem gửi cho người thân).

Chưa đủ dữ liệu → ghi "**tiềm năng – chưa xác nhận**", không gọi là viral.

## Chấm điểm ý tưởng (0–5 mỗi mục, tổng 20)
| Mục | Hỏi |
|---|---|
| Phù hợp | Đúng chuyện gia đình, kể được tử tế trong ≤ 90 s? |
| Tiềm năng | Bằng chứng viral/tiềm năng của nhóm chủ đề? |
| Góc mới | Khác tập trước, không trùng mâu thuẫn liền kề? |
| Bằng chứng | Nguồn đã xem đủ, số liệu có nhãn? |

Mỗi vòng: 5 ý → **Claude tự chọn 1** (điểm cao nhất, ưu tiên đa dạng nhóm chủ đề) → kịch bản gốc → QA văn bản → `tap/`.

## Nhịp
- Chạy 1 vòng khi chủ ra lệnh làm tập mới mà kho ý tưởng không còn ý tốt, hoặc khi chủ yêu cầu research. Mỗi vòng đo lại các nguồn vòng trước để có số liệu tăng trưởng.
- Lưu: `nghien-cuu/YYYY-MM-DD.md` + cập nhật `nghien-cuu/kho-y-tuong.md`.
