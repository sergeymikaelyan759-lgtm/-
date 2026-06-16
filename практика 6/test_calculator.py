import unittest
import math
from calculator import Calculator


class TestCalculatorBasicOperations(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def tearDown(self):
        self.calc.reset()
    
    # ADD TESTS
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5.0)
        self.assertEqual(self.calc.add(10, 20), 30.0)
    
    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5.0)
        self.assertEqual(self.calc.add(-10, -20), -30.0)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1.0)
        self.assertEqual(self.calc.add(2, -3), -1.0)
    
    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5.0)
        self.assertEqual(self.calc.add(5, 0), 5.0)
        self.assertEqual(self.calc.add(0, 0), 0.0)
    
    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertAlmostEqual(self.calc.add(-1.5, 2.5), 1.0)
    
    def test_add_none_values(self):
        with self.assertRaises(ValueError):
            self.calc.add(None, 5)
        with self.assertRaises(ValueError):
            self.calc.add(5, None)
        with self.assertRaises(ValueError):
            self.calc.add(None, None)
    
    def test_add_strings_as_numbers(self):
        self.assertEqual(self.calc.add("2", "3"), 5.0)
    
    # SUBTRACT TESTS
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2.0)
        self.assertEqual(self.calc.subtract(10, 20), -10.0)
    
    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2.0)
        self.assertEqual(self.calc.subtract(-10, -20), 10.0)
    
    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5.0)
        self.assertEqual(self.calc.subtract(0, 5), -5.0)
    
    def test_subtract_none_values(self):
        with self.assertRaises(ValueError):
            self.calc.subtract(None, 5)
        with self.assertRaises(ValueError):
            self.calc.subtract(5, None)
    
    # MULTIPLY TESTS
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6.0)
        self.assertEqual(self.calc.multiply(10, 20), 200.0)
    
    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6.0)
        self.assertEqual(self.calc.multiply(-10, 20), -200.0)
    
    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0.0)
        self.assertEqual(self.calc.multiply(5, 0), 0.0)
        self.assertEqual(self.calc.multiply(0, 0), 0.0)
    
    def test_multiply_none_values(self):
        with self.assertRaises(ValueError):
            self.calc.multiply(None, 5)
        with self.assertRaises(ValueError):
            self.calc.multiply(5, None)
    
    def test_multiply_large_numbers(self):
        self.assertEqual(self.calc.multiply(1000000, 1000000), 1000000000000.0)
    
    # DIVIDE TESTS
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(10, 2), 5.0)
    
    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
    
    def test_divide_with_zero_dividend(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_divide_none_values(self):
        with self.assertRaises(ValueError):
            self.calc.divide(None, 5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, None)
    
    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)
    
    # POWER TESTS
    def test_power_positive_exponent(self):
        self.assertEqual(self.calc.power(2, 3), 8.0)
        self.assertEqual(self.calc.power(5, 2), 25.0)
    
    def test_power_zero_exponent(self):
        self.assertEqual(self.calc.power(5, 0), 1.0)
        self.assertEqual(self.calc.power(100, 0), 1.0)
    
    def test_power_negative_exponent(self):
        self.assertAlmostEqual(self.calc.power(2, -1), 0.5)
        self.assertAlmostEqual(self.calc.power(5, -2), 0.04)
    
    def test_power_zero_base(self):
        self.assertEqual(self.calc.power(0, 5), 0.0)
    
    def test_power_none_values(self):
        with self.assertRaises(ValueError):
            self.calc.power(None, 2)
        with self.assertRaises(ValueError):
            self.calc.power(2, None)
    
    # SQUARE ROOT TESTS
    def test_square_root_perfect_squares(self):
        self.assertEqual(self.calc.square_root(4), 2.0)
        self.assertEqual(self.calc.square_root(9), 3.0)
        self.assertEqual(self.calc.square_root(16), 4.0)
        self.assertEqual(self.calc.square_root(0), 0.0)
    
    def test_square_root_non_perfect_squares(self):
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        self.assertAlmostEqual(self.calc.square_root(10), 3.1622776601683795)
    
    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
        with self.assertRaises(ValueError):
            self.calc.square_root(-100)
    
    def test_square_root_none(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(None)
    
    # MODULO TESTS
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(10, 3), 1.0)
        self.assertEqual(self.calc.modulo(15, 5), 0.0)
    
    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
    
    def test_modulo_none_values(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(None, 5)
        with self.assertRaises(ValueError):
            self.calc.modulo(5, None)
    
    # FACTORIAL TESTS
    def test_factorial_valid_inputs(self):
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        with self.assertRaises(ValueError):
            self.calc.factorial(-10)
    
    def test_factorial_float(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(3.5)
    
    def test_factorial_none(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(None)
    
    def test_factorial_large_number(self):
        self.assertEqual(self.calc.factorial(20), 2432902008176640000)


class TestCalculatorStateManagement(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_get_result_initial(self):
        self.assertEqual(self.calc.get_result(), 0.0)
    
    def test_get_result_after_calculation(self):
        self.calc.add(5, 3)
        self.assertEqual(self.calc.get_result(), 8.0)
    
    def test_get_history_initial(self):
        self.assertEqual(self.calc.get_history(), [])
    
    def test_get_history_after_calculations(self):
        self.calc.add(2, 3)
        self.calc.subtract(10, 5)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("2 + 3 = 5.0", history[0])
        self.assertIn("10 - 5 = 5.0", history[1])
    
    def test_clear_history(self):
        self.calc.add(2, 3)
        self.calc.clear_history()
        self.assertEqual(self.calc.get_history(), [])
    
    def test_reset(self):
        self.calc.add(5, 3)
        self.calc.reset()
        self.assertEqual(self.calc.get_result(), 0.0)
        self.assertEqual(self.calc.get_history(), [])


class TestCalculatorEdgeCases(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_very_large_numbers(self):
        large_num = 10**100
        result = self.calc.add(large_num, large_num)
        self.assertEqual(result, 2 * large_num)
    
    def test_very_small_numbers(self):
        small_num = 10**-100
        result = self.calc.multiply(small_num, small_num)
        self.assertAlmostEqual(result, 10**-200, places=10)
    
    def test_floating_point_precision(self):
        result = self.calc.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)
    
    def test_division_very_small_divisor(self):
        result = self.calc.divide(1, 0.0001)
        self.assertEqual(result, 10000.0)
    
    def test_power_large_exponent(self):
        result = self.calc.power(2, 10)
        self.assertEqual(result, 1024.0)
    
    def test_string_numbers(self):
        result = self.calc.add("10", "20")
        self.assertEqual(result, 30.0)
    
    def test_boolean_as_numbers(self):
        result = self.calc.add(True, False)
        self.assertEqual(result, 1.0)
        result = self.calc.multiply(True, True)
        self.assertEqual(result, 1.0)


class TestCalculatorExceptionHandling(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_type_error_for_non_numeric(self):
        with self.assertRaises((ValueError, TypeError)):
            self.calc.add("abc", 5)
    
    def test_multiple_operations_after_error(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8.0)
    
    def test_history_not_corrupted_after_error(self):
        self.calc.add(2, 3)
        try:
            self.calc.divide(10, 0)
        except ValueError:
            pass
        history = self.calc.get_history()
        self.assertEqual(len(history), 1)
        self.assertIn("2 + 3 = 5.0", history[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
