from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set your secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file path
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Increased length for hashed password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Create all database tables
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def home():
    username = None
    if 'user_id' in session:
        # Assuming you have stored the username in the session
        username = session['username']
    return render_template('home.html', username=username)
    return render_template('home.html')

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

        # Check if the username or email already exists
        existing_user = User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()
        if existing_user:
            return 'Username or email already exists!'

        # Check if passwords match
        if password != confirm_password:
            return 'Passwords do not match!'

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Create a new user
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

        # Check if user exists and password is correct
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

if __name__ == '__main__':
    app.run(debug=True)
