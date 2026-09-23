"""
Hệ thống chấm điểm Lead Bất Động Sản tự động (Python Engine)
Hỗ trợ đọc file CSV nội bộ hoặc tải trực tiếp từ Google Sheets.
Tích hợp tiêu chuẩn chấm điểm 5 tiêu chí & tieu_chi_cham_diem.txt.
"""

import sys
import os
import re
import csv
import json
import urllib.request

# Ensure UTF-8 output on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Định nghĩa bảng từ khóa và trọng số chấm điểm
SCORING_RULES = {
    # 1. TIÊU CHÍ CỘNG ĐIỂM VIP (+50 điểm)
    "vip_triggers": [
        (r"(20\s*tỷ|30\s*tỷ|50\s*tỷ|100\s*tỷ|ngân sách không thành vấn đề|tài chính mạnh|tài chính cực mạnh|không thành vấn đề)", 50, "Ngân sách VIP >= 20 tỷ / Tài chính cực mạnh"),
        (r"(penthouse|biệt thự đơn lập|shophouse mặt đường|quỹ đất công nghiệp|sàn văn phòng diện tích lớn|trên 2000m2)", 50, "Sản phẩm BĐS cao cấp / Quy mô lớn"),
        (r"(quận 1|ven sông|vinhomes ocean park|phú mỹ hưng)", 30, "Vị trí đắc địa / Khu đô thị cao cấp"),
        (r"(chủ doanh nghiệp|nhà đầu tư chuyên nghiệp|mua sỉ|mua số lượng lớn)", 40, "Chân dung VIP: Chủ DN / Mua sỉ"),
        (r"(pháp lý chuẩn 100%|sổ hồng riêng|muốn gặp trực tiếp chủ đầu tư|đàm phán)", 30, "Tính cấp thiết cao & Pháp lý chuẩn")
    ],
    
    # 2. TIÊU CHÍ CỘNG ĐIỂM TẦM TRUNG / TIỀM NĂNG (10 - 25 điểm)
    "warm_triggers": [
        (r"(8-10\s*tỷ|5-7\s*tỷ|4-5\s*tỷ|3-10\s*tỷ|2-3\s*tỷ)", 20, "Ngân sách rõ ràng phân khúc 2-10 tỷ"),
        (r"(căn hộ 2pn|nhà phố liền kề|đất nền vùng ven|thuê mặt bằng|mặt bằng kinh doanh)", 20, "Loại hình tiêu chuẩn có nhu cầu thực"),
        (r"(cuối tuần này|ngay trong tháng|cần ký hợp đồng dài hạn|muốn đi xem nhà)", 25, "Thời gian mua/thuê cấp thiết"),
        (r"(cần hỗ trợ vay|cân nhắc chính sách|tư vấn thêm|chiết khấu)", 15, "Đang cân nhắc phương án tài chính")
    ],

    # 3. TIÊU CHÍ TRỪ ĐIỂM / KHÁCH RÁC (-50 đến -100 điểm)
    "cold_triggers": [
        (r"(nhầm số|không có nhu cầu|dữ liệu cũ|nhầm ngành)", -60, "Không có nhu cầu / Dữ liệu rác"),
        (r"(thuê bao|không bắt máy|không phản hồi zalo|gọi nhiều lần)", -50, "Thông tin liên lạc lỗi / Không tương tác"),
        (r"(hỏi giá cho vui|chưa có ý định mua|thái độ không hợp tác)", -50, "Khách không thiện chí"),
        (r"(quận 1 giá 1|q1 giá 1|giá 1-2 tỷ|vài trăm triệu|thuê nguyên căn giá 2 triệu)", -60, "Yêu cầu phi thực tế / Ảo tưởng giá"),
        (r"(bảo hiểm|vay vốn|mời chào dịch vụ|quảng cáo)", -80, "Spam / Mời chào dịch vụ khác")
    ]
}

def analyze_lead(text):
    text_lower = text.lower() if text else ""
    
    # Khởi tạo điểm cho từng tiêu chí
    score_budget = 10     # Tiêu chí 1: Ngân sách (0 - 35)
    score_interest = 10   # Tiêu chí 2: Loại hình & Vị trí (0 - 25)
    score_timeline = 10   # Tiêu chí 3: Thời gian & Cấp thiết (0 - 20)
    score_persona = 5     # Tiêu chí 4: Chân dung & Nguồn (0 - 15)
    score_engagement = 5  # Tiêu chí 5: Tương tác & Thiện chí (0 - 10)
    
    reasons = []
    is_vip = False
    is_junk = False

    # 1. TIÊU CHÍ TRỪ ĐIỂM NẶNG / RÁC
    if re.search(r"(nhầm số|không có nhu cầu|dữ liệu cũ|nhầm ngành)", text_lower):
        score_persona = -50
        is_junk = True
        reasons.append("[-50] Dữ liệu rác/Nhầm số")
        
    if re.search(r"(thuê bao|không bắt máy|không phản hồi zalo|gọi nhiều lần)", text_lower):
        score_engagement = -40
        is_junk = True
        reasons.append("[-40] Không liên lạc được/Thuê bao")
        
    if re.search(r"(hỏi giá cho vui|chưa có ý định mua|thái độ không hợp tác)", text_lower):
        score_timeline = -40
        is_junk = True
        reasons.append("[-40] Không thiện chí/Hỏi cho vui")
        
    if re.search(r"(quận 1 giá 1|q1 giá 1|giá 1-2 tỷ|vài trăm triệu|thuê nguyên căn giá 2 triệu)", text_lower):
        score_budget = -50
        is_junk = True
        reasons.append("[-50] Yêu cầu phi thực tế/Ảo tưởng giá")

    if re.search(r"(bảo hiểm|vay vốn|mời chào dịch vụ|quảng cáo)", text_lower):
        score_persona = -80
        is_junk = True
        reasons.append("[-80] Spam/Quảng cáo dịch vụ")

    if not is_junk:
        # Tiêu chí 1: Ngân sách
        if re.search(r"(20\s*tỷ|30\s*tỷ|50\s*tỷ|100\s*tỷ|tài chính cực mạnh|tài chính mạnh|không thành vấn đề)", text_lower):
            score_budget = 35
            is_vip = True
            reasons.append("[+35] Ngân sách VIP >= 20 tỷ / Tài chính mạnh")
        elif re.search(r"(8-10\s*tỷ|5-7\s*tỷ|4-5\s*tỷ|3-10\s*tỷ)", text_lower):
            score_budget = 25
            reasons.append("[+25] Ngân sách tầm trung 4-10 tỷ")
        elif re.search(r"(2-3\s*tỷ|dưới 50 triệu)", text_lower):
            score_budget = 15
            reasons.append("[+15] Ngân sách phân khúc phổ thông")

        # Tiêu chí 2: Loại hình & Vị trí
        if re.search(r"(penthouse|biệt thự đơn lập|quỹ đất công nghiệp|sàn văn phòng diện tích lớn|trên 2000m2)", text_lower):
            score_interest = 25
            is_vip = True
            reasons.append("[+25] Phân khúc siêu cao cấp / Diện tích lớn")
        elif re.search(r"(quận 1|ven sông|vinhomes ocean park|phú mỹ hưng)", text_lower):
            score_interest = 20
            reasons.append("[+20] Vị trí trung tâm / Đại đô thị cao cấp")
        elif re.search(r"(căn hộ 2pn|nhà phố liền kề|đất nền vùng ven|thuê mặt bằng)", text_lower):
            score_interest = 15
            reasons.append("[+15] Nhu cầu sản phẩm phổ biến")

        # Tiêu chí 3: Thời gian mua & Cấp thiết
        if re.search(r"(cuối tuần này|ngay trong tháng|cần ký hợp đồng dài hạn|muốn đi xem nhà mẫu)", text_lower):
            score_timeline = 20
            reasons.append("[+20] Thời gian quyết định nhanh / Cấp thiết")
        elif re.search(r"(đang cân nhắc|cần tư vấn thêm|so sánh)", text_lower):
            score_timeline = 12
            reasons.append("[+12] Đang tìm hiểu / Cần tư vấn thêm")

        # Tiêu chí 4: Chân dung & Pháp lý
        if re.search(r"(chủ doanh nghiệp|nhà đầu tư chuyên nghiệp|mua sỉ)", text_lower):
            score_persona = 15
            is_vip = True
            reasons.append("[+15] Chân dung VIP (Chủ DN / Mua sỉ)")
        elif re.search(r"(pháp lý chuẩn 100%|sổ hồng riêng)", text_lower):
            score_persona = 10
            reasons.append("[+10] Yêu cầu pháp lý minh bạch/Sổ riêng")

        # Tiêu chí 5: Tương tác & Đòn bẩy
        if re.search(r"(hỗ trợ vay ngân hàng|chính sách chiết khấu)", text_lower):
            score_engagement = 8
            reasons.append("[+8] Thiện chí tương tác / Cần chính sách vay")

    # Tổng điểm và phân hạng
    total_raw = score_budget + score_interest + score_timeline + score_persona + score_engagement
    final_score = max(0, min(100, total_raw))

    if is_junk or final_score < 40:
        category = "COLD"
        sla = "Hệ thống Nurturing / Drip Marketing (Không gọi ngay)"
        action = "Đưa vào Blacklist hoặc nuôi dưỡng bằng Zalo OA tự động."
    elif is_vip or final_score >= 75:
        category = "HOT"
        sla = "Bàn giao ngay — Gọi lại trong vòng 5 - 15 phút"
        action = "Top Sales liên hệ trực tiếp, chuẩn bị hồ sơ dự án cao cấp."
    else:
        category = "WARM"
        sla = "Bàn giao theo ca — Phản hồi trong 2 - 4 giờ"
        action = "Gửi thông tin dự án, tư vấn gói vay và đặt lịch xem nhà mẫu."

    return {
        "score": final_score,
        "category": category,
        "sla": sla,
        "action": action,
        "reasons": reasons
    }

def process_leads(input_csv_path, output_csv_path=None, output_json_path=None):
    leads = []
    with open(input_csv_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            desc = row.get("nhu_cau_mo_ta", "") or row.get("mo_ta", "") or row.get("content", "")
            lead_id = row.get("id", "")
            ten_khach = row.get("ten_khach", "")
            sdt = row.get("sdt", "")
            
            analysis = analyze_lead(desc)
            
            leads.append({
                "id": lead_id,
                "ten_khach": ten_khach,
                "sdt": sdt,
                "nhu_cau_mo_ta": desc,
                "diem_so": analysis["score"],
                "phan_loai": analysis["category"],
                "sla": analysis["sla"],
                "de_xuat_hanh_dong": analysis["action"],
                "ly_do_cham_diem": " | ".join(analysis["reasons"])
            })

    # Thống kê
    total_leads = len(leads)
    hot_leads = sum(1 for l in leads if l["phan_loai"] == "HOT")
    warm_leads = sum(1 for l in leads if l["phan_loai"] == "WARM")
    cold_leads = sum(1 for l in leads if l["phan_loai"] == "COLD")

    summary = {
        "tong_so_khach": total_leads,
        "hot_count": hot_leads,
        "hot_ratio": f"{(hot_leads/total_leads*100):.1f}%" if total_leads else "0%",
        "warm_count": warm_leads,
        "warm_ratio": f"{(warm_leads/total_leads*100):.1f}%" if total_leads else "0%",
        "cold_count": cold_leads,
        "cold_ratio": f"{(cold_leads/total_leads*100):.1f}%" if total_leads else "0%",
    }

    if output_csv_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_csv_path)), exist_ok=True)
        with open(output_csv_path, mode='w', encoding='utf-8-sig', newline='') as f:
            fieldnames = ["id", "ten_khach", "sdt", "diem_so", "phan_loai", "sla", "de_xuat_hanh_dong", "nhu_cau_mo_ta", "ly_do_cham_diem"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for l in leads:
                writer.writerow(l)

    if output_json_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_json_path)), exist_ok=True)
        with open(output_json_path, mode='w', encoding='utf-8') as f:
            json.dump({"summary": summary, "leads": leads}, f, ensure_ascii=False, indent=2)

    return summary, leads

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python score_leads.py <input_csv_file> [output_csv_file] [output_json_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    out_csv = sys.argv[2] if len(sys.argv) > 2 else "outputs/reports/scored_leads.csv"
    out_json = sys.argv[3] if len(sys.argv) > 3 else "outputs/reports/scored_leads.json"
    
    summary, _ = process_leads(input_file, out_csv, out_json)
    print("=== KẾT QUẢ CHẤM ĐIỂM LEAD SCORING BĐS ===")
    print(f"Tổng số khách: {summary['tong_so_khach']}")
    print(f"🔥 HOT: {summary['hot_count']} ({summary['hot_ratio']})")
    print(f"⛅ WARM: {summary['warm_count']} ({summary['warm_ratio']})")
    print(f"❄️ COLD: {summary['cold_count']} ({summary['cold_ratio']})")
    print(f"File CSV kết quả: {out_csv}")
