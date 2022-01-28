from challenge_coodesh import __version__
from fastapi.testclient import TestClient
from challenge_coodesh.main import app

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Back-end Challenge 2021 :medal: - Space Flight News"
    }
