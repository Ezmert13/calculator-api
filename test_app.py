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


def test_multiply_invalid_input():
    with app.test_client() as client:
        response = client.get("/multiply?b=5")
        assert response.status_code == 400
        assert "error" in response.json


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
        assert "error" in response.json


def test_subtract():
    with app.test_client() as client:
        response = client.get("/subtract?a=4&b=2")
        assert response.status_code == 200
        assert response.json["result"] == 2.0


def test_subtract_invalid_input():
    with app.test_client() as client:
        response = client.get("/divide?a=x&b=3")
        assert response.status_code == 400
        assert "error" in response.json


def test_sum_list():
    with app.test_client() as client:
        response = client.get("/sum-list?numbers=1,2,3,4,5")
        assert response.status_code == 200
        assert response.json["result"] == 15


def test_health_check():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json == {"status": "ok"}


def test_ping():
    with app.test_client() as client:
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.json["message"] == "ping"
