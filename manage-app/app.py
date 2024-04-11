from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask.globals import request_ctx

app = Flask(__name__)
app.secret_key = 'secret-managing-application'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
db = SQLAlchemy(app)

#
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  
    tasks = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    task = db.Column(db.Text)
    assignee = db.Column(db.String(20), nullable=False)
    priority = db.Column(db.String(20), nullable=False)


    def __repr__(self):
        return f"Task('{self.title}')"
    
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/index')
def index():
    username = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            username = user.username
    return render_template('index.html', username=username)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
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

        new_user = User(name=name, role=role, username=username, email=email, password=hashed_password)
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
            return redirect(url_for('index'))

        return 'Invalid email or password!'

    return render_template('login.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'user_id' in session:
        session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/create_task', methods=['GET'])
def create_task_form():
    return render_template('task_create.html')


@app.route('/create_task',methods=['POST'])
def create_task():
    title = request.form.get('title')
    task = request.form.get('task')
    assignee = request.form.get('assignee')
    priority = request.form.get('priority')
    
    if not title:
        return jsonify({'error': 'Title is required'}), 400

    new_task = Task(title=title, task=task, assignee=assignee, priority=priority)
    db.session.add(new_task)
    db.session.commit()
    
    users_to_update = User.query.filter_by(role=assignee).all()
    for user in users_to_update:
        user.tasks += 1

    return jsonify({'message': 'Task created successfully'}), 201


@app.route('/tasks',methods=['GET'])
def view_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
    
