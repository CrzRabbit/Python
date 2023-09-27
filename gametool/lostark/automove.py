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

#查找相似度最小值
min_val = 0.8
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_green = (0, 255, 0)

me = 18

#获取屏幕的长宽
screen_width, screen_height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
print("屏幕宽：{0:4d} 屏幕高：{1:4d}".format(screen_width, screen_height))

#计算截屏范围
len = 360
mini_map = (screen_width - 410, 40, screen_width - 410 + len, 40 + len)

# 读取图标图片
ori_image = cv.imread("ori.jpg")
# 将图片转换为灰度图像
ori_image = cv.cvtColor(ori_image, cv.COLOR_BGR2GRAY)
ori_width, ori_height = ori_image.shape[1], ori_image.shape[0]
print("图标宽：{0:4d} 图标高：{1:4d}".format(ori_width, ori_height))

steps = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
pre_dirs = [7, 6, 5, 4, 3, 2, 1, 0]

def getDel():
    return random.random() / 100 + 0.3

def press(key, interval=0.1):
    time.sleep(getDel())
    kb.press(key)
    time.sleep(interval)
    kb.release(key)
    time.sleep(getDel())

def move(x, y):
    win32api.SetCursorPos((screen_width // 2 + ((x - len // 2) * 10), screen_height // 2 + ((y - len // 10) * 2)))
    ms.press(Button.right)
    ms.release(Button.right)
    time.sleep(1)

def get_contours():
    image = ImageGrab.grab(bbox=mini_map)

    image = array(image.getdata(), uint8).reshape(image.size[1], image.size[0], 3)
    #缩放
    # image = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

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
    draw_img = cv.drawContours(draw_img, contours, -1, (0, 0, 255), 3)

    #绘制当前位置
    # cv.drawMarker(res, pos, (255, 255, 255), cv.MARKER_STAR)

    draw_img = find_origin(draw_img)
    cv.imwrite("res.jpg", draw_img)
    return contours

def get_path(image, x, y, w, h, pre_dir):
    print(x, y, w, h)
    found = False
    for i in range(y - me, y + me + 1):
        for j in range(x - me, x + me + 1):
                 image[i, j] = color_green
    image[y, x] = color_black
    cv.imwrite("res.jpg", image)
    # 0 1 2
    # 3   4
    # 5 6 7
    if x < w:
        if y < h:
            direc = [7, 6, 4, 5, 2, 3, 1, 0]
        elif y > h:
            direc = [2, 1, 4, 0, 7, 3, 6, 5]
        else:
            direc = [4, 2, 7, 1, 6, 0, 5, 3]
    elif x > w:
        if y < h:
            direc = [5, 6, 3, 7, 0, 4, 1, 2]
        elif y > h:
            direc = [0, 1, 3, 2, 5, 4, 6, 7]
        else:
            direc = [3, 0, 5, 1, 6, 2, 7, 4]
    else:
        if y < h:
            direc = [6, 5, 7, 3, 4, 0, 2, 1]
        elif y > h:
            direc = [1, 2, 0, 4, 3, 7, 5, 6]
        else:
            return image, True
    for dir in direc:
        step = steps[dir]
        tx = x + step[0]
        ty = y + step[1]
        # if pre_dir != 8 and dir == pre_dirs[pre_dir]:
        #     return image, False
        ok = False
        for i in range(ty - me, ty + me + 1):
            for j in range(tx - me, tx + me + 1):
                b, g, r = image[i, j]
                if (abs(j - x) > me or abs(i - y) > me) and ((r, g, b) != color_green and (r, g, b) != color_red):
                    ok = True
        if ok:
            for i in range(ty - me, ty + me + 1):
                if ok:
                    for j in range(tx - me, tx + me + 1):
                        b, g, r = image[i, j]
                        if (abs(j - x) > me or abs(i - y) > me) and ((r, g, b) == color_red or b > 200):
                            ok = False
                            break
                else:
                    break
        if ok and (pre_dir == 8 or dir != pre_dirs[pre_dir]):
            image, found = get_path(image, tx, ty, w, h, dir)
        if found:
            break
    return image, found

def find_origin(image):
    # shape内包含三个元素：按顺序为高、宽、通道数
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("截屏宽：{0:4d} 截屏高：{1:4d}".format(width, height))

    index = 0
    h = 0
    while h < height - ori_height:
        w = 0
        while w < width - ori_width:
            #获取图标大小区域
            tmp_image = image[h: h + ori_height, w: w + ori_width]
            # cv.imshow("temp", tmp_image)
            # cv.waitKey(0)
            #转化为灰度图像
            tmp_image = cv.cvtColor(tmp_image, cv.COLOR_BGR2GRAY)
            # 计算相似度矩阵
            res = cv.matchTemplate(tmp_image, ori_image, cv.TM_CCOEFF_NORMED)
            # 找到最大匹配
            minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(res)

            # cv.imwrite("./test/res{0}_{1}.jpg".format(index, minVal), tmp_image)
            index += 1
            # print(index, minVal, maxVal, minLoc, maxLoc)

            if minVal >= min_val:
                cv.imwrite("./test/res{0}_{1}.jpg".format(index, minVal), tmp_image)
                index += 1

                image, found = get_path(image, len // 2 - 6, len // 2 + 5, w, h, 8)
                print("位置X：{0:4d} 位置Y：{1:4d} 结果：{2}".format(w, h, found))
                # cv.imshow("temp", tmp_image)
                # cv.waitKey(0)
                return image
            w += 2
        h += 2
    return image

if __name__ == "__main__":
    time.sleep(3)
    get_contours()