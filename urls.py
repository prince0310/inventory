from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from main import value
import re

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'  # db['mysql_host']
app.config['MYSQL_USER'] = 'root'  # db['mysql_user']
app.config['MYSQL_PASSWORD'] = '123456'  # db['mysql_password']
app.config['MYSQL_DB'] = 'flaskapp'  # db['mysql_db']


mysql = MySQL(app)


def register():
    msg = ''
    if request.method == 'POST' and request.form.get('reg') == 'Sign Up':
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM credentials WHERE email = % s', (email,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', email):
            msg = 'Username must contain only characters and numbers !'
        elif not email or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO credentials VALUES (% s, % s)', (email, password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('registration.html', msg=msg)

def login():
    val = value()
    msg = ''
    if request.method == 'POST' and request.form.get('login') == 'c':
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM credentials WHERE email = % s', (email,))
        account = cursor.fetchone()
        if account:
            if password == account['password']:
                msg = 'Logged in successfully !'
                return render_template("index.html", out = val)
            else:
                msg = 'Incorrect email / password !'
        else:
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg = msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))



