import streamlit as st
import pandas as pd
import numpy as np
import re
import os
import json

# ==========================================
# 1. CẤU HÌNH TRANG & GIAO DIỆN HIỆN ĐẠI (AESTHETICS)
# ==========================================
st.set_page_config(
    page_title="AI Lead Scoring BĐS — Human-in-the-Loop",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS cho phong cách hiện đại, trực quan
st.markdown("""
<style>
    /* Gradient Header */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f766e 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    .main-header h1 {
        color: #f8fafc;
        font-size: 26px;
        font-weight: 700;
        margin: 0 0 8px 0;
    }
    .main-header p {
        color: #cbd5e1;
        font-size: 14px;
        margin: 0;
    }
    
    /* Metric Cards */
    .metric-card {
        background: #ffffff;
        border-radius: 10px;
        padding: 16px 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        text-align: center;
    }
    .metric-card.hot { border-top: 4px solid #ef4444; }
    .metric-card.warm { border-top: 4px solid #f59e0b; }
    .metric-card.cold { border-top: 4px solid #64748b; }
    .metric-card.approved { border-top: 4px solid #10b981; }
    
    .metric-title {
        font-size: 13px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
    }
    .metric-value {
        font-size: 26px;
        font-weight: 700;
        margin: 4px 0;
    }
    .metric-sub {
        font-size: 12px;
        color: #94a3b8;
    }

    /* Handover Preview Card */
    .handover-card {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-left: 5px solid #0ea5e9;
        border-radius: 8px;
        padding: 16px;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 13px;
        line-height: 1.5;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIC AI LEAD SCORING ENGINE (5 TRỤ CỘT)
# ==========================================
def ai_score_lead(text):
    """
    Hàm phân tích tự động nội dung mô tả khách hàng BĐS dựa trên 5 trụ cột:
    1. Ngân sách (Budget)
    2. Loại hình & Vị trí (Interest & Fit)
    3. Thời gian & Cấp thiết (Timeline)
    4. Chân dung & Nguồn (Persona & Source)
    5. Tương tác & Thiện chí (Engagement)
    Tích hợp bộ tiêu chí tieu_chi_cham_diem.txt (+50 VIP, -50 Rác/Spam).
    """
    text_lower = text.lower() if isinstance(text, str) else ""
    
    score_budget = 10     # Tiêu chí 1: Ngân sách (0 - 35)
    score_interest = 10   # Tiêu chí 2: Loại hình & Vị trí (0 - 25)
    score_timeline = 10   # Tiêu chí 3: Thời gian & Cấp thiết (0 - 20)
    score_persona = 5     # Tiêu chí 4: Chân dung & Nguồn (0 - 15)
    score_engagement = 5  # Tiêu chí 5: Tương tác & Thiện chí (0 - 10)
    
    reasons = []
    is_vip = False
    is_junk = False

    # 1. BỘ LỌC TRỪ ĐIỂM RÁC / SPAM / DỮ LIỆU LỖI
    if re.search(r"(nhầm số|không có nhu cầu|dữ liệu cũ|nhầm ngành)", text_lower):
        score_persona = -50
        is_junk = True
        reasons.append("[-50] Dữ liệu rác / Nhầm số")
        
    if re.search(r"(thuê bao|không bắt máy|không phản hồi zalo|gọi nhiều lần)", text_lower):
        score_engagement = -40
        is_junk = True
        reasons.append("[-40] Không liên lạc được / Thuê bao")
        
    if re.search(r"(hỏi giá cho vui|chưa có ý định mua|thái độ không hợp tác)", text_lower):
        score_timeline = -40
        is_junk = True
        reasons.append("[-40] Không thiện chí / Hỏi cho vui")
        
    if re.search(r"(quận 1 giá 1|q1 giá 1|giá 1-2 tỷ|vài trăm triệu|thuê nguyên căn giá 2 triệu)", text_lower):
        score_budget = -50
        is_junk = True
        reasons.append("[-50] Yêu cầu phi thực tế / Ảo tưởng giá")

    if re.search(r"(bảo hiểm|vay vốn|mời chào dịch vụ|quảng cáo)", text_lower):
        score_persona = -80
        is_junk = True
        reasons.append("[-80] Spam / Quảng cáo dịch vụ")

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
            reasons.append("[+15] Ngân sách phân khúc 2-3 tỷ")

        # Tiêu chí 2: Loại hình & Vị trí
        if re.search(r"(penthouse|biệt thự đơn lập|quỹ đất công nghiệp|sàn văn phòng diện tích lớn|trên 2000m2)", text_lower):
            score_interest = 25
            is_vip = True
            reasons.append("[+25] BĐS Cao cấp / Quy mô lớn")
        elif re.search(r"(quận 1|ven sông|vinhomes ocean park|phú mỹ hưng)", text_lower):
            score_interest = 20
            reasons.append("[+20] Vị trí trung tâm / Đô thị cao cấp")
        elif re.search(r"(căn hộ 2pn|nhà phố liền kề|đất nền vùng ven|thuê mặt bằng)", text_lower):
            score_interest = 15
            reasons.append("[+15] Nhu cầu sản phẩm phổ biến")

        # Tiêu chí 3: Thời gian mua & Cấp thiết
        if re.search(r"(cuối tuần này|ngay trong tháng|cần ký hợp đồng dài hạn|muốn đi xem nhà mẫu)", text_lower):
            score_timeline = 20
            reasons.append("[+20] Thời gian cấp thiết / Xem ngay")
        elif re.search(r"(đang cân nhắc|cần tư vấn thêm|so sánh)", text_lower):
            score_timeline = 12
            reasons.append("[+12] Cần tư vấn / Đang cân nhắc")

        # Tiêu chí 4: Chân dung & Pháp lý
        if re.search(r"(chủ doanh nghiệp|nhà đầu tư chuyên nghiệp|mua sỉ)", text_lower):
            score_persona = 15
            is_vip = True
            reasons.append("[+15] Chân dung VIP (Chủ DN / Mua sỉ)")
        elif re.search(r"(pháp lý chuẩn 100%|sổ hồng riêng)", text_lower):
            score_persona = 10
            reasons.append("[+10] Yêu cầu pháp lý 100% / Sổ riêng")

        # Tiêu chí 5: Tương tác & Đòn bẩy
        if re.search(r"(hỗ trợ vay ngân hàng|chính sách chiết khấu)", text_lower):
            score_engagement = 8
            reasons.append("[+8] Thiện chí / Cần gói vay NH")

    # Tổng điểm và phân hạng
    total_raw = score_budget + score_interest + score_timeline + score_persona + score_engagement
    final_score = int(max(0, min(100, total_raw)))

    if is_junk or final_score < 40:
        category = "COLD"
        sla = "Nurturing / Drip Marketing (Không gọi)"
        action = "Đưa vào Blacklist hoặc nuôi dưỡng bằng Zalo OA tự động."
    elif is_vip or final_score >= 75:
        category = "HOT"
        sla = "Bàn giao ngay — Gọi lại trong < 15 phút"
        action = "Top Sales liên hệ trực tiếp, chuẩn bị hồ sơ dự án cao cấp."
    else:
        category = "WARM"
        sla = "Bàn giao theo ca — Phản hồi < 2 - 4 giờ"
        action = "Gửi thông tin dự án, tư vấn gói vay và đặt lịch xem nhà mẫu."

    return final_score, category, sla, action, " | ".join(reasons)


# ==========================================
# 3. QUẢN LÝ DỮ LIỆU & SESSION STATE
# ==========================================
def normalize_leads_df(df):
    df = df.copy()
    for col in ["id", "sdt", "ten_khach", "nhu_cau_mo_ta"]:
        if col in df.columns:
            df[col] = df[col].astype(str).replace("nan", "")
        else:
            df[col] = ""

    if "duyet" not in df.columns:
        df.insert(0, "duyet", False)
    else:
        df["duyet"] = df["duyet"].astype(bool)

    if "trang_thai_duyet" not in df.columns:
        df["trang_thai_duyet"] = "Chờ duyệt"
    if "sales_phu_trach" not in df.columns:
        df["sales_phu_trach"] = "Chưa gán"
    if "ghi_chu_sales" not in df.columns:
        df["ghi_chu_sales"] = ""

    if "diem_so" not in df.columns or "phan_loai" not in df.columns:
        scores, cats, slas, actions, reasons = [], [], [], [], []
        for _, row in df.iterrows():
            desc = str(row.get("nhu_cau_mo_ta", ""))
            s, c, sla, act, r = ai_score_lead(desc)
            scores.append(s)
            cats.append(c)
            slas.append(sla)
            actions.append(act)
            reasons.append(r)
        df["diem_so"] = scores
        df["phan_loai"] = cats
        df["sla"] = slas
        df["de_xuat_hanh_dong"] = actions
        df["ly_do_cham_diem"] = reasons
    else:
        df["diem_so"] = pd.to_numeric(df["diem_so"], errors="coerce").fillna(0).astype(int)

    return df

def load_default_data():
    sample_path = "sample-data/khach_hang_bds_sample.csv"
    if os.path.exists(sample_path):
        df = pd.read_csv(sample_path, dtype={"id": str, "sdt": str}, encoding='utf-8-sig')
    else:
        # Fallback dummy sample
        df = pd.DataFrame([
            {"id": "1", "ten_khach": "Phan Văn Hoa", "sdt": "0894782782", "nhu_cau_mo_ta": "Đang tìm thuê mặt bằng kinh doanh spa tại Quận 1, diện tích khoảng 80-100m2. Giá thuê dưới 50 triệu/tháng."},
            {"id": "2", "ten_khach": "Hồ Hồng Linh", "sdt": "0848475144", "nhu_cau_mo_ta": "Khách hàng nhầm số, không có nhu cầu về bất động sản."},
            {"id": "3", "ten_khach": "Lý Đức Cường", "sdt": "0953430096", "nhu_cau_mo_ta": "Quan tâm căn hộ 2PN tại Quận 7 cho gia đình trẻ. Tài chính 4-5 tỷ, cần vay ngân hàng 70%. Muốn xem nhà mẫu cuối tuần này."},
            {"id": "4", "ten_khach": "Lê Anh Lan", "sdt": "0964591036", "nhu_cau_mo_ta": "Tìm mua Penthouse diện tích lớn, có hồ bơi riêng và thang máy riêng. Ngân sách không thành vấn đề."},
            {"id": "28", "ten_khach": "Trần Hoàng Dũng", "sdt": "0943392982", "nhu_cau_mo_ta": "Chủ doanh nghiệp lớn, tìm quỹ đất công nghiệp trên 2000m2 khu Đông. Tài chính cực mạnh, pháp lý chuẩn 100%."}
        ])
    return normalize_leads_df(df)

if "leads_df" not in st.session_state:
    st.session_state.leads_df = load_default_data()


# ==========================================
# 4. THANH ĐIỀU KHIỂN BÊN TRÁI (SIDEBAR)
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/isometric/512/real-estate.png", width=70)
    st.title("Bộ Điều Khiển AI")
    st.caption("Agentic Real Estate Lead Scoring")
    st.divider()

    st.subheader("📥 Nguồn Dữ Liệu")
    uploaded_file = st.file_uploader("Tải lên file CSV / Excel", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                new_df = pd.read_csv(uploaded_file, dtype={"id": str, "sdt": str}, encoding='utf-8-sig')
            else:
                new_df = pd.read_excel(uploaded_file, dtype={"id": str, "sdt": str})
            if "nhu_cau_mo_ta" in new_df.columns or "mo_ta" in new_df.columns:
                st.session_state.leads_df = normalize_leads_df(new_df)
                st.success(f"Đã nạp {len(new_df)} bản ghi!")
                st.rerun()
            else:
                st.error("File cần có cột 'nhu_cau_mo_ta'!")
        except Exception as e:
            st.error(f"Lỗi đọc file: {e}")

    google_sheet_url = st.text_input(
        "Hoặc Google Sheets CSV URL",
        value="https://docs.google.com/spreadsheets/d/17odkUsLWSnrnOebV0LzPCP5ZWz3mm-yR09ZFjslwh1w/gviz/tq?tqx=out:csv&gid=1542775777"
    )
    if st.button("🔄 Tải từ Google Sheets", use_container_width=True):
        try:
            gs_df = pd.read_csv(google_sheet_url, dtype={"id": str, "sdt": str}, encoding='utf-8-sig')
            st.session_state.leads_df = normalize_leads_df(gs_df)
            st.success(f"Đã tải {len(gs_df)} khách từ Google Sheets!")
            st.rerun()
        except Exception as e:
            st.error(f"Lỗi kết nối Sheet: {e}")

    st.divider()
    st.subheader("⚡ Tác Vụ AI Agent")
    if st.button("🤖 AI Quét & Chấm Điểm Toàn Bộ", type="primary", use_container_width=True):
        with st.spinner("AI Agent đang phân tích 5 tiêu chí..."):
            df = st.session_state.leads_df.copy()
            scores, cats, slas, actions, reasons = [], [], [], [], []
            for _, row in df.iterrows():
                desc = str(row.get("nhu_cau_mo_ta", ""))
                s, c, sla, act, r = ai_score_lead(desc)
                scores.append(s)
                cats.append(c)
                slas.append(sla)
                actions.append(act)
                reasons.append(r)
            df["diem_so"] = scores
            df["phan_loai"] = cats
            df["sla"] = slas
            df["de_xuat_hanh_dong"] = actions
            df["ly_do_cham_diem"] = reasons
            st.session_state.leads_df = df
            st.success("Đã hoàn tất quét và chấm điểm!")
            st.rerun()

    st.divider()
    st.markdown("""
    **Quy Chuẩn SLA BĐS:**
    - 🔥 **HOT ($\ge 75$):** Gọi lại $< 15$ phút
    - ⛅ **WARM ($40-74$):** Tư vấn trong $2-4$ giờ
    - ❄️ **COLD ($< 40$):** Nuôi dưỡng tự động
    """)


# ==========================================
# 5. KHU VỰC NỘI DUNG CHÍNH (MAIN DASHBOARD)
# ==========================================

# Header Banner
st.markdown("""
<div class="main-header">
    <h1>🏢 AI LEAD SCORING & HUMAN-IN-THE-LOOP COCKPIT</h1>
    <p>Hệ thống phân loại khách hàng tiềm năng Bất Động Sản tự động kết hợp bàn giao Sales thông minh.</p>
</div>
""", unsafe_allow_html=True)

df_current = st.session_state.leads_df

# Thống kê nhanh KPIs
total_count = len(df_current)
hot_count = len(df_current[df_current.get("phan_loai", "") == "HOT"]) if "phan_loai" in df_current.columns else 0
warm_count = len(df_current[df_current.get("phan_loai", "") == "WARM"]) if "phan_loai" in df_current.columns else 0
cold_count = len(df_current[df_current.get("phan_loai", "") == "COLD"]) if "phan_loai" in df_current.columns else 0
approved_count = len(df_current[df_current.get("duyet", False) == True]) if "duyet" in df_current.columns else 0

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Tổng Khách Hàng</div>
        <div class="metric-value" style="color: #0f172a;">{total_count}</div>
        <div class="metric-sub">Dữ liệu nạp vào</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card hot">
        <div class="metric-title">🔥 Khách HOT (VIP)</div>
        <div class="metric-value" style="color: #ef4444;">{hot_count}</div>
        <div class="metric-sub">{f"{(hot_count/total_count*100):.1f}%" if total_count else "0%"} (SLA &lt;15p)</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card warm">
        <div class="metric-title">⛅ Khách WARM</div>
        <div class="metric-value" style="color: #f59e0b;">{warm_count}</div>
        <div class="metric-sub">{f"{(warm_count/total_count*100):.1f}%" if total_count else "0%"} (SLA &lt;4h)</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card cold">
        <div class="metric-title">❄️ Khách COLD / Rác</div>
        <div class="metric-value" style="color: #64748b;">{cold_count}</div>
        <div class="metric-sub">{f"{(cold_count/total_count*100):.1f}%" if total_count else "0%"} (Nuôi dưỡng)</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="metric-card approved">
        <div class="metric-title">✅ Đã Duyệt Chuyển</div>
        <div class="metric-value" style="color: #10b981;">{approved_count}</div>
        <div class="metric-sub">{f"{(approved_count/total_count*100):.1f}%" if total_count else "0%"} đã phê duyệt</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Bộ lọc hiển thị
filter_col1, filter_col2, filter_col3 = st.columns([2, 2, 3])
with filter_col1:
    selected_tier = st.multiselect(
        "Lọc theo Phân Loại:",
        options=["HOT", "WARM", "COLD"],
        default=["HOT", "WARM", "COLD"]
    )
with filter_col2:
    selected_status = st.multiselect(
        "Lọc theo Trạng Thái Duyệt:",
        options=["Tất cả", "Chờ duyệt", "Đã duyệt", "Đã bàn giao Sales", "Từ chối / Rác"],
        default=["Tất cả"]
    )
with filter_col3:
    search_query = st.text_input("🔍 Tìm theo Tên, SĐT hoặc Từ khóa nhu cầu:", placeholder="Nhập tên, số điện thoại, Penthouse, Q1...")

# Áp dụng bộ lọc
filtered_df = df_current.copy()
if selected_tier and "phan_loai" in filtered_df.columns:
    filtered_df = filtered_df[filtered_df["phan_loai"].isin(selected_tier)]

if "Tất cả" not in selected_status and "trang_thai_duyet" in filtered_df.columns:
    filtered_df = filtered_df[filtered_df["trang_thai_duyet"].isin(selected_status)]

if search_query:
    q = search_query.lower()
    mask = (
        filtered_df["ten_khach"].astype(str).str.lower().str.contains(q) |
        filtered_df["sdt"].astype(str).str.lower().str.contains(q) |
        filtered_df["nhu_cau_mo_ta"].astype(str).str.lower().str.contains(q)
    )
    filtered_df = filtered_df[mask]

# ==========================================
# 6. BẢNG DỮ LIỆU TƯƠNG TÁC (ST.DATA_EDITOR)
# ==========================================
st.subheader("📋 Bảng Duyệt Trạng Thái Khách Hàng (Human-in-the-Loop)")
st.caption("Chỉnh sửa trực tiếp trên bảng: Click chọn duyệt, đổi trạng thái, gán Sales hoặc thêm ghi chú.")

column_config = {
    "duyet": st.column_config.CheckboxColumn(
        "Duyệt?",
        help="Tích chọn để phê duyệt chuyển giao Lead cho Sales",
        default=False,
    ),
    "trang_thai_duyet": st.column_config.SelectboxColumn(
        "Trạng Thái Duyệt",
        help="Trạng thái phê duyệt con người",
        options=["Chờ duyệt", "Đã duyệt", "Đã bàn giao Sales", "Từ chối / Rác"],
        required=True,
    ),
    "sales_phu_trach": st.column_config.SelectboxColumn(
        "Sales Phụ Trách",
        help="Chỉ định nhân viên tiếp nhận cuộc gọi",
        options=["Chưa gán", "Nguyễn Văn A (Top Sales)", "Trần Thị B (VIP Sales)", "Lê Văn C (Tư vấn)", "Zalo OA Automation"],
        required=True,
    ),
    "diem_so": st.column_config.ProgressColumn(
        "Điểm AI",
        help="Điểm số đánh giá 5 tiêu chí từ AI",
        format="%d pts",
        min_value=0,
        max_value=100,
    ),
    "phan_loai": st.column_config.SelectboxColumn(
        "Xếp Hạng",
        options=["HOT", "WARM", "COLD"],
        required=True,
    ),
    "id": st.column_config.TextColumn("ID", width="small", disabled=True),
    "ten_khach": st.column_config.TextColumn("Họ Tên Khách", width="medium"),
    "sdt": st.column_config.TextColumn("Số Điện Thoại", width="small"),
    "sla": st.column_config.TextColumn("SLA Phản Hồi", width="medium", disabled=True),
    "nhu_cau_mo_ta": st.column_config.TextColumn("Mô Tả Nhu Cầu Gốc", width="large"),
    "ly_do_cham_diem": st.column_config.TextColumn("Căn Cứ Chấm Điểm (AI Insights)", width="large", disabled=True),
    "ghi_chu_sales": st.column_config.TextColumn("Ghi Chú Sales", width="medium"),
}

# Hiển thị st.data_editor
edited_df = st.data_editor(
    filtered_df,
    column_config=column_config,
    use_container_width=True,
    num_rows="dynamic",
    height=420,
    key="lead_editor"
)

# Nút lưu thay đổi vào session state
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 4])
with col_btn1:
    if st.button("💾 Lưu Trạng Thái Duyệt", use_container_width=True):
        st.session_state.leads_df.update(edited_df)
        st.success("Đã cập nhật trạng thái phê duyệt!")
        st.rerun()

with col_btn2:
    # Xuất file CSV
    csv_data = edited_df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    st.download_button(
        label="📥 Tải Báo Cáo CSV",
        data=csv_data,
        file_name="leads_approved_bds.csv",
        mime="text/csv",
        use_container_width=True
    )

st.divider()

# ==========================================
# 7. XUẤT THẺ BÀN GIAO CHO SALES (LEAD CARD PREVIEW)
# ==========================================
st.subheader("📲 Xem Trước Thẻ Bàn Giao Sales (Zalo / CRM Push Notification)")

lead_options = [f"#{row.get('id', idx)} - {row.get('ten_khach', 'Khách')} ({row.get('phan_loai', 'N/A')})" for idx, row in edited_df.iterrows()]

if lead_options:
    selected_lead_idx = st.selectbox("Chọn khách hàng để tạo Thẻ Bàn Giao:", range(len(lead_options)), format_func=lambda x: lead_options[x])
    selected_row = edited_df.iloc[selected_lead_idx]

    lead_tier = selected_row.get("phan_loai", "WARM")
    emoji = "🔥" if lead_tier == "HOT" else ("⛅" if lead_tier == "WARM" else "❄️")
    
    # Gợi ý kịch bản mở đầu
    desc_sample = str(selected_row.get("nhu_cau_mo_ta", ""))
    if "penthouse" in desc_sample.lower() or "biệt thự" in desc_sample.lower():
        ice_breaker = f"Dạ em chào anh/chị {selected_row.get('ten_khach')}, em là chuyên viên BĐS cao cấp. Em nhận được yêu cầu về căn {desc_sample[:40]}... Em đã chuẩn bị sẵn layout và hồ sơ pháp lý độc quyền gửi qua Zalo cho mình ạ."
    elif "2pn" in desc_sample.lower() or "vay" in desc_sample.lower():
        ice_breaker = f"Dạ chào anh/chị {selected_row.get('ten_khach')}, em gửi anh/chị bảng tính dòng tiền và chính sách hỗ trợ lãi suất 0% cho căn hộ 2PN mình đang quan tâm để gia đình tham khảo nhé ạ."
    else:
        ice_breaker = f"Dạ em chào anh/chị {selected_row.get('ten_khach')}, em liên hệ hỗ trợ thông tin chi tiết về nhu cầu BĐS mà anh/chị đang tìm kiếm ạ."

    lead_card_text = f"""🚨 [{lead_tier} LEAD ALERT - BẤT ĐỘNG SẢN] {emoji}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Khách hàng: {selected_row.get('ten_khach', 'N/A')} | ID: #{selected_row.get('id', 'N/A')}
📞 Số điện thoại: {selected_row.get('sdt', 'N/A')}
⭐ Điểm tiềm năng: {selected_row.get('diem_so', 0)}/100 (HẠNG {lead_tier} {emoji})
⏱️ SLA Gọi lại: {selected_row.get('sla', 'Trong ngày')}
👨‍💼 Sales phụ trách: {selected_row.get('sales_phu_trach', 'Chưa gán')}
📌 Trạng thái duyệt: {selected_row.get('trang_thai_duyet', 'Chờ duyệt')}

📋 Nhu cầu mô tả:
"{selected_row.get('nhu_cau_mo_ta', 'N/A')}"

💡 Căn cứ chấm điểm (AI Insights):
{selected_row.get('ly_do_cham_diem', 'Đánh giá tổng hợp')}

🎯 Gợi ý kịch bản mở đầu (Ice-breaker):
"{ice_breaker}"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    st.markdown(f'<div class="handover-card">{lead_card_text}</div>', unsafe_allow_html=True)
    st.write("")
    if st.button("📋 Sao Chép Thẻ Bàn Giao", use_container_width=False):
        st.info("💡 Bạn có thể bôi đen và sao chép trực tiếp nội dung phía trên để gửi vào Zalo / CRM.")
else:
    st.info("Không có dữ liệu phù hợp với bộ lọc hiện tại.")
