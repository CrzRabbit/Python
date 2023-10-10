from pynput.mouse import Button
from pynput import mouse
from pynput.keyboard import Key
from pynput import keyboard
import time

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

time.sleep(2)
cx, cy = 1280, 707

mouse_controller.position = (1350, 1000)
mouse_controller.press(Button.right)
mouse_controller.release(Button.right)

time.sleep(2)
mouse_controller.position = (cx - (1350 - cx), cy - (1000 - cy))
mouse_controller.press(Button.right)
mouse_controller.release(Button.right)