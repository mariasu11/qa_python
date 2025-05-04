# API & Backend Testing Framework

A pytest-based setup for:
- **Smoke** test (health endpoint)  
- **Integration** tests for user/order APIs  
- **Contract** tests via JSON Schema  
- **Performance** tests via pytest-benchmark  

## Quickstart

1. ```git clone https://github.com/mariasu11/qa_python.git```
2. ```cd api_test_framework```
3. ```python3 -m venv venv && source venv/bin/activate```
4. ```pip install -r requirements.txt```

# Point at your API
export BASE_URL=https://api.example.com

# Run all tests
```pytest```

# Only smoke tests
```pytest -m smoke```

# Only performance tests
```pytest -m performance```
