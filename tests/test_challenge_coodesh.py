from challenge_coodesh import __version__
from fastapi.testclient import TestClient
from challenge_coodesh.db.database import Base
from challenge_coodesh.main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://natan:123@172.17.0.3:5432/teste"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_get_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Back-end Challenge 2021 :medal: - Space Flight News"
    }


def test_create_article():
    data = {
        "id": 137558,
        "url": "a",
        "featured": True,
        "imageurl": "a",
        "newssite": "a",
        "summary": "a",
        "publishedat": "a",
        "title": "a",
        "updatedat": "a",
        "launches": [{"id": "a", "provider": "a"}],
        "events": [{"id": "a", "provider": "a"}],
    }
    response = client.post("/articles/", json=data)
    print(response.json())
    assert response.status_code == 200


def test_create_article_already_exists():
    data = {
        "id": 137558,
        "url": "a",
        "featured": True,
        "imageurl": "a",
        "newssite": "a",
        "summary": "a",
        "publishedat": "a",
        "title": "a",
        "updatedat": "a",
        "launches": [{"id": "a", "provider": "a"}],
        "events": [{"id": "a", "provider": "a"}],
    }
    response = client.post("/articles/", json=data)
    assert response.status_code == 400


def test_delete_article():
    response = client.delete("/articles/137558")
    assert response.status_code == 200
