# This code is supporting material for the book
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
# published by PACKT Publishing
#
# It is made available under the MIT License

import sys
import os
import glob

import numpy as np
import scipy
import scipy.io.wavfile

from utils import GENRE_DIR, CHART_DIR

import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter




def create_fft(fn):
    sample_rate, X = scipy.io.wavfile.read(fn)
    fft_features = abs(scipy.fft(X)[:1000])
    base_fn, ext = os.path.splitext(fn)
    data_fn = base_fn + ".fft"
    np.save(data_fn, fft_features)


def read_fft(genre_list, base_dir=GENRE_DIR):
    X = []
    y = []
    for label, genre in enumerate(genre_list):
        genre_dir = os.path.join(base_dir, genre, "*.fft.npy")
        file_list = glob.glob(genre_dir)
        assert(file_list), genre_dir
        for fn in file_list:
            fft_features = np.load(fn)
            X.append(fft_features[:1000])
            y.append(label)

    return np.array(X), np.array(y)



if __name__ == "__main__":
    os.chdir(GENRE_DIR)
    glob_wav = os.path.join(sys.argv[1], "*.wav")
    print(glob_wav)
    for fn in glob.glob(glob_wav):
        create_fft(fn)


