import flask
import finfo

# from flask import redirect
from flask.templating import render_template

@finfo.app.route('/')
def show_index():
    print("printing from index.py in finfo/views")
    return render_template("index.html")