import win32api
from pynput.mouse import Button, Controller
ms = Controller()

while True:
    print(win32api.GetCursorPos())