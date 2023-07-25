import pyautogui
import os
import time
import speech_recognition as sr
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
say("which song would you like to play...")
song_name=takeCommand()
say("playing"+song_name)
os.system("spotify")
time.sleep(5)
pyautogui.hotkey('ctrl','l')
pyautogui.write(song_name, interval=0.1)
pyautogui.press('enter')
for key in ['enter', 'tab' ,'enter','enter']:

    pyautogui.press('key')

