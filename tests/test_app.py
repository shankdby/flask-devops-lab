from app.main import add, app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_add_function():
    assert add(2, 3) == 5


def test_home():
    r = client().get("/")
    assert r.status_code == 200
    assert "Hello" in r.get_json()["message"]


def test_health():
    r = client().get("/health")
    assert r.get_json() == {"status": "ok"}


def test_add_route():
    assert client().get("/add/4/6").get_json() == {"result": 10}


def test_unknown_route_404():
    assert client().get("/nope").status_code == 404
