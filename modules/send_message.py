import os

from twilio.rest import Client

from dotenv import load_dotenv
from twilio.base.exceptions import TwilioRestException

load_dotenv()

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
FROM = 'whatsapp:+14155238886'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_message(sender_id, message):
    message_chunks = [message[i:i + 320] for i in range(0, len(message), 320)]

    # Send each chunk as a separate WhatsApp message
    for i, chunk in enumerate(message_chunks):
        # Create a WhatsApp message
        try:
            res = client.messages.create(
                body=chunk,
                from_=FROM,
                to=f'{sender_id}'
            )
            print(res)
        except TwilioRestException as e:
            print(f"Twilio Error: {e.code} - {e.msg}")


def send_messageq(sender_id, message):
    try:
        res = client.messages.create(
            body=message,
            from_=FROM,
            # to=f'whatsapp:+{sender_id}'
            to=f'{sender_id}'
        )
        return res

    except TwilioRestException as e:
        print(f"Twilio Error: {e.code} - {e.msg}")
