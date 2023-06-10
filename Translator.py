from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition 
import os
from playsound import playsound
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import pygame
from translate import Translator

def translategl(query):
    speak("SURE SIR")
    translator = Translator(to_lang="hi")
    translation = translator.translate(query)
    text = translation.strip()
    try:
        speakgl = gTTS(text=text, lang="hi", slow=False)
        speakgl.save("voice.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()

        time.sleep(5)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        os.remove("voice.mp3")
    except:
        print("Unable to translate")
