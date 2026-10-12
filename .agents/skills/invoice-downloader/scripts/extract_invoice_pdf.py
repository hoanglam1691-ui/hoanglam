import asyncio
import os
import sys
import re
from playwright.async_api import async_playwright
from render_invoice_template import async_render_invoice_to_pdf

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

JS_EXTRACTOR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "extract_invoice_data.js"))

async def print_invoice_to_pdf(page, browser_context, output_pdf_path, invoice_title="Hóa đơn điện tử"):
    """
    Tự động hóa quy trình trích xuất dữ liệu gốc và in hóa đơn sang PDF chuẩn mẫu hd1.pdf / hd2.pdf.
    """
    with open(JS_EXTRACTOR_PATH, "r", encoding="utf-8") as f:
        js_func = f.read()
        
    js_eval = f"""() => {{
        {js_func}
        return extractInvoiceData();
    }}"""
    
    invoice_data = await page.evaluate(js_eval)
    if not invoice_data or not invoice_data.get('seller_name'):
        raise ValueError("Không thể trích xuất dữ liệu từ Modal xem hóa đơn (.ant-modal-body)!")

    # Render sang PDF chuẩn mẫu hd1.pdf / hd2.pdf
    await async_render_invoice_to_pdf(
        invoice_data=invoice_data,
        output_pdf_path=output_pdf_path,
        browser_context=browser_context
    )

    if os.path.exists(output_pdf_path) and os.path.getsize(output_pdf_path) > 0:
        print(f"[V] Đã in thành công hóa đơn sang PDF chuẩn mẫu hd1/hd2 ({os.path.getsize(output_pdf_path):,} bytes): {output_pdf_path}", flush=True)
        return True
    else:
        raise RuntimeError(f"In hóa đơn thất bại hoặc file rỗng: {output_pdf_path}")

async def close_invoice_modal(page):
    """Đóng Modal chi tiết sau khi in xong để trả lại giao diện ban đầu."""
    close_btn = page.locator(".ant-modal-close").first
    if await close_btn.count() > 0:
        await close_btn.click()
        await asyncio.sleep(0.4)
