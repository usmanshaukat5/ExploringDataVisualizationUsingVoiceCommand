from __future__ import print_function
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
    query=""
    words = displayme.split(' ')
    for word in words:
        if word=='select':
            query=query+word+" * "
        else:
            query=query+" "+word
    try:
        cur = mysql.connection.cursor()
        cur.execute(query)
        wishes = cur.fetchall()
        global port
        url = "http://127.0.0.1:5000"
        threading.Timer(1.25, lambda: webbrowser.open(url)).start()
        return statement("")
    except:
        global port
        url = "http://127.0.0.1:5000"
        threading.Timer(1.25, lambda: webbrowser.open(url)).start()
        return statement("Invalid Query! Data not Found. Please Speak Correctly.")







@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute(query)

        wishes = cur.fetchall()
        wishes_dict = []
        for wish in wishes:
            wish_dict = {'name': wish[1], 'population': wish[2]}
            wishes_dict.append(wish_dict)
        dataa = json.dumps(wishes_dict)
        words = query.split(' ')
        for word in words:
            temp=word

        return render_template("index.html", dataa=dataa, temp=temp)
    except Exception as e:
         return render_template("MySqlError.html", e=e)







if __name__ == '__main__':
	app.run(port=port,debug=True)