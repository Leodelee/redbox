from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calculate_add():
    response = client.post("/calculate", json={"operation": "add", "a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "result": 5.0}


def test_calculate_subtract():
    response = client.post("/calculate", json={"operation": "subtract", "a": 7, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"operation": "subtract", "result": 3.0}


def test_calculate_multiply():
    response = client.post("/calculate", json={"operation": "multiply", "a": 6, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"operation": "multiply", "result": 42.0}


def test_calculate_divide():
    response = client.post("/calculate", json={"operation": "divide", "a": 8, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "result": 4.0}


def test_calculate_divide_by_zero():
    response = client.post("/calculate", json={"operation": "divide", "a": 1, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "division by zero"}


def test_calculate_rejects_unknown_operation():
    response = client.post("/calculate", json={"operation": "power", "a": 2, "b": 3})
    assert response.status_code == 422
