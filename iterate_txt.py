import os
from shared import CountDownLatch 

basepath = os.path.abspath(__file__)
folder = os.path.dirname(basepath)
output_txt_folder = folder + "/output/txt/"
output_audio_folder = folder + "/output/audio/"

for filename in os.listdir(output_txt_folder):
    print(output_txt_folder + filename)
    os.system("python3 text_to_speech.py " + output_txt_folder + filename)
    os.system("python3 record_voice.py " + output_audio_folder + filename + " " + str(120))


