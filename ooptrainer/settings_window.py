"""
Окно настроек приложения
"""

import tkinter as tk
from tkinter import ttk, messagebox


class SettingsWindow:
    """Класс окна настроек"""
    
    def __init__(self, window):
        """
        Инициализация окна настроек
        
        Args:
            window: Окно настроек
        """
        self.window = window
        self.window.title("Настройки")
        self.window.geometry("500x400")
        self.window.resizable(True, True)  # Разрешаем изменение размера
        self.window.minsize(450, 350)  # Минимальный размер окна
        
        # Центрирование окна
        self._center_window()
        
        # Создание интерфейса
        self._create_widgets()
        
        # Обработка закрытия окна
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)
    
    def _center_window(self):
        """Центрирование окна на экране"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def _create_widgets(self):
        """Создание виджетов окна настроек"""
        # Заголовок
        title_label = tk.Label(
            self.window,
            text="Настройки",
            font=("Arial", 18, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Фрейм для настроек
        settings_frame = tk.Frame(self.window, padx=30, pady=20)
        settings_frame.pack(fill=tk.BOTH, expand=True)
        
        # Настройка темы
        theme_label = tk.Label(
            settings_frame,
            text="Тема оформления:",
            font=("Arial", 11),
            anchor=tk.W
        )
        theme_label.pack(fill=tk.X, pady=10)
        
        self.theme_var = tk.StringVar(value="Светлая")
        theme_frame = tk.Frame(settings_frame)
        theme_frame.pack(fill=tk.X, pady=5)
        
        light_radio = tk.Radiobutton(
            theme_frame,
            text="Светлая",
            variable=self.theme_var,
            value="Светлая",
            font=("Arial", 10)
        )
        light_radio.pack(side=tk.LEFT, padx=10)
        
        dark_radio = tk.Radiobutton(
            theme_frame,
            text="Тёмная",
            variable=self.theme_var,
            value="Тёмная",
            font=("Arial", 10)
        )
        dark_radio.pack(side=tk.LEFT, padx=10)
        
        # Разделитель
        separator = ttk.Separator(settings_frame, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=20)
        
        # Информация о программе
        info_label = tk.Label(
            settings_frame,
            text="О программе",
            font=("Arial", 12, "bold"),
            anchor=tk.W
        )
        info_label.pack(fill=tk.X, pady=10)
        
        info_text = tk.Text(
            settings_frame,
            height=8,
            width=40,
            wrap=tk.WORD,
            font=("Arial", 9),
            state=tk.DISABLED
        )
        info_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        info_content = """Графический учебный тренажёр по теории 
объектно-ориентированного программирования

Версия: 1.0
Разработчик: Стальмаков Михаил
Учебное заведение: РТУ МИРЭА
Группа: ИКБО-31-24

Дисциплина: Инструментальные средства разработки 
программного обеспечения с открытым исходным кодом

© 2025 РТУ МИРЭА"""
        
        info_text.config(state=tk.NORMAL)
        info_text.insert("1.0", info_content)
        info_text.config(state=tk.DISABLED)
        
        # Кнопка "Сохранить"
        save_button = tk.Button(
            settings_frame,
            text="Сохранить",
            font=("Arial", 11),
            width=15,
            command=self._save_settings,
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        save_button.pack(pady=20)
        
        # Кнопка "Закрыть"
        close_button = tk.Button(
            settings_frame,
            text="Закрыть",
            font=("Arial", 11),
            width=15,
            command=self._on_close,
            bg="#9E9E9E",
            fg="white",
            cursor="hand2"
        )
        close_button.pack(pady=5)
    
    def _save_settings(self):
        """Сохранение настроек"""
        theme = self.theme_var.get()
        messagebox.showinfo(
            "Настройки сохранены",
            f"Тема оформления установлена: {theme}\n\n"
            "Примечание: В текущей версии изменение темы не реализовано."
        )
    
    def _on_close(self):
        """Закрытие окна настроек"""
        self.window.destroy()

