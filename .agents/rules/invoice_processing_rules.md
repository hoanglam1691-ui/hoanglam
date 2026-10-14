# WORKSPACE RULES: QUY TẮC VẬN HÀNH & CHUẨN BÀN GIAO (HANDOFF)

> **Dự án:** Tìm kiếm, sắp xếp và tải hóa đơn điện tử còn thiếu  
> **Áp dụng cho:** Toàn bộ AI Agents, Skills và Scripts trong workspace  
> **Mục tiêu:** Đảm bảo an toàn dữ liệu, tính toàn vẹn chứng từ kế toán và sự thông suốt dữ liệu giữa các bước

---

## 1. ĐIỀU AGENT ĐƯỢC LÀM (ALLOWED ACTIONS)
1. **Đọc & Tiền kiểm Dữ liệu:** Đọc danh sách hóa đơn thiếu từ file CSV/Excel do kế toán nội bộ cung cấp; chuẩn hóa chuỗi, số hóa đơn, và mã số thuế.
2. **Kiểm tra Đối soát:** Thực hiện kiểm tra tính toán học số học, đối chiếu danh mục Whitelist và Blacklist thuế trong `knowledge_base/`.
3. **Kết nối Tự động hóa Trình duyệt:** Kết nối an toàn qua cổng Chrome CDP (mặc định 9222) mà người dùng đã khởi chạy và đăng nhập tài khoản Cổng Thuế.
4. **Kết xuất Máy in ảo:** Kích hoạt tính năng in ấn ảo của Chromium / Microsoft Print to PDF để lưu hóa đơn sang định dạng PDF/HTM chuẩn hiển thị 1:1.
5. **Tổ chức Lưu trữ Chuẩn mực:** Tự động tạo cây thư mục `outputs/HoaDon_LuuTru/{YYYY}/{MM}/{MauSo}/{MST}_{TenNCC}/` và đổi tên tệp theo quy chuẩn kế toán.
6. **Lập Báo cáo & Catalog:** Cập nhật cơ sở dữ liệu `outputs/storage_catalog.json` và xuất Báo cáo đối soát hoàn thiện hồ sơ cho ban quản lý.

---

## 2. ĐIỀU CẤM (FORBIDDEN ACTIONS & GUARDRAILS)
1. 🛑 **CẤM LƯU TRỮ CREDENTIALS:** Tuyệt đối KHÔNG yêu cầu, KHÔNG ghi nhận và KHÔNG lưu trữ mật khẩu đăng nhập, mã PIN chữ ký số, OTP của Cổng Thuế vào bất kỳ file mã nguồn, cấu hình hay log nào.
2. 🛑 **CẤM SỬA ĐỔI NỘI DUNG GỐC:** Tuyệt đối KHÔNG can thiệp, chỉnh sửa, làm tròn số tiền, hoặc thay đổi bất kỳ ký tự nào trong file PDF/HTM hóa đơn kết xuất từ trang Thuế.
3. 🛑 **CẤM BỎ QUA BLACKLIST:** Tuyệt đối KHÔNG tự ý tải hoặc đưa vào danh mục hợp lệ các hóa đơn có MST nằm trong Danh sách đen thuế mà chưa có phê duyệt từ Kế toán trưởng qua Human Checkpoint.
4. 🛑 **CẤM GHI ĐÈ MÙ QUÁNG:** Tuyệt đối KHÔNG ghi đè tệp tin đã tồn tại trong kho lưu trữ chính thức mà không kiểm tra hash và đánh số phiên bản `_v2`.

---

## 3. CÁCH XỬ LÝ KHI GẶP LỖI (ERROR HANDLING PROTOCOLS)
| Tình huống Lỗi | Nguyên nhân | Giao thức Xử lý Tự động của Agent | Trạng thái ghi nhận |
| :--- | :--- | :--- | :--- |
| **Lỗi mạng / 502 / 504** | Cổng Thuế quá tải hoặc mạng ngắt quãng | Kích hoạt Exponential Backoff: Tự động thử lại 3 lần sau 2s $\rightarrow$ 4s $\rightarrow$ 8s. Nếu vẫn lỗi, chuyển vào hàng đợi xử lý bù. | `RETRY_QUEUED` |
| **Lỗi File 0 Byte / Hỏng** | Quá trình in ảo bị ngắt đột ngột | Lập tức xóa file rác 0 byte; KHÔNG di chuyển vào kho lưu trữ; thử in lại lần 2. | `FILE_CORRUPTED_RETRY` |
| **Gặp Captcha / OTP mới** | Hết hạn phiên đăng nhập Cổng Thuế | Dừng ngay luồng tự động, phát cảnh báo HITL để con người trực tiếp thao tác trên Chrome. | `WAITING_HUMAN_AUTH` |
| **Lệch tiền toán học $> 1.000$đ** | Hóa đơn sai sót số học từ bên bán | Tạm dừng xử lý dòng này, gắn cờ và chuyển lên Human Checkpoint phê duyệt. | `FLAGGED_MATH_MISMATCH` |
| **MST thuộc Blacklist** | Doanh nghiệp bỏ trốn / mua bán hóa đơn | Cách ly bản ghi, ghi nhận cảnh báo đỏ, chuyển Kế toán trưởng thẩm định. | `FLAGGED_BLACKLIST` |

---

## 4. ĐỊNH DẠNG BÀN GIAO DỮ LIỆU ĐỒNG NHẤT (STANDARD HANDOFF SCHEMA)

Để đảm bảo dữ liệu bàn giao giữa Bước 1 (Tìm kiếm & Tiền kiểm), Bước 2 (Tải file), và Bước 3 (Lưu trữ & Báo cáo) hoàn toàn nhất quán về tên trường (field names), toàn bộ hệ thống bắt buộc sử dụng chuẩn JSON Schema sau:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "StandardInvoiceHandoffItem",
  "type": "object",
  "required": [
    "invoice_uid",
    "seller_tax_id",
    "seller_name",
    "invoice_form",
    "invoice_symbol",
    "invoice_number",
    "invoice_date",
    "amount_before_tax",
    "tax_amount",
    "total_payment",
    "pipeline_status"
  ],
  "properties": {
    "invoice_uid": {
      "type": "string",
      "description": "Mã định danh duy nhất: {seller_tax_id}_{invoice_symbol}_{invoice_number}"
    },
    "seller_tax_id": {
      "type": "string",
      "description": "Mã số thuế bên bán (10 hoặc 14 chữ số)"
    },
    "seller_name": {
      "type": "string",
      "description": "Tên đầy đủ của đơn vị bán hàng"
    },
    "invoice_form": {
      "type": "string",
      "description": "Mẫu số hóa đơn: '1' (GTGT), '2' (Bán hàng)"
    },
    "invoice_symbol": {
      "type": "string",
      "description": "Ký hiệu hóa đơn (ví dụ C26TCK, K26TYY)"
    },
    "invoice_number": {
      "type": "string",
      "description": "Số hóa đơn 7 chữ số (ví dụ 0000302)"
    },
    "invoice_date": {
      "type": "string",
      "format": "date",
      "description": "Ngày lập hóa đơn (định dạng YYYY-MM-DD)"
    },
    "amount_before_tax": {
      "type": "number",
      "description": "Tổng doanh số chưa có thuế (VNĐ)"
    },
    "tax_amount": {
      "type": "number",
      "description": "Tiền thuế GTGT (VNĐ)"
    },
    "total_payment": {
      "type": "number",
      "description": "Tổng tiền thanh toán (VNĐ)"
    },
    "tax_authority_code": {
      "type": "string",
      "description": "Mã cơ quan thuế cấp MCCQT (nếu có)"
    },
    "pipeline_status": {
      "type": "string",
      "enum": [
        "DISCOVERED",
        "READY_FOR_SEARCH",
        "DOWNLOADED",
        "ARCHIVED",
        "FLAGGED_HITL",
        "REJECTED"
      ],
      "description": "Trạng thái vòng đời của bản ghi trong quy trình"
    },
    "file_path_pdf": {
      "type": "string",
      "description": "Đường dẫn tương đối tới file PDF lưu trữ trong outputs/"
    },
    "audit_note": {
      "type": "string",
      "description": "Ghi chú nghiệp vụ, cảnh báo lỗi hoặc lý do phê duyệt HITL"
    }
  }
}
```
