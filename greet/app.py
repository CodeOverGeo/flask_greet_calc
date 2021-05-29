from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """returns welcome string for url endpoint of welcome"""
    return 'welcome'

@app.route('/welcome/home')
def home():
    """returns welcome home string for url endpoint of welcome/home"""
    return 'welcome home'

@app.route('/welcome/back')
def back():
    """returns welcome back string for url endpoint of welcome/back"""
    return 'welcome back'