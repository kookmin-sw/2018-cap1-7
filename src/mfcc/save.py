import pyaudio
import wave
import sys


def make_wav(name="file",num=0,sec=5, dirr ="0" ):
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	CHUNK = 2048
	RECORD_SECONDS = sec
	if dirr == "0":
		WAVE_OUTPUT_FILENAME = name+str(num)+".wav"
	else :
		WAVE_OUTPUT_FILENAME = dirr + name+str(num)+".wav"       
	audio = pyaudio.PyAudio()

	# start Recording
	stream = audio.open(format=pyaudio.paInt16, 
		            channels=CHANNELS, 
		            rate=RATE, 
		            input=True, 
		            #input_device_index=2,
		            frames_per_buffer=CHUNK)

	print "recording..."

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

		data = stream.read(CHUNK, exception_on_overflow = False)

		frames.append(data)

	print "finished recording"

	 
	# stop Recording

	stream.stop_stream()
	stream.close()
	audio.terminate()

	 

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')

	waveFile.setnchannels(CHANNELS)

	waveFile.setsampwidth(audio.get_sample_size(FORMAT))

	waveFile.setframerate(RATE)

	waveFile.writeframes(b''.join(frames))

	waveFile.close()


if __name__ == "__main__":
    make_wav("f",0)


