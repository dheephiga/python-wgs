from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('user.html', username=username)
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
