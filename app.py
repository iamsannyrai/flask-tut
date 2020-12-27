# imports Flask and create an instance of the Flask object
from flask import Flask
from flask import render_template # render_template helps to load a template
from datetime import datetime

# __name__ is a built-in variable which evaluates to the name of the current module
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_there(name = None):
    return render_template(
        'hello_there.html',
        name=name,
        date=datetime.now()
    )

""" 
    if we want to use a different filename than app.py
    such as program.py, we should define an environment
    variable named FLASK_APP and set its value to our chosen
    file. Flask development server than uses the value of 
    FLASK_APP instead of the default file app.py. 
"""
