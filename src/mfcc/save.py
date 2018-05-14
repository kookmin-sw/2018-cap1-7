import pyaudio
import wave

def make_wav(name="file",num=0):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 2048
    RECORD_SECONDS = 1
    WAVE_OUTPUT_FILENAME = name

    audio = pyaudio.PyAudio()

    # start Recording

    stream = audio.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                      #  input_device_index=2,
                        frames_per_buffer=CHUNK)

    print "recording..."

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    print "finished recording"

    # stop Recording

    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile = wave.open(WAVE_OUTPUT_FILENAME+str(num)+".wav", 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()



if __name__ == "__main__":
    wavfile_num = 0
    wavfile_name = "file"
    while 20 :
        make_wav(wavfile_name,wavfile_num)
        wavfile_num+=1
