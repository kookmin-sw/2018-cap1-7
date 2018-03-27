import os
import scipy
from scipy.io import wavfile

def create_fft(fn):
	sample_rate, X = scipy.io.wavfile.read(fn)
	fft_features = abs(scipy.fft(X)[:1000])
	base_fn, ext = os.path.splitext(fn)
	data_fn = base_fn + ".fft"
	scipy.save(data_fn, fft_features)
	
create_fft("gun.wav")
