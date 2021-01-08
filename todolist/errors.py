# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/10 21:44
# Product: PyCharm
# Project: todolist


from flask import render_template
from todolist import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def internals_server_error(e):
    return render_template("errors/500.html"), 500
