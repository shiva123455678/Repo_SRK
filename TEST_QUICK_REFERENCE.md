# Calculator Unit Tests - Quick Reference

## ⚡ Quick Commands

```bash
# Run all tests (recommended)
python test_calculator_unittest.py

# Verbose mode
python test_calculator_unittest.py -v

# With pytest
pytest test_calculator.py -v

# Coverage report
pytest test_calculator.py --cov=calculator --cov-report=html
```

## 📊 Test Summary

| Category | Tests | Status |
|----------|-------|--------|
| Basic Arithmetic | 7 | ✅ PASS |
| Complex Expressions | 3 | ✅ PASS |
| Edge Cases | 5 | ✅ PASS |
| Error Handling | 5 | ✅ PASS |
| Special Cases | 4 | ✅ PASS |
| Boolean Expressions | 2 | ✅ PASS |
| Coverage | 1 | ✅ PASS |
| **TOTAL** | **27** | **✅ ALL PASS** |

## 📁 Test Files

- `test_calculator_unittest.py` - Main test suite (unittest)
- `test_calculator.py` - Alternative test suite (pytest)
- `TEST_REPORT.md` - Detailed test report
- `TESTING_GUIDE.md` - Complete testing documentation
- `.github/workflows/test.yml` - CI/CD pipeline
- `requirements.txt` - Project dependencies

## 🧪 Supported Operations

### Arithmetic
```python
evaluate("2 + 3")      # 5
evaluate("10 - 3")     # 7
evaluate("3 * 4")      # 12
evaluate("10 / 2")     # 5.0
evaluate("10 // 3")    # 3
evaluate("10 % 3")     # 1
evaluate("2 ** 3")     # 8
```

### Complex Expressions
```python
evaluate("2 + 3 * 4")           # 14 (order of operations)
evaluate("(2 + 3) * 4")         # 20 (parentheses)
evaluate("2 ** 3 + 4 - 1")      # 11 (mixed operations)
```

### Error Handling
```python
evaluate("5 / 0")      # "Error: Division by zero"
evaluate("2 +")        # "Error: Invalid syntax"
evaluate("")           # "Error: EOFError"
```

## 🎯 Test Examples by Category

### Basic Arithmetic ➕➖✖️➗
```python
def test_addition(self):
    assert evaluate("2 + 3") == 5

def test_division_by_zero(self):
    assert evaluate("5 / 0") == "Error: Division by zero"
```

### Complex Expressions 🔢
```python
def test_order_of_operations(self):
    assert evaluate("2 + 3 * 4") == 14

def test_nested_parentheses(self):
    assert evaluate("((2 + 3) * (4 + 1))") == 25
```

### Edge Cases 🔍
```python
def test_negative_numbers(self):
    assert evaluate("-5 * -3") == 15

def test_large_numbers(self):
    assert evaluate("1000000 + 1000000") == 2000000
```

## 🚀 Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests:**
   ```bash
   python test_calculator_unittest.py
   ```

3. **Expected output:**
   ```
   Ran 27 tests in 0.003s
   OK
   ```

## 📝 Add New Test

```python
class TestNewFeature(unittest.TestCase):
    def test_something(self):
        result = evaluate("expression")
        self.assertEqual(result, expected)
```

## 🔧 Debugging

```bash
# Verbose output
python test_calculator_unittest.py -v

# Specific test
python test_calculator_unittest.py TestBasicArithmetic.test_addition

# With pytest (more detailed)
pytest test_calculator.py -v --tb=short
```

## 📈 Performance

- **Total tests:** 27
- **Execution time:** ~3ms
- **Status:** ✅ All passing

## 🔗 CI/CD

Tests run automatically on:
- ✅ Push to main/develop
- ✅ Pull requests
- See `.github/workflows/test.yml`

## ✨ Key Features

- ✅ 27 comprehensive tests
- ✅ Basic arithmetic operations
- ✅ Complex expression evaluation
- ✅ Edge case handling
- ✅ Error handling verification
- ✅ Floating-point precision tests
- ✅ Boolean operations
- ✅ CI/CD integration
- ✅ No external test framework required*

*pytest is optional; unittest is built-in

## 📚 Documentation

- `TESTING_GUIDE.md` - Comprehensive testing guide
- `TEST_REPORT.md` - Detailed test results
- `calculator.py` - Source code
- `README.md` - Project overview

---

**Last Updated:** 2026-10-08  
**Status:** Production Ready ✅
