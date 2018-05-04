import turtle
import numpy as np

t = turtle.Turtle()
myWin = turtle.Screen()

def draw_len(t, len):
    if len > 0:
        t.forward(len)
        t.right(90)
        draw_len(t, len - 5)

def draw_tree(t, len):
    if len > 0:
        t.forward(len)
        t.right(10)
        draw_tree(t, len - 20)
        t.left(20)
        draw_tree(t, len - 20)
        t.right(10)
        t.backward(len)

def draw_sector(t, angel, height):
    c = height * 2 * np.pi
    step = c * (angel / 100 / 360)
    t.forward(height)
    t.right(90)
    temp = angel / 100
    for i in range(100):
        t.right(temp)
        t.forward(step)
    t.right(90)
    t.forward(height)

if __name__ == '__main__':
    # draw_len(t, 100)
    t.left(90)
    t.color('red', 'green')
    # draw_tree(t, 100)
    draw_sector(t, 45 , 300)
    myWin.exitonclick()