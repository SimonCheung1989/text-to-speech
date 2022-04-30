import os
import pyttsx3
import time
import sys
from datetime import datetime

data_path = sys.argv[1]
print(data_path) 

now = datetime.now()
startTime = datetime.timestamp(now)

def isChinese(word):
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

with open(data_path, encoding='utf-8') as f:
    lines = f.readlines()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)
engine.setProperty('volume', volume+0.25)
engine.setProperty('voice', voices[0].id)
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

lineNumber = 0
for line in lines:
    lineNumber += 1
    print(line)
    if lineNumber == 1:
        continue
    if not isChinese(line):
        engine.say(line)
engine.runAndWait()

now = datetime.now()
endTime = datetime.timestamp(now)
print("Duration: " + str(endTime - startTime))