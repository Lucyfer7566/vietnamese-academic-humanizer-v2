# Vietnamese Academic Style — Hướng dẫn biên tập theo ngữ cảnh

## Mục tiêu
Biên tập tiếng Việt học thuật có logic, có chủ thể và có nhịp đọc dễ theo dõi. "Mùi AI" chỉ là nhãn không chính thức cho vấn đề văn phong; **không phải bằng chứng tác giả**.

## 9 loại vấn đề thường gặp
1. **Mở đầu rỗng:** “Trong bối cảnh công nghệ ngày càng phát triển...” → gọi đúng vấn đề kỹ thuật/đối tượng nghiên cứu.
2. **Tính từ cường điệu:** “mang tính đột phá”, “vô cùng quan trọng” → nêu cụ thể vai trò hoặc bỏ nếu không có bằng chứng.
3. **Chủ thể mơ hồ:** “Việc này giúp cải thiện...” → xác định cái gì tác động đến metric nào.
4. **Danh từ hóa:** “Tiến hành thực hiện việc đánh giá...” → “Đánh giá...” khi vẫn chính xác.
5. **Bị động vô cớ:** “Mô hình đã được tiến hành xây dựng...” → “Nhóm nghiên cứu xây dựng mô hình...”; nếu Methods cần tránh xưng “chúng tôi”, “Mô hình được huấn luyện...” vẫn đúng.
6. **Liên từ nối ý giả:** “Bên cạnh đó” khi hai câu có quan hệ giải thích/đối lập/nhân quả. Chọn đúng quan hệ hoặc bỏ nối.
7. **Nhắc lại thông điệp:** lặp “mục tiêu tối ưu hiệu quả” ở nhiều câu nhưng không cung cấp thông tin mới.
8. **Dịch máy không theo thuật ngữ ngành:** “thu hồi thông tin tăng cường tạo sinh” khi đề tài đang chuẩn hóa “sinh tăng cường truy xuất (RAG)”. Quyết định theo từ điển đề tài, không tự đổi tùy hứng.
9. **Tuyên bố vượt chứng cứ:** “chứng minh hiệu quả vượt trội” trong khi chỉ có quan sát trên một bộ dữ liệu. Đây là lỗi học thuật ưu tiên cao hơn phong cách.

## Danh mục những biểu thức cần xem lại, KHÔNG phải blacklist
| Cụm thường gặp | Câu hỏi biên tập | Cách sửa nếu thực sự thừa |
|---|---|---|
| Trong bối cảnh hiện nay | Thời gian/bối cảnh có quyết định claim không? | Đi thẳng vào vấn đề, hoặc nêu mốc cụ thể có nguồn |
| Không thể phủ nhận rằng | Có chứng cứ hay chỉ là lời dẫn? | Bỏ phần dẫn, viết luận điểm có căn cứ |
| Đóng vai trò quan trọng | Quan trọng theo cơ chế/biến nào? | Mô tả vai trò thực tế, không tự thêm số liệu |
| Giải pháp toàn diện, tối ưu | Đã chứng minh tính tối ưu chưa? | “phương pháp/giải pháp được đề xuất” |
| Không chỉ... mà còn... | Có thật hai chức năng không? | Giữ nếu giúp liệt kê logic, nếu không thì tách |
| Điều này cho thấy | “Điều này” chỉ vào bằng chứng nào? | Dùng chủ thể, kết quả cụ thể |
| Tận dụng, khai thác tối đa | Mức tối đa đo được không? | “sử dụng”, “áp dụng” |
| Một cách hiệu quả | Tiêu chí hiệu quả là gì? | Nêu metric hoặc bỏ |
| Tóm lại | Đoạn kết có nhắc lại vô ích không? | Nêu hàm ý/giới hạn thực sự |
| Đáng chú ý là | Có tiêu chí đáng chú ý? | Đi thẳng vào kết quả, điều kiện |

## Công thức biên tập ở cấp câu
- **Cụ thể hóa mà không bịa:** “Hệ thống cải thiện đáng kể” → nếu tài liệu không có số liệu, sửa thành “Hệ thống được thiết kế nhằm cải thiện ...” chỉ khi gốc xác nhận đây là *mục tiêu thiết kế*; không viết thành kết quả đạt được.
- **Đặt điều kiện đúng chỗ:** “Mô hình có độ chính xác cao khi ...” giữ gắn phạm vi theo bài gốc.
- **Tách câu overloaded:** mỗi câu chỉ nên có một trục ý chính. Nhưng nhiều ý phụ điều kiện/công thức có thể cần một câu dài.
- **Mối nối logic:** quan hệ **bổ sung / tương phản / nguyên nhân / điều kiện / ví dụ / hệ quả / giới hạn** phải có nội dung chứng minh, không chọn theo sở thích mỹ thuật.
- **Từ nối và nhịp điệu:** giữ đủ để người đọc theo được lý lẽ. Không dùng quota liên từ/câu hỏi tu từ/câu ngắn.

## Mức văn phong
- **Đại học:** rõ ràng, diễn giải đủ nền tảng, dùng thuật ngữ đúng; không “ngây thơ hóa”.
- **Thạc sĩ kỹ thuật (mặc định):** chính xác, tập trung vào thiết kế và bằng chứng, diễn giải quyết định phương pháp, nêu hạn chế.
- **Bài báo học thuật:** chú trọng tính cô đọng, chuẩn submission venue, kỷ luật claim và nguồn.

## Tiếng Việt chuyên ngành AI/SE
Giữ nguyên dạng theo hồ sơ thuật ngữ khi xuất hiện: `large language model (LLM)`, `retrieval-augmented generation (RAG)`, `fine-tuning`, `embedding`, `precision`, `recall`, `F1-score`, `accuracy`, `latency`, `throughput`, `drift`, `pipeline`, `baseline`, `ablation`, `train/validation/test split`. Có thể Việt hóa nếu tác giả đã chọn quy ước; đừng trộn hai cách gọi gây nhầm thực thể. Không “dịch cho khác” tên thư viện/framework, bộ dữ liệu, metric hay phương pháp.

## Điều chỉnh theo đoạn
Trước sửa, hỏi thầm: (1) Đoạn này trả lời câu hỏi gì? (2) claim nào chính? (3) bằng chứng nào đi kèm? (4) điều kiện/ngoại lệ nào không thể bỏ? (5) người đọc cần biết gì ở câu sau? Chỉ sửa những điểm khiến một trong năm câu hỏi trả lời khó khăn.

## Kiểm tra bằng cách đọc
Đọc từng câu: có động từ chính dễ tìm không; chủ thể có nhất quán không; referent của “này/đó” có rõ không; câu điều kiện có gắn đúng kết luận không; thuật ngữ có ổn định không. Sau đó đọc cả đoạn để kiểm tra progression. Không đánh giá tự nhiên bằng một con số perplexity/burstiness nào.
