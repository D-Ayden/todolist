# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/6 13:01
# Product: PyCharm
# Project: todolist


from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import login_required, logout_user, login_user, current_user
from todolist.ext import db
from todolist.models import User
from todolist.forms import RegisterForm, LoginForm


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for("todo.index"))
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Register success.")
        return redirect(url_for(".login"))
    return render_template("register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("todo.index"))
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = User.query.filter_by(username=username).first()
        if user:
            if user.validate_password(password):
                login_user(user, remember)
                flash("Login success.")
                return redirect(url_for("todo.index"))
            else:
                flash("Invalid username or password.")
        else:
            flash("No account", "warning")
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout success.")
    return redirect(url_for(".login"))
