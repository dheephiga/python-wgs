from flask import Flask,render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/our_users"
app.secret_key = 'secret key'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    email =db.Column(db.String(20), nullable = False, unique=True)
    date_added =db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Name %r> %self.name'
    
with app.app_context():
    db.create_all() 

class UserForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class NameForm(FlaskForm):
    name = StringField("What's your name",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/user/add',methods=['GET','POST'])
def add_user():
    name = None
    form = UserForm()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ""
        form.email.data = ""
        flash("User added succesfully"),
    our_users = Users.query.order_by(Users.date_added)
    return render_template('add_user.html',form=form,name = name, our_users=our_users)

@app.route('/')
def index():
    firstname = 'John'
    confident = 'this is bold here'
    pizza = [234.,3432,123,131,14135]
    return render_template('index.html',first_name=firstname,stuff=confident,pizza=pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NameForm()
    
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted sucessfully!")
    return render_template('name.html',name=name,form=form)
if __name__ == '__main__':
    app.run(debug=True)