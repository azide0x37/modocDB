import os, sys, logging,
import docScraper from scraper
from flask import Flask, render_template

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

dataSet = docScraper() 

@app.route('/')
@app.route('/index.html')
def indexPage():
    title = "MO Offender Search"
    table_data = dataSet.get()
    
    try:
        return render_template('basic_table.html', title = title, table_data = table_data)
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

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
