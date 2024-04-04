from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'

app.config["SECRET KEY"] = 'adminsecret'

db = SQLAlchemy()

login_Manager = LoginManager()
login_Manager.init_app(app)