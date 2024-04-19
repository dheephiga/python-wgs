from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, Date, String
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'bivdahifbeiHVWIRBIRBI'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(10), nullable=False)
    age = Column(Integer, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)  
    
    def __repr__(self):
        return f"Users('{self.username}', '{self.email}')"
    
class Pushupss(db.Model):
    __tablename__ = 'pushups'

    id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return f"Pushupss(id={self.id}, count={self.count}, comment='{self.comment}', date={self.date})"
    

# with app.app_context():
#     db.create_all()


@app.route('/')
@app.route('/home')
def home():
    username = ""
    if 'user_id' in session:
        user = Users.query.get(session['user_id'])
    
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

        existing_user = Users.query.filter_by(username=username).first() or Users.query.filter_by(email=email).first()
        if existing_user:
            return 'Username or email already exists!'

        if password != confirm_password:
            return 'Passwords do not match!'

        hashed_password = generate_password_hash(password)

        new_user = Users(name=name, gender=gender, age=age, username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return 'User created successfully!'

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(email=email).first()
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
    pushup_data = db.session.query(Pushupss).all()
    return render_template('dashboard.html',pushup_data=pushup_data)

@app.route('/add-workout',methods=['GET','POST'])
def add_workouts():
    if request.method == 'POST':
        count = request.form['count']
        comment = request.form['comment']
        date = request.form['date']
        date = datetime.strptime(date, '%Y-%m-%d')
        pushup = Pushupss(count=count, comment=comment, date=date)
        db.session.add(pushup)
        db.session.commit()
        return render_template('dashboard.html')
    
    else:
        return render_template('workout.html')
    

@app.route('/edit-pushup/<int:id>', methods =['GET','POST'])
def edit_pushup(id):
    pushup = Pushupss.query.get_or_404(id)
    if request.method == 'POST':
        pushup.count = request.form['count']
        pushup.comment = request.form['comment']
        pushup.date = request.form['date']
        pushup.date = datetime.strptime(pushup.date, '%Y-%m-%d')
        db.session.commit()
        return render_template('dashboard.html')
    else:
        return render_template('edit.html',pushup=pushup)
    
    
@app.route('/delete-pushup/<int:id>',methods=['POST','GET'])  
def delete_pushup(id):
    pushup = Pushupss.query.get_or_404(id)
    db.session.delete(pushup)
    db.session.commit()
    
    return render_template("dashboard.html")
    
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)