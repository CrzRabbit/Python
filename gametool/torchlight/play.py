from numpy import *
from PIL import ImageGrab
import cv2 as cv
from pynput.mouse import Button
from pynput import mouse
from pynput import keyboard
import time
#0: 2K 1:1080p
display_type = 1

tx = 1
ty = 1
boss_icon = 'bosspos.jpg'
boss_points_full = 'boss_points_0.jpg'

if display_type == 1:
    tx = 2560 / 1920
    ty = 1440 / 1080
    boss_icon = 'boss_icon_0.jpg'
    boss_points_full = 'boss_points_1.jpg'

def play(line):
    mouse_controller = mouse.Controller()
    keyboard_controller = keyboard.Controller()
    direc = {'Button.left': Button.left, 'Button.right': Button.right}
    # print(line)
    op = line.split(' ')
    if float(op[0]) > 0.0073:
        time.sleep(float(op[0]))
    if op[1] == 'mouse':
        if op[2] == '0':
            mouse_controller.position = (int(int(op[3]) / tx), int(int(op[4]) / ty))
        elif op[2] == '1':
            mouse_controller.position = (int(int(op[3]) / tx), int(int(op[4]) / ty))
            if op[6] == 'True':
                mouse_controller.press(direc[op[5]])
            else:
                mouse_controller.release(direc[op[5]])
                if op.__len__() > 7 and op[7] == 'check':
                    time.sleep(1.5)
                    if is_boss_points_full(0):
                        kill_boss()
                        return False
                    elif not is_right_pos(0):
                        reset()
                        return False

    if op[1] == 'key':
        if op[3] == 'Key.esc':
            pass
        if op[2] == '0':
            keyboard_controller.press(op[3][1])
        elif op[2] == '1':
            keyboard_controller.release(op[3][1])
    return True
def test():
    print('test')
    record = open('test.txt', 'r')
    ops = record.readlines()
    for line in ops:
        play(line)

def reset():
    print('resetd')
    record = open('reset.txt', 'r')
    ops = record.readlines()
    for line in ops:
        play(line)

def kill_boss():
    print("kill_boss")
    record = open('killboss.txt', 'r')
    ops = record.readlines()
    for line in ops:
        play(line)
    #clear_bag()

def clear_map():
    print('clear_map')
    record = open('clearmap.txt', 'r')
    ops = record.readlines()
    while True:
        for line in ops:
            ret = play(line)
            if not ret:
                break

def clear_bag():
    print("clear_bag")
    record = open('clearbag.txt', 'r')
    ops = record.readlines()
    for line in ops:
        play(line)

def check_image(image, oring_img):
    # 读取图片
    tpl = cv.imread(oring_img)

    # 将图片转换为灰度图像
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    tpl_gray = cv.cvtColor(tpl, cv.COLOR_BGR2GRAY)

    # 计算相似度矩阵
    res = cv.matchTemplate(img_gray, tpl_gray, cv.TM_CCOEFF_NORMED)

    # 找到最大匹配
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(res)
    print(minVal, maxVal, minLoc, maxLoc)
    return maxVal

def is_right_pos(index):
    x1 = int(1130 / tx)
    y1 = int(250 / ty)
    x2 = int(1470 / tx)
    y2 = int(470 / ty)
    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    image = array(image.getdata(), uint8).reshape(image.size[1], image.size[0], 3)
    cv.imwrite("./test/boss_icon_{0}.jpg".format(index), image)
    print(check_image(image, boss_icon))
    if check_image(image, boss_icon) > 0.96:
        return True
    return False

def is_boss_points_full(index):
    x1 = int(1130 / tx)
    y1 = int(540 / ty)
    x2 = int(1470 / tx)
    y2 = int(600 / ty)
    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    image = array(image.getdata(), uint8).reshape(image.size[1], image.size[0], 3)
    cv.imwrite("./test/boss_points_{0}.jpg".format(index), image)
    if check_image(image, boss_points_full) > 0.96:
        return True
    return False

time.sleep(3)
# test()
#is_right_pos(0)
#is_boss_points_full(1)
clear_map()