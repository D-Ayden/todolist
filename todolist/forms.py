# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/6 12:22
# Product: PyCharm
# Project: todolist


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from todolist.models import User


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(1, 24)])
    password = PasswordField("Password", validators=[DataRequired(), Length(1, 24)])
    password2 = PasswordField(
        "Repeat password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(1, 24)])
    password = PasswordField("Password", validators=[DataRequired(), Length(1, 24)])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")


class ItemForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(1, 64)])
    status = RadioField(
        "Status", validators=[DataRequired()], choices=[("1", "是"), ("0", "否")]
    )
    submit = SubmitField("Submit")
