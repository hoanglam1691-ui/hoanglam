# Operations KPI Definitions & Formulas Reference

> **Tài liệu tham chiếu công thức tính toán và ngưỡng cảnh báo vận hành**  
> Thuộc Skill: `ai4a:ops-analyst`  
> Phiên bản: 1.0.0  

Tài liệu này cung cấp công thức toán học chuẩn xác để tính toán các chỉ số hiệu suất vận hành (Operations Performance Metrics) và các ngưỡng kích hoạt điểm kiểm soát (Human Checkpoints).

---

## 1. Các Công Thức KPI Định Lượng Chuẩn

### 1.1 Tỷ lệ hoàn thành công việc (Completion Rate)
Đo lường mức độ hoàn thành các đầu việc được giao trong kỳ:

$$\text{Completion Rate (\%)} = \left( \frac{\text{Số việc trạng thái Completed}}{\text{Tổng số việc trong kỳ}} \right) \times 100\%$$

* **Ý nghĩa:** Đánh giá năng lực giải quyết công việc theo cam kết của bộ phận hoặc cá nhân.
* **Lưu ý:** Các công việc `Cancelled` do yếu tố bất khả kháng từ khách hàng có thể được trừ ra khỏi mẫu số nếu có biên bản duyệt.

---

### 1.2 Tỷ lệ trễ hạn (Delay / Overdue Rate)
Đo lường mức độ vi phạm thời hạn cam kết (SLA Breaches):

$$\text{Delay Rate (\%)} = \left( \frac{\text{Số việc trạng thái Delayed}}{\text{Tổng số việc trong kỳ}} \right) \times 100\%$$

---

### 1.3 Năng suất bình quân trên mỗi nhân sự (Productivity per Headcount)
Đo lường sản lượng trung bình mà một nhân sự tạo ra:

$$\text{Productivity} = \frac{\sum \text{Output Units}}{\text{Số lượng nhân sự có phát sinh việc (Active Headcount)}}$$

* Với phòng ban Kinh doanh: Thay `Output Units` bằng `Revenue (VND)`.

---

### 1.4 Mức độ biến động sản lượng so với kỳ trước (Month-over-Month Growth)

$$\text{MoM Growth (\%)} = \left( \frac{\text{Output Tháng N} - \text{Output Tháng N-1}}{\text{Output Tháng N-1}} \right) \times 100\%$$

---

## 2. Ma Trận Ngưỡng Cảnh Báo Vận Hành (Alert Threshold Matrix)

| Chỉ số | Mức An Toàn (Xanh) | Cảnh báo Cần Theo Dõi (Vàng) | Nguy Cơ Cao - Kích Hoạt Checkpoint (Đỏ) |
| :--- | :---: | :---: | :---: |
| **Completion Rate** | $\ge 85\%$ | $70\% - 84\%$ | $< 70\%$ |
| **Delay Rate** | $< 10\%$ | $10\% - 20\%$ | $> 20\%$ |
| **Tỷ lệ nhân sự dưới chuẩn** | $< 5\%$ | $5\% - 15\%$ | $> 15\%$ đội ngũ |
| **MoM Growth sản lượng** | $\ge 0\%$ | $-10\% \text{ đến } -1\%$ | Sụt giảm $> 10\%$ |

---

## 3. Quy Trình Kích Hoạt Human Checkpoint (Rà Soát Con Người)

Khi gặp các trường hợp sau, AI **không tự kết luận lỗi năng lực nhân sự** mà phải gắn nhãn cảnh báo để người phân tích vận hành hoặc Trưởng phòng xác minh:

1. **Khối lượng task tăng đột biến:** Nếu tổng số task giao cho một phòng ban tăng $> 50\%$ so với tháng trước nhưng tỷ lệ hoàn thành giảm nhẹ, nguyên nhân khả năng cao do thiếu nhân sự (Understaffed) chứ không phải do năng suất kém.
2. **Sự phụ thuộc liên phòng ban (Cross-functional Bottleneck):** Nếu một việc bị trễ ở bộ phận Vận hành do phải chờ phê duyệt từ bộ phận Kỹ thuật hoặc Tài chính, cần ghi nhận là "Nghẽn quy trình bàn giao" (Handoff Blocker).
3. **Phát hiện ngoại lệ (Outlier Detection):** Các nhân viên có sản lượng gấp $> 2.5$ lần mức trung bình cần được tuyên dương và phỏng vấn để nhân bản quy trình (Best Practice Sharing).
