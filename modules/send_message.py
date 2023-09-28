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
