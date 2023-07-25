import webbrowser
import speech_recognition as sr
import os
import time as tm
import pyautogui
import win32com.client
import datetime
from tkinter import Tk, Button, Label, StringVar

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
    indication.set("Function: Time")
    indication_label.configure(foreground="green")

def open_website(url):
    webbrowser.open(url)
    indication.set("Function: Open Website")
    indication_label.configure(foreground="green")

def music_player():
    say("which song would you like to hear")
    song_name= takeCommand()
    c=song_name[0]
    if "can't be recognized" in song_name.lower():
        say(song_name)
        music_player()
    else:
        say("playing..."+song_name)
        os.system("spotify")
        tm.sleep(5)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write(c, interval=0.1)
        pyautogui.write(song_name, interval=0.1)
        for key in ['enter', 'tab', 'enter', 'enter']:
            tm.sleep(2)
            pyautogui.press(key)
        return


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
        music_player()
        indication.set("Function: Playing Music")
        indication_label.configure(foreground="green")
    elif "spotify" in query:
        os.system("spotify")
        indication.set("Function: Opening Spotify")
        indication_label.configure(foreground="green")
    else:
        indication.set("Command not recognized")
        indication_label.configure(foreground="red")

if __name__ == '__main__':


    root = Tk()
    root.title("Jarvis Assistant")
    root.geometry("300x200")

    indication = StringVar()

    indication_label = Label(root, textvariable=indication, font=("Arial", 12, "bold"))
    indication_label.pack(pady=10)

    command_button = Button(root, text="Process Command", command=process_command)
    command_button.pack(pady=10)

    music_button = Button(root, text="Play Music", command=music_player)
    music_button.pack(pady=10)

    quit_button = Button(root, text="Quit", command=quit_program)
    quit_button.pack(pady=10)

    root.mainloop()
