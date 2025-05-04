# API & Backend Testing Framework

A pytest-based setup for:
- **Smoke** test (health endpoint)  
- **Integration** tests for user/order APIs  
- **Contract** tests via JSON Schema  
- **Performance** tests via pytest-benchmark  

## Quickstart

```git clone https://github.com/mariasu11/qa_python.git```
```cd api_test_framework```

```python3 -m venv venv && source venv/bin/activate```
```pip install -r requirements.txt```

# Point at your API
export BASE_URL=https://api.example.com

# Run all tests
```pytest```

# Only smoke tests
```pytest -m smoke```

# Only performance tests
```pytest -m performance```
