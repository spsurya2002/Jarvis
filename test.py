import webbrowser
import speech_recognition as sr
import os
import win32com.client
import datetime
from tkinter import Tk, Button

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
            return "Sorry! Command can't be recognized"




def time():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    month = now.strftime("%B")
    year = now.year
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    say("Today is " + str(day) + " of " + str(month) + " " + str(year))
    say("The current time is " + str(int(hour)) + " o'clock " + str(int(minute)) + " minutes")

def open_website(url):
    webbrowser.open(url)

def quit_program():
    say("I am shutting down!")
    root.destroy()

def process_command():
    query = takeCommand().lower()
    if "time" in query:
        
        time()
    elif "youtube" in query:
        open_website("https://www.youtube.com/")
    elif "leetcode" in query:
        open_website("https://leetcode.com/studyplan/top-interview-150/")
    elif "codeforces" in query:
        open_website("https://codeforces.com/profile/Surya0123")
    elif "udemy" in query:
        open_website("https://www.udemy.com/home/my-courses/learning/")
    elif "quit" in query or "shut up" in query:
        quit_program()
    elif "music" in query:
        music_path = 'C:\\Users\\HP\\Desktop\\Project(python)\\jarvisAI\\Memories---Maroon-5-320-(PagalWorld).mp3'
        say("Enjoy!! Music is playing...")
        os.startfile(music_path)
    elif "spotify" in query:
        os.system("spotify")
    else:
        say("Command not recognized")

if __name__ == '__main__':
    root = Tk()
    root.title("Jarvis Assistant")
    root.geometry("300x200")

    command_button = Button(root, text="Command Button!!", command=process_command)
    command_button.pack(pady=10)

    quit_button = Button(root, text="Quit", command=quit_program)
    quit_button.pack(pady=10)


    root.mainloop()
