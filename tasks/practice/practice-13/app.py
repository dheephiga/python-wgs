from flask import Flask, render_template, request, redirect, session, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'secret_key'
Bootstrap(app)

users = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username]['password'] == password:
        session['username'] = username
        return redirect('/dashboard')
    else:
        flash('Invalid username or password', 'error')
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        user_info = users[username]
        return render_template('dashboard.html', user_info=user_info)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    
    if password != confirm_password:
        flash('Passwords do not match', 'error')
        return redirect('/signup')
    
    if username in users:
        flash('Username already exists', 'error')
        return redirect('/signup')
    
    users[username] = {'email': email, 'password': password}
    flash('Registration successful! Please log in.', 'success')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
