from app import app
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
	result = ''
	import cgi, cgitb
	from datetime import datetime as dt
	from threading import Timer
	from twilio.rest import Client
	from envparse import env

	cgitb.enable()

	result +=  ("Content-Type: text/html\r\n\r\n")
	result +=  ( "<html>\n<head>")
	result +=  ( "<title>appointment database</title>")
	result +=  ('<link rel="stylesheet" href="style.css">')
	result += ("</head>")
	result +=  ( "<body>")

	number = request.form['phone']
	datetime = request.form['sendTime']
	datetime = dt.strptime(datetime, '%Y-%m-%dT%H:%M')
	occasion = ""
	message = ""
	giphyurl = ""
	if request.form['occasion']:
		occasion = request.form['occasion']
	if request.form['msgbox']:
		message = request.form['msgbox']
	if request.form['url']:
		giphyurl = request.form['url']


	env.read_envfile()
	account_sid = env.str('ACCOUNT_SID')
	auth_token = env.str('AUTH_TOKEN')

	result += ','.join([number, str(datetime), occasion, message, giphyurl])

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


	result += ("</body>")
	result += ("</html>")
	return result







print("</body>")