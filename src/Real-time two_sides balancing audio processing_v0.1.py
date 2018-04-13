# coding: utf-8

# import audio_processing module in python
import pyaudio
import numpy as np

maxValue = 2**12 # # number of data points to read at a time(maximum)
bars = 2  # visualization of output value
p=pyaudio.PyAudio() # start the PyAudio class
# uses default input device
stream=p.open(format=pyaudio.paInt16,channels=2,rate=44100,
              input=True, frames_per_buffer=1024)
while True: # go for infinite loop : balancing two-sides volume size
    # convet BufferdData(int) to String for knowing audio level value 
    # 1024 is default value for Buffer
    data = np.fromstring(stream.read(1024),dtype=np.int16)
    dataL = data[0::2]  # Read the values in two steps (starting 0 index)
    dataR = data[1::2]  # Read the values in two steps (starting 1 index)
    # Peak value of two sides (max - min)/masvalue
    peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue  
    peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
    # visualize values by bars (L/R)
    lString = "#"*int(peakL*bars)+"-"*int(bars-peakL*bars)
    rString = "#"*int(peakR*bars)+"-"*int(bars-peakR*bars)
    print("L=[%s]\tR=[%s]"%(lString, rString))

