import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from main import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "ok"
    assert data["database"] == "connected"

def test_version():
    client = app.test_client()
    response = client.get("/version")

    assert response.status_code == 200
    data = response.get_json()
    assert data["application"] == "ops-pilot"
    assert data["version"] == "1.0.0"