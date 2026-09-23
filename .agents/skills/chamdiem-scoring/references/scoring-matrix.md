# Ma Trận Tiêu Chí Chấm Điểm Khách Hàng Tiềm Năng (Bất Động Sản)

Tài liệu tham chiếu chi tiết cho hệ thống AI Lead Scoring và Telesale/Marketing trong ngành Bất Động Sản.

---

## 1. Khung 5 Trụ Cột Đánh Giá (BANT + Engagement Model)

| Tiêu Chí | Trọng Số | Ý Nghĩa Nghiệp Vụ | Dấu Hiệu Nhận Diện |
| :--- | :---: | :--- | :--- |
| **1. Ngân Sách (Budget)** | **30%** | Khả năng chi trả thực tế của khách hàng | Số tiền cụ thể, mức vốn tự có, khả năng đòn bẩy tài chính |
| **2. Mức Độ Phù Hợp & Nhu Cầu (Interest & Fit)** | **25%** | Sự phù hợp giữa loại hình BĐS và phân khúc | Loại hình (Chung cư, Đất nền, Biệt thự, Penthouse, Kho xưởng), Vị trí mong muốn |
| **3. Thời Gian Quyết Định (Timeline / Urgency)** | **20%** | Tính cấp thiết và thời điểm chốt giao dịch | Thời hạn xuống tiền (Ngay trong tuần/tháng, Cuối tuần xem nhà, Đang tìm hiểu) |
| **4. Nguồn Khách & Hồ Sơ (Source & Persona)** | **15%** | Mức độ uy tín của kênh thu thập và chân dung khách | Khách tự đăng ký form, Khách giới thiệu, Chủ doanh nghiệp, Nhà đầu tư chuyên nghiệp |
| **5. Tương Tác & Thiện Chí (Engagement)** | **10%** | Mức độ phối hợp khi giao tiếp với tư vấn | Nghe máy, phản hồi tin nhắn Zalo, thái độ hợp tác, chia sẻ thông tin minh bạch |

---

## 2. Bảng Quy Đổi Điểm Chi Tiết (Scoring Breakdown)

### A. Phân Nhóm VIP (+30 đến +50 điểm)
*Khách hàng có ngân sách cực lớn, vị thế tài chính mạnh hoặc nhu cầu mua sỉ.*

- **Ngân sách siêu lớn (+50 điểm):** Đề cập số tiền $\ge 20\text{ tỷ}$ VNĐ (hoặc 50 - 100 tỷ), từ khóa: *"tài chính mạnh"*, *"ngân sách không thành vấn đề"*, *"thanh toán 100% tiền mặt"*.
- **Loại hình cao cấp & Quy mô lớn (+40 đến +50 điểm):** Tìm kiếm *"Biệt thự đơn lập"*, *"Penthouse"*, *"Shophouse mặt đường lớn"*, *"Quỹ đất công nghiệp"*, *"Sàn văn phòng diện tích lớn (>2000m²)"*.
- **Vị trí trung tâm & BĐS danh giá (+30 điểm):** *"Quận 1"*, *"Ven sông"*, *"Vinhomes Ocean Park"*, *"Phú Mỹ Hưng"*, *"Thảo Điền"*.
- **Chân dung khách hàng cao cấp (+40 điểm):** *"Chủ doanh nghiệp"*, *"Nhà đầu tư chuyên nghiệp"*, *"Mua sỉ"*, *"Mua theo block / sàn"*.
- **Tính cấp thiết & Pháp lý cao cấp (+30 điểm):** Yêu cầu *"Pháp lý chuẩn 100%"*, *"Sổ hồng riêng sang tên ngay"*, *"Muốn gặp trực tiếp chủ đầu tư đàm phán"*.

---

### B. Phân Nhóm Tiềm Năng / Tầm Trung (+10 đến +25 điểm)
*Khách hàng có nhu cầu thực tế, khả năng tài chính tầm trung, cần tư vấn thêm.*

- **Ngân sách tầm trung (+20 điểm):** Mức tài chính từ $2\text{ đến }10\text{ tỷ}$ VNĐ.
- **Loại hình phổ biến (+15 đến +20 điểm):** *"Căn hộ 2PN - 3PN"*, *"Nhà phố liền kề"*, *"Đất nền vùng ven có sổ"*, *"Mặt bằng kinh doanh / Spa 30 - 50 triệu/tháng"*.
- **Tính thời điểm rõ ràng (+20 đến +25 điểm):** *"Xem nhà mẫu cuối tuần này"*, *"Cần ký hợp đồng dài hạn"*, *"Xuống tiền trong tháng"*.
- **Cần hỗ trợ đòn bẩy tài chính (+15 điểm):** Cần tư vấn gói vay ngân hàng ($50\% - 70\%$), hỏi kỹ về chính sách chiết khấu, tiến độ thanh toán.

---

### C. Phân Nhóm Khách Hàng Rác / Không Tiềm Năng (-50 đến -80 điểm)
*Cần loại trừ ngay khỏi danh sách gọi telesale trực tiếp.*

- **Yêu cầu phi thực tế / Ảo tưởng giá (-60 điểm):** Tìm mua BĐS giá thấp vô lý (VD: *"Nhà Quận 1 giá 1 - 2 tỷ"*, *"Nhà trung tâm có sân vườn hồ bơi vài trăm triệu"*, *"Thuê nhà nguyên căn trung tâm 2 triệu"*).
- **Dữ liệu rác / Không có nhu cầu (-60 điểm):** Ghi chú *"Nhầm số"*, *"Không có nhu cầu BĐS"*, *"Dữ liệu cũ ngành khác trộn vào"*, *"Trẻ em bấm nhầm form"*.
- **Không thiện chí (-50 điểm):** *"Hỏi giá cho vui"*, *"Chưa có ý định mua trong 1-2 năm tới"*, *"Thái độ chửi bới / Không hợp tác"*.
- **Spam / Mời chào dịch vụ khác (-80 điểm):** Nội dung chứa dịch vụ bảo hiểm, cho vay tiêu dùng, quảng cáo sim số, SEO web.
- **Thông tin liên lạc lỗi (-50 điểm):** *"Số thuê bao"*, *"Gọi nhiều lần không bắt máy"*, *"Zalo chặn tin nhắn người lạ"*.

---

## 3. Thang Điểm Tổng Hợp & Phân Hạng Khách Hàng

$$\text{Tổng Điểm} = \text{Điểm Cơ Sở (50)} + \sum \text{Điểm Thưởng} - \sum \text{Điểm Phạt}$$
*(Thang điểm chuẩn hóa: 0 đến 100)*

```text
┌─────────────────────────┬──────────────────────────┬────────────────────────┐
│    ❄️ COLD (0 - 34)      │     ⛅ WARM (35 - 69)     │     🔥 HOT (70 - 100)   │
│   Rác / Nuôi dưỡng tự động│   Tiềm năng / Tư vấn thêm │    VIP / Chốt sale ngay │
└─────────────────────────┴──────────────────────────┴────────────────────────┘
```
