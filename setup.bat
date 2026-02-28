@echo off
setlocal

:: Find the python executable and store it
for /f "delims=" %%i in ('where python') do (
    set PYTHON=%%i
    goto :found
)

:notfound
echo Python not found. Installing...
winget install -e --id Python.Python.3.11 --scope machine
:: Refresh PATH after install
for /f "delims=" %%i in ('where python') do (
    set PYTHON=%%i
    goto :found
)

:found
echo Using Python: %PYTHON%
"%PYTHON%" -m pip install customtkinter pyautogui win11toast pynput requests winshell
"%PYTHON%" launch.py