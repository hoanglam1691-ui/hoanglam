# My Workspace — Quy Tắc Vận Hành

## Dự Án
**Hệ Thống Tự Động Hóa Tìm Kiếm, Sắp Xếp & Tải Hóa Đơn Điện Tử Còn Thiếu**  
*Capstone Project — Khóa học Agentic AI with Google Antigravity*

## Chủ Sở Hữu
- **Tên:** Hoàng Lâm
- **Lĩnh vực:** Kế toán Doanh nghiệp & Quản trị Thuế
- **Mục tiêu tự động hóa:** Tự động hóa rà soát, tìm kiếm số hóa đơn điện tử còn thiếu thông qua Cổng Thuế `hoadondientu.gdt.gov.vn`, kích hoạt máy in ảo Microsoft Print to PDF xuất file PDF 1:1, phân loại cây thư mục Năm/Tháng/MST và lập bảng đối soát kế toán nội bộ.

## Sứ Mệnh Workspace
Workspace hỗ trợ tự động hóa toàn diện quy trình hoàn thiện hồ sơ chứng từ kế toán mua vào: giải quyết dứt điểm tình trạng thiếu file PDF hóa đơn gốc, loại bỏ nguy cơ rủi ro từ doanh nghiệp bỏ trốn bằng hàng rào kiểm toán Blacklist, và tiết kiệm 95% thời gian thủ công của kế toán.

## Quy Tắc Vận Hành (Rules)

### Quy tắc 1 — Tích lũy, không phá vỡ
Mỗi buổi học, tôi CHỈ thêm mới vào workspace. Không xóa bỏ hoặc thay thế các thành phần đã tạo trừ khi có lý do audit rõ ràng.

### Quy tắc 2 — PDCA bắt buộc
Mọi thay đổi quan trọng phải được ghi vào `docs/pdca-log.md`. Format: Plan → Do → Check → Act.

### Quy tắc 3 — Workspace checkpoint
Sau mỗi buổi học, tôi đọc bridge guide tương ứng và hoàn thành ít nhất 1 workspace checkpoint.

### Quy tắc 4 — Output vào đúng thư mục
- Draft content → `outputs/drafts/`
- Báo cáo → `outputs/reports/`
- Dữ liệu thực hành → `sample-data/`
- Hóa đơn lưu trữ → `outputs/HoaDon_LuuTru/`

### Quy tắc 5 — Bảo mật
Không đưa API key, mật khẩu, dữ liệu khách hàng thật vào workspace này.

## Lịch Sử Phát Triển

| Buổi | Ngày | Thêm gì vào workspace | Ghi chú |
|:----:|------|----------------------|---------|
| 1 | 2026-07-10 | Khởi tạo workspace, cấu trúc thư mục ban đầu | Hoàn thành |
| 2 | 2026-07-17 | Thiết lập nhật ký PDCA Log | Bắt đầu PDCA |
| 3 | 2026-07-24 | Tạo Skill chuyên môn đầu tiên (`ai4a:brainstorm`) | Expertise Skill |
| 4 | 2026-08-01 | Xây dựng pipeline OIPO (`ai4a:ops-analyst`) | ERP Split Pipeline |
| 5 | 2026-08-15 | Nâng cấp AI Agent theo khung MICRO | Lead Scoring Agent |
| 6 | 2026-08-25 | Nạp Knowledge Base và Rules vận hành | Tiêu chí chấm điểm |
| 7 | 2026-09-05 | Thiết kế Handoff Contracts & Schema | Luân chuyển dữ liệu |
| 8 | 2026-09-15 | Tổ chức & Audit toàn diện workspace | Báo cáo kiểm toán |
| 9 | 2026-09-25 | Cơ chế Tự phục hồi dữ liệu (Self-Healing) | Marketing & PM |
| 10 | 2026-10-05 | Khung SCOPE Capstone Project Hóa đơn GDT | Scope & Architecture |
| 11 | 2026-10-14 | Hoàn thiện trọn bộ 7 thành tố Workspace Capstone | System Assembly |
