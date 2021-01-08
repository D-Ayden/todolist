# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/7 20:46
# Product: PyCharm
# Project: todolist


from todolist.models import User, Item


def test_initdb_commands(runner):
    rv = runner.invoke(args=["initdb"])
    assert "Initialized database." in rv.output


def test_initdb_commands_with_drop(runner):
    rv = runner.invoke(args=["initdb", "--drop"], input="y")  #y/n
    assert "Initialized database." in rv.output


def test_init_commands(runner):
    rv = runner.invoke(args=["init", "--username", "poseidon", "--password", "123"])
    assert "Initializing the database..." in rv.output
    assert "Creating the temporary administrator account..." in rv.output
    assert User.query.count() == 1
    assert "Done." in rv.output


def test_init_commands_with_update(runner):
    runner.invoke(args=["init", "--username", "poseidon", "--password", "123"])
    rv = runner.invoke(args=["init", "--username", "admin", "--password", "123456"])
    assert "Initializing the database..." in rv.output
    assert "The administrator already exist, updating..." in rv.output
    assert User.query.count() == 1
    assert "Done." in rv.output


def test_forge_commands(runner):
    rv = runner.invoke(args=["forge"])
    assert "Generating a User..."
    assert User.query.count() == 1
    assert "Creating the item..." in rv.output
    assert Item.query.count() == 10
    assert "Created 10 fake item." in rv.output


def test_forge_commands_with_count(runner):
    rv = runner.invoke(args=["forge", "--count", "50"])
    assert "Generating a User..."
    assert User.query.count() == 1
    assert "Creating the item..." in rv.output
    assert Item.query.count() == 50
    assert "Created 50 fake item." in rv.output