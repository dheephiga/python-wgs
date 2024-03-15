from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'homepage'


@app.route('/about')
def about():
    return 'about page'


if __name__ == '__main__':
    app.run()
