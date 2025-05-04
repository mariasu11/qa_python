import os
import pytest
import httpx

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

@pytest.fixture(scope="session")
def client():
    """HTTPX client for all tests"""
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as c:
        yield c
