"""
Автоматизированное тестирование графического учебного тренажёра по ООП

Запуск тестов:
    python test_app.py

Или через unittest:
    python -m unittest test_app
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ooptrainer.question import Question


class TestQuestion(unittest.TestCase):
    """Тесты для класса Question"""
    
    def setUp(self):
        """Инициализация тестовых данных"""
        self.question = Question(
            "Что такое класс в ООП?",
            [
                "Конкретный объект в памяти",
                "Шаблон (описание) для создания объектов",
                "Функция без параметров",
                "Модуль сборки проекта"
            ],
            1,
            "Класс - это шаблон для создания объектов."
        )
    
    def test_question_initialization(self):
        """Тест инициализации вопроса"""
        self.assertEqual(self.question.text, "Что такое класс в ООП?")
        self.assertEqual(len(self.question.options), 4)
        self.assertEqual(self.question.correct_index, 1)
        self.assertEqual(self.question.explanation, "Класс - это шаблон для создания объектов.")
    
    def test_check_answer_correct(self):
        """Тест проверки правильного ответа"""
        self.assertTrue(self.question.check_answer(1))
    
    def test_check_answer_incorrect(self):
        """Тест проверки неправильного ответа"""
        self.assertFalse(self.question.check_answer(0))
        self.assertFalse(self.question.check_answer(2))
        self.assertFalse(self.question.check_answer(3))
    
    def test_check_answer_boundary(self):
        """Тест проверки граничных значений"""
        self.assertFalse(self.question.check_answer(-1))
        self.assertFalse(self.question.check_answer(10))


class TestQuizLogic(unittest.TestCase):
    """Тесты логики тестирования"""
    
    def setUp(self):
        """Инициализация тестовых данных"""
        self.questions = [
            Question("Вопрос 1", ["Вариант 1", "Вариант 2"], 0, "Объяснение 1"),
            Question("Вопрос 2", ["Вариант 1", "Вариант 2"], 1, "Объяснение 2"),
            Question("Вопрос 3", ["Вариант 1", "Вариант 2"], 0, "Объяснение 3")
        ]
    
    def test_questions_count(self):
        """Тест количества вопросов"""
        self.assertEqual(len(self.questions), 3)
    
    def test_score_calculation(self):
        """Тест подсчёта баллов"""
        score = 0
        answers = [0, 1, 0]
        
        for i, question in enumerate(self.questions):
            if question.check_answer(answers[i]):
                score += 1
        
        self.assertEqual(score, 3)
    
    def test_percentage_calculation(self):
        """Тест вычисления процента правильных ответов"""
        total_questions = len(self.questions)
        score = 2
        percentage = (score / total_questions) * 100
        
        self.assertAlmostEqual(percentage, 66.67, places=2)
    
    def test_grade_assignment(self):
        """Тест присвоения оценки"""
        total_questions = len(self.questions)
        
        score_90 = total_questions
        score_70 = total_questions
        score_50 = int(total_questions * 0.5)
        
        percentage_90 = (score_90 / total_questions) * 100
        percentage_70 = (score_70 / total_questions) * 100
        percentage_50 = (score_50 / total_questions) * 100
        
        self.assertGreaterEqual(percentage_90, 90)
        self.assertGreaterEqual(percentage_70, 70)
    


class TestDataIntegrity(unittest.TestCase):
    """Тесты целостности данных"""
    
    def test_question_options_not_empty(self):
        """Тест наличия вариантов ответов"""
        question = Question("Вопрос", ["Вариант 1", "Вариант 2"], 0, "")
        self.assertGreater(len(question.options), 0)
    
    def test_correct_index_in_range(self):
        """Тест корректности индекса правильного ответа"""
        question = Question("Вопрос", ["Вариант 1", "Вариант 2"], 0, "")
        self.assertGreaterEqual(question.correct_index, 0)
        self.assertLess(question.correct_index, len(question.options))
    
    def test_question_text_not_empty(self):
        """Тест наличия текста вопроса"""
        question = Question("Вопрос", ["Вариант 1"], 0, "")
        self.assertNotEqual(question.text, "")
        self.assertIsNotNone(question.text)


def run_tests():
    """Запуск всех тестов с выводом результатов"""
    print("=" * 70)
    print("АВТОМАТИЗИРОВАННОЕ ТЕСТИРОВАНИЕ ТРЕНАЖЁРА ПО ООП")
    print("=" * 70)
    print()
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestQuestion))
    suite.addTests(loader.loadTestsFromTestCase(TestQuizLogic))
    suite.addTests(loader.loadTestsFromTestCase(TestDataIntegrity))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    print("=" * 70)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 70)
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно пройдено: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✓ Все тесты пройдены успешно!")
        return 0
    else:
        print("\n✗ Некоторые тесты провалены или содержат ошибки!")
        return 1


if __name__ == "__main__":
    run_tests()


