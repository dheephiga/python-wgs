from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import InputRequired, ValidationError
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class InputForm(FlaskForm):
    numbers = TextAreaField('Numbers', validators=[
        InputRequired(message='Please enter numbers'),
    ])
    submit = SubmitField('Calculate')

    def validate_numbers(form, field):
        try:
            # Split the input by any whitespace character and convert each part to float
            numbers = [float(x) for x in field.data.split()]
        except ValueError:
            raise ValidationError('Please enter valid numbers')

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
