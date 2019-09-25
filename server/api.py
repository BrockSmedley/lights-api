#!/usr/bin/python
import requests
from flask import (
    Flask,
    render_template
)
from flask_cors import CORS
from lights import toggle, init as initLights

app = Flask(__name__, template_folder="templates")
CORS(app)
initLights()

@app.route('/')
def index():
    """
    localhost:5000/

    :return: rendered template 'index.html'
    """
    return render_template('index.html')

@app.route('/0/<id>')
def relay0(id):
    return str(toggle(0))

@app.route('/1')
def relay1():
    return str(toggle(1))

@app.route('/2')
def relay2():
    return toggle(2)

@app.route('/3')
def relay3():
    return toggle(3)

@app.route('/4')
def relay4():
    return toggle(4)

@app.route('/5')
def relay5():
    return toggle(5)

@app.route('/6')
def relay6():
    return toggle(6)

@app.route('/7')
def relay7():
    return toggle(7)

@app.route('/status')
def state():
    return str(pinState)

@app.route('/kill')
def kill():
    return killRelays()

def main():
    print("Running flask on port 5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

main()
