import os, sys, logging
from flask import Flask, render_template

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/main')
def homePage():

    title = "Epic Tutorials"
    paragraph = ["Wow I am learning so much great stuff! Wow I am learning so much great stuff!"]

    try:
        return render_template("main.html", title = title, paragraph=paragraph)
    except Exception, e:
        return str(e)

@app.route('/table')
def tablePage():
    return render_template('basic_table.html')

@app.route('/cal')
def calPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("calendar.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/todo')
def todoPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("todo_list.html", title=title, paragraph=paragraph, pageType=pageType)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
