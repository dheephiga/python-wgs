from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']

        if file.filename == '':
            return render_template('home.html', error='No file selected')

        try:
            df = pd.read_csv(file)
            if not df.empty:
                # Pass column names and row data to the template
                df_head = df.head()
                column_names = df_head.columns.values
                row_data = list(df_head.values.tolist())
                return render_template('home.html', column_names=column_names, row_data=row_data, zip=zip)
            else:
                return render_template('home.html', error='Uploaded file is empty or invalid')
        except Exception as e:
            return render_template('home.html', error='Error reading file: ' + str(e))
    else:
        return render_template('home.html')


@app.route('/clean')
def clean():
    return render_template('clean.html')


@app.route('/visualize')
def visualize():
    return render_template('visualize.html')


if __name__ == '__main__':
    app.run()
