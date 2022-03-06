#NiceHexSpiral.py
import turtle
colors=['red', 'purple', 'turquoise', 'lime', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('gray')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+5)
    t.forward(x)
    t.left(30)
