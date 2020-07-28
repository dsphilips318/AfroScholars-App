# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/languages')
def languages():
    return render_template('languages.html')


@app.route('/yoruba-demo')
def yoruba_demo():
    return render_template('yoruba-demo.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')


@app.route('/log-in')
def log_in():
    return render_template('log-in.html')
