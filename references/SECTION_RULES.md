# Section-Specific Academic Editing — Khóa luận/luận văn kỹ thuật

**Nguyên tắc:** Chỉnh đúng chức năng từng chương thay vì áp công thức "humanize" như nhau cho mọi đoạn. Theo quy định của trường/khoa nếu có khác biệt.

## Tóm tắt (Abstract)
Phải thể hiện đúng bài đã làm: vấn đề, mục tiêu, phương pháp, dữ liệu/thiết kế thực nghiệm nếu có, kết quả **đã được cung cấp**, kết luận ở mức chứng cứ cho phép. Tránh mở bằng lịch sử vĩ mô, diễn đạt thành tựu chưa có. Không ép tỷ lệ câu hoặc số mục cố định. Kiểm tra đặc biệt `proposed` vs `evaluated`.

## 1. Mở đầu / đặt vấn đề
Chuỗi logic nên đọc được: **bài toán cụ thể → hạn chế của cách hiện có (có nguồn) → mục tiêu và phạm vi → đóng góp được chứng minh/được dự kiến → bố cục luận văn**. Không biến “cần tìm hiểu thêm” thành “chưa ai nghiên cứu”. Mỗi gap claim cần minh chứng; nếu không, gắn TODO xác thực.

## 2. Cơ sở lý thuyết / nghiên cứu liên quan
- Phân biệt lý thuyết nền tảng với tổng quan công trình liên quan.
- Mỗi công trình tóm lược: bài toán / phương pháp / điều kiện đánh giá / kết quả quan trọng / hạn chế thực sự được nguồn ghi nhận.
- Gom nhóm theo hướng tiếp cận hoặc tiêu chí so sánh, **không chỉ nối các bản tóm tắt công trình**.
- Kết phần bằng khoảng trống hoặc tiêu chí thiết kế **được dữ liệu/tài liệu hỗ trợ**.
- Citation đi theo đúng nhận định; diễn giải lại không được làm sai chính kiến tác giả nguồn.

## 3. Phân tích và đề xuất giải pháp / kiến trúc hệ thống
- Vạch rõ yêu cầu chức năng/phi chức năng, phạm vi, ràng buộc, giải pháp chọn và lý do chọn.
- Không thay luồng hệ thống thành quan hệ nhân quả khoa học. Gọi đúng service, module, API, queue, container, lớp mô hình, pipeline.
- “Đề xuất” khác “triển khai”, “sẵn sàng hoạt động” khác “đã benchmark”.
- Giữ tên interface, schema, tham số, hình/bảng, dependency và thuật toán.
- Đừng đưa tên code file/job ID vào văn bản chính nếu không giúp giải thích giải pháp; nhưng vẫn giữ những chi tiết phục vụ tái lập nơi thích hợp.

## 4. Cài đặt và thực nghiệm / đánh giá
- **Methods:** cấu hình, dữ liệu, tiền xử lý, điều kiện thí nghiệm, split, máy/phiên bản khi quyết định khả năng tái lập.
- **Results:** chỉ mô tả điều đo được, gắn metric và comparator; giữ bảng, số, khoảng tin cậy, phân nhóm.
- **Interpretation:** giải thích hợp lý nhưng không khẳng định cơ chế khi chưa kiểm chứng.
- Kiểm tra `latency` vs `throughput`, `accuracy` vs `F1`, `macro` vs `weighted`, tập `validation` vs `test`.
- Nếu đề tài **chưa có thực nghiệm**, chỉ viết thiết kế đánh giá / kế hoạch thực nghiệm; không tạo con số minh họa giả trong phần kết quả.

## 5. Thảo luận / giới hạn
Kết nối nhận định tới số liệu/bằng chứng cụ thể; nêu điều kiện áp dụng, tình huống chưa kiểm tra, chi phí/rủi ro nếu có trong dữ liệu. Không thêm phản biện giả chỉ để tăng sắc thái “người thật”. Tránh lặp nguyên Results và làm kết luận mạnh hơn dữ liệu.

## 6. Kết luận và hướng phát triển
Chốt kết quả **đã làm được**, điều chưa làm và hướng phát triển có liên hệ với hạn chế. Nếu chỉ có prototype, không biến thành hệ thống triển khai thực tế hay giải pháp được chứng minh ở quy mô lớn. Không phóng đại “tạo ra cuộc cách mạng”.

## Toàn văn
- **Reverse outline** từng đoạn: chức năng, claim, evidence, position.
- **Cross-chapter coherence:** Introduction nêu mục tiêu gì? Methods có triển khai đủ? Results có báo cáo? Conclusion có dựa vào Results?
- **Source-to-claim traceability:** mọi citation có thực và dùng đúng chỗ; nếu citation move, claim nó hỗ trợ cũng phải move.
- **Vocabulary registry:** chuẩn hóa cách gọi đầu tiên (đầy đủ + viết tắt), dùng xuyên suốt.
- **Formatting:** heading, cross-reference, công thức, hình/bảng phù hợp quy định trường; không tự áp tỷ lệ chữ của bài báo triết học vào luận văn kỹ thuật.

## Khi chỉ có một đoạn
Không suy ra nội dung chương khác, không bổ sung “khoảng trống nghiên cứu” hay “đóng góp” từ trí tưởng tượng. Nếu đoạn phụ thuộc hình/bảng chưa kèm, sửa mức nhỏ và gắn `NEEDS CONTEXT` ở báo cáo.
