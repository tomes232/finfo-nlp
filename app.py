import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import ask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']

    answer = ask(incoming_msg, None)
    r = MessagingResponse()
    r.message(answer)
    return str(r)