from twilio.rest import Client
from envparse import env

env.read_envfile()
account_sid = env.str('ACCOUNT_SID')
auth_token = env.str('AUTH_TOKEN')

def sendMessage(recipient, msg = "", gif = ""):
	# param: strings
	# must enter either msg or gif or both
	client = Client(account_sid, auth_token)

	if msg == "": 
		message = client.messages.create(
		        recipient,
		        from_ = "+12013477040",
		        media_url = gif)
	elif gif == "":
		message = client.messages.create(
		        recipient,
		        body = msg,
		        from_ = "+12013477040")
	else: 
		message = client.messages.create(
		        recipient,
		        body = msg,
		        from_ = "+12013477040",
		        media_url = gif)