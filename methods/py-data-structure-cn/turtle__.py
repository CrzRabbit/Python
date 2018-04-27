import turtle

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
        draw_tree(t, len - 10)
        t.left(20)
        draw_tree(t, len - 10)
        t.right(10)
        t.backward(len)

if __name__ == '__main__':
    # draw_len(t, 100)
    t.left(90)
    draw_tree(t, 100)
    myWin.exitonclick()