import turtle
screen = turtle.Screen()
screen.bgcolor("green")  
messi = turtle.Turtle()
messi.shape("turtle")
messi.color("blue")
messi.pensize(3)
messi.speed(5)  

# Function to draw the football ground
def draw_football_ground():
    messi.penup()
    messi.goto(-150, -150)  
    messi.pendown()
    for _ in range(4):
        messi.forward(300)
        messi.left(90)

# Function to make Messi leave a football stamp
def leave_football_stamp():
    messi.penup()
    messi.goto(0, 0)  
    messi.pendown()
    messi.color("black")  
    messi.shape("circle")  
    messi.stamp()  

draw_football_ground()
leave_football_stamp()
messi.hideturtle()
turtle.done()
