import flask
from flask import request
from modules.send_message import send_message
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = flask.Flask(__name__)

def chatgpt_msg(user_message):
    api_key = os.environ.get("OPENAI_KEY")
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

print(chatgpt_msg("Hello"))