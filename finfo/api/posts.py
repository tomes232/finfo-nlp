import os
from flask import Flask, request
from werkzeug.utils import redirect
import finfo
from finfo.api.q_and_a import genAnswer, genAnswer_config, genAnswer_text
import random
import json
from flask import Flask, render_template, request, url_for
# from flask_ngrok import run_with_ngrok
from finfo.api.web_scraper import scraper
from finfo.api.classification import classification
import openai
from datetime import datetime
from finfo.mongodb import search
import time 

with open('finfo/api/config.json', 'r') as f:
    config = json.load(f)

@finfo.app.route("/", methods=["GET"])
def home():
    with open('finfo/api/config.json', 'r') as f:
        config = json.load(f)
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
    with open('finfo/api/config.json', 'r') as f:
        config = json.load(f)
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
    #edit the config
    # if config["file"] != "":
    #     openai.File.delete(file=config["file"])    
    config['file'] = response["id"]
    #write it back to the file
    with open('finfo/api/config.json', 'w') as f:
        json.dump(config, f)

    return redirect(url_for('home', data=data))

@finfo.app.route('/api/v1/bot/', methods=['POST'])
def bot():
    with open('finfo/api/config.json', 'r') as f:
        config = json.load(f)
    incoming_msg = request.form["msg"]
    print(incoming_msg)
    if config['file'] == "":
        response  = openai.File.create(file=open("sandbox.jsonl"), purpose="answers")
        #edit the config
        config['file'] = response["id"]
        #write it back to the file
        with open('finfo/api/config.json', 'w') as f:
            json.dump(config, f)
    try:
        # response = genAnswer(incoming_msg, config['file'])
        # answer = response["answers"][0]
        # print(response["selected_documents"][0]["score"])
        # if response["selected_documents"][0]["score"] < 150:
        print("time for search")
        search_documents = search('articles', 'funding', incoming_msg)
        print(search_documents)
        response = genAnswer_text(incoming_msg, search_documents)
        print(response)
        answer = response["answers"][0]

        # answer = genAnswer(incoming_msg, config["file"])["answers"][0]

    except openai.error.InvalidRequestError:
        try:
            print("time for search")
            search_documents = search('articles', 'funding', incoming_msg)
            #response = genAnswer_text(incoming_msg, search_documents)
            #print(response)
            #answer = response["answers"][0]

        except openai.error.InvalidRequestError:
            answer = "I don't have enough information to answer that question. Please try another."
    return str(answer)
