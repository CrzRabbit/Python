from pynput.mouse import Button
from pynput import mouse
from pynput.keyboard import Key
from pynput import keyboard
import time

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

record = open('火炬之光.txt', 'r')
ops = record.readlines()
direc = {'Button.left': Button.left, 'Button.right': Button.right}
while True:
    for line in ops:
        op = line.split(' ')
        if float(op[0]) > 0.001:
            time.sleep(float(op[0]))
        if op[1] == 'mouse':
            if op[2] == '0':
                mouse_controller.position = (int(op[3]), int(op[4]))
            elif op[2] == '1':
                mouse_controller.position = (int(op[3]), int(op[4]))
                if op[6] == 'True':
                    mouse_controller.press(direc[op[5]])
                else:
                    mouse_controller.release(direc[op[5]])
        if op[1] == 'key':
            if op[3] == 'Key.esc':
                print('操作结束')
            if op[2] == '0':
                keyboard_controller.press(op[3][1])
            elif op[2] == '1':
                keyboard_controller.release(op[3][1])