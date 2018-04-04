# This code is supporting material for the book
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
# published by PACKT Publishing
#
# It is made available under the MIT License

import os
import glob
import sys


import numpy as np
import scipy
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
import librosa

from utils import GENRE_DIR


def write_mfcc(mfcc, fn):
   # Write the MFCC to separate files to speed up processing.
    base_fn, ext = os.path.splitext(fn)
    data_fn = base_fn + ".mfcc"
    np.save(data_fn, mfcc)
    print("Written %s"%data_fn)


def create_mfcc(fn):
    X, sample_rate = librosa.load(fn)
    mfccs = librosa.feature.mfcc(y=X,
                                 sr=sample_rate,
                                 n_mfcc=39,
                                 hop_length=int(sample_rate * 0.01),
                                 n_fft=int(sample_rate * 0.02),
                                 htk=True).T
    write_mfcc(mfccs, fn)


def read_mfcc(genre_list, base_dir=GENRE_DIR):
    X = []
    y = []
    for label, genre in enumerate(genre_list):
        for fn in glob.glob(os.path.join(base_dir, genre, "*.mfcc.npy")):
            mfcc = np.load(fn)
            num_mfcc = len(mfcc)
            X.append(
                np.mean(mfcc[int(num_mfcc / 10):int(num_mfcc * 9 / 10)], axis=0))
            y.append(label)

    return np.array(X), np.array(y)


if __name__ == "__main__":
    os.chdir(GENRE_DIR)
    glob_wav = os.path.join(sys.argv[1], "*.wav")
    print(glob_wav)
    for fn in glob.glob(glob_wav):
        create_mfcc(fn)