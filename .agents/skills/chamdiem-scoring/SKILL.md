---
name: Chamdiem_scoring
description: "Hệ thống chấm điểm khách hàng tiềm năng (Lead Scoring) chuyên sâu ngành Bất Động Sản. Tự động đánh giá 5 tiêu chí (Ngân sách, Nhu cầu/Loại hình, Thời gian mua, Nguồn khách, Tương tác), phân loại HOT/WARM/COLD, tính điểm VIP/Rác theo tieu_chi_cham_diem.txt, cảnh báo rủi ro AI và thiết lập giao thức bàn giao SLA cho Sales."
user-invocable: true
when_to_use: "Sử dụng khi cần chấm điểm danh sách khách hàng BĐS từ Google Sheets/CSV/CRM, phân loại mức độ tiềm năng HOT/WARM/COLD, lọc bỏ data rác và xuất thẻ bàn giao cho đội ngũ Sales."
category: real-estate
keywords: [lead-scoring, bat-dong-san, real-estate, cham-diem-lead, hot-warm-cold, sales-handover, ai4a]
argument-hint: "[lead_file_or_sheet_url] [--hot] [--warm] [--cold] [--export-csv] [--report]"
metadata:
  author: "AI4A Team & Real Estate Specialists"
  course: "Agentic AI with Google Antigravity"
  version: "1.0.0"
---

# Chamdiem_scoring — Hệ Thống Chấm Điểm Khách Hàng Tiềm Năng Bất Động Sản

> **Bộ kỹ năng chuẩn hóa chuyên sâu cho ngành Bất Động Sản (Real Estate Lead Scoring)**  
> Tích hợp bộ tiêu chí chuẩn từ [tieu_chi_cham_diem.txt](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/knowledge-base/tieu_chi_cham_diem.txt) và cơ chế tự động hóa Google Sheets / CSV.

---

## 1. Định Nghĩa Lead Scoring & Tầm Quan Trọng Trong Bất Động Sản

### 1.1. Lead Scoring trong Bất Động Sản là gì?
**Lead Scoring (Chấm điểm khách hàng tiềm năng)** là phương pháp định lượng giá trị và mức độ sẵn sàng giao dịch của từng khách hàng dựa trên dữ liệu hành vi, nhân khẩu học, khả năng tài chính và nội dung mô tả nhu cầu. 

Thay vì để đội ngũ Sales gọi điện dàn trải ngẫu nhiên theo danh sách dài hàng trăm số, Lead Scoring giúp xếp hạng từng khách hàng theo thang điểm chuẩn hóa ($0 - 100$) để xác định chính xác **Ai nên được gọi ngay lập tức** và **Ai cần đưa vào luồng nuôi dưỡng tự động**.

### 1.2. Tại sao Lead Scoring sống còn đối với doanh nghiệp BĐS?
1. **Tối ưu hóa thời gian "Vàng" của Sales (Speed-to-Lead):** Khách hàng BĐS có tính nóng rất cao. Tiếp cận khách hàng VIP/HOT trong vòng **15 phút đầu** tăng tỷ lệ chốt cọc lên gấp 4-8 lần so với việc để trễ qua ngày hôm sau.
2. **Loại bỏ lãng phí nhân lực & Giảm Burn-out Telesale:** Ngành BĐS chịu tỷ lệ "data rác" (nhầm số, hỏi cho vui, môi giới khác dò giá, spam) lên tới $40\% - 60\%$. Lead Scoring loại bỏ rác ngay từ đầu, giúp Sales giữ vững năng lượng cho các Deal thực sự giá trị.
3. **Phân bổ nhân sự chính xác (Skill-based Routing):** Khách hàng VIP ($\ge 20$ tỷ, Penthouse, Biệt thự) được tự động chuyển cho **Top Sales / Trưởng phòng**, trong khi khách hàng tầm trung được giao cho chuyên viên tư vấn tiêu chuẩn.
4. **Đo lường ROI chiến dịch Marketing:** Giúp Marketing nhận biết kênh quảng cáo nào (Facebook, Google, TikTok, Sự kiện) mang về Lead chất lượng cao thay vì chỉ nhìn vào số lượng số điện thoại thu về.

---

## 2. Quy Trình Chấm Điểm 5 Tiêu Chí Chuẩn BĐS

Quy trình đánh giá vận hành dựa trên khung 5 trụ cột kết hợp với bộ tiêu chí đặc thù ngành BĐS:

```text
       ┌────────────────────────────────────────────────────────┐
       │             5 TIÊU CHÍ CHẤM ĐIỂM BĐS                   │
       ├────────────────────────────────────────────────────────┤
       │ 1. Ngân sách (Budget / Tài chính)            - 30%     │
       │ 2. Mức độ quan tâm & Loại hình (Interest)     - 25%     │
       │ 3. Thời gian mua / Cấp thiết (Timeline)       - 20%     │
       │ 4. Nguồn khách & Chân dung (Source/Persona)   - 15%     │
       │ 5. Tương tác & Thiện chí (Engagement)         - 10%     │
       └────────────────────────────────────────────────────────┘
```

### 2.1. Chi tiết 5 Tiêu Chí Đánh Giá

#### Tiêu chí 1: Ngân Sách (Budget - Trọng số 30%)
- **Siêu lớn ($\ge 20$ tỷ / Không thành vấn đề):** $+50$ điểm.
- **Tầm trung - khá ($4 - 10$ tỷ):** $+20$ điểm.
- **Tầm thấp - đầu tư nhỏ ($1 - 3$ tỷ):** $+10$ điểm.
- **Yêu cầu phi thực tế / Ảo tưởng giá** *(VD: Mua nhà Q1 giá 1-2 tỷ, vài trăm triệu trung tâm)*: $-60$ điểm.

#### Tiêu chí 2: Mức Độ Quan Tâm & Loại Hình Phù Hợp (Interest & Fit - Trọng số 25%)
- **BĐS Cao cấp / Quy mô lớn:** Biệt thự đơn lập, Penthouse, Shophouse mặt đường lớn, Quỹ đất công nghiệp, Sàn văn phòng diện tích lớn ($>2000\text{m}^2$): $+40 \rightarrow +50$ điểm.
- **Vị trí đắc địa:** Quận 1, Ven sông, Vinhomes Ocean Park, Phú Mỹ Hưng, Thảo Điền: $+30$ điểm.
- **Loại hình tiêu chuẩn có nhu cầu thực:** Căn hộ 2PN-3PN, Nhà phố liền kề, Đất nền vùng ven có sổ: $+15 \rightarrow +20$ điểm.

#### Tiêu chí 3: Thời Gian Mua / Tính Cấp Thiết (Timeline & Urgency - Trọng số 20%)
- **Rất cấp thiết:** Xem nhà cuối tuần này, cần ký hợp đồng dài hạn ngay, muốn gặp trực tiếp CĐT đàm phán: $+25 \rightarrow +30$ điểm.
- **Cân nhắc phương án tài chính:** Đang tìm hiểu gói vay ngân hàng, so sánh chính sách chiết khấu giữa 2 dự án: $+15$ điểm.
- **Không có kế hoạch mua:** *"Hỏi giá cho vui"*, *"Chưa có ý định mua trong năm nay"*: $-50$ điểm.

#### Tiêu chí 4: Nguồn Khách & Chân Dung (Source & Persona - Trọng số 15%)
- **Chân dung VIP:** Chủ doanh nghiệp, Nhà đầu tư chuyên nghiệp, Mua sỉ / Mua theo tầng: $+40$ điểm.
- **Pháp lý minh bạch:** Yêu cầu sổ hồng riêng, pháp lý chuẩn 100%, không dính quy hoạch: $+30$ điểm.
- **Spam / Mời chào dịch vụ:** Bảo hiểm, vay vốn tín chấp, SEO, quảng cáo: $-80$ điểm.

#### Tiêu chí 5: Tương Tác & Thiện Chí (Engagement - Trọng số 10%)
- **Thiện chí cao:** Cung cấp đầy đủ thông tin, phản hồi nhanh, sẵn sàng trao đổi chi tiết.
- **Dữ liệu lỗi / Không tương tác:** Thuê bao, gọi nhiều lần không nghe máy, không phản hồi Zalo: $-50$ điểm.
- **Nhầm số / Rác:** Nhầm số, không có nhu cầu BĐS, dữ liệu cũ: $-60$ điểm.

> 📖 *Xem bảng chi tiết trọng số và từ khóa regex tại [references/scoring-matrix.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/references/scoring-matrix.md).*

---

## 3. Cách Phân Loại HOT / WARM / COLD & Ma Trận Hành Động

| Phân Loại | Thang Điểm | Dấu Hiệu Đặc Trưng | Hành Động Dành Cho Sales | SLA Phản Hồi |
| :---: | :---: | :--- | :--- | :---: |
| 🔥 **HOT** | **70 – 100 điểm**<br>*(hoặc có tín hiệu VIP)* | - Ngân sách $\ge 20$ tỷ hoặc tài chính cực mạnh<br>- Mua Penthouse, Biệt thự, Quỹ đất CN, Sàn lớn<br>- Yêu cầu gặp CĐT / Pháp lý chuẩn 100% | - Bàn giao cho **Top Sales / Trưởng nhóm**<br>- Chuẩn bị layout & chính sách VIP<br>- Chốt lịch xem thực tế trong 48h | **< 15 phút** *(Tức thì)* |
| ⛅ **WARM** | **35 – 69 điểm** | - Nhu cầu ở/đầu tư thực (Căn hộ 2PN, Nhà phố, Mặt bằng, Đất nền 2-10 tỷ)<br>- Cần tư vấn gói vay ngân hàng, so sánh chiết khấu<br>- Muốn xem nhà mẫu cuối tuần | - Chuyên viên tư vấn gọi điện chia sẻ giải pháp tài chính<br>- Kết bạn Zalo gửi bảng tính dòng tiền<br>- Mời tham gia sự kiện mở bán | **< 2 – 4 giờ** |
| ❄️ **COLD** | **0 – 34 điểm**<br>*(hoặc điểm âm)* | - Nhầm số, không có nhu cầu, dữ liệu cũ<br>- Hỏi cho vui, đòi mua nhà Q1 giá 1 tỷ<br>- Thuê bao, không bắt máy, spam dịch vụ | - **Không gọi trực tiếp** (tránh tốn thời gian)<br>- Đưa vào luồng Email / Zalo OA Nurturing<br>- Nếu là Spam/Nhầm số $\rightarrow$ Đưa vào Blacklist | **Tự động hóa** |

---

## 4. Lưu Ý Quan Trọng Khi AI Chấm Điểm Tự Động (Giới Hạn & Rủi Ro)

Khi triển khai AI chấm điểm tự động trong thực tế, cần tuân thủ các nguyên tắc an toàn:

### 4.1. Hiện tượng Ảo giác (Hallucination) & Hiểu sai ngữ cảnh
- **Nguy cơ:** AI có thể nhầm lẫn giữa khách hàng *"tìm thuê mặt bằng dưới 50 triệu"* với khách *"mua bất động sản 50 tỷ"* nếu chỉ bắt từ khóa con số đơn lẻ.
- **Biện pháp:** Sử dụng công thức Regex kết hợp cấu trúc ngữ pháp và phân tích ngữ cảnh (thuê vs mua, triệu vs tỷ).

### 4.2. Xử lý thuật ngữ địa phương & Tiếng lóng BĐS
- AI cần nhận diện chính xác các từ viết tắt thông dụng: *2PN (2 phòng ngủ), CĐT (Chủ đầu tư), SHR (Sổ hồng riêng), Q1/Q7 (Quận 1, Quận 7), HĐMB (Hợp đồng mua bán), Ngộp/Cắt lỗ (Cần bán gấp)*.
- Tránh trừ điểm oan khi khách hàng dùng ngôn ngữ ngắn gọn của nhà đầu tư sành sỏi.

### 4.3. Data Drift & Xu hướng thị trường thay đổi
- Mức giá 2 tỷ ở thời điểm sốt đất có thể là phân khúc thấp, nhưng ở giai đoạn trầm lắng có thể là dòng tiền sẵn sàng giao dịch cao. Bộ tiêu chí cần được Audit định kỳ mỗi Quý.

### 4.4. Bảo mật dữ liệu cá nhân (PII & Quy tắc Workspace)
- **Tuyệt đối tuân thủ Quy tắc 5:** Không chia sẻ số điện thoại thật, thông tin định danh của khách hàng ra môi trường công cộng ngoài Workspace. Dữ liệu bàn giao phải được mã hóa hoặc phân quyền đúng Sales phụ trách.

### 4.5. Cơ chế Kiểm soát con người (Human-in-the-loop)
- Với các Lead ở vùng ranh giới (*Borderline Leads: 30 - 40 điểm*), cần có bước Review nhanh từ Điều phối viên Lead trước khi quyết định loại bỏ hoặc chuyển Sales.

---

## 5. Giao Thức Bàn Giao Kết Quả Cho Sales (Handover Protocol)

> 📖 *Xem đầy đủ quy chuẩn bàn giao tại [references/handover-protocol.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/references/handover-protocol.md) và mẫu thông báo tại [resources/lead-card-template.md](file:///d:/my-workspace-20260906T133958Z-1-001/my-workspace/.agents/skills/chamdiem-scoring/resources/lead-card-template.md).*

### 5.1. Kênh bàn giao đa tầng:
1. **Thông báo khẩn (Lead HOT 🔥):** Đẩy thông báo tức thì qua Webhook vào Group Zalo / Telegram nội bộ của Team VIP Sales với đầy đủ thông tin: *Họ tên, SĐT, Điểm số, Nhu cầu tóm tắt, Kịch bản mở đầu*.
2. **Đồng bộ bảng dữ liệu (Lead WARM ⛅):** Tự động ghi nhận vào Google Sheet / CRM với cột điểm số và nhãn phân loại để Sales trực ca bốc máy liên hệ.
3. **Phân phối công bằng (Round-Robin):** Tự động chia đều Lead cho các Sales đủ tiêu chuẩn phục vụ phân khúc tương ứng.

### 5.2. Mẫu Thẻ Lead Bàn Giao Nhanh (Lead Card Example):
```text
🚨 [HOT LEAD ALERT - BĐS] 🚨
👤 Khách hàng: Trần Hoàng Dũng | ID: #28 | SĐT: 0943392982
⭐ Điểm: 100/100 (HẠNG HOT 🔥) | SLA: < 15 PHÚT
📋 Nhu cầu: Chủ DN tìm quỹ đất công nghiệp / sàn VP >2000m2 khu Đông. Tài chính cực mạnh, pháp lý chuẩn 100%.
🎯 Gợi ý mở đầu: "Chào anh Dũng, em phụ trách quỹ đất công nghiệp khu Đông, em gửi anh hồ sơ quy hoạch và pháp lý 100% để anh xem trước..."
👉 Điều phối: Phụ trách Khối Khách hàng Doanh nghiệp
```

---

## 6. Hướng Dẫn Thực Thi Tự Động Hóa (Automation Runbook)

### 6.1. Chạy chấm điểm tự động qua Script Python:
```powershell
python .agents/skills/chamdiem-scoring/scripts/score_leads.py sample-data/khach_hang_bds_sample.csv outputs/reports/scored_leads.csv outputs/reports/scored_leads.json
```

### 6.2. Chấm điểm trực tiếp từ Google Sheets:
1. Xuất file từ Google Sheets dạng CSV URL: `https://docs.google.com/spreadsheets/d/17odkUsLWSnrnOebV0LzPCP5ZWz3mm-yR09ZFjslwh1w/gviz/tq?tqx=out:csv&gid=1542775777`
2. Đọc và phân tích trực tiếp qua Agent hoặc lưu vào `sample-data/` để tiến hành chấm điểm hàng loạt.
3. Kết xuất báo cáo phân loại lưu vào thư mục chuẩn `outputs/reports/` theo Quy tắc 4 của Workspace.
