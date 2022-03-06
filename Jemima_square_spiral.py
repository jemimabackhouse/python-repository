# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen()
t.pencolor('lime')
c = 1
for x in range(100):
    if c == 1:
        t.pencolor('orange')
        c = 0
    else:
        t.pencolor('lime')
        c = 1
    t.forward(x)
    t.left(90)
