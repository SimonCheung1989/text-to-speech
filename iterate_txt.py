import os
import threading
from shared import CountDownLatch 
from TextToSpeech import TextToSpeech
from RecordVoice import RecordVoice
# from subprocess import call
import subprocess

basepath = os.path.abspath(__file__)
folder = os.path.dirname(basepath)
output_txt_folder = folder + "/output/txt/"
output_audio_folder = folder + "/output/audio/"

for filename in os.listdir(output_txt_folder):
    print("Start: " + output_txt_folder + filename)
    countDownLatch = CountDownLatch(2)
    # tts = TextToSpeech(data_path=output_txt_folder + filename, count_down_latch=countDownLatch)
    # tts.tts()
    # thread1 = threading.Thread(target=tts.tts)
    # thread1.daemon = True
    # call(["python3", "text_to_speech.py", output_txt_folder + filename])
    subprocess.Popen(["python3", "text_to_speech.py", str(output_txt_folder + filename)])
    print("Recording")
    rv = RecordVoice(data_path=output_audio_folder + filename.replace(".txt", ".wav"), duration_in_second=120, count_down_latch=countDownLatch)
    # rv.record()
    thread2 = threading.Thread(target=rv.record)

    # thread1.start()
    thread2.start()
    # thread1.join()
    thread2.join()
    print("Finish: " + output_txt_folder + filename)
    # countDownLatch.awaits()
    # os.system("python3 text_to_speech.py " + output_txt_folder + filename)
    # os.system("python3 record_voice.py " + output_audio_folder + filename + " " + str(120))


