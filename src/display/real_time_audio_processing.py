# coding: utf-8

# import audio_processing module in python 
import pyaudio  
import numpy as np
import os
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

value_sound = GPIO.input(18)

CHUNK = 2**11 # number of data points to read at a time --> buffr로
RATE = 44100  # time resolution of the recoding device(mic module) -- 44Kbyte(Hz) 

p=pyaudio.PyAudio() # start the PyAudio class
# convert analog signal to digital signal(Int16) (uses default input device)  
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) 
time.sleep(1)
while True and value_sound : # go for infinite loop
    # convet BufferdData(int) to String for knowing audio level value 
    # steam.read(Slieced Data)
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    # Audio level meter -> peak average method
    peak=np.average(np.abs(data))*2

    print peak
    # visualize values by bars
    if peak > 2000 : 
        bars="l"*int(50*peak/2**16)
        print("%04d %s"%(peak,bars)) # output 
        os.system("sudo ./show %s" %bars)
        time.sleep(0.12)
    value_sound = GPIO.input(18)

# stop stream
stream.stop_stream()  
stream.close()      
p.terminate()

