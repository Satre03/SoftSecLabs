from src.api import app

def test_hello():
    client = app.test_client()
    response = client.get("/hello?name=Anna")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello Anna"}