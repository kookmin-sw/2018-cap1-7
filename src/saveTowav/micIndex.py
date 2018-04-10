import pyaudio

po = pyaudio.PyAudio()

for index in range(po.get_device_count()):
    desc = po.get_device_info_by_index(index)
    print("Device: %s Index: %s Rate: %s" % (desc["name"],index,int(desc["defaultSampleRate"])))
