import os
from flask import Flask, request
from werkzeug.utils import redirect
import finfo
from finfo.api.q_and_a import genAnswer, genAnswer_config
import random
import json
from flask import Flask, render_template, request, url_for
# from flask_ngrok import run_with_ngrok
from finfo.api.web_scraper import scraper
from finfo.api.classification import classification
import openai
from datetime import datetime

file = ""

@finfo.app.route("/", methods=["GET"])
def home():
    print("blah")
    with open("time.txt", "r") as f: 
        """
        need to use txt file for the last scraped because 
        what happens is when we kill the project in our 
        terminals all the time initializations reset on launch
        so by writing the last-scraped time to the txt which doesnt
        change on relaunch we can keep it as a "constant variable"
        """
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
    #upload file to gpt-3 
    
    response  = openai.File.create(file=open("sandbox.jsonl"), purpose="answers")
    print(response)
    file = response["id"]

    return redirect(url_for('home', data=data))

@finfo.app.route('/api/v1/bot/', methods=['POST'])
def bot():
    incoming_msg = request.form["msg"]
    classifier = classification(incoming_msg)
    print(classifier)
    try:
        answer = genAnswer_config(incoming_msg, file, classification(incoming_msg))["answers"][0]
    except openai.error.InvalidRequestError:
        answer = "I don't have enough information to answer that question. Please try another."
    return str(answer)
