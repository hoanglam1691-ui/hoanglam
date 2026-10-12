# QUY TẮC VẬN HÀNH (CLEAR) & CƠ CHẾ BÀN GIAO (HANDOFF)

---

## 1. BỘ QUY TẮC VẬN HÀNH TOÀN HỆ THỐNG THEO KHUNG CLEAR

| Quy tắc | Nhóm nghiệp vụ | Nội dung quy tắc (CLEAR Specification) | Hành động khi vi phạm / Lỗi |
| :---: | :--- | :--- | :--- |
| **R1** | **Bảo mật & Phiên** | `Explicit`: Thông tin tài khoản (`MST`, `Password`) chỉ được nạp từ biến môi trường `.env`. Thời gian sống của Token $T_{expire} = 20\text{ phút}$. | Hủy phiên ngay lập tức; không ghi log chứa plain text password. |
| **R2** | **Tần suất & Rate-limit** | `Actionable`: Giữa 2 request tra cứu/tải file liên tiếp bắt buộc nghỉ tối thiểu $1.5\text{ giây}$. Số luồng tải song song tối đa $N = 3\text{ workers}$. | Tự động pause luồng $30\text{ giây}$ nếu máy chủ GDT trả về mã `429 Too Many Requests`. |
| **R3** | **Toàn vẹn Dữ liệu** | `Resilient`: Một hóa đơn chỉ được xác nhận tải thành công khi có đủ cả 2 file `.xml` ($>0\text{ bytes}$, có chữ ký) và `.pdf` ($>0\text{ bytes}$). | Đưa vào hàng đợi `Retry Queue`; không bàn giao cho Agent tiếp theo nếu thiếu 1 trong 2 file. |
| **R4** | **Bất biến Nội dung** | `Concise`: **Chỉ đọc và bóc tách metadata**. Tuyệt đối không can thiệp, định dạng lại hay chỉnh sửa bất kỳ byte nào trong file XML/PDF gốc. | Hệ thống chặn thao tác ghi đè nội dung; kích hoạt cảnh báo vi phạm bảo mật. |
| **R5** | **Định danh & Lưu trữ** | `Logical`: Mọi file phải được đổi tên chuẩn `[YYYYMMDD]_[MauSo]_[MST]_[KHHDon]_[SoHD].[ext]` và lưu đúng cây thư mục `outputs/HoaDon_MuaVao/{YYYY}/{MM}/{MauSo}/{MST}/`. | File không đúng mẫu tên bị cô lập tại thư mục `outputs/unclassified/`. |
| **R6** | **Chống Trùng lặp** | `Logical`: Trước khi tải/lưu, tính khóa duy nhất `Unique_Key = Hash(MST_NguoiBan + KHHDon + SoHDon)`. Nếu đã tồn tại trong Catalog $\rightarrow$ Bỏ qua. | Ghi log `DUPLICATE_SKIPPED` và tiếp tục hóa đơn kế tiếp. |

---

## 2. CƠ CHẾ BÀN GIAO DỮ LIỆU (HANDOFF SPECIFICATION)

### 2.1. Trạng thái Vòng đời Hóa đơn (Lifecycle States)
* `DISCOVERED`: Đã quét thấy trên web GDT.
* `VERIFIED`: Đã kiểm tra tính hợp lệ toán học & chữ ký số.
* `DOWNLOAD_PENDING`: Đang chờ tải file.
* `DOWNLOADED`: Đã tải đủ trọn bộ cặp XML + PDF vào thư mục tạm.
* `STORED`: Đã đổi tên chuẩn và lưu vào cây thư mục phân cấp.
* `FLAGGED`: Bị cảnh báo bất thường (cần duyệt tại Human Checkpoint).
* `FAILED`: Tải/xử lý thất bại sau 3 lần retry.

---

### 2.2. Chi tiết Giao thức Handoff JSON

#### Handoff 1: `Invoice Search Agent` $\rightarrow$ `Invoice Download Agent`
* **File:** `sample-data/manifests/invoices_manifest.json`
```json
{
  "batch_id": "BATCH_20261005_001",
  "generated_at": "2026-10-05T21:30:00",
  "total_records": 3,
  "items": [
    {
      "invoice_uid": "001065008691_C26MYY_0000240",
      "nbmst": "001065008691",
      "nbten": "HỘ KINH DOANH NGUYỄN QUỐC GIAO",
      "khmshdon": "2",
      "khhdon": "C26MYY",
      "shdon": "0000240",
      "tdlap": "2026-05-09",
      "tgtttbso": 5850000,
      "tgtthue": 0,
      "tgtttoan": 5850000,
      "mccqt": "M2-26-LNW6T-00000000305",
      "state": "DISCOVERED"
    }
  ]
}
```

#### Handoff 2: `Invoice Download Agent` $\rightarrow$ `Invoice Storage Agent`
* **File:** `sample-data/manifests/download_status.json`
```json
{
  "batch_id": "BATCH_20261005_001",
  "summary": { "requested": 3, "success": 3, "failed": 0 },
  "downloaded_items": [
    {
      "invoice_uid": "001065008691_C26MYY_0000240",
      "nbmst": "001065008691",
      "khmshdon": "2",
      "khhdon": "C26MYY",
      "shdon": "0000240",
      "tdlap": "2026-05-09",
      "raw_xml_path": "sample-data/raw_downloads/001065008691_C26MYY_0000240/raw.xml",
      "raw_pdf_path": "sample-data/raw_downloads/001065008691_C26MYY_0000240/raw.pdf",
      "xml_size_bytes": 18450,
      "pdf_size_bytes": 142300,
      "state": "DOWNLOADED"
    }
  ]
}
```

#### Handoff 3: `Invoice Storage Agent` $\rightarrow$ `Invoice Report Agent`
* **File:** `outputs/storage_catalog.json`
```json
{
  "catalog_version": "1.0",
  "total_archived": 3,
  "archived_invoices": [
    {
      "invoice_uid": "001065008691_C26MYY_0000240",
      "mau_so": "2",
      "ky_hieu": "C26MYY",
      "so_hd": "0000240",
      "ngay_lap": "2026-05-09",
      "mst_ban": "001065008691",
      "ten_ban": "HỘ KINH DOANH NGUYỄN QUỐC GIAO",
      "tong_tien_chua_thue": 5850000,
      "tien_thue": 0,
      "tong_thanh_toan": 5850000,
      "final_pdf_path": "outputs/HoaDon_MuaVao/2026/05/MauSo_2_BanHang/001065008691_HKD_NguyenQuocGiao/20260509_MS2_001065008691_C26MYY_0000240.pdf",
      "final_xml_path": "outputs/HoaDon_MuaVao/2026/05/MauSo_2_BanHang/001065008691_HKD_NguyenQuocGiao/20260509_MS2_001065008691_C26MYY_0000240.xml",
      "state": "STORED"
    }
  ]
}
```
