from app import app


def test_add():
    with app.test_client() as client:
        response = client.get("/add?a=2&b=3")
        assert response.status_code == 200
        assert response.json["result"] == 5


def test_multiply():
    with app.test_client() as client:
        response = client.get("/multiply?a=2&b=3")
        assert response.status_code == 200
        assert response.json["result"] == 6


def test_divide():
    with app.test_client() as client:
        response = client.get("/divide?a=6&b=2")
        assert response.status_code == 200
        assert response.json["result"] == 3.0


def test_divide_by_zero():
    with app.test_client() as client:
        response = client.get("/divide?a=6&b=0")
        assert response.status_code == 400
        assert "error" in response.json


def test_divide_invalid_input():
    with app.test_client() as client:
        response = client.get("/divide?a=x&b=3")
        assert response.status_code == 400
        assert "error" on response.json
