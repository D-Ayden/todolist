# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/8 16:59
# Product: PyCharm
# Project: todolist


from .test_auth import login


def test_index(client):
    login(client)
    rv = client.get("/")
    assert "TODO" in rv.get_data(as_text=True)
    assert "Logout" in rv.get_data(as_text=True)


def test_add_item(client):
    login(client)
    rv = client.post("/", data=dict(
        title="hello flask",
        status=1,
    ), follow_redirects=True)
    assert "Item Added." in rv.get_data(as_text=True)


def test_delete_item(client):
    login(client)
    rv = client.get("/delete/1", follow_redirects=True)
    assert "Item Deleted." in rv.get_data(as_text=True)


def test_change_item(client):
    login(client)
    rv = client.post("/change/1", data=dict(
        title="hello django",
        status=0,
    ), follow_redirects=True)
    assert "Item Changed." in rv.get_data(as_text=True)

