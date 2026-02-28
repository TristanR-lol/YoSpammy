from customtkinter import *
import pyautogui as control
from time import *
from win11toast import notify, update_progress
from pynput import keyboard
from threading import Thread
import winshell
from pathlib import Path

target_file = r"setup.bat"
shortcut_name = "Spammy.lnk"
desktop = winshell.desktop()
shortcut_path = Path(desktop) / shortcut_name

with winshell.shortcut(shortcut_path) as link:
    link.path = target_file
    link.description = "Open spammy and begin the evil"
    link.icon = target_file, 0  # Use the file's icon
    link.working_directory = Path(target_file).parent   

root = CTk()
root.title("spammy")
root.geometry("500x350")
root.attributes("-topmost", True)

Looping = False
SpamText = ""
ChatPos = 0, 0
Tab1Pos = 0, 0
Tab2Pos = 0, 0

def kill_switch():
    global Looping
    def on_press(key):
        global Looping
        print("Key pressed. Key: "+str(key))
        if key == keyboard.Key.esc:
            print("STOP!")
            notify("Spammy","❌ Stopped ❌")
            Looping = False
            exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def SelectTabPos(TabNum):
    global ChatPos, Tab1Pos, Tab2Pos
    notify("Spammy", "Move your mouse over the button")
    sleep(5)
    notify("Spammy", "📸 Captured 📸")
    Pos = control.position()
    if TabNum == 0:
        ChatPos = Pos
    elif TabNum == 1:
        Tab1Pos = Pos
    elif TabNum == 2:
        Tab2Pos = Pos

def Start():
    global Looping
    Looping = True
    Thread(target=kill_switch, daemon=True).start()
    notify("Spammy","✅ Started. Press ESCAPE to stop. ✅")
    while True:
       if Looping == False:
        return
       control.click(Tab1Pos)
       control.click(Tab1Pos)
       sleep(.1)
       control.click(ChatPos)
       sleep(.1)
       control.typewrite(MessageBox.get())
       sleep(.3)
       control.press("enter")
       control.click(Tab2Pos)
       sleep(.1)
       control.click(ChatPos)
       sleep(.1)
       control.typewrite(MessageBox.get())
       sleep(.3)
       control.press("enter")

#Config
Info = CTkLabel(master=root, text="Enter the text to spam")
MessageBox = CTkEntry(
    master=root,
    width=350,
)
Info.pack()
MessageBox.pack()
Info = CTkLabel(
    master=root,
    text="Select the tab positions"
)
TabButton1 = CTkButton(
    master=root,
    text="Tab 1",
    command=lambda: SelectTabPos(1),
)
TabButton2 = CTkButton(
    master=root,
    text="Tab 2",
    command=lambda: SelectTabPos(2),
)
Info.pack()
TabButton1.pack(pady=2)
TabButton2.pack(pady=2)
Info = CTkLabel(
    master=root,
    text="Select the chat position"
)
ChatButton = CTkButton(
    master=root,
    text="Chat",
    command= lambda: SelectTabPos(0),
)
Info.pack()
ChatButton.pack()
StartButton = CTkButton(
    master=root,
    text="START",
    command=Start,
)
Info = CTkLabel(
    master=root,
    text="Once you have configured everything, click START above.\nClick ESCAPE to stop the program."
)
StartButton.pack(pady=30)
Info.pack()
root.mainloop()