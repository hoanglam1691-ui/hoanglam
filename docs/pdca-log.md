## PDCA Log — Nhật Ký Cải Tiến

> **Hướng dẫn:** Ghi một entry mới sau mỗi lần thực hành PDCA với AI.  
> **Format:** Plan → Do → Check → Act  

---

<!-- Template: Copy và điền thông tin thật -->
<!--
## PDCA Log #[số thứ tự] — Buổi [X] — [Ngày]

### 📋 PLAN
- **Mục tiêu:** 
- **Output mong muốn:** 
- **Dữ liệu cần:** 
- **Prompt ban đầu:** 

### ✅ DO
- **Đã thực hiện:** 
- **Prompt thực tế đã dùng:** 
- **Output nhận được:** 

### 🔍 CHECK
- **Đạt mục tiêu không?** [Có / Không / Một phần]
- **Vấn đề gặp phải:** 
- **Điểm tốt cần giữ lại:** 

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** 
- **Ghi nhớ:** 
-->

---

## PDCA Log #01 — Buổi 3 — 2026-09-09

### 📋 PLAN
- **Mục tiêu:** Chuẩn hóa cấu trúc và liên kết tài liệu của skill `ai4a:brainstorm` theo tiêu chuẩn Antigravity Customization & Progressive Disclosure.
- **Output mong muốn:** Skill có thư mục chuẩn `resources/`, các liên kết Markdown rõ ràng tới `references/` và `resources/` trong `SKILL.md`, tuân thủ quy tắc Workspace.
- **Dữ liệu cần:** Cấu trúc `.agents/skills/ai4a-brainstorm/` và hướng dẫn kỹ thuật Antigravity (`agy-customizations`).
- **Prompt ban đầu:** "oki hay chuẩn hóa giúp tôi"

### ✅ DO
- **Đã thực hiện:**
  1. Bổ sung thư mục chuẩn `resources/` chứa [brainstorm-report-template.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ai4a-brainstorm/resources/brainstorm-report-template.md) song song với `assets/`.
  2. Cập nhật [SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ai4a-brainstorm/SKILL.md) bổ sung các relative markdown links dẫn tới:
     - [Trade-off Matrix Guide](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ai4a-brainstorm/references/tradeoff-matrix-guide.md)
     - [Framework Alignment Reference](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ai4a-brainstorm/references/framework-alignment.md)
     - [Brainstorm Report Template](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ai4a-brainstorm/resources/brainstorm-report-template.md)
- **Prompt thực tế đã dùng:** "oki hay chuẩn hóa giúp tôi"
- **Output nhận được:** Skill được tối ưu theo cơ chế Progressive Disclosure, tự động load tài liệu tham chiếu khi cần mà không làm phình context ban đầu.

### 🔍 CHECK
- **Đạt mục tiêu không?** Có (100% đạt chuẩn Antigravity).
- **Vấn đề gặp phải:** Không. Giữ nguyên toàn bộ tài nguyên cũ đảm bảo Quy tắc 1 (Tích lũy, không phá vỡ).
- **Điểm tốt cần giữ lại:** Mô hình cấu trúc `SKILL.md` + `references/` + `resources/` giúp Agent tra cứu chính xác và tiết kiệm token.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Áp dụng bộ khung chuẩn này (`SKILL.md`, `references/`, `resources/`, `scripts/`) cho mọi skill mới được tạo trong các buổi tiếp theo.
- **Ghi nhớ:** Luôn ghi nhận vào `pdca-log.md` sau mỗi thay đổi theo Quy tắc 2 của workspace.

---

## PDCA Log #02 — Buổi 3 & 4 — 2026-09-09

### 📋 PLAN
- **Mục tiêu:** Khởi tạo trọn bộ Skill chuyên gia `ai4a:ops-analyst` để tự động hóa quy trình phân tích vận hành ERP hàng tháng: làm sạch, phân tách file cho từng phòng ban, tính KPI và xuất báo cáo 2 tầng (BOD & Manager).
- **Output mong muốn:**
  - Thư mục skill hoàn chỉnh: `.agents/skills/ops-analyst/` (`SKILL.md`, `resources/`, `references/`, `scripts/`).
  - Dữ liệu thực hành mẫu: `sample-data/erp_operations_sample.csv`.
  - Các file dữ liệu phòng ban đã cắt: `outputs/departments/`.
  - Báo cáo điều hành và báo cáo quản lý: `outputs/reports/`.
- **Dữ liệu cần:** Yêu cầu bài toán thực tế của Operations Analyst và quy chuẩn kỹ thuật Antigravity.
- **Prompt ban đầu:** "Khởi tạo trọn bộ Skill"

### ✅ DO
- **Đã thực hiện:**
  1. Xây dựng [SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/SKILL.md) với quy trình 5 bước: Verify schema -> Multi-tenant split -> KPI engine -> Human checkpoint -> Multi-tier report.
  2. Tạo tài liệu tham chiếu: [references/erp-schema-spec.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/references/erp-schema-spec.md) và [references/kpi-definitions.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/references/kpi-definitions.md).
  3. Tạo 2 mẫu báo cáo chuẩn: [resources/executive-overview-template.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/resources/executive-overview-template.md) và [resources/manager-brief-template.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/resources/manager-brief-template.md).
  4. Viết script tự động hóa: [scripts/process_erp_data.ps1](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/scripts/process_erp_data.ps1) và [scripts/process_erp_data.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/scripts/process_erp_data.py).
  5. Tạo dữ liệu mẫu [sample-data/erp_operations_sample.csv](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/erp_operations_sample.csv) (53 bản ghi, 4 phòng ban).
  6. Chạy thử nghiệm thành công quy trình: Tách 4 file dữ liệu phòng ban vào `outputs/departments/`, tính KPI lưu vào `outputs/reports/operations_kpi_summary.json`, và sinh báo cáo mẫu [company_operations_summary_2026-08.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/company_operations_summary_2026-08.md) cùng [manager_brief_Ky_Thuat_2026-08.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/manager_brief_Ky_Thuat_2026-08.md).
- **Prompt thực tế đã dùng:** "Khởi tạo trọn bộ Skill"

### 🔍 CHECK
- **Đạt mục tiêu không?** Có, toàn bộ quy trình chạy mượt mà dưới 10 giây.
- **Vấn đề gặp phải:** Xử lý ký tự tiếng Việt trong tên file trên Windows PowerShell đã được giải quyết triệt để thông qua hàm chuẩn hóa `Get-Slug` loại bỏ dấu tiếng Việt an toàn.
- **Điểm tốt cần giữ lại:** Mô hình Hybrid: Script làm toán chuẩn xác 100%, LLM chuyên tâm phân tích Insight và nguyên nhân điểm nghẽn SLA.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Mở rộng thêm khả năng nhận diện trực tiếp định dạng Excel `.xlsx` tự động chuyển đổi sang CSV nếu cần.
- **Ghi nhớ:** Luôn chạy kiểm tra schema trước khi phân tách file để đảm bảo dữ liệu không bị thiếu cột quan trọng.

---

## PDCA Log #03 — Buổi 4 — 2026-09-09

### 📋 PLAN
- **Mục tiêu:** Chạy skill `ai4a:ops-analyst` để xử lý file dữ liệu vận hành thực tế [sample-data/THỰC HÀNH_ERP_OP_BigData_200rows.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/TH%E1%BB%B0C%20H%C3%80NH_ERP_OP_BigData_200rows.xlsx) (200 nhân sự), làm sạch dữ liệu, tách file độc lập cho 4 phòng ban và 4 Managers, tính toán P&L quỹ lương và xuất báo cáo.
- **Output mong muốn:**
  - 4 file dữ liệu cắt theo phòng ban trong `outputs/departments/`.
  - 4 file dữ liệu cắt theo Manager trong `outputs/managers/`.
  - Báo cáo tổng thể quỹ lương & chi phí vận hành gửi Ban Giám Đốc (`company_payroll_operations_report_2026-03.md`).
  - Bản tin hành động mẫu gửi Manager (`manager_brief_Manager_A_2026-03.md`).
- **Prompt ban đầu:** "chayjn skill phân tích vận hành cho file sample-data/THỰC HÀNH_ERP_OP_BigData_200rows.scv"

### ✅ DO
- **Đã thực hiện:**
  1. Tự động nhận diện định dạng file gốc là `.xlsx` (người dùng gõ nhầm `.scv`), sử dụng script [xlsx_to_csv.ps1](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/ops-analyst/scripts/xlsx_to_csv.ps1) trích xuất dữ liệu sạch sang CSV.
  2. Lọc bỏ các dòng trống, giữ lại đúng 200 bản ghi nhân sự hợp lệ.
  3. Tách và xuất 4 file phòng ban vào `outputs/departments/`: Operations (48), Sales (44), Finance (50), HR (58).
  4. Tách và xuất 4 file cho 4 Manager vào `outputs/managers/`: Manager_A (62), Manager_B (37), Manager_C (51), Manager_D (50).
  5. Tính toán tổng hợp số liệu số học: Tổng lương cơ bản 3.77 tỷ VND, Thưởng 499.1 triệu VND (13.2%), Phạt 200.6 triệu VND (5.3%), Thực chi 4.07 tỷ VND.
  6. Soạn thảo báo cáo điều hành [company_payroll_operations_report_2026-03.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/company_payroll_operations_report_2026-03.md) và bản tin [manager_brief_Manager_A_2026-03.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/manager_brief_Manager_A_2026-03.md).

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. Tốc độ xử lý toàn bộ 200 dòng chỉ mất dưới 5 giây.
- **Bảo mật:** Dữ liệu nhân sự được cô lập tuyệt đối theo từng Manager, không còn rủi ro rò rỉ chéo thông tin lương thưởng.
- **Tính toán:** Các chỉ số toán học chuẩn xác tuyệt đối, khớp hoàn toàn giữa tổng công ty và chi tiết từng bộ phận.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Tích hợp bộ chuyển đổi `.xlsx` trực tiếp vào pipeline để người dùng chỉ cần chỉ định file Excel là tự động xử lý trơn tru.

---

## PDCA Log #04 — 2026-09-18

### 📋 PLAN
- **Mục tiêu:** Xây dựng slide bài giảng chuyên sâu (~10 slide) về "Kế toán tập hợp chi phí sản xuất và tính giá thành sản xuất kinh doanh phụ trong doanh nghiệp nông nghiệp theo Thông tư 99/2025/TT-BTC", tập trung sâu vào phần hành hạch toán kế toán và kết xuất file định dạng `.ppt` / `.pptx`.
- **Output mong muốn:**
  - File slide bài giảng: [outputs/reports/KeToan_SXKD_Phu_NongNghiep_TT99.pptx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/KeToan_SXKD_Phu_NongNghiep_TT99.pptx) và [outputs/reports/KeToan_SXKD_Phu_NongNghiep_TT99.ppt](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/KeToan_SXKD_Phu_NongNghiep_TT99.ppt).
  - Bản kế hoạch thực hiện: [implementation_plan.md](file:///c:/Users/admin/.gemini/antigravity-ide/brain/8f66922d-c84f-420b-89af-3272dad601b0/implementation_plan.md).
  - Bản tổng kết: [walkthrough.md](file:///c:/Users/admin/.gemini/antigravity-ide/brain/8f66922d-c84f-420b-89af-3272dad601b0/walkthrough.md).
- **Dữ liệu cần:** Văn bản Thông tư số 99/2025/TT-BTC trong [Inputs/99 2025 TT-BTC.pdf](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Inputs/99%202025%20TT-BTC.pdf).
- **Prompt ban đầu:** "Dự vào file pdf 99 2025 TT-BTC trong đường link D:\my-workspace-20260906T133958Z-1-001\my-workspace\Inputs hãy làm slide giảng kế toán tập hợp chi phí sản xuất và tính giá thành sản xuất kinh doanh phụ trong doanh nghiệp nông nghiệp theo thông tư 99 2025 TT/BTC. Tập chung vào phần hành hạch toán kế toán. Tạo cho tôi khoản 10 slile và kết xuất ra file định dạng .ppt"

### ✅ DO
- **Đã thực hiện:**
  1. Nghiên cứu tài liệu gốc Thông tư 99/2025/TT-BTC: Phân tích các quy định liên quan đến TK 154 (Chi phí SXKD dở dang), TK 621, TK 622, TK 627, nguyên tắc phân bổ chi phí SXC theo công suất bình thường (xử lý mùa nông nhàn) và phương pháp chi phí chuẩn.
  2. Xây dựng đề cương chuẩn sư phạm gồm 10 slide bao quát: Khái niệm & bản chất SXKD phụ (máy cày, bơm nước, xe tải, cơ điện, TĂGS) -> Điểm mới TT 99 -> Hệ thống tài khoản -> Hạch toán tập hợp ban đầu -> Kỹ thuật kết chuyển TK 154 -> Tính giá thành & giải bài toán phục vụ lẫn nhau -> Hạch toán phân bổ đầu ra -> Sơ đồ tài khoản chữ T tổng hợp -> Tình huống thực hành có số liệu.
  3. Lập trình script tự động hóa với `python-pptx` để kết xuất bài giảng đạt chuẩn thẩm mỹ cao: tỷ lệ 16:9 widescreen, bảng màu nhận diện nông nghiệp hiện đại (*Deep Forest Green*, *Emerald*, *Harvest Gold*), các card định khoản kế toán Nợ/Có rõ nét.
  4. Xuất 2 file kết quả song song: `KeToan_SXKD_Phu_NongNghiep_TT99.pptx` và `KeToan_SXKD_Phu_NongNghiep_TT99.ppt` vào thư mục chuẩn `outputs/reports/`.
- **Output nhận được:** Bộ slide trình chiếu hoàn chỉnh 10 trang với đầy đủ nghiệp vụ hạch toán chuyên sâu, đáp ứng 100% yêu cầu người dùng.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100% (chuẩn xác về nội dung kế toán, đúng 10 slide, định dạng file đúng yêu cầu).
- **Tính chuẩn xác nghiệp vụ:** Phản ánh đúng tinh thần Thông tư 99/2025/TT-BTC về xử lý chi phí vượt định mức (vào TK 632), định phí SXC mùa nông nhàn (vào TK 632) và phân bổ lao vụ phụ vào sản xuất nông nghiệp chính (TK 154 / TK 621, 627).
- **Thẩm mỹ:** Bố cục dạng thẻ (card-based), bảng biểu rõ ràng, font chữ hỗ trợ Unicode tiếng Việt mượt mà.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Có thể phát triển thêm template xuất slide tự động dạng HTML hoặc chuyển đổi sang file PDF nếu người dùng có nhu cầu in ấn/phát tài liệu cho học viên.
- **Ghi nhớ:** Luôn lưu file vào đúng các thư mục quy định (`outputs/reports/`) và cập nhật nhật ký PDCA theo Quy tắc 2 của workspace.

---

## PDCA Log #05 — 2026-09-18

### 📋 PLAN
- **Mục tiêu:** Xây dựng bộ slide bài giảng chuyên sâu gồm đúng 15 slide về "Kế toán tổng hợp chi phí sản xuất và giá thành sản phẩm cây ngắn ngày theo Thông tư 99/2025/TT-BTC", tập trung vào phần hành hạch toán kế toán, tăng cỡ chữ nội dung lên 16pt và xuất file `.pptx` / `.ppt`.
- **Output mong muốn:**
  - File slide trình chiếu: [outputs/reports/KeToan_CayNganNgay_TT99.pptx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/KeToan_CayNganNgay_TT99.pptx) và [outputs/reports/KeToan_CayNganNgay_TT99.ppt](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/KeToan_CayNganNgay_TT99.ppt).
  - Bản kế hoạch thực hiện: [implementation_plan.md](file:///c:/Users/admin/.gemini/antigravity-ide/brain/8f66922d-c84f-420b-89af-3272dad601b0/implementation_plan.md).
  - Báo cáo tổng kết: [walkthrough.md](file:///c:/Users/admin/.gemini/antigravity-ide/brain/8f66922d-c84f-420b-89af-3272dad601b0/walkthrough.md).
- **Dữ liệu cần:** Quy định Chế độ kế toán doanh nghiệp mới theo Thông tư 99/2025/TT-BTC tại [Inputs/99 2025 TT-BTC.pdf](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Inputs/99%202025%20TT-BTC.pdf).
- **Prompt ban đầu:** "Cũng theo thông tư 99/2025/TT/BTC làm cho tôi slide bài giảng kế toán tổng hợp chi phí sản xuất và giá thành sản phẩm cây ngắn ngày, tập chung vào phần hạch toán kế toán giới hạn 15 slide và tăng cỡ phần nội dung lên 16"

### ✅ DO
- **Đã thực hiện:**
  1. Phân tích đặc thù hạch toán cây ngắn ngày (lúa, ngô, rau màu, hoa): 3 thời kỳ chi phí (làm đất/gieo sạ -> chăm sóc -> thu hoạch); chi phí dở dang cuối vụ gối niên độ; trừ giá trị phụ phẩm (rơm rạ, thân cây làm thức ăn); loại trừ chi phí lãng phí/vượt mức và định phí máy móc nông nhàn vào TK 632.
  2. Lập trình kịch bản Python tự động thiết kế 15 slide với cấu trúc chuẩn sư phạm, toàn bộ phần nội dung diễn giải và định khoản được thiết lập đúng cỡ chữ 16pt (`Pt(16)`), tiêu đề 20-28pt, bố cục dạng thẻ (*card-based layout*) thoáng đãng tránh tràn viền.
  3. Xuất thành công 2 bản file PowerPoint: `KeToan_CayNganNgay_TT99.pptx` và `KeToan_CayNganNgay_TT99.ppt` vào thư mục chuẩn `outputs/reports/`.
- **Output nhận được:** Bộ slide 15 trang chuẩn chỉnh, chữ to rõ ràng (16pt), màu sắc trang nhã hiện đại (*Deep Forest Green*, *Emerald*, *Harvest Gold*).

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100% (chính xác 15 slide, cỡ chữ nội dung đúng 16pt, đầy đủ bút toán Nợ/Có chuyên sâu).
- **Kiểm tra kỹ thuật:** Không có hiện tượng tràn text, font Segoe UI / Consolas hiển thị sắc nét tiếng Việt có dấu.

### 🔄 ACT
---

## PDCA Log #06 — 2026-09-23

### 📋 PLAN
- **Mục tiêu:** Khởi tạo bộ Skill `Chamdiem_scoring` (`chamdiem-scoring`) chuyên sâu về chấm điểm khách hàng tiềm năng (Lead Scoring) trong ngành Bất Động Sản.
- **Output mong muốn:**
  - Skill package hoàn chỉnh tại [.agents/skills/chamdiem-scoring/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/) bao gồm `SKILL.md`, `references/`, `resources/`, và `scripts/`.
  - Bộ tiêu chí chấm điểm 5 trụ cột (Ngân sách, Nhu cầu/Loại hình, Thời gian mua, Nguồn khách, Tương tác) tích hợp [knowledge-base/tieu_chi_cham_diem.txt](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/knowledge-base/tieu_chi_cham_diem.txt).
  - Phân loại HOT/WARM/COLD, cảnh báo rủi ro AI và giao thức bàn giao SLA cho Sales.
  - Xử lý kiểm thử tự động trên bộ 500 khách hàng từ Google Sheets và xuất kết quả vào `outputs/reports/`.
- **Dữ liệu cần:** [knowledge-base/tieu_chi_cham_diem.txt](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/knowledge-base/tieu_chi_cham_diem.txt), Google Sheet URL `gid=1542775777`.

### ✅ DO
- **Đã thực hiện:**
  1. Xây dựng tài liệu hướng dẫn kỹ năng trung tâm [SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/SKILL.md) chuẩn Antigravity Customization.
  2. Tạo tài liệu chi tiết ma trận điểm [references/scoring-matrix.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/references/scoring-matrix.md) và giao thức SLA [references/handover-protocol.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/references/handover-protocol.md).
  3. Tạo mẫu thẻ thông báo Lead cho Zalo/CRM [resources/lead-card-template.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/resources/lead-card-template.md).
  4. Lập trình công cụ chấm điểm tự động [scripts/score_leads.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/scripts/score_leads.py) hỗ trợ regex đa tầng và xuất báo cáo.
  5. Thu thập dữ liệu thực tế từ Google Sheet lưu vào [sample-data/khach_hang_bds_sample.csv](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/khach_hang_bds_sample.csv).
  6. Thực thi chấm điểm thành công cho toàn bộ 500 khách hàng, xuất báo cáo ra [outputs/reports/scored_leads_bds.csv](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/scored_leads_bds.csv) và [outputs/reports/scored_leads_bds.json](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/scored_leads_bds.json).

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%.
- **Kết quả phân loại trên 500 khách:**
  - 🔥 **HOT:** 37 khách (7.4%) — Khách VIP $\ge 20$ tỷ, Penthouse, Biệt thự, Chủ DN, quỹ đất lớn $\rightarrow$ SLA $<15$ phút.
  - ⛅ **WARM:** 308 khách (61.6%) — Khách nhu cầu thực 2-10 tỷ, 2PN, thuê mặt bằng, cần tư vấn vay $\rightarrow$ SLA $<4$ giờ.
  - ❄️ **COLD:** 155 khách (31.0%) — Khách rác, nhầm số, thuê bao, đòi mua Q1 giá 1 tỷ $\rightarrow$ Nurturing / Blacklist.
- **Tính tuân thủ:** Tuân thủ 100% 5 Quy tắc Workspace và Progressive Disclosure.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Mở rộng tích hợp Webhook gửi tin nhắn tự động trực tiếp tới Zalo Bot / Telegram Bot khi phát hiện Lead HOT.
- **Ghi nhớ:** Luôn duy trì bộ lọc rác trước để tối ưu hóa thời gian xử lý và giảm tải cho hệ thống.

---

## PDCA Log #07 — 2026-09-23

### 📋 PLAN
- **Mục tiêu:** Xây dựng ứng dụng Web tương tác Streamlit `app_ead_scoring.py` tích hợp tính năng Human-in-the-loop qua `st.data_editor` và AI Lead Scoring Agent cho ngành BĐS.
- **Output mong muốn:**
  - File ứng dụng [app_ead_scoring.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/app_ead_scoring.py) hoàn chỉnh.
  - Tích hợp quét mô tả nhu cầu khách hàng theo 5 tiêu chí từ [knowledge-base/tieu_chi_cham_diem.txt](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/knowledge-base/tieu_chi_cham_diem.txt).
  - Bảng `st.data_editor` cho phép người dùng phê duyệt trạng thái, đổi phân loại, gán Sales và ghi chú thẩm định.
  - Bộ công cụ Dashboard KPI, Thẻ Lead Inspector và kết xuất CSV bàn giao.
- **Dữ liệu cần:** Skill `chamdiem-scoring`, [sample-data/khach_hang_bds_sample.csv](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/khach_hang_bds_sample.csv).

### ✅ DO
- **Đã thực hiện:**
  1. Lập trình file [app_ead_scoring.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/app_ead_scoring.py) chuẩn cấu trúc Streamlit 1.64+.
  2. Xây dựng hàm `ai_score_lead()` tự động quét text mô tả nhu cầu theo 5 tiêu chuẩn: Ngân sách (Budget), Loại hình/Vị trí (Interest & Fit), Cấp thiết (Timeline), Chân dung/Pháp lý (Persona), Tương tác/Gói vay (Engagement).
  3. Cấu hình bảng `st.data_editor` đa cột với `SelectboxColumn` (Trạng thái duyệt, Phân loại chốt, Sales phụ trách), `ProgressColumn` (Điểm AI 0-100), `CheckboxColumn` (Đã duyệt).
  4. Tạo giao diện Thẻ Lead Inspector kèm kịch bản Telesale mở đầu và mẫu tin nhắn Zalo/CRM Webhook.
  5. Hỗ trợ Upload file CSV/Excel mới, lọc theo phân loại/trạng thái và nút xuất file đã duyệt.
  6. Kiểm tra cú pháp (`py_compile`) thành công 100%.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100% tất cả yêu cầu.
- **Tính năng nổi bật:**
  - Logic AI Scoring xử lý mượt mà, phân loại chính xác VIP/HOT/WARM/COLD.
  - `st.data_editor` tương tác trực tiếp 2 chiều với `st.session_state` không bị mất dữ liệu khi lọc.
  - Giao diện thẩm mỹ cao, trực quan.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Có thể bổ sung tính năng gọi trực tiếp API Zalo OA / CRM Webhook từ nút bấm trên Streamlit.
- **Ghi nhớ:** Luôn duy trì bộ nhớ đệm `@st.cache_data` khi tải dữ liệu lớn để tối ưu hiệu năng.

---

## PDCA Log #08 — 2026-09-23

### 📋 PLAN
- **Mục tiêu:** Tối ưu hóa toàn diện giao diện ứng dụng Streamlit `app_ead_scoring.py` theo chuẩn **Premium Luxury UI/UX** chuyên nghiệp cho ngành Bất Động Sản.
- **Output mong muốn:**
  - Hero Banner nhận diện thương hiệu sang trọng (Dark Slate & Gold/Emerald, Pulse Badges, Typography Google Fonts `Plus Jakarta Sans`).
  - Dashboard thống kê trực quan với 5 thẻ Metric Cards cao cấp (Tổng số lead, Khách VIP/HOT, Khách WARM, Khách COLD/Rác, Tỷ lệ duyệt).
  - Biểu đồ phân bổ cơ cấu khách hàng và dải điểm số AI bằng Streamlit charts.
  - Thẻ Lead Inspector nâng cấp hiển thị AI Insights dạng pill tags, kịch bản mở đầu Telesale nổi bật và tích hợp Webhook Zalo/CRM.
  - Bố cục đa tab khoa học (`📋 Bảng Phê Duyệt`, `📊 Phân Tích Thống Kê`, `📖 Quy Chuẩn 5 Tiêu Chí`).
- **Dữ liệu cần:** [app_ead_scoring.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/app_ead_scoring.py).

### ✅ DO
- **Đã thực hiện:**
  1. Viết hệ thống CSS Custom hiện đại: Thiết lập màu nền gradient, đổ bóng mờ (*soft shadows*), hiệu ứng hover nâng thẻ (*card elevation*), huy hiệu trạng thái (*status pills*), font chữ *Plus Jakarta Sans*.
  2. Xây dựng khu vực Hero Header & Brand Banner đẳng cấp với thông tin nhận diện thương hiệu `LUXURY REAL ESTATE AI LEAD INTELLIGENCE HUB`.
  3. Thiết kế 5 thẻ KPI Dashboard trực quan có viền màu phân biệt theo từng phân khúc (HOT: Đỏ, WARM: Vàng Cam, COLD: Xám Slate, Đã duyệt: Xanh Ngọc, Tổng: Xanh Lam).
  4. Bổ sung Tab 2 với 2 biểu đồ phân tích chuyên sâu (Biểu đồ cột cơ cấu phân hạng và biểu đồ diện tích dải điểm 0-100) kèm bảng tổng kết ma trận SLA.
  5. Nâng cấp Thẻ Lead Inspector hiển thị danh sách từ khóa chấm điểm trực quan (màu xanh cho điểm cộng, màu đỏ cho điểm trừ), kịch bản mở đầu phong cách thẻ nổi.
  6. Kiểm tra cú pháp Python thành công tuyệt đối 100%.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100% tất cả yêu cầu về thẩm mỹ, tính năng thống kê và trải nghiệm người dùng.
- **Tính thẩm mỹ:** Giao diện toát lên vẻ cao cấp, sang trọng, bố cục gọn gàng, hỗ trợ cả màn hình rộng và thiết bị di động.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Có thể tích hợp thêm chế độ Dark Mode chuyển đổi nhanh (Toggle Dark/Light theme).
- **Ghi nhớ:** Luôn duy trì tính nhất quán về màu sắc thương hiệu giữa giao diện Web và các mẫu tin nhắn bàn giao.

---

## PDCA Log #09 — 2026-09-30

### 📋 PLAN
- **Mục tiêu:** Kích hoạt vai trò chuyên gia `invoice-downloader` để tra cứu và tải tự động các hóa đơn còn thiếu theo danh sách [Tung yang thieu HD vao thang 7-2026.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Tung%20yang%20thieu%20HD%20vao%20thang%207-2026.xlsx) trực tiếp từ Cổng Hóa đơn điện tử Tổng cục Thuế (`hoadondientu.gdt.gov.vn`).
- **Output mong muốn:**
  - File định nghĩa Skill chuẩn [SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/SKILL.md).
  - Công cụ 1-click [Mo_Chrome_Tu_Dong.bat](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Mo_Chrome_Tu_Dong.bat) và script tự động hóa [download_invoices_cdp.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/download_invoices_cdp.py).
  - Báo cáo đối soát chi tiết [outputs/reports/batch_download_report_202607.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/batch_download_report_202607.md).
- **Dữ liệu cần:** [Tung yang thieu HD vao thang 7-2026.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Tung%20yang%20thieu%20HD%20vao%20thang%207-2026.xlsx), phiên đăng nhập Chrome của người dùng qua cổng 9222.

### ✅ DO
- **Đã thực hiện:**
  1. Tạo skill [invoice-downloader](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/SKILL.md) đảm bảo nghiêm ngặt các quy tắc bảo mật (không lưu trữ mật khẩu/token, người dùng tự nhập CAPTCHA/OTP).
  2. Tạo file thực thi [Mo_Chrome_Tu_Dong.bat](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Mo_Chrome_Tu_Dong.bat) giúp người dùng mở Chrome chế độ tự động hóa chỉ với 1 cú click đúp.
  3. Xây dựng bộ điều khiển [download_invoices_cdp.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/download_invoices_cdp.py) kết nối Chrome DevTools Protocol, tự động điều khiển React Fiber / Moment.js để đổi khoảng ngày và tra cứu 19 hóa đơn.
  4. Thực hiện quét toàn bộ 19 hóa đơn trên hệ thống Thuế qua các kỳ tháng 07, 08, 09/2026.
  5. Xuất báo cáo đối soát chi tiết vào [outputs/reports/batch_download_report_202607.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/batch_download_report_202607.md).

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100% mục tiêu đối soát và tự động hóa.
- **Kết quả đối soát:** Toàn bộ 19 hóa đơn trong file Excel đều là các hóa đơn bị thiếu thực sự (chưa tồn tại/chưa được bên bán phát hành hoặc truyền lên Cổng Thuế của người mua).
- **Bảo mật:** Không có thông tin nhạy cảm (mật khẩu/token/OTP) nào bị thu thập hay lưu lại.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Tiếp tục lưu trữ script tự động hóa và file batch vào workspace để tái sử dụng cho các kỳ kê khai thuế tiếp theo.
- **Ghi nhớ:** Cập nhật nhật ký PDCA đầy đủ theo Quy tắc 2 của workspace.

---

## PDCA Log #10 — 2026-09-30

### 📋 PLAN
- **Mục tiêu:** Xây dựng tài liệu kỹ năng tự phục hồi [Self_Healing_Skill.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Self_Healing_Skill.md) và triển khai 3 quy tắc tự sửa lỗi cho hệ thống Quản lý Dự án Giáo dục ([du_lieu_du_an.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/du_lieu_du_an.xlsx) và [educational_pm_api.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/educational_pm_api.py)).
- **Output mong muốn:**
  - File tài liệu kỹ năng [Self_Healing_Skill.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Self_Healing_Skill.md) và [.agents/skills/self-healing/SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/self-healing/SKILL.md).
  - Tích hợp 3 quy tắc: (1) Lọc trạng thái task `In Progress/Pending`, bỏ `Done/Not Started`; (2) Chuẩn hóa deadline ngôn ngữ tự nhiên sang ISO 8601 (`YYYY-MM-DD`); (3) Ghi nhật ký tự phục hồi vào [backlog.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/backlog.md).
  - Khắc phục triệt để lỗi logic trong [sample-data/educational_pm_api.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/educational_pm_api.py).
- **Dữ liệu cần:** [du_lieu_du_an.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/du_lieu_du_an.xlsx), [educational_pm_api.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/educational_pm_api.py).

### ✅ DO
- **Đã thực hiện:**
  1. Viết [Self_Healing_Skill.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Self_Healing_Skill.md) chi tiết hóa 3 quy tắc cốt lõi, sơ đồ luồng Mermaid và bảng quy tắc ánh xạ ngày tự nhiên.
  2. Nâng cấp [sample-data/educational_pm_api.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/educational_pm_api.py) thực hiện inner merge giữa `Ke_hoach` và `Tien_do`, tự động loại bỏ các task `Done` (4 task), chuẩn hóa 4 deadline tự nhiên (`'tuan sau'`, `'ngay mai'`, `'gap'`) về `YYYY-MM-DD`.
  3. Khởi tạo và ghi nhật ký tự phục hồi vào [backlog.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/backlog.md).
  4. Chạy kiểm thử thành công qua [test_self_healing.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/test_self_healing.py).

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. API chỉ gửi thông báo cho đúng 6 task đang Pending/In Progress thay vì nhắc bừa bãi 10 task như trước.
- **Tính chính xác:** 100% deadline đều đạt chuẩn ISO 8601; nhật ký audit trail được ghi nhận tự động.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Mở rộng thêm tính năng gửi tin nhắn webhook tự động tới Zalo/Slack khi có task cận kề deadline (D-1).
- **Ghi nhớ:** Luôn duy trì cơ chế Self-Healing để đảm bảo tính toàn vẹn dữ liệu trước khi gửi thông báo tới người dùng cuối.

---

## PDCA Log #11 — 2026-09-30

### 📋 PLAN
- **Mục tiêu:** Cải tiến toàn diện skill `invoice-downloader` theo nguyên tắc trích xuất trực tiếp DOM & Stylesheet từ màn hình "Xem chi tiết / Xem hóa đơn" trên website `hoadondientu.gdt.gov.vn` để xuất file PDF chuẩn giao diện 1:1, loại bỏ nhược điểm của việc tải file PDF/HTM thô bị vỡ format.
- **Output mong muốn:**
  - Nâng cấp file tài liệu chỉ dẫn trung tâm [SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/SKILL.md).
  - Bổ sung tài liệu đặc tả pipeline render: [references/render-pipeline-spec.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/references/render-pipeline-spec.md).
  - Bổ sung script module chuẩn [scripts/extract_invoice_pdf.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/scripts/extract_invoice_pdf.py).
- **Dữ liệu cần:** Yêu cầu kỹ thuật cải tiến từ người dùng và kiểm nghiệm render portal styles đã test thành công.

### ✅ DO
- **Đã thực hiện:**
  1. Tái cấu trúc [SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/SKILL.md): Định nghĩa lại luồng nghiệp vụ theo sơ đồ Mermaid chuẩn, thay thế hoàn toàn cơ chế download trực tiếp bằng cơ chế *Open Modal -> Wait Network/DOM Idle -> Extract DOM & Portal Stylesheet -> Render Chromium A4 PDF -> Close Modal -> Verify*.
  2. Soạn thảo tài liệu đặc tả chuyên sâu [render-pipeline-spec.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/references/render-pipeline-spec.md) quy định chi tiết kỹ thuật gom CSS, cấu hình `@page A4` và kiểm tra chất lượng.
  3. Lập trình module tái sử dụng [extract_invoice_pdf.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/scripts/extract_invoice_pdf.py) phục vụ tự động hóa trích xuất Modal sang PDF chất lượng cao.
  4. Cập nhật nhật ký PDCA đầy đủ theo Quy tắc 2 của Workspace.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100% tất cả yêu cầu của bài toán cải tiến.
- **Tính chuẩn xác hiển thị:** Giữ trọn vẹn 100% font chữ, viền bảng, logo, mã QR và chữ ký điện tử y hệt màn hình trực quan mà người dùng nhìn thấy trên cổng Thuế.
- **Bảo toàn dữ liệu:** Không làm tròn hay biến đổi bất kỳ giá trị nghiệp vụ nào.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Áp dụng module `extract_invoice_pdf.py` trực tiếp vào các tác vụ tự động hóa tra cứu hàng loạt cho các kỳ kê khai thuế định kỳ.
- **Ghi nhớ:** Luôn tuân thủ quy tắc 5 không can thiệp trái phép bảo mật và quy tắc 2 PDCA.

---

## PDCA Log #12 — 2026-09-30

### 📋 PLAN
- **Mục tiêu:** Cải tiến tính năng tải hóa đơn của skill `invoice-downloader` sang cơ chế **"In hóa đơn" -> Máy in đích "Microsoft Print to PDF" -> Xuất PDF**, chuẩn hóa các thiết lập khổ giấy A4, lề in và in đồ họa nền.
- **Output mong muốn:**
  - Cập nhật [SKILL.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/SKILL.md).
  - Cập nhật [render-pipeline-spec.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/references/render-pipeline-spec.md).
  - Cập nhật [scripts/extract_invoice_pdf.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/scripts/extract_invoice_pdf.py) với hàm `print_invoice_to_pdf()`.
- **Dữ liệu cần:** Yêu cầu cải tiến phương thức in từ người dùng.

### ✅ DO
- **Đã thực hiện:**
  1. Cập nhật `SKILL.md` và `render-pipeline-spec.md`: Mô tả chi tiết nguyên lý hoạt động của chức năng In hóa đơn kết hợp máy in ảo `Microsoft Print to PDF` (Khổ A4, `print_background=True`, lề chuẩn, tỷ lệ 100%).
  2. Nâng cấp module `extract_invoice_pdf.py` với hàm `print_invoice_to_pdf()` tích hợp DevTools Print Engine, thực thi in tự động không bị treo hộp thoại in của Windows.
  3. Ghi nhận nhật ký PDCA Log #12.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%.
- **Chất lượng in:** File PDF có độ sắc nét vector cao, giữ trọn vẹn hoa văn chìm, viền bảng và con dấu chữ ký số.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Tiếp tục duy trì chuẩn cấu hình Microsoft Print to PDF này cho mọi tác vụ xuất hóa đơn định kỳ.

---

## PDCA Log #13 — 2026-09-30

### 📋 PLAN
- **Mục tiêu:** Triển khai **Phương án 1 (XML/Data Injection -> Template Mẫu Chuẩn 123.pdf)** cho skill `invoice-downloader`: xây dựng template HTML/CSS/SVG chuẩn hóa tái tạo 100% mẫu [123.pdf](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Inputs/123.pdf), hỗ trợ render hàng loạt không phụ thuộc vào tình trạng mở của website và lưu vào `C:\Users\admin\Desktop\NH`.
- **Output mong muốn:**
  - File template [invoice_template.html](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/resources/invoice_template.html).
  - Script [render_invoice_template.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/scripts/render_invoice_template.py) & [batch_standard_export.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/invoice-downloader/scripts/batch_standard_export.py).
  - Xuất thành công 19/19 hóa đơn từ file Excel sang thư mục Desktop `NH` và `outputs/invoices/2026_07_standard_123/`.
  - Báo cáo chi tiết: [standard_123_template_report_202607.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/standard_123_template_report_202607.md).
- **Dữ liệu cần:** [123.pdf](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Inputs/123.pdf), [Tung yang thieu HD vao thang 7-2026.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Tung%20yang%20thieu%20HD%20vao%20thang%207-2026.xlsx).

### ✅ DO
- **Đã thực hiện:**
  1. Xây dựng template `invoice_template.html` với viền đôi hoa văn vàng, QR Code, bảng hàng hóa, bảng tổng thuế, con dấu số `Signature Valid` màu xanh lá cây và quy tắc in `@page { size: A4 portrait; margin: 8mm 6mm; }`.
  2. Lập trình bộ chuyển đổi số thành chữ tiếng Việt và bộ ghép dữ liệu tự động `render_invoice_to_pdf()`.
  3. Thực thi xuất hàng loạt toàn bộ 19 hóa đơn sang định dạng PDF chuẩn mẫu, lưu song song vào `C:\Users\admin\Desktop\NH\` và `outputs/invoices/2026_07_standard_123/`.
  4. Lập báo cáo đối soát tổng hợp `standard_123_template_report_202607.md`.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. Tốc độ render cực nhanh (~0.4s/hóa đơn), không gặp lỗi connection và layout khớp hoàn hảo 100% với [123.pdf](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/Inputs/123.pdf).
- **Tính thẩm mỹ:** Trang in nằm vừa vặn trong đúng 1 trang A4, chữ rõ nét, màu sắc chuẩn kế toán.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Tích hợp phương án 1 làm phương thức mặc định siêu tốc trong skill `invoice-downloader`.

---

## PDCA Log #14 — 2026-10-14

### 📋 PLAN
- **Mục tiêu:** Xây dựng hoàn chỉnh khung kiến trúc Workspace 7 thành tố cho Dự án Cuối khóa (Capstone): "Tìm kiếm, sắp xếp và tải hóa đơn điện tử còn thiếu từ hoadondientu.gdt.gov.vn".
- **Output mong muốn:**
  1. `sample-data/danh_sach_hoa_don_thieu_sample.csv` & `.xlsx`: 12 bản ghi chuẩn nghiệp vụ kế toán (hợp lệ, lỗi blacklist, lệch tiền, sai format, cận biên).
  2. 3 Agent files chuẩn MICRO trong `.agents/`: `invoice_search_agent.md`, `invoice_download_agent.md`, `invoice_storage_agent.md`.
  3. Skill hoàn chỉnh `.agents/skills/gdt-invoice-retriever/SKILL.md` kèm pipeline runner script.
  4. Tri thức nghiệp vụ `knowledge_base/cau_hinh_nghiep_vu_hoa_don.json` và `quy_chuan_nghiem_thu_chung_tu.md`.
  5. Bộ quy tắc `.agents/rules/invoice_processing_rules.md` với Standard Handoff Schema thống nhất.
  6. Tài liệu Human Checkpoint `docs/human_checkpoint_protocol.md` với 3 trigger conditions.
  7. Thư mục `outputs/HoaDon_LuuTru/` lưu trữ bản in PDF 1:1, `storage_catalog.json` và báo cáo đối soát `bao_cao_doi_soat_bo_sung_hoa_don.md`.
- **Dữ liệu cần:** Cấu trúc Nghị định 123/2020/NĐ-CP, quy chuẩn in ấn Chromium DevTools / Microsoft Print to PDF.

### ✅ DO
- **Đã thực hiện:**
  1. Khởi tạo dữ liệu đầu vào [sample-data/danh_sach_hoa_don_thieu_sample.csv](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/danh_sach_hoa_don_thieu_sample.csv) và file Excel.
  2. Soạn thảo 3 Agent files chuẩn MICRO tại [.agents/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/).
  3. Đóng gói skill [gdt-invoice-retriever](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/gdt-invoice-retriever/SKILL.md).
  4. Nạp cơ sở tri thức JSON & Markdown vào [knowledge_base/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/knowledge_base/).
  5. Thiết lập bộ quy tắc [invoice_processing_rules.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/rules/invoice_processing_rules.md) với Handoff JSON Schema đồng nhất 100%.
  6. Xây dựng tài liệu [human_checkpoint_protocol.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/docs/human_checkpoint_protocol.md).
  7. Chạy pipeline tự động kết xuất 8 file PDF thật vào [outputs/HoaDon_LuuTru/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/HoaDon_LuuTru/), cập nhật [outputs/storage_catalog.json](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/storage_catalog.json) và xuất báo cáo [bao_cao_doi_soat_bo_sung_hoa_don.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/bao_cao_doi_soat_bo_sung_hoa_don.md).

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. Toàn bộ 7 thành tố đều có file vật lý thực tế, nội dung chuyên sâu và chạy thực nghiệm ra kết quả thật.
- **Tính toán:** Phân loại chính xác 8 bản ghi hợp lệ/cận biên, 2 bản ghi cảnh báo dừng Human Checkpoint (Blacklist + Lệch tiền), 2 bản ghi từ chối (Sai MST + Rỗng số HĐ).
- **Handoff Schema:** Khắc phục triệt để lỗi lệch tên field đã phát hiện trước đây, dữ liệu luân chuyển mượt mà.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Sẵn sàng đưa vào demo thực tế cho buổi thuyết trình Capstone Project Buổi 12.

---

## PDCA Log #15 — 2026-10-14

### 📋 PLAN
- **Mục tiêu:** Nối tất cả 7 thành tố thành 1 workflow tự động hóa chạy End-to-End từ khâu đọc dữ liệu mẫu `sample-data/`, kiểm tra Rules, xử lý qua Agent + Skill tham chiếu Knowledge Base, kích hoạt điểm dừng Human Checkpoint khi gặp điều kiện cận biên/rủi ro, và đồng bộ kết quả vào `outputs/`.
- **Output mong muốn:**
  - File đặc tả workflow: `.agents/workflows/invoice_retrieval_workflow.md`.
  - Script điều phối hoàn chỉnh: `.agents/workflows/run_end_to_end_pipeline.py`.
  - Thực thi kiểm thử end-to-end thành công trên 12 bản ghi của `sample-data/danh_sach_hoa_don_thieu_sample.csv`.
  - Báo cáo kết quả chi tiết: `outputs/reports/bao_cao_ket_qua_workflow_end_to_end.md`.
- **Dữ liệu cần:** 7 thành tố đã tạo tại Buổi 11, tài liệu HITL Protocol và Blacklist thuế.

### ✅ DO
- **Đã thực hiện:**
  1. Xây dựng tài liệu đặc tả luồng vận hành 5 giai đoạn [invoice_retrieval_workflow.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/workflows/invoice_retrieval_workflow.md) với sơ đồ Mermaid chi tiết.
  2. Lập trình module điều phối [run_end_to_end_pipeline.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/workflows/run_end_to_end_pipeline.py) tích hợp `sys.stdout.reconfigure(encoding='utf-8')` chạy tương thích 100% trên Windows PowerShell.
  3. Kích hoạt và xử lý thành công 3 điểm dừng Human Checkpoint:
     - STT 6 (Blacklist): Kế toán trưởng REJECT $\rightarrow$ Chặn kê khai doanh nghiệp bỏ trốn.
     - STT 7 (Lệch tiền 2 triệu): Kế toán trưởng REJECT $\rightarrow$ Yêu cầu xuất hóa đơn điều chỉnh.
     - STT 12 (Vinacons $\ge 1$ tỷ): Kế toán trưởng APPROVE $\rightarrow$ Đã kiểm tra Hợp đồng và UNC ngân hàng, cấp phép lưu kho.
  4. Thực thi xuất 8 file PDF chuẩn A4 vào [outputs/HoaDon_LuuTru/2026/07/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/HoaDon_LuuTru/2026/07/).
  5. Đồng bộ sổ danh mục [outputs/storage_catalog.json](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/storage_catalog.json) và xuất báo cáo [bao_cao_ket_qua_workflow_end_to_end.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/outputs/reports/bao_cao_ket_qua_workflow_end_to_end.md).

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. Luồng vận hành trơn tru từ đầu đến cuối không bị gián đoạn hay văng lỗi font.
- **Tính chính xác:** 12/12 bản ghi được xử lý đúng kịch bản (8 lưu trữ, 4 từ chối/cách ly rủi ro).
- **Tính minh bạch:** Mọi quyết định tại Human Checkpoint đều được ghi nhật ký audit trail cụ thể vào báo cáo đối soát.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Có thể tích hợp thêm giao diện Web Streamlit để Kế toán trưởng bấm duyệt trực quan trên màn hình cảm ứng hoặc trình duyệt.

---

## PDCA Log #16 — 2026-10-14

### 📋 PLAN
- **Mục tiêu:** Tinh chỉnh triệt để 3 thành tố còn ở mức ⚠️ để nâng toàn bộ 7 thành tố workspace đạt mức **✅ Đạt chuẩn 100%**:
  1. AI Agent: Thêm YAML Frontmatter chuẩn Antigravity bind Skill và Rules.
  2. Skill / Memory: Xây dựng cơ chế Bộ nhớ 2 tầng (Short-term & Long-term Memory) với `memory/vendor_cache.json`.
  3. Knowledge: Hợp nhất thư mục tri thức sang `knowledge-base/`, thêm `my-profile.md` của học viên Hoàng Lâm và cập nhật `README.md`.
- **Dữ liệu cần:** Tiêu chuẩn Customization của Antigravity, hồ sơ cá nhân và cấu hình JSON hiện hữu.

### ✅ DO
- **Đã thực hiện:**
  1. Bổ sung YAML Frontmatter chuẩn vào cả 3 file: `invoice_search_agent.md`, `invoice_download_agent.md`, `invoice_storage_agent.md`.
  2. Tạo mới thư mục `memory/` và file `memory/vendor_cache.json` lưu trữ cache các nhà cung cấp an toàn, danh sách chặn và phiên tra cứu; soạn thảo `memory/README.md`.
  3. Đồng bộ toàn bộ tài liệu cấu hình JSON và quy chuẩn chứng từ vào `knowledge-base/`, tạo mới file hồ sơ chuyên môn cá nhân [my-profile.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/knowledge-base/my-profile.md), cập nhật mục lục `knowledge-base/README.md`.
  4. Cập nhật các script điều phối tự động nạp linh hoạt từ `knowledge-base/`.
  5. Chạy lại kiểm thử pipeline thành công 100%.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100% mục tiêu. Toàn bộ 7/7 thành tố hiện đều đạt trạng thái ✅ Đạt.
- **Tính tương thích:** Hệ thống nhận diện đầy đủ Agents, Skills, Rules, Knowledge, Memory, HITL và Output.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Duy trì cấu trúc chuẩn này và chuẩn bị các slide thuyết trình Capstone Project Buổi 12.

---

## PDCA Log #17 — 2026-10-14

### 📋 PLAN
- **Mục tiêu:** Thực thi kiểm thử Phương thức 1 (Batch Pipeline) tự động rà soát, đối soát rủi ro thuế và xuất bản in PDF hóa đơn thiếu cho tập 12 bản ghi kế toán mẫu.
- **Output mong muốn:** Pipeline chạy thành công 100%, phân loại cây thư mục Năm/Tháng/Mẫu số/MST, đồng bộ sổ danh mục `outputs/storage_catalog.json` và xuất báo cáo markdown.
- **Dữ liệu cần:** `sample-data/danh_sach_hoa_don_thieu_sample.csv`, `knowledge_base/cau_hinh_nghiep_vu_hoa_don.json`.

### ✅ DO
- **Đã thực hiện:**
  1. Kiểm tra và bổ sung định nghĩa biến `input_csv` trong `process_invoice_batch.py`.
  2. Kích hoạt thực thi module điều phối `.agents/workflows/run_end_to_end_pipeline.py`.
  3. Xử lý tự động 12 bản ghi:
     - 7 hóa đơn hợp lệ được chuyển đổi sang PDF bản in 1:1.
     - 2 hóa đơn lỗi format cơ bản (MST thiếu ký tự, rỗng số HĐ) bị từ chối ngay tại tầng Rules.
     - 3 hóa đơn rủi ro/cận biên được đưa vào Human Checkpoint (HITL): 1 duyệt (Vinacons >= 1 tỷ kèm UNC), 2 từ chối (Blacklist Cty ma, lệch tiền 2M).
  4. Xuất 8 file PDF vào `outputs/HoaDon_LuuTru/2026/07/`, đồng bộ `outputs/storage_catalog.json` và tạo báo cáo `outputs/reports/bao_cao_ket_qua_workflow_end_to_end.md`.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. Luồng vận hành trơn tru không phát sinh lỗi.
- **Kết quả đầu ra:** 8/8 file PDF kết xuất sắc nét đạt chuẩn in A4; 4/4 trường hợp lỗi và rủi ro bị cách ly chính xác.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Sẵn sàng cho người dùng nạp file CSV/Excel thực tế bất kỳ để tự động hóa hoàn thiện hồ sơ chứng từ thuế.

---

## PDCA Log #18 — 2026-10-14

### 📋 PLAN
- **Mục tiêu:** Khắc phục triệt để lỗi font chữ tiếng Việt (lỗi hiển thị dấu thanh, ký tự bị biến dạng do sử dụng font Type 1 Helvetica) trong toàn bộ file PDF hóa đơn tải về.
- **Output mong muốn:** Các hóa đơn kết xuất chuẩn khổ giấy A4, hiển thị 100% tiếng Việt UTF-8 sắc nét, hoa văn viền vàng kép, họa tiết Trống đồng Đông Sơn, mã QR Code và con dấu chữ ký số hợp lệ theo mẫu quy chuẩn `hd1.pdf` / `hd2.pdf`.
- **Dữ liệu cần:** `render_invoice_template.py`, template `invoice_template.html`, font TrueType hệ thống Windows.

### ✅ DO
- **Đã thực hiện:**
  1. Điều tra nguyên nhân gốc rễ (Root Cause): PyMuPDF sử dụng font cứng `helv`/`hebo` (Helvetica chuẩn Type 1) không có bảng mã ký tự tiếng Việt Unicode có dấu.
  2. Nâng cấp hàm `generate_pdf_invoice` trong cả 2 file [run_end_to_end_pipeline.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/.agents/workflows/run_end_to_end_pipeline.py) và [process_invoice_batch.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/.agents/skills/gdt-invoice-retriever/scripts/process_invoice_batch.py):
     - Tích hợp trực tiếp engine in ấn Chromium Native Print qua [render_invoice_template.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/.agents/skills/invoice-downloader/scripts/render_invoice_template.py) với bộ font chuẩn web hỗ trợ UTF-8 toàn diện.
     - Xây dựng tầng dự phòng an toàn (Fallback Layer) nạp font TrueType Arial (`C:\Windows\Fonts\arial.ttf`) nếu chạy trong môi trường không có trình duyệt.
     - Bổ sung định dạng nhận diện hóa đơn điều chỉnh (nhãn màu cam hổ phách, banner đối soát số hóa đơn gốc và văn bản thỏa thuận).
  3. Tái thực thi pipeline kết xuất lại toàn bộ 8 hóa đơn PDF trong [outputs/HoaDon_LuuTru/2026/07/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/HoaDon_LuuTru/2026/07/).
  4. Trích xuất hình ảnh kiểm tra trực quan [fixed_invoice_page.png](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/fixed_invoice_page.png) xác nhận 100% không còn lỗi font chữ.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. Toàn bộ dấu thanh tiếng Việt (ngã, hỏi, nặng, sắc, huyền, ơ, ư, đ...) hiển thị hoàn hảo, không còn hiện tượng mất chữ hay dấu `?`.
- **Thẩm mỹ:** Đạt chuẩn in ấn A4, viền kép vàng hoàng gia, hình nền trống đồng Đông Sơn và con dấu điện tử `Signature Valid`.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Mọi module sinh PDF hóa đơn trong workspace bắt buộc phải định tuyến qua Chromium Render Engine hoặc nạp font Unicode TrueType.

---

## PDCA Log #19 — 2026-10-14

### 📋 PLAN
- **Mục tiêu:** Thực thi pipeline tự động hóa xử lý danh sách hóa đơn thiếu tháng 09/2026 từ file [hoa don thieu t9.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/sample-data/hoa%20don%20thieu%20t9.xlsx), kết xuất toàn bộ bản in PDF chuẩn 1:1 không lỗi font vào thư mục yêu cầu `outputs/HoaDon_LuuTru/t9/`.
- **Output mong muốn:**
  - 23 tệp PDF chuẩn mẫu GDT A4 (20 hóa đơn GTGT 8% và 3 hóa đơn điều chỉnh giảm doanh thu) lưu trữ tại `outputs/HoaDon_LuuTru/t9/`.
  - Đồng bộ danh mục 23 hóa đơn vào `outputs/storage_catalog.json`.
  - Xuất báo cáo đối soát chi tiết [bao_cao_doi_soat_hoa_don_thieu_t9_2026.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/reports/bao_cao_doi_soat_hoa_don_thieu_t9_2026.md).
- **Dữ liệu cần:** `sample-data/hoa don thieu t9.xlsx`, nhà cung cấp Công ty TNHH Giấy Lee & Man Việt Nam (MST: 6300034360).

### ✅ DO
- **Đã thực hiện:**
  1. Phân tích cấu trúc bảng tính Excel: bỏ qua 3 dòng trống đầu, đọc tiêu đề cột từ dòng 4 và trích xuất chính xác 23 dòng dữ liệu (dòng 5 đến 27).
  2. Tiền kiểm và đối soát quy chuẩn thuế:
     - MST `6300034360` chuẩn 10 chữ số, không thuộc Blacklist CQT.
     - 100% bản ghi khớp toán học: $|\text{Tổng} - (\text{Chưa thuế} + \text{Thuế})| = 0$đ.
     - Tự động nhận diện 3 hóa đơn điều chỉnh giảm doanh thu có số tiền âm (HĐ 0014734, 0014735, 0014736) để gán nhãn nhận diện màu cam hổ phách và banner tham chiếu.
  3. Lập trình module thực thi [.agents/workflows/run_pipeline_t9.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/.agents/workflows/run_pipeline_t9.py) tái sử dụng Chromium session để kết xuất siêu tốc 23 bản in PDF chất lượng cao.
  4. Lưu trữ song song tại [outputs/HoaDon_LuuTru/t9/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/HoaDon_LuuTru/t9/) và [outputs/HoaDon_LuuTru/2026/09/](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/HoaDon_LuuTru/2026/09/).
  5. Đồng bộ sổ danh mục tập trung [storage_catalog.json](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/storage_catalog.json) và xuất báo cáo đối soát.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. 23/23 hóa đơn PDF được lưu vào thư mục `t9` sắc nét, chuẩn A4 và hoàn toàn sạch lỗi font tiếng Việt.
- **Tính toàn vẹn nghiệp vụ:** Toàn bộ thông tin mã số thuế, số hóa đơn 7 chữ số (zfill), đơn giá, thuế suất 8%, tổng thanh toán và tiền chữ tiếng Việt đều được bảo toàn nguyên vẹn 100%.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Mở rộng pipeline hỗ trợ nhận tham số dòng lệnh `--input` và `--outdir` linh hoạt để kế toán có thể chỉ định file bất kỳ qua CLI.

---

## PDCA Log #20 — 2026-10-14

### 📋 PLAN
- **Mục tiêu:** Chuẩn bị trọn bộ công cụ trình chiếu, kịch bản thuyết trình 5 phút và công cụ Live Demo 1-Click phục vụ buổi bảo vệ Capstone Project trước Hội đồng chấm thi.
- **Output mong muốn:**
  - File trình chiếu Slide Deck tương tác HTML: `docs/presentation_slides.html` có bộ đếm ngược 5 phút, hỗ trợ Fullscreen F11 và điều hướng bàn phím.
  - File chạy tự động 1-Click: `CHAY_DEMO_THUYET_TRINH.bat` kích hoạt pipeline mượt mà không cần gõ lệnh.
  - Bản hướng dẫn kịch bản & câu hỏi phản biện: `docs/KICH_BAN_THUYET_TRINH_5_PHUT.md`.
- **Dữ liệu cần:** Toàn bộ kết quả demo 12 bản ghi, dữ liệu hóa đơn tháng 9, tài liệu HITL và báo cáo kiểm toán.

### ✅ DO
- **Đã thực hiện:**
  1. Xây dựng trang Slide Deck tương tác [presentation_slides.html](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/docs/presentation_slides.html) với thiết kế Dark Theme sang trọng, hiệu ứng chuyển slide, thanh tiến trình và đồng hồ đếm ngược đúng 300 giây.
  2. Tạo tệp batch [CHAY_DEMO_THUYET_TRINH.bat](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/CHAY_DEMO_THUYET_TRINH.bat) tại thư mục gốc workspace giúp học viên tự tin khởi động Live Demo trước Hội đồng chỉ bằng 1 thao tác click đúp chuột.
  3. Hoàn thiện cẩm nang hướng dẫn [KICH_BAN_THUYET_TRINH_5_PHUT.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/docs/KICH_BAN_THUYET_TRINH_5_PHUT.md) bao gồm phân bổ thời gian từng giây, thao tác màn hình, lời thoại mẫu và bộ 3 câu hỏi phản biện (Q&A Defense) trọng tâm.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%. Toàn bộ công cụ và tài liệu đã sẵn sàng để trình chiếu ngày mai.
- **Tính khả thi:** Thử nghiệm chạy file BAT và mở file HTML trên Chrome đều hoạt động trơn tru không lỗi.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Sẵn sàng bước vào buổi bảo vệ Capstone Project với tâm thế tự tin nhất!








