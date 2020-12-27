# imports Flask and create an instance of the Flask object
from flask import Flask
from flask import render_template # render_template helps to load a template
from datetime import datetime

# __name__ is a built-in variable which evaluates to the name of the current module
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_there(name = None):
    return render_template(
        'hello_there.html',
        name=name,
        date=datetime.now()
    )

@app.route('/api/data')
def get_data():
    return app.send_static_file("data.json") # send static files from static folder

""" 
    if we want to use a different filename than app.py
    such as program.py, we should define an environment
    variable named FLASK_APP and set its value to our chosen
    file. Flask development server than uses the value of 
    FLASK_APP instead of the default file app.py. 
"""
