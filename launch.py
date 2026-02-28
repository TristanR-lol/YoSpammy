from subprocess import Popen
from requests import get

UpdateLink1 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/main.pyw"
UpdateLink2 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/setup.bat"
NewContent1 = get(UpdateLink1)
NewContent2 = get(UpdateLink2)

with open("main.pyw", "w", encoding="utf-8") as f:
  f.write(NewContent1.text)
with open("setup.bat", "w", encoding="utf-8") as f:
  f.write(NewContent2.text)

Popen(['pythonw', 'main.pyw'])   