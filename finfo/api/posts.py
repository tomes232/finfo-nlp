import os
from flask import Flask, request
import finfo
from finfo.api.q_and_a import genAnswer
import random
import json
from flask import Flask, render_template, request
# from flask_ngrok import run_with_ngrok
import openai

@finfo.app.route("/api/v1/kosi/", methods=["GET"])
def home():
    print("kosineh")
    return render_template("index.html")

@finfo.app.route('/api/v1/bot/', methods=['POST'])
def bot():
    incoming_msg = request.form["msg"]
    try:
        answer = genAnswer(incoming_msg, "file-QRZKYePIEhaQGkjS8ajlzPXJ")["answers"][0]
    except openai.error.InvalidRequestError:
        answer = "I don't have enough information to answer that question. Please try another."
    return str(answer)
