from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI Cloud"}


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_item_with_query() -> None:
    response = client.get("/items/5?q=somequery")

    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "somequery"}


def test_item_id_validation_error() -> None:
    response = client.get("/items/not-an-int")

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["path", "item_id"]
