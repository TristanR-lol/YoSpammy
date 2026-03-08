from subprocess import Popen
from requests import get

UpdateLink1 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/main.pyw"
UpdateLink2 = "https://raw.githubusercontent.com/TristanR-lol/YoSpammy/refs/heads/main/setup.bat"

NewContent1 = get(UpdateLink1).text
NewContent2 = get(UpdateLink2).text

# --- Update setup.bat ---
try:
    with open("setup.bat", "r", encoding="utf-8") as r:
        ReadVal = r.read()
except FileNotFoundError:
    ReadVal = ""

if ReadVal != NewContent2:
    with open("setup.bat", "w", encoding="utf-8") as f:
        f.write(NewContent2)
    Popen(["setup.bat"], shell=True)

# --- Update main.pyw ---
with open("main.pyw", "w", encoding="utf-8") as f:
    f.write(NewContent1)

Popen(['pythonw', 'main.pyw'])