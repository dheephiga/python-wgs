from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, Date, String
from sqlalchemy.orm import declarative_base 
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'bivdahifbeiHVWIRBIRBI'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
db = SQLAlchemy(app)
   
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(10), nullable=False)
    age = Column(Integer, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)  
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
class Pushups(Base):
    __tablename__ = 'pushups'

    id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return f"Pushups(id={self.id}, count={self.count}, comment='{self.comment}', date={self.date})"
    
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def home():
    username = ""
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    
        if user:
            username = user.username
    return render_template('home.html', username=username, session=session)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        existing_user = User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()
        if existing_user:
            return 'Username or email already exists!'

        if password != confirm_password:
            return 'Passwords do not match!'

        hashed_password = generate_password_hash(password)

        new_user = User(name=name, gender=gender, age=age, username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return 'User created successfully!'

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))

        return 'Invalid email or password!'

    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/show-workouts')
def show_workouts():
    pushup_data = db.session.query(Pushups).all()
    return render_template('dashboard.html',pushup_data=pushup_data)

@app.route('/add-workout',methods=['GET','POST'])
def add_workouts():
    if request.method == 'GET':
        return render_template('workout.html')
    
    if request.method == 'POST':
        count = request.form['count']
        comment = request.form['comment']
        date = request.form['date']
        date = datetime.strptime(date, '%Y-%m-%d')
        pushup = Pushups(count=count, comment=comment, date=date)
        db.session.add(pushup)
        db.session.commit()
        return 'Record created successfully!'
    
if __name__ == '__main__':
    app.run(debug=True)
