# Báo Cáo Tổng Quan Vận Hành Toàn Công Ty — Tháng {{month}}

> **Đối tượng nhận:** Ban Giám Đốc (CEO, COO)  
> **Người lập báo cáo:** Operations Analyst Agent (`ai4a:ops-analyst`)  
> **Ngày xuất bản:** {{export_date}}  
> **Nguồn dữ liệu:** Dữ liệu ERP xuất kỳ {{month}}  

---

## 1. Tóm Tắt Điều Hành (Executive Summary)

- **Điểm số sức khỏe vận hành toàn diện:** `{{health_score}}/100` (Xếp loại: `{{health_status}}`)
- **Tổng sản lượng / Doanh số toàn công ty:** `{{total_volume_or_revenue}}`
- **Tỷ lệ hoàn thành công việc chung:** `{{overall_completion_rate}}%` (So với tháng trước: `{{completion_rate_trend}}`)
- **Tỷ lệ công việc trễ hạn (SLA Delay Rate):** `{{overall_delay_rate}}%`
- **Thông điệp cốt lõi:**
  > *{{executive_takeaway_message}}*

---

## 2. Bảng Điểm Hiệu Hiệu Quả Từng Phòng Ban (Cross-Department Scorecard)

| Bộ phận | Nhân sự | Tổng Task | Hoàn thành | Đang làm | Trễ hạn | Tỷ lệ HT (%) | Tỷ lệ trễ (%) | Trạng thái |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Kinh Doanh** | {{sales_headcount}} | {{sales_tasks}} | {{sales_done}} | {{sales_doing}} | {{sales_late}} | {{sales_comp_pct}}% | {{sales_late_pct}}% | {{sales_status}} |
| **Kỹ Thuật** | {{tech_headcount}} | {{tech_tasks}} | {{tech_done}} | {{tech_doing}} | {{tech_late}} | {{tech_comp_pct}}% | {{tech_late_pct}}% | {{tech_status}} |
| **Vận Hành** | {{ops_headcount}} | {{ops_tasks}} | {{ops_done}} | {{ops_doing}} | {{ops_late}} | {{ops_comp_pct}}% | {{ops_late_pct}}% | {{ops_status}} |
| **CSKH** | {{cs_headcount}} | {{cs_tasks}} | {{cs_done}} | {{cs_doing}} | {{cs_late}} | {{cs_comp_pct}}% | {{cs_late_pct}}% | {{cs_status}} |

---

## 3. Các Điểm Nghẽn Vận Hành Trọng Yếu (Operational Bottlenecks)

1. **Điểm nghẽn 1: {{bottleneck_1_title}}**
   - *Phòng ban ảnh hưởng:* {{bottleneck_1_dept}}
   - *Biểu hiện:* {{bottleneck_1_desc}}
   - *Hậu quả:* {{bottleneck_1_impact}}
2. **Điểm nghẽn 2: {{bottleneck_2_title}}**
   - *Phòng ban ảnh hưởng:* {{bottleneck_2_dept}}
   - *Biểu hiện:* {{bottleneck_2_desc}}
   - *Hậu quả:* {{bottleneck_2_impact}}

---

## 4. Tuyên Dương Đội Ngũ & Nhân Sự Xuất Sắc (Recognition)

- 🏆 **Phòng ban xuất sắc nhất tháng:** `{{best_department}}` (Tỷ lệ đúng hạn {{best_dept_comp_pct}}%, không có task tồn quá 3 ngày).
- 🌟 **Top 3 nhân sự đạt năng suất cao nhất:**
  1. `{{top_emp_1}}` (Bộ phận {{top_emp_1_dept}}): Sản lượng {{top_emp_1_metric}}
  2. `{{top_emp_2}}` (Bộ phận {{top_emp_2_dept}}): Sản lượng {{top_emp_2_metric}}
  3. `{{top_emp_3}}` (Bộ phận {{top_emp_3_dept}}): Sản lượng {{top_emp_3_metric}}

---

## 5. Kiến Nghị Hành Động Chiến Lược Cho Ban Giám Đốc (Action Items)

- [ ] **Ưu tiên 1 (Giải quyết ngay trong tuần 1):** {{action_priority_1}}
- [ ] **Ưu tiên 2 (Điều chỉnh quy trình trong tháng):** {{action_priority_2}}
- [ ] **Ưu tiên 3 (Kế hoạch phân bổ lại nguồn lực):** {{action_priority_3}}

---
*Báo cáo được tự động khởi tạo bởi Workspace AI cá nhân tuân thủ khung PDCA & OIPO.*
