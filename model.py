from flask_mysqldb import MySQL
from flask import Flask, render_template, Response, request,redirect,url_for

def config():
    # congiure db
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'sql309.epizy.com'  # db['mysql_host']
    app.config['MYSQL_USER'] = 'epiz_33509789'  # db['mysql_user']
    app.config['MYSQL_PASSWORD'] = 'PoNjOIc1d2'  # db['mysql_password']
    app.config['MYSQL_DB'] = 'epiz_33509789_inventory'  # db['mysql_db']
    mysql = MySQL(app)
    return  mysql

def login_config():
    # congiure db
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'sql309.epizy.com'  # db['mysql_host']
    app.config['MYSQL_USER'] = 'epiz_33509789'  # db['mysql_user']
    app.config['MYSQL_PASSWORD'] = '123456'  # db['mysql_password']
    app.config['MYSQL_DB'] = 'epiz_33509789_inventory'  # db['mysql_db']
    mysql_login = MySQL(app)
    return  mysql_login
