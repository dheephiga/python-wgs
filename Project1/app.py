from flask import Flask, render_template, request, send_file
import pandas as pd
import io

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
        
        na_rows = df[df.isna().any(axis=1)].to_html(classes='table table-stripped')
        
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
            return '<script>alert("No columns selected");window.history.back();</script>'
        
        if df is not None:
            df.drop(columns=selected_columns, inplace=True)
            new_df_head = df.head().to_html(classes='table table-stripped')
            return render_template('new_df.html', new_df_head=new_df_head)
        else:
            return '<script>alert("DataFrame is not available");window.history.back();</script>'
    else:
        return '<script>alert("Method not allowed");window.history.back();</script>'

@app.route('/rename',methods=['GET', 'POST'])
def rename():
    global df
    new_column_names = {}
    for index, column in enumerate(df.columns):
        new_name = request.form.get(f'renameColumn{index+1}')
        original_name = request.form.get(f'original_column_{index+1}')
        if new_name and new_name != original_name:
            new_column_names[original_name] = new_name
    
    if new_column_names:
        df.rename(columns=new_column_names, inplace=True)
        rename_df = df.head().to_html(classes='table table-stripped')
        return render_template('new_df.html', new_df_head=rename_df)
        # return 'Columns renamed successfully'
    else:
        return '<script>alert("No columns renamed");window.history.back();</script>'

    
@app.route('/reset_index',methods=['POST'])
def reset_index():
    global df
    new_index_name = request.form.get("newIndex")
    # newdf = df.reset_index(new_index_name,drop=False, inplace=True)
    newdf = df.set_index(new_index_name, inplace=True)
    newdf = df.head().to_html(classes='table table-stripped')
    
    return render_template('new_df.html', new_df_head=newdf)
    
    # return 'Index reset successfully'
    
@app.route('/sort',methods=['GET','POST'])
def sortdf():
    global df
    colName = request.form.get("sortCol")
    boolValue = request.form.get("sortOrder")
    if boolValue=="ascending":
        boolValue = True
    else:
        boolValue = False
        
    sort_df = df.sort_values(by=colName,ascending=boolValue)
    sort_df = df.to_html(classes='table table-stripped')

    return render_template('new_df.html', new_df_head=sort_df)

@app.route('/info')
def info():# Assuming df is your DataFrame
    global df
    if df is not None:
        # Capture info summary in a buffer
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_summary = buffer.getvalue()

        # Write info summary into an HTML file
        with open("df_info.html", "w", encoding="utf-8") as f:
            f.write(info_summary)
        
        describe_summary = df.describe().to_html(classes='table table-stripped')
        return render_template('df_info.html', info_summary=info_summary,describe_summary=describe_summary)
    else:
        return '<script>alert("No dataframe available");window.history.back();</script>'

@app.route('/save')
def save():
    global df
    df.to_csv(f'modified_file.csv', index=False)
    try:
        return send_file(f'modified_file.csv', as_attachment=True)
    except Exception as e:
        # return render_template('error.html', error=f'Error downloading CSV file: {str(e)}')
        return '<script>alert("Error downloading CSV file");window.history.back();</script>'
     
@app.route('/visualize')
def visualize():
    if df is not None:
        columns = df.columns.tolist()
        return render_template('visualize.html', columns=columns)
    else:
        return '<script>alert("DataFrame is not available");window.history.back();</script>'
    # return render_template('visualize.html')



if __name__ == '__main__':
    app.run(debug=True)
