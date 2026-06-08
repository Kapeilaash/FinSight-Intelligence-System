from fastapi.testclient import TestClient

from app.main import app


def test_generate_report_endpoint():
    client = TestClient(app)
    response = client.post("/api/reports/generate", json={"topic": "AAPL"})
    assert response.status_code == 200
    data = response.json()
    assert "markdown" in data
    assert data["topic"] == "AAPL"
    assert len(data["markdown"]) > 80
