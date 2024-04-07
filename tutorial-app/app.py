from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "hey"

@app.route('/hello')
def hello():
    return 'helloWorld'

@app.route('/greet/<name>')
def greet(name):
    return f'hey {name}'

@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    return f'{n1} + {n2} = {n1+n2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'parameters missing'
    


if __name__ == '__main__':
    app.run(debug=True)