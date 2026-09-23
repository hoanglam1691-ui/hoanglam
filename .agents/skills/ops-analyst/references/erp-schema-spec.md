# ERP Schema Specification

> **Tài liệu tham chiếu chuẩn hóa dữ liệu ERP**  
> Thuộc Skill: `ai4a:ops-analyst`  
> Phiên bản: 1.0.0  

Tài liệu này định nghĩa bảng ánh xạ cột, kiểu dữ liệu và quy tắc xử lý làm sạch dữ liệu đầu vào được xuất ra từ các hệ thống ERP / CRM / Project Management phổ biến (SAP, Odoo, Oracle, Base, Jira, Lark...).

---

## 1. Bảng Ánh Xạ Các Cột Dữ Liệu Cốt Lõi (Field Mapping)

| Tên chuẩn hóa (Standard Field) | Tên tiếng Việt thường gặp | Tên tiếng Anh thường gặp | Kiểu dữ liệu | Bắt buộc | Ghi chú xử lý |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `employee_id` | Mã NV, Mã nhân viên, ID NV | Employee ID, Staff ID, Emp_ID | String / Text | Có | Xóa khoảng trắng đầu cuối, giữ nguyên dạng chuỗi (không chuyển thành số để tránh mất số 0 đầu) |
| `employee_name` | Họ và tên, Tên NV, Nhân viên | Full Name, Employee Name, Staff | String / Text | Có | Chuẩn hóa Title Case (viết hoa chữ cái đầu) |
| `department` | Bộ phận, Phòng ban, Khối | Department, Division, Team, Dept | String / Text | Có | Nhóm các biến thể (vd: "KD", "Sales", "Kinh doanh" về một tên chuẩn "Kinh Doanh") |
| `record_date` | Ngày, Ngày ghi nhận, Ngày tạo | Date, Created Date, Log Date | Date | Có | Chuyển về định dạng ISO `YYYY-MM-DD` |
| `output_units` | Sản lượng, Số lượng, Điểm task | Output, Units, Volume, Quantity | Numeric (Float/Int) | Có | Mặc định điền `0` nếu ô trống |
| `revenue` | Doanh số, Doanh thu (VND) | Revenue, Sales, Total Amount | Numeric (Float) | Không | Loại bỏ ký tự tiền tệ (`đ`, `VND`, `$`) và dấu chấm/phẩy phân cách hàng nghìn |
| `task_status` | Trạng thái, Tình trạng, Kết quả | Status, Task Status, State | String | Có | Ánh xạ về 4 trạng thái chuẩn (xem mục 2) |
| `due_date` | Hạn chót, Ngày đến hạn | Due Date, Deadline, Target Date | Date | Không | Dùng để đối soát hạn hoàn thành nếu có |

---

## 2. Chuẩn Hóa Trạng Thái Công Việc (Status Standardization)

Tất cả các trạng thái trong file xuất dữ liệu phải được quy về 4 nhóm chuẩn sau:

| Nhóm chuẩn (Standard Status) | Các biến thể tiếng Việt | Các biến thể tiếng Anh | Trọng số hoàn thành |
| :--- | :--- | :--- | :---: |
| **`Completed`** | Hoàn thành, Đã xong, Đạt, Thành công, Đã giao | Completed, Done, Closed, Finished, Delivered, Resolved | 100% |
| **`In Progress`** | Đang làm, Đang xử lý, Chờ duyệt, Tiếp diễn | In Progress, Doing, Pending, Processing, On Hold | 50% (được tính là đang theo dõi) |
| **`Delayed`** | Trễ hạn, Quá hạn, Chậm tiến độ, Treo | Delayed, Overdue, Late, Behind Schedule | 0% (Tính vào tỷ lệ trễ hạn) |
| **`Cancelled`** | Hủy, Thất bại, Bỏ dở, Không đạt | Cancelled, Dropped, Failed, Rejected | Loại trừ khỏi mẫu tính SLA nếu có lý do khách quan |

---

## 3. Quy Tắc Làm Sạch Dữ Liệu (Cleansing Rules)

1. **Dòng rỗng (Empty Rows):** Nếu cả 3 trường `employee_id`, `department`, và `record_date` đều rỗng thì loại bỏ bản ghi.
2. **Khuyết thiếu phòng ban (Missing Department):** Nếu `department` để trống nhưng có `employee_id`, cố gắng tra cứu từ hồ sơ nhân sự trước đó. Nếu vẫn không có, gán vào nhóm `[Chưa Phân Loại]`.
3. **Format ngày tháng không đồng nhất:**
   - Hỗ trợ tự động nhận diện cả hai dạng `DD/MM/YYYY` và `YYYY-MM-DD`.
   - Lưu ý kiểm tra tháng trước ngày (`MM/DD/YYYY` theo chuẩn US) nếu ngày $\le 12$.
4. **Dữ liệu trùng lặp (Duplicate Detection):** Nếu trùng đồng thời cả `employee_id`, `record_date`, và `task_name` với cùng trạng thái, chỉ giữ lại 1 bản ghi mới nhất.
