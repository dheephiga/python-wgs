from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/hello/<user>')
# def hello_name(user):
#     return render_template('index.html', name=user)

# @app.route('/hello/<int:user>')
# def hello_name(user):
#     return render_template('index.html', marks=user)
@app.route('/hello')
def hello_name():
    mydict = {'phy': 90, 'chem': 80, 'bio': 99}
    return render_template('index.html', result=mydict)


if __name__ == '__main__':
    app.run(debug=True)
