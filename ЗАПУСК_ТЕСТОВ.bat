@echo off
chcp 65001 >nul
echo ========================================
echo ЗАПУСК АВТОМАТИЗИРОВАННОГО ТЕСТИРОВАНИЯ
echo ========================================
echo.

python test_app.py 2>nul
if %errorlevel% equ 0 goto :end

py test_app.py 2>nul
if %errorlevel% equ 0 goto :end

python3 test_app.py 2>nul
if %errorlevel% equ 0 goto :end

where python >nul 2>&1
if %errorlevel% equ 0 (
    python test_app.py
    goto :end
)

where py >nul 2>&1
if %errorlevel% equ 0 (
    py test_app.py
    goto :end
)

echo ❌ Python не найден!
echo Попробуйте запустить вручную: python test_app.py
echo Или установите Python с https://www.python.org/
pause
exit /b 1

:end
echo.
echo ========================================
pause


