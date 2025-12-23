@echo off
chcp 65001 >nul
echo ========================================
echo Сборка exe файла тренажёра по ООП
echo ========================================
echo.

REM Пробуем найти Python разными способами
set PYTHON_CMD=

REM Вариант 1: python
python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
    goto :found_python
)

REM Вариант 2: py (Windows Python Launcher)
py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :found_python
)

REM Вариант 3: python3
python3 --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python3
    goto :found_python
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
echo.
pause
exit /b 1

:found_python
echo ✅ Python найден:
%PYTHON_CMD% --version
echo.

REM Проверка наличия PyInstaller
%PYTHON_CMD% -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo PyInstaller не установлен. Устанавливаю...
    echo.
    %PYTHON_CMD% -m pip install pyinstaller
    if errorlevel 1 (
        echo.
        echo ❌ Ошибка установки PyInstaller!
        echo Попробуй установить вручную:
        echo %PYTHON_CMD% -m pip install pyinstaller
        echo.
        pause
        exit /b 1
    )
    echo.
    echo ✅ PyInstaller установлен!
    echo.
) else (
    echo ✅ PyInstaller уже установлен
    echo.
)

echo Начинаю сборку exe файла БЕЗ консоли...
echo Это может занять несколько минут...
echo.

REM Проверяем наличие иконки
set ICON_PARAM=
if exist "icon.ico" (
    set ICON_PARAM=--icon=icon.ico
    echo ✅ Иконка найдена: icon.ico
    echo.
)

REM Используем spec файл для более точной настройки
if exist "OOPTrainer.spec" (
    %PYTHON_CMD% -m PyInstaller OOPTrainer.spec --clean
) else (
    REM Альтернативный способ через командную строку
    %PYTHON_CMD% -m PyInstaller --onefile --windowed --noconsole --name=OOPTrainer --add-data "ooptrainer;ooptrainer" --hidden-import=tkinter --hidden-import=tkinter.ttk --hidden-import=tkinter.messagebox %ICON_PARAM% --clean main.py
)

echo.
echo ========================================
if exist "dist\OOPTrainer.exe" (
    echo ✅ Сборка успешна!
    echo.
    echo exe файл находится в папке: dist\OOPTrainer.exe
    echo.
    echo Запускай его двойным кликом - консоль НЕ появится!
) else (
    echo ❌ Ошибка сборки. Проверьте сообщения выше.
    echo.
    echo Попробуй установить PyInstaller вручную:
    echo python -m pip install pyinstaller
)
echo ========================================
pause

