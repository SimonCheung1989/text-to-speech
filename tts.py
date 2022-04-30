import os
import pyttsx3
import time
import sys
 
def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

engine = pyttsx3.init()
voices = engine.getProperty('voices')
number = 0
print(len(voices))
for voice in voices:
    engine.setProperty('voice', voice.id)
    print(str(number) + '. Age: ' + str(voice.age) + ', Name:' + voice.name + ', Gender: ' + voice.gender + ', Languages: ' + str(voice.languages))
    number += 1

# engine = pyttsx3.init()
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('volume', volume+0.25)
content = sys.argv[1]
if isChinese(content):
    engine.setProperty('voice', voices[39].id)
else:
    engine.setProperty('voice', voices[0].id)
engine.say(content)
engine.runAndWait()