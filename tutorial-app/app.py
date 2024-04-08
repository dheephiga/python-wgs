from flask import Flask, request,make_response,render_template,url_for,redirect  

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index3.html')
    elif request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return 'success'
        else:
            return 'fail'









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
# @app.route('/')
# def index():
#     v1 = 'neuron'
#     result = 10 + 393
#     myl = [10,90,44,89,45]
#     return render_template('index.html',v1=v1,result=result,list=myl)

# @app.route('/nope')
# def other():
#     text = 'Hello Python'
#     return render_template('index2.html',text=text)

# @app.route('/redirect')
# def redirect_point():
#     return redirect(url_for('other'))

# @app.template_filter('reverse_string')
# def reverse_string(s):
#     return s[::-1]

# @app.template_filter('repeat')
# def repeat(s,times=2):
#     return s*times

# @app.template_filter('alternate_case')
# def alternate_case(s):
#     return ''.join([c.upper() if i%2==0 else c.lower() for i,c in enumerate(s)])


if __name__ == '__main__':
    app.run(debug=True)