import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.intent("DisplayMeIsIntent")
def my_name_is(firstname):
    msg="My name is {}".format(firstname)
    return statement(msg)




if __name__ == '__main__':

    app.run(debug=True)