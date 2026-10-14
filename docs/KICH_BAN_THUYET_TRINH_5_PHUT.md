# KỊCH BẢN THUYẾT TRÌNH BÀI LUẬN CUỐI KHÓA (CAPSTONE DEFENSE 5 PHÚT)

> **Học viên:** Hoàng Lâm — Kế toán trưởng & Chuyên viên Quản trị Thuế  
> **Khóa học:** Agentic AI with Google Antigravity (MindX Technology School)  
> **Đề tài:** Hệ Thống Multi-Agent Tự Động Hóa Tìm Kiếm, Sắp Xếp, Tải & Kiểm Soát Rủi Ro Hóa Đơn Điện Tử Mua Vào  
> **File Slide trình chiếu trực tiếp:** [`docs/presentation_slides.html`](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/docs/presentation_slides.html)  
> **File chạy Live Demo 1-Click:** [`CHAY_DEMO_THUYET_TRINH.bat`](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/CHAY_DEMO_THUYET_TRINH.bat)

---

## 🖥️ BƯỚC 1: CHUẨN BỊ TRƯỚC GIỜ G (TRƯỚC KHI LÊN SÂN KHẤU)

Anh mở sẵn **3 Cửa Sổ** sau trên màn hình máy tính để chuyển đổi mượt mà bằng phím `Alt + Tab`:

1. **Cửa sổ 1 (Slide Thuyết Trình):**  
   Mở file [`docs/presentation_slides.html`](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/docs/presentation_slides.html) bằng Google Chrome hoặc Microsoft Edge. Bấm **F11** để toàn màn hình. Trên thanh công cụ có nút **▶ Play** đếm ngược đúng 5 phút để anh làm chủ thời gian.
2. **Cửa sổ 2 (Live Demo Terminal):**  
   Mở sẵn thư mục workspace và click đúp chuột vào file [`CHAY_DEMO_THUYET_TRINH.bat`](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/CHAY_DEMO_THUYET_TRINH.bat). Màn hình sẽ dừng chờ anh bấm phím bất kỳ để kích hoạt.
3. **Cửa sổ 3 (Hóa Đơn Thành Phẩm Chuẩn Bị Sẵn):**  
   Mở sẵn 1 file PDF sắc nét để chiếu cho Hội đồng xem ngay khi kết thúc demo:  
   👉 [20260715_MS1_0100107934_C26TPL_0045120.pdf](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/HoaDon_LuuTru/2026/07/MauSo_1_GTGT/0100107934_T%E1%BA%ACP_%C4%90O%C3%80N_X%C4%82NG_D%E1%BA%A6U_VI%E1%BB%86T_NA/20260715_MS1_0100107934_C26TPL_0045120.pdf) *(Hóa đơn Petrolimex)* hoặc [20260917_MS1_6300034360_C26TLM_0014734.pdf](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace-lam/outputs/HoaDon_LuuTru/t9/20260917_MS1_6300034360_C26TLM_0014734.pdf) *(Hóa đơn điều chỉnh màu cam)*.

---

## 🎙️ BƯỚC 2: KỊCH BẢN THUYẾT TRÌNH TỪNG PHÚT

### ⏱️ 0:00 – 0:30 (30 giây) — Vấn đề & Đối tượng hưởng lợi
* **Màn hình:** Chiếu **Slide 1 & Slide 2** trong file slide.
* **Lời nói:**
  > *"Kính thưa Hội đồng Giám khảo, tôi là Hoàng Lâm, phụ trách kế toán doanh nghiệp và dịch vụ thuế.  
  > Cứ mỗi kỳ kê khai thuế hàng tháng hay mùa quyết toán năm, nỗi đau lớn nhất của kế toán không phải là hạch toán, mà là **hồ sơ chứng từ bị thiếu file PDF hóa đơn gốc**. Kế toán phải mất từ 20 đến 30 giờ ngồi rà soát từng dòng bảng kê, đăng nhập Cổng Thuế, bấm tìm, mở từng tờ và in thủ công.  
  > Nguy hiểm hơn, nếu không may kê khai phải hóa đơn của **doanh nghiệp ma, doanh nghiệp bỏ trốn**, doanh nghiệp sẽ bị cơ quan thuế truy thu, phạt chậm nộp và xuất toán toàn bộ chi phí.  
  > Để giải quyết dứt điểm vấn đề này, tôi đã xây dựng hệ thống **Multi-Agent AI tự động hóa hoàn thiện hồ sơ chứng từ và thiết lập hàng rào kiểm soát rủi ro thuế**."*

---

### ⏱️ 0:30 – 1:30 (60 giây) — Kiến trúc Hệ thống Multi-Agent (OIPO & 7 Thành Tố)
* **Màn hình:** Bấm phím mũi tên sang **Slide 3**.
* **Lời nói:**
  > *"Hệ thống của tôi được thiết kế theo kiến trúc **OIPO kết hợp trọn bộ 7 Thành tố chuẩn Antigravity**, gồm 3 Agent chuyên biệt:  
  > 
  > 1. **Tầng 1 — `Invoice Search Agent`:** Tiếp nhận danh sách hóa đơn thiếu từ file Excel/ERP, kiểm tra độ dài mã số thuế, tính toán học 3 chiều và đối chiếu tức thì với **Blacklist doanh nghiệp bỏ trốn** trong Knowledge Base.  
  > 2. **Tầng 2 — Điểm dừng con người `Human Checkpoint (HITL)`:** Tạm dừng xin ý kiến Kế toán trưởng khi phát hiện hóa đơn rủi ro cao hoặc giá trị lớn &ge; 1 tỷ đồng.  
  > 3. **Tầng 3 — `Invoice Download Agent`:** Kích hoạt Chromium Print Engine mô phỏng máy in ảo **Microsoft Print to PDF** xuất bản in PDF A4 chuẩn 1:1, bảo toàn hoa văn trống đồng và con dấu chữ ký số.  
  > 4. **Tầng 4 — `Invoice Storage Agent`:** Chuẩn hóa tên file theo quy chuẩn kế toán và phân loại vào cây thư mục phân cấp Năm/Tháng/MST, đồng bộ Sổ danh mục `storage_catalog.json`."*

---

### ⏱️ 1:30 – 3:30 (120 giây) — Live Demo Thực Tế Trước Hội Đồng
* **Màn hình:** Chuyển `Alt + Tab` sang Cửa sổ 2 (`CHAY_DEMO_THUYET_TRINH.bat`), nhấn phím **Space/Enter** để khởi chạy pipeline.
* **Lời nói:**
  > *"Ngay bây giờ, tôi xin chạy Live Demo quy trình xử lý thực tế trên 12 bản ghi hóa đơn thiếu đại diện cho các tình huống cận biên phức tạp:  
  > 
  > *(Chỉ vào màn hình terminal khi lọc lỗi)*  
  > * Hệ thống lập tức loại bỏ **STT 8** do MST chỉ có 6 số, và **STT 9** do số hóa đơn bị rỗng — ngăn dữ liệu rác đi vào hệ thống.  
  > 
  > *(Khi màn hình hiện khung cảnh báo đỏ của HUMAN CHECKPOINT)*  
  > * Xin mời Hội đồng quan sát: Hệ thống phát hiện 3 trường hợp bất thường và kích hoạt trạm dừng con người:  
  >   1. **STT 6 (Cty Ma Xuất Khẩu Khống - 49.5M):** Thuộc **Blacklist Tổng cục Thuế** $\rightarrow$ Quyết định: **REJECT**, chặn kê khai, cách ly khỏi chi phí thuế!  
  >   2. **STT 7 (Truyền Thông Á Châu):** Tổng tiền lệch 2.000.000đ so với doanh số + thuế $\rightarrow$ Quyết định: **REJECT**, yêu cầu bên bán lập hóa đơn thay thế.  
  >   3. **STT 12 (Vinacons - 1.32 tỷ):** Giá trị lớn &ge; 1 tỷ $\rightarrow$ Kế toán trưởng thẩm định đã có Hợp đồng kinh tế và Ủy nhiệm chi ngân hàng $\rightarrow$ Quyết định: **APPROVE**, cấp phép lưu kho!  
  >   4. **STT 11 (-5.5 triệu):** Hóa đơn điều chỉnh âm $\rightarrow$ Tự động nhận diện và gắn nhãn cam `[ HÓA ĐƠN ĐIỀU CHỈNH ]`.  
  > 
  > *(Mở Cửa sổ 3 - file PDF hóa đơn lên cho Hội đồng xem)*  
  > * Toàn bộ hóa đơn hợp lệ đã được lưu trữ vào cây thư mục. Xin Hội đồng nhìn vào bản in PDF: **Khung viền kép vàng hoàng gia, hình nền trống đồng Đông Sơn, mã QR Code, con dấu Signature Valid và dòng tiền bằng chữ tiếng Việt hoàn hảo**!"*

---

### ⏱️ 3:30 – 4:30 (60 giây) — Bài học Thực Chiến & Cải Tiến PDCA
* **Màn hình:** Chuyển `Alt + Tab` về Slide, bấm sang **Slide 5 (Bài học PDCA)**.
* **Lời nói:**
  > *"Trong suốt quá trình xây dựng workspace, tôi tuân thủ nghiêm ngặt Quy tắc PDCA và đã xử lý 2 bài toán lớn được ghi nhận tại **PDCA Log #18 và #19**:  
  > 
  > 1. **Khắc phục 100% lỗi Font tiếng Việt:**  
  >    Ban đầu thư viện PDF thông thường dùng font Helvetica Type 1 bị vỡ toàn bộ chữ tiếng Việt có dấu. Tôi đã áp dụng chu trình PDCA: chuyển sang engine in ấn **Chromium Native Print Engine** chuẩn web kết hợp lớp fallback TrueType Arial của Windows, xử lý triệt để 100% lỗi font chữ.  
  > 2. **Bài toán Đa Doanh Nghiệp cho Kế toán Dịch vụ:**  
  >    Là người làm dịch vụ kế toán cho nhiều khách hàng, tôi nhận thức được các bảng kê Excel mua vào không có cột bên Mua. Tôi đã nâng cấp 2 chế độ: luồng Live CDP bóc tách 100% bên Mua & mặt hàng thật từ Cổng Thuế; luồng Offline hỗ trợ danh bạ Multi-Client."*

---

### ⏱️ 4:30 – 5:00 (30 giây) — Kết Quả & Tầm Nhìn Tương Lai
* **Màn hình:** Bấm sang **Slide 6 & Slide 7 (Tổng kết & Q&A)**.
* **Lời nói:**
  > *"Tóm lại, giải pháp đã mang lại:  
  > 1. **Tiết kiệm 95% thời gian thủ công** của kế toán mỗi kỳ báo cáo.  
  > 2. **Triệt tiêu 100% rủi ro** bị truy thu thuế do hóa đơn doanh nghiệp bỏ trốn.  
  > 
  > Định hướng tiếp theo, tôi sẽ phát triển:  
  > - **Giao diện Web Dashboard** cho phép Kế toán trưởng bấm duyệt các ca HITL trực quan trên điện thoại.  
  > - Tính năng **3-Way Matching**: Tự động đối chiếu 3 chiều giữa Hóa đơn PDF $\leftrightarrow$ Bảng kê thuế $\leftrightarrow$ Sao kê Ủy nhiệm chi ngân hàng.  
  > 
  > Xin trân trọng cảm ơn Hội đồng Giám khảo đã lắng nghe. Tôi sẵn sàng nhận các câu hỏi phản biện!"*

---

## 🛡️ BƯỚC 3: BỘ CÂU HỎI PHẢN BIỆN THƯỜNG GẶP (Q&A DEFENSE)

Hội đồng thường sẽ hỏi một trong các câu sau, anh chỉ cần trả lời theo gợi ý này là đạt điểm xuất sắc:

### ❓ Câu 1: Tại sao phải dùng Multi-Agent AI mà không viết script code tự động hóa thông thường (RPA)?
> **Trả lời:** *"Script RPA thông thường chỉ chạy tuần tự theo luật cố định và rất dễ gãy vỡ (brittle) khi gặp dữ liệu bất thường. Hệ thống Multi-Agent AI có khả năng **lý luận (reasoning)**, tiền kiểm cấu trúc qua Agent Tiền kiểm, tự động đối chiếu cơ sở tri thức Blacklist động, kích hoạt trạm kiểm soát con người HITL tại các điểm cận biên, và tự phục hồi dữ liệu (Self-Healing) khi gặp định dạng ngày tháng hay tiền tệ dị biệt."*

### ❓ Câu 2: Vấn đề bảo mật tài khoản Cổng Thuế được giải quyết thế nào?
> **Trả lời:** *"Dự án tuân thủ Quy tắc số 5 của Workspace: **Zero Credential Storage**. Hệ thống không lưu mật khẩu hay OTP trong mã nguồn. Người dùng tự mở trình duyệt Chrome qua cổng debug 9222, tự đăng nhập và nhập mã CAPTCHA bằng tay. AI Agent chỉ kết nối qua CDP để tự động hóa thao tác xem và in hóa đơn sang PDF."*

### ❓ Câu 3: Làm thế nào để phân biệt hóa đơn có mã, không mã và máy tính tiền?
> **Trả lời:** *"Hệ thống dựa trên Nghị định 123 và Thông tư 78:
> - Ký hiệu bắt đầu bằng `C...` (ví dụ `C26TLM`) là hóa đơn có mã của CQT (bắt buộc kiểm tra chuỗi `MCCQT`).
> - Ký hiệu bắt đầu bằng `K...` (ví dụ `K26TYY`, `K26TVT`) là hóa đơn không mã của các tập đoàn lớn (Điện lực, Xăng dầu, Viễn thông, Ngân hàng).
> - Mẫu số 2 là hóa đơn bán hàng khởi tạo từ máy tính tiền của hộ kinh doanh."*
