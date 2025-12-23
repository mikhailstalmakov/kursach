@echo off
chcp 65001 >nul
echo ========================================
echo Установка зависимостей для тренажёра
echo ========================================
echo.

REM Пробуем найти Python разными способами
set PYTHON_CMD=

REM Вариант 1: python
python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
    goto :found
)

REM Вариант 2: py (Windows Python Launcher)
py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :found
)

REM Вариант 3: python3
python3 --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python3
    goto :found
)

REM Python не найден
echo ❌ Python не найден!
echo.
echo Попробуй установить Python с официального сайта:
echo https://www.python.org/downloads/
echo.
echo Или попробуй выполнить вручную:
echo py -m pip install pyinstaller
echo python -m pip install pyinstaller
echo python3 -m pip install pyinstaller
echo.
pause
exit /b 1

:found
echo ✅ Python найден:
%PYTHON_CMD% --version
echo.

echo Устанавливаю PyInstaller...
%PYTHON_CMD% -m pip install pyinstaller

if errorlevel 1 (
    echo.
    echo ❌ Ошибка установки!
    echo Попробуй выполнить вручную:
    echo %PYTHON_CMD% -m pip install pyinstaller
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Все зависимости установлены!
echo Теперь можно запустить build.bat для сборки exe
echo.
pause

