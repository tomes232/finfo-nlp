import os
from flask import Flask, request
from werkzeug.utils import redirect
import finfo
from finfo.api.q_and_a import genAnswer
import random
import json
from flask import Flask, render_template, request, url_for
# from flask_ngrok import run_with_ngrok
from finfo.api.web_scraper import scraper
import openai
from datetime import datetime

@finfo.app.route("/", methods=["GET"])
def home():
    print("blah")
    with open("time.txt", "r") as f:
        readtime = f.readline().rstrip()
        currtime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    data = [
        {
            "read": readtime,
            "curr": currtime
        }
    ]
    return render_template("index.html", data=data)

@finfo.app.route("/api/v1/scrape/", methods=["POST"])
def scrape():
    
    with open("time.txt", "w") as f:
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        f.write(time)
    data = [
        {
            "read": time,
            "curr": time
        }
    ]
    scraper()
    return redirect(url_for('home', data=data))

@finfo.app.route('/api/v1/bot/', methods=['POST'])
def bot():
    incoming_msg = request.form["msg"]
    try:
        answer = genAnswer(incoming_msg, "file-QRZKYePIEhaQGkjS8ajlzPXJ")["answers"][0]
    except openai.error.InvalidRequestError:
        answer = "I don't have enough information to answer that question. Please try another."
    return str(answer)
