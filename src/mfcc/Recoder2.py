import sys
from save import make_wav
from ceps import create_ceps

import numpy as np
import os

#
import pyaudio  
import time
import RPi.GPIO as GPIO
#

#
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

value_sound = 1

CHUNK = 2**11 # number of data points to read at a time
RATE = 44100
#



if __name__ == "__main__":

    DIR = "/home/viewtiful/2018-cap1-7/src/mfcc/"
    #    DIR = "C:\Users\lynn\PycharmProjects\\2018-cap1-7\src\mfcc"

    f = sys.argv[1]
    peak_range = 500
    num = 0
    sec = 0.5

    p=pyaudio.PyAudio() # start the PyAudio class 

    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) 



    while 1:

        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)

        peak=np.average(np.abs(data))*2

        print peak

        #time.sleep(0.09)#print time
        if peak > peak_range:
            print "a"
            make_wav(f, num, sec)
            fn = DIR + f + str(num) + ".wav"
            X = []
            create_ceps(fn)
            num = num + 1

    
    stream.stop_stream()  
    stream.close()
    p.terminate()



     
