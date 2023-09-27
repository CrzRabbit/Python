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

len = 360
width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
print("屏幕长：{0} 屏幕宽：{1}".format(width, height))
mini_map = (2150, 40, 2150 + len, 40 + len)

# 读取图片
ori_image = cv.imread("ori.jpg")
# 将图片转换为灰度图像
ori_image = cv.cvtColor(ori_image, cv.COLOR_BGR2GRAY)
print("图标长：{0} 图标宽：{1}".format(ori_image.shape[1], ori_image.shape[0]))

def getDel():
    return random.random() / 100 + 0.3

def press(key, interval=0.1):
    time.sleep(getDel())
    kb.press(key)
    time.sleep(interval)
    kb.release(key)
    time.sleep(getDel())

def move_to(x, y):
    win32api.SetCursorPos((width // 2 + ((x - len // 2) * 10), height // 2 + ((y - len // 10) * 2)))
    ms.press(Button.right)
    ms.release(Button.right)
    time.sleep(1)

def get_contours():
    image = ImageGrab.grab(bbox=mini_map)

    image = array(image.getdata(), uint8).reshape(image.size[1], image.size[0], 3)
    #缩放
    # image = cv.resize(image, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)

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
    draw_img = cv.drawContours(draw_img, contours, -1, (255, 255, 255), 2)

    #绘制当前位置
    # cv.drawMarker(res, pos, (255, 255, 255), cv.MARKER_STAR)
    draw_img = find_origin(draw_img)
    cv.imwrite("res.jpg", draw_img)
    return contours

def find_origin(image):
    print(image.shape)  # shape内包含三个元素：按顺序为高、宽、通道数
    height = image.shape[0]
    weight = image.shape[1]
    channels = image.shape[2]
    print("weight : %s, height : %s, channel : %s" % (weight, height, channels))

    index = 0
    for col in range(weight - ori_image.shape[0]):  # 遍历宽
        for row in range(height - ori_image.shape[1]):  # 遍历高
            tpl_image = image[row:row + 25, col:col + 28]
            tpl_image = cv.cvtColor(tpl_image, cv.COLOR_BGR2GRAY)
            # 计算相似度矩阵
            res = cv.matchTemplate(tpl_image, ori_image, cv.TM_CCOEFF_NORMED)
            # 找到最大匹配
            minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(res)

            if minVal >= 0.8:
            #     cv.imshow("temp", tpl_image)
            #     cv.waitKey(0)
                print(row, col)
                move_to(col, row)
                cv.imwrite("./tes/res{0}_{1}.jpg".format(index, minVal), tpl_image)
                cv.drawMarker(res, (row, col), (255, 255, 255), cv.MARKER_STAR)
                return image
            index += 1
    return image

if __name__ == "__main__":
    time.sleep(3)
    while True:
        get_contours()