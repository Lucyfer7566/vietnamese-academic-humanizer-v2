# Ví dụ biên tập — hoàn toàn minh họa, không phải dữ liệu nghiên cứu

**Lưu ý:** Các đoạn bên dưới là ví dụ tự tạo về cách diễn đạt. Không coi là phát hiện thực nghiệm, không lấy nguyên văn vào luận văn khi chưa có tài liệu của tác giả xác thực.

## 1. Sáo ngữ → chủ thể cụ thể
**Bản thô:** “Trong bối cảnh công nghệ trí tuệ nhân tạo phát triển vượt bậc, RAG đóng vai trò vô cùng quan trọng trong các hệ thống hỏi đáp. Cụ thể, hệ thống dùng RAG sẽ truy xuất các tài liệu có liên quan trước khi tiến hành sinh câu trả lời nhằm khai thác thêm tri thức ở nguồn ngoài.”

**Bản sửa:** “Retrieval-Augmented Generation (RAG) kết hợp bước truy xuất tài liệu với quá trình sinh câu trả lời. Cách tiếp cận này cho phép mô hình sử dụng thông tin lấy từ nguồn ngoài thay vì chỉ dựa vào tri thức đã học trong giai đoạn huấn luyện.”

**Chú ý bảo toàn:** bản sửa chỉ lấy cơ chế đã nêu trong bản thô, không khẳng định một hệ thống cụ thể đạt metric tốt hơn. Nếu thuật ngữ/khái niệm cần trích dẫn, tác giả phải cung cấp nguồn phù hợp.

## 2. Từ ngữ cường điệu → phát biểu về thiết kế
**Bản thô:** “Giải pháp đề xuất đã tạo ra sự đột phá trong việc phát hiện dữ liệu bất thường.”

**Tình huống A:** nếu chỉ có thiết kế chưa kiểm thử, **không thể** giữ mệnh đề “đã tạo ra sự đột phá”. Agent phải **báo lỗi claim–evidence** và đề xuất có điều kiện: “Đề tài đề xuất một quy trình phát hiện dữ liệu bất thường. Hiệu quả của quy trình cần được đánh giá qua các chỉ số đã xác định.” Chỉ dùng khi đúng tình trạng đề tài.

**Tình huống B:** nếu có số liệu đánh giá đã cung cấp, phải diễn giải đúng metric, tập dữ liệu, baseline, điều kiện. Không tự đặt ví dụ bằng số giả.

## 3. Sửa mạch đoạn nhưng không chèn phản biện giả
**Bản thô:** “Dữ liệu được chia thành các tập train, validation và test. Mô hình thực hiện huấn luyện. Ngoài ra, kết quả test giúp đánh giá hệ thống.”

**Bản sửa:** “Dữ liệu được chia thành ba tập phục vụ những mục đích khác nhau: huấn luyện, lựa chọn cấu hình và đánh giá cuối cùng. Tập huấn luyện dùng để cập nhật tham số mô hình; tập validation phục vụ lựa chọn cấu hình, còn tập test được giữ riêng để đánh giá sau khi quá trình lựa chọn mô hình hoàn tất.”

**Cảnh báo:** đây là quy trình ví dụ; chỉ dùng cho luận văn khi người viết xác nhận đúng vai trò từng tập, tránh suy ra cách chia dữ liệu từ tên gọi.

## 4. Không được tăng sức nặng kết luận
**Bản thô:** “Kết quả ban đầu cho thấy mô hình có thể phù hợp với tập dữ liệu A.”

**Sai:** “Mô hình đã chứng minh khả năng tổng quát hóa tốt trên nhiều dữ liệu.”

**Đúng (giữ claim):** “Các kết quả ban đầu gợi ý rằng mô hình có thể phù hợp với tập dữ liệu A.”

**Vì sao:** giữ tính thăm dò, phạm vi một tập dữ liệu và không thêm khả năng tổng quát hóa.

## 5. Bảng phân loại chuyển ý
- **Nguyên nhân có căn cứ:** “Do [điều kiện], [hiện tượng]” chỉ khi chứng cứ thể hiện quan hệ nhân quả.
- **Tương phản:** “Tuy nhiên, ...” nếu câu sau thật sự giới hạn hoặc đảo kỳ vọng.
- **Giới hạn:** “Kết luận này chỉ áp dụng cho ...” nếu phạm vi đó có trong nguồn.
- **Liệt kê:** “Bên cạnh đó” phù hợp khi đưa thêm thông tin độc lập và liên quan.

Không phải cứ xuất hiện “trong bối cảnh”, “bên cạnh đó” hay câu dài là lỗi. Chỉ sửa khi khái niệm hoặc lập luận được truyền đạt rõ hơn.
