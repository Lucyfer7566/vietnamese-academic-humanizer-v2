# AI Detector Literacy — Đọc báo cáo AI Detection đúng giới hạn

## Phân biệt nhiệm vụ
1. **Biên tập học thuật**: nâng rõ ràng, logic và chính xác.
2. **Phát hiện nguồn gốc văn bản**: công cụ máy học ước lượng đặc điểm của văn bản; không phải chứng cứ độc lập đáng tin để kết luận tác giả.
3. **Kiểm tra trùng lặp/đạo văn**: đánh giá trích dẫn, mức độ vay mượn và quy định trường; không đồng nghĩa với điểm AI.

Skill này chỉ làm (1) và giúp diễn giải phương pháp/hạn chế của (2), không tối ưu để né (2) hoặc khai man (3).

## Các khái niệm hay bị hiểu sai
- **Perplexity:** phụ thuộc mô hình ngôn ngữ được dùng để chấm và cách tokenization; không có “perplexity của người” phổ quát. LLM không bắt buộc luôn chọn token xác suất cao nhất; sampling và prompt ảnh hưởng phân phối. Không thể suy ra nguồn gốc văn bản bằng một metric đơn lẻ.
- **Burstiness:** cách dùng không thống nhất giữa nghiên cứu và sản phẩm; thay đổi độ dài câu không tương đương người viết và không đảm bảo phân loại.
- **DetectGPT/Fast-DetectGPT:** một họ phương pháp nghiên cứu dựa vào thuộc tính phân bố xác suất; không phải mô hình của mọi dịch vụ thương mại. Không thể suy ra tất cả detector vận hành giống nhau.
- **Classifier-based systems:** độ chính xác phụ thuộc dữ liệu huấn luyện, lĩnh vực, ngôn ngữ, phiên bản, độ dài, loại văn bản và phương pháp đánh giá.
- **False positive:** văn bản người viết bị đánh dấu AI. **False negative:** văn bản AI bị bỏ sót.

## Giới hạn có nguồn
- Turnitin nêu AI Writing Report có thể sai và **không nên là cơ sở duy nhất** cho hành động bất lợi với sinh viên. Xem `https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report`.
- Tài liệu Turnitin được đối chiếu ngày 2026-10-16 liệt kê các ngôn ngữ báo cáo hỗ trợ: Anh, Tây Ban Nha, Nhật, Ả Rập; **chưa liệt kê tiếng Việt**. Không suy rộng kết quả một báo cáo tiếng Anh cho toàn bộ luận văn tiếng Việt.
- Liang et al., *Patterns* (2023), DOI `10.1016/j.patter.2023.100779`, cảnh báo false positives trên tập tiếng Anh của người viết không phải bản ngữ. Không được nội suy định lượng cho tiếng Việt hoặc phiên bản detector khác.
- Turnitin công bố thay đổi mô hình theo thời gian, vì vậy đánh giá về độ tin cậy phải kèm ngày/phiên bản nếu có.

## Khi người dùng cung cấp AI score/report
1. Ghi rõ công cụ, ngày chấm, ngôn ngữ, độ dài, loại nội dung, phiên bản (nếu biết).
2. Kiểm tra liệu ngôn ngữ/loại văn bản nằm trong phạm vi hỗ trợ của công cụ.
3. Đọc hướng dẫn chính thức về ý nghĩa score, dấu sao, highlight và disclaimer.
4. Phân tích những câu được đánh dấu **theo tiêu chí viết** (rõ, đúng, có nguồn) chứ không “sửa cho score giảm”.
5. Nếu có false-positive concern: giữ lịch sử file, bản gốc, ghi chú nghiên cứu, tài liệu thô; trao đổi với giảng viên/hội đồng theo quy định.
6. Không tự nói đã test GPTZero/Turnitin/ZeroGPT khi không có report thật. Không tự ước lượng “% AI sau sửa”.

## Minh bạch sử dụng AI
Quy định từng cơ sở đào tạo khác nhau. Tham khảo ICMJE/COPE về trách nhiệm tác giả và khai báo hỗ trợ AI trong nghiên cứu; với luận văn tại trường, **quy định trường là nguồn cần áp dụng trực tiếp**. Biên tập viên hỗ trợ tác giả hoàn thiện và chịu trách nhiệm về nội dung, không đưa lời khuyên giấu việc dùng AI hay “fake draft history”.
