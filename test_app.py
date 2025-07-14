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
