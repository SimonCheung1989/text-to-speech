import pyttsx3
import time
from datetime import datetime
from shared import CountDownLatch

class TextToSpeech(object):
    def __init__(self, data_path, count_down_latch: CountDownLatch):
        self.__data_path = data_path
        self.__count_down_latch = count_down_latch

    def isChinese(self, word):
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False

    def onStart(name):
        print('starting', name)

    def onWord(name, location, length):
        print('word', name, location, length)

    def onEnd(name, completed):
        print('finishing', name, completed)
        time.sleep(1)

    def tts(self):
        print(self.__data_path) 
        now = datetime.now()
        startTime = datetime.timestamp(now)

        with open(self.__data_path, encoding='utf-8') as f:
            lines = f.readlines()

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        volume = engine.getProperty('volume')

        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-80)
        engine.setProperty('volume', volume+0.25)
        engine.setProperty('voice', voices[0].id)
        engine.connect('started-utterance', self.onStart)
        engine.connect('started-word', self.onWord)
        engine.connect('finished-utterance', self.onEnd)

        lineNumber = 0
        for line in lines:
            lineNumber += 1
            print(line)
            if lineNumber == 1:
                continue
            if not self.isChinese(line):
                print("engine.say: " + line)
                engine.say(line)
        engine.runAndWait()

        now = datetime.now()
        endTime = datetime.timestamp(now)
        print("Duration: " + str(endTime - startTime))
        # self.__count_down_latch.countDown()