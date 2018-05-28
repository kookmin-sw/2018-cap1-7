import RPi.GPIO as GPIO
import time

#system control
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(18, GPIO.IN)

#show instrunction
instruction = "Press white or yellow button"
os.system('sudo ./oled 1 %s' %instruction)

while True :
    value_stt = GPIO.input(14)
    value_sound = GPIO.input(18)
    print ("value is ", value_stt, "value_sound is", value_sound)
    if value_stt == False :
        instruction = 'white button is pressed'
        os.system('sudo ./oled 1 %s' %instruction)
        os.system('python transcribe_streaming_mic_gaeul.py')
    if value_sound == False :
        instruction = 'yellow button is pressed'
        os.system('sudo ./oled 1 %s' %instruction)
        os.system('python ../mfcc/main.py')
    time.sleep(0.1)
