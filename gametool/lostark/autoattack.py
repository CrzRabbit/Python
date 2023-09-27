from numpy import *
import time
import win32api
import win32con
from pynput.keyboard import Key, Controller
kb = Controller()
from pynput.mouse import Button, Controller
ms = Controller()

def getDel():
    return random.random() / 100 + 0.3

def press(key, interval=0.1):
    time.sleep(getDel())
    kb.press(key)
    time.sleep(interval)
    kb.release(key)
    time.sleep(getDel())

def attack(count):
    width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    print("屏幕长：", width)
    print("屏幕宽：", height)

    time.sleep(1)
    win32api.SetCursorPos((width // 2, height // 2))

    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -100, 0, 0)
    time.sleep(0.5)
    ms.press(Button.left)
    ms.release(Button.left)
    time.sleep(1.5)
    if count % 2500 == 0:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -100, 0, 0)
        time.sleep(0.5)
        ms.press(Button.left)
        ms.release(Button.left)
        time.sleep(1)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 200, 0, 0)
        time.sleep(0.5)
        ms.press(Button.left)
        ms.release(Button.left)
        time.sleep(1)

if __name__ == "__main__":
    time.sleep(1)
    count = 0
    while True:
        count += 1
        press('w')
        time.sleep(7)
        press('s', 3)
        time.sleep(1)
        if count % 50 == 0:
            attack(count)