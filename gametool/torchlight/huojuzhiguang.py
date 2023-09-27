from numpy import *
from PIL import ImageGrab, Image
import cv2 as cv
from threading import Thread
import time
import win32api
import win32con
from pynput.keyboard import Key, Controller, KeyCode
kb = Controller()
from pynput.mouse import Button, Controller
ms = Controller()

middle_x = 1280
middle_y = 720
full_x = 2560
full_y = 1440
pos = [184, 217]
attack = False
steps = [[1200, 500], [1100, 1270], [1400, 900], [360, 400], [2160, 1215], [1618, 920]]
life = [1200, 1220]

def getDel():
    return random.random() / 100 + 0.2

def press(key, interval=0.1):
    time.sleep(getDel())
    kb.press(key)
    time.sleep(interval)
    kb.release(key)
    time.sleep(getDel())

def attack_e():
    key = 'e'
    while attack:
        time.sleep(0.2)
        kb.press(key)
        time.sleep(1)
        kb.release(key)

def attack_r():
    key = 'r'

def attack_a():
    while attack:
        press('a')
        time.sleep(6)

def attack_s():
    while attack:
        press('s')
        time.sleep(8)

def attack_q():
    while attack:
        press('q')

def attack_w():
    while attack:
        press('w')

def attack_mr():
    while attack:
        ms.press(Button.right)
        time.sleep(0.01)
        ms.release(Button.right)
        time.sleep(8)

def move_up():
    win32api.SetCursorPos([middle_x, 0])
    # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 128, 72, 0, 0)
    time.sleep(0.3)
    kb.press('r')
    time.sleep(0.1)
    kb.release('r')

def move_down():
    win32api.SetCursorPos([middle_x, 1440])
    # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -128, -72, 0, 0)
    time.sleep(0.3)
    kb.press('r')
    time.sleep(0.1)
    kb.release('r')

def move_left():
    win32api.SetCursorPos([0, middle_y])
    # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 128, 72, 0, 0)
    time.sleep(0.2)
    kb.press('r')
    time.sleep(0.1)
    kb.release('r')

def move_right():
    win32api.SetCursorPos([2560, middle_y])
    # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 128, 72, 0, 0)
    time.sleep(0.2)
    kb.press('r')
    time.sleep(0.1)
    kb.release('r')

def move():
    count = 500
    win32api.SetCursorPos([middle_x, middle_y])
    time.sleep(0.5)
    while count > 0:
        count -= 1
        move_up()
        move_down()
        move_down()
        move_down()
        move_up()
        move_up()
        # move_left()
        # move_right()
        # move_right()
        # move_left()

def attack_start():
    attacks = [attack_e, attack_r, attack_a, attack_s, attack_q, attack_w, attack_mr, move]
    threads = []
    global attack
    attack = True
    for i in range(attacks.__len__()):
        thread = Thread(target=attacks[i])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def attack_stop():
    global attack
    attack = False

def recovery_pos():
    press('t')
    time.sleep(5)
    press('w')
    time.sleep(10)
    print('back success')
    win32api.SetCursorPos([middle_x, middle_y])
    kb.press('r')
    time.sleep(3)
    kb.release('r')
    win32api.SetCursorPos([middle_x, 0])
    ms.press(Button.left)
    time.sleep(1.1)
    ms.release(Button.left)
    win32api.SetCursorPos([full_x, middle_y])
    ms.press(Button.left)
    time.sleep(0.5)
    ms.release(Button.left)
    time.sleep(2)
    press('w')
    for step in steps:
        win32api.SetCursorPos([step[0], step[1]])
        ms.press(Button.left)
        time.sleep(0.5)
        ms.release(Button.left)
        time.sleep(4)
    time.sleep(10)

# def filter_contours(contours):
#     for cou in contours:
#         if

def get_contours():
    image = ImageGrab.grab(bbox=(40, 60, 420, 460))
    image = array(image.getdata(), uint8).reshape(image.size[1], image.size[0], 3)

    #转化为灰度图
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #转化为二值图
    #返回值一：计算好或者设定好的阈值
    #返回值二：处理好的图像
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    #返回值一：轮廓信息
    #返回值二：层级
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    #绘制图像轮廓函数drawContours():图像、轮廓信息、轮廓索引(需要多少轮廓，-1默认全部)、颜色模式、线条厚度
    draw_img = image.copy()
    res = cv.drawContours(draw_img, contours, -1, (255, 255, 255), 1)
    #绘制当前位置
    cv.drawMarker(res, pos, (255, 255, 255), cv.MARKER_STAR)
    cv.imwrite("res.jpg", res)
    return contours

if __name__ == '__main__':
    time.sleep(3)
    contours = get_contours()
    recovery_pos()
    thread = Thread(target=attack_start())
    thread.start()
