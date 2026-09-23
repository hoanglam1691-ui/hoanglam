"""
================================================================================
🏢 REAL ESTATE AI LEAD SCORING & SALES HANDOVER PLATFORM
Phiên bản: 2.0.0 (Premium Luxury UI/UX Edition)
Được phát triển cho khóa học: Agentic AI with Google Antigravity
Tích hợp: AI Lead Scoring Agent (5 Trụ Cột) + Human-in-the-loop st.data_editor
================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import re
import json
import os
import io

# -----------------------------------------------------------------------------
# 1. CẤU HÌNH TRANG STREAMLIT & METADATA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Lead Scoring — Luxury Real Estate Intelligence",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. BỘ STYLING CSS CAO CẤP (PREMIUM LUXURY DESIGN SYSTEM)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero Banner Section */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
        border: 1px solid rgba(255, 215, 0, 0.2);
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 24px;
        color: #FFFFFF;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }

    .hero-container::before {
        content: "";
        position: absolute;
        top: -50%;
        right: -20%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(217, 119, 6, 0.15) 0%, transparent 70%);
        pointer-events: none;
    }

    .brand-title {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FFFFFF 0%, #F59E0B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 6px 0;
        letter-spacing: -0.5px;
    }

    .brand-subtitle {
        font-size: 0.98rem;
        color: #94A3B8;
        max-width: 850px;
        margin: 0;
        line-height: 1.5;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #34D399;
        font-size: 0.78rem;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .status-pill-pulse {
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        box-shadow: 0 0 8px #10B981;
    }

    /* Premium Metric Card */
    .metric-card-premium {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
        transition: all 0.25s ease-in-out;
        position: relative;
        overflow: hidden;
    }

    .metric-card-premium:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.08);
        border-color: #CBD5E1;
    }

    .metric-card-premium.hot-accent {
        border-top: 4px solid #EF4444;
    }
    .metric-card-premium.warm-accent {
        border-top: 4px solid #F59E0B;
    }
    .metric-card-premium.cold-accent {
        border-top: 4px solid #64748B;
    }
    .metric-card-premium.success-accent {
        border-top: 4px solid #10B981;
    }
    .metric-card-premium.total-accent {
        border-top: 4px solid #3B82F6;
    }

    .metric-label {
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        color: #64748B;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }

    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.1;
        margin-bottom: 4px;
    }

    .metric-desc {
        font-size: 0.8rem;
        color: #94A3B8;
        font-weight: 500;
    }

    /* Badges */
    .badge-vip {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        color: #DC2626;
        border: 1px solid #FECACA;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 0.8rem;
    }

    .badge-warm-pill {
        background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
        color: #D97706;
        border: 1px solid #FDE68A;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 0.8rem;
    }

    .badge-cold-pill {
        background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
        color: #475569;
        border: 1px solid #E2E8F0;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.8rem;
    }

    /* Lead Inspector Card */
    .inspector-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
        margin-top: 10px;
    }

    .criteria-tag {
        display: inline-block;
        background: #F1F5F9;
        color: #334155;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 6px;
        margin: 3px 4px 3px 0;
        border: 1px solid #E2E8F0;
    }

    .criteria-tag.plus {
        background: #ECFDF5;
        color: #065F46;
        border-color: #A7F3D0;
    }

    .criteria-tag.minus {
        background: #FEF2F2;
        color: #991B1B;
        border-color: #FECACA;
    }

    .script-box {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        border: 1px solid #86EFAC;
        border-radius: 8px;
        padding: 14px 16px;
        color: #14532D;
        font-size: 0.92rem;
        line-height: 1.5;
        margin-top: 8px;
    }

    /* Streamlit overrides */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 18px;
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. CORE ENGINE: AI LEAD SCORING AGENT (5 TRỤ CỘT BĐS)
# -----------------------------------------------------------------------------
def ai_score_lead(text: str) -> dict:
    """
    Hệ thống AI Scoring Agent: Quét ngôn ngữ tự nhiên mô tả nhu cầu khách hàng theo 5 tiêu chí:
    1. Ngân sách (Budget - Max 35đ)
    2. Loại hình & Vị trí (Interest & Fit - Max 25đ)
    3. Thời gian & Cấp thiết (Timeline - Max 20đ)
    4. Nguồn khách & Chân dung (Persona - Max 15đ)
    5. Tương tác & Gói vay (Engagement - Max 10đ)
    Tích hợp bộ tiêu chí tieu_chi_cham_diem.txt (+50 VIP, -50 đến -80 Rác/Spam).
    """
    text_lower = text.lower() if isinstance(text, str) else ""
    
    score_budget = 10
    score_interest = 10
    score_timeline = 10
    score_persona = 5
    score_engagement = 5
    
    tags = []
    is_vip = False
    is_junk = False

    # A. TIÊU CHÍ TRỪ ĐIỂM / LỌC DỮ LIỆU RÁC (Cold / Junk Triggers)
    if re.search(r"(nhầm số|không có nhu cầu|dữ liệu cũ|nhầm ngành)", text_lower):
        score_persona = -50
        is_junk = True
        tags.append(("minus", "❌ Nhầm số / Dữ liệu rác (-50đ)"))
        
    if re.search(r"(thuê bao|không bắt máy|không phản hồi zalo|gọi nhiều lần)", text_lower):
        score_engagement = -40
        is_junk = True
        tags.append(("minus", "📵 Thông tin liên lạc lỗi / Thuê bao (-40đ)"))
        
    if re.search(r"(hỏi giá cho vui|chưa có ý định mua|thái độ không hợp tác)", text_lower):
        score_timeline = -40
        is_junk = True
        tags.append(("minus", "⚠️ Không thiện chí / Hỏi cho vui (-40đ)"))
        
    if re.search(r"(quận 1 giá 1|q1 giá 1|giá 1-2 tỷ|vài trăm triệu|thuê nguyên căn giá 2 triệu)", text_lower):
        score_budget = -50
        is_junk = True
        tags.append(("minus", "🛑 Yêu cầu phi thực tế / Ảo tưởng giá (-50đ)"))

    if re.search(r"(bảo hiểm|vay vốn|mời chào dịch vụ|quảng cáo)", text_lower):
        score_persona = -80
        is_junk = True
        tags.append(("minus", "🚫 Spam / Quảng cáo dịch vụ (-80đ)"))

    # B. TIÊU CHÍ CỘNG ĐIỂM TIỀM NĂNG & VIP
    if not is_junk:
        # Tiêu chí 1: Ngân sách
        if re.search(r"(20\s*tỷ|30\s*tỷ|50\s*tỷ|100\s*tỷ|tài chính cực mạnh|tài chính mạnh|không thành vấn đề)", text_lower):
            score_budget = 35
            is_vip = True
            tags.append(("plus", "💎 Ngân sách VIP >= 20 tỷ (+35đ)"))
        elif re.search(r"(8-10\s*tỷ|5-7\s*tỷ|4-5\s*tỷ|3-10\s*tỷ)", text_lower):
            score_budget = 25
            tags.append(("plus", "💰 Ngân sách 4-10 tỷ (+25đ)"))
        elif re.search(r"(2-3\s*tỷ|dưới 50 triệu)", text_lower):
            score_budget = 15
            tags.append(("plus", "💵 Phổ thông 2-3 tỷ / Thuê 50tr (+15đ)"))

        # Tiêu chí 2: Loại hình & Vị trí
        if re.search(r"(penthouse|biệt thự đơn lập|quỹ đất công nghiệp|sàn văn phòng diện tích lớn|trên 2000m2)", text_lower):
            score_interest = 25
            is_vip = True
            tags.append(("plus", "🏰 Penthouse / Biệt thự / Sàn >2000m2 (+25đ)"))
        elif re.search(r"(quận 1|ven sông|vinhomes ocean park|phú mỹ hưng)", text_lower):
            score_interest = 20
            tags.append(("plus", "📍 Vị trí đắc địa (Q1, Ven sông, Vinhomes) (+20đ)"))
        elif re.search(r"(căn hộ 2pn|nhà phố liền kề|đất nền vùng ven|thuê mặt bằng)", text_lower):
            score_interest = 15
            tags.append(("plus", "🏠 Căn hộ 2PN / Nhà phố / Mặt bằng (+15đ)"))

        # Tiêu chí 3: Thời gian & Cấp thiết
        if re.search(r"(cuối tuần này|ngay trong tháng|cần ký hợp đồng dài hạn|muốn đi xem nhà mẫu)", text_lower):
            score_timeline = 20
            tags.append(("plus", "⚡ Cấp thiết / Xem nhà cuối tuần (+20đ)"))
        elif re.search(r"(đang cân nhắc|cần tư vấn thêm|so sánh)", text_lower):
            score_timeline = 12
            tags.append(("plus", "🔍 Cân nhắc / Cần tư vấn thêm (+12đ)"))

        # Tiêu chí 4: Chân dung & Pháp lý
        if re.search(r"(chủ doanh nghiệp|nhà đầu tư chuyên nghiệp|mua sỉ)", text_lower):
            score_persona = 15
            is_vip = True
            tags.append(("plus", "👑 Chân dung VIP (Chủ DN / Mua sỉ) (+15đ)"))
        elif re.search(r"(pháp lý chuẩn 100%|sổ hồng riêng)", text_lower):
            score_persona = 10
            tags.append(("plus", "📜 Yêu cầu Sổ hồng riêng / Pháp lý 100% (+10đ)"))

        # Tiêu chí 5: Tương tác & Đòn bẩy
        if re.search(r"(hỗ trợ vay ngân hàng|chính sách chiết khấu)", text_lower):
            score_engagement = 8
            tags.append(("plus", "🤝 Nhu cầu Gói vay / Chiết khấu (+8đ)"))

    # Tổng điểm và phân hạng
    total_raw = score_budget + score_interest + score_timeline + score_persona + score_engagement
    final_score = max(0, min(100, total_raw))

    if is_junk or final_score < 40:
        category = "❄️ COLD"
        sla = "Tự động hóa Nurturing / Blacklist"
        action = "Đưa vào luồng Zalo OA / Email Drip hoặc Blacklist"
        script_hint = "Gửi tin nhắn tự động thăm dò thị trường hoặc loại bỏ khỏi danh sách gọi."
    elif is_vip or final_score >= 75:
        category = "🔥 HOT"
        sla = "< 15 Phút (Ưu tiên gọi ngay)"
        action = "Top Sales liên hệ trực tiếp, chuẩn bị layout & hồ sơ pháp lý 100%"
        script_hint = "Dạ em chào anh/chị, em gửi layout độc quyền và bộ hồ sơ pháp lý 100% qua Zalo để mình xem trước và xếp lịch xem thực tế ạ!"
    else:
        category = "⛅ WARM"
        sla = "< 2 - 4 Giờ"
        action = "Tư vấn gói vay ngân hàng, gửi bảng tính dòng tiền và hẹn xem nhà mẫu"
        script_hint = "Dạ em chào anh/chị, bên em có chính sách hỗ trợ lãi suất 0% cho căn hộ 2PN rất phù hợp với kế hoạch dòng tiền của gia đình mình ạ!"

    return {
        "diem_ai": final_score,
        "phan_loai_ai": category,
        "sla": sla,
        "hanh_dong": action,
        "tags": tags,
        "kich_ban": script_hint
    }


# -----------------------------------------------------------------------------
# 4. DATA LOADER & CACHING
# -----------------------------------------------------------------------------
@st.cache_data
def load_initial_dataset():
    local_path = "sample-data/khach_hang_bds_sample.csv"
    if os.path.exists(local_path):
        return pd.read_csv(local_path)
    
    # Fallback to Google Sheets URL
    sheet_url = "https://docs.google.com/spreadsheets/d/17odkUsLWSnrnOebV0LzPCP5ZWz3mm-yR09ZFjslwh1w/gviz/tq?tqx=out:csv&gid=1542775777"
    try:
        return pd.read_csv(sheet_url)
    except Exception:
        return pd.DataFrame([
            {"id": 1, "ten_khach": "Phan Văn Hoa", "sdt": "0894782782", "nhu_cau_mo_ta": "Đang tìm thuê mặt bằng kinh doanh spa tại Quận 1, diện tích khoảng 80-100m2. Giá dưới 50 triệu/tháng."},
            {"id": 2, "ten_khach": "Hồ Hồng Linh", "sdt": "0848475144", "nhu_cau_mo_ta": "Khách hàng nhầm số, không có nhu cầu về bất động sản."},
            {"id": 3, "ten_khach": "Lý Đức Cường", "sdt": "0953430096", "nhu_cau_mo_ta": "Quan tâm căn hộ 2PN tại Quận 7, tài chính 4-5 tỷ, cần vay 70%, xem cuối tuần."},
            {"id": 4, "ten_khach": "Lê Anh Lan", "sdt": "0964591036", "nhu_cau_mo_ta": "Tìm mua Penthouse diện tích lớn có hồ bơi riêng. Ngân sách không thành vấn đề."}
        ])


# -----------------------------------------------------------------------------
# 5. INITIALIZE SESSION STATE
# -----------------------------------------------------------------------------
if "leads_df" not in st.session_state:
    raw_df = load_initial_dataset()
    scored_records = []
    for _, row in raw_df.iterrows():
        desc = str(row.get("nhu_cau_mo_ta", "") or "")
        analysis = ai_score_lead(desc)
        
        default_status = "Chờ duyệt"
        default_assigned = "Chưa gán"
        if "HOT" in analysis["phan_loai_ai"]:
            default_assigned = "Top Sales VIP 1"
        
        scored_records.append({
            "id": int(row.get("id", 0)) if str(row.get("id", "")).isdigit() else row.get("id", 0),
            "ten_khach": row.get("ten_khach", ""),
            "sdt": str(row.get("sdt", "")),
            "nhu_cau_mo_ta": desc,
            "diem_ai": analysis["diem_ai"],
            "phan_loai_ai": analysis["phan_loai_ai"],
            "duyet_trang_thai": default_status,
            "phan_loai_chot": analysis["phan_loai_ai"],
            "sales_phu_trach": default_assigned,
            "ghi_chu_tham_dinh": "",
            "da_duyet": False,
            "sla": analysis["sla"],
            "tags": analysis["tags"],
            "kich_ban": analysis["kich_ban"]
        })
    st.session_state.leads_df = pd.DataFrame(scored_records)


# -----------------------------------------------------------------------------
# 6. SIDEBAR NAVIGATION & BATCH CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 12px 0 16px 0;">
        <div style="font-size: 2.2rem; margin-bottom: 4px;">👑</div>
        <div style="font-weight: 800; font-size: 1.15rem; color: #0F172A; letter-spacing: -0.3px;">LUXURY REAL ESTATE</div>
        <div style="font-size: 0.78rem; color: #64748B; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px;">AI Lead Intelligence Hub</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 📥 **Nạp Dữ Liệu Khách Hàng**")
    uploaded_file = st.file_uploader("Tải file Lead (.csv, .xlsx)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                new_df = pd.read_csv(uploaded_file)
            else:
                new_df = pd.read_excel(uploaded_file)
            
            if st.button("🚀 Quét AI & Nạp Danh Sách Mới", use_container_width=True, type="primary"):
                new_records = []
                for idx, row in new_df.iterrows():
                    desc = str(row.get("nhu_cau_mo_ta", "") or row.get("mo_ta", ""))
                    analysis = ai_score_lead(desc)
                    new_records.append({
                        "id": row.get("id", idx + 1),
                        "ten_khach": row.get("ten_khach", f"Khách #{idx+1}"),
                        "sdt": str(row.get("sdt", "")),
                        "nhu_cau_mo_ta": desc,
                        "diem_ai": analysis["diem_ai"],
                        "phan_loai_ai": analysis["phan_loai_ai"],
                        "duyet_trang_thai": "Chờ duyệt",
                        "phan_loai_chot": analysis["phan_loai_ai"],
                        "sales_phu_trach": "Top Sales VIP 1" if "HOT" in analysis["phan_loai_ai"] else "Chưa gán",
                        "ghi_chu_tham_dinh": "",
                        "da_duyet": False,
                        "sla": analysis["sla"],
                        "tags": analysis["tags"],
                        "kich_ban": analysis["kich_ban"]
                    })
                st.session_state.leads_df = pd.DataFrame(new_records)
                st.success("✅ Đã nạp và chấm điểm toàn bộ danh sách mới!")
                st.rerun()
        except Exception as e:
            st.error(f"Lỗi khi đọc file: {e}")

    st.markdown("---")
    st.markdown("#### 🔍 **Bộ Lọc Đa Chiều**")
    
    filter_category = st.multiselect(
        "Phân loại Lead:",
        options=["🔥 HOT", "⛅ WARM", "❄️ COLD"],
        default=["🔥 HOT", "⛅ WARM", "❄️ COLD"]
    )
    
    filter_status = st.multiselect(
        "Trạng thái thẩm định:",
        options=["Chờ duyệt", "✅ Đã duyệt bàn giao", "⚠️ Cần kiểm tra lại", "⛔ Từ chối / Blacklist"],
        default=["Chờ duyệt", "✅ Đã duyệt bàn giao", "⚠️ Cần kiểm tra lại", "⛔ Từ chối / Blacklist"]
    )
    
    search_keyword = st.text_input("🔎 Tìm kiếm tên / SĐT / Nhu cầu:", placeholder="VD: Penthouse, 098..., Căn hộ")

    st.markdown("---")
    st.markdown("#### ⚡ **Thao Tác Nhanh (Batch Actions)**")
    
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("✅ Duyệt Hết HOT", use_container_width=True):
            mask = st.session_state.leads_df["phan_loai_chot"] == "🔥 HOT"
            st.session_state.leads_df.loc[mask, "duyet_trang_thai"] = "✅ Đã duyệt bàn giao"
            st.session_state.leads_df.loc[mask, "da_duyet"] = True
            st.success("Đã duyệt tất cả HOT Lead!")
            st.rerun()
    with col_b2:
        if st.button("⛔ Chặn Hết Rác", use_container_width=True):
            mask = st.session_state.leads_df["phan_loai_chot"] == "❄️ COLD"
            st.session_state.leads_df.loc[mask, "duyet_trang_thai"] = "⛔ Từ chối / Blacklist"
            st.rerun()

    if st.button("🔄 Khôi Phục Dữ Liệu Gốc", use_container_width=True):
        st.session_state.pop("leads_df", None)
        st.rerun()


# -----------------------------------------------------------------------------
# 7. HERO BANNER & BRAND IDENTITY SECTION
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
        <div>
            <div style="margin-bottom: 8px;">
                <span class="status-pill">
                    <span class="status-pill-pulse"></span>
                    AI AGENT ENGINE ACTIVE • SLA PROTOCOL VERIFIED
                </span>
            </div>
            <h1 class="brand-title">👑 Hệ Thống Chấm Điểm Khách Hàng Tiềm Năng BĐS</h1>
            <p class="brand-subtitle">
                Nền tảng trí tuệ nhân tạo chuyên sâu Bất Động Sản: Tự động phân tích 5 trụ cột nhu cầu, 
                sàng lọc dữ liệu rác, tính điểm VIP và hỗ trợ <b>Human-in-the-loop</b> phê duyệt bàn giao chuẩn SLA.
            </p>
        </div>
        <div style="text-align: right; background: rgba(255, 255, 255, 0.07); padding: 12px 18px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="font-size: 0.75rem; color: #CBD5E1; text-transform: uppercase; font-weight: 600;">Chuẩn Chấm Điểm</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #F59E0B;">5 Trụ Cột BANT + Fit</div>
            <div style="font-size: 0.75rem; color: #94A3B8;">Tích hợp tieu_chi_cham_diem.txt</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 8. VISUAL KPI DASHBOARD METRICS CARDS
# -----------------------------------------------------------------------------
df = st.session_state.leads_df

total_leads = len(df)
hot_count = len(df[df["phan_loai_chot"] == "🔥 HOT"])
warm_count = len(df[df["phan_loai_chot"] == "⛅ WARM"])
cold_count = len(df[df["phan_loai_chot"] == "❄️ COLD"])
approved_count = len(df[df["duyet_trang_thai"] == "✅ Đã duyệt bàn giao"])

hot_pct = (hot_count / total_leads * 100) if total_leads else 0
warm_pct = (warm_count / total_leads * 100) if total_leads else 0
cold_pct = (cold_count / total_leads * 100) if total_leads else 0
approved_pct = (approved_count / total_leads * 100) if total_leads else 0

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="metric-card-premium total-accent">
        <div class="metric-label">📋 Tổng Quy Mô Lead</div>
        <div class="metric-value">{total_leads}</div>
        <div class="metric-desc">Toàn bộ database xử lý</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card-premium hot-accent">
        <div class="metric-label">🔥 Lead VIP / HOT</div>
        <div class="metric-value" style="color: #DC2626;">{hot_count} <span style="font-size: 1rem; font-weight: 600;">({hot_pct:.1f}%)</span></div>
        <div class="metric-desc">SLA &lt; 15 phút • Gọi trực tiếp</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card-premium warm-accent">
        <div class="metric-label">⛅ Lead WARM (Tiềm năng)</div>
        <div class="metric-value" style="color: #D97706;">{warm_count} <span style="font-size: 1rem; font-weight: 600;">({warm_pct:.1f}%)</span></div>
        <div class="metric-desc">SLA &lt; 4 giờ • Tư vấn gói vay</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card-premium cold-accent">
        <div class="metric-label">❄️ Lead COLD / Rác</div>
        <div class="metric-value" style="color: #475569;">{cold_count} <span style="font-size: 1rem; font-weight: 600;">({cold_pct:.1f}%)</span></div>
        <div class="metric-desc">Lọc bỏ / Nuôi dưỡng tự động</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="metric-card-premium success-accent">
        <div class="metric-label">✅ Đã Duyệt Bàn Giao</div>
        <div class="metric-value" style="color: #059669;">{approved_count} <span style="font-size: 1rem; font-weight: 600;">({approved_pct:.1f}%)</span></div>
        <div class="metric-desc">Đã chuyển giao cho Sales</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 9. MAIN TAB INTERFACE
# -----------------------------------------------------------------------------
tab_table, tab_charts, tab_docs = st.tabs([
    "📋 Bảng Phê Duyệt & Thẩm Định Lead", 
    "📊 Phân Tích Thống Kê & Trực Quan Hóa", 
    "📖 Quy Chuẩn 5 Tiêu Chí & Hướng Dẫn Vận Hành"
])


# =============================================================================
# TAB 1: BẢNG PHÊ DUYỆT HUMAN-IN-THE-LOOP (st.data_editor)
# =============================================================================
with tab_table:
    # Áp dụng bộ lọc
    filtered_df = df[
        (df["phan_loai_chot"].isin(filter_category)) &
        (df["duyet_trang_thai"].isin(filter_status))
    ]

    if search_keyword:
        kw = search_keyword.lower()
        filtered_df = filtered_df[
            filtered_df["ten_khach"].str.lower().str.contains(kw, na=False) |
            filtered_df["sdt"].str.contains(kw, na=False) |
            filtered_df["nhu_cau_mo_ta"].str.lower().str.contains(kw, na=False)
        ]

    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
        <h3 style="margin: 0; font-size: 1.25rem; font-weight: 700; color: #1E293B;">
            📝 Danh Sách Khách Hàng Chờ Phê Duyệt ({len(filtered_df)} / {total_leads} khách)
        </h3>
        <span style="font-size: 0.85rem; color: #64748B;">💡 <i>Nhấp đúp vào ô để chỉnh sửa trực tiếp thông tin thẩm định</i></span>
    </div>
    """, unsafe_allow_html=True)

    column_config = {
        "id": st.column_config.NumberColumn("ID", width="small", disabled=True),
        "ten_khach": st.column_config.TextColumn("Họ & Tên Khách", width="medium"),
        "sdt": st.column_config.TextColumn("Số Điện Thoại", width="small"),
        "nhu_cau_mo_ta": st.column_config.TextColumn("Nhu Cầu Chi Tiết (Mô tả)", width="large", disabled=True),
        "diem_ai": st.column_config.ProgressColumn(
            "Điểm AI",
            help="Điểm số đánh giá từ 0 đến 100 theo 5 trụ cột BĐS",
            min_value=0,
            max_value=100,
            format="%d",
            width="small"
        ),
        "phan_loai_ai": st.column_config.TextColumn("Gợi Ý AI", width="small", disabled=True),
        "duyet_trang_thai": st.column_config.SelectboxColumn(
            "Duyệt Trạng Thái",
            help="Trạng thái bàn giao chính thức cho Sales",
            options=["Chờ duyệt", "✅ Đã duyệt bàn giao", "⚠️ Cần kiểm tra lại", "⛔ Từ chối / Blacklist"],
            required=True,
            width="medium"
        ),
        "phan_loai_chot": st.column_config.SelectboxColumn(
            "Phân Loại Chốt",
            options=["🔥 HOT", "⛅ WARM", "❄️ COLD", "🗑️ RÁC/SPAM"],
            required=True,
            width="small"
        ),
        "sales_phu_trach": st.column_config.SelectboxColumn(
            "Sales Phụ Trách",
            options=["Chưa gán", "Top Sales VIP 1", "Top Sales VIP 2", "Sales Dự Án A", "Sales Dự Án B", "CSKH Automation"],
            width="medium"
        ),
        "ghi_chu_tham_dinh": st.column_config.TextColumn("Ghi Chú Thẩm Định", width="medium"),
        "da_duyet": st.column_config.CheckboxColumn("Đã Duyệt", width="small"),
        "sla": None,
        "tags": None,
        "kich_ban": None
    }

    # Hiển thị st.data_editor
    edited_df = st.data_editor(
        filtered_df,
        column_config=column_config,
        use_container_width=True,
        num_rows="dynamic",
        height=420,
        key="lead_data_editor"
    )

    # Đồng bộ 2 chiều ngược về st.session_state
    if not edited_df.equals(filtered_df):
        for idx, row in edited_df.iterrows():
            lead_id = row["id"]
            mask = st.session_state.leads_df["id"] == lead_id
            if mask.any():
                st.session_state.leads_df.loc[mask, "duyet_trang_thai"] = row["duyet_trang_thai"]
                st.session_state.leads_df.loc[mask, "phan_loai_chot"] = row["phan_loai_chot"]
                st.session_state.leads_df.loc[mask, "sales_phu_trach"] = row["sales_phu_trach"]
                st.session_state.leads_df.loc[mask, "ghi_chu_tham_dinh"] = row["ghi_chu_tham_dinh"]
                st.session_state.leads_df.loc[mask, "da_duyet"] = (row["duyet_trang_thai"] == "✅ Đã duyệt bàn giao")

    st.markdown("---")

    # THẺ INSPECTOR LEAD & TRỢ LÝ TELESALE
    st.markdown("### 🎯 **Thẩm Định Chuyên Sâu & Thẻ Bàn Giao (Lead Card Inspector)**")

    selected_ids = df["id"].tolist()
    col_sel, col_card = st.columns([1, 2])

    with col_sel:
        selected_id = st.selectbox(
            "Chọn khách hàng để xem phân tích AI chi tiết:",
            options=selected_ids,
            format_func=lambda x: f"ID #{x} — {df[df['id']==x]['ten_khach'].values[0]} ({df[df['id']==x]['phan_loai_chot'].values[0]})"
        )

    selected_row = df[df["id"] == selected_id].iloc[0]

    with col_card:
        badge_style = "badge-vip" if "HOT" in selected_row["phan_loai_chot"] else ("badge-warm-pill" if "WARM" in selected_row["phan_loai_chot"] else "badge-cold-pill")
        
        # Render các tags lý do chấm điểm
        tags_html = ""
        for tag_type, tag_text in selected_row["tags"]:
            tag_class = "plus" if tag_type == "plus" else "minus"
            tags_html += f'<span class="criteria-tag {tag_class}">{tag_text}</span> '
        if not tags_html:
            tags_html = '<span class="criteria-tag">Nhu cầu cơ bản</span>'

        st.markdown(f"""
        <div class="inspector-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <div>
                    <h3 style="margin: 0; color: #0F172A; font-weight: 800;">
                        👤 {selected_row['ten_khach']} 
                        <span style="font-size: 0.9rem; color: #64748B; font-weight: 500;">(ID: #{selected_row['id']})</span>
                    </h3>
                    <div style="color: #475569; font-size: 0.88rem; margin-top: 2px;">
                        📞 <b>{selected_row['sdt']}</b> &nbsp;•&nbsp; 
                        ⏱️ Cam kết SLA: <b style="color: #DC2626;">{selected_row['sla']}</b>
                    </div>
                </div>
                <div style="text-align: right;">
                    <span class="{badge_style}">{selected_row['phan_loai_chot']}</span>
                    <div style="font-size: 1.3rem; font-weight: 800; color: #0F172A; margin-top: 4px;">{selected_row['diem_ai']}<span style="font-size: 0.8rem; color: #64748B;">/100đ</span></div>
                </div>
            </div>
            
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 14px; margin-bottom: 14px;">
                <div style="font-size: 0.78rem; font-weight: 700; color: #64748B; text-transform: uppercase;">Mô Tả Nhu Cầu Gốc</div>
                <div style="color: #1E293B; font-size: 0.92rem; font-style: italic; margin-top: 4px;">"{selected_row['nhu_cau_mo_ta']}"</div>
            </div>

            <div style="margin-bottom: 14px;">
                <div style="font-size: 0.78rem; font-weight: 700; color: #64748B; text-transform: uppercase; margin-bottom: 6px;">Căn Cứ AI Chấm Điểm (AI Insights)</div>
                <div>{tags_html}</div>
            </div>

            <div style="margin-bottom: 14px;">
                <div style="font-size: 0.78rem; font-weight: 700; color: #15803D; text-transform: uppercase;">Gợi Ý Kịch Bản Mở Đầu Cho Telesale</div>
                <div class="script-box">"{selected_row['kich_ban']}"</div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px solid #E2E8F0; font-size: 0.88rem;">
                <div>👨‍💼 Sales phụ trách: <b>{selected_row['sales_phu_trach']}</b></div>
                <div>Trạng thái: <b>{selected_row['duyet_trang_thai']}</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # KHU VỰC XUẤT DỮ LIỆU & BÀN GIAO CRM
    st.markdown("---")
    st.markdown("### 📤 **Kết Xuất Bàn Giao & Tích Hợp CRM / Zalo**")
    
    exp_c1, exp_c2, exp_c3 = st.columns([1, 1, 2])
    
    with exp_c1:
        csv_all = io.StringIO()
        df.to_csv(csv_all, index=False, encoding="utf-8-sig")
        st.download_button(
            label="📥 Tải Toàn Bộ Lead (.CSV)",
            data=csv_all.getvalue(),
            file_name="real_estate_leads_all.csv",
            mime="text/csv",
            use_container_width=True
        )

    with exp_c2:
        approved_df = df[df["duyet_trang_thai"] == "✅ Đã duyệt bàn giao"]
        csv_appr = io.StringIO()
        approved_df.to_csv(csv_appr, index=False, encoding="utf-8-sig")
        st.download_button(
            label=f"⭐ Tải Lead Đã Duyệt ({len(approved_df)})",
            data=csv_appr.getvalue(),
            file_name="real_estate_leads_approved.csv",
            mime="text/csv",
            disabled=(len(approved_df) == 0),
            use_container_width=True,
            type="primary"
        )

    with exp_c3:
        zalo_payload = f"""🚨 [HOT LEAD ALERT - BẤT ĐỘNG SẢN] 🚨
👤 Khách hàng: {selected_row['ten_khach']} | SĐT: {selected_row['sdt']}
⭐ Điểm AI: {selected_row['diem_ai']}/100 ({selected_row['phan_loai_chot']})
⏱️ SLA Phản hồi: {selected_row['sla']}
📋 Nhu cầu: {selected_row['nhu_cau_mo_ta']}
🎯 Kịch bản mở đầu: "{selected_row['kich_ban']}"
👉 Phân bổ Sales: {selected_row['sales_phu_trach']}"""
        
        with st.expander("💬 Xem mẫu tin nhắn Webhook Zalo / Telegram Bàn Giao"):
            st.code(zalo_payload, language="text")


# =============================================================================
# TAB 2: PHÂN TÍCH THỐNG KÊ & BIỂU ĐỒ TRỰC QUAN
# =============================================================================
with tab_charts:
    st.markdown("### 📊 **Phân Tích Đa Chiều Cơ Cấu Lead & Hiệu Quả Pipeline**")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("#### 🏢 **Cơ Cấu Phân Hạng Khách Hàng (Tỷ Lệ %)**")
        category_counts = df["phan_loai_chot"].value_counts()
        chart_data = pd.DataFrame({
            "Phân Loại": category_counts.index,
            "Số Lượng Lead": category_counts.values
        }).set_index("Phân Loại")
        st.bar_chart(chart_data, color="#3B82F6")
        st.caption("Biểu đồ thể hiện tỷ trọng khách hàng theo 3 nhóm HOT (VIP), WARM (Tiềm năng) và COLD (Rác/Lỗi).")

    with chart_col2:
        st.markdown("#### 📈 **Phân Phối Điểm Số Tiềm Năng (AI Score Distribution)**")
        # Phân nhóm dải điểm
        bins = [0, 20, 40, 60, 80, 100]
        labels = ["0 - 20 (Rác nặng)", "21 - 40 (Kém)", "41 - 60 (Trung bình)", "61 - 80 (Khá/Tốt)", "81 - 100 (VIP Siêu Tiềm Năng)"]
        df["score_range"] = pd.cut(df["diem_ai"], bins=bins, labels=labels, include_lowest=True)
        score_counts = df["score_range"].value_counts().sort_index()
        score_data = pd.DataFrame({
            "Dải Điểm": score_counts.index,
            "Số Khách": score_counts.values
        }).set_index("Dải Điểm")
        st.area_chart(score_data, color="#10B981")
        st.caption("Phân bố số lượng khách hàng tập trung theo các dải điểm chuẩn hóa 0 - 100.")

    st.markdown("---")
    
    # Bảng Ma trận SLA & Khuyến nghị hành động
    st.markdown("#### ⚡ **Ma Trận Phân Bổ Nguồn Lực & SLA Phản Hồi**")
    sla_summary_data = [
        {"Nhóm Lead": "🔥 HOT (VIP)", "Quy Mô": f"{hot_count} khách ({hot_pct:.1f}%)", "SLA Mục Tiêu": "< 15 Phút", "Phân Bổ Nhân Sự": "Top Sales VIP / Trưởng nhóm", "Hành Động Trọng Tâm": "Gọi điện ngay, gửi layout độc quyền, chốt xem thực tế trong 48h"},
        {"Nhóm Lead": "⛅ WARM (Nhu cầu thực)", "Quy Mô": f"{warm_count} khách ({warm_pct:.1f}%)", "SLA Mục Tiêu": "< 2 - 4 Giờ", "Phân Bổ Nhân Sự": "Chuyên viên tư vấn dự án", "Hành Động Trọng Tâm": "Gửi bảng tính dòng tiền, tư vấn gói vay 0%, hẹn lịch xem nhà mẫu"},
        {"Nhóm Lead": "❄️ COLD (Rác/Chưa nhu cầu)", "Quy Mô": f"{cold_count} khách ({cold_pct:.1f}%)", "SLA Mục Tiêu": "Tự động hóa", "Phân Bổ Nhân Sự": "Hệ thống Zalo OA / CRM", "Hành Động Trọng Tâm": "Chuyển vào luồng Email/Zalo Drip Marketing; Đưa vào Blacklist nếu là Spam/Nhầm số"}
    ]
    st.table(pd.DataFrame(sla_summary_data))


# =============================================================================
# TAB 3: QUY CHUẨN 5 TIÊU CHÍ (KNOWLEDGE BASE)
# =============================================================================
with tab_docs:
    st.markdown(r"""
    ### 📖 **Bộ Tiêu Chuẩn Chấm Điểm Lead Bất Động Sản (BANT + Fit Model)**
    *(Căn cứ theo tài liệu chuẩn nghiệp vụ `knowledge-base/tieu_chi_cham_diem.txt` & Skill `Chamdiem_scoring`)*
    
    ---
    
    #### 1. Khung 5 Trụ Cột Đánh Giá:
    - **1. Ngân Sách (Budget - 35%):** Khả năng tài chính và dòng tiền. VIP khi $\ge 20$ tỷ hoặc *"tài chính không thành vấn đề"*. Phạt $-50$ điểm khi ảo tưởng giá (nhà Q1 giá 1-2 tỷ).
    - **2. Mức Độ Phù Hợp & Loại Hình (Interest & Fit - 25%):** BĐS cao cấp (Penthouse, Biệt thự, Shophouse, Sàn $>2000\text{m}^2$) $\rightarrow +25$đ; Vị trí đắc địa (Q1, Ven sông, Vinhomes, Phú Mỹ Hưng) $\rightarrow +20$đ.
    - **3. Thời Gian Quyết Định (Timeline - 20%):** Tính cấp thiết (Xem nhà cuối tuần, ký hợp đồng ngay trong tháng) $\rightarrow +20$đ; Hỏi cho vui / chưa có ý định $\rightarrow -40$đ.
    - **4. Chân Dung & Nguồn Khách (Persona - 15%):** Chủ doanh nghiệp, Mua sỉ, Nhà đầu tư chuyên nghiệp $\rightarrow +15$đ; Spam / Rao vặt dịch vụ khác $\rightarrow -80$đ; Nhầm số / Dữ liệu rác $\rightarrow -50$đ.
    - **5. Tương Tác & Thiện Chí (Engagement - 10%):** Cần tư vấn gói vay $\rightarrow +8$đ; Thuê bao / Không bắt máy / Không phản hồi Zalo $\rightarrow -40$đ.

    ---

    #### 2. Nguyên Tắc An Toàn Khi AI Vận Hành:
    1. **Không Hallucination:** Luôn phân biệt giữa khách thuê mặt bằng kinh doanh (dưới 50 triệu/tháng) với khách mua BĐS giá trị lớn.
    2. **Xử lý tiếng lóng BĐS:** Tự động nhận diện chuẩn xác các từ viết tắt: *2PN, CĐT, SHR (sổ hồng riêng), Q1, Q7, HĐMB*.
    3. **Bảo mật PII:** Toàn bộ số điện thoại và thông tin định danh chỉ lưu hành nội bộ, không đưa ra môi trường công cộng.
    4. **Human-in-the-loop:** Điều phối viên kiểm soát toàn quyền trạng thái phê duyệt trước khi chuyển dữ liệu cho Sales.
    """)

st.markdown("<div style='margin-top: 36px;'></div>", unsafe_allow_html=True)
st.caption("🏛️ **Hệ Thống Phân Tích & Chấm Điểm Khách Hàng Tiềm Năng Bất Động Sản** | Khóa học: **Agentic AI with Google Antigravity** | Bản quyền: **AI4A & Real Estate Tech Team**")
