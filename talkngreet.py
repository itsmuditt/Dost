import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(tet):
    print(tet)
    engine.say(tet)
    engine.runAndWait()


def greet():
    hr = int(datetime.datetime.now().hour)
    greeting = ''
    if (hr >= 0) and (hr < 12):
        greeting = 'Good Morning Sir!'
    elif (hr >= 12) and (hr < 17):
        greeting = 'Good Afternoon Sir!'
    elif hr >= 17:
        greeting = 'Good Evening Sir!'
    talk(greeting)
