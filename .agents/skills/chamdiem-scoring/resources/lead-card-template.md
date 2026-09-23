# Mẫu Thẻ Bàn Giao Lead Chuẩn (Zalo / CRM / Sheet Notification)

Mẫu định dạng tin nhắn gửi tự động vào nhóm Zalo hoặc CRM của Sales khi có Lead mới được chấm điểm.

---

## 1. Mẫu Thông Báo Lead 🔥 HOT (Gửi tức thì vào nhóm Sales VIP)

```text
🚨 [HOT LEAD ALERT - BẤT ĐỘNG SẢN] 🚨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Khách hàng: {{ten_khach}} | ID: #{{id}}
📞 SĐT: {{sdt}}
⭐ Điểm tiềm năng: {{diem_so}}/100 (HẠNG HOT 🔥)
⏱️ SLA Gọi lại: TRONG VÒNG 15 PHÚT

📋 Nhu cầu tóm tắt:
- Phân khúc: {{loai_hinh}}
- Ngân sách: {{ngan_sach}}
- Vị trí quan tâm: {{vi_tri}}
- Tiến độ: {{thoi_gian}}

💡 AI Insights (Căn cứ chấm điểm):
{{ly_do_cham_diem}}

🎯 Gợi ý kịch bản mở đầu:
"{{kich_ban_mo_dau}}"

👉 Phân bổ cho: {{ten_sales_phu_trach}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 2. Mẫu Bảng Tổng Hợp Chấm Điểm (Bàn giao theo Ca / Sheet)

```markdown
| ID | Họ Tên Khách | Số Điện Thoại | Điểm | Xếp Hạng | Nhu Cầu Cốt Lõi | SLA | Gợi Ý Hành Động |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| #04 | Lê Anh Lan | 0964591036 | **100** | 🔥 **HOT** | Penthouse diện tích lớn, hồ bơi riêng, tài chính vô hạn | <15p | Chuyên viên VIP gọi chốt lịch xem thực tế |
| #28 | Trần Hoàng Dũng | 0943392982 | **100** | 🔥 **HOT** | Chủ DN tìm quỹ đất CN / Sàn >2000m2 khu Đông | <15p | Gửi hồ sơ pháp lý 100% & hẹn gặp CĐT |
| #03 | Lý Đức Cường | 0953430096 | **70** | ⛅ **WARM** | Căn hộ 2PN Q7 (4-5 tỷ), cần vay 70%, xem cuối tuần | <4h | Tư vấn chính sách vay, hẹn xem nhà mẫu |
| #02 | Hồ Hồng Linh | 0848475144 | **0** | ❄️ **COLD** | Nhầm số, dữ liệu cũ ngành khác | N/A | Đưa vào Blacklist, không gọi làm phiền |
```
