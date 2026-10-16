# Quality Gates — Bảo đảm chất lượng biên tập

Không có chỉ số nào đo trực tiếp tính “người viết”. Bộ gate dùng **bằng chứng xem xét được** và rubric, không biến thành công cụ AI detection.

## Bốn mức severity
- **CRITICAL:** thay đổi số liệu/citation/negation/scope/causation hoặc tạo kết quả, nguồn không có thật.
- **MAJOR:** mất claim, cấu trúc lập luận sai, dùng thuật ngữ không nhất quán dẫn đến hiểu sai.
- **MODERATE:** câu khó hiểu, lặp, chuyển ý vô nghĩa, lỗi điều chỉnh giọng.
- **MINOR:** thay đổi tùy chọn về nhịp, độ cô đọng, sắc thái.

## Gates
| Gate | Kiểm tra bắt buộc | Pass condition |
|---|---|---|
| G0: Claim preservation | Ledger claim trước/sau; modality, scope, phủ định | Không có drift CRITICAL/MAJOR |
| G1: Evidence integrity | Số, citation, đơn vị, mô hình, bảng/hình | Không có mismatch chưa lý giải; mục chưa xác minh được gắn cảnh báo |
| G2: Logical coherence | Chủ thể, quan hệ nhân quả/điều kiện, các bước lập luận | Không có suy diễn ngầm vượt bằng chứng |
| G3: Academic clarity | Câu rõ, thuật ngữ ổn định, đúng chức năng phần | Đạt theo hồ sơ chuyên ngành |
| G4: Natural voice | Không lạm dụng sáo ngữ; phù hợp mẫu giọng thực | Cải thiện hữu ích, không diễn đạt giả tạo |
| G5: Accountability | Log thay đổi, các điểm cần người viết duyệt, quy định AI | Không che thiếu chứng cứ hoặc nguồn gốc |

## Rubric tùy chọn (0–4 mỗi chiều)
`meaning_preservation`, `factual_integrity`, `citation_accuracy`, `argument_flow`, `clarity`, `terminology`, `author_voice`.
0 = nghiêm trọng/không đủ thông tin; 1 = nhiều lỗi; 2 = tạm dùng nhưng có lỗi rõ; 3 = phù hợp; 4 = rất tốt và có bằng chứng đối chiếu. **Đánh giá của LLM là nhận định biên tập, không phải phép đo khách quan.**

## Quyết định
- `PASS`: tất cả hard gates an toàn; những kiểm tra đã thực hiện được có kết quả phù hợp; không có blocker.
- `CONDITIONAL PASS`: bản sửa đạt về phong cách và chưa phát hiện lỗi nội dung, nhưng còn nguồn/citation hoặc bối cảnh chưa thể xác minh; liệt kê điều kiện bắt buộc trước nộp.
- `FAIL`: có CRITICAL/MAJOR chưa sửa được, ví dụ số liệu sai, citation bịa, claim tăng sức nặng, nhầm validation và test.

Không gán PASS chỉ vì tổng điểm cao. `NOT CHECKED` phải ghi rõ, không coi là PASS.

## Red-team test (tự phản biện)
1. Có câu nào nghe hay hơn nhưng mạnh hơn chứng cứ?
2. Có từ đồng nghĩa kỹ thuật nào đổi đối tượng đo?
3. Có citation vẫn còn nhưng không hỗ trợ mệnh đề mới?
4. Có bỏ sót kết quả âm tính, điều kiện hay giới hạn?
5. Có phần nguồn chưa đọc nhưng tuyên bố “theo nghiên cứu”?
6. Nếu đọc bản mới mà không có bản gốc, người đọc có hiểu khác không?
7. Tác giả có thể giải thích tại sao các câu được viết như vậy không?

## Decision-reversal test
Giả sử ưu tiên đổi ngược từ “mượt hơn” sang “trung thực hơn”: có thay đổi nào cần hoàn tác? Nếu có, hoàn tác; ghi lý do. Nếu nỗ lực chỉnh sau hai vòng chỉ làm câu khác đi mà không rõ hơn, dừng ở phương án can thiệp tối thiểu.

## Nhật ký lỗi (đối với bài dài)
| ID | Span | Severity | Problem | Evidence | Decision | Owner |
|---|---|---|---|---|---|---|
| Q01 | P2.S1 | MODERATE | mở đầu rỗng | bản gốc | sửa câu | editor |
| Q02 | P5.S3 | CRITICAL | accuracy đổi F1 | bảng gốc | rollback | editor |

## Các số đo chỉ mang tính gợi ý
- Độ dài từ/câu/đoạn; tỷ lệ đoạn lặp biểu thức; thống kê số lần xuất hiện từ nối.
- Semantic similarity của embedding, nếu dùng, chỉ là cảnh báo vì câu phủ định hoặc đơn vị sai vẫn có thể cho điểm tương tự rất cao.
- Không áp ngưỡng perplexity/burstiness, không tối ưu phần trăm AI Detector.
