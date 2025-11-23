# Tests Directory

This directory contains the comprehensive test suite for the FarmTech Solutions project.

## 📋 Test Overview

The test suite includes:

- **Unit Tests**: Test individual functions and components in isolation
- **Integration Tests**: Test interaction between multiple components
- **API Tests**: Test FastAPI endpoints and request/response handling
- **ML Tests**: Test machine learning model loading and prediction

## 🗂️ Test Files

- `test_alertas.py` - Tests for the alert system (sensor condition evaluation, throttling, consolidation)
- `test_email.py` - Tests for AWS SNS email notifications
- `test_ml_prediction.py` - Tests for ML model predictions (irrigation decisions)
- `test_api.py` - Tests for FastAPI endpoints (init, leitura, irrigacao)
- `conftest.py` - Shared pytest fixtures and configuration
- `__init__.py` - Package initialization

## 🚀 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_alertas.py
pytest tests/test_email.py
pytest tests/test_ml_prediction.py
pytest tests/test_api.py
```

### Run Tests by Category
```bash
# Unit tests only
pytest -m unit

# Integration tests only
pytest -m integration

# API tests only
pytest -m api

# ML tests only
pytest -m ml
```

### Run with Verbose Output
```bash
pytest -v
```

### Run with Coverage Report
```bash
pytest --cov=src --cov-report=html
```

This generates a coverage report in `htmlcov/index.html`

### Run Specific Test
```bash
pytest tests/test_alertas.py::TestAvaliarCondicoes::test_umidade_critica
```

## 📊 Test Coverage

The test suite aims to cover:

- ✅ **Notification System** (alertas.py, email.py)
  - Critical condition evaluation
  - Alert consolidation
  - Throttling mechanism
  - AWS SNS integration
  
- ✅ **ML Prediction** (realizar_previsao_func.py)
  - Model loading
  - Date/time conversion
  - Prediction logic
  - Edge cases
  
- ✅ **API Endpoints** (api_basica.py)
  - Sensor initialization
  - Reading reception
  - Irrigation prediction
  - Request validation

## 🔧 Configuration

Test configuration is defined in:
- `pytest.ini` - Pytest settings and markers
- `conftest.py` - Shared fixtures and mocks

## 🧪 Mocking Strategy

Tests use mocking to avoid external dependencies:

- **AWS SNS**: Mocked with `unittest.mock` to avoid real AWS calls
- **Database**: Mocked to avoid requiring database setup
- **ML Models**: Mocked to avoid loading actual model files

This ensures tests run quickly and don't require external services.

## ⚠️ Important Notes

1. **Environment Variables**: Tests mock environment variables (SNS_REGION, SNS_TOPIC_ARN, etc.)
2. **Database**: Tests don't require a real database - all DB calls are mocked
3. **AWS Credentials**: Tests don't require AWS credentials - SNS client is mocked
4. **ML Models**: Tests don't require actual model files - joblib.load is mocked

## 📈 Test Results

After running tests, you'll see:
- Number of tests passed/failed
- Coverage percentage
- List of uncovered lines
- Execution time

Example output:
```
============ test session starts ============
collected 45 items

tests/test_alertas.py ............ [ 26%]
tests/test_email.py .......... [ 48%]
tests/test_ml_prediction.py ............ [ 75%]
tests/test_api.py ............ [100%]

========== 45 passed in 2.34s ===========
```

## 🐛 Debugging Failed Tests

If a test fails:

1. Check the error message and stack trace
2. Run the specific test with `-v` for verbose output
3. Use `pytest --pdb` to drop into debugger on failure
4. Check if environment variables are properly mocked
5. Verify mock return values match expected types

## 🔄 Continuous Integration

These tests are designed to run in CI/CD pipelines:
- Fast execution (< 10 seconds)
- No external dependencies
- Clear pass/fail indicators
- Coverage reporting

## 📝 Adding New Tests

When adding new tests:

1. Create test file with `test_` prefix
2. Use descriptive test names starting with `test_`
3. Group related tests in classes
4. Add appropriate markers (@pytest.mark.unit, etc.)
5. Use fixtures from conftest.py when possible
6. Mock external dependencies
7. Test both success and failure cases
8. Test edge cases and boundary conditions

## 🎯 Best Practices

- **AAA Pattern**: Arrange, Act, Assert
- **One assertion per test** (when possible)
- **Descriptive names**: test_should_do_something_when_condition
- **Independence**: Tests should not depend on each other
- **Speed**: Keep tests fast by mocking I/O operations

## 📚 Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Python unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
