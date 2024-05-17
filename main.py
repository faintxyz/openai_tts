"""
Complete: tts,responses
Todo: history, ui
"""

from utils.ai import *
from utils.say import *

import time

while True:
    prompt = input('(User) => ')
    print('AI Responding...')
    response = respond(prompt)
    tts(response)
    time.sleep(1)