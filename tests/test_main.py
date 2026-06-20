from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_root_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Azure Operations Platform",
        "documentation": "/docs"
    }


def test_health_endpoint() -> None:
    response = client.get("/health")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["status"] == "healthy"
    assert "timestamp" in response_body

def test_services_endpoint() -> None:
    response = client.get("/services")
    response_body = response.json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0]["name"] == "customer-api"
    assert response_body[0]["status"] == "operational"