---
name: self-healing
description: Cơ chế tự phục hồi (Self-Healing) cho hệ thống quản lý dự án giáo dục, tự động làm sạch dữ liệu, chuẩn hóa ngày tháng và ghi log sự cố.
---

# Self-Healing Skill — Cơ Chế Tự Phục Hồi Dữ Liệu Quản Lý Dự Án

Skill này định nghĩa các nguyên tắc và thuật toán **Tự Phục Hồi (Self-Healing)** nhằm khắc phục tự động các lỗi dữ liệu, lỗi logic điều kiện và bất đồng bộ giữa các bảng dữ liệu trong hệ thống Quản lý Dự án Giáo dục ([du_lieu_du_an.xlsx](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/du_lieu_du_an.xlsx)) và API nhắc việc tự động ([educational_pm_api.py](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/sample-data/educational_pm_api.py)).

---

## 📌 3 Quy Tắc Vận Hành Bắt Buộc (Core Self-Healing Rules)

```mermaid
flowchart TD
    A[Dữ liệu thô từ Excel / API] --> B{Quy tắc 1: Lọc trạng thái}
    B -- Status == 'Done' hoặc 'Not Started' --> C[Loại bỏ khỏi danh sách nhắc việc]
    B -- Status == 'In Progress' / 'Pending' --> D{Quy tắc 2: Chuẩn hóa ngày}
    D --> E[Chuyển chuỗi tự nhiên 'tuan sau', 'ngay mai' sang YYYY-MM-DD]
    E --> F[Tạo thông báo nhắc việc chính xác]
    A -. Phát hiện lỗi/sai lệch .-> G{Quy tắc 3: Ghi log tự phục hồi}
    G --> H[Cập nhật backlog.md: Thời gian | Sự cố | Hành động | Trạng thái]
```

---

### 🔹 Quy Tắc 1 — Lọc Task Theo Trạng Thái Đúng
- **Nguyên lý:** Hệ thống nhắc việc **CHỈ** được phép xử lý các task đang trong quá trình thực hiện (`In Progress` / `Pending`).
- **Xử lý triệt để:**
  - Thực hiện liên kết (`JOIN / MERGE`) giữa Sheet `Ke_hoach` và Sheet `Tien_do` thông qua khóa chung `Task_ID`.
  - **LOẠI BỎ HOÀN TOÀN** các task có trạng thái:
    - `Done` (Đã hoàn thành — tránh nhắc việc gây phiền hà cho nhân sự).
    - `Not Started` (Chưa đến giai đoạn bắt đầu).
  - Không đọc đơn lẻ Sheet `Ke_hoach` mà thiếu kiểm tra trạng thái thực tế từ `Tien_do`.

---

### 🔹 Quy Tắc 2 — Chuẩn Hóa Ngày Sang Định Dạng ISO 8601 (`YYYY-MM-DD`)
- **Nguyên lý:** Mọi trường Deadline nhập dạng văn bản tự nhiên phải được máy học/thuật toán chuyển đổi về chuỗi ngày giờ tiêu chuẩn ISO 8601 (`YYYY-MM-DD`).
- **Bảng quy tắc ánh xạ (Date Mapping Rules):**

| Chuỗi Tự Nhiên Đầu Vào | Diễn Giải Logic | Quy Đổi Chuẩn (Mốc thời gian $T_0$) |
|:-----------------------|:----------------|:-------------------------------------|
| `'hom nay'`, `'today'` | Cùng ngày hiện tại | $T_0 \rightarrow$ `YYYY-MM-DD` |
| `'ngay mai'`, `'tomorrow'` | Ngày kế tiếp | $T_0 + 1\text{ ngày} \rightarrow$ `YYYY-MM-DD` |
| `'ngay kia'` | 2 ngày tới | $T_0 + 2\text{ ngày} \rightarrow$ `YYYY-MM-DD` |
| `'tuan sau'`, `'next week'` | 7 ngày tới | $T_0 + 7\text{ ngày} \rightarrow$ `YYYY-MM-DD` |
| `'gap'`, `'urgent'`, `'asap'` | Ưu tiên xử lý ngay | $T_0 + 1\text{ ngày}$ kèm cờ `[URGENT]` |
| Định dạng khác (`DD/MM/YYYY`, `YYYY/MM/DD`) | Chuẩn hóa format | Đưa về format duy nhất `YYYY-MM-DD` |

---

### 🔹 Quy Tắc 3 — Ghi Nhật Ký Mọi Hành Động Sửa Chữa Vào `backlog.md`
- **Nguyên lý:** Mọi hành vi phát hiện lỗi bất thường (Anomalies), tự động vá lỗi (Self-Repair) hoặc chuẩn hóa dữ liệu đều phải được lưu vết minh bạch vào file `backlog.md` tại thư mục gốc của workspace.
- **Cấu trúc bảng Audit Trail bắt buộc:**

```markdown
| Thời gian | Sự cố | Hành động | Trạng thái |
|:---|:---|:---|:---:|
| YYYY-MM-DD HH:MM:SS | [Mô tả chi tiết sự cố phát hiện] | [Giải pháp tự phục hồi đã áp dụng] | [Trạng thái khắc phục] |
```

---

## 🛠️ Code Mẫu Tích Hợp Cho `educational_pm_api.py`

```python
import datetime
import os
import re
import pandas as pd
from fastapi import FastAPI

app = FastAPI(title="Educational PM Auto-Remind API (Self-Healing Enabled)")

FILE_PATH = "sample-data/du_lieu_du_an.xlsx"
BACKLOG_PATH = "backlog.md"

def normalize_deadline(val, ref_date=None):
    """Quy tắc 2: Chuẩn hóa ngày tự nhiên sang ISO 8601 (YYYY-MM-DD)"""
    if ref_date is None:
        ref_date = datetime.date.today()
        
    if pd.isna(val):
        return ref_date.strftime("%Y-%m-%d"), "Missing Date Defaulted"
        
    val_str = str(val).strip().lower()
    
    # Kiểm tra format YYYY-MM-DD sẵn có
    if re.match(r'^\d{4}-\d{2}-\d{2}$', val_str):
        return val_str, None
        
    # Xử lý chuỗi tự nhiên
    if "hom nay" in val_str or "today" in val_str:
        return ref_date.strftime("%Y-%m-%d"), f"Converted '{val}' -> today"
    elif "ngay mai" in val_str or "tomorrow" in val_str:
        d = ref_date + datetime.timedelta(days=1)
        return d.strftime("%Y-%m-%d"), f"Converted '{val}' -> +1 day"
    elif "tuan sau" in val_str or "next week" in val_str:
        d = ref_date + datetime.timedelta(days=7)
        return d.strftime("%Y-%m-%d"), f"Converted '{val}' -> +7 days"
    elif "gap" in val_str or "urgent" in val_str or "asap" in val_str:
        d = ref_date + datetime.timedelta(days=1)
        return d.strftime("%Y-%m-%d"), f"Converted urgent '{val}' -> +1 day"
    
    # Parse ngày thông thường nếu có
    try:
        dt = pd.to_datetime(val)
        return dt.strftime("%Y-%m-%d"), f"Formatted '{val}' to ISO"
    except Exception:
        return ref_date.strftime("%Y-%m-%d"), f"Unrecognized date '{val}', defaulted"

def log_to_backlog(issues):
    """Quy tắc 3: Ghi nhật ký mọi hành động sửa chữa vào backlog.md"""
    if not issues:
        return
    
    file_exists = os.path.exists(BACKLOG_PATH)
    lines = []
    if not file_exists:
        lines.append("# NHẬT KÝ TỰ PHỤC HỒI HỆ THỐNG (SELF-HEALING AUDIT LOG)\n")
        lines.append("| Thời gian | Sự cố | Hành động | Trạng thái |")
        lines.append("|:---|:---|:---|:---:|")
        
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for issue, action, status in issues:
        lines.append(f"| {now_str} | {issue} | {action} | {status} |")
        
    with open(BACKLOG_PATH, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

@app.get("/auto-remind")
def auto_remind():
    issues_logged = []
    
    # Đọc dữ liệu từ 3 sheet
    df_tasks = pd.read_excel(FILE_PATH, sheet_name='Ke_hoach')
    df_status = pd.read_excel(FILE_PATH, sheet_name='Tien_do')
    df_staff = pd.read_excel(FILE_PATH, sheet_name='Nhan_su')
    
    # QUY TẮC 1: Merge để lấy trạng thái đúng & lọc 'In Progress' / 'Pending'
    df_merged = pd.merge(df_tasks, df_status, on='Task_ID', how='inner')
    
    # Kiểm tra các task Done bị lọc bỏ
    done_count = len(df_merged[df_merged['Status'].str.strip().str.lower() == 'done'])
    if done_count > 0:
        issues_logged.append((
            f"Phát hiện {done_count} task đã 'Done' trong Ke_hoach",
            "Đã lọc loại bỏ các task Done, chỉ giữ lại 'In Progress/Pending'",
            "Đã khắc phục"
        ))
        
    # Chỉ giữ task chưa hoàn thành
    active_tasks = df_merged[df_merged['Status'].str.strip().str.lower().isin(['in progress', 'pending'])].copy()
    
    # QUY TẮC 2: Chuẩn hóa ngày deadline
    reminders = []
    date_fix_count = 0
    
    for _, row in active_tasks.iterrows():
        assignee = row['Assignee']
        task_name = row['Task_Name']
        raw_deadline = row['Deadline']
        
        iso_deadline, fix_msg = normalize_deadline(raw_deadline)
        if fix_msg:
            date_fix_count += 1
            
        msg = f"🔔 NHẮC VIỆC: {assignee} đang xử lý '{task_name}', hạn chót: {iso_deadline} (Status: {row['Status']})"
        reminders.append({
            "task_id": row['Task_ID'],
            "assignee": assignee,
            "task_name": task_name,
            "original_deadline": str(raw_deadline),
            "normalized_deadline": iso_deadline,
            "message": msg
        })
        
    if date_fix_count > 0:
        issues_logged.append((
            f"Phát hiện {date_fix_count} deadline dạng chuỗi tự nhiên ('tuan sau', 'ngay mai', 'gap')",
            "Tự động chuẩn hóa toàn bộ về định dạng chuẩn ISO 8601 (YYYY-MM-DD)",
            "Đã khắc phục"
        ))
        
    # QUY TẮC 3: Ghi log
    log_to_backlog(issues_logged)
    
    return {
        "status": "Success",
        "total_active_tasks": len(reminders),
        "self_healing_applied": len(issues_logged) > 0,
        "reminders": reminders
    }
```
