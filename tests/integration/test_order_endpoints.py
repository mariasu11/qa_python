import pytest

@pytest.mark.integration
def test_create_order_and_list(client):
    # Create order
    order = {"user_id": 1, "product": "Widget", "qty": 3}
    r = client.post("/orders", json=order)
    assert r.status_code == 201

    # List orders
    r2 = client.get("/orders")
    assert r2.status_code == 200
    assert any(o["product"] == "Widget" for o in r2.json())
