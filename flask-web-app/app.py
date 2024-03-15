from flask import Flask,render_template

app = Flask(__name__)
app.debug = True

posts = [
    {
        'author': 'John Doe',
        'title': 'Post-1',
        'content': 'Hey there, just checking out this local app',
        'date_posted': 'April 29, 2022'
     },
    {
        'author': 'John Doe',
        'title': 'Post-2',
        'content': 'Hey there, just checking out bug fixes',
        'date_posted': 'May 5, 2022'
     }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run()
