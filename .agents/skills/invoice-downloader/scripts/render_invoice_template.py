import os
import sys
import re
import datetime
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resources/invoice_template.html"))

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
]

def get_chrome_executable():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    return None

VIETNAMESE_NUMBERS = {
    0: "không", 1: "một", 2: "hai", 3: "ba", 4: "bốn",
    5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"
}

def number_to_vietnamese_words(n):
    """Chuyển đổi số tiền thành chữ tiếng Việt chuẩn kế toán."""
    try:
        n = int(round(float(n)))
    except:
        return ""
    if n == 0:
        return "Không đồng."
    if n < 0:
        return "Âm " + number_to_vietnamese_words(-n)
        
    units = ["", "nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ"]
    
    def read_block_3(num, is_highest):
        h = num // 100
        t = (num % 100) // 10
        u = num % 10
        res = []
        
        if h > 0 or not is_highest:
            res.append(f"{VIETNAMESE_NUMBERS[h]} trăm")
            
        if t > 1:
            res.append(f"{VIETNAMESE_NUMBERS[t]} mươi")
            if u == 1:
                res.append("mốt")
            elif u == 5:
                res.append("lăm")
            elif u > 0:
                res.append(VIETNAMESE_NUMBERS[u])
        elif t == 1:
            res.append("mười")
            if u == 5:
                res.append("lăm")
            elif u > 0:
                res.append(VIETNAMESE_NUMBERS[u])
        elif t == 0:
            if u > 0:
                if h > 0 or not is_highest:
                    res.append("lẻ")
                res.append(VIETNAMESE_NUMBERS[u])
                
        return " ".join(res)

    blocks = []
    temp = n
    while temp > 0:
        blocks.append(temp % 1000)
        temp //= 1000
        
    words = []
    for i in reversed(range(len(blocks))):
        b = blocks[i]
        if b > 0:
            b_words = read_block_3(b, i == len(blocks) - 1)
            unit = units[i]
            if unit:
                words.append(f"{b_words} {unit}")
            else:
                words.append(b_words)
                
    result = " ".join(words).strip()
    result = result[0].upper() + result[1:] + " đồng."
    return result

def generate_invoice_html(invoice_data):
    """
    Tạo nội dung HTML hoàn chỉnh từ Template chuẩn hd1.pdf / hd2.pdf.
    """
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Parse date
    date_obj = invoice_data.get("invoice_date") or invoice_data.get("ngay_lap") or datetime.date.today()
    if isinstance(date_obj, str):
        date_clean = re.sub(r'[^0-9]', '', date_obj)
        if len(date_clean) >= 8:
            ngay = invoice_data.get("ngay") or (date_clean[6:8] if date_clean.startswith('20') else date_clean[:2])
            thang = invoice_data.get("thang") or (date_clean[4:6] if date_clean.startswith('20') else date_clean[2:4])
            nam = invoice_data.get("nam") or (date_clean[:4] if date_clean.startswith('20') else date_clean[4:8])
        else:
            ngay = invoice_data.get("ngay", "01")
            thang = invoice_data.get("thang", "07")
            nam = invoice_data.get("nam", "2026")
    else:
        ngay = invoice_data.get("ngay") or f"{date_obj.day:02d}"
        thang = invoice_data.get("thang") or f"{date_obj.month:02d}"
        nam = invoice_data.get("nam") or f"{date_obj.year}"

    # Build Items Rows
    items = invoice_data.get("items", [])
    if not items:
        # Default single item
        items = [{
            "stt": "1",
            "tinh_chat": "Hàng hóa, dịch vụ",
            "loai_hang": "",
            "ten_hang": invoice_data.get("mat_hang", "Hàng hóa dịch vụ"),
            "dvt": invoice_data.get("dvt", "Lô/Gói"),
            "so_luong": "1",
            "don_gia": f"{invoice_data.get('tien_chua_thue', 0):,}" if isinstance(invoice_data.get('tien_chua_thue'), (int, float)) else str(invoice_data.get('tien_chua_thue', '')),
            "chiet_khau": "0",
            "thue_suat": str(invoice_data.get('thue_suat', '10%')),
            "thanh_tien": f"{invoice_data.get('tien_chua_thue', 0):,}" if isinstance(invoice_data.get('tien_chua_thue'), (int, float)) else str(invoice_data.get('tien_chua_thue', ''))
        }]

    item_rows_html = ""
    for it in items:
        item_rows_html += f"""
        <tr>
            <td class="text-center">{it.get('stt', '1')}</td>
            <td class="text-center">{it.get('tinh_chat', 'Hàng hóa, dịch vụ')}</td>
            <td class="text-center">{it.get('loai_hang', '')}</td>
            <td class="text-left"><b>{it.get('ten_hang', '')}</b></td>
            <td class="text-center">{it.get('dvt', '')}</td>
            <td class="text-right">{it.get('so_luong', '1')}</td>
            <td class="text-right">{it.get('don_gia', '')}</td>
            <td class="text-right">{it.get('chiet_khau', '')}</td>
            <td class="text-center">{it.get('thue_suat', '10%')}</td>
            <td class="text-right"><b>{it.get('thanh_tien', '')}</b></td>
        </tr>
        """

    # Format numbers
    tien_chua_thue = invoice_data.get("tien_chua_thue", 0)
    tien_thue = invoice_data.get("tien_thue", 0)
    tong_thanh_toan = invoice_data.get("tong_thanh_toan", "")
    
    tien_chua_thue_str = f"{tien_chua_thue:,}" if isinstance(tien_chua_thue, (int, float)) else str(tien_chua_thue)
    tien_thue_str = f"{tien_thue:,}" if isinstance(tien_thue, (int, float)) else str(tien_thue)
    tong_thanh_toan_str = f"{tong_thanh_toan:,}" if isinstance(tong_thanh_toan, (int, float)) else str(tong_thanh_toan)

    tien_chu = invoice_data.get("tien_chu")
    if not tien_chu and isinstance(tong_thanh_toan, (int, float)):
        tien_chu = number_to_vietnamese_words(tong_thanh_toan)
    elif not tien_chu:
        tien_chu = ""

    sign_date = invoice_data.get("sign_date", f"{nam}-{thang}-{ngay} 10:00:00")

    # Xử lý Hóa đơn điều chỉnh & Hóa đơn thay thế
    ref_type = str(invoice_data.get("ref_type", "")).upper()
    ref_note = str(invoice_data.get("ref_invoice_note", "")).strip()
    ref_mau_so = str(invoice_data.get("ref_mau_so", "")).strip()
    ref_ky_hieu = str(invoice_data.get("ref_ky_hieu", "")).strip()
    ref_so_hd = str(invoice_data.get("ref_so_hd", "")).strip()
    ref_ngay_lap = str(invoice_data.get("ref_ngay_lap", "")).strip()
    ref_ly_do = str(invoice_data.get("ref_ly_do", "")).strip()
    ref_van_ban = str(invoice_data.get("ref_van_ban", "")).strip()

    trang_thai = str(invoice_data.get("trang_thai", "")).lower()
    title_raw = str(invoice_data.get("title", "HOÁ ĐƠN GIÁ TRỊ GIA TĂNG"))

    # Tự động phát hiện nếu ref_type chưa được gán rõ
    if not ref_type:
        if "đã bị điều chỉnh" in trang_thai or "bị điều chỉnh" in trang_thai:
            ref_type = "BI_DIEU_CHINH"
        elif "đã bị thay thế" in trang_thai or "bị thay thế" in trang_thai:
            ref_type = "BI_THAY_THE"
        elif "điều chỉnh" in trang_thai or "điều chỉnh" in title_raw.lower() or "điều chỉnh cho" in ref_note.lower():
            ref_type = "DIEU_CHINH"
        elif "thay thế" in trang_thai or "thay thế" in title_raw.lower() or "thay thế cho" in ref_note.lower():
            ref_type = "THAY_THE"

    badge_html = ""
    banner_html = ""
    ref_row_html = ""
    invoice_title = title_raw

    if ref_type == "DIEU_CHINH":
        if "(ĐIỀU CHỈNH)" not in invoice_title.upper() and "ĐIỀU CHỈNH" not in invoice_title.upper():
            invoice_title = f"{invoice_title} (ĐIỀU CHỈNH)"
        badge_html = '<div class="invoice-badge-container"><span class="invoice-badge badge-adjustment">HÓA ĐƠN ĐIỀU CHỈNH</span></div>'
        
        detail_parts = []
        if ref_mau_so: detail_parts.append(f"ký hiệu mẫu số hóa đơn <b>{ref_mau_so}</b>")
        if ref_ky_hieu: detail_parts.append(f"ký hiệu hóa đơn <b>{ref_ky_hieu}</b>")
        if ref_so_hd:
            so_fmt = str(ref_so_hd).zfill(7) if str(ref_so_hd).isdigit() else str(ref_so_hd)
            detail_parts.append(f"số hóa đơn <b>{so_fmt}</b>")
        if ref_ngay_lap: detail_parts.append(f"ngày lập <b>{ref_ngay_lap}</b>")
        
        detail_str = ", ".join(detail_parts) if detail_parts else ref_note
        if not detail_str and ref_note:
            detail_str = ref_note
        elif not detail_str:
            detail_str = "hóa đơn gốc theo biên bản điều chỉnh"

        extra_str = ""
        if ref_ly_do: extra_str += f" &nbsp;|&nbsp; <i>Lý do: {ref_ly_do}</i>"
        if ref_van_ban: extra_str += f" &nbsp;|&nbsp; <i>Văn bản: {ref_van_ban}</i>"

        banner_html = f'<div class="ref-invoice-banner ref-banner-adjustment"><b>Điều chỉnh cho:</b> {detail_str}{extra_str}</div>'
        ref_row_html = f'<div class="info-row" style="margin-top: 2px;"><span class="info-label">Thông tin điều chỉnh:</span><span class="info-val"><b>{detail_str}{extra_str}</b></span></div>'

    elif ref_type == "THAY_THE":
        if "(THAY THẾ)" not in invoice_title.upper() and "THAY THẾ" not in invoice_title.upper():
            invoice_title = f"{invoice_title} (THAY THẾ)"
        badge_html = '<div class="invoice-badge-container"><span class="invoice-badge badge-replacement">HÓA ĐƠN THAY THẾ</span></div>'
        
        detail_parts = []
        if ref_mau_so: detail_parts.append(f"ký hiệu mẫu số hóa đơn <b>{ref_mau_so}</b>")
        if ref_ky_hieu: detail_parts.append(f"ký hiệu hóa đơn <b>{ref_ky_hieu}</b>")
        if ref_so_hd:
            so_fmt = str(ref_so_hd).zfill(7) if str(ref_so_hd).isdigit() else str(ref_so_hd)
            detail_parts.append(f"số hóa đơn <b>{so_fmt}</b>")
        if ref_ngay_lap: detail_parts.append(f"ngày lập <b>{ref_ngay_lap}</b>")
        
        detail_str = ", ".join(detail_parts) if detail_parts else ref_note
        if not detail_str and ref_note:
            detail_str = ref_note
        elif not detail_str:
            detail_str = "hóa đơn gốc theo thỏa thuận thay thế"

        extra_str = ""
        if ref_ly_do: extra_str += f" &nbsp;|&nbsp; <i>Lý do: {ref_ly_do}</i>"
        if ref_van_ban: extra_str += f" &nbsp;|&nbsp; <i>Văn bản: {ref_van_ban}</i>"

        banner_html = f'<div class="ref-invoice-banner ref-banner-replacement"><b>Thay thế cho:</b> {detail_str}{extra_str}</div>'
        ref_row_html = f'<div class="info-row" style="margin-top: 2px;"><span class="info-label">Thông tin thay thế:</span><span class="info-val"><b>{detail_str}{extra_str}</b></span></div>'

    elif ref_type == "BI_DIEU_CHINH":
        if "(ĐÃ BỊ ĐIỀU CHỈNH)" not in invoice_title.upper() and "BỊ ĐIỀU CHỈNH" not in invoice_title.upper():
            invoice_title = f"{invoice_title} (ĐÃ BỊ ĐIỀU CHỈNH)"
        badge_html = '<div class="invoice-badge-container"><span class="invoice-badge badge-adjusted">HÓA ĐƠN ĐÃ BỊ ĐIỀU CHỈNH</span></div>'
        
        detail_parts = []
        if ref_mau_so: detail_parts.append(f"ký hiệu mẫu số <b>{ref_mau_so}</b>")
        if ref_ky_hieu: detail_parts.append(f"ký hiệu <b>{ref_ky_hieu}</b>")
        if ref_so_hd:
            so_fmt = str(ref_so_hd).zfill(7) if str(ref_so_hd).isdigit() else str(ref_so_hd)
            detail_parts.append(f"số hóa đơn <b>{so_fmt}</b>")
        if ref_ngay_lap: detail_parts.append(f"ngày lập <b>{ref_ngay_lap}</b>")
        
        detail_str = ", ".join(detail_parts) if detail_parts else ref_note
        if not detail_str and ref_note:
            detail_str = ref_note
        elif not detail_str:
            detail_str = "Hóa đơn gốc đã phát sinh điều chỉnh theo quy định."

        banner_html = f'<div class="ref-invoice-banner ref-banner-adjusted"><b>Lưu ý:</b> {detail_str}</div>'
        ref_row_html = f'<div class="info-row" style="margin-top: 2px;"><span class="info-label">Trạng thái:</span><span class="info-val"><b>{detail_str}</b></span></div>'

    elif ref_type == "BI_THAY_THE":
        if "(ĐÃ BỊ THAY THẾ)" not in invoice_title.upper() and "BỊ THAY THẾ" not in invoice_title.upper():
            invoice_title = f"{invoice_title} (ĐÃ BỊ THAY THẾ)"
        badge_html = '<div class="invoice-badge-container"><span class="invoice-badge badge-replaced">HÓA ĐƠN ĐÃ BỊ THAY THẾ</span></div>'
        
        detail_parts = []
        if ref_mau_so: detail_parts.append(f"ký hiệu mẫu số <b>{ref_mau_so}</b>")
        if ref_ky_hieu: detail_parts.append(f"ký hiệu <b>{ref_ky_hieu}</b>")
        if ref_so_hd:
            so_fmt = str(ref_so_hd).zfill(7) if str(ref_so_hd).isdigit() else str(ref_so_hd)
            detail_parts.append(f"số hóa đơn <b>{so_fmt}</b>")
        if ref_ngay_lap: detail_parts.append(f"ngày lập <b>{ref_ngay_lap}</b>")
        
        detail_str = ", ".join(detail_parts) if detail_parts else ref_note
        if not detail_str and ref_note:
            detail_str = ref_note
        elif not detail_str:
            detail_str = "Hóa đơn gốc đã bị thay thế theo thỏa thuận."

        banner_html = f'<div class="ref-invoice-banner ref-banner-replaced"><b>Lưu ý:</b> {detail_str}</div>'
        ref_row_html = f'<div class="info-row" style="margin-top: 2px;"><span class="info-label">Trạng thái:</span><span class="info-val"><b>{detail_str}</b></span></div>'

    # Replace placeholders (support both single and double curly braces)
    replacements = {
        "INVOICE_TYPE_TITLE": invoice_title,
        "INVOICE_BADGE_HTML": badge_html,
        "REF_INVOICE_BANNER_HTML": banner_html,
        "REF_INFO_ROW_HTML": ref_row_html,
        "NGAY": ngay,
        "THANG": thang,
        "NAM": nam,
        "MCCQT": invoice_data.get("mccqt", ""),
        "MAU_SO": invoice_data.get("mau_so", "1"),
        "KY_HIEU": invoice_data.get("ky_hieu", ""),
        "SO_HOADON": str(invoice_data.get("so_hd", "")).zfill(7) if str(invoice_data.get("so_hd", "")).isdigit() else str(invoice_data.get("so_hd", "")),
        "SELLER_NAME": invoice_data.get("seller_name", ""),
        "SELLER_MST": invoice_data.get("seller_mst", ""),
        "SELLER_STORE_CODE": invoice_data.get("seller_store_code", ""),
        "SELLER_STORE_NAME": invoice_data.get("seller_store_name", ""),
        "SELLER_ADDRESS": invoice_data.get("seller_address", ""),
        "SELLER_PHONE": invoice_data.get("seller_phone", ""),
        "SELLER_BANK_ACC": invoice_data.get("seller_bank_acc", ""),
        "SELLER_BANK_NAME": invoice_data.get("seller_bank_name", ""),
        "BUYER_NAME": invoice_data.get("buyer_name", ""),
        "BUYER_CONTACT": invoice_data.get("buyer_contact", ""),
        "BUYER_MST": invoice_data.get("buyer_mst", ""),
        "BUYER_BUDGET_CODE": invoice_data.get("buyer_budget_code", ""),
        "BUYER_CCCD": invoice_data.get("buyer_cccd", ""),
        "BUYER_PASSPORT": invoice_data.get("buyer_passport", ""),
        "BUYER_ADDRESS": invoice_data.get("buyer_address", ""),
        "PAYMENT_METHOD": invoice_data.get("payment_method", "TM/CK"),
        "BUYER_BANK_ACC": invoice_data.get("buyer_bank_acc", ""),
        "CURRENCY": invoice_data.get("currency", "VND"),
        "BANG_KE_SO": invoice_data.get("bang_ke_so", ""),
        "BANG_KE_NGAY": invoice_data.get("bang_ke_ngay", ""),
        "ITEMS_ROWS": item_rows_html,
        "THUE_SUAT_SUMMARY": str(invoice_data.get("thue_suat", "10%")),
        "TONG_CHUA_THUE": tien_chua_thue_str,
        "TONG_TIEN_THUE": tien_thue_str,
        "TONG_TIEN_PHI": str(invoice_data.get("tong_tien_phi", "")),
        "TONG_CHIET_KHAU": str(invoice_data.get("tong_chiet_khau", "")),
        "TONG_THANH_TOAN": tong_thanh_toan_str,
        "TONG_TIEN_CHU": tien_chu,
        "SIGN_DATE": sign_date
    }

    for k, v in replacements.items():
        html = html.replace(f"{{{{{k}}}}}", str(v))
        html = html.replace(f"{{{k}}}", str(v))

    return html

def render_invoice_to_pdf(invoice_data, output_pdf_path):
    """
    Điền dữ liệu vào Template chuẩn hd1.pdf / hd2.pdf và xuất PDF sắc nét (sync).
    """
    html = generate_invoice_html(invoice_data)
    abs_path = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    
    chrome_exec = get_chrome_executable()
    with sync_playwright() as p:
        launch_kwargs = {"headless": True}
        if chrome_exec:
            launch_kwargs["executable_path"] = chrome_exec
        browser = p.chromium.launch(**launch_kwargs)
        page = browser.new_page()
        page.set_content(html, wait_until="networkidle")
        page.pdf(
            path=abs_path,
            format="A4",
            print_background=True,
            margin={"top": "8mm", "bottom": "8mm", "left": "6mm", "right": "6mm"},
            prefer_css_page_size=True
        )
        browser.close()

    print(f"[V] Đã render thành công PDF chuẩn mẫu hd1/hd2 ({os.path.getsize(abs_path):,} bytes) tại: {abs_path}", flush=True)
    return True

async def async_render_invoice_to_pdf(invoice_data, output_pdf_path, browser_context=None, extra_output_path=None):
    """
    Điền dữ liệu vào Template chuẩn hd1.pdf / hd2.pdf và xuất PDF sắc nét (async qua Playwright context).
    """
    html = generate_invoice_html(invoice_data)
    abs_path = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    if extra_output_path:
        os.makedirs(os.path.dirname(os.path.abspath(extra_output_path)), exist_ok=True)

    if browser_context:
        page = await browser_context.new_page()
        try:
            await page.set_content(html, wait_until="networkidle")
            await page.pdf(
                path=abs_path,
                format="A4",
                print_background=True,
                margin={"top": "8mm", "bottom": "8mm", "left": "6mm", "right": "6mm"},
                prefer_css_page_size=True
            )
            if extra_output_path:
                await page.pdf(
                    path=os.path.abspath(extra_output_path),
                    format="A4",
                    print_background=True,
                    margin={"top": "8mm", "bottom": "8mm", "left": "6mm", "right": "6mm"},
                    prefer_css_page_size=True
                )
        finally:
            await page.close()
    else:
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.set_content(html, wait_until="networkidle")
            await page.pdf(
                path=abs_path,
                format="A4",
                print_background=True,
                margin={"top": "8mm", "bottom": "8mm", "left": "6mm", "right": "6mm"},
                prefer_css_page_size=True
            )
            if extra_output_path:
                await page.pdf(
                    path=os.path.abspath(extra_output_path),
                    format="A4",
                    print_background=True,
                    margin={"top": "8mm", "bottom": "8mm", "left": "6mm", "right": "6mm"},
                    prefer_css_page_size=True
                )
            await browser.close()

    return True
