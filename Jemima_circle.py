import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(200):
    print(str(x))
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)
