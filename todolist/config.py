# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/6 13:06
# Product: PyCharm
# Project: todolist


import os
import sys


WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

dev_db: str = prefix + os.path.join(basedir, "data-dev.db")
SECRET_KEY = os.getenv("SECRET_KEY", "secret string")
SQLALCHEMY_TRACK_MODIFICATIONS: bool = True
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", dev_db)
# DEBUG_TB_INTERCEPT_REDIRECTS: bool = False
