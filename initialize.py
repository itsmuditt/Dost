import talkngreet as tg
import speech_recognition as sr

bey = ''


def audioOnly():
    ear = sr.Recognizer()
    ear.pause_threshold = 1
    try:
        with sr.Microphone() as mic:
            global bey
            audio = ear.listen(mic, timeout=3600)
            bey = ear.recognize_google(audio, language="en-IN")
            bey = bey.lower()
            print(bey)
            return bey
    except:
        pass


def chat():
    global bey
    bey = input()
    return bey


def initialize():
    try:
        tg.talk('.')
        hey = audioOnly() or chat()

    except Exception as e:
        tg.talk(e)
        tg.talk('Perhaps, you could write what you want me to do or say it out loud!')
        hey = audioOnly() or chat()

    return hey