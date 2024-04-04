from flask import Flask, render_template, request, redirect, flash, session, make_response

app = Flask(__name__)
app.secret_key = 'sRnlskUafHMbvzPGxbWerP'

users = {}

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']

        if not uname:
            flash('Please enter a username', 'danger')
        if not email:
            flash('Please enter an email', 'danger')
        if not password:
            flash('Please enter a password', 'danger')
        if not cpassword:
            flash('Please confirm your password', 'danger')
        if password != cpassword:
            flash('Passwords do not match', 'danger')
        else:
            if email in users:
                flash('Email already exists. Please log in.', 'danger')
            else:
                users[email] = {'username': uname, 'password': password}
                flash('Sign up successful! Please log in.', 'success')
                return redirect('/login')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            session['email'] = email
            session['uname'] = users[email]['username']
            resp = make_response(redirect('/home'))
            resp.set_cookie('uname',session['uname'])
            return resp
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    uname = session.get('uname')
    if uname:
        return render_template('home.html', uname=uname)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('uname', None)
    resp = make_response(redirect('/login'))
    resp.delete_cookie('uname')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
