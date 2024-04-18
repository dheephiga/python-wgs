from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = [{'todo': 'code', 'done': False}]


@app.route('/')
def index():
    return render_template('index.html',todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'todo':todo, 'done':False})
    return redirect(url_for('index'))

def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['todo'] = request.formt['todo']
        return redirect(url_for('index'))
    else:
        render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)