#!/usr/local/bin/python3
import cgi
import cgitb

cgitb.enable()

print ("Content-Type: text/html\r\n\r\n")
print ( "<html>\n<head>")
print ( "<title>sqlite selection</title>")
print ('<link rel="stylesheet" href="style.css">')
print("</head>")
print ( "<body>")


form = cgi.FieldStorage()

sendTime = form.getvalue('sendTime')
print(sendTime)
phone = form.getvalue('phone')
print(phone)
msgbox = form.getvalue('msgbox')
print(msgbox)
url = form.getvalue('url')
print(url)

print("<p>Your message will be sent on 2017/10/15</p>")

print("</body>")
print("</html>")