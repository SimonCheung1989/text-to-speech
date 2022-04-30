import sounddevice as sd
from scipy.io.wavfile import write
from shared import CountDownLatch

class RecordVoice(object):
    def __init__(self, data_path, duration_in_second, count_down_latch: CountDownLatch):
        self.__data_path = data_path
        self.__duration_in_second = duration_in_second
        self.__count_down_latch = count_down_latch

    def record(self):
        fs = 44100  # Sample rate
        myrecording = sd.rec(self.__duration_in_second * fs, samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        write(self.__data_path, fs, myrecording)  # Save as WAV file 
        # self.__count_down_latch.countDown()