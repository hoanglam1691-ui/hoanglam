# KỊCH BẢN KIỂM THỬ VÀ CƠ CHẾ CHẶN LỖI CHỦ ĐỘNG

---

## 1. TRƯỜNG HỢP 1: DỮ LIỆU HÓA ĐƠN KHÔNG ĐẦY ĐỦ HOẶC BẤT THƯỜNG

### 1.1. Cơ chế chặn lỗi chủ động (Guardrails)
* **XSD Schema Validator:** Kiểm tra cấu trúc thẻ XML chuẩn trước khi bóc tách.
* **Math Consistency Check:** Kiểm tra $|\text{Tổng thanh toán} - (\text{Doanh số} + \text{Tiền thuế})| \le 10\text{ đ}$.
* **Blacklist Cross-Check:** Đối chiếu tự động mã số thuế người bán với cơ sở dữ liệu doanh nghiệp rủi ro cao.

### 1.2. Ma trận kiểm thử
| Mã Test | Mock Input | Hành vi của Hệ thống | Trạng thái kỳ vọng |
| :---: | :--- | :--- | :--- |
| **TC-1.1** | Thẻ `<SHDon>` bị rỗng hoặc không có thẻ `<MST>`. | Chặn không gửi sang Download, cách ly bản ghi. | `FLAGGED_SCHEMA_ERROR` |
| **TC-1.2** | Tổng tiền lệch toán học $> 1.000\text{đ}$ so với thuế và doanh số. | Tạm dừng và chuyển lên Human Checkpoint #02. | `WAITING_HUMAN_APPROVAL` |
| **TC-1.3** | Hóa đơn từ MST thuộc danh sách đen CQT. | Gắn cờ cảnh báo đỏ, ghi chú vào Bảng kê. | `FLAGGED_HIGH_RISK_SUPPLIER` |

---

## 2. TRƯỜNG HỢP 2: TẢI HÓA ĐƠN THẤT BẠI (DOWNLOAD RESILIENCE)

### 2.1. Cơ chế chặn lỗi chủ động (Guardrails)
* **Exponential Backoff:** Tự động retry 3 lần sau 2s $\rightarrow$ 4s $\rightarrow$ 8s khi gặp lỗi mạng/502/504.
* **Dual-File Verification Gate:** Bắt buộc cả 2 file `.xml` và `.pdf` phải tồn tại, dung lượng $> 0$ bytes và có header hợp lệ (`%PDF-`, `<?xml`).
* **Dead Letter Queue:** Cách ly các hóa đơn lỗi vào hàng đợi tải bù cuối phiên.

### 2.2. Ma trận kiểm thử
| Mã Test | Mock Fault | Hành vi của Hệ thống | Trạng thái kỳ vọng |
| :---: | :--- | :--- | :--- |
| **TC-2.1** | Mạng ngắt quãng tạm thời khi đang tải file. | Bắt timeout, retry thành công ở lần 2. | `DOWNLOADED_AFTER_RETRY` |
| **TC-2.2** | Server trả về PDF hợp lệ nhưng XML $0\text{ byte}$. | Xóa file PDF rác, đưa cả cặp vào hàng đợi tải lại. | `RETRY_QUEUED` |
| **TC-2.3** | Tải thất bại 3 lần liên tiếp do server thuế khóa. | Đóng batch, chuyển sang Human Checkpoint #03. | `FAILED_NEEDS_MANUAL_CHECK` |

---

## 3. TRƯỜNG HỢP 3: HÓA ĐƠN HOẶC FILE ĐÃ TỒN TẠI TRONG KHO

### 3.1. Cơ chế chặn lỗi chủ động (Guardrails)
* **Pre-Download Fingerprinting:** Kiểm tra `Unique_Key = Hash(MST + KHHDon + SoHD)` trong Catalog trước khi gửi lệnh tải. Nếu đã có $\rightarrow$ **Smart Skip** ngay.
* **Atomic Move & Safe Write:** Không bao giờ ghi đè trực tiếp; tải vào thư mục tạm trước khi chuyển sang thư mục đích.
* **Hash Versioning:** Nếu số hóa đơn giống nhau nhưng nội dung thay đổi $\rightarrow$ Lưu tên file hậu tố `_v2`.

### 3.2. Ma trận kiểm thử
| Mã Test | Mock Input | Hành vi của Hệ thống | Trạng thái kỳ vọng |
| :---: | :--- | :--- | :--- |
| **TC-3.1** | Chạy lại kỳ tra cứu mà 100% hóa đơn đã được lưu trữ trước đó. | Bỏ qua toàn bộ 100% hóa đơn, thời gian thực thi $< 2\text{s}$. | `ALL_DUPLICATES_SKIPPED` |
| **TC-3.2** | Kho chỉ có file PDF nhưng thiếu file XML (do sự cố cũ). | Kích hoạt Repair Mode, tải bổ sung file XML còn thiếu. | `REPAIRED_AND_STORED` |
| **TC-3.3** | Xuất hiện hóa đơn thay thế/điều chỉnh cùng số HĐ. | Lưu phiên bản mới `..._0000240_v2.pdf/xml`, không ghi đè file cũ. | `STORED_VERSION_INCREMENT` |
