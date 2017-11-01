from flask import Flask, render_template,json,jsonify
from flask.ext.mysqldb import MySQL
from flask_ask import Ask, statement, question
import logging
from random import randint
import random, threading, webbrowser

app = Flask(__name__)
query=""
port=5000

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent("DisplayMeIsIntent")
def display_me(displayme):
    global query
    query = displayme
    global port
    url = "http://127.0.0.1:5000"
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    return statement("you speek "+displayme)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute(query)
	wishes = cur.fetchall()
	wishes_dict = []
	for wish in wishes:
		wish_dict = {'name': wish[1],'population': wish[2]}
		wishes_dict.append(wish_dict)
	dataa=json.dumps(wishes_dict)
	return render_template("index.html",dataa=dataa)

if __name__ == '__main__':
	app.run(port=port,debug=True)
