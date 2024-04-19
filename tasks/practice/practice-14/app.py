from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

# Define the Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(200))
    attachments = db.Column(db.String(200))
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref=db.backref('profiles', lazy=True))

# Create the database tables
with app.app_context():
    db.create_all()

# Flask-Login configuration
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def index():
    profiles = Profile.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', profiles=profiles)

@app.route('/profile/<int:id>')
def profile(id):
    profile = Profile.query.get_or_404(id)
    profile.views += 1
    db.session.commit()
    return render_template('profile.html', profile=profile)

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        status = request.form['status']
        attachments = request.form['attachments']

        profile = Profile(name=name, email=email, status=status, attachments=attachments)
        db.session.add(profile)
        db.session.commit()
        flash('Profile created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('create_profile.html')

@app.route('/update_profile/<int:id>', methods=['GET', 'POST'])
def update_profile(id):
    profile = Profile.query.get_or_404(id)
    if request.method == 'POST':
        profile.name = request.form['name']
        profile.email = request.form['email']
        profile.status = request.form['status']
        profile.attachments = request.form['attachments']
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('update_profile.html', profile=profile)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
