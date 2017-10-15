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
	# import psycopg2
	from datetime import datetime as dt

	cgitb.enable()

	result +=  ("Content-Type: text/html\r\n\r\n")
	result +=  ( "<html>\n<head>")
	result +=  ( "<title>appointment database</title>")
	result +=  ('<link rel="stylesheet" href="style.css">')
	result += ("</head>")
	result +=  ( "<body>")

	# Create instance of FieldStorage 
	form = cgi.FieldStorage()

	number = request.form['phone']
	datetime = request.form['sendTime']
	occasion = ""
	message = ""
	giphyurl = ""
	if request.form['occasion']:
		occasion = request.form['occasion']
	if request.form['msgbox']:
		message = request.form['msgbox']
	if request.form['url']:
		giphyurl = request.form['url']

	result += ','.join([number, datetime, occasion, message, giphyurl])


	result += ("</body>")
	result += ("</html>")
	return result