import RPi.GPIO as GPIO
import time

#system control
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(18, GPIO.IN)
while True :
    value_stt = GPIO.input(14)
    value_sound = GPIO.input(18)
    print ("value is ", value_stt, "value_sound is", value_sound)
    if value_stt == False :
        os.system('python transcribe_streaming_mic_gaeul.py')
    if value_sound == False :
        os.system('python real_time_audio_processing.py')
    time.sleep(0.1)
