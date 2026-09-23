"""
Hệ thống Chấm Điểm Khách Hàng Tiềm Năng Bất Động Sản (AI Lead Scoring App)
Phát triển trên nền tảng Streamlit với tính năng Human-in-the-loop st.data_editor.
Tích hợp AI Scoring Agent theo tiêu chuẩn 5 tiêu chí từ tieu_chi_cham_diem.txt.
"""

import streamlit as st
import pandas as pd
import re
import json
import os
import io

# 1. CẤU HÌNH TRANG STREAMLIT
st.set_page_config(
    page_title="Hệ Thống Chấm Điểm Lead BĐS — AI Lead Scoring",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tùy chỉnh CSS cho giao diện hiện đại, chuyên nghiệp
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .badge-hot {
        background-color: #FEE2E2;
        color: #DC2626;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .badge-warm {
        background-color: #FEF3C7;
        color: #D97706;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .badge-cold {
        background-color: #E2E8F0;
        color: #475569;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .lead-card-box {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-left: 5px solid #3B82F6;
        border-radius: 8px;
        padding: 18px;
        margin-top: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)


# 2. CORE ENGINE: AI LEAD SCORING AGENT (5 TIÊU CHÍ)
def ai_score_lead(text: str) -> dict:
    """
    Hàm phân tích ngôn ngữ tự nhiên quét mô tả nhu cầu khách hàng theo 5 tiêu chí:
    1. Ngân sách (Budget - 35đ)
    2. Loại hình & Vị trí (Interest & Fit - 25đ)
    3. Thời gian & Tính cấp thiết (Timeline - 20đ)
    4. Nguồn khách & Chân dung (Persona - 15đ)
    5. Tương tác & Đòn bẩy tài chính (Engagement - 10đ)
    Tích hợp bộ tiêu chí tieu_chi_cham_diem.txt (+50 VIP, -50 đến -80 Rác/Spam).
    """
    text_lower = text.lower() if isinstance(text, str) else ""
    
    score_budget = 10
    score_interest = 10
    score_timeline = 10
    score_persona = 5
    score_engagement = 5
    
    reasons = []
    is_vip = False
    is_junk = False

    # A. TIÊU CHÍ TRỪ ĐIỂM / LỌC DỮ LIỆU RÁC (Cold Triggers)
    if re.search(r"(nhầm số|không có nhu cầu|dữ liệu cũ|nhầm ngành)", text_lower):
        score_persona = -50
        is_junk = True
        reasons.append("❌ Nhầm số / Dữ liệu rác (-50đ)")
        
    if re.search(r"(thuê bao|không bắt máy|không phản hồi zalo|gọi nhiều lần)", text_lower):
        score_engagement = -40
        is_junk = True
        reasons.append("📵 Thông tin liên lạc lỗi / Thuê bao (-40đ)")
        
    if re.search(r"(hỏi giá cho vui|chưa có ý định mua|thái độ không hợp tác)", text_lower):
        score_timeline = -40
        is_junk = True
        reasons.append("⚠️ Không thiện chí / Hỏi cho vui (-40đ)")
        
    if re.search(r"(quận 1 giá 1|q1 giá 1|giá 1-2 tỷ|vài trăm triệu|thuê nguyên căn giá 2 triệu)", text_lower):
        score_budget = -50
        is_junk = True
        reasons.append("🛑 Yêu cầu phi thực tế / Ảo tưởng giá (-50đ)")

    if re.search(r"(bảo hiểm|vay vốn|mời chào dịch vụ|quảng cáo)", text_lower):
        score_persona = -80
        is_junk = True
        reasons.append("🚫 Spam / Quảng cáo dịch vụ (-80đ)")

    # B. TIÊU CHÍ CỘNG ĐIỂM TIỀM NĂNG & VIP
    if not is_junk:
        # Tiêu chí 1: Ngân sách
        if re.search(r"(20\s*tỷ|30\s*tỷ|50\s*tỷ|100\s*tỷ|tài chính cực mạnh|tài chính mạnh|không thành vấn đề)", text_lower):
            score_budget = 35
            is_vip = True
            reasons.append("💎 Ngân sách VIP >= 20 tỷ / Tài chính mạnh (+35đ)")
        elif re.search(r"(8-10\s*tỷ|5-7\s*tỷ|4-5\s*tỷ|3-10\s*tỷ)", text_lower):
            score_budget = 25
            reasons.append("💰 Ngân sách tầm trung 4-10 tỷ (+25đ)")
        elif re.search(r"(2-3\s*tỷ|dưới 50 triệu)", text_lower):
            score_budget = 15
            reasons.append("💵 Phân khúc phổ thông 2-3 tỷ / Thuê 50tr (+15đ)")

        # Tiêu chí 2: Loại hình & Vị trí
        if re.search(r"(penthouse|biệt thự đơn lập|quỹ đất công nghiệp|sàn văn phòng diện tích lớn|trên 2000m2)", text_lower):
            score_interest = 25
            is_vip = True
            reasons.append("🏰 BĐS Cao cấp / Penthouse / Quỹ đất lớn (+25đ)")
        elif re.search(r"(quận 1|ven sông|vinhomes ocean park|phú mỹ hưng)", text_lower):
            score_interest = 20
            reasons.append("📍 Vị trí đắc địa (Q1, Ven sông, KĐT lớn) (+20đ)")
        elif re.search(r"(căn hộ 2pn|nhà phố liền kề|đất nền vùng ven|thuê mặt bằng)", text_lower):
            score_interest = 15
            reasons.append("🏠 Nhu cầu thực tế (Căn hộ 2PN, Nhà phố, Mặt bằng) (+15đ)")

        # Tiêu chí 3: Thời gian & Cấp thiết
        if re.search(r"(cuối tuần này|ngay trong tháng|cần ký hợp đồng dài hạn|muốn đi xem nhà mẫu)", text_lower):
            score_timeline = 20
            reasons.append("⚡ Tính cấp thiết cao / Xem nhà cuối tuần (+20đ)")
        elif re.search(r"(đang cân nhắc|cần tư vấn thêm|so sánh)", text_lower):
            score_timeline = 12
            reasons.append("🔍 Đang tìm hiểu / Cân nhắc chính sách (+12đ)")

        # Tiêu chí 4: Chân dung & Pháp lý
        if re.search(r"(chủ doanh nghiệp|nhà đầu tư chuyên nghiệp|mua sỉ)", text_lower):
            score_persona = 15
            is_vip = True
            reasons.append("👑 Chân dung VIP (Chủ DN / Mua sỉ) (+15đ)")
        elif re.search(r"(pháp lý chuẩn 100%|sổ hồng riêng)", text_lower):
            score_persona = 10
            reasons.append("📜 Yêu cầu Pháp lý minh bạch / Sổ hồng riêng (+10đ)")

        # Tiêu chí 5: Tương tác & Đòn bẩy
        if re.search(r"(hỗ trợ vay ngân hàng|chính sách chiết khấu)", text_lower):
            score_engagement = 8
            reasons.append("🤝 Nhu cầu gói vay / Chính sách chiết khấu (+8đ)")

    # Tổng điểm và phân hạng
    total_raw = score_budget + score_interest + score_timeline + score_persona + score_engagement
    final_score = max(0, min(100, total_raw))

    if is_junk or final_score < 40:
        category = "❄️ COLD"
        sla = "Tự động hóa Nurturing / Blacklist"
        action = "Đưa vào luồng Zalo/Email Drip hoặc Blacklist"
        script_hint = "Gửi tin nhắn tự động thăm dò hoặc không làm phiền."
    elif is_vip or final_score >= 75:
        category = "🔥 HOT"
        sla = "< 15 Phút (Ưu tiên gọi ngay)"
        action = "Top Sales liên hệ trực tiếp, chuẩn bị layout & hồ sơ VIP"
        script_hint = "Chào anh/chị, em gửi layout chi tiết & hồ sơ pháp lý 100% qua Zalo để hẹn lịch xem thực tế..."
    else:
        category = "⛅ WARM"
        sla = "< 2 - 4 Giờ"
        action = "Tư vấn gói vay ngân hàng, gửi bảng tính dòng tiền và hẹn xem nhà mẫu"
        script_hint = "Chào anh/chị, bên em có chính sách hỗ trợ lãi suất 0% cho căn hộ 2PN rất phù hợp với mình..."

    return {
        "diem_ai": final_score,
        "phan_loai_ai": category,
        "sla": sla,
        "hanh_dong": action,
        "ly_do": " | ".join(reasons) if reasons else "Nhu cầu tiêu chuẩn",
        "kich_ban": script_hint
    }


# 3. HÀM TẢI DỮ LIỆU BAN ĐẦU
@st.cache_data
def load_default_dataset():
    local_path = "sample-data/khach_hang_bds_sample.csv"
    if os.path.exists(local_path):
        return pd.read_csv(local_path)
    
    # Fallback to Google Sheets link
    sheet_url = "https://docs.google.com/spreadsheets/d/17odkUsLWSnrnOebV0LzPCP5ZWz3mm-yR09ZFjslwh1w/gviz/tq?tqx=out:csv&gid=1542775777"
    try:
        return pd.read_csv(sheet_url)
    except Exception:
        # Minimal sample fallback
        return pd.DataFrame([
            {"id": 1, "ten_khach": "Phan Văn Hoa", "sdt": "0894782782", "nhu_cau_mo_ta": "Đang tìm thuê mặt bằng kinh doanh spa tại Quận 1, diện tích khoảng 80-100m2. Giá dưới 50 triệu/tháng."},
            {"id": 2, "ten_khach": "Hồ Hồng Linh", "sdt": "0848475144", "nhu_cau_mo_ta": "Khách hàng nhầm số, không có nhu cầu về bất động sản."},
            {"id": 3, "ten_khach": "Lý Đức Cường", "sdt": "0953430096", "nhu_cau_mo_ta": "Quan tâm căn hộ 2PN tại Quận 7, tài chính 4-5 tỷ, cần vay 70%, xem cuối tuần."},
            {"id": 4, "ten_khach": "Lê Anh Lan", "sdt": "0964591036", "nhu_cau_mo_ta": "Tìm mua Penthouse diện tích lớn có hồ bơi riêng. Ngân sách không thành vấn đề."}
        ])


# 4. KHỞI TẠO SESSION STATE
if "leads_df" not in st.session_state:
    raw_df = load_default_dataset()
    
    # Chạy AI Scoring lần đầu
    scored_records = []
    for _, row in raw_df.iterrows():
        desc = str(row.get("nhu_cau_mo_ta", ""))
        analysis = ai_score_lead(desc)
        
        # Gán giá trị mặc định cho Human-in-the-loop review
        default_status = "Chờ duyệt"
        default_assigned = "Chưa gán"
        if analysis["phan_loai_ai"] == "🔥 HOT":
            default_assigned = "Top Sales VIP 1"
        
        scored_records.append({
            "id": row.get("id", ""),
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
            "ly_do": analysis["ly_do"],
            "kich_ban": analysis["kich_ban"]
        })
    st.session_state.leads_df = pd.DataFrame(scored_records)


# 5. SIDEBAR: ĐIỀU HƯỚNG VÀ BỘ LỌC
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/real-estate.png", width=64)
    st.markdown("### 🏢 **Cấu Hình & Bộ Lọc**")
    
    # Tải file dữ liệu mới
    uploaded_file = st.file_uploader("📥 Tải file Lead mới (.csv, .xlsx)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                new_df = pd.read_csv(uploaded_file)
            else:
                new_df = pd.read_excel(uploaded_file)
            
            if st.button("⚡ Chấm Điểm & Nạp Dữ Liệu Mới", use_container_width=True, type="primary"):
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
                        "ly_do": analysis["ly_do"],
                        "kich_ban": analysis["kich_ban"]
                    })
                st.session_state.leads_df = pd.DataFrame(new_records)
                st.success("Đã nạp và chấm điểm thành công!")
                st.rerun()
        except Exception as e:
            st.error(f"Lỗi khi đọc file: {e}")

    st.markdown("---")
    st.markdown("#### 🔍 **Lọc Dữ Liệu Bảng**")
    
    filter_category = st.multiselect(
        "Phân loại Lead:",
        options=["🔥 HOT", "⛅ WARM", "❄️ COLD"],
        default=["🔥 HOT", "⛅ WARM", "❄️ COLD"]
    )
    
    filter_status = st.multiselect(
        "Trạng thái duyệt:",
        options=["Chờ duyệt", "✅ Đã duyệt bàn giao", "⚠️ Cần kiểm tra lại", "⛔ Từ chối / Blacklist"],
        default=["Chờ duyệt", "✅ Đã duyệt bàn giao", "⚠️ Cần kiểm tra lại", "⛔ Từ chối / Blacklist"]
    )
    
    search_keyword = st.text_input("🔎 Tìm kiếm tên / SĐT / nhu cầu:", placeholder="Nhập từ khóa...")

    st.markdown("---")
    st.markdown("#### ⚙️ **Thao Tác Nhanh**")
    if st.button("⚡ Duyệt nhanh toàn bộ Lead HOT", use_container_width=True):
        mask = st.session_state.leads_df["phan_loai_chot"] == "🔥 HOT"
        st.session_state.leads_df.loc[mask, "duyet_trang_thai"] = "✅ Đã duyệt bàn giao"
        st.session_state.leads_df.loc[mask, "da_duyet"] = True
        st.success("Đã duyệt bàn giao toàn bộ Lead HOT!")
        st.rerun()

    if st.button("🔄 Reset Dữ Liệu Về Mặc Định", use_container_width=True):
        st.session_state.pop("leads_df", None)
        st.rerun()


# 6. HEADER & DASHBOARD METRICS
st.markdown('<div class="main-title">🏢 Hệ Thống Chấm Điểm & Phê Duyệt Lead Bất Động Sản</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ứng dụng AI Agentic Workflow kết hợp <b>Human-in-the-loop</b> để phân loại, thẩm định và bàn giao khách hàng tiềm năng cho Sales.</div>', unsafe_allow_html=True)

df = st.session_state.leads_df

# Tính toán các chỉ số Dashboard
total_leads = len(df)
hot_count = len(df[df["phan_loai_chot"] == "🔥 HOT"])
warm_count = len(df[df["phan_loai_chot"] == "⛅ WARM"])
cold_count = len(df[df["phan_loai_chot"] == "❄️ COLD"])
approved_count = len(df[df["duyet_trang_thai"] == "✅ Đã duyệt bàn giao"])

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("📋 Tổng số Lead", f"{total_leads} khách")
with col2:
    st.metric("🔥 Lead HOT (VIP)", f"{hot_count} ({hot_count/total_leads*100:.1f}%)" if total_leads else "0")
with col3:
    st.metric("⛅ Lead WARM (Nhu cầu)", f"{warm_count} ({warm_count/total_leads*100:.1f}%)" if total_leads else "0")
with col4:
    st.metric("❄️ Lead COLD / Rác", f"{cold_count} ({cold_count/total_leads*100:.1f}%)" if total_leads else "0")
with col5:
    st.metric("✅ Đã Duyệt Bàn Giao", f"{approved_count} ({approved_count/total_leads*100:.1f}%)" if total_leads else "0")

st.markdown("---")


# 7. BẢNG PHÊ DUYỆT HUMAN-IN-THE-LOOP (st.data_editor)
st.markdown("### 📝 **Bảng Thẩm Định & Phê Duyệt Trạng Thái (Human-in-the-loop)**")
st.caption("💡 **Hướng dẫn:** Bạn có thể chỉnh sửa trực tiếp cột **Duyệt Trạng Thái**, **Phân Loại Chốt**, **Sales Phụ Trách**, **Ghi Chú** ngay trên bảng. Dữ liệu sẽ tự động lưu.")

# Áp dụng bộ lọc hiển thị
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

# Cấu hình các cột hiển thị trong st.data_editor
column_config = {
    "id": st.column_config.NumberColumn("ID", width="small", disabled=True),
    "ten_khach": st.column_config.TextColumn("Họ & Tên", width="medium"),
    "sdt": st.column_config.TextColumn("Số Điện Thoại", width="small"),
    "nhu_cau_mo_ta": st.column_config.TextColumn("Nhu Cầu Khách Hàng (Mô tả)", width="large", disabled=True),
    "diem_ai": st.column_config.ProgressColumn(
        "Điểm AI",
        help="Thang điểm 0 - 100 do AI Agent tính toán",
        min_value=0,
        max_value=100,
        format="%d",
        width="small"
    ),
    "phan_loai_ai": st.column_config.TextColumn("Gợi Ý AI", width="small", disabled=True),
    "duyet_trang_thai": st.column_config.SelectboxColumn(
        "Duyệt Trạng Thái",
        help="Chọn trạng thái phê duyệt bàn giao cho Sales",
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
    "ly_do": None,
    "kich_ban": None
}

# Hiển thị st.data_editor
edited_df = st.data_editor(
    filtered_df,
    column_config=column_config,
    use_container_width=True,
    num_rows="dynamic",
    height=400,
    key="lead_data_editor"
)

# Đồng bộ ngược lại st.session_state khi người dùng chỉnh sửa bảng
if not edited_df.equals(filtered_df):
    for idx, row in edited_df.iterrows():
        lead_id = row["id"]
        # Cập nhật các trường cho phép chỉnh sửa vào state chính
        mask = st.session_state.leads_df["id"] == lead_id
        if mask.any():
            st.session_state.leads_df.loc[mask, "duyet_trang_thai"] = row["duyet_trang_thai"]
            st.session_state.leads_df.loc[mask, "phan_loai_chot"] = row["phan_loai_chot"]
            st.session_state.leads_df.loc[mask, "sales_phu_trach"] = row["sales_phu_trach"]
            st.session_state.leads_df.loc[mask, "ghi_chu_tham_dinh"] = row["ghi_chu_tham_dinh"]
            st.session_state.leads_df.loc[mask, "da_duyet"] = (row["duyet_trang_thai"] == "✅ Đã duyệt bàn giao")

st.markdown("---")


# 8. CHI TIẾT LEAD & KỊCH BẢN MỞ ĐẦU TELESALE (LEAD CARD INSPECTOR)
st.markdown("### 🎯 **Chi Tiết Thẩm Định & Thẻ Bàn Giao Cho Sales (Lead Card)**")

selected_ids = df["id"].tolist()
col_select, col_preview = st.columns([1, 2])

with col_select:
    selected_id = st.selectbox(
        "Chọn khách hàng để xem phân tích AI chuyên sâu:",
        options=selected_ids,
        format_func=lambda x: f"ID #{x} — {df[df['id']==x]['ten_khach'].values[0]} ({df[df['id']==x]['phan_loai_chot'].values[0]})"
    )

selected_row = df[df["id"] == selected_id].iloc[0]

with col_preview:
    badge_class = "badge-hot" if "HOT" in selected_row["phan_loai_chot"] else ("badge-warm" if "WARM" in selected_row["phan_loai_chot"] else "badge-cold")
    
    st.markdown(f"""
    <div class="lead-card-box">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h4 style="margin:0; color:#1E293B;">👤 {selected_row['ten_khach']} <span style="font-size: 0.9rem; color:#64748B;">(ID: #{selected_row['id']})</span></h4>
            <span class="{badge_class}">{selected_row['phan_loai_chot']}</span>
        </div>
        <p>📞 <b>Số điện thoại:</b> {selected_row['sdt']} &nbsp;|&nbsp; ⏱️ <b>SLA Phản Hồi:</b> <span style="color:#DC2626; font-weight:600;">{selected_row['sla']}</span></p>
        <p>📋 <b>Nhu cầu ghi nhận:</b> <i>"{selected_row['nhu_cau_mo_ta']}"</i></p>
        <hr style="margin: 10px 0; border: none; border-top: 1px dashed #CBD5E1;">
        <p>💡 <b>Căn cứ AI chấm điểm ({selected_row['diem_ai']}/100 điểm):</b><br>
        <code>{selected_row['ly_do']}</code></p>
        <p>🎯 <b>Gợi ý kịch bản mở đầu cho Sales:</b><br>
        <span style="color:#047857; font-weight:500;">"{selected_row['kich_ban']}"</span></p>
        <p>👨‍💼 <b>Sales phụ trách:</b> <code>{selected_row['sales_phu_trach']}</code> &nbsp;|&nbsp; <b>Trạng thái duyệt:</b> <b>{selected_row['duyet_trang_thai']}</b></p>
    </div>
    """, unsafe_allow_html=True)


# 9. XUẤT BÁO CÁO & BÀN GIAO CRM / SHEET
st.markdown("---")
st.markdown("### 📤 **Kết Xuất Dữ Liệu Bàn Giao (Export & CRM Integration)**")

col_exp1, col_exp2, col_exp3 = st.columns([1, 1, 2])

with col_exp1:
    # Xuất danh sách toàn bộ hoặc danh sách đã duyệt
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, encoding="utf-8-sig")
    st.download_button(
        label="📥 Tải Toàn Bộ Lead (.CSV)",
        data=csv_buffer.getvalue(),
        file_name="lead_scoring_all.csv",
        mime="text/csv",
        use_container_width=True
    )

with col_exp2:
    approved_only_df = df[df["duyet_trang_thai"] == "✅ Đã duyệt bàn giao"]
    csv_approved_buffer = io.StringIO()
    approved_only_df.to_csv(csv_approved_buffer, index=False, encoding="utf-8-sig")
    st.download_button(
        label=f"⭐ Tải Danh Sách Đã Duyệt ({len(approved_only_df)} Lead)",
        data=csv_approved_buffer.getvalue(),
        file_name="lead_scoring_approved_sales.csv",
        mime="text/csv",
        disabled=(len(approved_only_df) == 0),
        use_container_width=True,
        type="primary"
    )

with col_exp3:
    # Mẫu tin nhắn bắn vào Zalo Group
    zalo_msg = f"""🚨 [HOT LEAD BẤT ĐỘNG SẢN] 🚨
👤 Khách hàng: {selected_row['ten_khach']} | SĐT: {selected_row['sdt']}
⭐ Điểm AI: {selected_row['diem_ai']}/100 ({selected_row['phan_loai_chot']})
⏱️ SLA: {selected_row['sla']}
📋 Nhu cầu: {selected_row['nhu_cau_mo_ta']}
🎯 Kịch bản: "{selected_row['kich_ban']}"
👉 Sales tiếp nhận: {selected_row['sales_phu_trach']}"""
    
    with st.expander("💬 Xem mẫu tin nhắn đẩy vào Zalo / CRM Webhook"):
        st.code(zalo_msg, language="text")

st.caption("Khóa học: **Agentic AI with Google Antigravity** | Phát triển bởi **AI4A & Real Estate Tech Team**")
