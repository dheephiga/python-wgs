from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import InputRequired, ValidationError
import numpy as np
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def validate_numbers(form, field):
        try:
            numbers = [float(x) for x in re.split(r',|\s+', field.data)]
        except ValueError:
            raise ValidationError('Please enter valid numbers')
        
class InputForm(FlaskForm):
    numbers = TextAreaField('Numbers', validators=[
        InputRequired(message='Please enter numbers'),validate_numbers
    ])
    submit = SubmitField('Calculate')

    

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    num = None
    mean = None
    std = None

    if form.validate_on_submit():
        try:
            num = np.array([float(x) for x in form.numbers.data.split()], dtype=float)
            std = np.std(num)
            mean = np.mean(num)
            print("Mean:", mean)
            print("Standard Deviation:", std)
        except ValueError:
            flash('Please enter valid numbers', 'error')
            return redirect(url_for('index'))

    return render_template('index.html', form=form, num=num, mean=mean, std=std)


if __name__ == "__main__":
    app.run(debug=True)