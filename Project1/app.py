from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = None


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    global df
    if request.method == 'POST':
        file = request.files['file']

        if file.filename == '':
            return render_template('home.html', error='No file selected')

        try:
            df = pd.read_csv(file)
            if not df.empty:
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
    global df
    if df is not None:
        columns = df.columns.tolist()
        return render_template('clean.html', columns=columns)
    else:
        return '<script>alert("DataFrame is not available");window.history.back();</script>'
    # return render_template('clean.html')


@app.route('/isnan')
def isnan():
    global df
    if 'df' is not None:
        
        na_rows = df[df.isna().any(axis=1)].to_html()
        
        na_columns = df.columns[df.isna().any()].tolist()
        return render_template('na_info.html', na_rows=na_rows, na_columns=na_columns)

    else:
        return '<script>alert("DataFrame is not available);window.history.back();</script>'


@app.route('/drop',methods=['GET', 'POST'])
def drop():
    global df
    if request.method == 'POST':
        selected_columns = request.form.getlist('selectedColumns')
        if not selected_columns:
            return 'No columns selected'
        
        if df is not None:
            df.drop(columns=selected_columns, inplace=True)
            new_df_head = df.head().to_html()
            return render_template('new_df.html', new_df_head=new_df_head)
        else:
            return '<script>alert("DataFrame is not available");window.history.back();</script>'
    else:
        return 'Method Not Allowed'



@app.route('/visualize')
def visualize():
    return render_template('visualize.html')


if __name__ == '__main__':
    app.run(debug=True)
