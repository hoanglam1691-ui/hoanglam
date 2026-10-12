# Đặc Tả Kỹ Thuật: Cơ Chế In Hóa Đơn & Xuất Microsoft Print to PDF

Tài liệu này mô tả chi tiết cơ chế kỹ thuật để chuyển đổi màn hình xem hóa đơn trên website `hoadondientu.gdt.gov.vn` thành file PDF chất lượng cao thông qua tính năng In hóa đơn kết hợp máy in ảo (**Microsoft Print to PDF** / **Chromium Native Print Engine**).

---

## 1. Nguyên Lý Hoạt Động Của Tính Năng "In Hóa Đơn"

Khi người dùng thao tác thủ công:
1. Mở màn hình Xem chi tiết hóa đơn.
2. Bấm nút **In** / Nhấn `Ctrl + P`.
3. Hộp thoại in của trình duyệt xuất hiện:
   - **Máy in đích (Destination)**: Chọn `Microsoft Print to PDF` (hoặc `Save as PDF`).
   - **Bố cục (Layout)**: `Dọc (Portrait)`.
   - **Khổ giấy (Paper size)**: `A4`.
   - **Tùy chọn khác**: Tích chọn **"Đồ họa nền" (Background graphics)** để hiển thị đầy đủ hoa văn nền, màu sắc tiêu đề bảng và watermark chữ ký số.
   - **Lề (Margins)**: Tối thiểu / Tùy chỉnh (8mm top/bottom, 6mm left/right).
4. Bấm **Lưu / Print** -> Chọn thư mục lưu -> Lưu file `.pdf`.

---

## 2. Tự Động Hóa Qua Chrome DevTools Protocol (CDP) & Playwright

Trong môi trường tự động hóa, nếu để hộp thoại Print của Windows bật lên thì luồng tự động sẽ bị chặn (modal blocking). Do đó, AI Agent sử dụng cơ chế **DevTools Protocol Print Engine** tương đương 100% với máy in Microsoft Print to PDF nhưng được thực thi ngầm tự động:

```python
async def print_invoice_to_pdf(page, browser_context, output_pdf_path, invoice_title="Hóa đơn điện tử"):
    # 1. Trích xuất nội dung hóa đơn và toàn bộ Stylesheet gốc của Portal
    render_data = await page.evaluate("""
        () => {
            const styles = Array.from(document.querySelectorAll('style, link[rel="stylesheet"]'))
                               .map(el => el.outerHTML)
                               .join('\\n');
            const modal = document.querySelector('.ant-modal-body') || document.querySelector('.ant-modal-content');
            const modalHtml = modal ? modal.innerHTML : '';
            return { styles, modalHtml };
        }
    """)
    
    if not render_data['modalHtml']:
        raise ValueError("Không tìm thấy nội dung hóa đơn để in!")

    # 2. Định hình chuẩn in ấn A4 (Microsoft Print to PDF Specs)
    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{invoice_title}</title>
{render_data['styles']}
<style>
@page {{
    size: A4 portrait;
    margin: 8mm 6mm;
}}
body {{
    background: #ffffff !important;
    padding: 0 !important;
    margin: 0 !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}}
.ant-modal-body {{
    padding: 0 !important;
}}
</style>
</head>
<body class="ant-modal-open">
<div class="ant-modal-body">
{render_data['modalHtml']}
</div>
</body>
</html>"""

    # 3. Kích hoạt engine in ảo Microsoft Print to PDF
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    render_page = await browser_context.new_page()
    try:
        await render_page.set_content(full_html, wait_until="networkidle")
        await asyncio.sleep(0.5) # Chờ render font chữ, hoa văn, mã QR và chữ ký số
        await render_page.pdf(
            path=output_pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "8mm", "bottom": "8mm", "left": "6mm", "right": "6mm"},
            prefer_css_page_size=True
        )
    finally:
        await render_page.close()

    return os.path.exists(output_pdf_path) and os.path.getsize(output_pdf_path) > 0
```

---

## 3. Bảng Tham Số In Ấn Chuẩn (Print Settings Matrix)

| Tham Số | Cấu Hình Khuyến Nghị | Mục Đích |
|:---|:---|:---|
| **Destination Printer** | `Microsoft Print to PDF` / `Chromium Engine` | Đảm bảo tính tương thích và kết xuất PDF chuẩn vector |
| **Page Format** | `A4` (210 x 297 mm) | Khổ giấy tiêu chuẩn kế toán và lưu trữ hóa đơn |
| **Print Background** | `True` (`-webkit-print-color-adjust: exact`) | In đầy đủ logo, background, watermark chữ ký số |
| **Margins** | Top: 8mm, Bottom: 8mm, Left: 6mm, Right: 6mm | Bố cục vừa vặn 1 trang A4, không bị tràn dòng |
| **Font Rendering** | Unicode UTF-8 | Chữ tiếng Việt sắc nét, không bị nhòe hay lỗi font |
