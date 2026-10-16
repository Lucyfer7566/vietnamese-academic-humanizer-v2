# Tích hợp quy trình nghiên cứu và biên tập đa chương

## Nguồn cảm hứng và phạm vi kế thừa
`lishix520/academic-paper-skills` có **strategist** (nền tảng nghiên cứu, nguồn, bố cục, đánh giá phản biện) và **composer** (triển khai bản thảo theo outline, kiểm tra chất lượng ở cấp chương/toàn bài). Bộ v2 **kế thừa ý tưởng gates và kiểm tra coherence**, không sao chép nội dung, và không áp các định mức triết học/tiền ấn phẩm (số tài liệu, giới hạn chữ, chuẩn platform) cho mọi luận văn thạc sĩ kỹ thuật.

## Lớp A — Research context (tùy chọn, không tự bịa)
1. **Research question & contribution:** câu hỏi, đối tượng, baseline, phạm vi.
2. **Evidence pack:** giấy tờ nguồn DOI/URL/PDF, dữ liệu thực nghiệm, bảng đánh giá, code/repo (nếu được cung cấp hoặc tác giả cho phép kiểm tra).
3. **Terminology registry:** thuật ngữ Anh–Việt, viết tắt, dataset, model, architecture, metrics.
4. **School style guide:** template luận văn, chuẩn tham khảo, phân chương, xưng hô.
5. **Author voice profile:** chỉ lấy từ văn bản do người dùng viết.

Nếu tài liệu thiếu: ghi `UNKNOWN/NOT VERIFIED`; không suy diễn hoặc giả lập truy cập công cụ.

## Lớp B — Writer/Editor workflow
`outline/source → chapter contract → content inventory → reverse outline → revise structure (when needed) → local rewrite → invariant check → author review`

**Chapter contract** (ghi nội bộ): `reader question | prior knowledge | core claims | evidence | boundaries | exit understanding`. Nếu Chương 3 là thiết kế hệ thống thì không sửa sang giọng “bàn luận triết học”; nếu Chương 4 là thực nghiệm thì không trộn Method và Result.

## Lớp C — Audit Gates (chốt trước khi qua chương)
- **Gate A: scope & evidence:** đầu vào có đủ để hỗ trợ claim? Nếu không, ghi thiếu chứng cứ.
- **Gate B: style/context fit:** từ vựng phù hợp cấp học, chuyên ngành, trường và vị trí chương?
- **Gate C: consistency:** thuật ngữ/biến số/viết tắt/citation xuyên chương có nhất quán?
- **Gate D: reviewer view:** người đọc có phân biệt rõ đóng góp được chứng minh với tính năng dự kiến?
- **Gate E: final author review:** tác giả ký xác nhận các thay đổi nội dung (nếu có), hoàn thiện bản nộp.

Không tiến hành viết lại phần toàn văn nếu chỉ nhận đoạn trích. Việc đánh giá lập luận quy mô luận văn cần toàn văn, mục lục hoặc phạm vi đủ rộng.

## Mẫu reviewer simulation — 7 chiều
Chấm mỗi chiều 0–4, kèm span và bằng chứng, không giả vờ khách quan tuyệt đối:
1. Chính xác claim/bằng chứng
2. Độ rõ mục tiêu luận chứng
3. Tích hợp nguồn và trích dẫn
4. Tái lập/phương pháp (nếu liên quan)
5. Mạch bố cục và quan hệ logic
6. Diễn đạt tiếng Việt và thuật ngữ
7. Phù hợp chuẩn trường và tính minh bạch

Điểm số chỉ giúp ưu tiên biên tập; `critical integrity errors` luôn khiến kết quả FAIL bất kể tổng điểm. Không dùng điểm AI Detection làm quality gate.

## Làm việc trên repo của luận văn
- Ưu tiên đọc README, mục lục, `docs/`, `figures/`, config và báo cáo chạy có thật.
- Không đồng nhất mục tiêu xây dựng với tính năng đã hoạt động, hoặc tính năng chạy demo với chỉ số benchmark.
- Khi trích dẫn code: file/commit đã kiểm tra; không tự đặt đường dẫn.
- Kiểm soát bản sửa qua git diff hoặc changelog; tránh sửa nhiều chương một lúc nếu chưa audit consistency.
