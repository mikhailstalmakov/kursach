"""
Окно тестирования по ООП
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
from ooptrainer.question import Question


class QuizWindow:
    """Класс окна тестирования"""
    
    def __init__(self, window, parent):
        """
        Инициализация окна теста
        
        Args:
            window: Окно теста
            parent: Родительское окно (главное меню)
        """
        self.window = window
        self.parent = parent
        self.window.title("Тест по ООП")
        self.window.geometry("700x600")
        self.window.resizable(True, True)  # Разрешаем изменение размера
        self.window.minsize(600, 500)  # Минимальный размер окна
        
        # Центрирование окна
        self._center_window()
        
        # Инициализация данных теста
        self.current_question_index = 0
        self.score = 0
        self.questions = self._load_questions()
        random.shuffle(self.questions)  # Перемешиваем вопросы случайным образом
        self.selected_answer = None
        
        # Создание интерфейса
        self._create_widgets()
        
        # Показ первого вопроса
        self._show_question()
        
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
    
    def _load_questions(self):
        """Загрузка вопросов теста"""
        return [
            Question(
                "Что такое класс в ООП?",
                [
                    "Конкретный объект в памяти",
                    "Шаблон (описание) для создания объектов",
                    "Функция без параметров",
                    "Модуль сборки проекта"
                ],
                1,
                "Класс - это шаблон или описание для создания объектов. Он определяет свойства и методы, которые будут у всех объектов этого класса."
            ),
            Question(
                "Какой принцип ООП отвечает за сокрытие внутренней реализации?",
                [
                    "Наследование",
                    "Полиморфизм",
                    "Инкапсуляция",
                    "Абстракция"
                ],
                2,
                "Инкапсуляция - это принцип ООП, который позволяет скрыть внутреннюю реализацию объекта и предоставить доступ только через публичные методы."
            ),
            Question(
                "Что такое наследование в ООП?",
                [
                    "Создание копии класса",
                    "Механизм создания новых классов на основе существующих",
                    "Объединение нескольких классов в один",
                    "Удаление методов из класса"
                ],
                1,
                "Наследование позволяет создавать новые классы на основе существующих, расширяя и модифицируя их функциональность."
            ),
            Question(
                "Что такое полиморфизм?",
                [
                    "Способность объектов разных классов иметь единый интерфейс",
                    "Создание множества одинаковых объектов",
                    "Хранение данных в разных форматах",
                    "Использование одного имени для разных переменных"
                ],
                0,
                "Полиморфизм - это способность объектов разных классов иметь единый интерфейс и по-разному реализовывать общее поведение."
            ),
            Question(
                "Что такое объект в ООП?",
                [
                    "Тип данных",
                    "Конкретный экземпляр класса",
                    "Функция класса",
                    "Переменная класса"
                ],
                1,
                "Объект - это конкретный экземпляр класса, обладающий состоянием (данные) и поведением (методы)."
            ),
            Question(
                "Что означает принцип инкапсуляции?",
                [
                    "Объединение данных и методов в одном классе",
                    "Разделение данных и методов",
                    "Создание публичных переменных",
                    "Удаление приватных методов"
                ],
                0,
                "Инкапсуляция означает объединение данных (полей) и методов (функций) в одном классе, а также контроль доступа к ним."
            ),
            Question(
                "Что такое абстрактный класс?",
                [
                    "Класс без методов",
                    "Класс, который нельзя наследовать",
                    "Класс, который содержит абстрактные методы и не может быть инстанцирован напрямую",
                    "Класс только с данными"
                ],
                2,
                "Абстрактный класс содержит абстрактные методы (без реализации) и служит основой для других классов. Его нельзя использовать для создания объектов напрямую."
            ),
            Question(
                "Что такое интерфейс в ООП?",
                [
                    "Графический интерфейс пользователя",
                    "Контракт, определяющий методы, которые должен реализовать класс",
                    "Внутренняя структура класса",
                    "Способ доступа к данным"
                ],
                1,
                "Интерфейс - это контракт, который определяет набор методов, которые класс должен реализовать, не определяя их реализацию."
            )
        ]
    
    def _create_widgets(self):
        """Создание виджетов окна теста"""
        # Фрейм для вопроса
        question_frame = tk.Frame(self.window, padx=20, pady=20)
        question_frame.pack(fill=tk.BOTH, expand=True)
        
        # Номер вопроса и прогресс
        self.progress_label = tk.Label(
            question_frame,
            text="",
            font=("Arial", 10),
            fg="gray"
        )
        self.progress_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Текст вопроса
        self.question_label = tk.Label(
            question_frame,
            text="",
            font=("Arial", 14, "bold"),
            wraplength=650,
            justify=tk.LEFT,
            anchor=tk.W
        )
        self.question_label.pack(anchor=tk.W, pady=20)
        
        # Фрейм для вариантов ответов
        self.answers_frame = tk.Frame(question_frame)
        self.answers_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Переменная для выбранного ответа
        self.answer_var = tk.IntVar(value=-1)
        
        # Кнопка "Ответить"
        self.submit_button = tk.Button(
            question_frame,
            text="Ответить",
            font=("Arial", 12),
            width=15,
            height=2,
            command=self._check_answer,
            bg="#4CAF50",
            fg="white",
            cursor="hand2",
            state=tk.DISABLED
        )
        self.submit_button.pack(pady=20)
        
        # Кнопка "Назад в меню"
        back_button = tk.Button(
            question_frame,
            text="Назад в меню",
            font=("Arial", 10),
            command=self._on_close,
            bg="#9E9E9E",
            fg="white",
            cursor="hand2"
        )
        back_button.pack(pady=10)
    
    def _show_question(self):
        """Отображение текущего вопроса"""
        if self.current_question_index >= len(self.questions):
            self._show_results()
            return
        
        question = self.questions[self.current_question_index]
        
        # Обновление прогресса
        self.progress_label.config(
            text=f"Вопрос {self.current_question_index + 1} из {len(self.questions)}"
        )
        
        # Обновление текста вопроса
        self.question_label.config(text=question.text)
        
        # Очистка предыдущих вариантов ответов
        for widget in self.answers_frame.winfo_children():
            widget.destroy()
        
        # Создание радиокнопок для вариантов ответов
        self.answer_var.set(-1)
        for i, option in enumerate(question.options):
            radio = tk.Radiobutton(
                self.answers_frame,
                text=option,
                variable=self.answer_var,
                value=i,
                font=("Arial", 11),
                anchor=tk.W,
                cursor="hand2",
                command=self._on_answer_selected
            )
            radio.pack(fill=tk.X, pady=5, padx=20)
        
        # Сброс состояния кнопки
        self.submit_button.config(state=tk.DISABLED)
    
    def _on_answer_selected(self):
        """Обработка выбора ответа"""
        self.submit_button.config(state=tk.NORMAL)
    
    def _check_answer(self):
        """Проверка ответа пользователя"""
        selected_index = self.answer_var.get()
        
        if selected_index == -1:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите ответ!")
            return
        
        question = self.questions[self.current_question_index]
        
        if question.check_answer(selected_index):
            self.score += 1
            messagebox.showinfo("Правильно!", f"Верно!\n\n{question.explanation}")
        else:
            messagebox.showerror(
                "Неправильно",
                f"Неверно. Правильный ответ: {question.options[question.correct_index]}\n\n{question.explanation}"
            )
        
        # Переход к следующему вопросу
        self.current_question_index += 1
        self._show_question()
    
    def _show_results(self):
        """Отображение результатов теста"""
        # Очистка окна
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Результаты
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100
        
        result_frame = tk.Frame(self.window, padx=20, pady=20)
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        # Заголовок
        title_label = tk.Label(
            result_frame,
            text="Тест завершён!",
            font=("Arial", 20, "bold"),
            pady=30
        )
        title_label.pack()
        
        # Результаты
        result_text = f"Правильных ответов: {self.score} из {total_questions}\n"
        result_text += f"Процент правильных ответов: {percentage:.1f}%"
        
        result_label = tk.Label(
            result_frame,
            text=result_text,
            font=("Arial", 14),
            pady=20
        )
        result_label.pack()
        
        # Оценка
        if percentage >= 90:
            grade = "Отлично!"
            color = "#4CAF50"
        elif percentage >= 70:
            grade = "Хорошо!"
            color = "#2196F3"
        elif percentage >= 50:
            grade = "Удовлетворительно"
            color = "#FF9800"
        else:
            grade = "Нужно повторить материал"
            color = "#f44336"
        
        grade_label = tk.Label(
            result_frame,
            text=grade,
            font=("Arial", 16, "bold"),
            fg=color,
            pady=20
        )
        grade_label.pack()
        
        # Кнопки
        buttons_frame = tk.Frame(result_frame)
        buttons_frame.pack(pady=30)
        
        restart_button = tk.Button(
            buttons_frame,
            text="Пройти ещё раз",
            font=("Arial", 12),
            width=15,
            height=2,
            command=self._restart_quiz,
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        restart_button.pack(side=tk.LEFT, padx=10)
        
        menu_button = tk.Button(
            buttons_frame,
            text="В главное меню",
            font=("Arial", 12),
            width=15,
            height=2,
            command=self._on_close,
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        menu_button.pack(side=tk.LEFT, padx=10)
    
    def _restart_quiz(self):
        """Перезапуск теста"""
        self.current_question_index = 0
        self.score = 0
        self.selected_answer = None
        
        # Перемешиваем вопросы заново для нового прохождения
        self.questions = self._load_questions()
        random.shuffle(self.questions)
        
        # Очистка окна
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Воссоздание интерфейса
        self._create_widgets()
        self._show_question()
    
    def _on_close(self):
        """Обработка закрытия окна"""
        self.window.destroy()
        self.parent.deiconify()  # Показываем главное окно

