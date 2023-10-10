from pynput import mouse
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput.keyboard import Listener
from pynput import keyboard
import threading
import time

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

dx, dy = 0, 0
cx, cy = 1280, 707
record = open('1.txt', 'w+')
record.write('3 mouse 0 {0} {1} \n'.format(cx, cy))
record.write('0 mouse 1 {0} {1} Button.right True \n'.format(cx, cy))
record.write('0 mouse 1 {0} {1} Button.right False \n'.format(cx, cy))

'''
mouse 0 699 920 1696682946758741300
mouse 0 703 920 1696682946764724700
mouse 0 706 920 1696682946770709900

mouse 0 899 847 1696682946804618600
mouse 0 934 836 1696682946810601600
mouse 0 972 822 1696682946815622100
'''
pre_time = time.time_ns()
time.sleep(2)

def record_event(info):
    global pre_time
    cur_time = time.time_ns()
    dur = (cur_time - pre_time) / (10 ** 9)
    record.write('{0} {1} \n'.format(dur, info))
    pre_time = cur_time

def mouse_move(x, y):
    """
    鼠标移动事件
    :param x: 横坐标
    :param y: 纵坐标
    :return:
    """
    # record_event('mouse 0 {0} {1}'.format(x, y))

def mouse_click(x, y, button, pressed):
    """
    鼠标点击事件
    :param x: 横坐标
    :param y: 纵坐标
    :param button: 按钮枚举对象 Button.left 鼠标左键 Button.right 鼠标右键 Button.middle 鼠标中键
    :param pressed: 按下或者是释放,按下是True释放是False
    :return:
    """
    if pressed and button == Button.right:
        global dx
        global dy
        dx += (x - cx)
        dy += (y - cy)
        print(x, y, dx, dy)
    record_event('mouse 1 {0} {1} {2} {3}'.format(x, y, button, pressed))

def mouse_scroll(x, y, dx, dy):
    """
    鼠标滚动事件
    :param x: 横坐标
    :param y: 纵坐标
    :param dx:滚轮的横坐标方向的移动量,0未移动,1向前面滚动和-1向后面滚动
    :param dy:滚轮的纵坐标方向的移动量,0未移动,1向前面滚动和-1向后面滚动
    :return:
    """
    pass

def listen_mouse():
    # 监听鼠标事件
    with mouse.Listener(
            on_move=mouse_move,  # 鼠标移动事件
            on_click=mouse_click,  # 鼠标点击事件
            on_scroll=mouse_scroll  # 鼠标滚动事件
            ) as mouse_listener:
        mouse_listener.join()

def keyboard_press(key):
    if key == Key.shift:
        mouse_controller.position = (cx - dx, cy - dy)
        mouse_controller.press(Button.right)
        mouse_controller.release(Button.right)
    else:
        record_event('key 0 {0}'.format(key))

def keyboard_release(key):
    record_event('key 1 {0}'.format(key))
    if key == Key.esc:  # 如果按下了ESC键,则结束监听
        return False

def listen_keyboard():
    # 监听键盘事件
    with Listener(on_press=keyboard_press,
                  on_release=keyboard_release) as keyboard_listener:
        keyboard_listener.join()
        record.close()

record_mouse_thread = threading.Thread(target=listen_mouse, args=(), name='record_mouse_thread')
record_keyboard_thread = threading.Thread(target=listen_keyboard, args=(), name='record_keyboard_thread')

record_mouse_thread.start()
record_keyboard_thread.start()

while True:
    time.sleep(100)