from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import InputRequired
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class InputForm(FlaskForm):
    numbers = TextAreaField('Numbers', validators=[InputRequired(message='Please enter numbers')])
    submit = SubmitField('Calculate')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    num = None
    mean = None
    std = None
    if form.validate_on_submit():
        try:
            num = np.array(form.numbers.data.split(), dtype=float)
            std = np.std(num)
            mean = np.mean(num)
        except ValueError:
            flash('Please enter valid numbers', 'error')
            return redirect(url_for('index'))
    return render_template('index.html', form=form, num=num, mean=mean, std=std)

if __name__ == "__main__":
    app.run(debug=True)
