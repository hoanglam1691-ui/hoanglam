---
name: ai4a:ops-analyst
description: "Automate monthly ERP operations data processing, department-level file splitting, quantitative KPI aggregation, and multi-tier executive and manager reporting. Use when the user needs to process monthly operational datasets, clean ERP exports, generate department reports, or detect operational bottlenecks."
user-invocable: true
when_to_use: "Use when processing monthly operations data, analyzing employee performance by department, splitting ERP exports for department managers, or generating monthly operational review reports."
category: operations
keywords: [operations, erp, monthly-report, department-split, kpi, workflow, ai4a]
argument-hint: "[erp_data_file] [--split] [--report] [--kpi] [--month YYYY-MM]"
metadata:
  author: "MT Đức Thuận & Operations Team"
  brand: "AI4A"
  course: "Agentic AI with Google Antigravity"
  version: "1.0.0"
---

# AI4A: Operations Analyst

> **Đóng gói & phát triển bởi MT Đức Thuận & Đội ngũ AI4A**  
> *Dành tặng học viên chương trình Agentic AI with Google Antigravity (AI4A)*

Chuyên gia tự động hóa vận hành hỗ trợ chuyển đổi quy trình xử lý dữ liệu ERP hàng tháng từ thao tác bảng tính thủ công sang **Agentic Workflow 5 bước**: Tự động làm sạch dữ liệu, phân tách file riêng cho từng phòng ban, tính toán chỉ số KPI định lượng và soạn thảo báo cáo đa tầng (C-Level & Trưởng bộ phận).

---

## 1. Quy Trình Vận Hành 5 Tầng (5-Stage Operational Pipeline)

Mọi phiên xử lý dữ liệu vận hành tuân thủ quy trình chuẩn 5 bước:

```text
[Input ERP Raw Data]
        │
        ▼
[1. Ingestion & Schema Sanitizer] ──> Chuẩn hóa định dạng, khử lỗi chính tả, map cột
        │
        ▼
[2. Multi-tenant Department Splitter] ──> Cắt file riêng lưu vào outputs/departments/
        │
        ▼
[3. Quantitative KPI Engine] ──> Tính Completion %, Delay %, Volume, SLA
        │
        ▼
[4. Human Checkpoint (Analyst Review)] ──> Gắn cờ [High Risk] nếu Delay Rate > 20%
        │
        ▼
[5. Multi-Tier Report Generation] ──> Soạn Executive Summary & Manager Action Briefs
```

### Bước 1: Khởi tạo & Kiểm tra Schema (Ingestion & Sanitization)
1. Đọc file dữ liệu đầu vào trong `sample-data/` (định dạng CSV hoặc XLSX).
2. Đối chiếu các trường dữ liệu với đặc tả chuẩn trong [ERP Schema Specification](./references/erp-schema-spec.md).
3. Tự động chuẩn hóa:
   - Khoảng trắng thừa và kiểu chữ hoa/thường ở tên phòng ban.
   - Định dạng ngày tháng về dạng chuẩn `YYYY-MM-DD`.
   - Chuẩn hóa các trạng thái công việc về 4 nhóm chuẩn: `Completed`, `In Progress`, `Delayed`, `Cancelled`.

### Bước 2: Phân tách file theo từng phòng ban (Department Isolation)
1. Quét danh sách các phòng ban duy nhất (`unique departments`) trong kỳ.
2. Tự động trích xuất các bản ghi thuộc từng bộ phận và lưu thành các file riêng biệt:
   * Đường dẫn: `outputs/departments/[Ten_Bo_Phan]_[YYYY-MM].csv` (hoặc `.xlsx`).
3. **Nguyên tắc bảo mật:** Đảm bảo dữ liệu được cô lập hoàn toàn, tránh việc dữ liệu nhân sự của bộ phận này bị gửi nhầm cho bộ phận khác.

### Bước 3: Tính toán chỉ số KPI định lượng (KPI Engine)
Áp dụng các công thức chuẩn từ tài liệu [KPI Definitions Reference](./references/kpi-definitions.md):
- **Tổng sản lượng / Doanh số thực tế:** $\sum \text{Output\_Units}$ hoặc $\sum \text{Revenue}$.
- **Tỷ lệ hoàn thành đúng hạn (Completion Rate %):** $\frac{\text{Completed Tasks}}{\text{Total Tasks}} \times 100\%$.
- **Tỷ lệ trễ hạn (Delay Rate %):** $\frac{\text{Delayed Tasks}}{\text{Total Tasks}} \times 100\%$.
- **Năng suất bình quân nhân sự:** $\frac{\text{Total Output}}{\text{Active Employees}}$.

### Bước 4: Human Checkpoint (Điểm kiểm soát con người)
Trước khi phát hành báo cáo, hệ thống tự động gắn cờ rà soát:
- **Cờ đỏ `[Critical Alert]`:** Nếu bất kỳ phòng ban nào có $\text{Delay Rate} > 20\%$ hoặc sản lượng sụt giảm trên $25\%$ so với kỳ trước.
- **Cờ vàng `[Outlier Alert]`:** Nếu phát hiện các nhân sự có số lượng công việc bất thường (quá tải gấp 2 lần mức bình quân hoặc hoàn toàn không phát sinh sản lượng).
- Người phân tích vận hành (Analyst) xác nhận nguyên nhân sơ bộ trước khi xuất báo cáo gửi BOD.

### Bước 5: Soạn thảo báo cáo đa tầng (Multi-tier Reporting)
Sử dụng các mẫu báo cáo chuẩn hóa để sinh văn bản đầu ra:
1. **Báo cáo cấp cao (Executive Overview):**
   - Lưu tại: `outputs/reports/company_operations_summary_[YYYY-MM].md`
   - Dùng mẫu tại: [Executive Overview Template](./resources/executive-overview-template.md)
   - Mục đích: Trình bày bức tranh tổng thể toàn công ty, bảng điểm so sánh giữa các phòng ban, và 3 kiến nghị chiến lược cho Ban Giám đốc (COO / CEO).
2. **Bản tin hành động cho Quản lý (Manager Action Brief):**
   - Lưu tại: `outputs/reports/manager_brief_[Ten_Bo_Phan]_[YYYY-MM].md`
   - Dùng mẫu tại: [Manager Brief Template](./resources/manager-brief-template.md)
   - Mục đích: Báo cáo cô đọng gồm bảng chỉ số nội bộ, danh sách nhân viên xuất sắc, các ca trễ hạn cần tháo gỡ, và 3 hành động cụ thể cho tuần đầu tháng tới.

---

## 2. Các Lệnh Thực Thi & Tham Số (Execution Flags)

Khi kích hoạt skill, người dùng có thể truyền kèm các cờ để điều chỉnh phạm vi công việc:

- **Mặc định:** Chạy toàn bộ chu trình 5 bước (Clean -> Split -> KPI -> Executive Report & Manager Briefs).
- **Cờ `--split`:** Chỉ thực hiện làm sạch dữ liệu và cắt file cho các phòng ban vào `outputs/departments/`.
- **Cờ `--kpi`:** Chỉ tính toán bảng tổng hợp số liệu định lượng mà không sinh văn bản phân tích chi tiết.
- **Cờ `--report`:** Sinh các báo cáo phân tích định tính từ bảng số liệu tổng hợp đã có.
- **Cờ `--month YYYY-MM`:** Chỉ định rõ kỳ tháng cần lọc và phân tích (mặc định lấy tháng gần nhất trong file dữ liệu).

---

## 3. Tài Liệu Tham Chiếu & Mẫu Báo Cáo (Progressive Disclosure)

- 📋 [ERP Schema Specification](./references/erp-schema-spec.md): Quy chuẩn trường dữ liệu và ánh xạ cột.
- 📐 [KPI Definitions Reference](./references/kpi-definitions.md): Công thức tính toán và ngưỡng cảnh báo vận hành.
- 📑 [Executive Overview Template](./resources/executive-overview-template.md): Mẫu báo cáo cấp công ty cho Ban Giám đốc.
- 📝 [Manager Action Brief Template](./resources/manager-brief-template.md): Mẫu báo cáo hành động cho từng Trưởng bộ phận.

---

## 4. Quy Tắc Ràng Buộc & Bảo Mật (Guardrails)

- **Bảo mật dữ liệu (Quy tắc 5 Workspace):** Không gửi dữ liệu khách hàng hoặc nhân sự nhạy cảm ra ngoài prompt nếu không cần thiết. Chỉ truyền các chỉ số tổng hợp (Aggregated Metrics) sang bước sinh văn bản.
- **Đúng thư mục (Quy tắc 4 Workspace):**
  - File dữ liệu cắt: `outputs/departments/`
  - Báo cáo phân tích: `outputs/reports/`
- **Không tự suy diễn lỗi cá nhân:** Khi tỷ lệ trễ hạn cao, AI phải chỉ ra các yếu tố khách quan (khối lượng task tăng đột biến, phụ thuộc chéo phòng ban) trước khi đề xuất giải pháp đào tạo/nhắc nhở.
