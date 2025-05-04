import pytest

@pytest.mark.integration
def test_create_and_get_user(client):
    # Create
    payload = {"name": "Alice", "email": "alice@example.com"}
    r = client.post("/users", json=payload)
    assert r.status_code == 201
    user = r.json()
    user_id = user["id"]

    # Read
    r2 = client.get(f"/users/{user_id}")
    assert r2.status_code == 200
    data = r2.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"

@pytest.mark.integration
def test_update_user(client):
    # Assume user exists: you could create one first
    r = client.post("/users", json={"name": "Bob", "email": "bob@example.com"})
    uid = r.json()["id"]
    r2 = client.put(f"/users/{uid}", json={"name": "Robert"})
    assert r2.status_code == 200
    assert r2.json()["name"] == "Robert"
