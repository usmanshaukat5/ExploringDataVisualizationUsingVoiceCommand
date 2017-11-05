import logging

from random import randint

from flask import Flask, render_template,session

from flask_ask import Ask, statement, question, session

import random, threading, webbrowser


app = Flask(__name__)
query=""
port=5000

ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)





@ask.intent("DisplayMeIsIntent")
def display_me(displayme):
    global query
    words = displayme.split(' ')
    for word in words:
        if word=='select':
            query=query+word+" * "
        else:
            query=query+" "+word

    global port
    url = "http://127.0.0.1:5000"
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    return statement("you speak "+query)

@app.route('/')
def index():
	return query




if __name__ == '__main__':

    app.run(port=port,debug=True)