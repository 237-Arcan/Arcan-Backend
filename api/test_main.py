from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "ArcanApp API fonctionne !"}

def test_analyze_arcanx():
    data = {"example_key": "example_value"}
    response = client.post("/arcanx/analyze", json=data)
    assert response.status_code == 200
    assert "success" in response.json()

def test_analyze_shadowodds():
    odds_data = {"example_key": "example_value"}
    response = client.post("/shadowodds/analyze", json=odds_data)
    assert response.status_code == 200
    assert "success" in response.json()

def test_activate_module():
    module_name = "test_module"
    response = client.post(f"/modules/activate?module_name={module_name}")
    assert response.status_code == 200
    assert "success" in response.json()

def test_deactivate_module():
    module_name = "test_module"
    response = client.post(f"/modules/deactivate?module_name={module_name}")
    assert response.status_code == 200
    assert "success" in response.json()