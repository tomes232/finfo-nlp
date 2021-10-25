import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from q_and_a import genAnswer
import random
import json
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

@app.route("/")
def home():
    print("I")
    return render_template("index.html")

@app.route('/bot', methods=['POST'])
def bot():
    print("like")
    incoming_msg = request.form["msg"]
    print(incoming_msg)
    print(type(incoming_msg))
    answer = genAnswer(incoming_msg, "file-QRZKYePIEhaQGkjS8ajlzPXJ")["answers"][0]
    print("big Butts")
    r = MessagingResponse()
    r.message(answer)
    print(str(r))
    return str(r)