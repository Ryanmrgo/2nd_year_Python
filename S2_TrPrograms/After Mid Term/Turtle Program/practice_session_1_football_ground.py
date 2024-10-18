import turtle
screen = turtle.Screen()
screen.bgcolor("green")  
# Create the turtle (MessiJ)
messiJ = turtle.Turtle()
messiJ.shape("turtle")
messiJ.color("blue")
messiJ.pensize(3)
# Draw the football ground
messiJ.penup()
messiJ.goto(-150,-150) 
messiJ.pendown()
# Draw the outer perimeter of the football ground
for _ in range(4):
    messiJ.forward(300)
    messiJ.left(90)
# Draw the inner square
messiJ.penup()
messiJ.goto(-120, -120)  
messiJ.pendown()

messiJ.color("orange")  
messiJ.pensize(2)     

for _ in range(4):
    messiJ.forward(240)
    messiJ.left(90)

# Hide the turtle
messiJ.hideturtle()
turtle.done()
