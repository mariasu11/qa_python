import pytest

@pytest.mark.smoke
def test_health_endpoint(client):
    """Basic health check"""
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"
