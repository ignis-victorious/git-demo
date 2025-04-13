#  ___________________
#  Import LIBRARIES
from fastapi.testclient import TestClient

#  Import FILES
from src.main import app
#  ___________________


# Setup the TestClient
client = TestClient(app)


def test_hello() -> None:
    response = client.get("/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == "Hello, World!"


def test_goodbye() -> None:
    response = client.get("/goodbye")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == "Goodbye, World!"


def test_goodbye_name() -> None:
    response = client.get("/goodbye?name=Test")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == "Goodbye, Test!"
