# tests/test_log.py
import unittest
from parameterized import parameterized
from app.main import Calculator, InvalidInputException

class TestCalculatorLog(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @parameterized.expand([
        # Тест нормального использования
        (10, 2, 2.302585092994241),
        (1, 3, 0),
        (2, 2, 1),

        # Тест неправильных типов входных данных
        ('a', 2, TypeError),
        (2, 'b', TypeError),

        # Тест неправильных значений входных данных
        (0, 2, InvalidInputException),
        (1, 0, InvalidInputException),
        (1, 1, InvalidInputException),
        (-1, 2, InvalidInputException),
    ])
    def test_log(self, a, base, expected_result, func_name='log'):
        if isinstance(expected_result, type) and issubclass(expected_result, BaseException):
            with self.assertRaises(expected_result):
                getattr(self.calc, func_name)(a, base)
        else:
            actual_result = getattr(self.calc, func_name)(a, base)
            self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()