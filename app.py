# imports Flask and create an instance of the Flask object
from flask import Flask
# __name__ is a built-in variable which evaluates to the name of the current module
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

""" 
    if we want to use a different filename than app.py
    such as program.py, we should define an environment
    variable named FLASK_APP and set its value to our chosen
    file. Flask development server than uses the value of 
    FLASK_APP instead of the default file app.py. 
"""
