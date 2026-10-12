@echo off
chcp 65001 >nul
title KHOI DONG CHROME TRA CUU HOA DON TU DONG
color 1F

echo ================================================================
echo        CONG CU HO TRO TRA CUU HOA DON DIEN TU TU DONG
echo ================================================================
echo.
echo [*] Dang tao thu muc du lieu tam: C:\ChromeDebug...
if not exist "C:\ChromeDebug" mkdir "C:\ChromeDebug"

echo [*] Dang tim kiem trinh duyet Google Chrome tren may cua ban...

set CHROME_PATH=""

if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    set CHROME_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
) else if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    set CHROME_PATH="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
) else if exist "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" (
    set CHROME_PATH="%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
)

if %CHROME_PATH%=="" (
    echo [!] Khong tim thay Google Chrome tai cac duong dan mac dinh.
    echo [*] Thu khoi dong bang lenh chrome...
    start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug" "https://hoadondientu.gdt.gov.vn"
) else (
    echo [V] Da tim thay Chrome tai: %CHROME_PATH%
    echo [*] Dang khoi dong Chrome voi che do Tu dong hoa...
    start "" %CHROME_PATH% --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug" "https://hoadondientu.gdt.gov.vn"
)

echo.
echo ================================================================
echo   CHROME DA DUOC MO THANH CONG!
echo.
echo   CAC BUOC TIEP THEO TREN CUA SO CHROME VUA MO:
echo   1. Dang nhap tai khoan va nhap ma CAPTCHA nhu binh thuong.
echo   2. Vao muc: Tra cuu -> Tra cuu hoa don -> Hoa don mua vao.
echo   3. Quay lai phan mem chat va bao: "Toi da dang nhap xong".
echo ================================================================
echo.
pause
