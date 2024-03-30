from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')

@app.route('/task1')
def task1():
    return render_template('task1.html')

@app.route('/marks', methods=['POST'])
def result():
    physics_marks = int(request.form['physics'])
    chemistry_marks = int(request.form['chemistry'])
    math_marks = int(request.form['math'])

    total_marks = physics_marks + chemistry_marks + math_marks
    average_marks = total_marks / 3

    return render_template('marks.html', physics=physics_marks, chemistry=chemistry_marks, math=math_marks,
                           total=total_marks, average=average_marks)

@app.route('/task2')
def task2():
    return render_template('task2.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return render_template('login_info.html', username=username, password=password)

@app.route('/task3')
def task3():
    return render_template('task3.html')

def calculate_sum(n):
    return sum(range(1, n + 1))

@app.route('/sum', methods=['GET'])
def sum_of_numbers():
    number = int(request.args.get('number'))
    total_sum = calculate_sum(number)
    return render_template('answer.html', number=number, sum=total_sum)

@app.route('/task4')
def task4():
    return render_template('task4.html')

if __name__ == '__main__':
    app.run()
