import random
import time
import win32api
import win32con
from pynput.keyboard import Key, Controller
kb = Controller()
from pynput.mouse import Button, Controller
ms = Controller()

total = 0
cur = 0

MAX_ARROW_TOTAL = 396
MAX_ARROW_EQUIPED = 99
def getDel():
    return random.random() / 100 + 0.3

def press(key, interval=0.1):
    time.sleep(getDel())
    kb.press(key)
    time.sleep(interval)
    kb.release(key)
    time.sleep(getDel())

def buy():
    press('g')
    press('f')
    for i in range(2):
        press('x')
    for i in range(2):
        press(Key.up)
    press('e')
    press('e')
    time.sleep(15)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -800, 0, 0, 0)
    time.sleep(getDel())
    kb.press('w')
    time.sleep(1.2)
    kb.release('w')
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -800, 0, 0, 0)
    time.sleep(getDel())
    kb.press('w')
    time.sleep(2)
    kb.release('w')
    time.sleep(1)
    for i in range(5):
        press('e')
        time.sleep(0.5)
    for i in range(2):
        press(Key.right)
    press(Key.down)
    press('e')
    press(Key.down)
    press('e')
    time.sleep(1)
    press('e')
    time.sleep(1)
    press('q')
    time.sleep(1)
    press('q')
    time.sleep(1)
    press('e')
    time.sleep(5)
    press('g')
    press('f')
    for i in range(3):
        press('x')
    press('e')
    press('e')
    time.sleep(8)

def usearrow():
    while(True):
        if total >= MAX_ARROW_TOTAL:
            time.sleep(5)
            total = 0
            cur = 0
            buy()
        else:
            rt = random.random() + 5
            time.sleep(rt)
            kb.press('g')
            time.sleep(getDel())
            kb.release('g')
            time.sleep(getDel())
            kb.press('d')
            time.sleep(0.05)
            kb.release('d')
            time.sleep(getDel())
            kb.press('e')
            time.sleep(getDel())
            kb.release('e')
            time.sleep(getDel())
            kb.press('e')
            time.sleep(getDel())
            kb.release('e')
            time.sleep(getDel())
            if cur >= MAX_ARROW_EQUIPED:
                time.sleep(random.random() + 7)
                cur = 0
                kb.press('w')
                time.sleep(0.7)
                kb.release('w')
                time.sleep(getDel())
                press('e')
                time.sleep(3)
                press('q')
                continue
        time.sleep(random.random() + 7)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1420, 30, 0, 0)
        time.sleep(0.2)
        kb.press('w')
        time.sleep(1.6)
        kb.release('w')
        time.sleep(getDel())
        ms.press(Button.right)
        time.sleep(0.01)
        ms.press(Button.left)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -160, 490, 0, 0)
        time.sleep(1.4)
        ms.release(Button.left)
        time.sleep(getDel() + 2)
        ms.release(Button.right)
        total += 1
        cur += 1

def usesheng():
    while True:
        rt = random.random() + 3
        time.sleep(rt)
        kb.press('g')
        time.sleep(getDel())
        kb.release('g')
        time.sleep(getDel())
        kb.press('s')
        time.sleep(0.05)
        kb.release('s')
        time.sleep(getDel())
        kb.press('e')
        time.sleep(getDel())
        kb.release('e')
        time.sleep(getDel())
        kb.press('e')
        time.sleep(getDel())
        kb.release('e')
        time.sleep(getDel())
        time.sleep(rt)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -270, 50, 0, 0)
        time.sleep(0.2)
        kb.press('w')
        time.sleep(4)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -270, 50, 0, 0)
        time.sleep(1.3)
        kb.release('w')
        ms.press(Button.right)
        time.sleep(0.1)
        kb.press(Key.shift_l)
        time.sleep(0.1)
        kb.release(Key.shift_l)
        time.sleep(0.1)
        ms.release(Button.right)
        time.sleep(5)

type = 1
if __name__ == "__main__":
    if type == 0:
        usearrow()
    else:
        usesheng()
