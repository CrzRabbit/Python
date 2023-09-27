import os, time, random
import pyttsx3
from playsound import playsound

def play_hint_sound(info):
    try:
        voice = pyttsx3.init()
        if info is None:
            voice.say('')
        else:
            voice.say(info)
    except Exception as e:
        voice.say('play hint sound error')
    finally:
        voice.runAndWait()

def auto_merge():
    ret = 0
    try:
        for i in range(0, 50):
            ret = os.system('adb shell input swipe {0} {1} 540 1400 200'.format(random.randint(400, 600), random.randint(1200, 1600)))
        # if ret == 1:
        #     play_hint_sound('operation error, check mobile phone please')
    except Exception as e:
        print('error')

def watch_ads():
    # os.system('adb shell input tap 1000 2100')
    # os.system('adb shell input tap 1000 950')
    # time.sleep(35)
    # os.system('adb shell input tap 1000 50')
    # time.sleep(5)
    # os.system('adb shell input tap 200 1900')
    # time.sleep(1)
    # os.system('adb shell input tap 200 1300')
    # time.sleep(10)
    # os.system('adb shell input tap 1000 2200')
    pass

if __name__ == "__main__":
    #watch_ads()
    # while True:
    #     auto_merge()
    #     time.sleep(600)
    while True:
        os.system('adb shell input swipe 800 1170 800 1170 13000')
        os.system('adb shell input swipe 500 1370 500 1135 4000')
        time.sleep(1)