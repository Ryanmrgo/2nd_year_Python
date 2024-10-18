import turtle
screen=turtle.Screen()
a=turtle.Turtle()
a.penup()
a.goto(-400,250)
a.pendown()

        
a.speed(0)     
a.color("yellow")
a.begin_fill()
a.forward(800)
a.right(90)
a.forward(167)
a.right(90)
a.forward(800)
a.end_fill()
a.left(180)

a.color("green")
a.begin_fill()
a.forward(800)
a.right(90)
a.forward(167)
a.right(90)
a.forward(800)
a.end_fill()
a.left(180)
a.color("red")
a.begin_fill()
a.forward(800)
a.right(90)
a.forward(167)
a.right(90)
a.forward(800)
a.end_fill()

a.color("white")
a.penup()
a.goto(150,30)
a.pendown()
a.fillcolor("white")
a.begin_fill()
for _ in range(5):
    a.forward(300)
    a.left(144)
    
a.end_fill() 
  
a.penup()
a.fd(114)
a.pendown()
a.fillcolor("white")
a.begin_fill()
for _ in range(5):
    a.fd(72)
    a.left(72)

a.end_fill() 


a.hideturtle()
turtle.done()
