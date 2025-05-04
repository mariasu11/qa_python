import pytest
import json
from pathlib import Path

@pytest.mark.contract
def test_user_contract(client, jsonschema_validate):
    # Get a sample user
    r = client.get("/users/1")
    assert r.status_code == 200
    user = r.json()
    schema = json.loads(Path(__file__).parent / "user_schema.json")
    jsonschema_validate(user, schema)
