import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage(name=None):
    return render_template('main.html', name=name)

@app.route('/test/')
def testpage():
    return "Test page, get rekt"

if __name__ == "__main__":
    app.run()
