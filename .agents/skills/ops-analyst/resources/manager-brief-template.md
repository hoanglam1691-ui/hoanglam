# Bản Tin Hiệu Suất Vận Hành — Bộ Phận {{department_name}}

> **Đối tượng nhận:** Trưởng bộ phận (Department Manager)  
> **Kỳ báo cáo:** Tháng {{month}}  
> **File dữ liệu chi tiết nội bộ:** `outputs/departments/{{department_file_name}}`  
> **Người tổng hợp:** Operations Analyst Assistant (`ai4a:ops-analyst`)  

---

## 1. Tóm Tắt Chỉ Số Phòng Ban (Department Performance Snapshot)

- **Tổng số nhân sự hoạt động:** `{{active_headcount}}` nhân viên
- **Tổng số công việc được giao:** `{{total_tasks}}` công việc
- **Số công việc hoàn thành đúng hạn:** `{{completed_tasks}}` (`{{completion_rate}}%`)
- **Số công việc đang xử lý:** `{{in_progress_tasks}}`
- **Số công việc trễ hạn:** `{{delayed_tasks}}` (`{{delay_rate}}%`)
- **Đánh giá chung:** `{{performance_rating}}` *(Đạt chuẩn / Cần khắc phục gấp / Vượt kỳ vọng)*

---

## 2. Bảng Xếp Hạng Hiệu Suất Nhân Sự Trong Phòng

| Mã NV | Họ và tên | Công việc đã giao | Đã hoàn thành | Đang làm | Trễ hạn | Tỷ lệ HT (%) | Đánh giá |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `{{emp_1_id}}` | {{emp_1_name}} | {{emp_1_total}} | {{emp_1_done}} | {{emp_1_doing}} | {{emp_1_late}} | {{emp_1_rate}}% | {{emp_1_badge}} |
| `{{emp_2_id}}` | {{emp_2_name}} | {{emp_2_total}} | {{emp_2_done}} | {{emp_2_doing}} | {{emp_2_late}} | {{emp_2_rate}}% | {{emp_2_badge}} |
| `{{emp_3_id}}` | {{emp_3_name}} | {{emp_3_total}} | {{emp_3_done}} | {{emp_3_doing}} | {{emp_3_late}} | {{emp_3_rate}}% | {{emp_3_badge}} |

---

## 3. Phân Tích Nguyên Nhân Trễ Hạn & Điểm Nghẽn Nội Bộ

- **Nguyên nhân chính dẫn đến trễ hạn:**
  > *{{delay_root_cause_analysis}}*
- **Các đầu việc cờ đỏ cần giải cứu ngay:**
  - [ ] `{{critical_task_1}}` — Phụ trách: `{{critical_task_1_owner}}` (Quá hạn {{critical_task_1_days}} ngày)
  - [ ] `{{critical_task_2}}` — Phụ trách: `{{critical_task_2_owner}}` (Quá hạn {{critical_task_2_days}} ngày)

---

## 4. Gợi Ý 3 Hành Động Cải Thiện Trong Tháng Tới Cho Trưởng Phòng

1. 🎯 **Hành động 1 (Tối ưu phân bổ tải công việc):**
   {{action_recommendation_1}}
2. 🔄 **Hành động 2 (Giải phóng nút thắt quy trình):**
   {{action_recommendation_2}}
3. 👥 **Hành động 3 (Đào tạo hoặc hỗ trợ kèm cặp):**
   {{action_recommendation_3}}

---
*Dữ liệu chi tiết từng công việc đã được tự động lưu trong file nội bộ của phòng. Vui lòng mở file đính kèm để đối soát chi tiết.*
