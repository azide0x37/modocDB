import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/test/')
def testpage():
    return "Test page, get rekt"

if __name__ == "__main__":
    app.run(host='0.0.0.0')