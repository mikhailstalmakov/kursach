

import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ooptrainer.menu_window import MenuWindow
import tkinter as tk


def main():
    """Точка входа в приложение"""
    root = tk.Tk()
    
    # Установка иконки приложения
    try:
        # Пробуем загрузить иконку из файла
        import os
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
        else:
            # Если файла нет, используем стандартную иконку Windows
            # На Windows можно использовать встроенную иконку
            root.iconbitmap(default='')
    except Exception as e:
        # Если не получилось, продолжаем без иконки
        pass
    
    app = MenuWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()

