# app/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

def test_register_user():
    response = client.post("/register", json={
        "username": "arijit",
        "email": "arijit@example.com"
    })
    assert response.status_code == 200
    assert "registered" in response.json()["message"]
