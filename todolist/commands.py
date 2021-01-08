# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/6 13:24
# Product: PyCharm
# Project: todolist


import click
from todolist import app, db
from todolist.models import User, Item


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop: str):
    """Initialize the database."""
    if drop:
        click.confirm(
            "This operation will delete the database, do you want to continue?",
            abort=True,
        )
        db.drop_all()
        click.echo("Drop tables.")
    db.create_all()
    click.echo("Initialized database.")


@app.cli.command()
@click.option("--username", prompt=True, help="The username use to login.")
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help="The password use to login.",
)
def init(username: str, password: str):
    """Initialize a user."""
    click.echo("Initializing the database...")
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo("The administrator already exist, updating...")
        user.username = username
        user.set_password(password)
    else:
        click.echo("Creating the temporary administrator account...")
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo("Done.")


@app.cli.command()
@click.option("--count", default=10, help="Quantity of messages, default is 20.")
def forge(count: int):
    """Generate fake message."""
    from faker import Faker
    import random

    fake = Faker()

    db.drop_all()
    db.create_all()

    click.echo("Generating a User...")
    user = User(username="poseidon")
    user.set_password("123")

    for i in range(count):
        click.echo("Creating the item...")
        item = Item(
            user=user,
            title=fake.sentence(),
            status=random.randint(0, 1),
            create_time=fake.date_time_this_year(),
        )
        db.session.add(item)
    db.session.commit()
    click.echo(f"Created {count} fake item.")
