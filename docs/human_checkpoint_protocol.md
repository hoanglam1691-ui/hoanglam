# QUY CHUẨN ĐIỂM KIỂM SOÁT CON NGƯỜI (HUMAN-IN-THE-LOOP - HITL)

> **Hệ thống:** Tìm kiếm, sắp xếp và tải hóa đơn điện tử còn thiếu  
> **Áp dụng cho:** Kế toán nội bộ, Kế toán trưởng và AI Agent điều phối  
> **Nguyên tắc cốt lõi:** *"AI phát hiện bất thường — Con người giữ quyền quyết định pháp lý"*

---

## 1. VỊ TRÍ ĐIỂM DỪNG TRONG WORKFLOW

Điểm kiểm soát con người cốt lõi được thiết lập tại:  
**🛑 Trạm Kiểm Soát Tiền Tải (Pre-Download Risk & Math Gate — HITL #1)**

```text
[Input: File Danh sách thiếu]
         │
         ▼
[Bước 1: Parse & Validate Format]
         │
         ▼
[Bước 2: Math Check & Blacklist Match]
         │
         ├─────────────────────────────────────────────┐
         ▼                                             ▼
  (Dữ liệu Hợp lệ)                             (Phát hiện Bất thường)
         │                                             │
         │                                             ▼
         │                                  ╔════════════════════════════════╗
         │                                  ║  🛑 HUMAN CHECKPOINT #1        ║
         │                                  ║  Hệ thống dừng hoàn toàn       ║
         │                                  ║  Chờ Kế toán trưởng phê duyệt  ║
         │                                  ╚════════════════════════════════╝
         │                                             │
         │                      ┌──────────────────────┴──────────────────────┐
         │                      ▼ [Duyệt cho phép]                            ▼ [Từ chối loại bỏ]
         │             (Chuyển tiếp trạng thái)                      (Cách ly khỏi luồng tải)
         │                      │                                             │
         ▼                      ▼                                             ▼
[Bước 3: Tải PDF qua CDP 9222 / Print to PDF]                    [Ghi nhận cờ REJECTED]
         │                                                                    │
         ▼                                                                    │
[Bước 4: Phân loại & Lưu trữ Cây thư mục]                                     │
         │                                                                    │
         ▼                                                                    │
[Bước 5: Cập nhật Catalog & Báo cáo đối soát hoàn thiện hồ sơ] ◄──────────────┘
```

---

## 2. ĐIỀU KIỆN KÍCH HOẠT ĐIỂM DỪNG (TRIGGER CONDITIONS)

Hệ thống **BẮT BUỘC DỪNG NGAY LẬP TỨC** khi xuất hiện ít nhất 1 trong 3 điều kiện sau:

| Mã Điều Kiện | Tên Điều Kiện | Tiêu Chí Xác Định Cụ Thể | Rủi Ro Tiềm Ẩn Nếu Tự Động Hóa |
| :---: | :--- | :--- | :--- |
| **TRG-01** | **MST thuộc Blacklist Thuế** | Mã số thuế người bán trùng với danh mục rủi ro trong `cau_hinh_nghiep_vu_hoa_don.json` (doanh nghiệp bỏ trốn, buôn bán hóa đơn ma). | Rủi ro bị Cơ quan Thuế loại chi phí và truy thu thuế GTGT, phạt vi phạm hành chính. |
| **TRG-02** | **Lệch tiền toán học** | Lệch giữa tổng tiền thanh toán và tiền hàng + thuế:  <br>$\|\text{Tổng tiền} - (\text{Chưa thuế} + \text{Thuế})\| > 1.000\text{ VNĐ}$. | Sai lệch số liệu kế toán, không khớp sổ sách và phần mềm kế toán. |
| **TRG-03** | **Giá trị hóa đơn siêu lớn** | Tổng tiền thanh toán $\ge 1.000.000.000\text{ VNĐ}$ (hoặc hóa đơn điều chỉnh âm $> 100\text{ triệu}$). | Nghiệp vụ trọng yếu bắt buộc phải kiểm tra kèm Hợp đồng kinh tế và Ủy nhiệm chi. |

---

## 3. GIAO DIỆN & THÔNG BÁO TƯƠNG TÁC CON NGƯỜI (HUMAN REVIEW PROMPT)

Khi điều kiện kích hoạt xảy ra, AI Agent sẽ in thông điệp cảnh báo rõ ràng ra bảng điều khiển hoặc màn hình giao diện:

```text
========================================================================================
⚠️ CẢNH BÁO KIỂM SOÁT RỦI RO HÓA ĐƠN MUA VÀO (HUMAN CHECKPOINT #1)
========================================================================================
Hệ thống phát hiện bản ghi có dấu hiệu bất thường cần Kế toán trưởng thẩm định:

• Dòng STT      : 6
• Số Hóa Đơn    : 0000105 (Ký hiệu: C26TMA)
• Người Bán     : CÔNG TY TNHH THƯƠNG MẠI MA XUẤT KHẨU KHỐNG (MST: 0109999999)
• Doanh Số      : 45.000.000 VNĐ | Tiền Thuế: 4.500.000 VNĐ | Tổng: 49.500.000 VNĐ
• CẢNH BÁO ĐỎ   : 🛑 Doanh nghiệp có thông báo không hoạt động tại địa chỉ đăng ký (Bỏ trốn)

👉 LỰA CHỌN CỦA BẠN (Nhập lựa chọn để tiếp tục):
  [1] APPROVE (Xác nhận hàng hóa thực tế đã nhận, cho phép tải PDF để đối soát giải trình)
  [2] REJECT  (Chặn hoàn toàn, loại bỏ khỏi hồ sơ thanh toán và cảnh báo nội bộ)
========================================================================================
```

---

## 4. LUỒNG BÀN GIAO SAU KHI CON NGƯỜI RA QUYẾT ĐỊNH
1. **Nếu Con người chọn [1] APPROVE:**
   - Cập nhật trường `pipeline_status = "APPROVED_BY_HUMAN"`.
   - Bổ sung `audit_note = "Kế toán trưởng duyệt bổ sung hồ sơ ngày YYYY-MM-DD"`.
   - Bàn giao sang Bước 3 (`Invoice Download Agent`) để tiếp tục tải bản in PDF.
2. **Nếu Con người chọn [2] REJECT:**
   - Cập nhật trường `pipeline_status = "REJECTED_HIGH_RISK"`.
   - Bổ sung `audit_note = "Từ chối do rủi ro MST bỏ trốn / sai lệch số liệu"`.
   - Chặn không gửi lệnh tải lên Cổng GDT, ghi nhận bản ghi vào mục "Hóa đơn cần loại bỏ" trong Báo cáo đối soát cuối cùng.
