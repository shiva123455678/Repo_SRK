#!/usr/bin/env python3
"""
Unit tests for the calculator tool using unittest framework.
Tests the evaluate() function from calculator.py
"""

import unittest
from calculator import evaluate


class TestBasicArithmetic(unittest.TestCase):
    """Test basic arithmetic operations"""

    def test_addition(self):
        self.assertEqual(evaluate("2 + 3"), 5)
        self.assertEqual(evaluate("10 + 20"), 30)
        self.assertEqual(evaluate("-5 + 3"), -2)

    def test_subtraction(self):
        self.assertEqual(evaluate("10 - 3"), 7)
        self.assertEqual(evaluate("5 - 10"), -5)
        self.assertEqual(evaluate("0 - 5"), -5)

    def test_multiplication(self):
        self.assertEqual(evaluate("3 * 4"), 12)
        self.assertEqual(evaluate("0 * 100"), 0)
        self.assertEqual(evaluate("-3 * 4"), -12)
        self.assertEqual(evaluate("-3 * -4"), 12)

    def test_division(self):
        self.assertEqual(evaluate("10 / 2"), 5.0)
        self.assertEqual(evaluate("7 / 2"), 3.5)
        self.assertEqual(evaluate("1 / 4"), 0.25)

    def test_floor_division(self):
        self.assertEqual(evaluate("10 // 3"), 3)
        self.assertEqual(evaluate("7 // 2"), 3)
        self.assertEqual(evaluate("9 // 3"), 3)

    def test_modulo(self):
        self.assertEqual(evaluate("10 % 3"), 1)
        self.assertEqual(evaluate("7 % 2"), 1)
        self.assertEqual(evaluate("10 % 5"), 0)

    def test_exponentiation(self):
        self.assertEqual(evaluate("2 ** 3"), 8)
        self.assertEqual(evaluate("5 ** 2"), 25)
        self.assertEqual(evaluate("10 ** 0"), 1)


class TestComplexExpressions(unittest.TestCase):
    """Test complex expressions with multiple operations"""

    def test_order_of_operations(self):
        self.assertEqual(evaluate("2 + 3 * 4"), 14)
        self.assertEqual(evaluate("(2 + 3) * 4"), 20)
        self.assertEqual(evaluate("10 - 2 * 3"), 4)
        self.assertEqual(evaluate("100 / 2 / 5"), 10.0)

    def test_nested_parentheses(self):
        self.assertEqual(evaluate("((2 + 3) * (4 + 1))"), 25)
        self.assertEqual(evaluate("(10 - (2 + 3)) * 2"), 10)

    def test_mixed_operations(self):
        self.assertEqual(evaluate("2 + 3 * 4 - 5"), 9)
        self.assertEqual(evaluate("100 / 10 + 5 * 2"), 20.0)
        self.assertEqual(evaluate("2 ** 3 + 4 - 1"), 11)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""

    def test_zero_operations(self):
        self.assertEqual(evaluate("0 + 0"), 0)
        self.assertEqual(evaluate("0 * 1000"), 0)
        self.assertEqual(evaluate("0 - 5"), -5)

    def test_negative_numbers(self):
        self.assertEqual(evaluate("-5 + 3"), -2)
        self.assertEqual(evaluate("-5 * -3"), 15)
        self.assertEqual(evaluate("-10 / -2"), 5.0)

    def test_floating_point(self):
        self.assertEqual(evaluate("0.5 + 0.5"), 1.0)
        self.assertEqual(evaluate("1.5 * 2"), 3.0)
        self.assertEqual(evaluate("3.5 / 2"), 1.75)

    def test_large_numbers(self):
        self.assertEqual(evaluate("1000000 + 1000000"), 2000000)
        self.assertEqual(evaluate("999999 * 999999"), 999998000001)

    def test_very_small_fractions(self):
        result = evaluate("1 / 1000000")
        self.assertAlmostEqual(result, 1e-6, places=10)


class TestErrorHandling(unittest.TestCase):
    """Test error handling and validation"""

    def test_division_by_zero(self):
        self.assertEqual(evaluate("5 / 0"), "Error: Division by zero")
        self.assertEqual(evaluate("10 // 0"), "Error: Division by zero")

    def test_invalid_syntax(self):
        self.assertEqual(evaluate("2 +"), "Error: Invalid syntax")
        self.assertEqual(evaluate("* 5"), "Error: Invalid syntax")
        self.assertEqual(evaluate("(2 + 3"), "Error: Invalid syntax")

    def test_undefined_variables(self):
        error = evaluate("x + 5")
        self.assertIn("Error", str(error))

    def test_bitwise_operations(self):
        # Python supports bitwise operations, so these are valid
        self.assertEqual(evaluate("5 & 3"), 1)  # bitwise AND
        self.assertEqual(evaluate("5 | 3"), 7)  # bitwise OR

    def test_empty_expression(self):
        error = evaluate("")
        self.assertIn("Error", str(error))


class TestSpecialCases(unittest.TestCase):
    """Test special mathematical cases"""

    def test_identity_operations(self):
        self.assertEqual(evaluate("5 + 0"), 5)
        self.assertEqual(evaluate("5 - 0"), 5)
        self.assertEqual(evaluate("5 * 1"), 5)
        self.assertEqual(evaluate("5 / 1"), 5.0)

    def test_scientific_notation(self):
        self.assertEqual(evaluate("1e2"), 100.0)
        self.assertEqual(evaluate("1.5e2"), 150.0)
        self.assertEqual(evaluate("1e-2"), 0.01)

    def test_power_of_zero(self):
        self.assertEqual(evaluate("0 ** 5"), 0)
        self.assertEqual(evaluate("5 ** 0"), 1)

    def test_single_number(self):
        self.assertEqual(evaluate("42"), 42)
        self.assertEqual(evaluate("3.14"), 3.14)
        self.assertEqual(evaluate("-100"), -100)


class TestBooleanExpression(unittest.TestCase):
    """Test boolean and comparison operations"""

    def test_comparison_operators(self):
        self.assertIs(evaluate("5 > 3"), True)
        self.assertIs(evaluate("5 < 3"), False)
        self.assertIs(evaluate("5 == 5"), True)
        self.assertIs(evaluate("5 != 3"), True)

    def test_logical_operators(self):
        self.assertIs(evaluate("True and True"), True)
        self.assertIs(evaluate("True and False"), False)
        self.assertIs(evaluate("True or False"), True)
        self.assertIs(evaluate("not True"), False)


class TestCoverageReport(unittest.TestCase):
    """Generate test coverage report"""

    def test_coverage_summary(self):
        """This test just runs to show coverage"""
        pass


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
