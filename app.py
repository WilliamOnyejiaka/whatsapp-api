import flask
from flask import request
from modules.send_message import send_message
import openai

app = flask.Flask(__name__)

def chatgpt_msg(user_message):
    api_key = "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"
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply


@app.route('/whatsapp', methods=['GET', 'POST'])
def receive_message():
    incoming_message = request.values.get('Body', None)
    sender_phone_number = request.values.get('From', None)
    print(sender_phone_number)
    response_msg = chatgpt_msg(incoming_message)
    res = send_message(sender_phone_number, response_msg)
    print(res)
    return "200"


if __name__ == "__main__":
    app.run(debug=True)
