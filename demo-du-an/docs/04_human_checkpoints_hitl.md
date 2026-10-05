# THIẾT KẾ ĐIỂM KIỂM SOÁT CON NGƯỜI (HUMAN-IN-THE-LOOP - HITL)

---

## 1. MA TRẬN PHÂN QUYỀN TỰ ĐỘNG VS CON NGƯỜI

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │                 PHÂN QUYỀN TỰ ĐỘNG VS CAN THIỆP CON NGƯỜI              │
  │                                                                        │
  │  [ AGENT TỰ ĐỘNG 100% ]               [ BẮT BUỘC CON NGƯỜI DUYỆT ]     │
  │  • Giải Captcha tự động lần 1-3       • Captcha/OTP thất bại sau 3 lần │
  │  • Tra cứu & phân trang               • MST người bán thuộc Blacklist  │
  │  • Tải song song XML + PDF            • Chữ ký số XML bị Invalid/Lỗi   │
  │  • Bỏ qua file trùng lặp              • Chênh lệch tiền thuế > 1.000đ  │
  │  • Đổi tên & tạo cây thư mục          • Phê duyệt Bảng kê trước nộp thuế│
  └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. BẢNG CHI TIẾT CÁC ĐIỂM KIỂM SOÁT (HITL CHECKPOINTS)

| Mã | Vị trí kích hoạt | Điều kiện bắt buộc chuyển cho Con Người | Dữ liệu cung cấp để ra quyết định | Luồng bàn giao sau khi duyệt |
| :---: | :--- | :--- | :--- | :--- |
| **HC-01** | **Xác thực Đăng nhập** | AI OCR giải Captcha thất bại **3 lần liên tiếp** hoặc Cổng GDT yêu cầu mã **OTP xác thực SMS**. | • Ảnh Captcha trực quan.<br>• Ô nhập Captcha/OTP thủ công.<br>• Thời gian đếm ngược phiên ($60s$). | Bàn giao lại cho **Invoice Search Agent** tiếp tục tra cứu. |
| **HC-02** | **Kiểm định Hóa đơn Rủi ro** | • MST người bán nằm trong Blacklist thuế.<br>• Chữ ký số XML báo `Invalid Signature`.<br>• Lệch tổng tiền: $|\text{Tổng tiền} - (\text{Chưa thuế} + \text{Thuế})| > 1.000\text{ đ}$. | • Bảng so sánh dữ liệu XML vs Tiêu chuẩn.<br>• Tên, MST, Số HĐ, Tiền thanh toán.<br>• Nút chọn: `[Duyệt lưu trữ]` / `[Loại bỏ]` | • Nếu `Duyệt`: Chuyển **Download Agent** tải tiếp.<br>• Nếu `Loại`: Đánh dấu `REJECTED`. |
| **HC-03** | **Lỗi Tải file Ngoại lệ** | Tải file XML/PDF thất bại sau $3\text{ lần retry}$ (máy chủ GDT trả lỗi tệp hoặc mạng đứt). | • MST & Số HĐ bị lỗi.<br>• Link tra cứu trực tiếp trên web GDT.<br>• Lựa chọn: `[Thử lại sau 15p]` / `[Bỏ qua]` | • Nếu `Thử lại`: Xếp hàng đợi cuối phiên.<br>• Nếu `Bỏ qua`: Bỏ qua hóa đơn lỗi. |
| **HC-04** | **Phê duyệt Bảng kê Cuối** | Hoàn thành quét, lưu trữ và tổng hợp Bảng kê mua vào của kỳ. | • Bảng tổng hợp KPI (Tổng số HĐ, Doanh số, Thuế).<br>• Bảng kê chi tiết Excel nháp.<br>• Danh sách ngoại lệ đã xử lý. | Bàn giao kết quả cho **Invoice Director Agent** lưu kho chính thức. |

---

## 3. MẪU THÔNG BÁO TƯƠNG TÁC (PROMPT TEMPLATE)

```text
================================================================================
⚠️ CẢNH BÁO KIỂM SOÁT RỦI RO HÓA ĐƠN ĐẦU VÀO (HUMAN CHECKPOINT #02)
================================================================================
Hệ thống phát hiện 01 hóa đơn có dấu hiệu bất thường cần Kế toán xác nhận:

• Số Hóa Đơn   : 0004521 (Ký hiệu: C26TCK)
• Nhà Cung Cấp : CÔNG TY TNHH PHÁT TRIỂN CƠ KHÍ NAM HÀ NỘI (MST: 0101893254)
• Tổng Thanh Toán: 18.583.950 VND (Tiền thuế: 1.689.450 VND)
• Cảnh Báo     : 🛑 Chữ ký số XML không khớp với Chứng thư số công bố trên GDT!

👉 Lựa chọn xử lý của bạn:
  [1] Xác nhận HỢP LỆ (Bỏ qua cảnh báo & Tiếp tục Tải/Lưu trữ)
  [2] LOẠI BỎ (Đánh dấu từ chối kê khai & Ghi nhật ký kiểm toán)
================================================================================
```
