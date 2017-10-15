#!/usr/local/bin/python3

import cgi, cgitb
import psycopg2
from datetime import datetime as dt

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
occasion = ""
message = ""
giphyurl = ""
if form.getvalue('occasion'):
	occasion = form.getvalue('occasion')
if form.getvalue('msgbox'):
	message = form.getvalue('msgbox')
if form.getvalue('gif_url'):
	giphyurl = form.getvalue('gif_url')

date_obj = dt.strptime(datetime, '%Y-%m-%dT%H:%M')
datetime = date_obj

hostname = 'localhost'
username = 'alice'
password = ''
database = 'specially'

def doQuery(conn):
	cur = conn.cursor()
	string = "(" + number + ", " + datetime + ", " + occasion + ", " + message + ", " + giphyurl + ")"
	cur.execute( "INSERT INTO specially (number, datetime, occasion, message, giphyurl) VALUES" + string)
	print(string)

connection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( connection )
connection.close()

print("</body>")
print("</html>")