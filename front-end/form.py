#!/usr/local/bin/python3

import cgi, cgitb
import psycopg2
from datetime import datetime as dt
from threading import Timer
from twilio.rest import Client
from envparse import env

cgitb.enable()

print ("Content-Type: text/html\r\n\r\n")
print ( "<html>\n<head>")
print ( "<title>appointment database</title>")
print ('<link rel="stylesheet" href="style.css">')
print("</head>")
print ( "<body>")

# Create instance of FieldStorage 
form = cgi.FieldStorage()

number = form.getvalue('phone')
datetime = form.getvalue('sendTime')
datetime = dt.strptime(datetime, '%Y-%m-%dT%H:%M')
occasion = ""
message = ""
giphyurl = ""
if form.getvalue('occasion'):
	occasion = form.getvalue('occasion')
if form.getvalue('msgbox'):
	message = form.getvalue('msgbox')
if form.getvalue('gif_url'):
	giphyurl = form.getvalue('gif_url')

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

x = dt.today()
y = datetime
delta_t = y - x
secs = delta_t.seconds + 1

timer = Timer(secs, sendMessage, [number, message, giphyurl])
timer.start()

print("</body>")
print("</html>")