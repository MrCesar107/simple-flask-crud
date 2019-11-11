from flask import Flask, request, redirect, render_template
import sys

sys.path.insert(1, "PATH TO LOCAL PYTHON PACKAGES")
sys.path.insert(2, "PATH TO FLASK DIRECTORY")

app = Flask(__name__)

@app.route('/')
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'SELECT * FROM data_table'
    return render_template('sqldatabase.html', results=results, msg=msg)

@app.route('/insert', methods = ['POST', 'GET'])
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        sql_edit_insert(''' INSERT INTO data_table (first_name, last_name, address, city, state, zip) VALUES (?, ?, ?, ?, ? , ?) ''', (first_name, last_name, address, city, state, zip) )
    results = sql_query(''' SELECT * FROM data_table ''')
    msg = 'INSERT INTO data_table (first_name, last_name, address, city, state, zip) VALUES ('+first_name+', '+last_name+', '+address+', '+city+', '+state+', '+zip+')'
    return render_template('templates/sqldatabase.html', results=results, msg=msg)

@app.route('/delete', methods = ['POST', 'GET'])
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM data_table where first_name = ? and last_name = ? ''', (fname,lname))
    results = sql_query(''' SELECT * FROM data_table ''')
    msg = 'DELETE FROM data_table WHERE first_name = ' + fname + ' and last_name = ' + lname
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)