# 🧠 HỆ THỐNG BỘ NHỚ AGENTIC (AGENTIC MEMORY SYSTEM)

> **Dự án:** Tìm kiếm, sắp xếp và tải hóa đơn điện tử còn thiếu  
> **Kiến trúc:** 2-Tier Memory Architecture (Short-term Working Memory & Long-term Persistent Memory)

---

## 1. CẤU TRÚC 2 TẦNG BỘ NHỚ

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        AGENTIC MEMORY ARCHITECTURE                     │
│                                                                        │
│  [ TẦNG 1: SHORT-TERM MEMORY (Bộ nhớ làm việc) ]                       │
│  • File: sample-data/manifests/invoices_manifest.json                  │
│  • Chức năng: Lưu trữ danh sách hóa đơn đang xử lý trong phiên         │
│  • Vòng đời: Khởi tạo khi nạp file CSV/Excel -> Hủy khi hoàn tất batch  │
│                                                                        │
│  [ TẦNG 2: LONG-TERM MEMORY (Bộ nhớ dài hạn) ]                         │
│  • File: memory/vendor_cache.json & outputs/storage_catalog.json       │
│  • Chức năng: Ghi nhớ các nhà cung cấp tin cậy, MST Blacklist đã chặn, │
│               các kỳ đã tra cứu thành công, và quyết định của Kế toán  │
│  • Vòng đời: Lưu trữ vĩnh viễn, tích lũy liên tục qua các kỳ kê khai   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. QUY CHUẨN VẬN HÀNH BỘ NHỚ (MEMORY PROTOCOLS)

1. **Smart Skip (Bỏ qua tra cứu thừa):**
   Trước khi kết nối Cổng GDT, Agent đọc `memory/vendor_cache.json` và `outputs/storage_catalog.json`. Nếu một hóa đơn đã được lưu trữ trong kho và nội dung không đổi $\rightarrow$ Agent tự động bỏ qua (Skip) ngay trong $0.1$ giây.
2. **Auto-Blacklist Blocking (Bộ nhớ ngăn chặn rủi ro):**
   Khi một MST đã bị Kế toán trưởng REJECT tại Human Checkpoint, Agent tự động ghi vào `blocked_vendors_cache` để tự động cảnh báo ở các kỳ tra cứu tiếp theo.
3. **Audit Trail Synchronization:**
   Mọi thay đổi cấu trúc bộ nhớ đều được đồng bộ vào `docs/pdca-log.md` theo Quy tắc 2 của Workspace.
