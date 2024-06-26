from flask import Flask,render_template, flash, request
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/our_users"
app.secret_key = 'secret key'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    email =db.Column(db.String(20), nullable = False, unique=True)
    favorite_color = db.Column(db.String(20))
    date_added =db.Column(db.DateTime, default=datetime.now)
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<Name %r> %self.name'
    
class UserForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    favorite_color = StringField("Favorite Color")
    password_hash = PasswordField('Password',validators=[DataRequired(),EqualTo('password_hash2',message='Passwords must match')])
    password_hash2 = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField("Submit")
    
class NameForm(FlaskForm):
    name = StringField("What's your name",validators=[DataRequired()])
    submit = SubmitField("Submit")
    
with app.app_context():
    db.create_all()


#json
@app.route('/date')
def get_date():
    favorite_pizza
    return {"Date": date.today()}   

@app.route('/user/add',methods=['GET','POST'])
def add_user():
    name = None
    form = UserForm()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            hashed_pw = generate_password_hash(form.password_hash.data)
            user = Users(name=form.name.data, email=form.email.data,favorite_color=form.favorite_color.data,password_hash=form.password_hash.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ""
        form.email.data = ""
        form.favorite_color.data =""
        form.password_hash = ""
        flash("User added succesfully"),
    our_users = Users.query.order_by(Users.date_added)
    return render_template('add_user.html',form=form,name = name, our_users=our_users)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.favorite_color = request.form['favorite_color']
        
        try:
            db.session.commit()
            flash('User updated sucessfully')
            return render_template('update.html',form=form,name_to_update=name_to_update)
        except:
            flash('Error, try again')
            return render_template('update.html',form=form,name_to_update=name_to_update)
            
    else:
        return render_template('update.html',form=form,name_to_update=name_to_update,id=id)
        
@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Users.query.get_or_404(id) 
    name = None
    form = UserForm()
    
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted successfully") 
        our_users = Users.query.order_by(Users.date_added)
        return render_template('add_user.html',form=form,name = name, our_users=our_users)
    
    except:
        flash("There was a problem deleting the user")
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