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
