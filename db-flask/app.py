from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY DATABASE URI'] = 'sqlite:///./testdb.db'
    
    db.init_app(app)
    
    migrate = Migrate(app,db)
    
    return app