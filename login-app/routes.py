from flask import render_template, request
from models import User
from flask_login import login_user, logout_user, current_user, login_required


def register_routes(app, db, bcrypt):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if current_user.is_authenticated:
            return str(current_user.username)
        else:
            return 'No user logged in'

    @app.route('/login/<uid>')
    def login(uid):
        user = User.query.get(uid)
        login_user(user)
        return 'success'

    @app.route('/logout')
    def logout():
        logout_user()
        return 'success'

