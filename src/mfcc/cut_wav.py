import scipy.io.wavfile as WF
import wave

if __name__ == "__main__":
    rate, data = WF.read("C:\Users\lynn\PycharmProjects\\2018-cap1-7\src\mfcc\car.wav")
    print(rate)

    for i in range(0,len(data),len(data)/2):
        fout = wave.open("s3_"+`i`+".wav","w")
        fout.setnchannels(1)
        fout.setsampwidth(2)
        fout.setframerate(44100)
        fout.setcomptype('NONE','Not Compressed')
        if len(data)-i > len(data)/2:
            print(i)
            print('a')
            fout.writeframesraw(data[i:i+len(data)/2])
        else:
            print(i)
            print('b')
            fout.writeframesraw(data[i:len(data)])
        fout.close()

