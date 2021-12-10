import flask
import finfo

# from flask import redirect
from flask.templating import render_template

@finfo.app.route('/')
def show_index():
    print("asfasdffasfjksadfh")
    return render_template("index.html")