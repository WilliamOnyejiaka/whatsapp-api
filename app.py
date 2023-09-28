import time
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

def split_reply(assistant_reply,sender_phone_number):
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
            res = send_message(sender_phone_number, segment)
            time.sleep(2)
            print(res)
    else:
        res = send_message(sender_phone_number, assistant_reply)
        print(res)

@app.route('/whatsapp', methods=['GET', 'POST'])
def receive_message():
    incoming_message = request.values.get('Body', None)
    sender_phone_number = request.values.get('From', None)
    print(sender_phone_number)
    response_msg = chatgpt_msg(incoming_message)
    # res = send_message(sender_phone_number, response_msg)
    # print(res)
    split_reply(response_msg,sender_phone_number)
    return "200"


if __name__ == "__main__":
    app.run(debug=True)
