@echo off
chcp 65001 >nul
title DEMO THUYET TRINH CAPSTONE - AGENTIC AI HOADON GDT
color 1F

echo ===============================================================================
echo   HOC VIEN: HOANG LAM - CAPSTONE PROJECT AGENTIC AI WITH GOOGLE ANTIGRAVITY
echo   DE TAI: HE THONG TU DONG HOA TIM KIEM, SAP XEP, TAI VA KIEM SOAT HOA DON
echo ===============================================================================
echo.
echo [*] Kiem tra moi truong thuc thi Python...
python --version
if errorlevel 1 (
    echo [!] Khong tim thay Python. Vui long cai dat hoac kiem tra PATH.
    pause
    exit /b
)

echo.
echo [*] San sang kich hoat Live Demo Workflow End-to-End!
echo [*] Nhan phim bat ky de bat dau chay Demo truoc Hoi dong...
echo.
pause

cls
echo ===============================================================================
echo                     DANG KHOI CHAY LIVE DEMO MULTI-AGENT PIPELINE
echo ===============================================================================
echo.

python .agents/workflows/run_end_to_end_pipeline.py

echo.
echo ===============================================================================
echo [V] LIVE DEMO HOAN TAT THANH CONG 100%!
echo [*] Toan bo hoa don PDF da duoc ket xuat vao: outputs/HoaDon_LuuTru/
echo [*] Bao cao tong hop doi soat tai: outputs/reports/bao_cao_ket_qua_workflow_end_to_end.md
echo ===============================================================================
echo.
pause
