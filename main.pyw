from customtkinter import *
import pyautogui as control
from time import *
from pynput import keyboard
from threading import Thread

root = CTk()
root.title("spammy")
root.geometry("500x350")
root.attributes("-topmost", True)

Looping = False
SpamText = ""
ChatPos = 0, 0
Tabs = []
TabNum = 0

def kill_switch():
    global Looping
    def on_press(key):
        global Looping
        print("Key pressed. Key: "+str(key))
        if key == keyboard.Key.esc:
            print("STOP!")
            #notify("Spammy","❌ Stopped ❌")
            Looping = False
            exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def SelectTabPos(TabNum2):
    global ChatPos, Tabs, TabNum
    #notify("Spammy", "Move your mouse over the button")
    sleep(5)
    #notify("Spammy", "📸 Captured 📸")
    Pos = control.position()
    if TabNum2 == 0:
        ChatPos = Pos
    else:
        Tabs.insert(TabNum2, Pos)
        TabNum += 1
        print(Tabs)

def Start():
    global Looping, TabNum, Tabs
    print(str(Tabs)+str(TabNum))
    Looping = True
    Thread(target=kill_switch, daemon=True).start()
    #notify("Spammy","✅ Started. Press ESCAPE to stop. ✅")
    while True:
       if Looping == False:
           return
       for i in range(TabNum):
            print(i)
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
    text="Add tabs to spam in"
)
TabButton = CTkButton(
    master=root,
    text="Add Tab",
    command=lambda: SelectTabPos(1),
)
Info.pack()
TabButton.pack(pady=7)

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