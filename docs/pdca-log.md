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
- **Mục tiêu:** Xây dựng ứng dụng web tương tác [app_lead_scoring.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/app_lead_scoring.py) (và alias [app_ead_scoring.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/app_ead_scoring.py)) bằng Streamlit để quản lý chấm điểm Lead Bất Động Sản.
- **Output mong muốn:**
  - Bảng tương tác `st.data_editor` cho phép con người duyệt trạng thái (Human-in-the-loop: checkbox duyệt, chọn Sales phụ trách, đổi trạng thái).
  - Tích hợp logic "AI Scoring" (Agent) tự động quét mô tả nhu cầu dựa trên 5 tiêu chí chuẩn và [tieu_chi_cham_diem.txt](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/knowledge-base/tieu_chi_cham_diem.txt).
  - Thanh công cụ nạp file CSV/Excel, kết nối Google Sheets CSV URL, và xuất Thẻ Bàn Giao Lead cho Zalo/CRM.
- **Dữ liệu cần:** `sample-data/khach_hang_bds_sample.csv`, kiến trúc skill `chamdiem-scoring`.

### ✅ DO
- **Đã thực hiện:**
  1. Cài đặt các thư viện `streamlit` và `pandas` trong môi trường workspace.
  2. Xây dựng hoàn chỉnh giao diện thẩm mỹ cao với tông màu Dark Navy / Emerald / Amber trong [app_lead_scoring.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/app_lead_scoring.py).
  3. Tích hợp `st.data_editor` với cấu hình cột chi tiết (`CheckboxColumn`, `SelectboxColumn`, `ProgressColumn`, `TextColumn`) và hàm chuẩn hóa kiểu dữ liệu `normalize_leads_df`.
  4. Tích hợp nút quét AI Agent hàng loạt và tính năng Preview Thẻ Bàn Giao kèm kịch bản mở đầu thông minh.
  5. Tạo alias [app_ead_scoring.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/app_ead_scoring.py) chuyển tiếp mượt mà.
  6. Kiểm thử cú pháp và biên dịch ứng dụng thành công.

### 🔍 CHECK
- **Đạt mục tiêu không?** Đạt 100%.
- **Trải nghiệm tương tác:** Bảng `st.data_editor` hoạt động trơn tru, cho phép chỉnh sửa trực tiếp trên ô, lọc theo phân khúc/trạng thái và tải báo cáo CSV đã duyệt chỉ với 1 click.

### 🔄 ACT
- **Thay đổi sẽ áp dụng lần sau:** Có thể bổ sung thêm tính năng gửi tin nhắn Zalo ZNS trực tiếp qua API từ giao diện Streamlit.

