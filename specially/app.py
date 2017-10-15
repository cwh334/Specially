from twilio.rest import Client

def sendMessage(receiver, msg = "", gif = ""):
	# param: strings
	# must enter either msg or gif or both
	account_sid = "ACf87efe442272782a8258dbd82860db7f"
	auth_token = "7d2a87a82cdcbb18ef4d478ecaff4bb8"
	client = Client(account_sid, auth_token)

	if msg == "": 
		message = client.messages.create(
		        receiver,
		        from_ = "+12013477040",
		        media_url = gif)
	elif gif == "":
		message = client.messages.create(
		        receiver,
		        body = msg,
		        from_ = "+12013477040")
	else: 
		message = client.messages.create(
		        receiver,
		        body = msg,
		        from_ = "+12013477040",
		        media_url = gif)

# sendMessage("+17186002718", "testing function")