import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Face recognition complete, Good Morning Jashan")
    elif hour >12 and hour<=18:
        speak("Face recognition complete, Good Afternoon Jashan")

    else:
        speak("Face recognition complete, Good Evening Jashan")

    speak("How can I help you ?")

