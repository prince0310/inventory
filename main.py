from flask import Flask, render_template, request
from qrcode import data
from model import config


app = Flask(__name__)

mysql = config()
def value():
    temp = [i for i in data()]
    if len(temp[0]) > 0:
        return  temp
    else:
        return [['xx, yy, zz, ww']]

def index():
    val = value()
    if request.method == 'POST':
        if request.form.get('action1') == 'INSERT':
            userDetails = request.form
            Product = userDetails['Product ID']
            Origin = userDetails['Origin']
            Current = userDetails['Current']
            Destination = userDetails['Destination']
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO inventory(Product_ID, Origin,Current,Destination) VALUES(%s,%s,%s,%s)',
                        (Product, Origin, Current, Destination))
            mysql.connection.commit()
            cur.close()
            return render_template('index.html', out=val)
        if request.form.get('action2') == 'DELETE':
            userDetails = request.form
            Product = userDetails['Product ID']
            # Origin = userDetails['Origin']
            # Current = userDetails['Current']
            # Destination = userDetails['Destination']
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM inventory WHERE Product_ID = %s', [Product])
            mysql.connection.commit()
            cur.close()
            return render_template('index.html', out=val)
        if request.form.get('action3') == 'UPDATE':
            userDetails = request.form
            Product = userDetails['Product ID']
            # Origin = userDetails['Origin']
            Current = userDetails['Current']
            # Destination = userDetails['Destination']
            cur = mysql.connection.cursor()
            cur.execute("UPDATE inventory SET Current = %s WHERE Product_ID = %s", (Current, Product))
            mysql.connection.commit()
            cur.close()
            return render_template('index.html', out=val)
        if request.form.get('action4') == 'FETCH':
            userDetails = request.form
            Product = userDetails['Product ID']
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM inventory WHERE Product_ID = %s', (Product))
            output = cur.fetchall()
            return render_template('index.html', output=output, out=val)
    return render_template('index.html', out=val)