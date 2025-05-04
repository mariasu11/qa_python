import pytest

@pytest.mark.performance
def test_users_list_latency(benchmark, client):
    """Measure latency of listing users"""
    result = benchmark(client.get, "/users")
    assert result.status_code == 200
