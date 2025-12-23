"""
Окно главного меню приложения
"""

import tkinter as tk
from tkinter import ttk, messagebox
from ooptrainer.quiz_window import QuizWindow
from ooptrainer.settings_window import SettingsWindow


class MenuWindow:
    """Класс главного меню тренажёра"""
    
    def __init__(self, root):
        """
        Инициализация главного окна меню
        
        Args:
            root: Корневое окно tkinter
        """
        self.root = root
        self.root.title("Тренажёр по ООП")
        self.root.geometry("600x500")
        self.root.resizable(True, True)  # Разрешаем изменение размера
        self.root.minsize(500, 400)  # Минимальный размер окна
        
        # Центрирование окна
        self._center_window()
        
        # Создание интерфейса
        self._create_widgets()
        
    def _center_window(self):
        """Центрирование окна на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def _create_widgets(self):
        """Создание виджетов главного меню"""
        # Заголовок
        title_label = tk.Label(
            self.root,
            text="Тренажёр по ООП",
            font=("Arial", 24, "bold"),
            pady=50
        )
        title_label.pack()
        
        # Подзаголовок
        subtitle_label = tk.Label(
            self.root,
            text="Графический учебный тренажёр по теории\nобъектно-ориентированного программирования",
            font=("Arial", 12),
            pady=20
        )
        subtitle_label.pack()
        
        # Кнопка "Начать тест"
        start_button = tk.Button(
            self.root,
            text="Начать тест",
            font=("Arial", 14),
            width=20,
            height=2,
            command=self._start_quiz,
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        start_button.pack(pady=15)
        
        # Кнопка "Настройки"
        settings_button = tk.Button(
            self.root,
            text="Настройки",
            font=("Arial", 14),
            width=20,
            height=2,
            command=self._open_settings,
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        settings_button.pack(pady=15)
        
        # Кнопка "Выход"
        exit_button = tk.Button(
            self.root,
            text="Выход",
            font=("Arial", 14),
            width=20,
            height=2,
            command=self._exit_app,
            bg="#f44336",
            fg="white",
            cursor="hand2"
        )
        exit_button.pack(pady=15)
        
        # Информация о версии
        version_label = tk.Label(
            self.root,
            text="Версия 1.0 | Стальмаков М. | ИКБО-31-24 | РТУ МИРЭА, 2025",
            font=("Arial", 8),
            fg="gray"
        )
        version_label.pack(side=tk.BOTTOM, pady=10)
    
    def _start_quiz(self):
        """Запуск окна тестирования"""
        self.root.withdraw()  # Скрываем главное окно
        quiz_window = tk.Toplevel(self.root)
        QuizWindow(quiz_window, self.root)
    
    def _open_settings(self):
        """Открытие окна настроек"""
        settings_window = tk.Toplevel(self.root)
        SettingsWindow(settings_window)
    
    def _exit_app(self):
        """Выход из приложения"""
        if tk.messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.quit()

