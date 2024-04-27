from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info',methods = ['GET','POST'])
def info():
    name = request.form['name']
    student_id = request.form['id']
    course = request.form['course']
    comment = request.form['comment']
    
    return render_template('info.html',name=name,student_id=id,course=course,comment=comment)
    
    
if __name__ == "__main__":
    app.run(debug=True)
