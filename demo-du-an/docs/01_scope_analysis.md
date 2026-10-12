# PHÂN TÍCH ĐỀ BÀI DỰ ÁN THEO KHUNG SCOPE

**Đề tài:** Hệ thống Tự động hóa tìm kiếm, tải và lưu giữ hoá đơn mua vào thông qua Cổng thông tin Tổng cục Thuế (`hoadondientu.gdt.gov.vn`)  
**Khung phương pháp:** SCOPE Framework *(Situation – Constraints – Objectives – Process – Evaluation)*

---

## 1. S — Situation (Thực Trạng & Điểm Nghẽn Vận Hành)

### 1.1. Bối cảnh chung
Theo **Nghị định 123/2020/NĐ-CP** và **Thông tư 78/2021/TT-BTC**, 100% doanh nghiệp tại Việt Nam bắt buộc sử dụng Hóa đơn điện tử (HĐĐT). Cổng thông tin của Tổng cục Thuế (`hoadondientu.gdt.gov.vn`) là nguồn dữ liệu chuẩn hóa và chính xác nhất để kiểm soát toàn bộ hóa đơn đầu vào phục vụ kê khai thuế GTGT và quyết toán thuế TNDN.

### 1.2. Hiện trạng quy trình thủ công (As-Is Baseline)
* **Thao tác lặp lại tốn thời gian:** Hàng tuần/tháng, kế toán phải đăng nhập thủ công, giải mã Captcha hình ảnh, lọc từng khoảng thời gian (tối đa 31 ngày/lần tra cứu).
* **Tải file rời rạc:** Nhấp tải từng hóa đơn bao gồm 02 định dạng: **file PDF** (để tra cứu nhanh) và **file XML** (file gốc có chữ ký số hợp lệ theo luật). Với doanh nghiệp có 200 – 1.000 hóa đơn/tháng, nhân sự mất từ **15 – 35 giờ công/tháng** chỉ để thao tác chuột.
* **Đặt tên và lưu trữ phân tán:** File tải về thường có tên mặc định dạng mã hash hoặc chuỗi ký tự khó hiểu, kế toán phải tự đổi tên và tạo thư mục thủ công, dễ dẫn đến thất lạc hoặc nhầm lẫn giữa các kỳ kế toán.

### 1.3. Điểm nghẽn & Rủi ro doanh nghiệp (Pain Points)
| Yếu tố | Thực trạng thủ công | Hệ quả đối với doanh nghiệp |
| :--- | :--- | :--- |
| **Năng suất** | 3 – 5 phút/hóa đơn (Tra cứu, tải, đổi tên, lưu) | Lãng phí nguồn lực trình độ cao vào công việc hành chính cơ học |
| **Độ chính xác** | Bỏ sót hóa đơn phát sinh cuối kỳ hoặc nhà cung cấp xuất chậm | Sai lệch số thuế GTGT được khấu trừ, nộp phạt chậm nộp/kê khai bổ sung |
| **Pháp lý & Toàn vẹn** | Thường chỉ lưu bản PDF, thất lạc file XML gốc | Rủi ro bị loại chi phí khi thanh tra thuế do thiếu file XML nguyên gốc |
| **Tốc độ báo cáo** | Dữ liệu cập nhật chậm (chỉ làm khi đến kỳ kê khai) | Ban Giám đốc không nắm bắt kịp thời chi phí đầu vào theo thời gian thực |

---

## 2. C — Constraints & Boundaries (Ràng Buộc & Ranh Giới Dự Án)

### 2.1. Ràng buộc Kỹ thuật & Hạ tầng (Technical Constraints)
* **Cơ chế chống bot (Captcha):** Hệ thống GDT sử dụng Captcha hình ảnh khi đăng nhập. Giải pháp cần tích hợp mô hình AI OCR / Captcha Solver chuyên biệt hoặc cơ chế duy trì Session Token thông minh.
* **Giới hạn truy vấn (Rate Limiting):** Cổng GDT thường xuyên nghẽn mạng vào các ngày cao điểm (ngày 15–20 hàng tháng). Hệ thống cần cơ chế `retry` ngắt quãng (Exponential Backoff) và điều tiết tốc độ request để tránh bị khóa IP.
* **Quy chuẩn lưu trữ:** Bắt buộc phải tải và bảo toàn nguyên vẹn **cả 2 định dạng (XML + PDF)**. Không can thiệp sửa đổi cấu trúc thẻ XML để đảm bảo tính hợp lệ của chữ ký số.

### 2.2. Ràng buộc Bảo mật & Tuân thủ (Security & Compliance)
* **Bảo mật thông tin đăng nhập:** Tài khoản thuế, mật khẩu, Token không được hardcode vào mã nguồn; phải quản lý qua file biến môi trường (`.env`) hoặc Keyring cục bộ.
* **Lưu trữ dữ liệu nhạy cảm:** Toàn bộ dữ liệu hóa đơn, mã số thuế và số tiền giao dịch chỉ lưu trữ trên môi trường nội bộ doanh nghiệp (Local Workspace / Private Cloud), không gửi qua dịch vụ bên thứ ba không được kiểm chứng.

### 2.3. Ranh giới dự án (In-Scope vs. Non-Goals)
* **In-Scope (Phạm vi thực hiện):**
  * Tự động xác thực đăng nhập và lấy phiên làm việc (Session Management).
  * Tra cứu và lọc danh sách hóa đơn mua vào theo khoảng thời gian linh hoạt.
  * Tải hàng loạt trọn bộ file XML và PDF của từng hóa đơn.
  * Tự động bóc tách thông tin chính (Ngày lập, MST người bán, Tên nhà cung cấp, Tổng tiền, Tiền thuế).
  * Tự động chuẩn hóa tên file và cấu trúc thư mục lưu trữ khoa học.
  * Xuất Bảng kê tổng hợp (Excel/Google Sheet) và báo cáo nhanh trạng thái.
* **Non-Goals (Ngoài phạm vi - Tránh phình phạm vi dự án):**
  * Không tự động hạch toán vào phần mềm kế toán (MISA, FAST, SAP) mà không qua bước đối soát của người dùng.
  * Không thực hiện tra cứu hóa đơn bán ra (chỉ tập trung hóa đơn mua vào trong pha 1).

---

## 3. O — Objectives (Mục Tiêu & Chỉ Số Đo Lường)

### 3.1. Mục tiêu định lượng (Quantitative KPIs)
1. **Tiết kiệm thời gian:** Rút ngắn thời gian thu thập hóa đơn từ **20 – 30 giờ/tháng xuống dưới 30 phút/tháng** (Giảm > 90%).
2. **Tốc độ tải:** Đạt năng lực xử lý tự động **≥ 50 hóa đơn/phút** (bao gồm tải cả PDF + XML và trích xuất dữ liệu).
3. **Độ chính xác:** Đảm bảo **100% hóa đơn** trên hệ thống GDT được tải về và khớp nối chính xác với Bảng kê tổng hợp (Zero Missed Invoices).
4. **Tỷ lệ giải Captcha thành công:** Đạt **≥ 90%** ngay lần đầu và 100% qua cơ chế tự động thử lại (Auto-Retry).

### 3.2. Mục tiêu định tính (Qualitative Values)
* **Chuẩn hóa quy trình dữ liệu:** Hệ thống hóa cấu trúc lưu trữ thông minh: `HoaDon_MuaVao/YYYY/MM/[MauSo]/[MST_NhaCungCap]/[Ngay]_[MauSo]_[MST]_[KyHieu]_[SoHD].[pdf/xml]`.
* **Sẵn sàng thanh tra & quyết toán:** Khi cơ quan Thuế yêu cầu kiểm tra, kế toán có thể trích xuất hóa đơn bất kỳ chỉ trong **3 giây**.
* **Giải phóng năng lực nhân sự:** Chuyển dịch vai trò kế toán từ "người nhập liệu thủ công" thành "chuyên viên phân tích và kiểm soát rủi ro chi phí".

---

## 4. P — Process & Solution Architecture (Quy Trình Đề Xuất - OIPO)

* **Input:** Tài khoản GDT (`.env`), Khoảng thời gian (From Date - To Date), Thư mục đích.
* **Process:**
  1. *Authentication & Session Init:* Vượt Captcha, lấy Bearer Token phiên làm việc.
  2. *Query & Pagination Handling:* Gửi request lấy toàn bộ danh sách HĐĐT mua vào.
  3. *Concurrent Download Engine:* Tải song song file XML gốc và file PDF hiển thị.
  4. *Data Parsing & Smart Filing:* Bóc tách metadata, chuẩn hóa tên file theo mẫu số.
  5. *Reporting & Notification:* Tạo Bảng kê Excel, cập nhật Catalog và gửi thông báo.
* **Output:** Cây thư mục lưu trữ HĐĐT chuẩn hóa (XML + PDF), Bảng kê Excel, Catalog JSON.

---

## 5. E — Evaluation & Risk Management (Đánh Giá & Quản Trị Rủi Ro)

### 5.1. Tiêu chí nghiệm thu dự án (Acceptance Criteria)
| Hạng mục | Tiêu chí đánh giá (Pass / Fail) | Bằng chứng kiểm tra (Evidence) |
| :--- | :--- | :--- |
| **Tính xác thực** | Tự động đăng nhập và duy trì phiên thành công không cần can thiệp tay | Log kết nối & Token hợp lệ |
| **Tính toàn vẹn** | 100% hóa đơn tra cứu được có đủ cả 2 file `.xml` và `.pdf` tương ứng | Kiểm tra số lượng file trong thư mục đầu ra |
| **Tính chính xác dữ liệu** | Bảng kê Excel khớp 100% các chỉ số (Doanh số, Tiền thuế, MST) so với cổng GDT | Đối chiếu ngẫu nhiên 20 hóa đơn thực tế |
| **Khả năng phục hồi** | Tự động kết nối lại khi mạng lag hoặc GDT timeout mà không làm gián đoạn toàn bộ batch | Test case mô phỏng ngắt kết nối mạng |

### 5.2. Ma trận rủi ro và Phương án giảm thiểu (Risk Matrix)
* **Rủi ro 1: Cổng Thuế thay đổi Captcha hoặc API.** $\rightarrow$ Tách module xử lý Auth thành Adapter độc lập.
* **Rủi ro 2: Nghẽn mạng / GDT trả về lỗi 502/504.** $\rightarrow$ Thiết lập cơ chế Exponential Backoff Retry (2s, 4s, 8s).
* **Rủi ro 3: Trùng lặp hóa đơn giữa các kỳ quét.** $\rightarrow$ Kiểm tra mã hash và UID trước khi tải (Smart Skip).
