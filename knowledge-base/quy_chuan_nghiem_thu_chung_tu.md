# CẨM NANG NGHIỆP VỤ: QUY CHUẨN KIỂM TRA & NGHIỆM THU HÓA ĐƠN ĐIỆN TỬ MUA VÀO

> **Ban hành bởi:** Bộ phận Kế toán & Quản trị Rủi ro Thuế  
> **Áp dụng cho:** Toàn bộ quy trình hoàn thiện hồ sơ chứng từ thanh toán và lưu trữ dữ liệu thuế

---

## 1. PHÂN BIỆT CÁC MẪU HÓA ĐƠN ĐIỆN TỬ THEO NGHỊ ĐỊNH 123/2020/NĐ-CP

### 1.1. Mẫu số 1: Hóa đơn Giá trị Gia tăng (VAT Invoice)
- **Ký hiệu mẫu số:** `1` (Ví dụ ký hiệu: `C26TCK`, `K26TYY`).
- **Đặc điểm cốt lõi:** Bắt buộc phải có dòng phân tách rõ ràng:
  - Doanh số chưa có thuế GTGT (`tgtttbso`).
  - Thuế suất GTGT (0%, 5%, 8%, 10% hoặc KCT - Không chịu thuế).
  - Tiền thuế GTGT (`tgtthue`).
  - Tổng tiền thanh toán đã bao gồm thuế (`tgtttoan`).
- **Phân loại có mã vs không có mã:**
  - `C...`: Có mã của Cơ quan thuế (bắt buộc có chuỗi `MCCQT` 34 ký tự).
  - `K...`: Không có mã của Cơ quan thuế (doanh nghiệp lớn như Điện lực EVN, Xăng dầu, Viễn thông, Ngân hàng được phép tự truyền dữ liệu lên CQT).

### 1.2. Mẫu số 2: Hóa đơn Bán hàng (Sales Invoice)
- **Ký hiệu mẫu số:** `2` (Ví dụ ký hiệu: `C26MYY`).
- **Đối tượng áp dụng:** Hộ kinh doanh, cá nhân kinh doanh hoặc doanh nghiệp nộp thuế GTGT theo phương pháp trực tiếp trên doanh thu.
- **Đặc điểm cốt lõi:** **KHÔNG CÓ TIỀN THUẾ GTGT RIÊNG**. Tổng giá thanh toán là giá cuối cùng đã bao gồm các nghĩa vụ thuế của bên bán.

---

## 2. QUY ĐỊNH VỀ CHỨNG TỪ THANH TOÁN & ĐIỀU KIỆN KHẤU TRỪ THUẾ

Theo Thông tư 78/2021/TT-BTC và Thông tư 219/2013/TT-BTC:
1. **Hóa đơn từ 20 triệu đồng trở lên:**
   - Bắt buộc phải có chứng từ thanh toán không dùng tiền mặt (Ủy nhiệm chi ngân hàng, Giấy báo Nợ).
   - Hóa đơn tải về phải được kẹp chung với Ủy nhiệm chi tương ứng trước khi đóng tập lưu trữ.
2. **Hóa đơn điều chỉnh / thay thế:**
   - Phải có Biên bản thỏa thuận điều chỉnh/thu hồi hóa đơn giữa hai bên mua bán.
   - Khi lưu trữ, hệ thống tự động lưu file bản in với hậu tố `_v2.pdf` và ghi chú rõ số hóa đơn gốc bị điều chỉnh.
3. **Xử lý doanh nghiệp có rủi ro cao về thuế (Blacklist):**
   - Nghiêm cấm đưa vào bảng kê khai thuế các hóa đơn phát hành sau ngày cơ quan thuế ra thông báo doanh nghiệp bỏ trốn hoặc tạm ngừng kinh doanh.
   - Mọi hóa đơn có MST nằm trong Blacklist bắt buộc phải dừng lại tại Human Checkpoint để Kế toán trưởng đối soát thực tế hàng hóa, dịch vụ và hợp đồng kinh tế.
