# V2.0 Build Audit & Validation

**Ngày:** 2026-10-16 | **Trạng thái:** CONDITIONAL PASS — source-based design complete; chưa có thử nghiệm người dùng với luận văn thật.

## Goal fit
Mục tiêu chính: đưa bản nháp học thuật AI hỗ trợ soạn về ngôn ngữ tự nhiên, chặt chẽ, đúng giọng người viết và bảo toàn dữ kiện. Đã xây 8-pass workflow, hard gates, source audit, ba cấp input và các file có thể chuyển nền tảng. Mục tiêu phụ “vượt detector khắc nghiệt” **không được đặt làm tiêu chí hiệu quả** do thiếu tính bảo đảm, dễ khuyến khích che giấu nguồn gốc và khác với mục tiêu trung thực học thuật. Thay bằng module đánh giá/diễn giải báo cáo và hướng dẫn lưu bản thảo để giải trình.

## Source audit
- Hai file gốc của tác giả: đọc toàn bộ; tích hợp và sửa các tiền đề quá đơn giản về perplexity, burstiness.
- `lishix520/academic-paper-skills`: xác nhận thực tế là strategist + composer, có standards/checkpoints (không phải detector).
- Đối chiếu thêm ba repo: `SyntaxSmith/humanize-paper`, `Zink-Liu/Academic-Writing-Humanizer`, `labarba/sciwrite`.
- Hướng dẫn chính thức/đọc chuyên ngành: Turnitin, Liang et al. (Patterns), Manchester Phrasebank, ICMJE và COPE.
- Đường dẫn chi tiết + mức tin cậy: `references/SOURCES.md`.

## Risk & decision log
| Rủi ro | Xử lý | Trạng thái |
|---|---|---|
| Câu khác đi nhưng claim bị mạnh lên | claim-locked + evidence ledger, mandatory review | Addressed by design; cần human review |
| Citation vẫn có nhưng hỗ trợ sai mệnh đề | claim-citation mapping | Addressed by design; cần source access |
| Lỗi do thay từ chuyên ngành | terminology registry | Addressed by design |
| Áp câu dài/ngắn theo quota detector | bỏ quota; dùng logic/readability | Resolved |
| Coi detector score là bằng chứng tác giả | detector literacy, chính sách học thuật | Resolved |
| LLM tự báo PASS không chứng cứ | gates + trạng thái NOT CHECKED | Addressed by design |
| Rò rỉ luận văn chưa công bố | xin phép trước khi gửi dịch vụ ngoài | Addressed by design |
| Chưa có corpus đánh giá tiếng Việt | ghi kết quả CONDITIONAL PASS | Open |

## Tests
`python3 -m unittest discover -s tests -v` kiểm thử thay số, thay citation, cảnh báo modality/negation, DOI giữ nguyên và trường hợp số không đổi. Script **chỉ cho cảnh báo**, không xác nhận đúng ngữ nghĩa. Xem README.

## Những gì chưa được chứng minh
- Không có đo lường AI-detector evasion hay % AI trước/sau.
- Chưa chạy study trên tập luận văn tiếng Việt của nhiều tác giả; chưa có đánh giá mù của hội đồng hay giảng viên.
- Các nguồn thứ cấp khác ngành/khác ngôn ngữ chỉ cung cấp design ideas, chưa là bằng chứng hiệu quả trong tiếng Việt.

## Acceptance conditions để lên PASS thực nghiệm
1. Tác giả cung cấp 10–20 đoạn đại diện + bản gốc và tài liệu thực chứng, được phép dùng để đánh giá.
2. Reviewer chuyên ngành so sánh blind A/B về clarity, claim integrity, style fit, citation accuracy.
3. Có số lỗi critical/major trước/sau, ghi inter-reviewer agreement khi có từ hai người chấm.
4. Tỷ lệ sai nội dung/citation bằng 0 ở tập được chấm mới nên xem xét đưa skill vào dùng thường xuyên; không tối ưu AI score.

*Không gọi CONDITIONAL PASS là chứng nhận chất lượng thực nghiệm.*
