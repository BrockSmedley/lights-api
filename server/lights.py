#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import requests
from flask import (
    Flask,
    render_template
)
from flask_cors import CORS

TEST = False
GPIO.setmode(GPIO.BCM)

# init list w/ pin numbers
pinList = [2,3,4,17,27,22,10,9]
pinState = 8*[GPIO.HIGH]

app = Flask(__name__, template_folder="templates")
CORS(app)

def toggle(pin):
    #...
    if (pin > 0 and pin <= 8):
        s = pinState[pin-1]
        if (s == GPIO.HIGH):
            ns = GPIO.LOW
        else:
            ns = GPIO.HIGH
        pinState[pin-1] = ns
        for s in range(len(pinState)):
            GPIO.output(pinList[s], pinState[s])
        return color(pinState)

@app.route('/')
def index():
    """
    localhost:5000/
    
    :return: rendered template 'index.html'
    """
    return render_template('index.html')

@app.route('/red')
def red():
    return toggle(4)
@app.route('/green')
def grn():
    return toggle(3)
@app.route('/blue')
def blu():
    return toggle(2)
@app.route('/power')
def pwr():
    return toggle(1)
@app.route('/status')
def state():
    return str(pinState[:4])
@app.route('/kill')
def kill():
    return killRelays()

def main():
    initRelays()
    if (TEST):
        inputLoop()
    else:
        runFlask()
    killRelays()

def runFlask():
    print("Running flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)

def color(pin_state):
    s = ""
    if (pin_state[0] == GPIO.LOW):
        s = "lights off"
    else:
        if (pin_state[3] == GPIO.LOW):
            s += "R"
        else:
            s += "_"
        if (pin_state[2] == GPIO.LOW):
            s += "G"
        else:
            s += "_"
        if (pin_state[1] == GPIO.LOW):
            s += "B"
        else:
            s += "_"
    return s


def initRelays(): 
    # loop thru pins, setting state to 'low'
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

def inputLoop():
    while (True):
        try:
            print("Enter a number 1-8: ")
            n = raw_input()
            if (n == "x" or n == "X"):
                break
            try:
                n = int(n)
            except Exception:
                continue
            if (n > 0 and n <= 8):
                s = pinState[n-1]
                if (s == GPIO.HIGH):
                    ns = GPIO.LOW
                else:
                    ns = GPIO.HIGH
                pinState[n-1] = ns
                GPIO.output(pinList[n-1], pinState[n-1])
                print(color(pinState))
        except KeyboardInterrupt:
            print ("Quit")
            #GPIO.cleanup()
            break

def killRelays():
    for p in range(len(pinState)):
        pinState[p] = GPIO.HIGH
    for i in pinList:
        GPIO.output(i, GPIO.HIGH)
    return "dead"
main()
