from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_python_domain():
    response = client.get("/question/python")
    assert response.status_code == 200

def test_data_science_domain():
    response = client.get("/question/ds")
    assert response.status_code == 200

def test_machine_learning_domain():
    response = client.get("/question/ml")
    assert response.status_code == 200

def test_web_development_domain():
    response = client.get("/question/web")
    assert response.status_code == 200

def test_invalid_domain():
    response = client.get("/question/java")
    assert response.status_code == 400