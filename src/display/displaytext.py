import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN)
count = 0
while True :
    value = GPIO.input(15)
    print ("value is ", value)
    if value == False :
        count = count + 1
        print count
    time.sleep(0.1)
