import turtle
a=turtle.Turtle()
a.shape("circle")
a.pensize(3)
a.up()
a.goto(-100,-100)
def square():
    for i in range(4):
        a.forward(210)
        a.left(90)

        
a.color("blue")
bg=turtle.Screen()
bg.bgcolor("lightgreen")
a.down()
a.speed(5)
square()
a.left(45)
a.forward(30)

a.up()

def circle():
    for _ in range(6):
        
        a.fillcolor("yellow")
        a.begin_fill()
        a.circle(2)
        a.stamp()
        a.forward(47.14)
      

circle()
a.hideturtle()


