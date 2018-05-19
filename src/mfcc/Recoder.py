
from save import make_wav
from ceps import create_ceps

if __name__ == "__main__":

    DIR = "/home/viewtiful/2018-cap1-7/src/mfcc/"
    #    DIR = "C:\Users\lynn\PycharmProjects\\2018-cap1-7\src\mfcc"

    f = "dog"
    while 1:
        num = int(input())
        sec = int(input())
        make_wav(f, num, sec)
        fn = DIR + f + str(num) + ".wav"
        X = []
        create_ceps(fn)