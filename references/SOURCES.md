# Research Sources, Provenance & Adaptation Audit

**Ngày đối chiếu:** 2026-10-16. Repo/tài liệu bên ngoài có thể thay đổi. Các đường dẫn nêu nguồn ý tưởng; bộ skill này viết lại nguyên bản bằng tiếng Việt, không tái phân phối nguyên văn mã/tài liệu bên ngoài.

## A. Nguồn trực tiếp do người dùng cung cấp
1. `AGENTS.md` (48 dòng): vai trò editor, anti-cliché, bảo toàn luận điểm, nguyên tắc `draft.md`, cadence report. **Giữ:** anti-sáo ngữ, giọng viết vừa phải, audit/rewrite. **Sửa:** mục tiêu bypass detector, số từ cứng, mặc định đại học thành cấu hình cấp học linh hoạt.
2. `SKILL(1).md` (189 dòng): 8 nhóm lỗi diễn đạt, bảng thay thế sáo ngữ, 4-pass workflow, sample output. **Giữ:** danh mục lỗi là công cụ chẩn đoán, preserving claim, mẫu báo cáo. **Sửa:** khẳng định mọi AI luôn chọn từ có xác suất lớn nhất; mọi người viết đều bursty; áp quy tắc 3 câu chênh >=5 từ; dùng ẩn dụ/câu ngắn để qua detector; “conditional probability curvature” như kỹ thuật của mọi detector. Chuyển sang đánh giá chất lượng thực chất.

## B. GitHub đã kiểm tra nội dung chính
3. **lishix520/academic-paper-skills** — `https://github.com/lishix520/academic-paper-skills` — đọc `README.md`, `strategist/SKILL.md`, `composer/SKILL.md`, tài liệu `quality_standards.md`, `section_guides.md`, `writing_standards.md`. **Ứng dụng:** phân vai planning/composition, reverse outline, đánh giá theo chương, mô phỏng phản biện, quality gates. **Giới hạn:** tập trung philosophy/interdisciplinary preprints; không phải AI-checker; tỷ lệ chương/tần suất trích dẫn trong repo không phổ quát cho thạc sĩ kỹ thuật.
4. **SyntaxSmith/humanize-paper** — `https://github.com/SyntaxSmith/humanize-paper` — đọc `humanize-paper/SKILL.md`. **Ứng dụng:** tách excerpt/manuscript/evidence-grounded, claim-locked, minimum intervention, luận điểm và bằng chứng, giữ đúng claim–evidence boundaries, reverse outline và argument graph. **Giới hạn:** repo tập trung Anh/Trung và ML; bộ này bổ sung đặc điểm tiếng Việt.
5. **Zink-Liu/Academic-Writing-Humanizer** — `https://github.com/Zink-Liu/Academic-Writing-Humanizer` — đọc `SKILL.md`. **Ứng dụng:** content ledger, preservation of scope/modality, numerical integrity, section-level editing, privacy khi chia sẻ bản chưa công bố. **Giới hạn:** tiếng Anh là trọng tâm.
6. **labarba/sciwrite** — `https://github.com/labarba/sciwrite` — đọc `SKILL.md`. **Ứng dụng:** 5-pass clarity audit (clutter, voice/verbs, sentence architecture, terminology, numbers/citations). **Giới hạn:** có khuyến nghị cho scientific English không nên áp đặt máy móc lên tiếng Việt.

## C. Hướng dẫn, khảo cứu ngoài GitHub
7. **Turnitin: Using the AI Writing Report** — `https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report` — mô tả phạm vi và disclaimer, dữ kiện ngôn ngữ hỗ trợ tại thời điểm đối chiếu.
8. **Turnitin: AI writing detection model updates** — `https://guides.turnitin.com/hc/en-us/articles/28294949544717-AI-writing-detection-model` — các thay đổi mô hình theo thời gian, cảnh báo khi so sánh score khác thời điểm.
9. **Liang et al. (2023), Patterns** — `https://doi.org/10.1016/j.patter.2023.100779` — nghiên cứu về thiên lệch nhận diện đối với một tập văn bản tiếng Anh của người không phải bản ngữ. Không thể dùng làm chứng cứ định lượng về detector tiếng Việt.
10. **University of Manchester Academic Phrasebank** — `https://www.phrasebank.manchester.ac.uk/` và `https://www.phrasebank.manchester.ac.uk/using-cautious-language/` — chức năng rhetorical moves/hedging. **Ứng dụng:** sức nặng lời khẳng định phải tương thích bằng chứng; không sao chép hệ thống mẫu câu vào bài.
11. **ICMJE — Use of AI by Authors (2026)** — `https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html` — trách nhiệm con người, công bố AI khi quy định yêu cầu; là hướng dẫn publication ethics, không tự động thay quy định trường.
12. **COPE — Authorship and AI tools** — `https://doi.org/10.24318/cCVRZBms` — AI không thể là tác giả chịu trách nhiệm, tác giả phải minh bạch.

## D. Ma trận Source → Design Decision
| Quyết định kiến trúc | Nguồn ưu tiên | Trạng thái |
|---|---|---|
| Anti-cliché tiếng Việt | 2 file người dùng, rà lại theo ngữ cảnh | Giữ có điều kiện |
| Thay quota câu dài-ngắn bằng logic câu | 2 file + sciwrite + humanize-paper | Sửa có chủ đích |
| Claim ledger + số/citation invariants | Zink-Liu, humanize-paper, sciwrite | Tích hợp và phát triển |
| Excerpt vs complete manuscript | humanize-paper | Tích hợp |
| Per-chapter gate + reviewer simulation | academic-paper-skills | Điều chỉnh cho ngành kỹ thuật |
| Nêu rõ giới hạn AI Detection | Turnitin, Liang et al. | Đưa thành module độc lập |
| Tác giả phê duyệt và disclosure | ICMJE, COPE | Đưa thành gate accountability |

## E. Confidence & giới hạn nghiên cứu
- **High**: thông tin mô tả trong tệp đã đọc và chính sách trên trang chính thức.
- **Moderate**: hiệu quả thực tế của các nguyên tắc biên tập khi chuyển ngữ Anh/Trung sang Việt, cần pilot tại đúng chuyên ngành.
- **Low/Not established**: cam kết giảm score AI Detection, tối ưu perplexity hay đạt ngưỡng qua bất kỳ detector nào. **Không đưa các cam kết này vào skill.**
- **Chưa thực hiện**: thử nghiệm định lượng trên corpus luận văn tiếng Việt có đối chứng và đánh giá mù từ giảng viên. Cần dữ liệu/thiết kế thí nghiệm riêng nếu muốn nghiên cứu.
