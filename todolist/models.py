# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/6 12:22
# Product: PyCharm
# Project: todolist


from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from todolist.ext import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    items = db.relationship("Item", back_populates="user", cascade="all")

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="items")
    title = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
