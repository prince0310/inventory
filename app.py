from flask_mysqldb import MySQL
from flask import Flask, render_template, Response, request, redirect, url_for
from video import generate_frames
from main import index
from urls import login, register

app = Flask(__name__)
# congiure db
app.config['MYSQL_HOST'] = 'localhost'  # db['mysql_host']
app.config['MYSQL_USER'] = 'root'  # db['mysql_user']
app.config['MYSQL_PASSWORD'] = '123456'  # db['mysql_password']
app.config['MYSQL_DB'] = 'flaskapp'  # db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def start():
    return login()


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/main', methods=['GET', 'POST'])
def load():
    return index()

@app.route('/registration', methods=['GET', 'POST'])
def regi():
    return register()

# main driver function
if __name__ == "__main__":
    app.run(debug=True)
