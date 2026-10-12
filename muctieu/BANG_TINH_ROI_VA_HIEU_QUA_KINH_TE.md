# BẢNG PHÂN TÍCH HIỆU QUẢ KINH TẾ & TỶ SUẤT HOÀN VỐN (ROI)
## DỰ ÁN TỰ ĐỘNG HÓA THU THẬP & LƯU TRỮ HÓA ĐƠN ĐIỆN TỬ MUA VÀO

> **Tài liệu đính kèm Slide báo cáo Ban Giám đốc & Kế toán trưởng**  
> **Phương pháp phân tích:** Mô hình Định lượng Chi phí - Lợi ích (Cost-Benefit Analysis)  
> **Cơ sở giả định:** Doanh nghiệp sản xuất/thương mại quy mô vừa (Phát sinh trung bình 300 hóa đơn mua vào/tháng)

---

## 1. CÁC THÔNG SỐ ĐẦU VÀO GIẢ ĐỊNH (INPUT ASSUMPTIONS)

| Thông số nghiệp vụ | Giá trị cơ sở | Căn cứ thực tế |
| :--- | :---: | :--- |
| **Số lượng hóa đơn mua vào bình quân / tháng** | **300 HĐ** | Dựa trên thực tế hoạt động sản xuất, kinh doanh thông thường. |
| **Số lượng hóa đơn thiếu cần tìm & tải / tháng** | **150 HĐ** (50%) | Các hóa đơn điện, nước, viễn thông, tiếp khách, nhà cung cấp phụ trợ. |
| **Thời gian kế toán xử lý thủ công 1 hóa đơn** | **2.5 phút / HĐ** | Bao gồm: Gõ tìm kiếm, chờ load, bấm in, chọn thư mục, gõ tên file. |
| **Chi phí giờ công bình quân của kế toán viên** | **100.000 VNĐ / giờ** | Mức lương kế toán cứng 12 - 16 triệu VNĐ/tháng (~160 giờ làm việc). |
| **Mức phạt trung bình lỗi chậm/mất chứng từ kế toán** | **6.000.000 VNĐ / vụ** | Khung phạt từ 4 - 10 triệu đồng theo Điều 15 Nghị định 125/2020/NĐ-CP. |
| **Chi phí bản quyền giải pháp đề xuất** | **0 VNĐ** | Phát triển nội bộ dựa trên Python, Chrome và Agentic RPA có sẵn. |

---

## 2. SO SÁNH ĐỊNH LƯỢNG: TRƯỚC VÀ SAU KHI TỰ ĐỘNG HÓA

### 2.1. Về mặt Thời gian Lao động (Labor Time)

```text
┌──────────────────────────────────────┬──────────────────────┬──────────────────────┬─────────────────────┐
│ Chu kỳ đo lường                      │ Quy trình Thủ công   │ Tự động hóa (RPA)    │ Tiết kiệm được      │
├──────────────────────────────────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ Thời gian xử lý 1 hóa đơn            │ 150 giây             │ 4 giây               │ Tiết kiệm 146 giây  │
│ Thời gian xử lý 150 hóa đơn thiếu    │ 375 phút (6.25 giờ)  │ 10 phút (0.17 giờ)   │ Tiết kiệm 6.08 giờ  │
│ Thời gian rà soát, đối soát bảng kê  │ 120 phút (2.0 giờ)   │ Tự động sinh báo cáo │ Tiết kiệm 2.0 giờ   │
├──────────────────────────────────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ TỔNG THỜI GIAN HAO PHÍ / THÁNG       │ 8.25 giờ / tháng     │ 0.17 giờ / tháng     │ TIẾT KIỆM 8.08 GIỜ  │
│ TỔNG THỜI GIAN HAO PHÍ / NĂM         │ 99.0 giờ / năm       │ 2.0 giờ / năm        │ TIẾT KIỆM 97.0 GIỜ  │
└──────────────────────────────────────┴──────────────────────┴──────────────────────┴─────────────────────┘
```

> 🎯 **Kết luận thời gian:** Tiết kiệm được **hơn 97 giờ làm việc mỗi năm** (tương đương gần **12 ngày công trọn vẹn** của một nhân viên kế toán).

---

### 2.2. Về mặt Chi phí Tài chính Trực tiếp (Direct Financial Costs)

```text
┌──────────────────────────────────────┬──────────────────────┬──────────────────────┬─────────────────────┐
│ Khoản mục chi phí                    │ Chi phí Hiện tại (Cũ)│ Chi phí Đề xuất (Mới)│ Chênh lệch Tiết kiệm│
├──────────────────────────────────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ Chi phí nhân công xử lý hàng tháng   │ 825.000 VNĐ          │ 17.000 VNĐ           │ 808.000 VNĐ / tháng │
│ Chi phí nhân công xử lý hàng năm     │ 9.900.000 VNĐ        │ 204.000 VNĐ          │ 9.696.000 VNĐ / năm │
│ Chi phí bản quyền phần mềm / năm     │ 0 VNĐ                │ 0 VNĐ                │ 0 VNĐ               │
│ Chi phí vận hành máy tính & điện toán│ Không đáng kể        │ Không đáng kể        │ 0 VNĐ               │
├──────────────────────────────────────┼──────────────────────┼──────────────────────┼─────────────────────┤
│ TỔNG CHI PHÍ VẬN HÀNH TRỰC TIẾP / NĂM│ 9.900.000 VNĐ        │ 204.000 VNĐ          │ TIẾT KIỆM 9.696.000 │
└──────────────────────────────────────┴──────────────────────┴──────────────────────┴─────────────────────┘
```

---

### 2.3. Về mặt Quản trị Rủi ro & Chi phí Tránh được (Avoided Risk Costs)

Trong nghiệp vụ kế toán, giá trị lớn nhất của số hóa không chỉ nằm ở việc tiết kiệm thời gian, mà nằm ở việc **Phòng ngừa rủi ro tài chính (Risk Avoidance)**:

1. **Rủi ro Bị phạt Hành chính Thuế:**
   - Khi doanh nghiệp không lưu giữ hoặc làm thất lạc hóa đơn gốc theo đúng chuẩn định dạng điện tử (Nghị định 123/2020/NĐ-CP & Thông tư 78/2021/TT-BTC), mức xử phạt theo Nghị định 125/2020/NĐ-CP dao động từ **4.000.000 đ đến 10.000.000 đ**.
   - *Giá trị bảo vệ dự tính:* Tối thiểu **6.000.000 VNĐ / năm**.
2. **Rủi ro Bị loại trừ Chi phí Hợp lý (Bóc tách thuế TNDN):**
   - Hóa đơn không có file chứng từ hợp lệ kèm chữ ký số toàn vẹn có thể bị cơ quan thuế bác bỏ khỏi chi phí được trừ khi tính thuế TNDN. Với một hóa đơn chi phí 50.000.000 VNĐ, số tiền thuế TNDN 20% bị truy thu và phạt chậm nộp là **10.000.000 VNĐ**.
   - *Giá trị bảo vệ dự tính:* Tối thiểu **10.000.000 VNĐ / năm**.

---

## 3. TỔNG HỢP BÀI TOÁN KINH TẾ & TỶ SUẤT HOÀN VỐN (ROI MATRIX)

### 3.1. Bảng Tổng hợp Giá trị Mang lại Hàng năm (Annual Value Summary)

```text
┌──────────────────────────────────────────────────────────┬─────────────────────────────┐
│ Nguồn giá trị tạo ra                                     │ Giá trị quy đổi / Năm (VNĐ) │
├──────────────────────────────────────────────────────────┼─────────────────────────────┤
│ 1. Tiết kiệm chi phí thời gian lao động của kế toán      │ 9.696.000 VNĐ               │
│ 2. Tránh rủi ro bị xử phạt hành chính hóa đơn chứng từ   │ 6.000.000 VNĐ               │
│ 3. Tránh rủi ro bị truy thu chi phí tính thuế TNDN       │ 10.000.000 VNĐ              │
│ 4. Tiết kiệm chi phí mua các phần mềm trung gian bên ngoài│ 5.000.000 VNĐ               │
├──────────────────────────────────────────────────────────┼─────────────────────────────┤
│ TỔNG LỢI ÍCH KINH TẾ QUY ĐỔI / NĂM                       │ 30.696.000 VNĐ              │
└──────────────────────────────────────────────────────────┴─────────────────────────────┘
```

### 3.2. Tính toán Tỷ suất Hoàn vốn (ROI Calculation)

- **Tổng chi phí đầu tư ban đầu (Initial Investment):**
  - Chi phí thiết lập, cấu hình kịch bản và chạy thử nghiệm (khoảng 15 giờ công nội bộ): **~1.500.000 VNĐ** (hoặc 0 VNĐ nếu tận dụng thời gian học viên/kế toán nội bộ).
  - Chi phí bản quyền phần mềm: **0 VNĐ**.
- **Công thức tính ROI:**
  $$\text{ROI} = \frac{\text{Tổng lợi ích kinh tế năm} - \text{Chi phí đầu tư}}{\text{Chi phí đầu tư}} \times 100\%$$
  $$\text{ROI} = \frac{30.696.000 - 1.500.000}{1.500.000} \times 100\% = 1.946\%$$

- **Thời gian hoàn vốn (Payback Period):**
  $$\text{Thời gian hoàn vốn} = \frac{1.500.000}{30.696.000 / 12} \approx 0.58 \text{ tháng (khoảng 18 ngày vận hành)}$$

> 🏆 **KẾT LUẬN TÀI CHÍNH:** Dự án đạt tỷ suất hoàn vốn lên tới gần **2.000%**, thu hồi vốn toàn bộ chi phí thử nghiệm chỉ sau chưa đầy **1 tháng** đưa vào vận hành. Đây là dự án có tỷ lệ lợi nhuận/rủi ro hoàn hảo nhất trong các sáng kiến chuyển đổi số cấp phòng ban!

---
*Bản tính toán này được chuẩn hóa để đưa vào Slide 9 của Báo cáo đề xuất dự án.*
