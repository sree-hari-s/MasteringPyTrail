import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_AUTH_TOKEN'])

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.environ['TWILIO_VIRTUAL_NUMBER'],
            to=os.environ['TWILIO_VERIFIED_NUMBER'],
        )
        # Prints if successfully sent.
        print(message.sid)