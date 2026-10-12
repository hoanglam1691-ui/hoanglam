function extractInvoiceData() {
    const modal = document.querySelector('.ant-modal-body') || document.querySelector('.ant-modal-content');
    if (!modal) return null;
    
    const text = modal.innerText;
    
    const knownLabels = [
        'Mẫu số', 'Ký hiệu:', 'Số:', 'HOÁ ĐƠN', 'HÓA ĐƠN', 'Ngày', 'tháng', 'năm', 'MCCQT:',
        'Tên người bán:', 'Mã số thuế:', 'Mã cửa hàng:', 'Tên cửa hàng:', 'Địa chỉ:', 'Điện thoại:', 'Số tài khoản:',
        'Tên người mua:', 'Họ tên người mua hàng:', 'Mã ĐVCQHVNSNN:', 'CCCD người mua:', 'Số hộ chiếu:',
        'Hình thức thanh toán:', 'Đơn vị tiền tệ:', 'Số bảng kê:', 'Ngày bảng kê:', 'STT', 'Tính chất',
        'Thuế suất', 'Tổng tiền', 'Ký bởi:', 'Ký ngày:'
    ];
    
    const cleanVal = function(val) {
        if (!val) return '';
        val = val.trim();
        for (let i = 0; i < knownLabels.length; i++) {
            const kl = knownLabels[i];
            if (val === kl) return '';
            if (kl !== 'HOÁ ĐƠN' && kl !== 'HÓA ĐƠN' && val.startsWith(kl)) {
                return '';
            }
        }
        return val;
    };
    
    const getMatch = function(re, defVal) {
        if (defVal === undefined) defVal = '';
        const m = text.match(re);
        if (!m) return defVal;
        const val = cleanVal(m[1]);
        return val ? val : defVal;
    };
    
    const mauSo = getMatch(/Mẫu số\s*([0-9A-Za-z]+)/i, '1');
    const kyHieu = getMatch(/Ký hiệu:\s*([0-9A-Za-z]+)/i, '');
    const soHd = getMatch(/Số:\s*([0-9]+)/i, '');
    const title = getMatch(/(HOÁ ĐƠN [^\n\r]+|HÓA ĐƠN [^\n\r]+)/i, 'HOÁ ĐƠN GIÁ TRỊ GIA TĂNG');
    
    const ngayMatch = text.match(/Ngày\s*(\d{1,2})\s*tháng\s*(\d{1,2})\s*năm\s*(\d{4})/i);
    const ngay = ngayMatch ? ngayMatch[1].padStart(2, '0') : '01';
    const thang = ngayMatch ? ngayMatch[2].padStart(2, '0') : '07';
    const nam = ngayMatch ? ngayMatch[3] : '2026';
    
    const mccqt = getMatch(/MCCQT:\s*([0-9A-Za-z-]+)/i, '');
    
    // Split text sections for Seller & Buyer
    const sellerPart = text.includes('Tên người mua:') ? text.split('Tên người mua:')[0] : text;
    const buyerPart = text.includes('Tên người mua:') ? ('Tên người mua:' + text.split('Tên người mua:')[1]) : text;
    
    const getPartMatch = function(src, re, defVal) {
        if (defVal === undefined) defVal = '';
        const m = src.match(re);
        if (!m) return defVal;
        const val = cleanVal(m[1]);
        return val ? val : defVal;
    };
    
    const sellerName = getPartMatch(sellerPart, /Tên người bán:\s*([^\n\r]+)/i, '');
    const sellerMst = getPartMatch(sellerPart, /Mã số thuế:\s*([0-9A-Za-z-]+)/i, '');
    const sellerStoreCode = getPartMatch(sellerPart, /Mã cửa hàng:\s*([^\n\r]+)/i, '');
    const sellerStoreName = getPartMatch(sellerPart, /Tên cửa hàng:\s*([^\n\r]+)/i, '');
    const sellerAddress = getPartMatch(sellerPart, /Địa chỉ:\s*([^\n\r]+)/i, '');
    const sellerPhone = getPartMatch(sellerPart, /Điện thoại:\s*([0-9\s.-]+)/i, '');
    const sellerBank = getPartMatch(sellerPart, /Số tài khoản:\s*([^\n\r]+)/i, '');
    
    const buyerName = getPartMatch(buyerPart, /Tên người mua:\s*([^\n\r]+)/i, '');
    const buyerContact = getPartMatch(buyerPart, /Họ tên người mua hàng:\s*([^\n\r]+)/i, '');
    const buyerMst = getPartMatch(buyerPart, /Mã số thuế:\s*([0-9A-Za-z-]+)/i, '');
    const buyerBudgetCode = getPartMatch(buyerPart, /Mã ĐVCQHVNSNN:\s*([^\n\r]+)/i, '');
    const buyerCccd = getPartMatch(buyerPart, /Căn cước công dân:\s*([^\n\r]+)|CCCD người mua:\s*([^\n\r]+)/i, '');
    const buyerPassport = getPartMatch(buyerPart, /Số hộ chiếu:\s*([^\n\r]+)/i, '');
    const buyerAddress = getPartMatch(buyerPart, /Địa chỉ:\s*([^\n\r]+)/i, '');
    const paymentMethod = getPartMatch(buyerPart, /Hình thức thanh toán:\s*([^\n\r]+)/i, 'TM/CK');
    const buyerBankAcc = getPartMatch(buyerPart, /Số tài khoản:\s*([^\n\r]+)/i, '');
    let currency = getPartMatch(buyerPart, /Đơn vị tiền tệ:\s*([^\n\r]+)/i, 'VND');
    if (currency.includes('Tỷ giá')) currency = 'VND';
    const bangKeSo = getPartMatch(buyerPart, /Số bảng kê:\s*([^\n\r]+)/i, '');
    const bangKeNgay = getPartMatch(buyerPart, /Ngày bảng kê:\s*([^\n\r]+)/i, '');
    
    const tables = Array.from(modal.querySelectorAll('table'));
    const items = [];
    if (tables.length > 0) {
        const itemTrs = Array.from(tables[0].querySelectorAll('tbody tr'));
        itemTrs.forEach(function(tr) {
            const tds = Array.from(tr.querySelectorAll('td')).map(function(td) { return td.innerText.trim(); });
            if (tds.length === 9) {
                // Hóa đơn bán hàng / Máy tính tiền (Không có cột thuế suất)
                items.push({
                    stt: tds[0] || '',
                    tinh_chat: tds[1] || 'Hàng hóa, dịch vụ',
                    loai_hang: tds[2] || '',
                    ten_hang: tds[3] || '',
                    dvt: tds[4] || '',
                    so_luong: tds[5] || '',
                    don_gia: tds[6] || '',
                    chiet_khau: tds[7] || '',
                    thue_suat: '',
                    thanh_tien: tds[8] || ''
                });
            } else if (tds.length >= 10) {
                // Hóa đơn GTGT chuẩn (Có cột thuế suất)
                items.push({
                    stt: tds[0] || '',
                    tinh_chat: tds[1] || 'Hàng hóa, dịch vụ',
                    loai_hang: tds[2] || '',
                    ten_hang: tds[3] || '',
                    dvt: tds[4] || '',
                    so_luong: tds[5] || '',
                    don_gia: tds[6] || '',
                    chiet_khau: tds[7] || '',
                    thue_suat: tds[8] || '',
                    thanh_tien: tds[9] || ''
                });
            }
        });
    }
    
    let thueSuatSummary = '';
    let tongChuaThueSummary = '';
    let tongTienThueSummary = '';
    
    // Parse Tax Breakdown Table
    for (let t = 1; t < tables.length; t++) {
        const trs = Array.from(tables[t].querySelectorAll('tr'));
        trs.forEach(function(tr) {
            const tds = Array.from(tr.querySelectorAll('td')).map(function(td) { return td.innerText.trim(); });
            if (tds.length === 3 && (tds[0].includes('%') || tds[0].includes('KCT') || tds[0].includes('0%') || tds[0].includes('5%') || tds[0].includes('8%') || tds[0].includes('10%'))) {
                thueSuatSummary = tds[0];
                tongChuaThueSummary = tds[1];
                tongTienThueSummary = tds[2];
            }
        });
    }
    
    // Grand Summary
    let tongChuaThue = tongChuaThueSummary;
    let tongTienThue = tongTienThueSummary;
    let tongPhi = '';
    let tongChietKhau = '';
    let tongThanhToan = '';
    let tongTienChu = '';
    
    for (let t = 1; t < tables.length; t++) {
        const trs = Array.from(tables[t].querySelectorAll('tr'));
        trs.forEach(function(tr) {
            const tds = Array.from(tr.querySelectorAll('td')).map(function(td) { return td.innerText.trim(); });
            if (tds.length >= 2) {
                const lbl = tds[0].toLowerCase();
                const val = tds[tds.length - 1];
                if (lbl.includes('chưa thuế') || lbl.includes('chưa có thuế')) {
                    if (val && !lbl.includes('thuế suất')) tongChuaThue = val;
                } else if (lbl.includes('tiền thuế') || lbl.includes('cộng tiền thuế')) {
                    if (val && !lbl.includes('thuế suất')) tongTienThue = val;
                } else if (lbl.includes('tiền phí')) {
                    tongPhi = val;
                } else if (lbl.includes('chiết khấu')) {
                    tongChietKhau = val;
                } else if (lbl.includes('bằng số')) {
                    tongThanhToan = val;
                } else if (lbl.includes('bằng chữ')) {
                    tongTienChu = val;
                }
            }
        });
    }

    // Direct text fallback for summary fields (especially on MTT / Bán Hàng)
    if (!tongThanhToan) {
        const ttMatch = text.match(/Tổng tiền thanh toán bằng số\s*([0-9.,]+)/i) || text.match(/Tổng tiền thanh toán[:\s]*([0-9.,]+)/i);
        if (ttMatch) tongThanhToan = ttMatch[1].trim();
    }
    if (!tongTienChu) {
        const tcMatch = text.match(/Tổng tiền thanh toán bằng chữ\s*([^\n\r]+)/i) || text.match(/Số tiền viết bằng chữ[:\s]*([^\n\r]+)/i);
        if (tcMatch) tongTienChu = cleanVal(tcMatch[1]);
    }
    if (!tongChietKhau) {
        const ckMatch = text.match(/Tổng tiền chiết khấu thương mại\s*([0-9.,]+)/i);
        if (ckMatch) tongChietKhau = ckMatch[1].trim();
    }
    if (!tongChuaThue && tongThanhToan) {
        tongChuaThue = tongThanhToan;
        if (!tongTienThue) tongTienThue = '0';
    }
    
    // Fallback: If summary values are missing, calculate accurately from items
    let calcChuaThue = 0;
    let calcThue = 0;
    let primaryThueSuat = '10%';
    
    items.forEach(function(it) {
        const rawTT = (it.thanh_tien || '').replace(/\./g, '').replace(/,/g, '').trim();
        const numTT = parseFloat(rawTT) || 0;
        calcChuaThue += numTT;
        
        let pct = 10;
        if (it.thue_suat) {
            primaryThueSuat = it.thue_suat;
            const matchPct = it.thue_suat.match(/(\d+)/);
            if (matchPct) pct = parseFloat(matchPct[1]);
        }
        calcThue += Math.round(numTT * (pct / 100));
    });
    
    const formatVND = function(num) {
        return Math.round(num).toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    };
    
    if (!thueSuatSummary) thueSuatSummary = primaryThueSuat;
    if (!tongChuaThue && calcChuaThue > 0) tongChuaThue = formatVND(calcChuaThue);
    if (!tongTienThue && calcThue > 0) tongTienThue = formatVND(calcThue);
    if (!tongThanhToan && calcChuaThue > 0) tongThanhToan = formatVND(calcChuaThue + calcThue);
    
    const signMatch = text.match(/Ký bởi:\s*([^\n\r]+)/i);
    const signDateMatch = text.match(/Ký ngày:\s*([^\n\r]+)/i);
    const signer = signMatch ? cleanVal(signMatch[1]) : sellerName;
    const signDate = signDateMatch ? cleanVal(signDateMatch[1]) : (ngay + '/' + thang + '/' + nam + ' 10:00:00');
    
    // Trích xuất thông tin Hóa đơn điều chỉnh & Hóa đơn thay thế
    let refType = ''; // 'DIEU_CHINH' | 'THAY_THE' | ''
    let refInvoiceNote = '';
    let refMauSo = '';
    let refKyHieu = '';
    let refSoHd = '';
    let refNgayLap = '';
    let refLyDo = '';
    let refVanBan = '';

    // Tìm trong DOM các thẻ chứa text 'Điều chỉnh cho' hoặc 'Thay thế cho'
    const candidateNodes = Array.from(modal.querySelectorAll('.mg-bottom, div, p, span'));
    for (let i = 0; i < candidateNodes.length; i++) {
        const elTxt = candidateNodes[i].innerText ? candidateNodes[i].innerText.trim() : '';
        if (elTxt.toLowerCase().includes('điều chỉnh cho') || elTxt.toLowerCase().includes('thay thế cho')) {
            refInvoiceNote = elTxt;
            if (elTxt.toLowerCase().includes('điều chỉnh cho')) refType = 'DIEU_CHINH';
            else if (elTxt.toLowerCase().includes('thay thế cho')) refType = 'THAY_THE';
            break;
        }
    }

    if (!refInvoiceNote) {
        const refMatch = text.match(/((?:Điều chỉnh cho|Thay thế cho)\s*[^\n\r]+)/i);
        if (refMatch) {
            refInvoiceNote = refMatch[1].trim();
            if (refInvoiceNote.toLowerCase().includes('điều chỉnh cho')) refType = 'DIEU_CHINH';
            else if (refInvoiceNote.toLowerCase().includes('thay thế cho')) refType = 'THAY_THE';
        }
    }

    if (refInvoiceNote) {
        const cMatch = refInvoiceNote.match(/(?:Điều chỉnh cho|Thay thế cho)\s*ký hiệu mẫu số hóa đơn\s*([^,]+),\s*ký hiệu hóa đơn\s*([^,]+),\s*số hóa đơn\s*([^,]+),\s*ngày lập\s*([0-9/.-]+)/i)
            || refInvoiceNote.match(/(?:Điều chỉnh cho|Thay thế cho)\s*hóa đơn(?:\s*Mẫu số|\s*mẫu số)?\s*([^,]+)?.*?Ký hiệu[:\s]*([^,]+).*?Số[:\s]*([^,]+).*?ngày[:\s]*([0-9/.-]+)/i);
        if (cMatch) {
            refMauSo = cMatch[1] ? cMatch[1].trim() : '';
            refKyHieu = cMatch[2] ? cMatch[2].trim() : '';
            refSoHd = cMatch[3] ? cMatch[3].trim() : '';
            refNgayLap = cMatch[4] ? cMatch[4].trim() : '';
        }
    }

    const lyDoMatch = text.match(/Lý do(?:\s*điều chỉnh|\s*thay thế)?[:\s]*([^\n\r]+)/i);
    if (lyDoMatch) refLyDo = cleanVal(lyDoMatch[1]);

    const vbMatch = text.match(/(?:Văn bản thỏa thuận|Biên bản)(?:\s*số)?[:\s]*([^\n\r]+)/i);
    if (vbMatch) refVanBan = cleanVal(vbMatch[1]);

    if (!refType) {
        if (text.toLowerCase().includes('hóa đơn điều chỉnh') || text.toLowerCase().includes('hoá đơn điều chỉnh')) {
            refType = 'DIEU_CHINH';
        } else if (text.toLowerCase().includes('hóa đơn thay thế') || text.toLowerCase().includes('hoá đơn thay thế')) {
            refType = 'THAY_THE';
        }
    }

    return {
        mau_so: mauSo,
        ky_hieu: kyHieu,
        so_hd: soHd,
        title: title,
        ngay: ngay,
        thang: thang,
        nam: nam,
        mccqt: mccqt,
        seller_name: sellerName,
        seller_mst: sellerMst,
        seller_store_code: sellerStoreCode,
        seller_store_name: sellerStoreName,
        seller_address: sellerAddress,
        seller_phone: sellerPhone,
        seller_bank_acc: sellerBank,
        buyer_name: buyerName,
        buyer_contact: buyerContact,
        buyer_mst: buyerMst,
        buyer_budget_code: buyerBudgetCode,
        buyer_cccd: buyerCccd,
        buyer_passport: buyerPassport,
        buyer_address: buyerAddress,
        payment_method: paymentMethod,
        buyer_bank_acc: buyerBankAcc,
        currency: currency,
        bang_ke_so: bangKeSo,
        bang_ke_ngay: bangKeNgay,
        items: items,
        thue_suat: thueSuatSummary,
        tien_chua_thue: tongChuaThue,
        tien_thue: tongTienThue,
        tong_tien_phi: tongPhi,
        tong_chiet_khau: tongChietKhau,
        tong_thanh_toan: tongThanhToan,
        tien_chu: tongTienChu,
        sign_date: signDate,
        ref_type: refType,
        ref_invoice_note: refInvoiceNote,
        ref_mau_so: refMauSo,
        ref_ky_hieu: refKyHieu,
        ref_so_hd: refSoHd,
        ref_ngay_lap: refNgayLap,
        ref_ly_do: refLyDo,
        ref_van_ban: refVanBan
    };
}
