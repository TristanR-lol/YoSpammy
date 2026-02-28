from subprocess import Popen
from requests import get

UpdateLink1 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/main.pyw"
UpdateLink2 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/setup.bat"
NewContent1 = get(UpdateLink1)
NewContent2 = get(UpdateLink2)

with open("setup.bat", "w", encoding="utf-8") as f:
  f.write(NewContent2.text)
with open("main.pyw", "w", encoding="utf-8") as f:
  if f.read() != NewContent1:
    f.write(NewContent1.text)
    Popen(["setup.bat"], shell=True)
  else:
    Popen(['pythonw', 'main.pyw']) 