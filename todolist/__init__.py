from flask import Flask
from todolist.ext import db, login_manager, bootstrap, csrf, moment
from todolist.blueprints.auth import auth_bp
from todolist.blueprints.todo import todo_bp


app = Flask("todolist")
app.config.from_pyfile("config.py")
db.init_app(app)
bootstrap.init_app(app)
login_manager.init_app(app)
csrf.init_app(app)
moment.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)

from todolist import commands, errors