import webbrowser
import speech_recognition as sr
import os
import win32com.client
speaker = win32com.client.Dispatch("SAPI.Spvoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:

            return "sorry ! command can't be recognized"

def open_website():
    say("which website")
    domain_name=takeCommand()
    print(domain_name)
    webbrowser.open(f"https://{domain_name}.com/")

query=takeCommand()
say(query)
if "website" in query.lower():
    open_website()
