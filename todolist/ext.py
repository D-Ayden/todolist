# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/6 12:22
# Product: PyCharm
# Project: todolist


from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment


db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
csrf = CSRFProtect()
moment = Moment()


login_manager.login_view = "auth.login"
login_manager.login_message = "Please login to access this page."


@login_manager.user_loader
def load_user(user_id):
    from todolist.models import User

    return User.query.get(int(user_id))
