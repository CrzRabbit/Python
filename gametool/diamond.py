import os, time
import random

def auto_get_diamond():
    while True:
        os.system('adb shell input tap 1000 2100')
        os.system('adb shell input swipe 1000 1000 500 200 4000')
        os.system('adb shell input tap 5 1000')
        time.sleep(15)
        #os.system('adb shell input tap 150 1100')
        os.system('adb shell input tap 150 1600')
        time.sleep(32)
        os.system('adb shell input tap 50 50')
        time.sleep(0.2)
        os.system('adb shell input tap 1000 50')
        time.sleep(0.2)
        os.system('adb shell input tap 500 1600')

def auto_get_candy():
    while True:
        time.sleep(15)
        os.system('adb shell input tap 150 750')
        time.sleep(32)
        os.system('adb shell input tap 50 50')
        time.sleep(0.2)
        os.system('adb shell input tap 1000 50')

if __name__ == '__main__':
    auto_get_diamond()
