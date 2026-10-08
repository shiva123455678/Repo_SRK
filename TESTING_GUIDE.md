# Calculator Tool - Testing Guide

## Overview
This guide covers how to run, write, and maintain unit tests for the Python calculator tool.

## Quick Start

### Run All Tests
```bash
python test_calculator_unittest.py
```

### Expected Output
```
Ran 27 tests in 0.003s
OK
```

## Available Test Files

### 1. test_calculator_unittest.py (Recommended)
- Uses Python's built-in `unittest` framework
- No external dependencies
- Easier to run in any environment
- **Command**: `python test_calculator_unittest.py`

### 2. test_calculator.py
- Uses `pytest` framework
- More features and better output formatting
- Requires `pytest` installation
- **Command**: `pytest test_calculator.py -v`

## Installation

```bash
# Install project dependencies
pip install -r requirements.txt

# For pytest (optional)
pip install pytest pytest-cov

# For advanced testing with coverage
pip install coverage
```

## Test Execution Examples

### 1. Basic Test Run
```bash
python test_calculator_unittest.py
```

### 2. Verbose Output
```bash
python test_calculator_unittest.py -v
```

### 3. Run Specific Test Class
```bash
python test_calculator_unittest.py TestBasicArithmetic -v
```

### 4. Run Specific Test Method
```bash
python test_calculator_unittest.py TestBasicArithmetic.test_addition -v
```

### 5. With pytest
```bash
# Run all tests
pytest test_calculator.py

# With verbose output
pytest test_calculator.py -v

# Show print statements
pytest test_calculator.py -v -s

# Stop on first failure
pytest test_calculator.py -x

# Show only failures
pytest test_calculator.py --tb=short
```

## Coverage Analysis

### Generate Coverage Report
```bash
# Run with coverage tracking
coverage run test_calculator_unittest.py

# View coverage report in terminal
coverage report

# Generate HTML report
coverage html

# View HTML report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### With pytest-cov
```bash
pytest test_calculator.py --cov=calculator --cov-report=html
```

## Writing New Tests

### Test Template
```python
class TestNewFeature(unittest.TestCase):
    """Test description"""

    def test_specific_case(self):
        """Test case description"""
        result = evaluate("expression")
        self.assertEqual(result, expected_value)
```

### Adding Tests to Existing Class
1. Open `test_calculator_unittest.py`
2. Find the appropriate test class
3. Add a new test method following the naming convention `test_*`
4. Use assertions to verify the result

### Common Assertions
```python
# Equality
self.assertEqual(a, b)
self.assertNotEqual(a, b)

# Truth values
self.assertTrue(value)
self.assertFalse(value)
self.assertIs(a, b)
self.assertIsNot(a, b)

# Container membership
self.assertIn(item, container)
self.assertNotIn(item, container)

# Floating point
self.assertAlmostEqual(a, b, places=7)

# Exception handling
with self.assertRaises(ZeroDivisionError):
    evaluate("5/0")

# String matching
self.assertIn("Error", result_string)
```

## Test Categories

### 1. Basic Arithmetic (TestBasicArithmetic)
Tests single operations:
- Addition, Subtraction, Multiplication
- Division, Floor Division, Modulo
- Exponentiation

**When to add tests here**: When adding support for a new single operator

### 2. Complex Expressions (TestComplexExpressions)
Tests multiple operations with precedence:
- Order of operations
- Nested parentheses
- Mixed operations

**When to add tests here**: When modifying operator precedence or expression parsing

### 3. Edge Cases (TestEdgeCases)
Tests boundary conditions:
- Zero, negative numbers, large numbers
- Floating point precision
- Special numeric values

**When to add tests here**: When fixing edge case bugs or supporting new numeric types

### 4. Error Handling (TestErrorHandling)
Tests error conditions:
- Division by zero
- Invalid syntax
- Undefined variables
- Malformed expressions

**When to add tests here**: When adding new error conditions or improving error messages

### 5. Special Cases (TestSpecialCases)
Tests mathematical identities:
- Identity operations
- Scientific notation
- Power operations
- Single inputs

**When to add tests here**: When adding support for special notation or formats

### 6. Boolean Expressions (TestBooleanExpression)
Tests logical and comparison operations:
- Comparison operators
- Logical operators

**When to add tests here**: When ensuring compatibility with boolean algebra

## Continuous Integration

Tests run automatically on:
- Push to `main` or `develop` branches
- Pull requests

See `.github/workflows/test.yml` for CI configuration.

## Debugging Failed Tests

### 1. Run Test with Verbose Output
```bash
python test_calculator_unittest.py -v TestNameHere.test_method_name -v
```

### 2. Use Print Debugging
```python
def test_case(self):
    result = evaluate("2 + 2")
    print(f"Result: {result}, Type: {type(result)}")
    self.assertEqual(result, 4)
```

Run with: `python test_calculator_unittest.py -v -s`

### 3. Add Temporary Debug Code
```python
def test_case(self):
    import pdb; pdb.set_trace()  # Debugger will pause here
    result = evaluate("2 + 2")
    self.assertEqual(result, 4)
```

### 4. Inspect Error Messages
```bash
# Run with full traceback
python test_calculator_unittest.py
```

## Best Practices

1. **One assertion per concept**: Each test should verify one behavior
2. **Clear test names**: Use descriptive names like `test_addition_with_negative_numbers`
3. **Test isolation**: Tests should not depend on each other
4. **Use appropriate assertions**: Choose the right assertion method
5. **Test edge cases**: Include boundary conditions and special values
6. **Document complex tests**: Add comments explaining non-obvious test logic

## Performance Considerations

Current test execution time: **~3ms for 27 tests**

To check performance:
```bash
# Time the test execution
time python test_calculator_unittest.py

# Profile test execution
python -m cProfile test_calculator_unittest.py
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'calculator'"
**Solution**: Run tests from the project root directory where `calculator.py` is located

### Issue: "Error: Division by zero"
**Solution**: This is expected for division by zero tests. Verify the error message matches the test expectation

### Issue: Floating point assertion fails
**Solution**: Use `assertAlmostEqual` instead of `assertEqual` for floating point comparisons
```python
self.assertAlmostEqual(evaluate("1 / 3"), 0.3333333, places=7)
```

### Issue: pytest not found
**Solution**: Install pytest: `pip install pytest`

## Adding Tests for New Features

When adding a new feature to the calculator:

1. **Write the test first** (Test-Driven Development):
   ```python
   def test_new_feature(self):
       result = evaluate("expression_using_new_feature")
       self.assertEqual(result, expected_value)
   ```

2. **Implement the feature** in `calculator.py`

3. **Run tests**: `python test_calculator_unittest.py`

4. **Verify all tests pass**

5. **Add to appropriate test class** or create new test class if needed

## Resources

- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)

## Support

For issues or questions about testing:
1. Check this guide
2. Review existing test examples
3. Consult unittest/pytest documentation
