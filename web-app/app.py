from flask import Flask, render_template

dodo =  Flask(__name__)

@dodo.route('/')
def index():
    title = 'index'
    return render_template('index.html', title=title)

@dodo.route('/about')
def about():
    names = ['Meredith', 'Yang', 'George', 'Izzy', 'Alex']
    return render_template('about.html', names=names)

if __name__ == '__main__':
   dodo.run(debug=True)