# BÁO CÁO KẾT QUẢ THỰC THI WORKFLOW END-TO-END

> **Quy trình:** Tự động hóa Tìm kiếm, Sắp xếp và Tải Hóa đơn Điện tử Mua vào  
> **Cổng thông tin nguồn:** `hoadondientu.gdt.gov.vn`  
> **Ngày vận hành:** 2026-10-14 | **Trạng thái:** Hoàn thành 100%  

---

## 1. TỔNG HỢP KẾT QUẢ VẬN HÀNH 5 GIAI ĐOẠN

- **Tổng số hóa đơn tiếp nhận từ `sample-data/`:** **12** hóa đơn
- **✅ Đã lưu trữ thành công vào cây thư mục (`ARCHIVED`):** **8** hóa đơn (bao gồm 7 hóa đơn hợp lệ + 1 hóa đơn Vinacons $\ge 1$ tỷ đã được duyệt HITL)
- **🛑 Đã xử lý qua Human Checkpoint (HITL):** **3** trường hợp (1 duyệt, 2 từ chối)
- **❌ Tổng số hóa đơn bị loại bỏ (`REJECTED`):** **4** hóa đơn (2 lỗi rules cơ bản + 2 lỗi rủi ro do con người bác bỏ)

---

## 2. BẢNG ĐỐI SOÁT CHI TIẾT 12 HÓA ĐƠN THEO HANDOFF SCHEMA

| STT | Mã Định Danh (UID) | Tên Nhà Cung Cấp | Mẫu & Ký Hiệu | Số HĐ | Ngày Lập | Số Tiền (VNĐ) | Trạng Thái Cuối | Ghi Chú Nghiệp Vụ & Audit Trail |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `0101893254_C26TCK_0000302` | CÔNG TY TNHH PHÁT TRIỂN C | 1-C26TCK | 0000302 | 2026-07-05 | 18,583,950 đ | `✅ ARCHIVED` | HỢP LỆ: Đủ điều kiện tra cứu và tải hóa đơn |
| 2 | `0301452948_K26TYY_22233849` | NGÂN HÀNG TMCP Á CHÂU (AC | 1-K26TYY | 22233849 | 2026-07-10 | 15,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đủ điều kiện tra cứu và tải hóa đơn |
| 3 | `001065008691_C26MYY_0000240` | HỘ KINH DOANH NGUYỄN QUỐC | 2-C26MYY | 0000240 | 2026-07-12 | 5,850,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đủ điều kiện tra cứu và tải hóa đơn |
| 4 | `0100107934_C26TPL_0045120` | TẬP ĐOÀN XĂNG DẦU VIỆT NA | 1-C26TPL | 0045120 | 2026-07-15 | 5,000,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đủ điều kiện tra cứu và tải hóa đơn |
| 5 | `0100684740_K26TVT_0891234` | TẬP ĐOÀN CÔNG NGHIỆP - VI | 1-K26TVT | 0891234 | 2026-07-18 | 1,320,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đủ điều kiện tra cứu và tải hóa đơn |
| 6 | `0109999999_C26TMA_0000105` | CÔNG TY TNHH THƯƠNG MẠI M | 1-C26TMA | 0000105 | 2026-07-20 | 49,500,000 đ | `❌ REJECTED_HIGH_RISK` | KẾ TOÁN TRƯỞNG TỪ CHỐI: MST thuộc danh sách đen CQT bỏ trốn |
| 7 | `0104863508_C26TYY_0000330` | CÔNG TY CP TRUYỀN THÔNG C | 1-C26TYY | 0000330 | 2026-07-21 | 18,500,000 đ | `❌ REJECTED_MATH_MISMATCH` | KẾ TOÁN TRƯỞNG TỪ CHỐI: Lệch tiền toán học 2M, yêu cầu HĐ điều chỉnh |
| 8 | `010258_C26THH_0000512` | CÔNG TY THIẾT BỊ ĐIỆN HẢI | 1-C26THH | 0000512 | 2026-07-22 | 9,350,000 đ | `❌ REJECTED` | LỖI ĐỊNH DẠNG: MST '010258' không thuộc độ dài hợp lệ [10, 12, 14] |
| 9 | `0108765432_C26TDA_ERR9` | CÔNG TY TNHH VẬT TƯ THIẾT | 1-C26TDA |  | 2026-07-23 | 27,500,000 đ | `❌ REJECTED` | LỖI THIẾU DỮ LIỆU: Số hóa đơn bị trống |
| 10 | `0312456789_C26TSW_0000889` | CÔNG TY TNHH PHẦN MỀM THÔ | 1-C26TSW | 0000889 | 2026-07-25 | 50,000,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đủ điều kiện tra cứu và tải hóa đơn |
| 11 | `0105678912_C26TTL_0000456` | CÔNG TY TNHH CÔNG NGHỆ TỰ | 1-C26TTL | 0000456 | 2026-07-28 | -5,500,000 đ | `✅ ARCHIVED` | HỢP LỆ: Đủ điều kiện tra cứu và tải hóa đơn |
| 12 | `0101234567_C26TVC_0000999` | CÔNG TY TNHH ĐẦU TƯ & XÂY | 1-C26TVC | 0000999 | 2026-07-30 | 1,320,000,000 đ | `✅ ARCHIVED` | KẾ TOÁN TRƯỞNG PHÊ DUYỆT: Đã kiểm tra Hợp đồng & UNC ngân hàng hợp lệ |

---

## 3. BẢNG NHẬT KÝ THẨM ĐỊNH TẠI HUMAN CHECKPOINT (HITL AUDIT TRAIL)

| STT | Mã Hóa Đơn | Nhà Cung Cấp | Rủi Ro Phát Hiện | Quyết Định Kế Toán Trưởng | Hành Động Hệ Thống |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **6** | `0109999999_C26TMA_0000105` | CTY MA XUẤT KHẨU KHỐNG | MST thuộc Blacklist CQT bỏ trốn | **🛑 REJECT** | Chặn tải, cách ly khỏi chi phí thuế |
| **7** | `0104863508_C26TYY_0000330` | TRUYỀN THÔNG Á CHÂU | Lệch tiền 2.000.000 VNĐ | **🛑 REJECT** | Từ chối, yêu cầu bên bán xuất HĐ thay thế |
| **12** | `0101234567_C26TVC_0000999` | ĐẦU TƯ VINACONS | Giá trị lớn >= 1 tỷ VNĐ | **✅ APPROVE** | Xác nhận Hợp đồng & UNC, cấp phép lưu kho |

---

## 4. CÂY THƯ MỤC LƯU TRỮ HÓA ĐƠN ĐÃ ĐƯỢC ĐỒNG BỘ

Các file PDF đã kết xuất chuẩn khổ giấy A4, lề chuẩn và dấu số điện tử, lưu trữ tại:
```text
outputs/HoaDon_LuuTru/2026/07/
├── MauSo_1_GTGT/
│   ├── 0100107934_TAP_DOAN_XANG_DAU_VIET_N/
│   ├── 0100684740_TAP_DOAN_CONG_NGHIEP_VI/
│   ├── 0101234567_CONG_TY_TNHH_DAU_TU_XAY/ (Đã duyệt HITL)
│   ├── 0101893254_CONG_TY_TNHH_PHAT_TRIEN/
│   ├── 0105678912_CONG_TY_TNHH_CONG_NGHE/
│   ├── 0301452948_NGAN_HANG_TMCP_A_CHAU_AC/
│   └── 0312456789_CONG_TY_TNHH_PHAN_MEM_T/
└── MauSo_2_BanHang/
    └── 001065008691_HO_KINH_DOANH_NGUYEN_QU/
```