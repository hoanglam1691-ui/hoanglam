# THIẾT KẾ KIẾN TRÚC HỆ THỐNG AGENTIC WORKSPACE (7 THÀNH TỐ & 3 TẦNG)

---

## 1. SƠ ĐỒ KIẾN TRÚC TỔNG THỂ (MERMAID)

```mermaid
flowchart TD
    %% ==========================================
    %% GLOBAL GOVERNANCE & KNOWLEDGE BASE
    %% ==========================================
    subgraph FOUNDATION [" TẦNG TRI THỨC & NGUYÊN TẮC (Foundation Layer) "]
        KB[("📚 KNOWLEDGE BASE (KB)<br/>• Danh bạ Nhà cung cấp & Mã số thuế<br/>• Tiêu chuẩn cấu trúc thẻ XML HĐĐT<br/>• Quy chuẩn đặt tên file & Thư mục kế toán<br/>• Danh sách Doanh nghiệp rủi ro cao về Thuế")]
        RULES{{"⚖️ WORKSPACE RULES<br/>• Bảo mật Credential/Token GDT qua .env<br/>• Bắt buộc tải đủ trọn bộ file XML gốc & PDF<br/>• Chống trùng lặp (Anti-duplication Hash)<br/>• Tuân thủ Nghị định 123/2020 & TT 78/2021"}}
    end

    %% ==========================================
    %% TIER 1: STRATEGIC & GOVERNANCE
    %% ==========================================
    subgraph TIER_1 [" TẦNG 1: CẤP ĐIỀU PHỐI (Governance & Strategy Layer) "]
        DIR_AGENT["👔 INVOICE DIRECTOR AGENT<br/>• Giám sát tổng chi phí & nghĩa vụ thuế GTGT<br/>• Phê duyệt ngoại lệ & rủi ro hóa đơn bất thường<br/>• Định hướng chiến lược kiểm soát tài chính"]
        SKILL_DIR["⚡ Skill: tax-compliance-audit"]
        DIR_AGENT --- SKILL_DIR
    end

    %% ==========================================
    %% TIER 2: MANAGEMENT & ORCHESTRATION
    %% ==========================================
    subgraph TIER_2 [" TẦNG 2: CẤP QUẢN LÝ (Management Layer) "]
        MGR_AGENT["📋 INVOICE MANAGER AGENT<br/>• Thiết lập kỳ tra cứu (Từ ngày - Đến ngày)<br/>• Điều phối luồng làm việc & Phân bổ tác vụ<br/>• Giám sát SLA và xử lý retry khi nghẽn mạng"]
        SKILL_MGR["⚡ Skill: invoice-pipeline-orchestrator"]
        MGR_AGENT --- SKILL_MGR
    end

    %% ==========================================
    %% HUMAN CHECKPOINTS (HITL)
    %% ==========================================
    subgraph HITL [" 👤 HUMAN CHECKPOINTS (Điểm Kiểm Soát Con Người) "]
        HC_1["🛑 Human Checkpoint 1:<br/>Kế toán duyệt hóa đơn bất thường (Nhà cung cấp rủi ro / Chữ ký số lỗi)"]
        HC_2["🛑 Human Checkpoint 2:<br/>Kế toán trưởng phê duyệt Bảng kê mua vào trước khi nộp tờ khai Thuế"]
    end

    %% ==========================================
    %% TIER 3: EXECUTION & SPECIALISTS
    %% ==========================================
    subgraph TIER_3 [" TẦNG 3: CẤP THỰC THI (Specialist Agents Layer) "]
        
        subgraph AG_SEARCH [" 1. Invoice Search Agent "]
            SEARCH_AGENT["🔍 INVOICE SEARCH AGENT<br/>Đăng nhập, giải Captcha & quét danh sách HĐ"]
            SKILL_SEARCH["⚡ Skill: gdt-crawler-session"]
            SEARCH_AGENT --- SKILL_SEARCH
        end

        subgraph AG_VERIFY [" 2. Invoice Verification Agent "]
            VERIFY_AGENT["🛡️ INVOICE VERIFICATION AGENT<br/>Kiểm tra trạng thái & xác thực chữ ký số XML"]
            SKILL_VERIFY["⚡ Skill: xml-signature-validator"]
            VERIFY_AGENT --- SKILL_VERIFY
        end

        subgraph AG_DOWNLOAD [" 3. Invoice Download Agent "]
            DOWNLOAD_AGENT["📥 INVOICE DOWNLOAD AGENT<br/>Tải song song trọn bộ file XML và PDF"]
            SKILL_DOWNLOAD["⚡ Skill: async-bulk-downloader"]
            DOWNLOAD_AGENT --- SKILL_DOWNLOAD
        end

        subgraph AG_STORAGE [" 4. Invoice Storage Agent "]
            STORAGE_AGENT["📁 INVOICE STORAGE AGENT<br/>Chuẩn hóa tên file & phân loại thư mục"]
            SKILL_STORAGE["⚡ Skill: smart-renamer-filer"]
            STORAGE_AGENT --- SKILL_STORAGE
        end

        subgraph AG_REPORT [" 5. Invoice Report Agent "]
            REPORT_AGENT["📊 INVOICE REPORT AGENT<br/>Tổng hợp Bảng kê Excel & Báo cáo điều hành"]
            SKILL_REPORT["⚡ Skill: excel-tax-reporter"]
            REPORT_AGENT --- SKILL_REPORT
        end

    end

    %% ==========================================
    %% WORKFLOW & HANDOFF CONNECTIONS
    %% ==========================================
    KB -. Cung cấp danh bạ/mẫu XML .-> TIER_3
    RULES -. Kiểm soát chính sách .-> TIER_1
    RULES -. Ràng buộc quy trình .-> TIER_2
    RULES -. Ràng buộc kỹ thuật .-> TIER_3

    DIR_AGENT ==>|"Chỉ đạo kỳ xử lý & Ngân sách"| MGR_AGENT

    %% Handoff Flow giữa các Agent thực thi
    MGR_AGENT -->|"🤝 Handoff 1: Tham số kỳ tra cứu"| SEARCH_AGENT
    SEARCH_AGENT -->|"🤝 Handoff 2: Metadata danh sách HĐĐT"| VERIFY_AGENT
    
    VERIFY_AGENT -->|"Hóa đơn hợp lệ"| DOWNLOAD_AGENT
    VERIFY_AGENT -.->|"⚠️ Cảnh báo HĐ rủi ro"| HC_1
    HC_1 -->|"Xác nhận cho phép xử lý"| DOWNLOAD_AGENT

    DOWNLOAD_AGENT -->|"🤝 Handoff 3: Raw XML & PDF files"| STORAGE_AGENT
    STORAGE_AGENT -->|"🤝 Handoff 4: File paths & Clean Data"| REPORT_AGENT
    
    REPORT_AGENT -->|"🤝 Handoff 5: Bảng kê mua vào nháp"| HC_2
    HC_2 -->|"Phê duyệt bảng kê hoàn tất"| DIR_AGENT

    %% Báo cáo tiến độ ngược dòng
    MGR_AGENT -.->|"Báo cáo tình trạng xử lý & Tỷ lệ hoàn thành"| DIR_AGENT

    %% ==========================================
    %% STYLING
    %% ==========================================
    classDef executive fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#ffffff;
    classDef manager fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#ffffff;
    classDef worker fill:#0f172a,stroke:#06b6d4,stroke-width:1.5px,color:#ffffff;
    classDef checkpoint fill:#450a0a,stroke:#ef4444,stroke-width:2px,color:#ffffff;
    classDef foundation fill:#134e4a,stroke:#10b981,stroke-width:1.5px,color:#ffffff;

    class DIR_AGENT executive;
    class MGR_AGENT manager;
    class SEARCH_AGENT,VERIFY_AGENT,DOWNLOAD_AGENT,STORAGE_AGENT,REPORT_AGENT worker;
    class HC_1,HC_2 checkpoint;
    class KB,RULES foundation;
```

---

## 2. MA TRẬN 7 THÀNH TỐ HỆ THỐNG

| STT | Thành tố | Nội dung triển khai cụ thể |
| :---: | :--- | :--- |
| **1** | **Agents** | • Tầng 1: `Invoice Director Agent`<br>• Tầng 2: `Invoice Manager Agent`<br>• Tầng 3: 5 Specialist Agents (`Search`, `Verify`, `Download`, `Storage`, `Report`). |
| **2** | **Skills** | • `gdt-invoice-searcher`<br>• `xml-signature-validator`<br>• `gdt-bulk-downloader`<br>• `invoice-smart-filer`<br>• `excel-tax-reporter` |
| **3** | **Workflow** | Pipeline 5 giai đoạn: Auth $\rightarrow$ Query $\rightarrow$ Verify $\rightarrow$ Download $\rightarrow$ Organize $\rightarrow$ Report. |
| **4** | **Knowledge Base** | Cấu trúc thẻ XML NĐ123, Danh bạ NCC, Blacklist thuế, Mẫu số 1 & Mẫu số 2. |
| **5** | **Rules** | Khung CLEAR: Bảo mật credentials, không sửa nội dung hóa đơn, tải đủ cặp file, chống trùng lặp. |
| **6** | **Handoff** | Giao thức truyền dữ liệu JSON schema giữa các Agent (`invoices_manifest.json`, `download_status.json`, `storage_catalog.json`). |
| **7** | **Human Checkpoint** | HC-01 (Duyệt rủi ro/Chữ ký số) & HC-02 (Ký duyệt Bảng kê thuế trước khi kê khai). |
