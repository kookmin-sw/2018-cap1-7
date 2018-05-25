#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import numpy as np
import sys

#
import pyaudio  
import time
import RPi.GPIO as GPIO
#

import scipy
import scipy.io.wavfile

from scikits.talkbox.features import mfcc

from collections import defaultdict

from sklearn.metrics import precision_recall_curve, roc_curve
from sklearn.metrics import auc
from sklearn.cross_validation import ShuffleSplit

from sklearn.metrics import confusion_matrix

from utils import plot_roc, plot_confusion_matrix, GENRE_LIST, GENRE_DIR, WAV_DIR

from ceps import read_ceps

from save import make_wav

genre_list = GENRE_LIST
genre_dir = GENRE_DIR


#
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

value_sound = 1

CHUNK = 2**11 # number of data points to read at a time --> buffr로
RATE = 44100
#




def get_volume():
    p=pyaudio.PyAudio() # start the PyAudio class 

    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) 
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)

    peak=np.average(np.abs(data))*2

   
    bars = ""
    if peak > 100: 
        bars="ll"*int(50*peak/2**16)
        print("%04d %s"%(peak,bars)) # output 
        
        #time.sleep(0.09)#print time
        if peak > 700:
            #stop stream
            stream.stop_stream()  
            stream.close()
            p.terminate()
            return 1, bars
    else :
        print peak
    # stop stream
    stream.stop_stream()  
    stream.close()
    p.terminate()
    return 0, bars

	

def train_model(clf_factory, X, Y):
    train_errors = []

    clfs = []  # just to later get the median

    clf = clf_factory()

    clf.fit(X, Y)
    clfs.append(clf)

    train_score = clf.score(X, Y)

    train_errors.append(1 - train_score)

    return np.mean(train_errors), clf


def create_model():
    from sklearn.linear_model.logistic import LogisticRegression
    clf = LogisticRegression()

    return clf

def read_files(fn, base_dir=genre_dir):
    X = []
    for fn in glob.glob(os.path.join(base_dir, fn)):
        ceps = np.load(fn)
        num_ceps = len(ceps)
        X.append(
            np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))

    return np.array(X)


def create_ceps(fn):
    sample_rate, X = scipy.io.wavfile.read(fn)
    ceps, mspec, spec = mfcc(X)
    return ceps



if __name__ == "__main__":
    sounds = {0:'dog', 1:'gun', 2:'dryer', 3:'car_horn', 4:'break', 5: 'scream'}
    wavfile_num = 0
    wavfile_name = "file"
    X, y = read_ceps(genre_list)
    train_avg, clfss = train_model(create_model, X, y)
    DIR = "/home/viewtiful/2018-cap1-7/src/mfcc/"

    #    DIR = "C:\Users\lynn\PycharmProjects\\2018-cap1-7\src\mfcc"

    instruction = "started the volume size function"
    os.system('sudo ./oled %s' %instruction)
    time.sleep(1.5)


    while 1 and value_sound:
        if (wavfile_num > 5):
             wavfile_num = 0

        # should think better idea
        value_sound = GPIO.input(18)
        if value_sound == 0 :
            os.system('sudo ./oled off')
            os.system("python displaytext.py")

        make_wav("file", wavfile_num, 0.5)

        # should think better idea
        value_sound = GPIO.input(18)
        if value_sound == 0 :
            os.system("sudo ./oled off")
            os.system("python displaytext.py")

        fn = DIR + "file" + str(wavfile_num) + ".wav"

        # should think better idea
        value_sound = GPIO.input(18)
        if value_sound == 0 :
            os.system("sudo ./oled off")
            os.system("python displaytext.py")

        X = []
        ceps = create_ceps(fn)
        num_ceps = len(ceps)

        # should think better idea
        value_sound = GPIO.input(18)
        if value_sound == 0 :
            os.system("sudo ./oled off")
            os.system("python displaytext.py")

        X.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))

        check, bars = get_volume()
        
        # should think better idea
        value_sound = GPIO.input(18)
        if value_sound == 0 :
            os.system("sudo ./oled off")
            os.system("python displaytext.py")
       
        if check==1 :
            arr_c = clfss.predict(X)
            predicted_key = arr_c[0]
 
            for key in sounds.keys():
                if arr_c == key:
                    str_ =  '0 '+ str(predicted_key)
                    os.system('sudo ./oled %s' %str_)
                    print '-----------------------'
                    print '>> file_'+str(wavfile_num)+ ' = ['+sounds.get(predicted_key)+']'
                    print '-----------------------'
        else:
            a = '1 '+bars
            os.system("sudo ./oled %s" %a)
        wavfile_num = wavfile_num + 1

        value_sound = GPIO.input(18)


    os.system("sudo ./oled off")
    os.system("python displaytext.py")
