from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = [{'todo': 'code', 'done': False}]


@app.route('/')
def index():
    return render_template('index.html',todos=todos)

if __name__ == '__main__':
    app.run(debug=True)