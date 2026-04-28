from fastapi.testclient import TestClient

from app.main import app


def test_health_returns_ok_status_and_schema() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "0.1.0"}


def test_cors_denies_unallowlisted_origins_by_default() -> None:
    client = TestClient(app)

    response = client.options(
        "/health",
        headers={
            "Origin": "https://attacker.example",
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 400
    assert "access-control-allow-origin" not in response.headers
