# Project Brief: Công Cụ Phân Tích Doanh Thu & Chi Phí Hàng Tháng

> **Định dạng:** SCOPE Framework (Capstone & Project Brief)  
> **Framework:** AI4A Brainstorm Contract (`ai4a:brainstorm --scope`)  
> **Tác giả:** Học viên Agentic AI  
> **Người hướng dẫn:** MT Đức Thuận  
> **Ngày khởi tạo:** 2026-09-09  

---

## 1. Situation (S) — Bối Cảnh Vận Hành

- **Hiện trạng:** Doanh nghiệp, phòng ban hoặc chủ kinh doanh theo dõi hoạt động bán hàng định kỳ qua các bảng tính Excel/CSV (ví dụ file `sample-data/Sales_Performance_Dashboard_Cleaned.xlsx` hoặc `sample-data/MINDX_Lesson 2_DEMO_synthetic_sales_data_500x20.xlsx`).
- **Cấu trúc bảng dữ liệu điển hình:** Mã đơn, Ngày giao dịch, Kênh bán (Online/Showroom/Đại lý), Ngành hàng/Sản phẩm, Đơn giá, Số lượng, Doanh thu (Revenue), Giá vốn (COGS), Chi phí vận chuyển/chiết khấu/Marketing, Nhân viên bán hàng.
- **Điểm nghẽn (Baseline Friction):**
  - Mất 3–5 giờ mỗi cuối tháng để đối soát, lọc tháng, lập bảng Pivot Table và tính toán các chỉ số: Doanh thu thuần, Tổng chi phí, Lợi nhuận gộp (Gross Profit), Tỷ suất lợi nhuận (Margin %).
  - Khó nhận diện kịp thời các sản phẩm hoặc kênh bán "ăn mòn lợi nhuận" (doanh thu cao nhưng biên lợi nhuận mỏng do chi phí ẩn/chiết khấu lớn).
  - Thiếu báo cáo phân tích định tính (Insights & Actionable Takeaways) tự động để gửi ngay cho ban quản lý đưa ra quyết định kinh doanh.

---

## 2. Constraints (C) — Ràng Buộc & Điểm Kiểm Soát

- **Ràng buộc định dạng dữ liệu (Data Robustness):**
  - Chấp nhận đầu vào là bảng dữ liệu CSV hoặc Excel trong thư mục `sample-data/`.
  - Phải xử lý được các vấn đề thường gặp: dòng trống, dữ liệu khuyết thiếu (NaN), format số tiền có dấu phân cách nghìn (`.` hoặc `,`).
- **Quy tắc bảo mật (Quy tắc 5 Workspace):**
  - Không gửi thông tin định danh cá nhân nhạy cảm của khách hàng (SĐT, địa chỉ chi tiết, số CCCD) ra ngoài mô hình ngôn ngữ lớn. Chỉ gửi các trường aggregated (tổng hợp) hoặc dữ liệu đã khử PII.
- **Human Checkpoint (Kiểm soát phê duyệt):**
  - Bất kỳ đơn hàng hoặc nhóm sản phẩm có **Biên lợi nhuận gộp âm (Gross Margin < 0)** hoặc chi phí tăng vọt đột biến (> 2 lần mức bình quân) phải được gắn cờ `[Cảnh báo: Margin Alert]` để người quản lý kiểm tra đối soát, không tự động quy kết lỗi vận hành.
  - Các đề xuất cắt giảm chi phí hay dừng kinh doanh sản phẩm chỉ mang tính tham mưu; quyết định thuộc về nhà quản lý.

---

## 3. Objective (O) — Mục Tiêu Định Lượng & Output

- **Mục tiêu cốt lõi:** Xây dựng quy trình tự động hóa phân tích toàn diện Doanh thu và Chi phí trong 1 tháng từ bảng dữ liệu thô, sinh báo cáo P&L thu nhỏ và khuyến nghị tối ưu biên lợi nhuận trong dưới 60 giây.
- **Chỉ số thành công (Success Metrics):**
  - Giảm thời gian tổng hợp và phân tích báo cáo tháng từ 3–5 giờ xuống dưới 1 phút.
  - 100% số liệu tổng hợp (Doanh thu, Chi phí, Lợi nhuận gộp) khớp chính xác tuyệt đối với kết quả tính toán số học chuẩn (Excel Ground Truth).
  - Tự động phát hiện Top 3 sản phẩm sinh lời cao nhất và Top 3 "hố đen" chi phí trong tháng.
- **Output Artifacts (Theo Quy tắc 4 Workspace):**
  - `outputs/reports/monthly-pnl-summary-YYYY-MM.csv`: Bảng tổng hợp số liệu P&L theo danh mục/kênh bán.
  - `outputs/reports/monthly-revenue-cost-report-YYYY-MM.md`: Báo cáo phân tích chuyên sâu gồm:
    1. *Executive Summary:* Tóm tắt sức khỏe doanh thu & lợi nhuận tháng.
    2. *P&L Breakdown:* Bảng phân tích cơ cấu chi phí so với doanh thu.
    3. *Category & Channel Performance:* Đánh giá hiệu quả từng kênh/ngành hàng.
    4. *Anomaly & Margin Leaks:* Cảnh báo các khoản chi phí bất thường hoặc đơn hàng lỗ.
    5. *Action Plan:* Đề xuất 3 hành động cụ thể để cải thiện biên lợi nhuận tháng sau.

---

## 4. Proposal (P / OIPO) — Kiến Trúc Quy Trình

### 4.1 So sánh các phương án (Trade-off Matrix)

| Tiêu chí | Phương án 1: Direct LLM Prompt | Phương án 2: OIPO Workflow (Khuyến nghị) | Phương án 3: Enterprise BI System |
| :--- | :--- | :--- | :--- |
| **Kiến trúc** | Đọc file Excel rồi nạp toàn bộ vào 1 prompt LLM | Bộ xử lý số học Deterministic + Agent phân tích Insight | Xây database SQL + Kết nối PowerBI / Tableau Live |
| **Độ chính xác tính toán** | Dễ gặp ảo giác (hallucination) khi tính cộng dồn hàng nghìn dòng | **Chính xác 100% (script làm toán, LLM bình luận insight)** | Chính xác 100% |
| **Thời gian & Chi phí** | Dễ tràn Token Context, chi phí cao | Rất nhẹ token, tốc độ < 30 giây, chi phí cực thấp | Tốn kém cài đặt máy chủ và bản quyền phần mềm |
| **Điểm lỗi đầu tiên** | Tính sai tổng tiền khi file vượt quá 500 dòng | File Excel bị đổi tên cột gốc không báo trước | Lỗi kết nối ODBC / Database pipeline |
| **Đánh giá** | Kém tin cậy cho tài chính | **Lựa chọn tối ưu nhất cho Capstone và vận hành thực tế** | Quá cồng kềnh cho phạm vi phân tích định kỳ |

### 4.2 Thiết kế kiến trúc OIPO đề xuất (Phương án 2)

```text
[Input: sample-data/*.xlsx hoặc *.csv]
   │
   ▼
[Bước 1: Data Aggregator & P&L Engine (Deterministic)]
   ├── Làm sạch dữ liệu, xử lý dòng rỗng, chuẩn hóa định dạng số
   ├── Lọc theo kỳ tháng được chọn (YYYY-MM)
   ├── Tính toán số học: Doanh thu, Giá vốn (COGS), Chi phí vận hành, Gross Profit, Margin %
   └── Xuất bảng số liệu tổng hợp sạch (Aggregated Table)
   │
   ▼
[Bước 2: Margin & Anomaly Detector]
   ├── So sánh tỷ suất lợi nhuận giữa các kênh bán (Online vs Showroom vs B2B)
   ├── Phát hiện sản phẩm có chi phí chiết khấu/vận chuyển vượt ngưỡng
   └── [Human Checkpoint]: Gắn cờ [Margin Alert] các đơn hàng có Gross Margin < 0
   │
   ▼
[Bước 3: Financial Insight & Action Agent]
   ├── Đọc bảng số liệu tổng hợp (nhẹ token, bảo mật số liệu chi tiết PII)
   ├── Phân tích nguyên nhân đằng sau các biến động chi phí
   └── Đề xuất 3 giải pháp cải thiện biên lợi nhuận tháng tới
   │
   ▼
[Output] outputs/reports/monthly-revenue-cost-report-YYYY-MM.md
         outputs/reports/monthly-pnl-summary-YYYY-MM.csv
```

---

## 5. Evaluation (E) — Nghiệm Thu & Dữ Liệu Kiểm Thử

- **Bộ dữ liệu kiểm thử (Demo Data):**
  - Sử dụng ngay dữ liệu có sẵn tại `sample-data/Sales_Performance_Dashboard_Cleaned.xlsx` hoặc `sample-data/MINDX_Lesson 2_DEMO_synthetic_sales_data_500x20.xlsx`.
- **Tiêu chuẩn nghiệm thu (Acceptance Criteria):**
  - [ ] **Tính chính xác:** Doanh thu thuần = Doanh thu gộp - Chiết khấu/Giảm giá; Lợi nhuận gộp = Doanh thu thuần - Chi phí giá vốn; Margin % tính đúng công thức.
  - [ ] **Lọc kỳ chuẩn:** Chỉ phân tích đúng các giao dịch phát sinh trong tháng mục tiêu.
  - [ ] **Cảnh báo hữu ích:** Chỉ ra cụ thể tên ít nhất 1 dòng sản phẩm hoặc kênh bán đang chịu chi phí cao bất thường kèm tỷ lệ %.
  - [ ] **Định dạng chuẩn:** File báo cáo Markdown và bảng CSV sinh ra chuẩn cú pháp, hiển thị trực quan, lưu đúng thư mục `outputs/reports/`.

---

## 6. Out of Scope (Non-goals) — Ngoài Phạm Vi

Để đảm bảo dự án tinh gọn, hiệu quả và hoàn thành đúng hạn:
- Không tích hợp API thời gian thực (Real-time webhook) từ phần mềm kế toán (MISA, FAST, SAP); công cụ tập trung vào phân tích file export định kỳ.
- Không huấn luyện mô hình Machine Learning dự báo xu hướng 3-5 năm; tập trung vào phân tích kỳ tháng hiện tại so với kế hoạch hoặc tháng liền kề.
- Không tự động gửi email phát hành hóa đơn hay điều chỉnh giá bán trên hệ thống bán hàng.
