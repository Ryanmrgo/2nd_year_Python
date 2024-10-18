import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("green")

t.speed(3)

t.begin_fill()
t.fillcolor("blue")
t.goto(-50,0)
for i in range(4):
    t.fd(100)
    t.left(90)

t.end_fill()
t.hideturtle()
