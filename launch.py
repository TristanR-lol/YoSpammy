from subprocess import Popen
from requests import get

UpdateLink1 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/main.pyw"
UpdateLink2 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/setup.bat"
NewContent1 = get(UpdateLink1)
NewContent2 = get(UpdateLink2)

with open("setup.bat", "w", encoding="utf-8") as f:
    ReadVal = ""
    with open("setub.bat", "r", encoding="utf-8") as r:
        ReadVal = r.read()
    if ReadVal != NewContent1.text:
        f.write(NewContent1.text)

with open("main.pyw", "w", encoding="utf-8") as f:
  f.write(NewContent1.text)
Popen(['pythonw', 'main.pyw'])