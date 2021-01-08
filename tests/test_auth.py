# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/7 18:41
# Product: PyCharm
# Project: todolist


def register(client, username=None, password=None, password2=None):
    if username is None or password is None:
        username = "poseidon1"
        password = "1234"
        password2 = password

    return client.post(
        "/register", data=dict(username=username, password=password, password2=password), follow_redirects=True
    )


def login(client, username=None, password=None):
    if username is None or password is None:
        username = "poseidon"
        password = "123"

    return client.post(
        "/login", data=dict(username=username, password=password), follow_redirects=True
    )


def logout(client):
    return client.get("/logout", follow_redirects=True)


def test_register(client):
    rv = register(client)
    assert "Register success." in rv.get_data(as_text=True)


def test_login_logout(client):
    rv = login(client)
    print(rv.get_data(as_text=True))
    assert "Login success." in rv.get_data(as_text=True)

    rv = logout(client)
    assert "Logout success." in rv.get_data(as_text=True)


def test_fail_register_username(client):
    ok = register(client)
    rv = register(client, username="poseidon", password="123", password2="123")
    assert "Please use a different username." in rv.get_data(as_text=True)


def test_fail_register_password(client):
    rv = register(client, username="wrong-username", password="wrong-username", password2="wrong-username2")
    assert "Field must be equal to password." in rv.get_data(as_text=True)


def test_fail_login(client):
    rv = login(client, username="wrong-username", password="wrong-username")
    assert "Invalid username or password." in rv.get_data(as_text=True)


def test_login_protect(client):
    rv = client.get("/", follow_redirects=True)
    assert "Please login to access this page." in rv.get_data(as_text=True)
