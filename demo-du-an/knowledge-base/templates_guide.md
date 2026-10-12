# HƯỚNG DẪN NHẬN DIỆN CÁC MẪU HÓA ĐƠN ĐIỆN TỬ MUA VÀO (THEO NGHỊ ĐỊNH 123)

---

## 1. MẪU SỐ 1 — HÓA ĐƠN GIÁ TRỊ GIA TĂNG (CÓ MÃ CƠ QUAN THUẾ)
* **Ký hiệu mẫu:** `Mẫu số 1` (Thẻ XML: `<KHMSHDon>1</KHMSHDon>`)
* **Ký hiệu hóa đơn:** Bắt đầu bằng chữ `C` (Ví dụ: `C26TCK`).
  * `C`: Có mã của cơ quan thuế.
  * `26`: Năm lập hóa đơn (2026).
  * `T`: Hóa đơn điện tử do doanh nghiệp, tổ chức phát hành.
  * `CK`: Ký tự quản lý nội bộ người bán.
* **Đặc điểm thuế:** Có tách biệt rõ ràng Doanh số chưa thuế, Thuế suất GTGT (5%, 8%, 10%), Tiền thuế GTGT và Tổng tiền thanh toán.
* **Mã CQT:** Bắt buộc có mã băm cơ quan thuế cấp (`MCCQT`).

---

## 2. MẪU SỐ 1 — HÓA ĐƠN GIÁ TRỊ GIA TĂNG (KHÔNG CÓ MÃ CƠ QUAN THUẾ)
* **Ký hiệu mẫu:** `Mẫu số 1` (Thẻ XML: `<KHMSHDon>1</KHMSHDon>`)
* **Ký hiệu hóa đơn:** Bắt đầu bằng chữ `K` (Ví dụ: `K26TYY`).
  * `K`: Không có mã của cơ quan thuế (Doanh nghiệp đủ điều kiện tự truyền dữ liệu lên CQT, ví dụ: Ngân hàng ACB, Viettel, VNPT, Điện lực EVN).
  * `26`: Năm lập hóa đơn (2026).
  * `T`: Hóa đơn do tổ chức/doanh nghiệp phát hành.
* **Mã CQT:** Thẻ `<MCCQT>` để trống.

---

## 3. MẪU SỐ 2 — HÓA ĐƠN BÁN HÀNG (DÀNH CHO HỘ KINH DOANH / NỘP THUẾ TRỰC TIẾP)
* **Ký hiệu mẫu:** `Mẫu số 2` (Thẻ XML: `<KHMSHDon>2</KHMSHDon>`)
* **Ký hiệu hóa đơn:** Bắt đầu bằng `C...M...` (Ví dụ: `C26MYY`).
  * `C`: Có mã của cơ quan thuế.
  * `26`: Năm 2026.
  * `M`: Hóa đơn điện tử khởi tạo từ máy tính tiền hoặc HĐ bán hàng trực tiếp.
* **Đặc điểm thuế:** **KHÔNG CÓ** dòng tiền thuế GTGT riêng. Số tiền thanh toán là tổng giá thanh toán của hàng hóa, dịch vụ.
