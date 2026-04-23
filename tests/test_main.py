import sys
import os

from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200

def test_invalid_route():
    response = client.get("/rota-invalida")
    assert response.status_code == 404

def test_root_content():
    response = client.get("/")
    assert "message" in response.json()