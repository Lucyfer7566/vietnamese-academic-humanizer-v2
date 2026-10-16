# Vietnamese Academic Humanizer v2.0

**Bộ skill Markdown dành cho biên tập khóa luận, luận văn và báo cáo nghiên cứu bằng tiếng Việt.** Được tổng hợp, viết lại và mở rộng dựa trên hai tệp người dùng cung cấp (`AGENTS.md`, `SKILL(1).md`), đối chiếu với academic-paper-skills và các nguồn được liệt kê trong `references/SOURCES.md`.

**Mục tiêu:** tự nhiên hóa văn bản do AI hỗ trợ soạn *mà không đánh đổi tính chính xác*. Bộ skill **không** cung cấp cam kết vượt AI detector và không phải công cụ che giấu việc sử dụng AI. Kết quả chỉ có thể kết luận sau khi đối chiếu với tài liệu gốc và tác giả duyệt.

## Thành phần

```text
vietnamese-academic-humanizer-v2/
├── SKILL.md                   # Bộ điều phối / kích hoạt
├── AGENTS.md                  # Quy tắc cho agent trong workspace
├── README.md                  # Hướng dẫn sử dụng
├── AUDIT_AND_VALIDATION.md    # Nhật ký nghiên cứu và giới hạn kiểm thử
├── references/
│   ├── VIETNAMESE_STYLE.md    # Chẩn đoán sáo ngữ và kỹ thuật biên tập
│   ├── CLAIM_EVIDENCE.md      # Claim ledger, factual integrity, citations
│   ├── SECTION_RULES.md       # Chuẩn cho từng phần của khóa luận kỹ thuật
│   ├── RESEARCH_WORKFLOW.md   # Tích hợp strategist/composer, coherence
│   ├── VOICE_PROFILE.md       # Học phong cách thực của người viết
│   ├── QUALITY_GATES.md      # Thẩm định đa tiêu chí
│   ├── DETECTOR_LITERACY.md  # Đọc báo cáo AI Detection có trách nhiệm
│   └── SOURCES.md            # Các nguồn, giới hạn bằng chứng
├── templates/
│   ├── BRIEF.md              # Thông số cho 1 lần biên tập
│   ├── REVISION_REPORT.md    # Biểu mẫu so sánh và kiểm toán
│   └── STYLE_PROFILE.md      # Hồ sơ giọng cá nhân điền được
├── examples/
│   └── VI_REWRITE_CASES.md   # Ví dụ tổng hợp, không lấy từ bản thảo thật
├── scripts/
│   └── audit_invariants.py   # Kiểm tra token/number/citation bề mặt
└── tests/
    └── test_audit_invariants.py  # 7 bài kiểm thử script
```

## Cài đặt

**Claude Code**: chép toàn bộ thư mục vào `~/.claude/skills/vietnamese-academic-humanizer/` rồi gọi skill theo hướng dẫn nền tảng. **Codex**: đưa thư mục vào vị trí skills mà Codex hỗ trợ. **ChatGPT, Gemini hoặc LLM khác**: cung cấp `SKILL.md` + `AGENTS.md` làm hướng dẫn đầu; thêm tài liệu trong `references/` khi phù hợp (nhiều nền tảng không tự nạp mọi tệp). Skill hoạt động bằng hướng dẫn, **không tự đảm bảo agent đọc được file** nếu công cụ không hỗ trợ.

## Ví dụ gọi

```text
@Humanize rewrite
Ngữ cảnh: Chương 2, tổng quan RAG trong luận văn thạc sĩ Kỹ thuật phần mềm.
Mức sửa: standard; không đổi citation, định nghĩa, thuật ngữ và số liệu.
Hãy xuất bản sạch + 3 ghi chú biên tập + cảnh báo nếu có.
[Văn bản gốc]
```

```text
@Humanize deep
Tôi cung cấp Chương 3 và mục tiêu nghiên cứu.
Hãy xây reverse outline, chỉ ra logic đứt gãy, sửa cấu trúc nếu có lý do,
giữ nguyên tất cả chứng cứ và bảng số liệu.
```

```text
@Humanize learn-voice
Dưới đây là hai trang do chính tôi viết không sử dụng AI.
Hãy trích hồ sơ đặc điểm cú pháp, cách chuyển ý, mức độ thuật ngữ và xưng hô.
Sau đó sử dụng hồ sơ ấy để biên tập các đoạn khác, không sao chép câu gốc.
```

## Pipeline khuyến nghị
`source → source_inventory → diagnosis → rewrite → claim-audit → style-audit → author-review → revised + report`

Cách dùng kiểm tra token:

```bash
python3 scripts/audit_invariants.py draft.md revised.md
```

Mã thoát `0`: chưa phát hiện thay đổi ở các nhóm token được script giám sát; **không phải giấy chứng nhận giữ nguyên nghĩa**. Mã `1`: có mismatch hoặc cảnh báo, cần đối chiếu thủ công. `--json` xuất kết quả dễ tích hợp vào CI. Công cụ có false positives khi chuyển định dạng số hoặc bố cục bảng.

## Giới hạn
- Không tự tra cứu và xác thực DOI nếu agent không có quyền truy cập web.
- Không tự kiểm chứng ngữ nghĩa bằng thống kê độ dài câu; cần người có chuyên môn rà lại.
- Không dùng một AI detector để quyết định tính trung thực của tác giả.
- Nếu bản nháp AI chứa claim sai, skill **không thể** biến claim sai thành đúng chỉ bằng thay ngôn từ.

Bản v2.0: ngày 2026-10-16. Xem `references/SOURCES.md` để truy vết nguồn và phần được điều chỉnh từ dự án gốc.
