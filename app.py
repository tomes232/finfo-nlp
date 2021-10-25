import os
from flask import Flask, request
from q_and_a import genAnswer
import random
import json
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'top-secret!'

@app.route("/")
def home():
    print("I")
    return render_template("index.html")

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.form["msg"]
    answer = genAnswer(incoming_msg, "file-QRZKYePIEhaQGkjS8ajlzPXJ")["answers"][0]
    return str(answer)
