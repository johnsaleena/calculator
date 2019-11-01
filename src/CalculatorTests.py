import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(6, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(6, 2), 12)
        self.assertEqual(self.calculator.result, 12)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.result, 3)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_square_rt_method_calculator(self):
        self.assertEqual(self.calculator.square_rt(16), 4)
        self.assertEqual(self.calculator.result, 4)

if __name__ == '__main__':
    unittest.main()
