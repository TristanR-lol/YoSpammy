from customtkinter import *
from subprocess import Popen
from requests import get
root = CTk()

TaskLabel  = CTkLabel(root, text="Updating!")
TaskLabel.pack()

UpdateLink = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/main.py"
NewContent = get(UpdateLink)

with open("main.pyw", "w") as f:
  f.write(NewContent.text)

Popen(['pythonw', 'main.pyw'])   
root.mainloop()