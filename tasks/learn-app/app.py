from flask import Flask, render_template, request, redirect, flash, session, make_response

app = Flask(__name__)
app.secret_key = 'sRfqaefqfcqqvhetuwcbWerP'
users = {}

@app.route('/')
@app.route('/home')
def home():
    if 'logged_in' in session:
        logged_in = session['logged_in']
    else:
        logged_in = False
    
    return render_template('home.html', logged_in=logged_in)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email not in users:
            flash('Email does not exist. Please sign up.', 'danger')
        elif users[email]['password'] != password:
            flash('Incorrect password. Please try again.', 'danger')
        else:
            session['email'] = email
            session['logged_in'] = True
            resp = make_response(redirect('/home'))
            resp.set_cookie('email', email)
            flash('Login successful!', 'success')
            return resp
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('logged_in', None)
    resp = make_response(redirect('/login'))
    resp.delete_cookie('email')
    flash('Logged out successfully.', 'success')
    return resp


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']  
        age = request.form['age']
        course = request.form['course']
        
        if email not in users:
            users[email] = {'password': password, 'name': name, 'age': age, 'course': course}
            flash('Sign up successful! Please log in.', 'success')
            return redirect('/login')
        else:
            flash('Email already exists. Please log in.', 'danger')
    return render_template('signup.html')


@app.route('/info')
def info():
    if 'email' in session:
        email = session['email']
        if email in users:
            user_info = users[email]  
            return render_template('info.html', user_info=user_info)
        else:
            flash('User information not found.', 'danger')
            return redirect('/login')
    else:
        flash('You must be logged in to view this page.', 'danger')
        return redirect('/login')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
