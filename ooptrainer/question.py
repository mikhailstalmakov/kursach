"""
Класс для представления вопроса теста
"""


class Question:
    """Класс вопроса с вариантами ответов"""
    
    def __init__(self, text, options, correct_index, explanation=""):
        """
        Инициализация вопроса
        
        Args:
            text: Текст вопроса
            options: Список вариантов ответов
            correct_index: Индекс правильного ответа
            explanation: Пояснение к правильному ответу
        """
        self.text = text
        self.options = options
        self.correct_index = correct_index
        self.explanation = explanation
    
    def check_answer(self, selected_index):
        """
        Проверка выбранного ответа
        
        Args:
            selected_index: Индекс выбранного ответа
            
        Returns:
            True, если ответ правильный, иначе False
        """
        return selected_index == self.correct_index

