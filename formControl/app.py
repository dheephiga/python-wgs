from flask import Flask, render_template, request, redirect, flash, session, make_response

app = Flask(__name__)
app.secret_key = 'sRnlskUafHMbvzPGxbWerP'
valid_email = 'abc@gmail.com'

@app.route('/', methods=['GET', 'POST'])
def home():
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
            flash('Form submitted successfully!', 'success')
            return redirect('/success')

    return render_template('index.html')

@app.route('/success')
def success():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if email == valid_email:
            session['email'] = email
            resp = make_response(redirect('/home'))
            resp.set_cookie('email', email)
            return resp
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    email = session.get('email')
    if email:
        return render_template('home.html', email=email)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email', None)
    resp = make_response(redirect('/login'))
    resp.delete_cookie('email')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
