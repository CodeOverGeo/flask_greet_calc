# Web app to do a math operation depending on url enpoints

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

math_oper = {
    'add' : add,
    'sub' : sub,
    'div' : div,
    'mult' : mult
}

@app.route('/add')
def web_add():
    """returns addition of 2 passed query strings"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))

@app.route('/sub')
def web_sub():
    """returns subtraction of 2 passed query strings"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.route('/mult')
def web_mult():
    """returns multiplication of 2 passed query strings"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.route('/div')
def web_div():
    """returns division of 2 passed query strings"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))

@app.route('/math/<oper>')
def math(oper):
    """returns result of query strings using passed operation depending on url endpoint"""
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    result = math_oper[oper](a,b)
    return str(result)