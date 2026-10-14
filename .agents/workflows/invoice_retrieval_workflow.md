# WORKFLOW SPECIFICATION: END-TO-END INVOICE RETRIEVAL & ARCHIVAL

> **Tên quy trình:** Quy trình Tự động hóa Tìm kiếm, Sắp xếp và Tải Hóa đơn Điện tử Mua vào  
> **Kiến trúc:** OIPO (Origin/Input - Ingestion - Processing - Output) kết hợp 7 Thành tố  
> **Framework:** Google Antigravity Multi-Agent Orchestration  
> **Vị trí file:** `.agents/workflows/invoice_retrieval_workflow.md`

---

## 1. SƠ ĐỒ KẾT NỐI TOÀN DIỆN 7 THÀNH TỐ (WORKFLOW ARCHITECTURE)

```mermaid
flowchart TD
    subgraph S1 [" 1. INPUT LAYER "]
        IN["📁 sample-data/danh_sach_hoa_don_thieu_sample.csv<br/>(12 bản ghi kế toán thực tế)"]
    end

    subgraph S2 [" 2. RULES & GOVERNANCE LAYER "]
        RULES["⚖️ .agents/rules/invoice_processing_rules.md<br/>• Standard Handoff Schema<br/>• Rate limiting & Không sửa file gốc"]
    end

    subgraph S3 [" 3. KNOWLEDGE BASE LAYER "]
        KB["📚 knowledge_base/<br/>• cau_hinh_nghiep_vu_hoa_don.json<br/>• quy_chuan_nghiem_thu_chung_tu.md"]
    end

    subgraph S4 [" 4. AGENTS & SKILL LAYER "]
        AG_SEARCH["🔍 Invoice Search Agent<br/>(Tiền kiểm & Đối soát Blacklist)"]
        AG_DOWNLOAD["📥 Invoice Download Agent<br/>(Skill: gdt-invoice-retriever)"]
        AG_STORAGE["📁 Invoice Storage Agent<br/>(Chuẩn hóa tên & Phân cây thư mục)"]
    end

    subgraph S5 [" 5. HUMAN-IN-THE-LOOP (HITL) "]
        HITL{"🛑 HUMAN CHECKPOINT #1<br/>Dừng duyệt khi gặp Cận biên / Rủi ro:<br/>1. MST Blacklist<br/>2. Lệch tiền > 1.000đ<br/>3. Giá trị >= 1 tỷ đồng"}
    end

    subgraph S6 [" 6. OUTPUT LAYER "]
        OUT_DIR["📁 outputs/HoaDon_LuuTru/<br/>(Cây thư mục Năm/Tháng/MST)"]
        OUT_CAT["📄 outputs/storage_catalog.json<br/>(Sổ danh mục tập trung)"]
        OUT_REP["📊 outputs/reports/bao_cao_ket_qua_workflow_end_to_end.md<br/>(Báo cáo tổng hợp đối soát)"]
    end

    %% Execution connections
    IN --> RULES --> AG_SEARCH
    KB -. Cung cấp tiêu chí & Blacklist .-> AG_SEARCH
    
    AG_SEARCH -->|"Hóa đơn Hợp lệ"| AG_DOWNLOAD
    AG_SEARCH -->|"Phát hiện Cận biên / Rủi ro"| HITL
    
    HITL -->|"Duyệt [APPROVE]"| AG_DOWNLOAD
    HITL -->|"Từ chối [REJECT]"| AG_STORAGE
    
    AG_DOWNLOAD --> AG_STORAGE
    AG_STORAGE --> OUT_DIR
    AG_STORAGE --> OUT_CAT
    AG_STORAGE --> OUT_REP
```

---

## 2. NĂM GIAI ĐOẠN VẬN HÀNH END-TO-END

### Giai đoạn 1 — Khởi tạo & Đọc dữ liệu (Input Ingestion)
- Nạp danh sách hóa đơn thiếu từ `sample-data/danh_sach_hoa_don_thieu_sample.csv` với chế độ `dtype=str` để bảo toàn số `0` ở đầu của Mã số thuế và Số hóa đơn.
- Ghi nhận tổng số bản ghi và khởi tạo phiên xử lý (Batch ID).

### Giai đoạn 2 — Áp dụng Rules & Tiền kiểm định dạng
- Áp dụng các quy tắc bắt buộc trong `.agents/rules/invoice_processing_rules.md`:
  - Kiểm tra tính đầy đủ của số hóa đơn (không được rỗng).
  - Kiểm tra độ dài chuẩn của MST: 10 chữ số (doanh nghiệp), 12 chữ số (CCCD hộ kinh doanh), 14 ký tự (chi nhánh).
  - Nếu sai phạm cấu trúc cơ bản $\rightarrow$ Gán cờ `REJECTED` ngay, không đưa vào luồng tra cứu mạng.

### Giai đoạn 3 — Phân tích Nghiệp vụ qua Agent, Skill & Knowledge Base
- Tham chiếu `knowledge_base/cau_hinh_nghiep_vu_hoa_don.json`:
  - Đối chiếu mã số thuế với `tax_risk_blacklist` (Doanh nghiệp ma, bỏ trốn).
  - Kiểm tra tính toán học: $|\text{Tổng thanh toán} - (\text{Chưa thuế} + \text{Thuế})| \le 10$đ.
  - Phân loại mẫu số: Mẫu số 1 (GTGT có mã / không mã CQT) hoặc Mẫu số 2 (Bán hàng trực tiếp).

### Giai đoạn 4 — Điểm kiểm soát con người (Human Checkpoint - HITL)
- **Điều kiện kích hoạt:**
  - Hóa đơn của đơn vị nằm trong Blacklist (ví dụ STT 6 - Cty Ma Xuất Khẩu Khống).
  - Hóa đơn lệch tiền số học (ví dụ STT 7 - Lệch 2 triệu đồng).
  - Hóa đơn cận biên có giá trị lớn $\ge 1.000.000.000$ VNĐ (ví dụ STT 12 - Vinacons 1.32 tỷ đồng).
- **Hành vi hệ thống:**
  - Tạm dừng tiến trình tự động hóa.
  - Hiển thị bảng cảnh báo chi tiết và yêu cầu Kế toán trưởng thẩm định:
    - Nếu chọn `[1] APPROVE`: Cập nhật trạng thái `APPROVED_BY_HUMAN`, bổ sung ghi chú kiểm toán, tiếp tục chuyển sang khâu tải và lưu trữ.
    - Nếu chọn `[2] REJECT`: Đánh dấu `REJECTED_HIGH_RISK`, chặn tải file, cách ly khỏi hồ sơ thuế.

### Giai đoạn 5 — Tải file, Phân loại Cây lưu trữ & Xuất Báo cáo (Output Synchronization)
- Với các hóa đơn hợp lệ và hóa đơn đã được con người duyệt:
  - Skill `gdt-invoice-retriever` tạo bản in PDF sắc nét 1:1 mô phỏng máy in ảo Chromium / Microsoft Print to PDF.
  - Tự động phân loại vào cây thư mục: `outputs/HoaDon_LuuTru/{YYYY}/{MM}/MauSo_{M}/{MST}_{TenNCC}/`.
- Đồng bộ danh mục toàn bộ 12 bản ghi vào `outputs/storage_catalog.json` theo đúng Handoff Schema.
- Soạn thảo Báo cáo đối soát hoàn chỉnh tại `outputs/reports/bao_cao_ket_qua_workflow_end_to_end.md`.
