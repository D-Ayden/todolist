from todolist import app


def test_app_exist(client):
    assert app is not None


def test_app_is_testing(client):
    assert app.config["TESTING"]


def test_404_error(client):
    rv = client.get("/foo")
    assert 404 == rv.status_code
    assert "404 Not Found" in rv.get_data(as_text=True)

