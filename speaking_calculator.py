from tkinter import Tk, Button, Entry
import win32com.client

speaker = win32com.client.Dispatch("SAPI.Spvoice")
def say(text):
    speaker.Speak(text)

def button_click(number):
    current = entry.get()
    entry.delete(0, "end")
    entry.insert("end", str(current) + str(number))
    say(str(number))


def button_clear():
    entry.delete(0, "end")

def button_equal():
    result = eval(entry.get())
    say("= to..."+str(result))
    entry.delete(0, "end")
    entry.insert("end", str(result))

if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    say("calci")
    entry = Entry(root, width=20)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Adjusted columnspan to 4

    # Buttons
    buttons = [
        ("1", 1, 0),
        ("2", 1, 1),
        ("3", 1, 2),
        ("4", 2, 0),
        ("5", 2, 1),
        ("6", 2, 2),
        ("7", 3, 0),
        ("8", 3, 1),
        ("9", 3, 2),
        ("0", 4, 0),
        ("+", 1, 3),
        ("-", 2, 3),
        ("*", 3, 3),
        ("/", 4, 3),
        ("=", 4, 2),
        ("C", 4, 1),
    ]

    for btn_text, row, col in buttons:
        button = Button(root, text=btn_text, padx=15, pady=15)
        button.grid(row=row, column=col, padx=5, pady=5)

        if btn_text.isdigit():
            button.config(command=lambda number=btn_text: button_click(number))

        elif btn_text == "=":
            button.config(command=button_equal)
        elif btn_text == "C":
            button.config(command=button_clear)
        else:
            button.config(command=lambda operator=btn_text: button_click(operator))

    root.mainloop()




