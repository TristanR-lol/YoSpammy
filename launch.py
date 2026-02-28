from customtkinter import *
from subprocess import Popen
from requests import get
root = CTk()

TaskLabel  = CTkLabel(root, text="Updating!")
TaskLabel.pack()

UpdateLink = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/main.pyw"
NewContent = get(UpdateLink)

with open("main.pyw", "w", encoding="utf-8") as f:
  f.write(NewContent.text)

Popen(['pythonw', 'main.pyw'])   
root.mainloop()