import os, sys, logging
from flask import Flask, render_template

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/test/')
def testpage():
    return "Test page, get rekt"

if __name__ == "__main__":
    app.run()