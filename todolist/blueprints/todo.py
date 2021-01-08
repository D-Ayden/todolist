# -*- coding=utf-8 -*-

# Author: D-zilch
# Datetime: 2020/4/6 13:02
# Product: PyCharm
# Project: todolist


from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from todolist.forms import ItemForm
from todolist.models import Item
from todolist.ext import db


todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/", methods=["GET"])
@login_required
def index():
    form = ItemForm()
    todolist = Item.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", todolist=todolist, form=form)


@todo_bp.route("/", methods=["POST"])
@login_required
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        title = form.title.data
        status = form.status.data
        item = Item(user=current_user, title=title, status=status)
        db.session.add(item)
        db.session.commit()
        flash("Item Added.")
    return redirect(url_for(".index"))


@todo_bp.route("/delete/<int:item_id>")
@login_required
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash("Item Deleted.")
    return redirect(url_for(".index"))


@todo_bp.route("/change/<int:item_id>", methods=["GET", "POST"])
@login_required
def change_item(item_id):
    form = ItemForm()
    item = Item.query.get_or_404(item_id)
    if form.validate_on_submit():
        item.title = form.title.data
        item.status = form.status.data
        db.session.commit()
        flash("Item Changed.")
        return redirect(url_for(".index"))

    form.title.data = item.title
    form.status.data = str(item.status)
    return render_template("modify.html", form=form)
