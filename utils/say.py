import os

try:
    import pyttsx4
except ModuleNotFoundError:
    os.system('pip install pyttsx4')

engine = pyttsx4.init()

def tts(text):
    engine.say(str(text))
    return engine.runAndWait()