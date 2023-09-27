from numpy import *
from PIL import ImageGrab, Image
import cv2 as cv
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

def get_image(index):
    image = ImageGrab.grab(bbox=(1260, 600, 1300, 680))
    image = array(image.getdata(), uint8).reshape(image.size[1], image.size[0], 3)
    # cv.imwrite("./test/res{0}_{1}.jpg".format(index, find_image(image)), image)
    if find_image(image) > 0.30:
        press('e')
        return True
    return False

def find_image(image):
    # 读取图片
    tpl = cv.imread("origin.jpg")

    # 将图片转换为灰度图像
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    tpl_gray = cv.cvtColor(tpl, cv.COLOR_BGR2GRAY)

    # 计算相似度矩阵
    res = cv.matchTemplate(img_gray, tpl_gray, cv.TM_CCOEFF_NORMED)

    # 找到最大匹配
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(res)
    print(minVal, maxVal, minLoc, maxLoc)
    return maxVal

if __name__ == "__main__":
    count = 0
    time.sleep(3)
    press('e')
    while True:
        count += 1
        if get_image(count) or count >= 300:
            time.sleep(6 + getDel())
            press('e')
            count = 0
        time.sleep(0.01)
