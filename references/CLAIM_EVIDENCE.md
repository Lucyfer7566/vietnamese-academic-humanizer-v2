# Claim, Evidence, Citation & Invariant Protocol

## 1. Claim ledger
Trước rewrite, trích các claim cần khóa. Mỗi claim có ID, scope, modality, bằng chứng, citation và vị trí. Bảng nội bộ:

| ID | Claim nguyên bản | Scope / điều kiện | Modality | Evidence/citation | Action |
|---|---|---|---|---|---|
| C01 | `[mệnh đề]` | `[dataset/nhóm/thời gian]` | `observed|suggests|may|proposed` | `[Bảng 2.1]/[7]` | `lock|flag` |

## 2. Các bất biến tuyệt đối
- Số, đơn vị, dấu, độ chính xác thập phân: 0,85 ≠ 0,8, 5% ≠ 5 điểm phần trăm, 10 ms ≠ 10 s.
- So sánh: tốt hơn so với **baseline nào**, theo **metric nào**, trên **tập nào**.
- Trạng thái kết quả: “dự kiến”, “thiết kế nhằm”, “đã thử nghiệm”, “quan sát được”, “chứng minh”, “không có ý nghĩa thống kê” là các trạng thái khác nhau.
- Tương quan không suy ra nhân quả; association/correlation khác causal effect.
- Không có khác biệt có ý nghĩa thống kê không đồng nghĩa tương đương thực nghiệm.
- Kết quả trên validation không được gọi là kết quả test độc lập.
- Citation markers (ví dụ `[12]`, `Nguyễn và cs. (2023)`, `\cite{key}`), DOI, bảng/hình, phương trình phải gắn đúng claim như bản gốc.
- Định nghĩa thuật ngữ khoa học giữ nhất quán; không đổi tên dữ liệu, phiên bản, tệp mô hình.
- Không loại bỏ negative/null results, ngoại lệ hay hạn chế quan trọng để văn bản mượt hơn.

## 3. Phân quyền thay đổi mức độ khẳng định
**claim-locked:** chỉ sửa ngôn ngữ. “có thể cải thiện” không thành “cải thiện”; “có liên hệ” không thành “là nguyên nhân”. **evidence-calibrated:** chỉ khi người dùng cung cấp bảng nguồn độc lập và yêu cầu cập nhật claim, phải ghi dòng minh chứng rõ: `source claim → revised claim → evidence path/line → author approval needed`.

## 4. Evidence verification
- Với bài báo khoa học: tìm DOI/canonical paper, đọc ít nhất abstract/methods/results liên quan; giữ citation đúng tác giả, năm, claim.
- Nếu chỉ có tên tài liệu tham khảo mà không có bài gốc: không khẳng định đã kiểm chứng nội dung.
- Tài liệu code, README và benchmark: phân biệt tính năng được mô tả và kết quả được thực nghiệm.
- Nếu không có internet hoặc dữ liệu: cảnh báo `NOT VERIFIED`, không tự tạo nguồn.

## 5. Bảng audit sau biên tập
| Hạng mục | Check | Nếu lỗi |
|---|---|---|
| Claim coverage | Mọi Cxx còn trong revised? | FAIL nếu mất claim cốt lõi |
| Claim additions | Có phát biểu thực chất mới? | FAIL nếu vô căn cứ |
| Scope/modality/negation | Không chuyển đổi? | FAIL nếu sai |
| Numbers/formulas/units | Giữ đúng? | FAIL nếu thay |
| Citation mapping | Citation đi theo đúng claim? | CONDITIONAL/FAIL |
| Terms | Một khái niệm một thuật ngữ? | CONDITIONAL |
| Proof status | Có phân biệt đã đo và mới đề xuất? | FAIL nếu đảo trạng thái |

## 6. Kiểm tra tự động và giới hạn
`scripts/audit_invariants.py` chỉ kiểm tra các token có thể tách bằng biểu thức chính quy: số (bao gồm định dạng thường gặp), citation ngoặc vuông, `\cite{...}`, DOI, một số chuỗi phương trình/LaTeX. Thay đổi thứ tự đoạn hoặc định dạng có thể tạo cảnh báo giả. Một PASS từ script không thay được phép đối chiếu ngữ nghĩa claim-by-claim.

## 7. Mẫu change log
| Span nguồn | Sửa thành | Loại sửa | Bằng chứng | Trạng thái |
|---|---|---|---|---|
| P2.S3 | P2.S2 | tách câu, giữ nghĩa | chính câu gốc | OK |
| P4.S1 | đề xuất diễn đạt mới | điều chỉnh claim | chưa có | HOLD — tác giả duyệt |
