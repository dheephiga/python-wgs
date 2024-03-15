from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<int:user>')
def hello_name(user):
    return render_template('index.html', marks=user)


if __name__ == '__main__':
    app.run(debug=True)
