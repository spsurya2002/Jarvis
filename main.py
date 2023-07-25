import webbrowser
import speech_recognition as sr
import os
import datetime
import time as tm
import pyautogui
import win32com.client
speaker = win32com.client.Dispatch("SAPI.Spvoice")

def say(text):
    speaker.Speak(text)

def music_player():
    say("which song")
    song_name= takeCommand()
    if song_name!="sorry ! command can't be recognized":
        os.system("spotify")
        tm.sleep(5)
        pyautogui.hotkey('ctrl', 'l')

        pyautogui.write(song_name, interval=0.1)
        for key in ['enter',  'tab', 'enter', 'enter']:
            tm.sleep(2)
            pyautogui.press(key)
        return
    else:
        music_player()


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


if __name__ == '__main__':

    say("hello! I am jarvis! how can i help you sir")
    # Get current date and time
    now = datetime.datetime.now()
    # Get the day, month, year, and time
    day = now.strftime("%A")
    month = now.strftime("%B")
    year = now.year
    hour = now.strftime("%H")
    min = now.strftime("%M")
    # saying current timestamp
    def time():
        say("Today is"+ str(day)+ "of"+ str(month)+ str(year))
        say("The current time is"+str(int(hour))+"bajke"+str(int(min))+"minute")
    # time()

    while 1:
        print("Listenning...")
        say("listenning...")
        query = takeCommand()
        print(query)
        sites=[["youtube","https://www.youtube.com/"],
               ["leetcode","https://leetcode.com/studyplan/top-interview-150/"],
               ["codeforces","https://codeforces.com/profile/Surya0123"],
               ["udemy","https://www.udemy.com/home/my-courses/learning/"]
               ]

        if "time".lower() in query.lower():
            time()
        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                say(f"openning {site[0]} sir...")
                webbrowser.open(site[1])
                break
        if query.lower()=="jarvis shutup"or query.lower()=="jarvis quit"or query.lower()=="shut up" :
            say("i am shutting down!")
            break
        if query.lower() == "music":
            music_player()
        if query.lower()=="spotify":
            os.system("spotify")

