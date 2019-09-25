import RPi.GPIO as GPIO
import time

TEST = False
# init list w/ pin numbers
pinList = [2,3,4,17,27,22,10,9]
initPinState = 8*[GPIO.HIGH]

def init():
    print("initiating lights library...")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    initRelays()

def pinState(pin):
    # TODO: fetch state from redis
    return 8*[GPIO.HIGH]

def setPinState(pin, state):
    # TODO: set state in redis
    print(pin, state)

def arrayState():
    # TODO: get states 0-7 from redis and compile into a list
    return 8*[GPIO.HIGH]

def toggle(pin):
    if (pin > 0 and pin < len(pinList)):
        s = pinState(pin)
        if (s == GPIO.HIGH):
            ns = GPIO.LOW
        else:
            ns = GPIO.HIGH
        setPinState(pin, ns)

        # push new GPIO state list
        for s in range(len(arrayState())):
            GPIO.output(pinList[s], arrayState()[s])

        return arrayState()

#def main():
#    initRelays()
#    if (TEST):
#        inputLoop()

def runFlask():
    print("Running flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)

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

#main()
