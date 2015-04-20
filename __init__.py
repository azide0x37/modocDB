<<<<<<< HEAD
import os, sys, logging
from flask import Flask, render_template

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def homepage(table_data = None):
    return render_template('main.html', table_data='http://wenzhixin.net.cn/p/bootstrap-table/docs/data1.json')

@app.route('/test/')
def testpage():
    return "Test page, get rekt"

if __name__ == "__main__":
    app.run()
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()
>>>>>>> 757cadd3d02be56cb11b56e79499d1fb77f2390e
