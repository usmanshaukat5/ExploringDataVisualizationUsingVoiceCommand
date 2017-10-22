import logging

from random import randint

from flask import Flask, render_template,session

from flask_ask import Ask, statement, question, session


app = Flask(__name__)
query=""

ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)



@ask.intent("DisplayMeIsIntent")
def display_me(displayme):
    global query
    query = displayme
    return statement("Please refresh browser.")

@app.route('/')
def index():
	return query




if __name__ == '__main__':

    app.run(debug=True)