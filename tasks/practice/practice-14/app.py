from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY DATABASE URI'] = "sqlite:///profile.db"



if __name__ == "__main__":
    app.run(debug=True)