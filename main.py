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

def split_reply(assistant_reply):
    message_length = len(assistant_reply)
    segment_length = 320

    if message_length > segment_length:
        num_segments = (message_length + segment_length - 1) // segment_length  # Use integer division
        message_segments = []

        for i in range(num_segments):
            start = i * segment_length
            end = (i + 1) * segment_length
            segment = assistant_reply[start:end]
            message_segments.append(segment)
        
        for segment in message_segments:
            print(f'{segment} \n')
    else:
        print(assistant_reply)






assistant_reply = chatgpt_msg("Python automation project ideas, in more than 500 words")

split_reply(assistant_reply)




# print(chatgpt_msg("Hello"))