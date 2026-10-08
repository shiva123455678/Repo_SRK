#!/usr/bin/env python3
"""
Unit tests for the calculator tool.
Tests the evaluate() function from calculator.py
"""

import pytest
from calculator import evaluate


class TestBasicArithmetic:
    """Test basic arithmetic operations"""

    def test_addition(self):
        """Test addition operation"""
        assert evaluate("2 + 3") == 5
        assert evaluate("10 + 20") == 30
        assert evaluate("-5 + 3") == -2

    def test_subtraction(self):
        """Test subtraction operation"""
        assert evaluate("10 - 3") == 7
        assert evaluate("5 - 10") == -5
        assert evaluate("0 - 5") == -5

    def test_multiplication(self):
        """Test multiplication operation"""
        assert evaluate("3 * 4") == 12
        assert evaluate("0 * 100") == 0
        assert evaluate("-3 * 4") == -12
        assert evaluate("-3 * -4") == 12

    def test_division(self):
        """Test true division operation"""
        assert evaluate("10 / 2") == 5.0
        assert evaluate("7 / 2") == 3.5
        assert evaluate("1 / 4") == 0.25

    def test_floor_division(self):
        """Test floor division operation"""
        assert evaluate("10 // 3") == 3
        assert evaluate("7 // 2") == 3
        assert evaluate("9 // 3") == 3

    def test_modulo(self):
        """Test modulo operation"""
        assert evaluate("10 % 3") == 1
        assert evaluate("7 % 2") == 1
        assert evaluate("10 % 5") == 0

    def test_exponentiation(self):
        """Test exponentiation operation"""
        assert evaluate("2 ** 3") == 8
        assert evaluate("5 ** 2") == 25
        assert evaluate("10 ** 0") == 1


class TestComplexExpressions:
    """Test complex expressions with multiple operations"""

    def test_order_of_operations(self):
        """Test operator precedence"""
        assert evaluate("2 + 3 * 4") == 14
        assert evaluate("(2 + 3) * 4") == 20
        assert evaluate("10 - 2 * 3") == 4
        assert evaluate("100 / 2 / 5") == 10.0

    def test_nested_parentheses(self):
        """Test nested parentheses"""
        assert evaluate("((2 + 3) * (4 + 1))") == 25
        assert evaluate("(10 - (2 + 3)) * 2") == 10

    def test_mixed_operations(self):
        """Test expressions with mixed operations"""
        assert evaluate("2 + 3 * 4 - 5") == 9
        assert evaluate("100 / 10 + 5 * 2") == 20.0
        assert evaluate("2 ** 3 + 4 - 1") == 11


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_zero_operations(self):
        """Test operations with zero"""
        assert evaluate("0 + 0") == 0
        assert evaluate("0 * 1000") == 0
        assert evaluate("0 - 5") == -5

    def test_negative_numbers(self):
        """Test operations with negative numbers"""
        assert evaluate("-5 + 3") == -2
        assert evaluate("-5 * -3") == 15
        assert evaluate("-10 / -2") == 5.0

    def test_floating_point(self):
        """Test floating point calculations"""
        assert evaluate("0.5 + 0.5") == 1.0
        assert evaluate("1.5 * 2") == 3.0
        assert evaluate("3.5 / 2") == 1.75

    def test_large_numbers(self):
        """Test with large numbers"""
        assert evaluate("1000000 + 1000000") == 2000000
        assert evaluate("999999 * 999999") == 999998000001

    def test_very_small_fractions(self):
        """Test with very small fractions"""
        result = evaluate("1 / 1000000")
        assert abs(result - 1e-6) < 1e-10


class TestErrorHandling:
    """Test error handling and validation"""

    def test_division_by_zero(self):
        """Test division by zero error"""
        assert evaluate("5 / 0") == "Error: Division by zero"
        assert evaluate("10 // 0") == "Error: Division by zero"

    def test_invalid_syntax(self):
        """Test invalid syntax errors"""
        assert evaluate("2 +") == "Error: Invalid syntax"
        assert evaluate("* 5") == "Error: Invalid syntax"
        assert evaluate("(2 + 3") == "Error: Invalid syntax"

    def test_undefined_variables(self):
        """Test undefined variable errors"""
        error = evaluate("x + 5")
        assert "Error" in str(error)

    def test_invalid_characters(self):
        """Test invalid character errors"""
        error = evaluate("5 & 3")
        assert "Error" in str(error)

    def test_empty_expression(self):
        """Test empty or whitespace expressions"""
        error = evaluate("")
        assert "Error" in str(error)


class TestSpecialCases:
    """Test special mathematical cases"""

    def test_identity_operations(self):
        """Test identity operations"""
        assert evaluate("5 + 0") == 5
        assert evaluate("5 - 0") == 5
        assert evaluate("5 * 1") == 5
        assert evaluate("5 / 1") == 5.0

    def test_scientific_notation(self):
        """Test scientific notation"""
        assert evaluate("1e2") == 100.0
        assert evaluate("1.5e2") == 150.0
        assert evaluate("1e-2") == 0.01

    def test_power_of_zero(self):
        """Test zero raised to various powers"""
        assert evaluate("0 ** 5") == 0
        assert evaluate("5 ** 0") == 1

    def test_single_number(self):
        """Test single number input"""
        assert evaluate("42") == 42
        assert evaluate("3.14") == 3.14
        assert evaluate("-100") == -100


class TestBooleanExpression:
    """Test boolean and comparison operations"""

    def test_comparison_operators(self):
        """Test comparison operations"""
        assert evaluate("5 > 3") is True
        assert evaluate("5 < 3") is False
        assert evaluate("5 == 5") is True
        assert evaluate("5 != 3") is True

    def test_logical_operators(self):
        """Test logical operations"""
        assert evaluate("True and True") is True
        assert evaluate("True and False") is False
        assert evaluate("True or False") is True
        assert evaluate("not True") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
