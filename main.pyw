from customtkinter import *
from tkinter import *
import pyautogui as control
from time import sleep
from pynput import keyboard, mouse
from threading import Thread
from requests import get

# --- Self-update ---
try:
    NewContent = get(
        "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/launch.py",
        timeout=5
    ).text
    try:
        with open("launch.py", "r", encoding="utf-8") as r:
            ReadVal = r.read()
    except FileNotFoundError:
        ReadVal = ""

    if ReadVal != NewContent:
        with open("launch.py", "w", encoding="utf-8") as f:
            f.write(NewContent)
except Exception as e:
    print(f"Self-update failed: {e}")

# --- Globals ---
root = CTk()
root.title("spammy")
root.geometry("500x350")
root.attributes("-topmost", True)

Looping = False
ChatPos = (0, 0)
Tabs = []
TabNum = 0

# --- Kill switch ---
def kill_switch():
    global Looping

    def on_press(key):
        global Looping
        if key == keyboard.Key.esc:
            print("STOP!")
            Looping = False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# --- Tab/chat position capture ---
def SelectTabPos(TabNum2):
    global ChatPos, Tabs, TabNum

    overlay = Toplevel(root)
    overlay.attributes("-fullscreen", True)
    overlay.attributes("-alpha", 0.7)
    overlay.attributes("-topmost", True)
    overlay.configure(bg="black")

    CTkLabel(overlay, text="Click to set the tab position", font=("Arial", 40)).pack(expand=True)

    def on_click(x, y, button, pressed):
        if pressed:
            root.after(0, overlay.destroy)
            return False

    def listen():
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

        Pos = control.position()
        if TabNum2 == 0:
            global ChatPos
            ChatPos = Pos
        else:
            Tabs.append(Pos)
            global TabNum
            TabNum += 1

    Thread(target=listen, daemon=True).start()

# --- Spam loop ---
def spam_loop():
    global Looping
    while True:
        if Looping == False:
            return
        for i in range(TabNum):
            if Looping == False:
                return
            control.click(Tabs[i])
            control.click(Tabs[i])
            sleep(.1)
            control.click(ChatPos)
            sleep(.1)
            control.typewrite(MessageBox.get())
            sleep(.1)
            control.press("enter")
            sleep(.1)

def Start():
    global Looping
    if Looping:
        return
    Looping = True
    Thread(target=kill_switch, daemon=True).start()
    Thread(target=spam_loop, daemon=True).start()

# --- UI ---
CTkLabel(master=root, text="Enter the text to spam").pack()
MessageBox = CTkEntry(master=root, width=350)
MessageBox.pack()

CTkLabel(master=root, text="Add tabs to spam in").pack()
CTkButton(master=root, text="Add Tab", command=lambda: SelectTabPos(1)).pack(pady=7)

CTkLabel(master=root, text="Select the chat position").pack()
CTkButton(master=root, text="Chat", command=lambda: SelectTabPos(0)).pack()

CTkButton(master=root, text="START", command=Start).pack(pady=30)
CTkLabel(
    master=root,
    text="Once you have configured everything, click START above.\nClick ESCAPE to stop the program."
).pack()

root.mainloop()