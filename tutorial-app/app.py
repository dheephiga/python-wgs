from flask import Flask, request,make_response,render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hey"

# @app.route('/hello')
# def hello():
# #    return 'helloWorld', 201
#     response = make_response('hola')
#     response.status_code = 202
#     response.headers['content-type'] = 'text/plain'
#     return response
    

# @app.route('/greet/<name>')
# def greet(name):
#     return f'hey {name}'

# @app.route('/add/<int:n1>/<int:n2>')
# def add(n1,n2):
#     return f'{n1} + {n2} = {n1+n2}'

# @app.route('/handle_url_params')
# def handle_params():
#     if 'greeting' in request.args.keys() and 'name' in request.args.keys():
#         greeting = request.args['greeting']
#         name = request.args.get('name')
#         return f'{greeting}, {name}'
#     else:
#         return 'parameters missing'
@app.route('/')
def index():
    v1 = 'neuron'
    result = 10 + 393
    myl = [10,90,44,89,45]
    return render_template('index.html',v1=v1,result=result,list=myl)


if __name__ == '__main__':
    app.run(debug=True)