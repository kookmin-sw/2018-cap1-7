#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import numpy as np
import sys

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

    wavfile_num = 0
    wavfile_name = "file"
    X, y = read_ceps(genre_list)
    train_avg, clfss = train_model(create_model, X, y)
    DIR = "/home/viewtiful/2018-cap1-7/src/mfcc/"

    #    DIR = "C:\Users\lynn\PycharmProjects\\2018-cap1-7\src\mfcc"

    while 1:
        make_wav("file", wavfile_num)
        fn = DIR + "file" + str(wavfile_num) + ".wav"
        X = []
        ceps = create_ceps(fn)
        num_ceps = len(ceps)
        X.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))


        arr_c = clfss.predict(X)
        print(wavfile_num)
        print (arr_c)
		
        print("-----------------------")
        print("-----------------------")

        wavfile_num = wavfile_num + 1
