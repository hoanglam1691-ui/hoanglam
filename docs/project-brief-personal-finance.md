# Project Brief: Workspace Phân Tích Tài Chính Cá Nhân

> **Định dạng:** SCOPE Framework (Capstone & Project Brief)  
> **Framework:** AI4A Brainstorm Contract (`ai4a:brainstorm --scope`)  
> **Tác giả:** Học viên Agentic AI  
> **Người hướng dẫn:** MT Đức Thuận  
> **Ngày khởi tạo:** 2026-09-09  

---

## 1. Situation (S) — Bối Cảnh Vận Hành

- **Hiện trạng:** Người dùng theo dõi thu chi, tiết kiệm và danh mục tài chính từ nhiều nguồn phân tán: file sao kê ngân hàng (Vietcombank, Techcombank, MB...), lịch sử ví điện tử (MoMo, ZaloPay), và các ghi chép chi tiêu tiền mặt.
- **Điểm nghẽn (Baseline Friction):**
  - Mất từ 2-4 giờ mỗi cuối tháng để sao chép, đối soát thủ công trên bảng tính Excel.
  - Phân loại giao dịch dễ nhầm lẫn (ví dụ: giao dịch GrabCar di chuyển vs GrabFood ăn uống).
  - Thiếu góc nhìn tổng thể theo các quy chuẩn quản lý tài chính chuẩn (như quy tắc 50/30/20 hoặc 6 chiếc lọ).
  - Không phát hiện kịp thời các khoản chi lặp lại ngầm (subscription không dùng, phí tài khoản, các giao dịch vi mô tích lũy lớn).

---

## 2. Constraints (C) — Ràng Buộc & Điểm Kiểm Soát

- **Quy tắc bảo mật PII (Tuân thủ Quy tắc 5 Workspace):**
  - Tuyệt đối không đưa số thẻ, số tài khoản đầy đủ, mã OTP/CVV hoặc thông tin danh tính cá nhân nhạy cảm lên mô hình LLM.
  - Phải có bước ẩn danh (data masking): Ví dụ tài khoản `1903...8888` chuyển thành `****8888`, tên người nhận/chuyển được mã hóa thành mã định danh hoặc phân nhóm.
- **Thời gian xử lý & Tài nguyên:**
  - Chạy xử lý hoàn toàn trong môi trường local của workspace.
  - Thời gian sinh báo cáo dưới 30 giây cho tập dữ liệu 500 giao dịch.
- **Human Checkpoint (Điểm kiểm soát con người):**
  - Mọi giao dịch bị phân loại không chắc chắn (confidence score < 80%) phải được gắn cờ `[Needs Review]` để người dùng xác nhận thủ công.
  - Hệ thống chỉ đóng vai trò phân tích và khuyến nghị quản lý ngân sách, **không** tự động thực hiện các thao tác chuyển tiền hoặc can thiệp tài khoản.

---

## 3. Objective (O) — Mục Tiêu Định Lượng & Output

- **Mục tiêu cốt lõi:** Tự động hóa toàn bộ chu trình từ nhập dữ liệu giao dịch thô đến lập báo cáo sức khỏe tài chính cá nhân định kỳ hàng tháng.
- **Chỉ số thành công (Success Metrics):**
  - Giảm thời gian tổng hợp tài chính cuối tháng từ 3 giờ xuống dưới 3 phút.
  - Độ chính xác phân loại giao dịch tự động đạt tối thiểu 90%.
  - 100% các khoản chi vượt ngân sách danh mục được cảnh báo rõ ràng.
- **Output Artifacts mong đợi:**
  - `sample-data/personal-transactions.csv`: Dữ liệu sao kê mẫu chuẩn hóa.
  - `outputs/reports/categorized-transactions.csv`: Dữ liệu giao dịch đã được phân loại theo danh mục và quy tắc 50/30/20.
  - `outputs/reports/financial-health-report-YYYY-MM.md`: Báo cáo đánh giá sức khỏe tài chính chi tiết (dòng tiền ròng, tỷ lệ tiết kiệm, các khoản chi bất thường và khuyến nghị tháng tiếp theo).

---

## 4. Proposal (P / OIPO) — Kiến Trúc Quy Trình

### 4.1 So sánh các phương án kỹ thuật (Trade-off Comparison)

| Tiêu chí | Phương án 1: Lean / Script Direct | Phương án 2: Agentic Workflow (Khuyến nghị) | Phương án 3: Advanced RAG + App |
| :--- | :--- | :--- | :--- |
| **Kiến trúc** | Script Python dùng Regex + 1 prompt tổng kết | Pipeline OIPO 3 bước + Human Checkpoint | Vector Database lưu lịch sử + Full-stack Dashboard |
| **Độ phức tạp** | Rất thấp (1 buổi) | Vừa phải (phù hợp khung 11 buổi học) | Rất cao (vượt phạm vi capstone cá nhân) |
| **Khả năng kiểm soát** | Kém linh hoạt với mô tả giao dịch mới | Cao, tách bạch rõ ràng từng vai trò agent | Khó kiểm soát khi mở rộng quy mô |
| **Điểm lỗi đầu tiên** | Lỗi phân loại khi mô tả chuyển khoản viết tắt lạ | Handoff dữ liệu giữa bước làm sạch và bước phân tích | Chi phí token và độ trễ kết nối cơ sở dữ liệu |
| **Đánh giá** | Tạm dùng cho MVP | **Tối ưu nhất cho Capstone và Workspace cá nhân** | Để dành mở rộng sau khóa học |

### 4.2 Thiết kế kiến trúc OIPO đề xuất (Phương án 2)

```text
[Input] sample-data/personal-transactions.csv
   │
   ▼
[Process 1: Ingestion & Sanitizer]
   ├── Chuẩn hóa định dạng ngày tháng, số tiền (VND)
   └── Masking PII (Số tài khoản, tên riêng nhạy cảm)
   │
   ▼
[Process 2: Categorization & Rules Engine]
   ├── Phân loại danh mục (Ăn uống, Nhà ở, Hóa đơn, Mua sắm, Đầu tư...)
   └── Áp khung 50% Thiết yếu / 30% Linh hoạt / 20% Tiết kiệm & Tích lũy
   │
   ├── [Human Checkpoint]: Xác nhận các giao dịch cờ vàng [Needs Review]
   │
   ▼
[Process 3: Financial Health Advisor Agent]
   ├── Tính toán Cashflow ròng (Thu - Chi)
   ├── Phân tích các khoản chi đột biến / lặp lại
   └── Đề xuất kế hoạch ngân sách cho chu kỳ tiếp theo
   │
   ▼
[Output] outputs/reports/financial-health-report-YYYY-MM.md
         outputs/reports/categorized-transactions.csv
```

---

## 5. Evaluation (E) — Nghiệm Thu & Bộ Dữ Liệu Kiểm Thử

- **Bộ dữ liệu kiểm thử (Demo Data):**
  - Tạo file `sample-data/personal-transactions.csv` với tối thiểu 60-100 giao dịch đại diện cho 1 tháng chi tiêu thực tế (bao gồm lương, thưởng, tiền nhà, ăn uống, chuyển khoản lẻ, tiền điện nước, mua sắm Tiki/Shopee).
- **Tiêu chuẩn nghiệm thu (Acceptance Criteria):**
  - [ ] **Làm sạch:** 100% giao dịch có số tiền âm (chi) và dương (thu) được chuyển đổi chuẩn xác.
  - [ ] **Bảo mật:** Không còn chuỗi số tài khoản đầy đủ nào xuất hiện trong các output tại `outputs/`.
  - [ ] **Cân đối ngân sách:** Báo cáo phản ánh đúng tỷ lệ % chi tiêu so với chuẩn 50/30/20.
  - [ ] **Cảnh báo:** Tự động phát hiện ít nhất 1 khoản chi bất thường hoặc vượt hạn mức ngân sách đặt ra.
  - [ ] **Khả năng tái lập:** Chạy lại toàn bộ quy trình với tập dữ liệu mới chỉ bằng một câu lệnh hoặc một prompt.

---

## 6. Out of Scope (Non-goals) — Ngoài Phạm Vi

Để đảm bảo dự án khả thi và hoàn thành đúng tiến độ trong khóa học, dự án **sẽ không** thực hiện:
- Không tích hợp Open Banking API hoặc cào dữ liệu đăng nhập trực tiếp từ tài khoản ngân hàng (tránh rủi ro bảo mật 2FA và chính sách ngân hàng).
- Không cung cấp lời khuyên đầu tư cổ phiếu/chứng khoán/crypto mang tính chất cam kết lợi nhuận pháp lý.
- Không xây dựng ứng dụng di động (Mobile App) riêng biệt trong giai đoạn này.
