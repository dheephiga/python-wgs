from flask import Flask, render_template,request,Response,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    pass

@app.route('/login',methods=['GET','POST'])
def login():
    pass
if __name__ == '__main__':
    app.run(debug=True)