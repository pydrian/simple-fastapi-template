from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_v1_items():
    response = client.get("/v1/items")
    assert response.status_code == 200


def test_v2_items():
    response = client.get("/v2/items/1")
    assert response.status_code in (200, 404)
