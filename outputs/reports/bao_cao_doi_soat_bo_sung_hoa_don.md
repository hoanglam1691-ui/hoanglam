# BÁO CÁO ĐỐI SOÁT & HOÀN THIỆN HỒ SƠ HÓA ĐƠN ĐIỆN TỬ MUA VÀO

> **Dự án:** Tìm kiếm, sắp xếp và tải hóa đơn điện tử còn thiếu  
> **Cổng thông tin nguồn:** `hoadondientu.gdt.gov.vn`  
> **Bộ phận thực hiện:** Kế toán Nội bộ & RPA AI Agent Pipeline  
> **Ngày báo cáo:** 2026-10-14  

---

## 1. TỔNG QUAN KẾT QUẢ ĐỐI SOÁT

- **Tổng số hóa đơn tiếp nhận rà soát:** **12** hóa đơn
- **✅ Đã tải và lưu trữ thành công vào kho:** **8** hóa đơn (100% bản in PDF chuẩn 1:1)
- **🛑 Cần Kế toán trưởng thẩm định (Human Checkpoint):** **2** hóa đơn (Rủi ro Blacklist / Lệch toán học)
- **❌ Bị từ chối do dữ liệu không hợp lệ:** **2** hóa đơn (Sai định dạng MST / Rỗng số HĐ)

---

## 2. BẢNG CHI TIẾT TỔNG HỢP THEO TIÊU CHÍ HANDOFF SCHEMA

| STT | Mã Định Danh (UID) | Người Bán | Mẫu & Ký Hiệu | Số HĐ | Ngày Lập | Tổng Thanh Toán | Trạng Thái Pipeline | Ghi Chú Nghiệp Vụ |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0101893254_C26TCK_0000302` | CÔNG TY TNHH PHÁT TRIỂN CƠ K | 1-C26TCK | 0000302 | 2026-07-05 | 18,583,950 đ | `✅ ARCHIVED` | HỢP LỆ: Đã tải và lưu trữ thành công bản in PDF 1:1 |
| 2 | `0301452948_K26TYY_22233849` | NGÂN HÀNG TMCP Á CHÂU (ACB) | 1-K26TYY | 22233849 | 2026-07-10 | 15,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đã tải và lưu trữ thành công bản in PDF 1:1 |
| 3 | `001065008691_C26MYY_0000240` | HỘ KINH DOANH NGUYỄN QUỐC GI | 2-C26MYY | 0000240 | 2026-07-12 | 5,850,000 đ | `✅ ARCHIVED` | HỢP LỆ (Cận biên): Hóa đơn không chịu thuế GTGT hoặc máy tính tiền |
| 4 | `0100107934_C26TPL_0045120` | TẬP ĐOÀN XĂNG DẦU VIỆT NAM ( | 1-C26TPL | 0045120 | 2026-07-15 | 5,000,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đã tải và lưu trữ thành công bản in PDF 1:1 |
| 5 | `0100684740_K26TVT_0891234` | TẬP ĐOÀN CÔNG NGHIỆP - VIỄN  | 1-K26TVT | 0891234 | 2026-07-18 | 1,320,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đã tải và lưu trữ thành công bản in PDF 1:1 |
| 6 | `0109999999_C26TMA_0000105` | CÔNG TY TNHH THƯƠNG MẠI MA X | 1-C26TMA | 0000105 | 2026-07-20 | 49,500,000 đ | `🛑 FLAGGED_HITL` | CẢNH BÁO BLACKLIST: CÔNG TY TNHH THƯƠNG MẠI MA XUẤT KHẨU KHỐNG (Doanh nghiệp có thông báo không hoạt động tại địa chỉ đăng ký (Bỏ trốn)) |
| 7 | `0104863508_C26TYY_0000330` | CÔNG TY CP TRUYỀN THÔNG CÔNG | 1-C26TYY | 0000330 | 2026-07-21 | 18,500,000 đ | `🛑 FLAGGED_HITL` | CẢNH BÁO LỆCH TOÁN HỌC: Tổng thanh toán lệch 2,000,000 VND so với (Chưa thuế + Thuế) |
| 8 | `010258_C26THH_0000512` | CÔNG TY THIẾT BỊ ĐIỆN HẢI HƯ | 1-C26THH | 0000512 | 2026-07-22 | 9,350,000 đ | `❌ REJECTED` | LỖI ĐỊNH DẠNG: MST '010258' không đủ 10, 12 hoặc 14 ký tự |
| 9 | `0108765432_C26TDA_ERR9` | CÔNG TY TNHH VẬT TƯ THIẾT BỊ | 1-C26TDA |  | 2026-07-23 | 27,500,000 đ | `❌ REJECTED` | LỖI THIẾU DỮ LIỆU: Số hóa đơn bị trống |
| 10 | `0312456789_C26TSW_0000889` | CÔNG TY TNHH PHẦN MỀM THÔNG  | 1-C26TSW | 0000889 | 2026-07-25 | 50,000,000 đ | `✅ ARCHIVED` | HỢP LỆ (Cận biên): Hóa đơn không chịu thuế GTGT hoặc máy tính tiền |
| 11 | `0105678912_C26TTL_0000456` | CÔNG TY TNHH CÔNG NGHỆ TỰ ĐỘ | 1-C26TTL | 0000456 | 2026-07-28 | -5,500,000 đ | `✅ ARCHIVED` | HỢP LỆ (Cận biên): Hóa đơn điều chỉnh giảm doanh thu và thuế |
| 12 | `0101234567_C26TVC_0000999` | CÔNG TY TNHH ĐẦU TƯ & XÂY DỰ | 1-C26TVC | 0000999 | 2026-07-30 | 1,320,000,000 đ | `✅ ARCHIVED` | HỢP LỆ (Cận biên): Hóa đơn giá trị lớn >= 1 tỷ, cần kẹp UNC ngân hàng |

---

## 3. DANH SÁCH HÓA ĐƠN CẦN XỬ LÝ TẠI HUMAN CHECKPOINT (HITL)

Kính đề nghị Kế toán trưởng xem xét và phê duyệt xử lý cho các trường hợp bất thường sau:

1. **Bản ghi STT 6:** `0109999999_C26TMA_0000105` — **CÔNG TY TNHH THƯƠNG MẠI MA XUẤT KHẨU KHỐNG**
   - **Số tiền:** 49.500.000 VNĐ
   - **Rủi ro:** Mã số thuế nằm trong Blacklist doanh nghiệp bỏ trốn của Tổng cục Thuế.
   - **Kiến nghị:** Chặn kê khai khấu trừ thuế GTGT; yêu cầu bộ phận mua hàng đối soát biên bản giao nhận thực tế.
2. **Bản ghi STT 7:** `0104863508_C26TYY_0000330` — **CÔNG TY CP TRUYỀN THÔNG CÔNG NGHỆ Á CHÂU**
   - **Số tiền:** 18.500.000 VNĐ (lệch 2.000.000 VNĐ so với doanh số 15M + thuế 1.5M).
   - **Kiến nghị:** Yêu cầu bên bán lập hóa đơn điều chỉnh sai sót số tiền trước khi thanh toán.

---

## 4. CẤU TRÚC LƯU TRỮ CHỨNG TỪ HOÀN TẤT

Toàn bộ các file PDF tải về thành công đã được phân bổ tự động vào thư mục:
```text
outputs/HoaDon_LuuTru/2026/07/
├── MauSo_1_GTGT/
│   ├── 0100107934_TAP_DOAN_XANG_DAU_VIET_N/
│   ├── 0100684740_TAP_DOAN_CONG_NGHIEP_VI/
│   ├── 0101234567_CONG_TY_TNHH_DAU_TU_XAY/
│   ├── 0101893254_CONG_TY_TNHH_PHAT_TRIEN/
│   ├── 0105678912_CONG_TY_TNHH_CONG_NGHE/
│   ├── 0301452948_NGAN_HANG_TMCP_A_CHAU_AC/
│   └── 0312456789_CONG_TY_TNHH_PHAN_MEM_T/
└── MauSo_2_BanHang/
    └── 001065008691_HO_KINH_DOANH_NGUYEN_QU/
```
