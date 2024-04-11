from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./logindb.db'
    app.secret_key = 'KEY'

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)

    # Register routes and other configurations
    from routes import register_routes
    register_routes(app, db, bcrypt)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Load user function for Flask-Login
    from models import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    return app
