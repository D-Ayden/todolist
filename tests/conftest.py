# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/7 18:50
# Product: PyCharm
# Project: todolist


import pytest
from todolist import app
from todolist.ext import db
from todolist.models import User, Item


@pytest.fixture(scope="function")
def client():
    app.config.update(
        TESTING=True, WTF_CSRF_ENABLED=False, SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
    )
    user = User(username="poseidon")
    user.set_password("123")
    item = Item(title="hello flask", status=1)
    with app.test_client() as client:
        with app.test_request_context():
            db.create_all()
            db.session.add_all([user, item])
            db.session.commit()
        yield client
    db.drop_all(app=app)


@pytest.fixture
def runner():
    app.config.update(
        TESTING=True, WTF_CSRF_ENABLED=False, SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
    )
    with app.app_context():
        runner = app.test_cli_runner()
        db.drop_all()
        yield runner
