import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from twilio.rest import TwilioRestClient

account_sid = os.environ['TWILIO_SID']
auth_token  = os.environ['TWILIO_TOKEN']

client = TwilioRestClient(account_sid, auth_token)

def send_text(message, number):
	try:
		message = client.messages.create(body=message,
		    to=number,
		    from_="+16474962879") 
		print(message.sid)
	except TwilioRestException as e:
	    print(e)