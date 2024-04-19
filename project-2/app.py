from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    firstname = 'John'
    confident = 'this is bold here'
    pizza = [234.,3432,123,131,14135]
    return render_template('index.html',first_name=firstname,stuff=confident,pizza=pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)