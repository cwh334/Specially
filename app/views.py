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

	result +=  ( "<html>\n<head>")
	result +=  ( "<title>appointment database</title>")
	result += ('<link href="https://fonts.googleapis.com/css?family=Bevan|Righteous" rel="stylesheet">')
	result +=  ('<link rel="stylesheet" href="static/css/thankyou.css">')

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

	# result += ','.join([number, str(datetime), occasion, message, giphyurl])
	result += ('<div id="label"><h1>SPECIAL.LY</h1><div><label>Thank You !!!!</label><br><label>We will send it to your beloved ONE !!!</label><br></div></div><div id="footer"><footer>Copyright &copy; HackNY Fall 2017</footer><br></div>')

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
