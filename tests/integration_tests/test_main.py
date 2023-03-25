from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    item_id = 42
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": None}

    q = "test"
    response = client.get(f"/items/{item_id}?q={q}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": q}