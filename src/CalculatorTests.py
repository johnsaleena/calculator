import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(6, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(6, 2), 12)
        self.assertEqual(calculator.result, 12)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertEqual(calculator.result, 3)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(3), 9)
        self.assertEqual(calculator.result, 9)

    def test_square_rt_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square_rt(16), 4)
        self.assertEqual(calculator.result, 4)

if __name__ == '__main__':
    unittest.main()
