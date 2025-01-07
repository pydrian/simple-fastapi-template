from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_v1_items():
    response = client.get("/v1/items")
    assert response.status_code == 200


def test_v1_get_item():
    response = client.get("/v1/items/1")
    assert response.status_code in (200, 404)


def test_v2_get_users():
    response = client.get("/v2/users")
    assert response.status_code == 200


def test_v2_get_user():
    response = client.get("/v2/users/1")
    assert response.status_code == 200


def test_v2_items():
    response = client.get("/v2/items/1")
    assert response.status_code in (200, 404)


def test_v2_get_item():
    response = client.get("/v2/items/1")
    assert response.status_code in (200, 404)


def test_v3_get_users():
    response = client.get("/v3/users")
    assert response.status_code == 200


def test_v3_get_user():
    response = client.get("/v3/users/1")
    assert response.status_code == 200


def test_v3_get_items():
    response = client.get("/v3/items")
    assert response.status_code == 200


def test_v3_get_item():
    response = client.get("/v3/items/1")
    assert response.status_code == 200
