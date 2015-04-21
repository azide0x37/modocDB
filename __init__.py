import os, sys, logging
from flask import Flask, render_template

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def indexPage():
    title = "modocDB Offender Search"
    table_data = {'name': "Duck, Donald",
                  'docId': 512073,
                  'assignedLocation': "ERDCC"}
    try:
        return render_template('basic_table.html', title = title, table_data = offenderDB)
    except Exception, e:
        return str(e)
    
@app.route('/main')
@app.route('/main.html')
def homePage():

    title = "Epic Tutorials"
    paragraph = ["Wow I am learning so much great stuff! Wow I am learning so much great stuff!"]

    try:
        return render_template("main.html", title = title, paragraph = paragraph)
    except Exception, e:
        return str(e)

@app.route('/basic_table')
@app.route('/basic_table.html')
def tablePage():
    return render_template('basic_table.html')

@app.route('/cal')
@app.route('/calendar.html')
def calPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("calendar.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/todo')
@app.route('/todo_list.html')
def todoPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("todo_list.html", title=title, paragraph=paragraph, pageType=pageType)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
