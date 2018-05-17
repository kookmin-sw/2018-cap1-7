import RPi.GPIO as GPIO
import time

#system control
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN)
count = 0
while True :
    value = GPIO.input(15)
    print ("value is ", value)
    if value == False :
        os.system('python transcribe_streaming_mic_gaeul.py')
        count = count + 1
        print count
    time.sleep(0.1)
