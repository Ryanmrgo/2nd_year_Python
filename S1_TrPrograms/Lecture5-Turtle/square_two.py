import turtle
cynthia=turtle.Turtle()
#cynthia.shape("turtle")
cynthia.color("yellow","green")
cynthia.begin_fill()
for i in range(5):
    cynthia.forward(130)
    cynthia.left(90)
cynthia.end_fill()

cynthia.penup()
cynthia.forward(130)
cynthia.pendown()
cynthia.color("red","blue")
cynthia.begin_fill()
for i in range(5):
    cynthia.forward(130)
    cynthia.left(90)
cynthia.end_fill()

#turtle.done()
