import sounddevice as sd
from scipy.io.wavfile import write
import sys

data_path = sys.argv[1]
duration_in_second = int(sys.argv[2])

fs = 44100  # Sample rate

myrecording = sd.rec(int(duration_in_second * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write(data_path, fs, myrecording)  # Save as WAV file 